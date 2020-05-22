from dataclasses import dataclass

from shapely.geometry import Point


@dataclass
class Location:
    lat: float
    lng: float

    def __init__(self, lat: float, lng: float):
        assert -90 <= lat <= 90
        assert -180 <= lng <= 180
        self.lat = lat
        self.lng = lng

    def __eq__(self, o: object) -> bool:
        return (self.lat, self.lng) == (o.lat, o.lng)

    def __hash__(self) -> int:
        return hash((self.lat, self.lng))

    def as_point(self):
        return Point(self.lng, self.lat)
