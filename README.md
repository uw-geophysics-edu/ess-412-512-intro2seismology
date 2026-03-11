# ESS 412/512: Introduction to Seismology

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy Jupyter Book](https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology/actions/workflows/deploy-book.yml/badge.svg)](https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology/actions/workflows/deploy-book.yml)

Computational labs and lectures for **ESS 412** (undergraduate) and **ESS 512** (graduate) seismology at the University of Washington by Marine Denolle. Materials supplement Peter Shearer's *Introduction to Seismology* with hands-on Python exercises using real seismic data.

**📖 Course site:** <https://uw-geophysics-edu.github.io/ess-412-512-intro2seismology/>

## Course Modules

| Module | Lecture | Labs | Topics |
|--------|---------|------|--------|
| 1 — Data Foundations | — | 01 | FDSN data access, ObsPy, Fourier analysis, filtering |
| 2 — Stress & Strain | [Stress & Strain](lectures/02_Stress_Strain_Lecture.md) | 02 | Elastic constants, stress/strain tensors, Hooke's Law |
| 3 — Body Waves | [Ray Theory](lectures/ray-theory.md) | 03a–c | P/S polarization, ray tracing (PyKonal), global phases (TauP) |
| 4 — Reflection | — | 04a–b | Reflection/transmission coefficients, CMP, NMO, migration |
| 5 — Surface Waves | [Surface Waves](lectures/surface-waves.md) | 05a–d | Rayleigh & Love waves, dispersion, ambient noise |
| 6 — Earthquake Sources | [Inverse Problem](lectures/earthquake-location.md) | 06a | Earthquake location methods & uncertainties |
| 7 — Moment Tensors & Magnitudes | [Moment Tensors](lectures/moment-tensor.md), [Radiation Patterns](lectures/07b-radiation-patterns.md), [Magnitudes](lectures/07c-magnitudes.md) | 07a–d | Moment tensor decomposition, radiation patterns, magnitude scales |
| Optional | [Tomography](lectures/tomography-lecture-whiteboard.md) | — | Travel-time tomography, surface wave inversion |

Each notebook includes a Colab badge — click it to run in Google Colab with no local setup.

## Quick Start

See [INSTALL.md](INSTALL.md) for full setup details.

```bash
# Option 1: Conda
git clone https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology.git
cd ess-412-512-intro2seismology
conda env create -f environment.yml
conda activate ess412

# Option 2: Pixi (preferred for development)
pixi install
```

## Repository Structure

```
notebooks/          Jupyter labs (01–07, named {Module}_{Topic}_{Type}.ipynb)
lectures/           MyST Markdown lecture notes
homework/           Assignments (midterm)
solutions/          Instructor solutions
scripts/            Validation & maintenance scripts
references.bib      Shared BibTeX bibliography
_toc.yml            Table of contents
_config.yml         Jupyter Book configuration
pixi.toml           Pixi tasks & dependencies
environment.yml     Conda environment
```

## ESS 412 vs 512

- **ESS 412**: Core exercises, provided code templates, physical interpretation
- **ESS 512**: Additional analytical depth, implement algorithms from scratch, literature connections, [paper presentation](lectures/Graduate_Paper_Presentation.md)

Graduate-only sections are clearly marked in each notebook.

## References & Citations

All references live in [`references.bib`](references.bib). Cite in MyST Markdown with:

```markdown
{cite:t}`Shearer2009`            → Shearer (2009)
{cite:p}`Shearer2009`            → (Shearer, 2009)
{cite}`Shearer2009,AkiRichards2002`  → multiple
```

Add a bibliography block at the bottom of any page that uses citations:

````markdown
```{bibliography}
:filter: docname in docnames
```
````

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for notebook conventions, naming, and validation steps. Quick checklist:

1. Follow the naming convention: `{Module}{Letter}_{Topic}_{Type}.ipynb`
2. Add a Colab badge in the first cell (URL must use `UW-geophysics-edu`)
3. Update `_toc.yml` if adding a new file
4. Run `pre-commit run --all-files` before committing

## Acknowledgments

- Course structure based on Peter Shearer's *Introduction to Seismology* (Cambridge University Press)
- Built with [ObsPy](https://obspy.org/), [Jupyter Book](https://jupyterbook.org/), and [sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/)
- Seismic data from [Earthscope Consortium](https://www.earthscope.org/) via FDSN web services

## License

MIT — see [LICENSE](LICENSE).

## Contact

**Instructor**: Marine Denolle · ESS 412/512, University of Washington
**Repo**: <https://github.com/UW-geophysics-edu/ess-412-512-intro2seismology>
