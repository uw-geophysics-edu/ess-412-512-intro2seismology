#!/usr/bin/env python3
import json
from pathlib import Path

notebooks = sorted(Path("/Users/marinedenolle/GitHub/ess-412-512-intro2seismology/notebooks").glob("*.ipynb"))
notebooks += sorted(Path("/Users/marinedenolle/GitHub/ess-412-512-intro2seismology/homework").glob("*.ipynb"))

print("\n=== SECTION HEADING PATTERNS FOUND ===\n")

for nb_path in notebooks[:5]:  # Check first 5 notebooks
    print(f"\n{nb_path.name}:")
    with open(nb_path) as f:
        nb = json.load(f)

    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            source = cell.get('source', [])
            source_str = ''.join(source) if isinstance(source, list) else source

            # Look for section headers
            for line in source_str.split('\n'):
                if '##' in line and (line.startswith('#')):
                    print(f"  Cell {i+1}: {line[:80]}")
                elif '**Part' in line:
                    print(f"  Cell {i+1}: {line[:80]}")
