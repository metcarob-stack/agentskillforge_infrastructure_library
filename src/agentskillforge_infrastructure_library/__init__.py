"""Shared infrastructure library for Agent Skill Forge."""

from .customers import CustomerInfo, get_customer_info
from .platform_naming_conventions import (
    generate_platform_id,
    generate_server_id,
    get_platform_dns_name,
    get_server_dns_name,
    get_server_hostname,
    validate_customer_id,
    validate_platform_id
)

__version__ = "0.0.8"


def hello_world() -> str:
    """Return the library's initial greeting."""
    return "Hello, world!"


__all__ = [
    "CustomerInfo",
    "__version__",
    "generate_platform_id",
    "generate_server_id",
    "get_customer_info",
    "get_platform_dns_name",
    "get_server_dns_name",
    "get_server_hostname",
    "hello_world",
]
