class BusStop:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_coordinates(self):
        return (self.lat, self.lon)


class BusRoute:
    def __init__(self, name, color="blue"):
        self.name = name
        self.color = color
        self.stops = []

    def add_stop(self, stop: BusStop):
        self.stops.append(stop)

    def get_coordinates(self):
        return [stop.get_coordinates() for stop in self.stops]
