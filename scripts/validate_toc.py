#!/usr/bin/env python3
"""
Validate that all file references in _toc.yml exist in the repository.
"""
import sys
from pathlib import Path
import yaml

def validate_toc(toc_path, repo_root):
    """Validate all file references in _toc.yml exist."""
    with open(toc_path, 'r', encoding='utf-8') as f:
        toc = yaml.safe_load(f)

    errors = []
    files_checked = []

    # Check root file
    if 'root' in toc:
        root_file = repo_root / f"{toc['root']}.md"
        files_checked.append(('root', toc['root'], root_file))
        if not root_file.exists():
            errors.append(f"Root file not found: {root_file}")

    # Check all parts and chapters
    if 'parts' in toc:
        for part_idx, part in enumerate(toc['parts']):
            part_caption = part.get('caption', f'Part {part_idx}')

            if 'chapters' in part:
                for chapter in part['chapters']:
                    if 'file' in chapter:
                        file_ref = chapter['file']

                        # Try with various extensions
                        possible_paths = [
                            repo_root / f"{file_ref}.ipynb",
                            repo_root / f"{file_ref}.md",
                            repo_root / file_ref,
                        ]

                        found = False
                        actual_path = None
                        for path in possible_paths:
                            if path.exists():
                                found = True
                                actual_path = path
                                break

                        files_checked.append((part_caption, file_ref, actual_path))

                        if not found:
                            errors.append(
                                f"[{part_caption}] File not found: {file_ref}\\n"
                                f"  Tried: {[str(p.relative_to(repo_root)) for p in possible_paths]}"
                            )

    return files_checked, errors

def main():
    """Main validation function."""
    repo_root = Path(__file__).parent.parent
    toc_path = repo_root / '_toc.yml'

    if not toc_path.exists():
        print(f"✗ _toc.yml not found at {toc_path}")
        sys.exit(1)

    print("Validating _toc.yml file references...")
    print(f"Repository root: {repo_root}")
    print(f"TOC file: {toc_path}\\n")

    files_checked, errors = validate_toc(toc_path, repo_root)

    # Print summary
    print(f"{'='*70}")
    print(f"Checked {len(files_checked)} file references:")
    print(f"{'='*70}\\n")

    for caption, file_ref, actual_path in files_checked:
        if actual_path and actual_path.exists():
            rel_path = actual_path.relative_to(repo_root)
            print(f"✓ [{caption:30}] {rel_path}")
        else:
            print(f"✗ [{caption:30}] {file_ref} (NOT FOUND)")

    print(f"\\n{'='*70}")

    if errors:
        print(f"\\n❌ VALIDATION FAILED: {len(errors)} error(s) found:\\n")
        for error in errors:
            print(f"  {error}\\n")
        sys.exit(1)
    else:
        print(f"\\n✅ VALIDATION PASSED: All {len(files_checked)} file references exist!")
        sys.exit(0)

if __name__ == '__main__':
    main()
