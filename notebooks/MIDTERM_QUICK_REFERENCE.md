# Quick Reference: Midterm Notebook Updates

## Summary for Instructor

**Total cells:** 48 (was 42)  
**New cells added:** 6  
**Cells modified:** 5

---

## What's New (Student-Facing)

### 🎨 **Image Embedding Guide** (Cell 2)
- Four methods for embedding hand-drawn sketches
- Technical how-to for drag-and-drop
- File size warnings

### 📝 **Enhanced Pre-Run Predictions** (Cells 4, 9, 21)  
All three Parts now require:
- **Mandatory annotations** (not just drawings)
- Specific elements to label
- 2-4 sentences of **physical reasoning**
- Grading note: Credit only for annotated reasoning

### 🔬 **NEW: Polarization Analysis** (Cells 14-15)  
**Part 2.1A** - Tests Chapter 3 material:
- Download 3-component data (Z, N, E)
- Covariance matrix eigendecomposition
- Compute rectilinearity & incidence angle
- Compare to TauP predictions
- **Time estimate:** +20 minutes

### 🤔 **NEW: Conceptual Checkpoint** (Cell 35)  
**Part 3.4A** - AI-resistant questions:
- Interpret YOUR diag(R) map (draw cartoon)
- Calculate slope from YOUR T(X) curve
- Explain YOUR dispersion trend
- Predict damping effect, then test it
- **Time estimate:** +15 minutes

### ✅ **NEW: Checkerboard Test** (Cells 37-38)  
**Part 3.5A** - Standard practice:
- Create alternating ±0.05 s/km pattern
- Noise-free inversion
- Plot true/recovered/difference
- Interpret smearing vs resolution
- **Time estimate:** +20 minutes

### 📋 **Enhanced AI Use Log** (Cell 48)  
Now requires 5 sections:
1. Physics-first question
2. Verification strategy  
3. Example where AI was wrong
4. Unresolved confusion
5. Citations

**Grading:** 0-3 pts (vague) → 7-10 pts (excellent)

### ✓ **Updated Checklist** (Cell 47)  
- All new items listed
- Points redistributed
- Estimated time: 8-10 hours

---

## Key Cells by Location

| Cell # | Type | Content |
|--------|------|---------|
| 2 | Markdown | **NEW:** Image embedding guide |
| 4 | Markdown | **UPDATED:** Part 1 pre-run prediction (with annotations) |
| 9 | Markdown | **UPDATED:** Part 2 pre-run prediction (with annotations) |
| 14 | Markdown | **NEW:** Polarization analysis instructions |
| 15 | Code | **NEW:** `polarization_analysis()` function scaffold |
| 21 | Markdown | **UPDATED:** Part 3 pre-run prediction (with annotations) |
| 35 | Markdown | **NEW:** Conceptual checkpoint (4 questions) |
| 37 | Markdown | **NEW:** Checkerboard test instructions |
| 38 | Code | **NEW:** `create_checkerboard()` function |
| 47 | Markdown | **UPDATED:** Submission checklist |
| 48 | Markdown | **UPDATED:** AI Use Log (5 sections) |

---

## Testing Recommendations

### Before Release:
1. ✅ Verify notebook loads (done - 48 cells valid)
2. ⚠️ Test image embedding in your Jupyter environment
3. ⚠️ Run code cells to verify no syntax errors
4. ⚠️ Check that `polarization_analysis()` hints are correct
5. ⚠️ Verify `create_checkerboard()` produces expected pattern

### Optional Enhancements (Tier 2):
- Add worked example for polarization analysis
- Provide sample checkerboard output
- Add PyKonal integration for Part 3.6
- Add particle motion plots for Part 2

---

## Point Allocation Suggestion

Current structure allows ~95-100 points. Suggested breakdown:

| Component | Points |
|-----------|--------|
| **Pre-run predictions** (3×5) | 15 |
| **Part 1: Ray tracing** | 12 |
| **Part 2: Real data** | 25 |
|   - Data processing | 8 |
|   - Polarization analysis (NEW) | 5 |
|   - Surface waves | 8 |
|   - Short answers | 4 |
| **Part 3: Tomography** | 38 |
|   - G matrix & inversion | 10 |
|   - Resolution metrics | 8 |
|   - Conceptual checkpoint (NEW) | 6 |
|   - Checkerboard test (NEW) | 6 |
|   - Curved rays | 5 |
|   - Short answers | 3 |
| **AI Use Log** | 10 |
| **Professionalism** | 5 |
| **TOTAL** | **100** |

---

## Student Communication Template

```markdown
## Midterm Assignment Updates

Hello everyone,

I've enhanced the midterm assignment to better align with our course learning objectives. Key changes:

### New Sections (Required):
1. **Polarization Analysis** (Part 2.1A): Apply eigendecomposition to analyze P-wave particle motion—directly from Chapter 3 material.

2. **Conceptual Checkpoint** (Part 3.4A): Answer questions about YOUR specific results (resolution maps, dispersion curves, etc.). These questions test understanding, not just coding.

3. **Checkerboard Resolution Test** (Part 3.5A): Standard tomography practice—shows what spatial scales your ray geometry can resolve.

### Enhanced Requirements:
- **Pre-run predictions** now require annotated sketches (not just vague drawings)
- **AI Use Log** now has 5 specific sections demonstrating verification

### Image Embedding:
- New guide (Cell 2) shows how to embed hand-drawn sketches
- Drag-and-drop recommended method

### Time Estimate:
Updated to **8-10 hours** (was ~6-7) due to new sections.

### Why These Changes:
- Tests Chapter 3 (polarization—previously untested)
- Emphasizes conceptual reasoning over pure coding
- Aligns with research-standard practices (checkerboard tests)
- Strengthens academic integrity (AI verification)

Let me know if you have questions!
```

---

## Files Modified

- `notebooks/Midterm_ComputerProgram1_Assignment.ipynb` (48 cells, +6 new)
- `notebooks/MIDTERM_IMPLEMENTATION_SUMMARY.md` (this summary)
- `notebooks/MIDTERM_QUICK_REFERENCE.md` (this file)

---

**Last updated:** February 11, 2026
