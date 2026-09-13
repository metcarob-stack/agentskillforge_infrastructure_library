from agentskillforge_infrastructure_library import (
    __version__,
    generate_platform_id,
    generate_server_id,
    get_customer_info,
    get_platform_dns_name,
    get_server_dns_name,
    get_server_hostname,
    hello_world,
)

def test_platform_naming_conventions():
    platform_id = generate_platform_id()
    assert len(platform_id) == 6
    assert platform_id.isalnum()
    assert platform_id.islower()
    assert generate_server_id("ab12cd") and len(generate_server_id("ab12cd")) == 3
    assert get_server_hostname("ab12cd", "x7z") == "x7z-ab12cd"
    assert get_server_dns_name("ab12cd", "x7z") == "s-x7z.a-ab12cd.agentskillforge.com"
    assert get_platform_dns_name("ab12cd") == "*.ab12cd.agentskillforge.com"


def test_platform_naming_conventions_validate_ids():
    import pytest

    with pytest.raises(ValueError):
        get_server_hostname("ab12cd", "bad-id")
    with pytest.raises(ValueError):
        get_platform_dns_name("bad-id")


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
