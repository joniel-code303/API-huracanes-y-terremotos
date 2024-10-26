class Hurricane:
    def __init__(self, name, category, wind_speed, pressure, location):
        self.name = name
        self.category = category
        self.wind_speed = wind_speed
        self.pressure = pressure
        self.location = location

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "wind_speed": self.wind_speed,
            "pressure": self.pressure,
            "location": self.location
        }

class Earthquake:
    def __init__(self, magnitude, location, depth):
        self.magnitude = magnitude
        self.location = location
        self.depth = depth

    def to_dict(self):
        return {
            "magnitude": self.magnitude,
            "location": self.location,
            "depth": self.depth
        }
