from hello_world.hello_world import hello_world, functools_reduce_test, VehicleTripStats


def test_hello_world():
    name = "John"
    assert f"Hello World {name}" == hello_world(name)


def test_functools_reduce():
    input_list = [
        VehicleTripStats(1, 2),
        VehicleTripStats(10, 20),
        VehicleTripStats(10, 200),
    ]
    assert functools_reduce_test(input_list) == VehicleTripStats(21, 222)
