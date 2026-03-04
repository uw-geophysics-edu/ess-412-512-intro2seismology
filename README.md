# ESS 412/512: Introduction to Seismology

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy Jupyter Book](https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology/actions/workflows/deploy-book.yml/badge.svg)](https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology/actions/workflows/deploy-book.yml)

Computational labs and exercises for upper-level undergraduate (ESS 412) and junior graduate (ESS 512) seismology course. Course materials supplement Peter Shearer's **"Introduction to Seismology"** textbook with hands-on Python exercises using real seismic data.

## Course Overview

This course introduces the fundamental principles of seismology through a combination of theoretical derivations and computational exercises. Students will learn to work with seismic data, implement key algorithms, and develop intuition for wave propagation, earthquake analysis, and Earth structure.

### Learning Objectives

By the end of this course, students will be able to:
- Apply elastic wave theory to seismic wave propagation problems
- Analyze seismic waveforms using Python and ObsPy
- Implement ray tracing and travel time calculations
- Measure and interpret surface wave dispersion
- Download and process real seismic data from global networks
- Differentiate between body waves (P, S) and surface waves (Love, Rayleigh)
- Apply signal processing techniques to seismological data
- Connect computational exercises to published seismological research (ESS 512)

### Prerequisites

- Physics fundamentals (waves, mechanics)
- Linear algebra and calculus
- Basic programming experience (Python recommended but not required)
- ESS 512 students: Additional mathematical maturity and research experience expected

## Repository Structure

```
ess-412-512-intro2seismology/
├── notebooks/                                    # Computational exercises (systematic naming)
│   ├── 01_Data_Fourier_Practice.ipynb          # Data handling, Fourier analysis, filtering
│   ├── 02_Stress_Strain_Practice.ipynb         # Elastic constants, stress/strain relationships
│   ├── 03a_Body_Waves_Theory.ipynb             # Body wave polarization and analysis
│   ├── 03b_Ray_Tracing_Cartesian_Practice.ipynb # 2D ray tracing with PyKonal
│   ├── 03c_Ray_Tracing_Global_Practice.ipynb   # Global ray tracing with TauP
│   ├── 03d_Global_Phases_Practice.ipynb        # Global phase identification
│   ├── 04a_Reflection_Coefficients_Theory.ipynb # Reflection/transmission at interfaces
│   ├── 04b_Reflection_CMP_Practice.ipynb       # CMP, NMO, migration demo
│   ├── 05a_Rayleigh_Waves_Theory.ipynb         # Rayleigh wave theory and derivations
│   ├── 05b_Love_Waves_Theory.ipynb             # Love wave theory and analysis
│   ├── 05c_Surface_Waves_Practice.ipynb        # Surface wave dispersion measurement
│   ├── 05d_Noise_CrossCorrelation_Practice.ipynb # Ambient noise interferometry
│   ├── Midterm_Integrated_Assignment.ipynb     # Comprehensive midterm assignment
│   ├── travel_time_tomography_iterative_pykonal.ipynb # Advanced: Iterative tomography
│   └── toy_surface_wave_inversion.ipynb        # Advanced: Surface wave inversion
├── solutions/                                    # Instructor-only solutions (gitignored)
│   └── 02_Stress_Strain_Solutions.ipynb        # Example solution with rubric
├── lectures/                                     # Lecture notes and teaching materials
│   ├── 02_Stress_Strain_Lecture.md             # Stress/strain lecture notes
│   ├── ray-theory.md                           # Ray theory fundamentals
│   ├── surface-waves.md                        # Surface wave theory (Rayleigh & Love)
│   ├── tomography-lecture-whiteboard.md        # Travel-time tomography notes
│   └── Graduate_Paper_Presentation.md          # ESS 512: Paper presentation guidelines
├── scripts/                                      # Utility scripts for book maintenance
│   ├── add_colab_badges.py                     # Add Google Colab badges to notebooks
│   └── validate_toc.py                         # Validate _toc.yml file references
├── environment.yml                               # Conda environment specification
├── pixi.toml                                     # Pixi configuration (preferred)
├── INSTALL.md                                    # Detailed setup instructions
├── LICENSE                                       # MIT License
└── README.md                                     # This file
```

## Quick Start

### Installation


See [INSTALL.md](INSTALL.md) for detailed setup instructions. Quick start:

**With Conda (Recommended):**
```bash
git clone https://github.com/uw-geophysics-edu/ess-412-512-intro2seismology.git
cd ess-412-512-intro2seismology
conda env create -f environment.yml
conda activate ess412
```

**With Pixi (Advanced):**

Install pixi on your system:
```bash
curl -fsSL https://pixi.sh/install.sh | sh
```
then install this local package.
```bash
git clone https://github.com/uw-geophysics-edu/ess-412-512-intro2seismology.git
cd ess-412-512-intro2seismology
pixi install
```

### Access the Course

**Interactive Jupyter Book** (Recommended for students):
- View: https://uw-geophysics-edu.github.io/ess-412-512-intro2seismology/
- Fully searchable, with launch buttons for Binder and Google Colab
- All lectures, labs, and assignments in one place

**Local Setup** (For development or offline work):
1. Start with [01_Data_Fourier_Practice.ipynb](notebooks/01_Data_Fourier_Practice.ipynb) to learn data handling and signal processing
2. Follow notebooks by module (see Course Content below)
3. Each notebook includes theory, demonstrations, and exercises
4. ESS 512 students should complete additional graduate-level exercises marked in each notebook

**Google Colab** (No installation required):
- Each notebook includes a "Open in Colab" badge at the top
- Click the badge to launch the notebook directly in Google Colab
- First cell installs required dependencies automatically
- Perfect for students without local Python setup

## Course Content by Theme

The course is organized around core seismological concepts, with notebooks progressing from data fundamentals through wave theory to advanced applications.

### Module 1: Data Foundations and Signal Processing
**Learning Goal**: Master seismic data acquisition and spectral analysis techniques

- **[01_Data_Fourier_Practice.ipynb](notebooks/01_Data_Fourier_Practice.ipynb)** (Week 1, ~3 hrs)
  - Shearer Chapter 3
  - Downloading seismic data from IRIS/FDSN using ObsPy
  - Instrument response removal and calibration
  - Fourier analysis and filtering techniques
  - Spectral analysis of earthquake signals

### Module 2: Stress, Strain, and Elasticity
**Learning Goal**: Connect elastic wave theory to material deformation

- **Lecture**: [02_Stress_Strain_Lecture.md](lectures/02_Stress_Strain_Lecture.md) (Week 2)
  - Shearer Chapter 2
  - Stress and strain tensors, traction boundary conditions
  - Hooke's Law and elastic constants (Lamé parameters)
  - P and S wave velocities from material properties
  - Real-world geodetic examples (1992 Landers earthquake, Pinon Flat Observatory)

- **[02_Stress_Strain_Practice.ipynb](notebooks/02_Stress_Strain_Practice.ipynb)** (Week 2, ~3 hrs)
  - Eigenvalue analysis of stress/strain tensors
  - Principal stress directions and magnitudes
  - Computational implementation of elastic relationships
  - Strain accumulation from borehole strainmeter data

### Module 3: Body Waves and Ray Theory
**Learning Goal**: Understand P and S wave propagation through Earth structure using ray theory

- **Lecture**: [ray-theory.md](lectures/ray-theory.md) (Week 3)
  - Shearer Chapter 4.1-4.2
  - Snell's law, ray parameter, and fermat's principle
  - Ray bending in velocity gradients
  - Travel-time curves and turning depths

- **[03a_Body_Waves_Theory.ipynb](notebooks/03a_Body_Waves_Theory.ipynb)** (Week 3, ~2 hrs)
  - Shearer Chapter 3
  - P/S wave separation using polarization analysis
  - Covariance matrix eigendecomposition for rectilinearity
  - Particle motion visualization in Z-R-T coordinates
  - Helmholtz decomposition (divergence and curl)

- **[03b_Ray_Tracing_Cartesian_Practice.ipynb](notebooks/03b_Ray_Tracing_Cartesian_Practice.ipynb)** (Week 3-4, ~3 hrs)
  - Shearer Chapter 4
  - 2D ray tracing in Cartesian coordinates using PyKonal
  - Eikonal equation solver for travel-time fields
  - Curved layers, low-velocity zones, and ray focusing
  - Travel-time residuals from structure vs source location errors

- **[03c_Ray_Tracing_Global_Practice.ipynb](notebooks/03c_Ray_Tracing_Global_Practice.ipynb)** (Week 4, ~2 hrs)
  - Shearer Chapters 4-5
  - Spherical Earth models (iasp91, PREM)
  - TauP toolkit for global ray tracing
  - Ray geometry in 2D/3D through Earth's interior

- **[03d_Global_Phases_Practice.ipynb](notebooks/03d_Global_Phases_Practice.ipynb)** (Week 4, ~3 hrs)
  - Shearer Chapters 4-5
  - Body wave phase identification (P, S, PcP, ScS, PKP, SKS, etc.)
  - Travel-time predictions with TauP
  - Real earthquake data analysis and phase picking

### Module 4: Reflection Seismology
**Learning Goal**: Understand wave reflection/transmission and exploration seismology methods

- **[04a_Reflection_Coefficients_Theory.ipynb](notebooks/04a_Reflection_Coefficients_Theory.ipynb)** (Week 5, ~2 hrs)
  - Shearer Chapter 5.4
  - SH and P-SV reflection and transmission coefficients
  - Post-critical incidence and total internal reflection
  - Complex coefficients and attenuation

- **[04b_Reflection_CMP_Practice.ipynb](notebooks/04b_Reflection_CMP_Practice.ipynb)** (Week 5, ~1 hr)
  - Reflection seismology basics
  - Common midpoint (CMP) gathers
  - Normal moveout (NMO) correction and stacking
  - Point diffractor migration
  - 20-minute toy demonstration

### Module 5: Surface Waves
**Learning Goal**: Analyze dispersive surface wave propagation and Earth structure

- **Lecture**: [surface-waves.md](lectures/surface-waves.md) (Week 6)
  - Shearer Chapter 7
  - Rayleigh and Love wave theory
  - Derivation of dispersion relations
  - Particle motion characteristics (retrograde elliptical for Rayleigh, horizontal for Love)
  - Practical workflow connecting theory to lab exercises

- **[05a_Rayleigh_Waves_Theory.ipynb](notebooks/05a_Rayleigh_Waves_Theory.ipynb)** (Week 6, ~2 hrs)
  - Shearer Chapter 7
  - Rayleigh wave boundary value problem in half-space
  - Numerical solution of dispersion equation
  - Particle motion (retrograde elliptical)
  - Depth sensitivity kernels

- **[05b_Love_Waves_Theory.ipynb](notebooks/05b_Love_Waves_Theory.ipynb)** (Week 6, ~2 hrs)
  - Shearer Chapter 7
  - Love wave theory: SH-guided waves in layered media
  - Layer-over-halfspace dispersion curves
  - Eigenfunctions and particle motion
  - Comparison with Rayleigh waves

- **[05c_Surface_Waves_Practice.ipynb](notebooks/05c_Surface_Waves_Practice.ipynb)** (Week 7, ~4 hrs)
  - Shearer Chapter 7
  - Group velocity vs. phase velocity measurement
  - Dispersion curve extraction from real earthquake data
  - Multiple-filter technique (MFT)
  - Inverting dispersion for 1D velocity structure
  - Comprehensive theory introduction and practical workflow

- **[05d_Noise_CrossCorrelation_Practice.ipynb](notebooks/05d_Noise_CrossCorrelation_Practice.ipynb)** (Week 7, ~3 hrs)
  - Shearer Chapter 9, Lawrence & Denolle (2013)
  - Ambient noise seismology fundamentals
  - Noise cross-correlation for Green's function extraction
  - Virtual source concept and reciprocity
  - Surface wave extraction from ambient noise

### Optional - Advanced Topics
**For interested students or advanced graduate work**

- **Lecture**: [tomography-lecture-whiteboard.md](lectures/tomography-lecture-whiteboard.md)
  - Ray-based inverse problems and regularization
  - Travel-time tomography theory
  - Resolution matrices and checkerboard tests
  - Damping vs smoothness regularization

- **[travel_time_tomography_iterative_pykonal.ipynb](notebooks/travel_time_tomography_iterative_pykonal.ipynb)** (~5 hrs)
  - Travel-time tomography: straight rays → iterative bent rays
  - PyKonal eikonal solver for curved rays
  - Resolution tests (checkerboard patterns)
  - Regularization parameter selection

- **[toy_surface_wave_inversion.ipynb](notebooks/toy_surface_wave_inversion.ipynb)** (~4 hrs)
  - End-to-end surface wave inversion workflow
  - F-K spectrum analysis → dispersion curve measurement
  - Love wave forward solver for 1D shear velocity structure
  - Synthetic tests and real data application

### Assessment
- **[Midterm_Integrated_Assignment.ipynb](notebooks/Midterm_Integrated_Assignment.ipynb)** (Week 5, ~8-10 hrs)
  - Comprehensive midterm examination
  - Part 1: Ray theory and travel-time curves
  - Part 2: Surface wave dispersion from real data
  - Part 3: Travel-time tomography (straight and curved rays with PyKonal)
  - Integrates observation → theory → inverse problem workflow
  - Resolution analysis and quality metrics

## Lecture Notes and Teaching Materials

The `lectures/` directory contains focused teaching materials designed for efficient knowledge transfer:

### Available Lecture Notes

- **[02_Stress_Strain_Lecture.md](lectures/02_Stress_Strain_Lecture.md)**:
  - 15-20 minute lecture on elastic wave fundamentals
  - Comprehensive coverage: stress/strain tensors, Hooke's Law, wave speeds
  - Real-world geodetic examples (Pinon Flat Observatory, 1992 Landers earthquake)
  - Worked numerical examples with physical units
  - Designed for pre-class reading (flipped classroom) or live presentation

- **[surface-waves.md](lectures/surface-waves.md)**:
  - Rayleigh and Love wave theory in one place
  - Dispersion relations and derivations with LaTeX equations
  - Particle motion characteristics
  - Workflow connecting theory to Labs 4–6
  - Avoids duplication between theory and practicum notebooks

### Graduate Student Resources

- **[Graduate_Paper_Presentation.md](lectures/Graduate_Paper_Presentation.md)**:
  - ESS 512 only: How to prepare a research paper presentation
  - Selecting papers that connect course methods to published research
  - Presentation structure and best practices
  - Critical evaluation of methodology
  - Rubric and expectations

### Using Lecture Materials

**Lecture notes** provide:
- Compact theoretical foundations before computational work
- Real-world seismological context
- Mathematical derivations with physical interpretation
- Bridge between textbook reading and hands-on exercises
- Flexibility: Use as pre-class reading, live lecture, or reference material

## Course Schedule

### Typical 10-Week Quarter Progression

| Week | Theme | Materials | Topics |
|------|-------|-----------|--------|
| 1 | Data Foundations | 01 | FDSN data access, ObsPy, instrument response, Fourier analysis, filtering |
| 2 | Stress & Strain | Lecture 02, 02 Practice | Elastic constants, stress/strain tensors, Hooke's Law, eigenvalue analysis |
| 3 | Body Waves I | Lecture Ray Theory, 03a, 03b | P/S polarization, rectilinearity, 2D ray tracing with PyKonal |
| 4 | Body Waves II | 03c, 03d | TauP toolkit, spherical Earth models, global phase identification |
| 5 | Reflection & Midterm | 04a, 04b, Midterm | Reflection coefficients, CMP/NMO, begin integrated assignment |
| 6 | Surface Waves I | Lecture Surface Waves, 05a, 05b | Rayleigh/Love theory, dispersion curves, eigenfunctions |
| 7 | Surface Waves II | 05c, 05d | Dispersion measurement, MFT, ambient noise cross-correlation |
| 8 | Advanced Topics | Optional notebooks | Tomography, surface wave inversion (as time permits) |
| 9-10 | Synthesis | Presentations | ESS 512: Research paper presentations |

### Prerequisites by Notebook

- **01 Data**: None (foundational - start here)
- **02 Stress/Strain**: 01 recommended (for data handling context)
- **03a-d Body Waves**: 01 (Fourier analysis), 02 (wave propagation theory)
- **04a-b Reflection**: 03 (ray theory for reflection angles)
- **05a-d Surface Waves**: 01 (spectral analysis), surface-waves lecture (theory)
- **Midterm**: 01, 03b-d (ray tracing), 05c (dispersion fundamentals)
- **Advanced**: All core modules completed

## ESS 412 vs ESS 512 Differentiation

### Undergraduate (ESS 412)
- Complete core exercises in each notebook (typically 3-4 questions)
- Use provided functions and code templates
- Focus on interpretation and physical understanding
- Single event/station analysis
- **Estimated time**: 4-6 hours per week on computational exercises

### Graduate (ESS 512)
- Complete all ESS 412 exercises **plus** additional graduate questions (5-7 total)
- Implement algorithms from scratch where specified
- Statistical analysis across multiple events/stations
- Error propagation and uncertainty quantification
- Literature connection exercises
- **Paper presentation**: One research paper connecting computational methods to published work
- Optional: Computer Programs in Seismology (CPS) integration for surface waves
- **Estimated time**: 6-9 hours per week on computational exercises + paper preparation

### Graduate Paper Presentation Component

ESS 512 students will present one published research paper (distributed throughout semester) that demonstrates:
- Application of methods learned in class to real research problems
- Publication best practices (reproducible code, clear figures, method documentation)
- Critical evaluation of methodology and results

See [lectures/Graduate_Paper_Presentation.md](lectures/Graduate_Paper_Presentation.md) for complete guidelines, rubric, and presentation expectations.

## Key Dependencies

- **Python** ≥3.9
- **ObsPy** ≥1.4 - Seismological data processing
- **NumPy** ≥1.20 - Numerical computations
- **Matplotlib** ≥3.5 - Visualization
- **Cartopy** ≥0.20 - Map projections
- **SciPy** ≥1.7 - Signal processing

See [environment.yml](environment.yml) or [pixi.toml](pixi.toml) for complete dependency list.

## Data Sources

All exercises use real seismic data from:
- **IRIS DMC** (Incorporated Research Institutions for Seismology Data Management Center)
- **SCEDC** (Southern California Earthquake Data Center)
- Accessed via ObsPy's FDSN client

No authentication required for course exercises. All data downloads are automated within notebooks.

## References & Citations

The book uses a shared BibTeX bibliography stored in [`references.bib`](references.bib).
[sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/) renders the
citations when the Jupyter Book is built.

### How to add a new reference

1. Open `references.bib` and add a standard BibTeX entry (keep entries sorted alphabetically by cite key).
2. Choose a cite key of the form `AuthorYear` or `AuthorAuthorYear`, e.g. `Shearer2009`, `HanksKanamori1979`.

### How to cite in Markdown / notebooks

In any **MyST Markdown** (`.md`) file or **Jupyter notebook Markdown cell**, use:

| Syntax | Rendered as |
|--------|-------------|
| `` {cite}`Shearer2009` `` | Inline citation (e.g., [1]) |
| `` {cite:p}`Shearer2009` `` | Parenthetical — (Shearer, 2009) |
| `` {cite:t}`Shearer2009` `` | Textual — Shearer (2009) |
| `` {cite}`Shearer2009,AkiRichards2002` `` | Multiple citations |

### How to print a bibliography on a page

Add the following at the bottom of any `.md` lecture or notebook Markdown cell:

````markdown
## References

```{bibliography}
:filter: docname in docnames
```
````

The `:filter: docname in docnames` directive prints only the references that were
actually cited on that page.  To print the full bibliography, omit the filter line.

### Quick example

```markdown
Shearer {cite:p}`Shearer2009` provides an excellent introduction.

## References

```{bibliography}
:filter: docname in docnames
```
```

## Contributing

This is an evolving course repository. Suggestions and contributions are welcome:
- Open an issue for bugs or unclear instructions
- Submit pull requests for improvements
- Graduate students: Share interesting research papers for future presentation options

## Acknowledgments

- Course structure based on Peter Shearer's **"Introduction to Seismology"** (Cambridge University Press)
- Some exercises adapted from Heiner Igel's computational seismology materials
- Built with [ObsPy](https://obspy.org/) - the seismological Python framework
- Seismic data provided by [IRIS DMC](http://ds.iris.edu/ds/)

## License

This work is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Contact

**Instructor**: Marine Denolle
**Course**: ESS 412/512, University of Washington
**Repository**: https://github.com/uw-geophysics-edu/ess-412-512-intro2seismology

For course-related questions, use Canvas discussion board. For repository issues, use GitHub Issues.

---

**Last Updated**: January 2026
