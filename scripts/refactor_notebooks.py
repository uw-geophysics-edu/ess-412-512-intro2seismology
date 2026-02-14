#!/usr/bin/env python3
"""
True Comprehensive Notebook Refactoring Script
1. Renames "Part X" headings to "X."
2. Inserts dependency cell (hidden) if missing.
3. Tags dependency cell as 'hide-input'.
4. Fixes Colab badges in Intro markdown if needed (not implemented yet, but dependency cell is the main issue).
"""
import json
import re
from pathlib import Path

# Dependency cell content to insert
DEPENDENCY_CELL_SOURCE = [
    "# Install dependencies (for Google Colab or missing packages)\n",
    "import sys\n",
    "\n",
    "# Check if running in Colab\n",
    "try:\n",
    "    import google.colab\n",
    "    IN_COLAB = True\n",
    "    print(\"Running in Google Colab\")\n",
    "except:\n",
    "    IN_COLAB = False\n",
    "    print(\"Running in local environment\")\n",
    "\n",
    "# Install required packages if needed\n",
    "required_packages = {\n",
    "    'numpy': 'numpy',\n",
    "    'matplotlib': 'matplotlib',\n",
    "    'scipy': 'scipy',\n",
    "    'obspy': 'obspy'\n",
    "}\n",
    "\n",
    "missing_packages = []\n",
    "for package, pip_name in required_packages.items():\n",
    "    try:\n",
    "        __import__(package)\n",
    "        print(f\"✓ {package} is already installed\")\n",
    "    except ImportError:\n",
    "        missing_packages.append(pip_name)\n",
    "        print(f\"✗ {package} not found\")\n",
    "\n",
    "if missing_packages:\n",
    "    print(f\"\\nInstalling missing packages: {', '.join(missing_packages)}\")\n",
    "    import subprocess\n",
    "    subprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", \"-q\"] + missing_packages)\n",
    "    print(\"✓ Installation complete!\")\n",
    "else:\n",
    "    print(\"\\n✓ All required packages are installed!\")"
]

def rename_headings(nb_path, nb_data):
    """Refactor part headings in place."""
    changed = False
    for cell in nb_data['cells']:
        if cell['cell_type'] in ['markdown', 'code']:
            source = cell.get('source', [])
            if isinstance(source, list):
                for i, line in enumerate(source):
                    original = line
                    # Regex replacement logic (combining patterns from previous attempts)

                    # Pattern 1: **Part X: Description** -> **X. Description**
                    line = re.sub(r'\*\*Part\s+([IVivx0-9]+):\s*(.+?)\*\*', r'**\1. \2**', line)

                    # Pattern 2: ## Part X: Description -> ## X. Description
                    line = re.sub(r'^(#+)\s+Part\s+([IVivx0-9]+):\s*(.+)$', r'\1 \2. \3', line)

                    # Pattern 3: # Part 1 — Description -> # 1. Description
                    line = re.sub(r'^(#+)\s+Part\s+(\d+)\s+—\s+(.+)$', r'\1 \2. \3', line)

                    # Pattern 4: # Part A — Description -> # A. Description
                    line = re.sub(r'^(#+)\s+Part\s+([A-Z])\s+—\s+(.+)$', r'\1 \2. \3', line)

                    if line != original:
                        source[i] = line
                        changed = True
    return changed

def ensure_dependency_cell(nb_path, nb_data):
    """
    Check if dependency cell exists. If not, insert after first markdown cell.
    """
    # Check if exists
    for cell in nb_data['cells']:
        if cell['cell_type'] == 'code':
            source_str = ''.join(cell.get('source', []))
            if 'Install dependencies' in source_str or 'google.colab' in source_str:
                return False # Already exists

    # Create new cell
    dep_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {
            "tags": ["hide-input"]
        },
        "outputs": [],
        "source": DEPENDENCY_CELL_SOURCE
    }

    # Insert after the first markdown intro (index 0 usually)
    # If notebook empty, append.
    if not nb_data['cells']:
        nb_data['cells'].append(dep_cell)
    elif nb_data['cells'][0]['cell_type'] == 'markdown':
         nb_data['cells'].insert(1, dep_cell)
    else:
         nb_data['cells'].insert(0, dep_cell)

    return True

def ensure_hide_input_tags(nb_path, nb_data):
    """Ensure existing dependency cells have hide-input tag."""
    changed = False
    for cell in nb_data['cells']:
        if cell['cell_type'] == 'code':
            source_str = ''.join(cell.get('source', []))
            if 'Install dependencies' in source_str or 'google.colab' in source_str:
                meta = cell.setdefault('metadata', {})
                tags = meta.setdefault('tags', [])
                if 'hide-input' not in tags:
                    tags.append('hide-input')
                    changed = True
    return changed

def main():
    repo_root = Path('.')
    # Find notebooks recursively or just in the 'notebooks' folder
    # Assuming user wants 'notebooks/' primarily
    notebooks = sorted(repo_root.glob('notebooks/*.ipynb'))

    print(f"Checking {len(notebooks)} notebooks...")

    for nb_path in notebooks:
        try:
            with open(nb_path, 'r') as f:
                nb_data = json.load(f)

            changes = []

            if rename_headings(nb_path, nb_data):
                changes.append("Renamed headings")

            if ensure_dependency_cell(nb_path, nb_data):
                changes.append("Inserted dependency cell")

            if ensure_hide_input_tags(nb_path, nb_data):
                changes.append("Added hide-input tag")

            if changes:
                print(f"✓ {nb_path.name}: {', '.join(changes)}")
                with open(nb_path, 'w') as f:
                    json.dump(nb_data, f, indent=4)
            else:
                print(f"  {nb_path.name} (No changes needed)")

        except Exception as e:
            print(f"✗ Error processing {nb_path.name}: {e}")

if __name__ == '__main__':
    main()
