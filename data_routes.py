from models import BusRoute, BusStop

def get_routes():
    routes = {}

    r1 = BusRoute("Penggaron - Banyumanik", color="blue")
    r1.add_stop(BusStop("Terminal Penggaron", -7.0003, 110.4707))
    r1.add_stop(BusStop("Simpang Lima", -6.9929, 110.4200))
    r1.add_stop(BusStop("Banyumanik", -7.0563, 110.4179))
    routes[r1.name] = r1

    r2 = BusRoute("Undip - UNNES", color="green")
    r2.add_stop(BusStop("Undip Tembalang", -7.0500, 110.4381))
    r2.add_stop(BusStop("Simpang Lima", -6.9929, 110.4200))
    r2.add_stop(BusStop("UNNES Sekaran", -7.0505, 110.3538))
    routes[r2.name] = r2

    r3 = BusRoute("Mangkang - Stasiun Tawang", color="red")
    r3.add_stop(BusStop("Terminal Mangkang", -6.9485, 110.3148))
    r3.add_stop(BusStop("Tugu Muda", -6.9858, 110.4060))
    r3.add_stop(BusStop("Stasiun Tawang", -6.9667, 110.4288))
    routes[r3.name] = r3

    r4 = BusRoute("Pelabuhan - Bandara", color="orange")
    r4.add_stop(BusStop("Pelabuhan Tanjung Emas", -6.9500, 110.4200))
    r4.add_stop(BusStop("Johar", -6.9744, 110.4288))
    r4.add_stop(BusStop("Bandara Ahmad Yani", -6.9726, 110.3751))
    routes[r4.name] = r4

    r5 = BusRoute("Sampangan - Peterongan", color="purple")
    r5.add_stop(BusStop("Sampangan", -7.0067, 110.3811))
    r5.add_stop(BusStop("Kota Lama", -6.9706, 110.4307))
    r5.add_stop(BusStop("Peterongan", -7.0146, 110.4533))
    routes[r5.name] = r5

    return routes
