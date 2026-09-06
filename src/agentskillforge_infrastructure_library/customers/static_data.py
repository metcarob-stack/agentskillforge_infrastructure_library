"""Temporary static customer information.

This data is intentionally limited to non-sensitive identifiers and names.
"""

from .models import CustomerInfo


CUSTOMERS: dict[str, CustomerInfo] = {
    "ax56": {
        "customer_id": "ax56",
        "name": "My First Cust",
    },
    "sys": {
        "customer_id": "sys",
        "name": "Agent Skill Forge",
    },
}
