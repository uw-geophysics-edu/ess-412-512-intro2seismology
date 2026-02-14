#!/usr/bin/env python3
"""
Comprehensive notebook refactoring across ALL 15 notebooks.
Updates section headings from 'Part X' to 'X.' format.
"""
import json
import re
from pathlib import Path

def refactor_notebook(nb_path):
    """
    Refactor a single notebook:
    1. Rename "Part X" section headings to "X." format
    2. Handle special cases (Roman numerals, letters)
    3. Skip problem parts like "Part (a)"
    """
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    changed = False
    nb_name = nb_path.name
    changes_made = []

    for cell in nb['cells']:
        if cell['cell_type'] in ['markdown', 'code']:
            source = cell.get('source', [])
            if isinstance(source, list):
                for i, line in enumerate(source):
                    original = line

                    # Pattern 1: "# Part 1 —" → "# 1. " (for numeric parts)
                    line = re.sub(
                        r'^(#+)\s+Part\s+(\d+)\s+—\s+(.+)$',
                        r'\1 \2. \3',
                        line
                    )

                    # Pattern 2: "# Part A —" → "# A. " (for letter parts)
                    line = re.sub(
                        r'^(#+)\s+Part\s+([A-Z])\s+—\s+(.+)$',
                        r'\1 \2. \3',
                        line
                    )

                    # Pattern 3: "## Part [1/2/3]:" → "## [1/2/3]." (template lines)
                    line = re.sub(
                        r'^(#+)\s+Part\s+\[([^\]]+)\]:\s+(.+)$',
                        r'\1 [\2]. \3',
                        line
                    )

                    # Pattern 4: "**Part II**" → "**II.**" (inline bold, roman numerals)
                    line = re.sub(
                        r'\*\*Part\s+([IVivx]+)\*\*',
                        r'**\1.**',
                        line
                    )

                    # Pattern 5: "Part II" → "II." (inline, no bold)
                    line = re.sub(
                        r'(?<!\*)\bPart\s+(II|III|IV|I)(?!\*)',
                        r'\1.',
                        line
                    )

                    if line != original:
                        source[i] = line
                        changed = True
                        changes_made.append(f"    ✓ {original.strip()[:60]} → {line.strip()[:60]}")

    if changed:
        with open(nb_path, 'w') as f:
            json.dump(nb, f, indent=4)
        return True, changes_made

    return False, []

def main():
    repo_root = Path('.')
    notebooks = sorted(repo_root.glob('notebooks/*.ipynb')) + sorted(repo_root.glob('homework/*.ipynb'))

    print("\n" + "="*80)
    print("COMPREHENSIVE NOTEBOOK REFACTORING")
    print("="*80)
    print("\nRefactoring ALL section headings: 'Part X' → 'X.' format\n")

    total_changed = 0

    for nb_path in notebooks:
        changed, changes = refactor_notebook(nb_path)

        if changed:
            total_changed += 1
            print(f"✓ {nb_path.name}")
            for change in changes:
                print(change)
        else:
            print(f"  (no changes needed in {nb_path.name})")

    print("\n" + "="*80)
    print(f"REFACTORING COMPLETE")
    print(f"Updated {total_changed} out of {len(notebooks)} notebooks")
    print("="*80)

if __name__ == '__main__':
    main()
