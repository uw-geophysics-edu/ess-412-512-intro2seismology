#!/usr/bin/env python3
"""Add unique cell IDs to every Jupyter notebook cell that is missing one.

Usage (from the repository root):

    python tools/add_cell_ids_to_notebooks.py

The script walks the repository recursively, finds all .ipynb files
(skipping hidden directories, _build, and node_modules), and assigns a
uuid4-based ``id`` to every cell that lacks one.  Modified files are
overwritten in place and listed on stdout.
"""

import json
import uuid
from pathlib import Path

SKIP_DIRS = {".git", ".ipynb_checkpoints", "_build", "node_modules", "__pycache__", ".pixi"}

REPO_ROOT = Path(__file__).resolve().parent.parent


def needs_ids(nb: dict) -> bool:
    """Return True if any cell is missing an 'id' field."""
    for cell in nb.get("cells", []):
        if "id" not in cell:
            return True
    return False


def add_ids(nb: dict) -> int:
    """Add a uuid4 id to every cell missing one. Return count of cells fixed."""
    count = 0
    for cell in nb.get("cells", []):
        if "id" not in cell:
            cell["id"] = str(uuid.uuid4())[:8]
            count += 1
    return count


def iter_notebooks(root: Path):
    """Yield all .ipynb paths under *root*, skipping SKIP_DIRS."""
    for path in sorted(root.rglob("*.ipynb")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def main():
    modified = []
    for path in iter_notebooks(REPO_ROOT):
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        if not needs_ids(nb):
            continue

        count = add_ids(nb)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")

        modified.append((path.relative_to(REPO_ROOT), count))

    if modified:
        print(f"Modified {len(modified)} notebook(s):\n")
        for rel, count in modified:
            print(f"  {rel}  ({count} cell(s) patched)")
    else:
        print("All notebooks already have cell IDs — nothing to do.")


if __name__ == "__main__":
    main()
