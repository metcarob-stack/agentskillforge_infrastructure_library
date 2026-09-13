"""Naming conventions for Agent Skill Forge platforms and servers."""

import re
import secrets


_PLATFORM_ID_LENGTH = 6
_SERVER_ID_LENGTH = 3
_ALLOWED_CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789"
_PLATFORM_ID_PATTERN = re.compile(r"^[a-z0-9]{6}$")
_SERVER_ID_PATTERN = re.compile(r"^[a-z0-9]{3}$")
_CUSTOMER_ID_PATTERN = re.compile(r"^[a-z0-9]{3,10}$")

def _validate_customer_id(customer_id: str) -> None:
    if customer_id is None:
        raise ValueError("customer_id must not be None")
    if not isinstance(customer_id, str) or not _CUSTOMER_ID_PATTERN.fullmatch(customer_id):
        raise ValueError("customer_id must contain between 3 and 10 lowercase letters or digits")


def _validate_platform_id(platform_id: str) -> None:
    if not isinstance(platform_id, str) or not _PLATFORM_ID_PATTERN.fullmatch(platform_id):
        raise ValueError("platform_id must contain exactly 6 lowercase letters or digits")


def _validate_server_id(server_id: str) -> None:
    if not isinstance(server_id, str) or not _SERVER_ID_PATTERN.fullmatch(server_id):
        raise ValueError("server_id must contain exactly 3 lowercase letters or digits")


def generate_platform_id() -> str:
    """Generate a six-character lowercase alphanumeric platform ID."""
    return "".join(
        secrets.choice(_ALLOWED_CHARACTERS) for _ in range(_PLATFORM_ID_LENGTH)
    )


def generate_server_id(platform_id: str) -> str:
    """Generate a three-character server ID for a valid platform ID.

    The caller is responsible for checking the generated ID against the
    platform's existing server registry and retrying on collision.
    """
    _validate_platform_id(platform_id)
    return "".join(
        secrets.choice(_ALLOWED_CHARACTERS) for _ in range(_SERVER_ID_LENGTH)
    )


def get_server_hostname(platform_id: str, server_id: str) -> str:
    """Return the internal hostname in the form ``{server_id}-{platform_id}``."""
    _validate_platform_id(platform_id)
    _validate_server_id(server_id)
    return f"{server_id}-{platform_id}"


def get_server_dns_name(platform_id: str, server_id: str) -> str:
    """Return the direct administrative DNS name for a server."""
    _validate_platform_id(platform_id)
    _validate_server_id(server_id)
    return f"s-{server_id}.a-{platform_id}.agentskillforge.com"


def get_platform_dns_name(platform_id: str) -> str:
    """Return the wildcard service DNS name for a platform."""
    _validate_platform_id(platform_id)
    return f"*.{platform_id}.agentskillforge.com"


__all__ = [
    "generate_platform_id",
    "generate_server_id",
    "get_platform_dns_name",
    "get_server_dns_name",
    "get_server_hostname",
]
