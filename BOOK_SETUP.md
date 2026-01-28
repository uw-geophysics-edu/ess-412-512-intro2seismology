# Jupyter Book Setup: Pixi + Conda Dual Environment

This course uses **Jupyter Book v1** with dual environment support for maximum flexibility.

## Quick Start

### Option 1: Using Pixi (Recommended for CI/Instructors)

```bash
pixi install
pixi run build-all    # Build with BASE_URL=/ess-412-512-intro2seismology
pixi run serve-all    # Preview at http://localhost:3000
```

### Option 2: Using Conda (For Students)

```bash
conda env create -f environment.yml
conda activate ess412
jupyter book build .
python -m http.server --directory _build/html 8000
```

## Key Features

- **Jupyter Book v1**: Sphinx-based with MyST markdown
- **Lecture markdown**: `.md` files with LaTeX and embedded figures
- **Figure embedding**: MyST `{figure}` directives render correctly
- **No execution**: `execute_notebooks: off` (notebooks include data downloads)
- **GitHub Pages**: Deployed at https://uw-geophysics-edu.github.io/ess-412-512-intro2seismology/

## Pixi Tasks

- `pixi run build-book` - Build HTML only
- `pixi run build-all` - Build + website structure (local preview)
- `pixi run serve-all` - Preview at localhost:3000
- `pixi run linkcheck` - Check all links
- `pixi run spellcheck` - Run codespell
- `pixi run clean` - Remove build artifacts

## LaTeX Math Rendering

**Inline**: `$v$ is velocity`  
**Display**: `$$ \sin\theta_1/v_1 = \sin\theta_2/v_2 $$`

## Figure Syntax

```markdown
{figure} lectures/scripts/figures/fig1_plane_wave_incident.png
---
name: fig-plane-wave-incident
alt: Description
---
Caption text here.
```

✅ **Status**: Build successful with all figures rendering!
