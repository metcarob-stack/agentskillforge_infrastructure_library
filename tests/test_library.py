from agentskillforge_infrastructure_library import __version__, hello_world


def test_version():
    assert __version__ == "0.0.1"


def test_hello_world():
    assert hello_world() == "Hello, world!"
