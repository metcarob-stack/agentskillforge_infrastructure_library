# Agent Skill Forge Infrastructure Library

The shared Python infrastructure library for Agent Skill Forge projects.

This `0.0.3` release contains customer information and platform/server naming APIs:

```python
from agentskillforge_infrastructure_library import (
    get_customer_info,
    get_server_dns_name,
)

print(get_customer_info("ax56"))
# {'customer_id': 'ax56', 'name': 'My First Cust'}
print(get_server_dns_name("ab12cd", "x7z"))
# s-x7z.a-ab12cd.agentskillforge.com
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
