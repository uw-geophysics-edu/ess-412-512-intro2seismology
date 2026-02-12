# Midterm Assignment Implementation Summary

**Date:** February 11, 2026  
**Notebook:** `Midterm_ComputerProgram1_Assignment.ipynb`

## Changes Implemented (Tier 1: High Impact, Low Overhead)

### 1. ✅ Enhanced Pre-Run Prediction Requirements (All 3 Parts)

**Changes:**
- Updated all three "Pre-run prediction" cells with **mandatory annotation requirements**
- Added specific prompts for what students must include:
  - **Part 1:** Label critical distances, ray paths with turning depths, slope changes
  - **Part 2:** Depth sensitivity annotations, frequency ranges, shallow vs deep spectra
  - **Part 3:** Ray coverage diagrams, resolution zones, crossing angles, PSF sketches
- Added grading note: Credit only for annotated reasoning, not vague drawings
- Required physics explanations (2-4 sentences)

**Impact:** Prevents "draw anything" sketches; forces students to think before coding

---

### 2. ✅ Added Image Embedding Guide (New Cell at Top)

**Location:** After title cell, before Part 1

**Content:**
- Four methods for embedding hand-drawn sketches
- Technical instructions for drag-and-drop
- File size warnings and best practices
- Requirements for image quality and annotations

**Impact:** Removes technical barriers to sketch submission

---

### 3. ✅ Added Polarization Analysis (Part 2.1A)

**Location:** Inserted after Part 2.1 (data download), before Part 2.2 (TauP)

**New Content:**
- **Markdown cell** explaining P-wave polarization analysis using covariance eigendecomposition
- **Code cell** with `polarization_analysis()` function scaffold
- Students must:
  - Download 3-component data (BHZ, BHN, BHE)
  - Compute covariance matrix of P-wave window
  - Extract eigenvalues/eigenvectors
  - Calculate rectilinearity $R = 1 - \frac{\lambda_2 + \lambda_3}{2\lambda_1}$
  - Calculate incidence angle from principal eigenvector
  - Compare to TauP-predicted ray parameter → incidence angle
- Includes extensive comments and hints

**Impact:** Tests Chapter 3 material (polarization, P/S wave theory); fills major gap

---

### 4. ✅ Added Conceptual Checkpoint (Part 3.4A)

**Location:** Inserted after Part 3.4 inversion code, before Part 3.5 PSFs

**New Content:**
Four questions requiring students to interpret THEIR OWN results:

1. **Resolution map interpretation:** Identify low-resolution region, draw ray coverage cartoon, explain why
2. **Ray parameter from T(X):** Pick a point, estimate slope, interpret physical meaning
3. **Dispersion and depth:** Compare U(T) at different periods, explain depth sensitivity
4. **Damping prediction:** Predict effect of doubling λ, test it, explain result

**Impact:** AI-resistant (requires referencing specific student results); tests conceptual understanding

---

### 5. ✅ Added Checkerboard Resolution Test (Part 3.5A)

**Location:** Inserted after Part 3.5 (PSFs), before Part 3.6 (curved rays)

**New Content:**
- **Markdown cell** explaining checkerboard test purpose and requirements
- **Code cell** with `create_checkerboard()` function and usage examples
- Students must:
  - Create alternating ±0.05 s/km checkerboard pattern
  - Generate noise-free synthetic data
  - Invert with same λ used earlier
  - Plot true/recovered/difference models
  - Interpret smearing in relation to diag(R) maps

**Impact:** Standard tomography practice; tests understanding of resolution vs coverage

---

### 6. ✅ Enhanced AI Use Log (Replaced Simple Version)

**Location:** Final cell before submission checklist

**New Structure:**
Five required sections per Part where AI was used:

1. **Physics-First Question:** What did you need to understand before prompting AI?
2. **Verification Strategy:** How did you check AI output was physically correct?
3. **AI Was Wrong:** Concrete example where AI misled you and how you corrected it
4. **Unresolved Confusion:** What do you still not understand? (honesty encouraged)
5. **Citation:** Formal citation if AI code/text used verbatim

**Grading rubric:** 0-3 pts (vague), 4-6 pts (adequate), 7-10 pts (excellent)

**Impact:** Forces reflection on AI use; demonstrates verification; catches outsourcing

---

### 7. ✅ Updated Submission Checklist

**Changes:**
- Added all new requirements (polarization, checkerboard, conceptual checkpoint)
- Reorganized by Part with point allocations
- Marked "NEW" items for clarity
- Increased estimated time to 8-10 hours (from ~6-7)
- Added reproducibility checks

**Impact:** Clear expectations; students know what's being graded

---

## Summary of New Learning Outcomes Tested

| **Topic** | **Before** | **After** |
|-----------|------------|-----------|
| **Chapter 3 (Polarization)** | ❌ Not tested | ✅ Covariance eigendecomposition, rectilinearity, incidence angle |
| **Resolution testing** | ⚠️ Mentioned, not required | ✅ Checkerboard test mandatory |
| **Conceptual reasoning** | ⚠️ Some interpretation questions | ✅ 4 questions requiring student-specific analysis |
| **Pre-run predictions** | ⚠️ Required but vague | ✅ Specific annotation requirements |
| **AI integrity** | ⚠️ Simple self-report | ✅ 5-section verification log with examples |

---

## Not Implemented (Future Enhancements)

### Tier 2 Recommendations (Moderate Scope):
- **Particle motion plots** (Z-R plane for Rayleigh waves)
- **PyKonal integration** for curved-ray tomography
- **Smoothness regularization** comparison vs damping
- **Verify slope(T(X)) = p** in Part 1

### Tier 3 Recommendations (Larger Scope / Grad-Level):
- **Forward surface-wave modeling** (Vs(z) → C(T) prediction)
- **Iterative bent-ray tomography** (nonlinear inversion)
- **Live oral check-ins** (10-min Zoom follow-ups)
- **Debugging task** (fix intentionally buggy code)

---

## Testing Checklist for Instructor

Before releasing to students:

- [ ] Run notebook top-to-bottom to verify all code cells execute
- [ ] Test image embedding in your Jupyter environment (Lab vs Notebook)
- [ ] Verify `polarization_analysis()` function scaffold is correct
- [ ] Check `create_checkerboard()` function produces expected pattern
- [ ] Review point allocations (currently sums to: 15+30+35+10 = 90 points; need 10 more?)
- [ ] Create optional Canvas assignment for sketch uploads (backup method)
- [ ] Update course schedule/deadlines
- [ ] Consider creating a **rubric document** for TAs

---

## Recommended Follow-Up Actions

1. **Create grading rubric spreadsheet** with:
   - Pre-run predictions (5 pts × 3 = 15)
   - Polarization analysis (5 pts)
   - Conceptual checkpoint (2 pts × 4 questions = 8)
   - Checkerboard test (7 pts)
   - AI Use Log (10 pts)
   - (Redistribute to total 100 pts)

2. **Post announcement** explaining:
   - New sections added (polarization, checkerboard, conceptual questions)
   - Why sketches need annotations
   - Image embedding methods
   - Increased time estimate (8-10 hrs)

3. **Create example sketch** showing good vs bad annotations (for Canvas)

4. **Prepare DataCamp/tutorial** on:
   - Covariance matrix eigendecomposition (if not covered in lectures)
   - Checkerboard testing procedure (or link to research paper example)

5. **For ESS 512 (grad students):**
   - Consider adding Tier 2 enhancements as required
   - Add Tier 3 (iterative tomography, forward modeling) as capstone

---

## File Locations

- **Modified notebook:** `notebooks/Midterm_ComputerProgram1_Assignment.ipynb`
- **This summary:** `notebooks/MIDTERM_IMPLEMENTATION_SUMMARY.md`

---

## Questions for Instructor Decision

1. **Point allocation:** Current ~90 points, need to balance to 100. Suggestions:
   - Reduce tomography to 33 pts?
   - Add 5 pts to professionalism?
   - Or keep 90 and scale grades?

2. **Image embedding method:** Will you create a Canvas backup assignment, or require Jupyter-only?

3. **PyKonal:** Should Part 3.6 (curved rays) use hand-coded shooter or integrate pykonal? (Tier 2 enhancement)

4. **Due date:** With 8-10 hour estimate, recommend 2 weeks (vs 1 week for lighter midterm)

5. **Late policy:** With new conceptual questions, partial credit more complex—update policy?

---

## Changelog

- **v2.0 (2026-02-11):** Implemented Tier 1 enhancements
  - Added polarization analysis (Part 2.1A)
  - Enhanced pre-run predictions (all 3 Parts)
  - Added conceptual checkpoint (Part 3.4A)
  - Added checkerboard test (Part 3.5A)
  - Enhanced AI Use Log
  - Added image embedding guide
  - Updated submission checklist

- **v1.0 (original):** Parts 1-3 with ray tracing, real data, tomography
