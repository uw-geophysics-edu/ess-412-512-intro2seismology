# Installation Guide - ESS 412/512 Introduction to Seismology

This guide provides setup instructions for the computational labs in this course. We support two package managers: **Conda** (recommended for most students) and **Pixi** (faster alternative for advanced users).

## Prerequisites

- Basic command line familiarity
- ~2 GB free disk space for environment
- Internet connection for downloading packages and seismic data

---

## Option 1: Conda/Mamba Setup (Recommended)

### Step 1: Install Conda

If you don't have Conda installed:

**Option A: Miniforge (Recommended)**
```bash
# macOS (Intel or Apple Silicon)
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh

# Linux
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
bash Miniforge3-Linux-x86_64.sh

# Windows: Download and run
# https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe
```

**Option B: Anaconda** (if already installed, skip to Step 2)
- Download from: https://www.anaconda.com/download

### Step 2: Create Course Environment

```bash
# Clone the repository
git clone https://github.com/marinedenolle/ess-412-512-intro2seismology.git
cd ess-412-512-intro2seismology

# Create environment from environment.yml
conda env create -f environment.yml

# Activate the environment
conda activate ess412
```

### Step 3: Launch Jupyter

```bash
# Make sure environment is activated
conda activate ess412

# Start JupyterLab (recommended)
jupyter lab

# OR start Jupyter Notebook (classic interface)
jupyter notebook
```

### Updating the Environment

If new packages are added during the course:
```bash
conda activate ess412
conda env update -f environment.yml --prune
```

---

## Option 2: Pixi Setup (Advanced/Optional)

Pixi is a fast, modern package manager that creates reproducible environments. It's particularly useful for instructors and graduate students working on multiple projects.

### Step 1: Install Pixi

```bash
# macOS and Linux
curl -fsSL https://pixi.sh/install.sh | bash

# Windows (PowerShell)
iwr -useb https://pixi.sh/install.ps1 | iex
```

Restart your terminal after installation.

### Step 2: Setup Course Environment

```bash
# Clone the repository
git clone https://github.com/marinedenolle/ess-412-512-intro2seismology.git
cd ess-412-512-intro2seismology

# Install dependencies (creates pixi.lock automatically)
pixi install

# For graduate students (ESS 512) with additional packages:
pixi install --environment graduate
```

### Step 3: Launch Jupyter

```bash
# Undergraduate environment (ESS 412)
pixi run lab

# Graduate environment (ESS 512)
pixi run --environment graduate lab
```

### Advantages of Pixi

- **Speed**: 3-5x faster than conda for installation
- **Reproducibility**: Automatic lock file ensures identical environments
- **No activation needed**: `pixi run` handles environment automatically
- **Cross-platform**: Better Windows support

---

## Verifying Installation

After setup, verify everything works:

```python
# In a Python console or Jupyter notebook:
import numpy as np
import matplotlib.pyplot as plt
import obspy
from obspy.clients.fdsn import Client

print(f"NumPy: {np.__version__}")
print(f"ObsPy: {obspy.__version__}")

# Test data download
client = Client("IRIS")
print("IRIS client connection successful!")
```

Expected output:
```
NumPy: 1.x.x
ObsPy: 1.4.x
IRIS client connection successful!
```

---

## Platform-Specific Notes

### macOS

**Apple Silicon (M1/M2/M3):**
- Both conda and pixi work natively on ARM architecture
- ObsPy and all dependencies are available for `osx-arm64`
- No Rosetta emulation needed

**Intel Macs:**
- Fully supported on `osx-64` platform

### Linux

- Ubuntu 20.04+ and similar distributions fully supported
- May need system packages: `build-essential`, `libgeos-dev`
- If you encounter cartopy installation issues:
  ```bash
  sudo apt-get update
  sudo apt-get install libgeos-dev libproj-dev
  ```

### Windows

**Known Issues:**
- ObsPy installation can be slow with conda on Windows
- Pixi generally provides faster installation
- Some FDSN clients may require SSL certificate configuration

**Troubleshooting:**
If you encounter SSL errors when downloading data:
```python
from obspy.clients.fdsn import Client
client = Client("IRIS", force_redirect=True)
```

For detailed Windows setup, see: https://docs.obspy.org/

---

## Troubleshooting

### Conda environment creation fails

```bash
# Try using mamba (faster solver)
conda install mamba -c conda-forge
mamba env create -f environment.yml
```

### "Command not found: jupyter"

The environment may not be activated:
```bash
conda activate ess412
```

### Import errors for specific packages

Reinstall the package explicitly:
```bash
conda activate ess412
conda install -c conda-forge obspy
```

### Pixi installation slow or failing

Check your internet connection and try with verbose output:
```bash
pixi install -v
```

If issues persist, fall back to conda setup (Option 1).

### Data download timeout errors

```python
# Increase timeout in ObsPy client
from obspy.clients.fdsn import Client
client = Client("IRIS", timeout=300)  # 5 minutes
```

### Jupyter kernel not found

```bash
# Conda
conda activate ess412
python -m ipykernel install --user --name ess412 --display-name "Python (ESS412)"

# Pixi
pixi run python -m ipykernel install --user --name ess412-pixi
```

---

## Getting Help

1. **Check existing issues**: https://github.com/marinedenolle/ess-412-512-intro2seismology/issues
2. **ObsPy documentation**: https://docs.obspy.org/
3. **Course Canvas**: Post questions in the technical help forum
4. **Office hours**: See syllabus for schedule

---

## For Instructors/TAs

### Setting up the development environment

```bash
# With Pixi (recommended for testing)
pixi install --environment dev
pixi run --environment dev lab

# With Conda
conda env create -f environment.yml
conda activate ess412
conda install -c conda-forge black pytest nbval
```

### Running notebook tests

```bash
# Pixi
pixi run test

# Conda
conda activate ess412
pytest --nbval notebooks/
```

### Generating solution notebooks

Solutions are kept in `notebooks/solutions/` (not committed to student-facing repository).
