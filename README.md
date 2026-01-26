# ESS 412/512: Introduction to Seismology

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
├── notebooks/                                    # Computational exercises (numbered in order)
│   ├── 01_Data_FourierTransform.ipynb           # Data handling, Fourier analysis, filtering
│   ├── 02_Stress_and_Strain.ipynb              # Elastic constants, stress/strain relationships
│   ├── 02_Stress_Strain_Test.ipynb             # 50-min in-class exercise (stress/strain)
│   ├── 03_chapter3_wrapup.ipynb                # Body waves analysis and polarization
│   ├── 04_RayleighWaves_Theory.ipynb           # Rayleigh wave theory and derivations
│   ├── 05_SurfaceWaves_Practicum.ipynb         # Surface wave dispersion measurement
│   ├── 06_RayTracing_BodyWaves.ipynb           # Ray theory, travel times, Snell's law
│   ├── 07_Global_Phases.ipynb                  # Body wave phase identification
│   ├── 08_Noise_CrossCorrelation.ipynb         # Ambient noise interferometry
│   └── HWK1_ComputerProgram1_Assignment.ipynb  # Formal graded assignment
├── solutions/                                    # Instructor-only solutions (gitignored)
│   └── 02_Stress_Strain_Solutions.ipynb        # Example solution with rubric
├── lectures/                                     # Lecture notes and teaching materials
│   ├── 02_Stress_Strain_Lecture.md             # Stress/strain lecture notes
│   └── Graduate_Paper_Presentation.md          # ESS 512: Paper presentation guidelines
├── environment.yml                               # Conda environment specification
├── pixi.toml                                     # Pixi configuration (alternative)
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

### First Steps

1. Start with [01_Data_FourierTransform.ipynb](notebooks/01_Data_FourierTransform.ipynb) to learn data handling and signal processing
2. Follow notebooks in numerical order (01 → 08, plus HWK1)
3. Each notebook includes theory, demonstrations, and exercises
4. ESS 512 students should complete additional graduate-level exercises marked in each notebook

## Course Content by Theme

The course is organized around core seismological concepts, with notebooks progressing from data fundamentals through wave theory to advanced applications.

### Module 1: Data Foundations and Signal Processing
**Learning Goal**: Master seismic data acquisition and spectral analysis techniques

- **[01_Data_FourierTransform.ipynb](notebooks/01_Data_FourierTransform.ipynb)** (Week 1)
  - Shearer Chapter 3
  - Downloading seismic data from IRIS/FDSN
  - Instrument response removal
  - Fourier analysis and filtering
  - Spectral analysis of earthquakes

### Module 2: Stress, Strain, and Elasticity
**Learning Goal**: Connect elastic wave theory to material deformation

- **Lecture**: [02_Stress_Strain_Lecture.md](lectures/02_Stress_Strain_Lecture.md) (Week 2)
  - Shearer Chapter 2
  - Stress and strain tensors
  - Hooke's Law and elastic constants
  - Lamé parameters and wave speeds
  - Real-world geodetic examples (1992 Landers earthquake)
  
- **[02_Stress_and_Strain.ipynb](notebooks/02_Stress_and_Strain.ipynb)** (Week 2)
  - Eigenvalue analysis of stress/strain tensors
  - Principal stress directions
  - Computational implementation of elastic relationships
  
- **[02_Stress_Strain_Test.ipynb](notebooks/02_Stress_Strain_Test.ipynb)** (Week 2)
  - 50-minute in-class assessment
  - Tiered difficulty: Parts a-e (ESS 412), Part f (ESS 512)
  - Hand-sketch visualization component
  - **Solution**: [solutions/02_Stress_Strain_Solutions.ipynb](solutions/02_Stress_Strain_Solutions.ipynb)

### Module 3: Body Waves and Ray Theory
**Learning Goal**: Understand P and S wave propagation through Earth structure

- **[03_chapter3_wrapup.ipynb](notebooks/03_chapter3_wrapup.ipynb)** (Week 3)
  - Shearer Chapter 3
  - P/S wave separation using polarization
  - Rectilinearity analysis
  - Particle motion visualization in Z-R-T coordinates
  - Divergence and curl for wave-type identification
  
- **[06_RayTracing_BodyWaves.ipynb](notebooks/06_RayTracing_BodyWaves.ipynb)** (Week 3-4)
  - Shearer Chapter 4
  - Snell's law and ray parameters
  - Travel time curves
  - Ray path computation through layered media
  
- **[07_Global_Phases.ipynb](notebooks/07_Global_Phases.ipynb)** (Week 4)
  - Shearer Chapters 4-5
  - Body wave phase identification (P, S, PcP, ScS, PKP, etc.)
  - TauP toolkit for phase predictions
  - Real data analysis of global earthquakes

### Module 4: Surface Waves
**Learning Goal**: Analyze dispersive surface wave propagation and Earth structure

- **[04_RayleighWaves_Theory.ipynb](notebooks/04_RayleighWaves_Theory.ipynb)** (Week 5)
  - Shearer Chapter 7
  - Rayleigh wave theory and derivations
  - Particle motion (retrograde elliptical)
  - Dispersion relationships
  
- **[05_SurfaceWaves_Practicum.ipynb](notebooks/05_SurfaceWaves_Practicum.ipynb)** (Week 6)
  - Shearer Chapter 7
  - Group velocity vs. phase velocity
  - Dispersion measurement from real data
  - Multiple-filter technique
  - Inverting dispersion for velocity structure

### Module 5: Advanced Methods
**Learning Goal**: Apply modern seismological techniques to ambient noise

- **[08_Noise_CrossCorrelation.ipynb](notebooks/08_Noise_CrossCorrelation.ipynb)** (Week 7)
  - Shearer Chapter 9
  - Ambient noise seismology
  - Cross-correlation and Green's function extraction
  - Virtual source concept
  - Surface wave extraction from noise

### Assessment
- **[HWK1_ComputerProgram1_Assignment.ipynb](notebooks/HWK1_ComputerProgram1_Assignment.ipynb)**
  - Formal graded assignment
  - Integrates concepts from multiple modules
  - Independent data analysis and interpretation

## Lecture Notes and Teaching Materials

The `lectures/` directory contains focused teaching materials designed for efficient knowledge transfer:

### Available Lecture Notes

- **[02_Stress_Strain_Lecture.md](lectures/02_Stress_Strain_Lecture.md)**: 
  - 15-20 minute lecture on elastic wave fundamentals
  - Comprehensive coverage: stress/strain tensors, Hooke's Law, wave speeds
  - Real-world geodetic examples (Pinon Flat Observatory, 1992 Landers earthquake)
  - Worked numerical examples with physical units
  - Designed for pre-class reading (flipped classroom) or live presentation

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
| 1 | Data Foundations | Notebook 01 | FDSN data access, instrument response, Fourier analysis, filtering |
| 2 | Stress & Strain | Lecture 02, Notebooks 02, Test 02 | Elastic constants, stress/strain tensors, Hooke's Law, eigenvalue analysis |
| 3 | Body Waves I | Notebook 03 | P/S separation, polarization, rectilinearity, particle motion |
| 4 | Body Waves II | Notebooks 06-07 | Ray tracing, travel times, global phases, TauP toolkit |
| 5 | Surface Waves I | Notebook 04 | Rayleigh wave theory, dispersion, particle motion |
| 6 | Surface Waves II | Notebook 05 | Group/phase velocity, dispersion measurement, inversion |
| 7 | Advanced Methods | Notebook 08 | Ambient noise, cross-correlation, Green's functions |
| 8 | Integration | HWK1 | Comprehensive assignment applying multiple methods |
| 9-10 | Synthesis | Student projects/presentations | ESS 512: Research paper presentations |

### Prerequisites by Notebook

- **01**: None (foundational - start here)
- **02**: 01 recommended (for data handling context)
- **03**: 01 (Fourier analysis), 02 (wave propagation theory)
- **04**: 01 (spectral analysis critical)
- **05**: 01, 04 (builds on dispersion theory)
- **06**: 01, 02, 03 (ray theory after wave fundamentals)
- **07**: 01, 06 (uses ray tracing and TauP)
- **08**: 01, 05 (cross-correlation builds on filtering/dispersion)
- **HWK1**: 01, 06, 07 (integrative assignment)

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
**Repository**: https://github.com/marinedenolle/ess-412-512-intro2seismology

For course-related questions, use Canvas discussion board. For repository issues, use GitHub Issues.

---

**Last Updated**: January 2026
