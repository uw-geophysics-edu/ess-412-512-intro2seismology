# Contributing to ESS 412/512 Seismology Course

Thank you for your interest in contributing to this educational repository! This guide will help you set up your development environment and understand our workflow.

## Quick Start for Developers

### 1. Clone and Setup Environment

```bash
git clone https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology.git
cd ess-412-512-intro2seismology

# Option A: Using Pixi (recommended)
curl -fsSL https://pixi.sh/install.sh | sh
pixi install

# Option B: Using Conda
conda env create -f environment.yml
conda activate ess412
```

### 2. Install Pre-commit Hooks (Recommended)

Pre-commit hooks automatically validate your changes before each commit:

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Install the hooks
pre-commit install

# Test the hooks
pre-commit run --all-files
```

Once installed, the hooks will run automatically on `git commit`. To bypass them temporarily (not recommended):
```bash
git commit --no-verify
```

## Development Workflow

### Before Making Changes

1. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Pull latest changes** from main:
   ```bash
   git pull origin main
   ```

### Adding or Modifying Notebooks

#### File Naming Convention

Notebooks follow a systematic naming pattern:
```
{Module}{Letter}_{Topic}_{Type}.ipynb

Examples:
- 01_Data_Fourier_Practice.ipynb       # Module 1, practice notebook
- 03a_Body_Waves_Theory.ipynb          # Module 3, part a, theory
- 05c_Surface_Waves_Practice.ipynb     # Module 5, part c, practice
```

**Types:**
- `Theory`: Theoretical derivations and explanations
- `Practice`: Hands-on computational exercises

#### Required Components for New Notebooks

Every notebook must include:

1. **Colab Badge** (first markdown cell):
   ```markdown
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UW-geophysics-edu/ess-412-512-intro2seismology/blob/main/notebooks/{notebook_name}.ipynb)
   ```

2. **Header with title and description**
3. **Learning outcomes** section
4. **Prerequisites** (if any)
5. **Estimated completion time**
6. **ESS 512 differentiation** (if graduate-level content exists)

#### Adding Notebooks to the Book

1. Place the notebook in `notebooks/` directory
2. Update `_toc.yml` to include it in the appropriate module
3. Run validation: `pixi run validate` or `python scripts/validate_toc.py`
4. Test build: `pixi run build-book`

### Validation Commands

Before committing, run these checks:

```bash
# Validate all file references in _toc.yml
pixi run validate-toc
# or: python scripts/validate_toc.py

# Check all notebooks have Colab badges
pixi run validate-badges
# or: python scripts/check_colab_badges.py

# Run both validations
pixi run validate

# Build the book locally
pixi run build-book

# Spell check
pixi run spellcheck

# Link check (checks external links)
pixi run linkcheck

# Run everything (validation + build)
pixi run precommit
```

### Testing Your Changes

#### Local Testing

```bash
# Build and serve the book locally
pixi run build-book
pixi run serve-book
# Visit http://localhost:8000

# Or use all-in-one command
pixi run build-all
pixi run serve-all
```

#### Testing in Google Colab

1. Commit and push your branch to GitHub
2. Click the Colab badge in your notebook
3. Verify it launches correctly and all dependencies install

### Common Issues and Solutions

#### Issue: _toc.yml validation fails

**Symptom:** `validate-toc` reports missing files

**Solution:**
- Check file paths in `_toc.yml` match actual files (case-sensitive)
- Ensure files have correct extensions (`.ipynb` or `.md`)
- Run `ls notebooks/` to verify file names

#### Issue: Colab badge validation fails

**Symptom:** `validate-badges` reports incorrect URLs

**Solution:**
- Badge URL must include `UW-geophysics-edu` and `ess-412-512-intro2seismology`
- Use the script to fix: `python scripts/add_colab_badges.py`

#### Issue: Book build fails

**Symptom:** `jupyter book build .` throws errors

**Solution:**
- Check for syntax errors in markdown cells
- Verify all code cells execute successfully
- Look for broken internal links (e.g., `[text](path/to/file.ipynb)`)
- Clean build artifacts: `pixi run clean` then rebuild

#### Issue: Large files rejected

**Symptom:** Git complains about file size

**Solution:**
- Pre-commit limits files to 5MB
- For data files, link to external sources instead
- Use `.gitignore` for large temporary files
- For figures, optimize image compression

## File Organization

```
ess-412-512-intro2seismology/
├── notebooks/            # All Jupyter notebooks (main content)
├── lectures/             # Markdown lecture notes
├── solutions/            # Instructor solutions (git ignored)
├── scripts/              # Utility scripts (validation, badges, etc.)
├── _build/               # Build artifacts (git ignored)
├── _toc.yml             # Table of contents for book structure
├── _config.yml          # Jupyter Book configuration
├── pixi.toml            # Pixi package/task manager config
├── environment.yml      # Conda environment specification
├── .pre-commit-config.yaml  # Pre-commit hook configuration
└── README.md            # Main course documentation
```

## Commit Message Guidelines

Use clear, descriptive commit messages:

```bash
# Good examples:
git commit -m "Add polarization analysis to 03a_Body_Waves_Theory"
git commit -m "Fix broken link in README to surface waves lecture"
git commit -m "Update _toc.yml with new reflection module"

# Less helpful:
git commit -m "Update notebook"
git commit -m "Fix stuff"
git commit -m "WIP"
```

## Pull Request Process

1. **Validate locally:**
   ```bash
   pixi run precommit
   ```

2. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request on GitHub:**
   - Provide clear description of changes
   - Reference any related issues
   - Describe testing performed
   - Note if this affects student assignments

4. **Wait for CI checks:**
   - GitHub Actions will run validation and build
   - Fix any failures before review

5. **Address review comments:**
   - Make requested changes
   - Push updates to the same branch

## Adding New Modules

To add an entirely new module (e.g., Module 6 - Tomography):

1. **Create notebooks** with proper naming:
   ```
   06a_Tomography_Theory.ipynb
   06b_Tomography_Practice.ipynb
   ```

2. **Create lecture notes** (optional):
   ```
   lectures/tomography-lecture.md
   ```

3. **Update `_toc.yml`:**
   ```yaml
   - caption: Module 6 - Tomography
     chapters:
       - file: lectures/tomography-lecture
         title: "Lecture: Travel-Time Tomography"
       - file: notebooks/06a_Tomography_Theory
         title: "Lab 6a: Tomography Theory"
       - file: notebooks/06b_Tomography_Practice
         title: "Lab 6b: Tomography Practicum"
   ```

4. **Update README.md** with module description and learning objectives

5. **Validate:**
   ```bash
   pixi run validate
   pixi run build-book
   ```

## Questions or Issues?

- **Course content questions:** Use Canvas discussion board (students) or email instructor
- **Technical/repository issues:** Open a GitHub Issue
- **Urgent bugs:** Tag with `bug` label and mention @marinedenolle

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
