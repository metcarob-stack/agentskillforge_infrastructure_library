# Agent Skill Forge Infrastructure Library

The shared Python infrastructure library for Agent Skill Forge projects.

This initial `0.0.1` release intentionally contains only a small demonstration function:

```python
from agentskillforge_infrastructure_library import hello_world

print(hello_world())
# Hello, world!
```

## Development

Run the tests with:

```bash
uv run --with pytest pytest
```

Build the distribution with:

```bash
uv build
```
