# Agent Skill Forge Infrastructure Library

The shared Python infrastructure library for Agent Skill Forge projects.

This `0.0.2` release contains a small customer information lookup API:

```python
from agentskillforge_infrastructure_library import get_customer_info

print(get_customer_info("ax56"))
# {'customer_id': 'ax56', 'name': 'My First Cust'}
```

The current customer data is intentionally limited to non-sensitive, hard-coded identifiers and names. Unknown customer IDs raise `KeyError`.

## Development

Run the tests with:

```bash
uv run --with pytest pytest
```

Build the distribution with:

```bash
uv build
```
