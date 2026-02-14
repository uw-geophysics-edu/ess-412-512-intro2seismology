#!/usr/bin/env python3
import json
from pathlib import Path

def extract_sources_from_notebook(notebook_path):
    """Extract just markdown and code sources, no outputs"""
    with open(notebook_path) as f:
        nb = json.load(f)

    text_parts = []
    for cell in nb.get('cells', []):
        if cell.get('cell_type') in ['markdown', 'code']:
            source = cell.get('source', [])
            if isinstance(source, list):
                text_parts.extend(source)
            elif isinstance(source, str):
                text_parts.append(source)

    return '\n'.join(text_parts)

# Test with 01_Data_Fourier_Practice
nb_path = Path("/Users/marinedenolle/GitHub/ess-412-512-intro2seismology/notebooks/01_Data_Fourier_Practice.ipynb")
source_text = extract_sources_from_notebook(nb_path)

print(f"✓ Extracted {len(source_text)} characters from {nb_path.name}")
print(f"  Contains 'Learning Objectives': {'Learning Objectives' in source_text}")
print(f"  Contains '1. Theory' (refactored): {'1. Theory' in source_text}")
print(f"  Contains 'Part 1' (old format): {'Part 1' in source_text}")
print(f"\nFirst 300 chars of extracted text:")
print(source_text[:300])
