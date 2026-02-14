#!/usr/bin/env python3
"""Comprehensive analysis of section heading patterns across all notebooks."""
import json
import re
from pathlib import Path

notebooks = sorted(Path("notebooks").glob("*.ipynb")) + sorted(Path("homework").glob("*.ipynb"))

print("\n" + "="*80)
print("SECTION HEADING ANALYSIS")
print("="*80)

for nb_path in notebooks:
    with open(nb_path) as f:
        nb = json.load(f)

    found_patterns = {}

    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell.get('source', []))

            # Find "Part" patterns (not problem parts like "Part (a)")
            # Match: "Part I", "Part II", "Part A", "Part 1"
            if 'Part (' in source:
                found_patterns['has_problem_parts'] = True

            # Match "**Part X:" or "## Part X:"
            for match in re.finditer(r'(?:^#+|^\*\*)\s+Part\s+([A-Z0-9IVivx]+)', source, re.MULTILINE):
                part = match.group(1)
                if part not in found_patterns:
                    found_patterns[part] = 0
                found_patterns[part] += 1

    if found_patterns:
        print(f"\n{nb_path.name}:")
        for pattern, count in sorted(found_patterns.items()):
            print(f"  {pattern}: {count}")
