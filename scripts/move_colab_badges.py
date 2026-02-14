#!/usr/bin/env python3
"""Move Colab badges below notebook titles and format as notes."""

import json
import glob
import re

def update_notebooks():
    notebooks = sorted(glob.glob("notebooks/*.ipynb"))
    updated_count = 0

    for nb_path in notebooks:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)

        # Find Colab badge cell and title cell
        colab_cell_idx = None
        title_cell_idx = None

        for idx, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'markdown':
                source = ''.join(cell['source'])

                # Check for Colab badge
                if 'colab.research.google.com' in source and colab_cell_idx is None:
                    colab_cell_idx = idx

                # Check for title (line starting with # but not ##)
                if re.match(r'^#\s+[^#]', source.strip()) and title_cell_idx is None:
                    title_cell_idx = idx

        # If we found both, reorganize
        if colab_cell_idx is not None and title_cell_idx is not None:
            # Get the cells
            colab_cell = nb['cells'][colab_cell_idx]

            # Extract the Colab badge HTML
            colab_source = ''.join(colab_cell['source']).strip()

            # Format as a note
            new_colab_content = f"```{{note}}\n{colab_source}\n```"

            # If Colab badge is before title, swap them
            if colab_cell_idx < title_cell_idx:
                # Remove the standalone Colab cell
                nb['cells'].pop(colab_cell_idx)
                # Title cell index shifts down by 1
                title_cell_idx -= 1
                # Get title content
                title_source = ''.join(nb['cells'][title_cell_idx]['source'])
                # Merge: title + newline + note with badge
                nb['cells'][title_cell_idx]['source'] = [
                    title_source.rstrip() + '\n\n' + new_colab_content + '\n'
                ]
                print(f"✓ {nb_path.split('/')[-1]}: moved badge below title")
                updated_count += 1
            # If Colab badge is after title
            elif colab_cell_idx > title_cell_idx:
                # Check if they're adjacent
                if colab_cell_idx == title_cell_idx + 1:
                    # Merge into title cell
                    title_source = ''.join(nb['cells'][title_cell_idx]['source'])
                    nb['cells'][title_cell_idx]['source'] = [
                        title_source.rstrip() + '\n\n' + new_colab_content + '\n'
                    ]
                    # Remove the standalone Colab cell
                    nb['cells'].pop(colab_cell_idx)
                    print(f"✓ {nb_path.split('/')[-1]}: formatted badge as note")
                    updated_count += 1
                else:
                    # Move and merge
                    title_source = ''.join(nb['cells'][title_cell_idx]['source'])
                    nb['cells'][title_cell_idx]['source'] = [
                        title_source.rstrip() + '\n\n' + new_colab_content + '\n'
                    ]
                    nb['cells'].pop(colab_cell_idx)
                    print(f"✓ {nb_path.split('/')[-1]}: moved and formatted badge")
                    updated_count += 1

            # Save the notebook
            with open(nb_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"\n✅ Updated {updated_count} notebooks!")

if __name__ == "__main__":
    update_notebooks()
