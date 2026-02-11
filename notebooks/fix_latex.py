#!/usr/bin/env python3
import json

# Read the notebook
with open('Midterm_ComputerProgram1_Assignment.ipynb', 'r') as f:
    nb = json.load(f)

count_cells = 0
total_replacements = 0

# Process each cell
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        cell_modified = False
        # Process source lines
        if isinstance(cell['source'], list):
            for i in range(len(cell['source'])):
                original = cell['source'][i]
                # Replace inline math \( \) with $ $
                modified = original.replace('\\(', '$').replace('\\)', '$')
                # Replace display math \[ \] with $$ $$
                modified = modified.replace('\\[', '$$').replace('\\]', '$$')
                if modified != original:
                    total_replacements += 1
                    cell_modified = True
                cell['source'][i] = modified
        elif isinstance(cell['source'], str):
            original = cell['source']
            modified = original.replace('\\(', '$').replace('\\)', '$')
            modified = modified.replace('\\[', '$$').replace('\\]', '$$')
            if modified != original:
                total_replacements += 1
                cell_modified = True
            cell['source'] = modified
        
        if cell_modified:
            count_cells += 1

# Save the modified notebook
with open('Midterm_ComputerProgram1_Assignment.ipynb', 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"✓ Successfully replaced LaTeX math delimiters")
print(f"  Modified {count_cells} cells with {total_replacements} line changes")
print(f"  \\( \\) → $ $ (inline math)")
print(f"  \\[ \\] → $$ $$ (display math)")
