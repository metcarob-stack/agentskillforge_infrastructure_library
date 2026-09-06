"""Shared infrastructure library for Agent Skill Forge."""

from .customers import CustomerInfo, get_customer_info

__version__ = "0.0.2"


def hello_world() -> str:
    """Return the library's initial greeting."""
    return "Hello, world!"


__all__ = ["CustomerInfo", "__version__", "get_customer_info", "hello_world"]
