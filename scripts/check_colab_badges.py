#!/usr/bin/env python3
"""
Check that all notebooks have Google Colab badges.
"""
import sys
import json
from pathlib import Path

def check_notebook_badge(notebook_path):
    """Check if a notebook has a Colab badge."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        if not nb.get('cells'):
            return False, "No cells found"
        
        # Check first few cells for badge
        for i, cell in enumerate(nb['cells'][:3]):  # Check first 3 cells
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                source_lower = source.lower()
                if 'colab-badge.svg' in source_lower or 'open in colab' in source_lower:
                    # Check if it has the correct org (uw-geophysics-edu) in the GitHub URL
                    if 'uw-geophysics-edu' in source_lower and 'ess-412-512-intro2seismology' in source_lower:
                        return True, f"Found in cell {i+1}"
                    else:
                        return False, f"Badge found in cell {i+1} but URL is incorrect"
        
        return False, "No badge found in first 3 cells"
    
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    """Check all notebooks for Colab badges."""
    notebooks_dir = Path(__file__).parent.parent / 'notebooks'
    
    if not notebooks_dir.exists():
        print(f"✗ Notebooks directory not found: {notebooks_dir}")
        sys.exit(1)
    
    # Get all .ipynb files except backups
    notebooks = sorted([
        nb for nb in notebooks_dir.glob('*.ipynb')
        if not nb.name.endswith('.backup') and not nb.name.startswith('old_')
    ])
    
    print(f"Checking Colab badges in {len(notebooks)} notebooks...\\n")
    print(f"{'='*70}")
    
    results = []
    for notebook_path in notebooks:
        has_badge, message = check_notebook_badge(notebook_path)
        results.append((notebook_path.name, has_badge, message))
        
        status = "✓" if has_badge else "✗"
        print(f"{status} {notebook_path.name:45} {message}")
    
    print(f"{'='*70}\\n")
    
    # Summary
    passed = sum(1 for _, has_badge, _ in results if has_badge)
    total = len(results)
    
    if passed == total:
        print(f"✅ VALIDATION PASSED: All {total} notebooks have Colab badges!")
        sys.exit(0)
    else:
        print(f"❌ VALIDATION FAILED: {total - passed}/{total} notebooks missing Colab badges")
        print(f"\\nMissing badges in:")
        for name, has_badge, message in results:
            if not has_badge:
                print(f"  - {name}: {message}")
        sys.exit(1)

if __name__ == '__main__':
    main()
