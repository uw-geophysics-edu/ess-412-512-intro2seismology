# Jupyter Book Deployment Guide

## ✅ Setup Complete!

Your Jupyter Book configuration is ready. The following files have been created:

- `_config.yml` - Jupyter Book configuration
- `_toc.yml` - Table of contents (organized by modules)
- `.github/workflows/deploy-book.yml` - Automatic deployment workflow
- `.gitignore` - Updated to exclude build artifacts

## 🚀 Deploy Your Course Book

### Step 1: Enable GitHub Pages

1. Go to: https://github.com/uw-geophysics-edu/ess-412-512-intro2seismology/settings/pages
2. Under **"Source"**, select: **GitHub Actions**
3. Click **Save**

### Step 2: Push to GitHub

```bash
cd /Users/marinedenolle/GitHub/ess-412-512-intro2seismology

# Add all the configuration files
git add _config.yml _toc.yml .github/ .gitignore

# Commit the Jupyter Book setup
git commit -m "Add Jupyter Book configuration and auto-deployment"

# Push to trigger the build
git push origin main
```

### Step 3: Monitor the Build

1. Go to: https://github.com/uw-geophysics-edu/ess-412-512-intro2seismology/actions
2. Watch the "Deploy Jupyter Book" workflow run (takes ~2-3 minutes)
3. Once complete (green checkmark ✅), your book is live!

### Step 4: View Your Course Book

Your course will be available at:
**https://uw-geophysics-edu.github.io/ess-412-512-intro2seismology/**

## 🔄 Weekly Workflow (From Now On)

Every time you update notebooks:

```bash
# Edit your notebooks as usual
jupyter lab

# When ready to publish:
git add notebooks/*.ipynb
git commit -m "Week X: Updated module Y"
git push

# ✨ That's it! GitHub Actions automatically rebuilds and deploys
```

## 🧪 Local Testing (Before Pushing)

Test your changes locally before deploying:

### Option 1: Using Pixi (Recommended)

```bash
cd /Users/marinedenolle/GitHub/ess-412-512-intro2seismology

# Install Jupyter Book in pixi environment
pixi add jupyter-book

# Build the book
pixi run jupyter-book build .

# View in browser
open _build/html/index.html

# Clean build (if needed)
pixi run jupyter-book clean .
```

### Option 2: Using Conda Environment

```bash
# Activate your ess412 environment
conda activate ess412

# Install Jupyter Book (one time)
pip install jupyter-book

# Build the book
jupyter-book build .

# View in browser
open _build/html/index.html

# Clean and rebuild if needed
jupyter-book clean .
jupyter-book build .
```

### Option 3: Standalone Virtual Environment

```bash
# Create test environment (one time)
python -m venv .venv-jb
source .venv-jb/bin/activate
pip install jupyter-book

# Build the book
jupyter-book build .

# View locally
open _build/html/index.html
```

### Verify Your Build

After building locally, check:
- ✅ All notebooks appear in navigation
- ✅ Lecture markdown files render correctly
- ✅ Math equations display properly
- ✅ Images and figures load
- ✅ No broken internal links
- ✅ Search functionality works

## 🎨 Optional: Customize Theme

To match your lab website colors, edit `_config.yml` and add:

```yaml
sphinx:
  config:
    html_theme_options:
      primary_color: "#4b2e83"  # UW purple
      secondary_color: "#b7a57a"  # UW gold
```

## 🔗 Update Your Course Page

Add this to your website at [denolle-lab.github.io/teaching/ess412/](https://denolle-lab.github.io/teaching/ess412/):

```markdown
## 📚 Course Materials

**[Interactive Course Book →](https://uw-geophysics-edu.github.io/ess-412-512-intro2seismology/)**

All lectures, labs, and assignments in an interactive, searchable format with direct links to launch notebooks in Binder or Colab.

**[GitHub Repository →](https://github.com/uw-geophysics-edu/ess-412-512-intro2seismology)**

Clone the repository to work on exercises locally.
```

## ❓ Troubleshooting

### Build fails?
- Check the Actions tab for error messages
- Most common issue: missing notebook files referenced in `_toc.yml`
- Verify all file paths in `_toc.yml` match your actual notebook names

### Need to skip a notebook temporarily?
Comment it out in `_toc.yml`:
```yaml
  # - file: notebooks/04_RayleighWaves_Theory
  #   title: "Lab 4: Rayleigh Waves"
```

### Want to add a new notebook?
1. Add the notebook to the repository
2. Add an entry in `_toc.yml` under the appropriate module
3. Push - the book rebuilds automatically!

## 📊 Features Your Students Will Love

✅ **Search**: Full-text search across all content
✅ **Navigation**: Organized by module with clear progression
✅ **Launch buttons**: "Open in Colab" and "Launch Binder" on every notebook
✅ **Mobile-friendly**: Works on phones and tablets
✅ **GitHub integration**: "Edit this page" links directly to GitHub
✅ **Download**: Students can download individual notebooks or entire book

---

**Questions?** Check the [Jupyter Book documentation](https://jupyterbook.org/) or open an issue on GitHub.
