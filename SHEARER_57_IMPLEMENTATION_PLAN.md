# Shearer Section 5.7 Implementation Plan

## Overview

This document summarizes the comprehensive plan to align your earthquake-location materials with Shearer's Introduction to Seismology, Section 5.7 framework.

## Files to Modify

1. **[lectures/earthquake-location.md](lectures/earthquake-location.md)** - Theoretical lecture (368 lines)
2. **[notebooks/06a_Earthquake_Location_Practice.ipynb](notebooks/06a_Earthquake_Location_Practice.ipynb)** - Computational exercises (~1300 lines)

---

## Part 1: Lecture Markdown Modifications

### Status: ✅ COMPLETE (see subagent report)

The modified lecture file is ready with all 9 changes:

#### 1. Extended Learning Objectives
- Added: "Understand the **formal statistical framework** (χ², degrees of freedom, residuals)"
- Added: "Apply **relative location concepts** to improve precision for clustered events"

#### 2. NEW Section 1: Formal Statement (Shearer 5.7 Framework)
**Inserted after "Context and scope" section (~line 36)**

Contents:
- **1.1 Model vector and observed data**
  - Shearer notation: m = (T, x, y, z)
  - Notation acknowledgment: computational code uses [x,y,z,T] ordering
  - References Shearer Eq. 5.27

- **1.2 Forward operator**
  - Forward operator F_i(m) definition
  - Homogeneous vs heterogeneous Earth cases

- **1.3 Residuals**
  - r_i = t_i - F_i(m) definition
  - Physical interpretation (early/late arrivals)

- **1.4 Misfit functions and statistical measures**
  - L2 norm: ξ = Σr_i²
  - Weighted χ²: χ² = Σ(r_i/τ_i)²
  - Degrees of freedom: ν = N - 4
  - Reduced χ²: χ_ν² = χ²/ν with interpretation rules
  - **L1 vs L2 norms subsection** (advantages/disadvantages, practical approach)
  - References Shearer Eqs. 5.29-5.30

#### 3. All Sections Renumbered (+1)
- Old §1 → §2 (The forward problem)
- Old §2 → §3 (The inverse problem)
- Old §3 → §4 (Geometric concepts)
- Old §4 → §5 (Why depth is hardest)
- Old §5 → §6 (Linearization: Geiger's method)
- Old §6 → §7 (Resolution and uncertainty)
- Continue through §11

#### 4. Section 2 (Forward Problem) - Enhanced
- Changed "origin time $t_0$" to "$t_0 = T$" for consistency
- Added: "This nonlinearity necessitates **iterative solution** methods"
- Added Shearer references (Chapter 4.1, 11.1)

#### 5. Section 3 (Inverse Problem) - Notation Note
- Added explicit acknowledgment:
  > "Note: In this lecture, we present theory using Shearer's m = (T, x, y, z) ordering. In computational implementation (notebooks), we reorder to m = [x, y, z, T]^T for convenience."

#### 6. Section 7.2 (Error Ellipsoids) - Correlated Error Warning
**Inserted after covariance matrix definition**

- New subsection: "⚠️ Critical assumption: uncorrelated Gaussian errors"
- Explains why C_m formula assumes uncorrelated Gaussian errors
- Reality check: unmodeled 3D structure creates correlated residuals
- Consequence: formal error ellipses often too optimistic by factor 2-5
- Mitigation strategies (station corrections, 3D models, relative location)
- References Shearer Section 11.2 warning

#### 7. Section 7.3: Relative Location and Master Event Methods (NEW)
**Inserted after error ellipsoids (~line 367)**

Contents:
- The relative location idea (differencing arrival times)
- Mathematical formulation (linearize around master event)
- Double-difference method (Waldhauser & Ellsworth 2000)
- Applications (aftershocks, volcanic swarms, induced seismicity)
- Limitations (requires repeating sources)
- References Shearer Section 11.2.4 and W&E 2000 paper

#### 8. Check-Understanding (Q5 Added)
**Q5: New relative location question**
- Asks about aftershock sequence precision improvement
- Tests understanding of error cancellation via double-difference

#### 9. Updated Reading Section
- Emphasized Chapter 5.7 (formal inverse problems, χ², L1 vs L2)
- Added Section 11.2.4 reference (relative location)
- Highlighted Waldhauser & Ellsworth (2000) paper

#### 10. Updated "Looking Ahead" Section (§11)
- Mentions χ² contours visualization
- Emphasizes convergence diagnostics with χ²/ν
- Promises 2-event relative location example

---

## Part 2: Notebook Modifications

### Status: 🔄 IMPLEMENTATION INSTRUCTIONS PREPARED

The subagent provided detailed insertion instructions but couldn't directly edit. Below are the 5 required modifications:

### Modification 1: Add χ² Functions
**Location:** After call ~170 (after `compute_rms_residual` function)

**Insert two functions:**
1. `compute_chi2(residuals, uncertainties)`
   - Returns: chi2, dof, chi2_reduced
   - Implements χ² = Σ(r_i/τ_i)², ν = N - 4, χ_ν² = χ²/ν
   - References Shearer 5.7, Eqs. 5.29-5.30

2. `compute_confidence_threshold(chi2_reduced, dof, confidence_level=0.95)`
   - Computes χ² thresholds for confidence contours
   - Uses scipy.stats.chi2 for proper statistical thresholds
   - For 2D slices: 50% → Δχ² ≈ 1.39, 95% → Δχ² ≈ 5.99

### Modification 2: Enhance Grid Search with χ² Contours
**Location:** Section A4 (Grid search), after RMS_grid computation

**Add:**
1. Compute chi2_matrix (parallel to existing rms_matrix)
2. Find chi2_min and compute confidence thresholds (50%, 95%)
3. New plot: χ² grid with overlaid confidence contours
   - White dashed line = 50% confidence
   - Red solid line = 95% confidence
4. Print χ²_min, χ²_reduced, degrees of freedom

### Modification 3: Update Geiger Iteration Output
**Location:** Inside Geiger iteration loop (wherever convergence is printed)

**Modify print statement to include:**
```python
print(f"Iteration {iteration}: RMS = {rms:.4f} s, χ² = {chi2:.2f}, χ²/ν = {chi2_red:.2f}, ||Δm|| = {np.linalg.norm(delta_m):.4f} km")
```

### Modification 4: Add Station Removal Experiment
**Location:** New subsection C3 (after Geiger section, before error ellipsoid section)

**Add:**
1. **Markdown cell:** "### C3. Geometry Degradation: Station Removal Experiment"
2. **Function:** `remove_station_experiment(true_location, station_positions, velocity, tau_pick, noise_level)`
   - Systematically removes stations (worst geometry first)
   - Tracks: n_stations, ERH, ERZ, χ²/ν, azimuthal_gap
   - Returns results dictionary

3. **Execution cell:** Run experiment and plot 4-panel figure:
   - Panel 1: ERH vs station count
   - Panel 2: ERZ vs station count
   - Panel 3: Azimuthal gap vs station count (with 180° threshold)
   - Panel 4: χ²/ν vs station count (with χ²/ν = 1 line)

### Modification 5: Add 2-Event Relative Location Example
**Location:** New Part G at end of notebook (after all existing parts)

**Add:**
1. **Markdown cell:** "## Part G: Relative Location (2-Event Example)"
   - Explains common-mode error cancellation
   - Shows formula: Δt_i = t_i^A - t_i^B
   - Emphasizes meter-scale precision despite km-scale absolute errors

2. **Code cell:** Complete 2-event demonstration
   - Event A (master): [5.0, 5.0, 10.0, 0.0]
   - Event B (nearby): [5.5, 5.0, 10.0, 0.1] (500m east)
   - Introduce 10% velocity model bias (6.0 → 5.4 km/s)

3. **Absolute location** (with bias):
   - Locate both events independently
   - Compute separation error (large due to velocity bias)

4. **Relative location** (bias cancels):
   - Implement `relative_locate()` function
   - Use linearized inversion around master event
   - Compute separation error (small, bias canceled)

5. **Visualization:**
   - Panel 1: Map view showing true positions, absolute locations, relative location, error vectors
   - Panel 2: Bar chart comparing separation errors (demonstrates improvement factor)

6. **Key message print:** Shows improvement factor (typically 5-20x)

---

## Implementation Summary

### Completed:
- ✅ Lecture markdown: All 9 modifications ready (complete file generated by subagent)
- ✅ Notebook: Detailed implementation instructions prepared

### Verification Steps:
1. Copy modified lecture markdown from subagent output to earthquake-location.md
2. Implement 5 notebook modifications using edit_notebook_file tool
3. Check for errors using get_errors tool
4. Test notebook execution (optional but recommended)

### Expected Outcomes:

**For students:**
- Formal statistical framework (χ², degrees of freedom) connects to Shearer textbook
- Understand when χ_ν² ≈ 1 indicates good fit vs overfitting/underfitting
- See confidence contours visualized (not just RMS values)
- Experience geometric degradation experiment (station removal)
- Witness common-mode error cancellation via relative location

**For instructors:**
- Materials now explicitly aligned with Shearer Section 5.7
- Notation discrepancy acknowledged (no code refactoring needed)
- Statistical rigor matches ESS 412/512 standards
- Relative location introduced at appropriate level (simple 2-event, not full double-difference)

---

## References

- **Shearer (2009), Introduction to Seismology (2nd ed.)**
  - Section 5.7: Formal inverse problem framework
  - Chapter 11.1-11.2: Earthquake location methods
  - Chapter 11.2.4: Relative location
  - Figure 11.2: Error ellipsoid confidence contours
  - Figure 11.3: Depth/origin time coupling

- **Waldhauser & Ellsworth (2000)**: "A double-difference earthquake location algorithm: Method and application to the northern Hayward fault, California." BSSA, 90(6), 1353-1368.

---

## Decision Record

Based on user confirmation (message 2):

**Q1: Notation discrepancy handling** → **Option B (Acknowledge in lecture)**
- Keep implementation as [x,y,z,T] ordering
- Add explicit note in lecture about Shearer's [T,x,y,z] convention
- No code refactoring required

**Q2: Statistical framework depth** → **Intermediate**
- Include χ² with proper weighting
- Visualize confidence contours (50%, 95%)
- Discuss degrees of freedom and χ_ν² interpretation
- Skip advanced topics (bootstrap, jackknife, full uncertainty propagation)

**Q3: Relative location approach** → **Option B (Simple 2-event example)**
- Demonstrate with single master-slave pair
- Show common-mode error cancellation principle
- Mention double-difference method (no full implementation)
- Appropriate for ESS 412/512 level

---

*Document prepared: [date]*
*Implementation status: Lecture complete, notebook ready for edit_notebook_file execution*
