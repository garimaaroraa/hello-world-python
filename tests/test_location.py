from shapely.geometry import Point

from hello_world.location import Location


def test_location_as_point():
    location = Location(10, 20)
    assert location.as_point() == Point(20, 10)
