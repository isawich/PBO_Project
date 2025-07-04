from math import radians, sin, cos, sqrt, atan2

def hitung_jarak_km(lat1, lon1, lat2, lon2):
    R = 6371  # radius bumi dalam km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
