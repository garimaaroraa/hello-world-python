from hello_world.hello_world import hello_world


def test_hello_world():
    name = "John"
    assert f"Hello World {name}" == hello_world(name)
