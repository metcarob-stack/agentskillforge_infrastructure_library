from agentskillforge_infrastructure_library import __version__, get_customer_info, hello_world


def test_version():
    assert __version__ == "0.0.2"


def test_hello_world():
    assert hello_world() == "Hello, world!"


def test_get_known_customer_info():
    assert get_customer_info("ax56") == {
        "customer_id": "ax56",
        "name": "My First Cust",
    }
    assert get_customer_info("sys") == {
        "customer_id": "sys",
        "name": "Agent Skill Forge",
    }


def test_get_customer_info_returns_independent_result():
    result = get_customer_info("ax56")
    result["name"] = "Changed locally"
    assert get_customer_info("ax56")["name"] == "My First Cust"


def test_unknown_customer_id_raises_key_error():
    try:
        get_customer_info("unknown")
    except KeyError as exc:
        assert str(exc) == "'Unknown customer_id: unknown'"
    else:
        raise AssertionError("Expected get_customer_info to raise KeyError")
