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
├── notebooks/
│   ├── 01_Data_FourierTransform.ipynb           # Data handling, Fourier analysis, filtering
│   ├── 02_Stress_and_Strain.ipynb              # Elastic constants, stress/strain relationships
│   ├── 03_RayTracing_BodyWaves.ipynb            # Ray theory, travel times
│   ├── 04_Global_Phases.ipynb                   # Body wave identification
│   ├── 05_SurfaceWaves_Theory_Analysis.ipynb    # Surface waves, dispersion
│   ├── 06_Noise_CrossCorrelation.ipynb          # Ambient noise methods
│   ├── 07_ComputerProgram1_Assignment.ipynb     # Formal graded assignment
│   └── solutions/                                # Instructor solutions (private)
├── environment.yml                               # Conda environment
├── pixi.toml                                     # Pixi configuration (alternative)
├── INSTALL.md                                    # Detailed setup instructions
├── LICENSE
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
2. Follow notebooks in numerical order (01 → 07)
3. Each notebook includes theory, demonstrations, and exercises
4. ESS 512 students should complete additional graduate-level exercises marked in each notebook

## Course Schedule

### Weekly Progression (10-week quarter)

| Week | Shearer Ch. | Notebook(s) | Topics |
|------|------------|-------------|--------|
| 1 | 3 | [01_Data_FourierTransform.ipynb](notebooks/01_Data_FourierTransform.ipynb) | Seismic data access, instrument response, Fourier analysis, filtering |
| 2 | 2 | [02_Stress_and_Strain.ipynb](notebooks/02_Stress_and_Strain.ipynb) | Elastic constants, stress-strain relationships, Lamé parameters |
| 3 | 4 | [03_RayTracing_BodyWaves.ipynb](notebooks/03_RayTracing_BodyWaves.ipynb) | Ray parameter, travel time curves, Snell's law |
| 4 | 4-5 | [04_Global_Phases.ipynb](notebooks/04_Global_Phases.ipynb), [07_ComputerProgram1_Assignment.ipynb](notebooks/07_ComputerProgram1_Assignment.ipynb) | Phase identification, real data analysis, TauP |
| 5 | 7 | [05_SurfaceWaves_Theory_Analysis.ipynb](notebooks/05_SurfaceWaves_Theory_Analysis.ipynb) (Part 1) | Love waves, Rayleigh waves, dispersion theory |
| 6 | 7 | [05_SurfaceWaves_Theory_Analysis.ipynb](notebooks/05_SurfaceWaves_Theory_Analysis.ipynb) (Part 2) | Group velocity, phase velocity, dispersion measurement |
| 7 | 9 | [06_Noise_CrossCorrelation.ipynb](notebooks/06_Noise_CrossCorrelation.ipynb) | Ambient noise, virtual sources, Green's function extraction |
| 8 | Various | Student projects | Application to real problems |
| 9-10 | - | Final projects | ESS 512: Paper presentations |

### Prerequisites by Notebook

- **01**: None (start here - foundational data skills)
- **02**: 01 recommended (for working with seismic data)
- **03**: 01, 02
- **04**: 01, 03
- **05**: 01 (Fourier analysis is critical), 03 (contrast with ray theory)
- **06**: 01, 05
- **07**: 01, 03, 04

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

See [notebooks/solutions/Graduate_Paper_Presentation.md](notebooks/solutions/Graduate_Paper_Presentation.md) for guidelines and rubric.

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
