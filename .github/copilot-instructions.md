# Copilot Instructions — ESS 412/512 Introduction to Seismology

## Project Overview

This is a **Jupyter Book** course site for **ESS 412/512: Introduction to Seismology** at the University of Washington, taught by Marine Denolle. The primary textbook is Peter Shearer's *Introduction to Seismology* (2nd ed. 2009, 3rd ed. 2019). The book is deployed to GitHub Pages via CI.

- **GitHub org**: `UW-geophysics-edu`
- **Repo**: `ess-412-512-intro2seismology`
- **Branch**: `main`
- **Site**: <https://uw-geophysics-edu.github.io/ess-412-512-intro2seismology/>
- **Package manager**: Pixi (preferred) or Conda
- **Python**: 3.11

The course has two tiers:
- **ESS 412** (undergraduate): Core exercises and theory
- **ESS 512** (graduate): Additional analytical depth, literature connections, and paper presentations

---

## Agent Division of Labor

This repository is maintained with **two AI agents** that have complementary roles:

### ChatGPT (PDF & pedagogy agent)
- Parse PDFs of scientific papers and textbook chapters
- Extract key equations, derivations, and concepts for lectures
- Suggest pedagogical framing and exercise design
- Review scientific accuracy of content drafts
- Summarize research papers for graduate reading lists

### GitHub Copilot (this agent — code & markdown editor)
- Edit MyST Markdown lectures and notebook markdown cells
- Write and debug Python code in Jupyter notebooks
- Manage `references.bib` — add entries, verify DOIs, fix metadata
- Run pre-commit hooks and fix validation failures
- Create, refactor, and restructure notebooks
- Maintain build infrastructure (`_config.yml`, `_toc.yml`, `pixi.toml`)
- Generate figures and visualization code

**Typical workflow**: ChatGPT parses a Shearer chapter PDF → produces a content outline with key equations → Copilot implements it as a MyST lecture file or Jupyter notebook, adds proper citations, and validates the build.

---

## File Organization

```
notebooks/          Jupyter notebooks — main student-facing content
lectures/           MyST Markdown lecture notes
  scripts/figures/  Generated lecture figures
solutions/          Instructor solutions (selectively tracked)
scripts/            Validation and maintenance scripts
references.bib      Shared BibTeX bibliography
_toc.yml            Table of contents (defines book structure)
_config.yml         Jupyter Book configuration
pixi.toml           Pixi tasks and dependencies
environment.yml     Conda environment specification
.pre-commit-config.yaml  Pre-commit hook definitions
```

---

## Citation & Reference Management

### Bibliography file: `references.bib`

All references live in a single `references.bib` at the repo root. Entries are organized by category with comment headers:

```bibtex
% ---- Textbooks -----------------------------------------------------------
% ---- Magnitude scales ----------------------------------------------------
% ---- Source mechanics ----------------------------------------------------
% ---- Moment tensors ------------------------------------------------------
% ---- Ambient noise -------------------------------------------------------
% ---- Magnitude calibration studies ---------------------------------------
% ---- Software ------------------------------------------------------------
```

### Cite key convention

Use `AuthorYear` or `AuthorAuthorYear` format:
- Single author: `Kanamori1977`
- Two authors: `HanksKanamori1979`
- Three+ authors: `DostEdwardsBommer2018` (first author + key coauthors)
- Software: `ObsPy2010`, `ObsPy2015`

### Required BibTeX fields

Every `@article` entry **must** include: `author`, `title`, `journal`, `volume`, `number`, `pages`, `year`, `doi` (when available). Use `{braces}` to protect capitalization in titles (e.g., `{P}-wave`, `{$M_L$}`).

### MyST citation syntax

In any `.md` or notebook markdown cell:

| Syntax | Renders as |
|---|---|
| `` {cite}`Shearer2009` `` | Inline citation |
| `` {cite:p}`Shearer2009` `` | (Shearer, 2009) |
| `` {cite:t}`Shearer2009` `` | Shearer (2009) |

### Bibliography block

Add at the bottom of any page that uses citations:

````markdown
## References

```{bibliography}
:filter: docname in docnames
```
````

### Shearer textbook references (informal)

For inline Shearer references in pedagogy contexts, use the 📖 convention:

```markdown
📖 *Shearer reference:* Section 9.7, Table 9.1
```

---

## DOI / Reference Verification Skill

When asked to verify references, or when adding new entries to `references.bib`, follow this systematic workflow.

### Step 1 — Inventory

Read `references.bib` and list all entries with their cite keys, DOIs, and basic metadata (title, journal, year).

### Step 2 — DOI resolution check

For each entry that has a DOI:

1. Fetch `https://doi.org/{DOI}` (it redirects to the publisher page)
2. Verify the redirect lands on a legitimate publisher domain:
   - Cambridge University Press → `cambridge.org`
   - GeoScienceWorld (BSSA, SRL) → `pubs.geoscienceworld.org`
   - AGU/Wiley (JGR, GRL) → `agupubs.onlinelibrary.wiley.com`
   - Oxford University Press (GJI) → `academic.oup.com`
   - IOP Publishing → `iopscience.iop.org`
   - Annals of Geophysics → `annalsofgeophysics.eu`
3. If the DOI returns a 404 or redirects to a completely different paper, the entry is **hallucinated** — flag it.

### Step 3 — Metadata cross-check

Compare every field against the publisher page:

- **Title**: Must match exactly (word order matters — e.g., "Source type plot for inversion of the moment tensor" ≠ "Source type plot for moment tensor inversion")
- **Authors**: Check all authors are present and correctly ordered
- **Journal**: Verify exact journal name (common hallucination: BSSA ↔ SRL swap)
- **Volume / Number / Pages**: Must match the publisher metadata
- **Year**: Must match publication year

### Step 4 — Entries without DOIs

For entries without DOIs (historic papers, textbooks):
- Search Google Scholar to confirm the paper exists with the claimed metadata
- If a DOI exists but was omitted, add it

### Step 5 — Fix errors

Apply corrections using the exact metadata from the publisher page. Common hallucination patterns to watch for:

| Pattern | Example |
|---|---|
| Swapped journals | BSSA entry that's actually in SRL (or vice versa) |
| Wrong page ranges | Pages from a different paper in the same issue |
| Altered title wording | Words reordered or synonyms substituted |
| Wrong/extra authors | Author list from a different paper by the same first author |
| DOI from different paper | Valid DOI that resolves to a completely unrelated article |
| Missing coauthors | Only 2 of 4 authors listed |

### Step 6 — Validate

After fixes, run `pre-commit run --all-files` to ensure the bib file passes codespell and formatting checks.

---

## Notebook Conventions

### Naming

```
{Module}{Letter}_{Topic}_{Type}.ipynb

Module: 01-07 (two digits)
Letter: a, b, c, d (sequential within module; omit for single notebooks)
Type:   Theory or Practice
```

Examples: `03a_Body_Waves_Theory.ipynb`, `05c_Surface_Waves_Practice.ipynb`

### Required first markdown cell

Every notebook must start with a Colab badge + title + learning objectives:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UW-geophysics-edu/ess-412-512-intro2seismology/blob/main/notebooks/{NOTEBOOK_NAME}.ipynb)

> **Note:** If running on Colab, uncomment and run the pip install cell below.

# Lab XX: Title Here

## Learning Objectives
- Objective 1
- Objective 2
```

**Critical**: The badge URL must use `UW-geophysics-edu` (capital U, W) and `ess-412-512-intro2seismology`.

### Required sections

1. Title with lab number (`# Lab 3b: Ray Tracing`)
2. Learning Objectives (bullet list)
3. Prerequisites (if any)
4. Estimated completion time
5. Setup / imports cell
6. Numbered content sections (`## 1. Topic`, `## 2. Topic`)
7. ESS 512 graduate extensions (clearly marked)

### Pedagogy pattern

Notebooks follow a **Predict → Do → Explain → Check** cycle:

1. **Predict**: Ask students to hypothesize before running code
2. **Do**: Computational exercise with guided code
3. **Explain**: Interpretation questions in markdown cells
4. **Check**: Validation or comparison with known results

### ESS 412 vs 512 differentiation

Mark graduate-only content with a clear header:

```markdown
## Graduate Extension (ESS 512)

> **ESS 512 students**: Complete the following additional analysis...
```

### Math formatting

- Inline: `$v_p = \sqrt{(\lambda + 2\mu)/\rho}$`
- Display: `$$\boxed{M_0 = \mu \, A \, \bar{D}}$$`
- Use `\boxed{}` for key/important equations students should remember
- Enabled by `dollarmath` + `amsmath` MyST extensions in `_config.yml`

### Code cells

- Use descriptive variable names
- Include docstrings for helper functions
- Add `# comments` explaining physics, not just code mechanics
- Use `matplotlib` for static figures, `plotly` for interactive ones
- Tag cells with `hide-input` for boilerplate setup code

---

## Lecture Markdown Conventions

Lecture files are MyST Markdown (`.md`) in the `lectures/` directory.

### Standard structure

```markdown
# Lecture Title

## Learning objectives
- **Key concept 1**: description
- **Key concept 2**: description

## Context and scope
Connection to Shearer chapters and other modules.

## 1. First Topic
Content...

## 2. Second Topic
Content...

## Check-your-understanding
1. Conceptual question 1?
2. Conceptual question 2?

## What we deliberately did not cover
- Topic A (covered in Module X)
- Topic B (beyond course scope)

## Looking ahead
Preview of the upcoming lab and how it connects.

## Reading
📖 *Shearer:* Chapters X–Y
- Additional references
```

### MyST directives

**Figures**:
````markdown
```{figure} scripts/figures/my_figure.png
---
name: fig-my-figure
alt: Description for accessibility
---
Caption text with {cite}`Reference2024` if needed.
```
````

**Admonitions**:
````markdown
```{note}
Important pedagogical note here.
```

```{warning}
Common misconception or pitfall.
```
````

**Summary tables**: Use standard Markdown tables for comparing related concepts (e.g., magnitude scales, wave types).

---

## Validation & Pre-commit

### Pre-commit hooks (10 total)

The repo has these hooks that run on every commit:

| Hook | What it checks |
|---|---|
| `trailing-whitespace` | No trailing spaces (excludes `.ipynb`) |
| `end-of-file-fixer` | Files end with newline (excludes `.ipynb`) |
| `check-yaml` | Valid YAML syntax |
| `check-json` | Valid JSON in `.ipynb` files |
| `check-added-large-files` | No files > 5 MB |
| `mixed-line-ending` | LF line endings only |
| `codespell` | Spell check (excludes `.ipynb`, `_build/`) |
| `validate-toc` | All `_toc.yml` references point to existing files |
| `check-colab-badges` | Notebooks have correct Colab badge URLs |
| `validate-notebooks` | All `.ipynb` files are valid JSON |

### Running checks

```bash
# Run all hooks
pre-commit run --all-files

# Individual pixi tasks
pixi run validate-toc      # Check _toc.yml
pixi run validate-badges   # Check Colab badges
pixi run spellcheck        # Run codespell
pixi run build-book        # Build the Jupyter Book HTML
pixi run linkcheck         # Verify external links
pixi run validate          # Full validation suite
```

**Always run `pre-commit run --all-files` after making changes.**

### CI pipeline

On push to `main`, GitHub Actions runs:
1. `validate-toc`
2. `validate-badges`
3. `spellcheck`
4. `build-ci` (Jupyter Book build)
5. `linkcheck` (continue-on-error)
6. Deploy to GitHub Pages

---

## Common Pitfalls

| Pitfall | Correct approach |
|---|---|
| Colab badge uses lowercase `uw-geophysics-edu` | Must be `UW-geophysics-edu` (capital U, W) |
| Editing `pixi.lock` directly | Only edit `pixi.toml`; run `pixi install` to regenerate lock |
| Expecting notebooks to execute during build | `_config.yml` has `execute_notebooks: off` — notebooks are rendered as-is |
| Using raw LaTeX in `.md` files | Use `$...$` / `$$...$$` (dollarmath) or `{math}` directive |
| Adding a notebook but not updating `_toc.yml` | Always add new files to `_toc.yml` and run `pixi run validate-toc` |
| Spell-checking notebooks with codespell CLI | codespell skips `.ipynb` — use `python scripts/spellcheck_notebooks.py` instead |
| Creating `@misc` bib entries for journal articles | Always use `@article` with full metadata; `@misc` only for truly non-journal sources |
| Adding references without DOI verification | Every new bib entry must be verified against the publisher page before committing |

---

## Quick Reference: Adding a New Module Notebook

1. Create `notebooks/XX_Topic_Practice.ipynb` following the naming convention
2. Add Colab badge in the first markdown cell
3. Include all required sections (objectives, prerequisites, time estimate)
4. Add the file to `_toc.yml` under the correct module part
5. Add any new references to `references.bib` with verified DOIs
6. Run `pre-commit run --all-files`
7. Build locally: `pixi run build-book`
8. Test in Colab: push branch, click badge, verify it works

## Quick Reference: Adding a New Lecture

1. Create `lectures/topic-name.md` following the lecture structure template
2. Use MyST `{figure}` directives for any figures (store in `lectures/scripts/figures/`)
3. Add citations using `{cite}` syntax and update `references.bib` if needed
4. Include bibliography block at the bottom if citations are used
5. Add the file to `_toc.yml` under the correct module part
6. Run `pre-commit run --all-files`
7. Build locally: `pixi run build-book`
