# Graduate Paper Presentation & Best Practices Guide

**ESS 512 - Introduction to Seismology**  
**Graduate Component**

---

## Overview

Graduate students (ESS 512) are required to present **one research paper** that demonstrates the application of computational methods learned in this course to real seismological research. This assignment develops critical skills in:

- Reading and understanding research literature
- Evaluating methodology and reproducibility
- Scientific communication
- Connecting theory to practice

**Weight**: 15% of final grade  
**Format**: 15-minute presentation + 5 minutes Q&A  
**Distributed throughout**: Weeks 5-9 (one student per week)

---

## Learning Objectives

By completing this assignment, you will:

1. **Connect coursework to research**: Understand how methods from our computational labs are used in published research
2. **Critical evaluation**: Assess the strengths and limitations of computational methods in real applications
3. **Reproducibility**: Evaluate whether the research could be reproduced from the information provided
4. **Communication**: Present complex technical material clearly to peers
5. **Best practices**: Learn standards for publication-quality figures, code documentation, and method description

---

## Paper Selection Guidelines

### Approved Topics

Your paper should connect to at least one of our computational modules:

| Module | Example Research Topics |
|--------|------------------------|
| **Ray Tracing & Travel Times** | Earthquake location algorithms, seismic tomography methods, phase identification |
| **Surface Waves** | Regional dispersion analysis, ambient noise tomography, crustal thickness studies |
| **Fourier Analysis** | Spectral analysis methods, attenuation (Q) measurement, time-frequency analysis |
| **Data Processing** | Network processing, data quality metrics, instrument response |
| **Noise Cross-Correlation** | Green's function extraction, velocity monitoring, noise sources |

### Selection Criteria

**Your paper should:**
- Be published in a peer-reviewed journal (last 10 years preferred)
- Include computational seismology methods
- Have clear methodology section
- Include code/data availability statement (bonus)
- Be accessible through UW Libraries

**Good Journals:**
- Seismological Research Letters (SRL)
- Bulletin of the Seismological Society of America (BSSA)
- Geophysical Journal International (GJI)
- Journal of Geophysical Research: Solid Earth (JGR)
- Geophysical Research Letters (GRL)
- Earth and Planetary Science Letters (EPSL)

### Paper Approval Process

1. **Week 3**: Submit 3 paper candidates to instructor via email
   - Include full citations
   - Brief (2-3 sentence) description of why each interests you
   - Which computational module(s) it connects to

2. **Week 4**: Instructor approves paper and assigns presentation week

3. **One week before presentation**: Send slides to instructor for feedback

---

## Presentation Structure

### Time Allocation (15 minutes total)

- **Introduction** (2 min): Scientific motivation and research question
- **Data & Methods** (5 min): **FOCUS HERE** - Computational approach, algorithms, processing
- **Results** (4 min): Key findings
- **Discussion & Critical Evaluation** (3 min): Strengths, limitations, reproducibility
- **Conclusion** (1 min): Main takeaway and connection to course

### Required Content

Your presentation **must** include:

#### 1. Research Context (Brief)
- What is the scientific question?
- Why does it matter?
- What was previously unknown?

#### 2. Data Description
- What seismic data was used? (Network, stations, events, time period)
- Data quality considerations
- How was data accessed/processed?

#### 3. Computational Methods (CORE - spend most time here)
- Algorithm(s) used - explain in detail
- Processing workflow (flowchart helpful)
- Key parameters and their selection
- How does this connect to methods we learned in class?
- What software/tools were used?

#### 4. Results
- Main findings (select 2-3 key figures)
- Uncertainty/error analysis
- Validation approach

#### 5. Critical Evaluation
- **Reproducibility Assessment**:
  - Is code/data available?
  - Could you reproduce the results from the paper?
  - What information is missing?
  
- **Methodological Strengths**:
  - What did they do well?
  - Novel aspects?
  
- **Limitations**:
  - Assumptions that may not hold?
  - Alternative approaches?
  - How could methods be improved?

#### 6. Connection to Course
- Which notebook(s) relate to this work?
- What extensions could we implement in class?
- What did you learn that enhances your understanding of course material?

---

## Publication Best Practices Analysis

As part of your presentation, evaluate the paper against modern publication standards:

### 1. Reproducibility Checklist

Assess whether the paper includes:

- [ ] **Code Availability**: Link to GitHub, Zenodo, or supplementary materials
- [ ] **Data Availability**: DOI or permanent archive link  
- [ ] **Software Versions**: Specific versions of tools used (e.g., ObsPy 1.4.0)
- [ ] **Parameter Documentation**: All processing parameters clearly stated
- [ ] **Workflow Description**: Step-by-step processing flow
- [ ] **Random Seed**: If applicable (for MC methods, inversions)

**Rate**: Poor / Fair / Good / Excellent

### 2. Figure Quality Assessment

Evaluate the main computational figure (choose one):

- [ ] **Axes Labels**: Clear, with units
- [ ] **Colorbar**: If applicable, with label and units
- [ ] **Font Size**: Readable when printed
- [ ] **Caption**: Self-contained (can understand without reading text)
- [ ] **Error Bars**: Shown where appropriate
- [ ] **Legend**: Clear identification of all elements
- [ ] **File Format**: Vector (PDF/SVG) for line plots?

**Example of Excellent Practice**: Include a screenshot showing good vs bad

### 3. Method Documentation

Evaluate the methods section:

- [ ] **Algorithm Description**: Mathematical formulation included
- [ ] **Pseudocode/Flowchart**: If complex algorithm
- [ ] **Trade-offs Discussed**: Why this method over alternatives?
- [ ] **Failure Cases**: When does the method fail?
- [ ] **Computational Cost**: Runtime, memory requirements mentioned
- [ ] **Validation**: Synthetic tests or comparison with known results

**Rate**: Poor / Fair / Good / Excellent

### 4. Open Science Practices

Does the paper follow open science principles?

- **Open Access**: Is the paper freely available?
- **Open Data**: Are datasets in public archives (IRIS, etc.)?
- **Open Source**: Is code freely available?
- **Permissive License**: MIT, BSD, GPL, or similar?
- **Community Standards**: Uses standard formats (SAC, miniSEED)?

**Discuss**: How does this paper compare to ideal open science standards?

---

## Deliverables

### 1. Presentation Slides

**Submit one week before**: PDF of slides to instructor for feedback

**Format Requirements**:
- 12-16 slides maximum (excluding title/references)
- Title slide: Paper citation, your name, date
- Clear slide titles
- Not text-heavy (use figures, diagrams, bullets)
- Readable fonts (≥18pt for body text)
- Final slide: 2-3 discussion questions for class

**Include**:
- At least one slide showing code snippet or algorithm pseudocode
- At least one slide with reproducibility checklist results
- References slide (cite paper + any additional sources)

### 2. One-Page Summary

**Due day of presentation**

**Content**:
- Paper citation
- 3-4 sentence summary of paper
- Key computational method(s) used
- Reproducibility score (1-5) with justification
- Connection to course module(s)
- One limitation or improvement you would suggest
- One question for further investigation

**Format**: PDF, single page

---

## Rubric (100 points total)

### Content (60 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Methods Explanation** | 20 | Clear description of algorithms; connection to course; technical accuracy |
| **Critical Evaluation** | 15 | Thoughtful assessment of reproducibility, strengths, and limitations |
| **Scientific Context** | 10 | Motivation clear; results summarized appropriately |
| **Best Practices Analysis** | 15 | Thorough evaluation of code/data availability, figures, documentation |

### Presentation Skills (25 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Clarity** | 10 | Logical flow; concepts explained clearly; appropriate level for audience |
| **Time Management** | 5 | Stays within 15 minutes; appropriate pacing |
| **Slides** | 5 | Readable, well-organized, good visuals |
| **Q&A Response** | 5 | Thoughtful answers; admits uncertainty appropriately |

### Written Summary (15 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Completeness** | 10 | All required elements included; accurate summary |
| **Writing Quality** | 5 | Clear, concise, professional |

---

## Example Papers (as inspiration)

### Surface Waves & Ambient Noise
- Bensen et al. (2007). "Processing seismic ambient noise data to obtain reliable broad-band surface wave dispersion measurements." *GJI* 169(3), 1239-1260.
  - **Why good**: Extremely detailed methods; became community standard
  
- Lin et al. (2008). "Surface wave tomography of the western United States from ambient seismic noise: Rayleigh and Love wave phase velocity maps." *GJI* 173(1), 281-298.
  - **Why good**: Clear workflow; connects noise to structure

### Ray Tracing & Tomography
- VanDecar & Crosson (1990). "Determination of teleseismic relative phase arrival times using multi-channel cross-correlation and least squares." *BSSA* 80(1), 150-169.
  - **Why good**: Algorithm details; widely used method

- Rawlinson & Sambridge (2004). "Wave front evolution in strongly heterogeneous layered media using the fast marching method." *GJI* 156(3), 631-647.
  - **Why good**: Clear algorithm description; synthetic tests

### Fourier Analysis & Attenuation
- Lawrence & Prieto (2011). "Attenuation tomography of the western United States from ambient seismic noise." *JGR* 116(B6).
  - **Why good**: Combines several methods; good validation

### Data Quality
- Ringler et al. (2015). "Seismic station installation orientation errors at ANSS and IRIS/USGS stations." *SRL* 86(3), 926-931.
  - **Why good**: Practical problem; straightforward analysis

---

## Tips for Success

### Reading the Paper

1. **First pass**: Skim for main idea (10 min)
   - Abstract, figures, conclusions
   - Identify computational methods

2. **Second pass**: Read in detail (1-2 hours)
   - Methods section carefully
   - Try to understand each figure
   - Look up unfamiliar terms/methods

3. **Third pass**: Critical reading (1 hour)
   - Could you reproduce this?
   - What's not explained?
   - Are conclusions justified?

### Preparing Presentation

1. **Start with methods**: Build presentation around computational approach
2. **Use paper's figures**: Okay to screenshot (with citation) - don't recreate
3. **Practice timing**: Rehearse at least twice
4. **Anticipate questions**: Prepare for what classmates might ask
5. **Connect explicitly**: Make course connections obvious

### Common Pitfalls to Avoid

- ❌ Spending too much time on background/introduction
- ❌ Just summarizing results without explaining methods
- ❌ Not evaluating reproducibility
- ❌ Reading dense text from slides
- ❌ Skipping connection to course material
- ❌ Exceeding time limit

### What Makes an Excellent Presentation

- ✅ Clear explanation of algorithms (could we implement it?)
- ✅ Critical but fair evaluation
- ✅ Engaging visuals (flowcharts, diagrams, not just text)
- ✅ Specific examples from the paper
- ✅ Thoughtful discussion questions
- ✅ Explicit course connections

---

## Resources

### Finding Papers

- **Google Scholar**: https://scholar.google.com
- **UW Libraries**: https://www.lib.washington.edu/
- **arXiv Geophysics**: https://arxiv.org/list/physics.geo-ph/recent
- **IRIS Publication Search**: http://ds.iris.edu/ds/publications/

### Evaluating Reproducibility

- **TOP Guidelines**: https://www.cos.io/initiatives/top-guidelines
- **FAIR Principles**: https://www.go-fair.org/fair-principles/
- **Stodden et al. (2016)**: "Enhancing reproducibility for computational methods" *Science* 354(6317), 1240-1241.

### Presentation Skills

- UW Communication Center: https://www.com.washington.edu/
- Ten Simple Rules for Effective Presentation Slides: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009554

---

## Presentation Schedule

Presentations will occur in **Weeks 5-9** (one student per week). Schedule determined after paper approval.

| Week | Date | Student | Paper Topic | Connection |
|------|------|---------|-------------|------------|
| 5 | TBD | Student 1 | TBD | TBD |
| 6 | TBD | Student 2 | TBD | TBD |
| 7 | TBD | Student 3 | TBD | TBD |
| 8 | TBD | Student 4 | TBD | TBD |
| 9 | TBD | Student 5 | TBD | TBD |

---

## Questions?

Contact instructor during office hours or via email. Start early - finding the right paper and understanding it deeply takes time!

---

**Last Updated**: January 2026
