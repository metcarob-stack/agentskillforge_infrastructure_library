from agentskillforge_infrastructure_library import (
    validate_agent_id
)
import pytest


def test_validate_agent_id():
    with pytest.raises(ValueError):
        validate_agent_id("a")
    with pytest.raises(ValueError):
        validate_agent_id("s-aaa")
    with pytest.raises(ValueError):
        validate_agent_id("x-aaa")
    with pytest.raises(ValueError):
        validate_agent_id("mee_too")
    with pytest.raises(ValueError):
        validate_agent_id("meE_too")
    validate_agent_id("mee-too123-555")
