import streamlit as st
import folium
from folium import Icon, PolyLine
from streamlit_folium import st_folium

from data_routes import get_routes
from helpers import hitung_jarak_km

JAM_OPERASIONAL = "05.30 - 17.00"

st.set_page_config(page_title="Jalur Bus Trans Semarang", layout="wide")
st.title("🚌 Sistem Petunjuk Jalur Bus Trans Semarang")

opsi_tampilan = st.radio("Pilih tampilan rute:", ["Semua Rute", "Satu Rute"])
rute_dict = get_routes()
peta = folium.Map(location=[-6.9840, 110.4200], zoom_start=13)

if opsi_tampilan == "Semua Rute":
    st.subheader("🗺️ Semua Koridor Bus")
    st.caption(f"🕓 Jam operasional seluruh rute: **{JAM_OPERASIONAL}**")

    for nama, route in rute_dict.items():
        coords = route.get_coordinates()
        PolyLine(coords, color=route.color, weight=5, tooltip=route.name).add_to(peta)

        for stop in route.stops:
            folium.Marker(
                location=stop.get_coordinates(),
                tooltip=stop.name,
                popup=f"<b>{stop.name}</b><br>{route.name}<br>🕓 {JAM_OPERASIONAL}",
                icon=Icon(icon="bus", prefix="fa", color="darkblue")
            ).add_to(peta)

else:
    pilihan = st.selectbox("Pilih rute:", list(rute_dict.keys()))
    route = rute_dict[pilihan]
    coords = route.get_coordinates()

    st.subheader(f"🧭 Rute: {route.name}")
    st.caption(f"🕓 Jam operasional: **{JAM_OPERASIONAL}**")

    PolyLine(coords, color=route.color, weight=6, tooltip=route.name).add_to(peta)

    # Halte awal
    folium.Marker(
        location=route.stops[0].get_coordinates(),
        tooltip="Halte Pemberangkatan",
        popup=f"<b>{route.stops[0].name}</b><br>🟢 Pemberangkatan<br>🕓 {JAM_OPERASIONAL}",
        icon=Icon(icon="play", prefix="fa", color="green")
    ).add_to(peta)

    # Halte akhir
    folium.Marker(
        location=route.stops[-1].get_coordinates(),
        tooltip="Halte Tujuan",
        popup=f"<b>{route.stops[-1].name}</b><br>🔴 Tujuan Akhir<br>🕓 {JAM_OPERASIONAL}",
        icon=Icon(icon="flag-checkered", prefix="fa", color="red")
    ).add_to(peta)

    # Halte tengah
    for stop in route.stops[1:-1]:
        folium.Marker(
            location=stop.get_coordinates(),
            tooltip=stop.name,
            popup=f"{stop.name}<br>{route.name}<br>🕓 {JAM_OPERASIONAL}",
            icon=Icon(icon="bus", prefix="fa", color="gray")
        ).add_to(peta)

    # Jarak antar halte
    st.subheader("📏 Estimasi Jarak Antar Halte:")
    total_jarak = 0
    for i in range(len(route.stops) - 1):
        s1 = route.stops[i]
        s2 = route.stops[i+1]
        jarak = hitung_jarak_km(s1.lat, s1.lon, s2.lat, s2.lon)
        st.markdown(f"- **{s1.name} ➜ {s2.name}**: `{jarak:.2f} km`")
        total_jarak += jarak

    st.success(f"🔁 Total estimasi jarak: **{total_jarak:.2f} km**")

st_folium(peta, width=900, height=600)
