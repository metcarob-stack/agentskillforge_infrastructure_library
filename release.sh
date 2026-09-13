#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

uv run --with pytest pytest

uv version --bump patch
VERSION=$(uv version --short)
uv lock

sed -i "s/^__version__ = .*/__version__ = \"${VERSION}\"/" \
  src/agentskillforge_infrastructure_library/__init__.py

uv build

git add .
git commit -m "release: v${VERSION}"
git push origin main

git tag -a v${VERSION} -m "Release v${VERSION}"
git push origin v${VERSION}

gh release create v${VERSION} \
--title "v${VERSION}" \
--notes "Describe the changes in this release." \
--verify-tag

exit 0