"""Customer information types."""

from typing import TypedDict


class CustomerInfo(TypedDict):
    """Public customer information returned by the library."""

    customer_id: str
    name: str
