#!/usr/bin/env python3
"""
Spellcheck notebooks, ignoring cell outputs.
Only checks markdown source and code source, skips execution outputs.
Integrates with codespell via temp files.
"""
import json
import subprocess
import tempfile
import os
from pathlib import Path

def extract_sources_from_notebook(notebook_path):
    """
    Extract markdown and code source from notebook, excluding cell outputs.
    Returns concatenated text of all cell sources.
    """
    with open(notebook_path, 'r') as f:
        nb = json.load(f)

    text_parts = []

    for cell in nb.get('cells', []):
        # Only process markdown and code cells
        # Explicitly skip outputs by not including them
        if cell.get('cell_type') in ['markdown', 'code']:
            source = cell.get('source', [])

            # Handle both list and string source formats
            if isinstance(source, list):
                text_parts.extend(source)
            elif isinstance(source, str):
                text_parts.append(source)

    return '\n'.join(text_parts)

def spellcheck_notebooks(verbose=False):
    """
    Run codespell on all notebooks' sources, excluding outputs.

    Args:
        verbose: If True, print files being checked
    """
    repo_root = Path('.')

    # Find all notebooks (excluding _build and checkpoints)
    notebook_paths = []
    for pattern in ['notebooks/*.ipynb', 'homework/*.ipynb', 'lectures/**/*.ipynb']:
        for nb_path in repo_root.glob(pattern):
            if '_build' not in str(nb_path) and '.ipynb_checkpoints' not in str(nb_path):
                notebook_paths.append(nb_path)

    if not notebook_paths:
        print("No notebooks found to check")
        return 0

    # Create temporary directory for extracted sources
    with tempfile.TemporaryDirectory() as tmpdir:
        check_files = []

        for nb_path in sorted(notebook_paths):
            if verbose:
                print(f"Extracting: {nb_path}")

            # Extract source text (no outputs)
            source_text = extract_sources_from_notebook(nb_path)

            # Create temp file with extracted source
            temp_file = Path(tmpdir) / f"{nb_path.stem}.txt"
            with open(temp_file, 'w') as f:
                f.write(source_text)

            check_files.append(str(temp_file))

        # Run codespell on all extracted files
        print(f"\n✓ Extracted {len(check_files)} notebooks (excluding outputs)")
        print(f"Running codespell...\n")

        try:
            result = subprocess.run(
                ['codespell'] + check_files,
                cwd=str(repo_root),
                capture_output=False,
                text=True
            )
            return result.returncode
        except FileNotFoundError:
            print("Error: codespell not found. Install with: pip install codespell")
            return 1

if __name__ == '__main__':
    import sys
    verbose = '-v' in sys.argv or '--verbose' in sys.argv
    exit_code = spellcheck_notebooks(verbose=verbose)
    sys.exit(exit_code)
