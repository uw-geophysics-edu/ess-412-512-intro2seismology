#!/usr/bin/env python3
"""Final comprehensive check of refactoring status."""
import json
from pathlib import Path

notebooks = sorted(Path("notebooks").glob("*.ipynb")) + sorted(Path("homework").glob("*.ipynb"))

print("\n" + "="*80)
print("FINAL COMPREHENSIVE REFACTORING STATUS CHECK")
print("="*80 + "\n")

stats = {
    'total': len(notebooks),
    'refactored': 0,
    'with_problem_parts': 0,
    'unchanged': 0,
    'still_needs_work': []
}

for nb_path in notebooks:
    with open(nb_path) as f:
        nb = json.load(f)

    has_old_format = False
    has_problem_parts = False

    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell.get('source', []))

            # Old format check (Part X — or Part X:)
            if ('## Part ' in source or '# Part ') and '## Part (' not in source and '# Part (' not in source:
                has_old_format = True

            # Problem parts check (Part (a), Part (b), etc.)
            if 'Part (' in source:
                has_problem_parts = True

    if has_old_format:
        stats['still_needs_work'].append(nb_path.name)
    elif has_problem_parts:
        stats['with_problem_parts'] += 1
    else:
        stats['refactored'] += 1

print(f"Total notebooks processed: {stats['total']}")
print(f"✓ Fully refactored (no 'Part X' headings): {stats['refactored']}")
print(f"✓ With problem/assignment parts (Part (a), (b)): {stats['with_problem_parts']}")

if stats['still_needs_work']:
    print(f"\n⚠️ Still needs refactoring: {len(stats['still_needs_work'])}")
    for nb in stats['still_needs_work']:
        print(f"   - {nb}")
else:
    print(f"\n✅ ALL NOTEBOOKS SUCCESSFULLY REFACTORED!")

print("\n" + "="*80)
