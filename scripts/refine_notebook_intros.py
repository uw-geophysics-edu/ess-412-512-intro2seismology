#!/usr/bin/env python3
"""
Refine notebook introductions to have a clean, consolidated structure:
- Title
- Colab badge (in note block)
- Single introduction/overview section (consolidating learning objectives, prerequisites, etc.)
"""

import json
import re
import os
from pathlib import Path

os.chdir('/Users/marinedenolle/GitHub/ess-412-512-intro2seismology')

# Process each notebook
notebooks = sorted(Path('notebooks').glob('*.ipynb'))

for nb_path in notebooks:
    print(f"\n{'='*60}")
    print(f"Processing: {nb_path.name}")
    print('='*60)

    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    if not nb['cells']:
        continue

    # Check if first cell is markdown with title and badge
    first_cell = nb['cells'][0]
    if first_cell['cell_type'] != 'markdown':
        print(f"  ⚠ First cell is not markdown, skipping")
        continue

    source = ''.join(first_cell['source'])

    # Check if it has the colab badge
    if 'colab.research.google.com' not in source:
        print(f"  ⚠ No Colab badge found, skipping")
        continue

    # Extract title (first h1 heading)
    title_match = re.search(r'^# (.+?)$', source, re.MULTILINE)
    if not title_match:
        print(f"  ⚠ No title found, skipping")
        continue

    title = title_match.group(0)  # Full line with #

    # Extract the Colab badge from note block
    badge_match = re.search(r'```\{note\}\n(\[!\[Open In Colab\][^\n]+)\n```', source, re.DOTALL)
    if not badge_match:
        print(f"  ⚠ Badge not in correct format, skipping")
        continue

    badge_block = badge_match.group(0)

    # Get everything after the badge block
    rest_of_cell = source.split(badge_block, 1)[1].strip()

    # Now consolidate the intro section
    # Look for common patterns to consolidate
    new_intro = []

    # Check for various intro elements
    has_learning_obj = 'Learning Objectives' in rest_of_cell or 'Learning outcomes' in rest_of_cell or 'Learning goals' in rest_of_cell
    has_prerequisites = 'Prerequisites' in rest_of_cell or 'Prereqs' in rest_of_cell
    has_reference = 'Reference:' in rest_of_cell
    has_overview = '## Overview' in rest_of_cell
    has_roadmap = 'Roadmap' in rest_of_cell or 'roadmap' in rest_of_cell

    # Extract key information sections before first ## or Part
    # Split at first occurrence of major section (##, Part, ---, etc.)
    intro_section = rest_of_cell
    main_content_start = -1

    # Find where main content starts (first ## that's not Overview/Background/Instructions)
    for match in re.finditer(r'\n## (?!Overview|Background|Instructions|Roadmap|Learning|Reference)', rest_of_cell):
        main_content_start = match.start()
        break

    # Also check for horizontal rules or "Part" markers
    part_match = re.search(r'\n(?:---\n+)?##? Part [0-9]', rest_of_cell)
    if part_match and (main_content_start == -1 or part_match.start() < main_content_start):
        main_content_start = part_match.start()

    # Also check for "## 0." or "## 1." style sections
    num_section_match = re.search(r'\n## [0-9]\.', rest_of_cell)
    if num_section_match and (main_content_start == -1 or num_section_match.start() < main_content_start):
        main_content_start = num_section_match.start()

    if main_content_start > 0:
        intro_section = rest_of_cell[:main_content_start].strip()
        main_content = rest_of_cell[main_content_start:].strip()
    else:
        intro_section = rest_of_cell.strip()
        main_content = ""

    # Remove "## Overview" heading if present
    intro_section = re.sub(r'^## Overview\s*\n+', '', intro_section, flags=re.MULTILINE)

    # Remove multiple horizontal rules
    intro_section = re.sub(r'\n---+\n+', '\n\n', intro_section)
    intro_section = re.sub(r'^---+\n+', '', intro_section)

    # Remove "### Roadmap" heading but keep content
    intro_section = re.sub(r'### Roadmap\s*\n+', '\n**Outline:**\n', intro_section)

    # Clean up excessive blank lines
    intro_section = re.sub(r'\n{3,}', '\n\n', intro_section)

    # Reconstruct the first cell with cleaner structure
    new_source = f"{title}\n\n{badge_block}\n\n{intro_section.strip()}"

    if main_content:
        new_source += f"\n\n{main_content}"

    # Update the cell
    first_cell['source'] = [new_source + '\n']

    # Save the notebook
    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"  ✓ Refined introduction section")

print(f"\n{'='*60}")
print("✅ All notebooks refined!")
print('='*60)
