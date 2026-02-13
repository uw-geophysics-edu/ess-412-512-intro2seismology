#!/usr/bin/env python3
"""
Add Colab badges to all notebooks in the notebooks/ directory.
"""
import json
from pathlib import Path

def create_colab_badge(notebook_name):
    """Create Colab badge markdown for a notebook."""
    repo_url = "https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology"
    colab_url = f"https://colab.research.google.com/github/UW-geophysics-edu/ess-412-512-intro2seismology/blob/main/notebooks/{notebook_name}"
    badge_url = "https://colab.research.google.com/assets/colab-badge.svg"
    
    return f"[![Open In Colab]({badge_url})]({colab_url})"

def add_badge_to_notebook(notebook_path):
    """Add or update Colab badge in a notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    notebook_name = notebook_path.name
    badge_markdown = create_colab_badge(notebook_name)
    
    # Check if first cell already has Colab badge
    if nb['cells'] and nb['cells'][0]['cell_type'] == 'markdown':
        first_cell_source = ''.join(nb['cells'][0]['source'])
        if 'colab-badge.svg' in first_cell_source.lower():
            # Update existing badge
            lines = nb['cells'][0]['source']
            # Find and replace the badge line
            for i, line in enumerate(lines):
                if 'colab-badge.svg' in line.lower():
                    lines[i] = badge_markdown + '\n'
                    break
            print(f"  ✓ Updated badge in {notebook_name}")
        else:
            # Prepend badge to existing first cell
            nb['cells'][0]['source'] = [badge_markdown + '\n\n'] + nb['cells'][0]['source']
            print(f"  ✓ Added badge to existing first cell in {notebook_name}")
    else:
        # Insert new markdown cell with badge at the beginning
        badge_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [badge_markdown + '\n']
        }
        nb['cells'].insert(0, badge_cell)
        print(f"  ✓ Inserted new badge cell in {notebook_name}")
    
    # Save notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write('\n')
    
    return True

def main():
    """Add badges to all notebooks."""
    notebooks_dir = Path(__file__).parent.parent / 'notebooks'
    
    # Get all .ipynb files except backups
    notebooks = sorted([
        nb for nb in notebooks_dir.glob('*.ipynb')
        if not nb.name.endswith('.backup')
    ])
    
    print(f"Adding Colab badges to {len(notebooks)} notebooks...\n")
    
    success_count = 0
    for notebook_path in notebooks:
        try:
            if add_badge_to_notebook(notebook_path):
                success_count += 1
        except Exception as e:
            print(f"  ✗ Error processing {notebook_path.name}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Added/updated badges in {success_count}/{len(notebooks)} notebooks")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
