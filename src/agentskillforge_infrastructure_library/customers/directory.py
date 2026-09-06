"""Customer information lookup functions."""

from .models import CustomerInfo
from .static_data import CUSTOMERS


def get_customer_info(customer_id: str) -> CustomerInfo:
    """Return customer information for a known customer ID.

    A new dictionary is returned for every call so callers cannot mutate the
    library's internal static registry.

    Raises:
        KeyError: If ``customer_id`` is not known.
    """
    try:
        customer = CUSTOMERS[customer_id]
    except KeyError as exc:
        raise KeyError(f"Unknown customer_id: {customer_id}") from exc

    return {
        "customer_id": customer["customer_id"],
        "name": customer["name"],
    }
