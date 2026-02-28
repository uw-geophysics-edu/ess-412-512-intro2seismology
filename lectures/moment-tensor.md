# Moment Tensors: Representing Earthquake Sources

## Learning objectives
After this lecture, students should be able to:

- State why the seismic moment tensor **M** is **symmetric** and count its **6 independent** components.
- Compute and interpret the **isotropic (ISO)** and **deviatoric (DEV)** parts of **M**.
- Explain what a **double couple (DC)** is, why it corresponds to **shear faulting**, and why **two nodal planes** appear.
- Decompose **DEV → DC + CLVD** using eigenvalues; interpret **CLVD** physically.
- Classify common source processes (faulting, hydrofracture, caldera collapse, landslide) by their **ISO/DC/CLVD content**.
- Read the key fields in a **USGS/GCMT moment tensor** product at a physics level.

---

## Context and scope

This lecture introduces how seismologists **represent earthquake sources mathematically** using a single 3×3 matrix: the **moment tensor**.

Whereas earthquake location (Module 6) answers *where* and *when*, the moment tensor answers *how* — what kind of internal deformation generated the seismic waves? This is one of the most powerful tools in observational seismology: from a handful of numbers we can infer fault orientation, slip direction, and even whether the source involves volume change (explosions, collapse, opening cracks).

The moment tensor framework connects naturally to:
- **Ray theory and wave propagation** (Modules 3–5): the MT enters the forward problem as a source term whose radiation pattern modulates observed amplitudes.
- **Earthquake location** (Module 6): accurate locations are a prerequisite for moment tensor inversion, and MT inversion in turn refines source depth.

This material corresponds primarily to **Shearer (2009), *Introduction to Seismology*, Chapter 9.2**.

---

## 1. The moment tensor: six numbers that summarize a rupture

### 1.1 Linear source representation

A seismic source enters waveforms **linearly**:

$$\mathbf{d} \approx \mathbf{G}\,\mathbf{m}$$

where:
- $\mathbf{d}$ is the observed data (seismograms)
- $\mathbf{G}$ contains Green's functions (Earth response)
- $\mathbf{m}$ are the moment tensor components

The moment tensor $\mathbf{M}$ is a **symmetric 3×3 matrix** that encodes the equivalent body forces at the source:

$$
\mathbf{M} = \begin{pmatrix} M_{xx} & M_{xy} & M_{xz} \\ M_{xy} & M_{yy} & M_{yz} \\ M_{xz} & M_{yz} & M_{zz} \end{pmatrix}
$$

### 1.2 Why symmetric?

The moment tensor is symmetric ($\mathbf{M} = \mathbf{M}^T$) because **conservation of angular momentum** requires that the equivalent force system produces no net torque. This is a fundamental physical constraint, not merely a mathematical convenience.

**Consequence:** A 3×3 symmetric matrix has only **6 independent components** (the upper triangle), not 9. These 6 numbers are the minimum description of a point source.

📖 *Shearer reference:* Section 9.2, Equation 9.11

### 1.3 Physical interpretation

Each component $M_{ij}$ represents a **force couple**: a pair of opposing forces in the $i$-direction, separated along the $j$-direction. The 6 independent components capture all possible internal deformation patterns at a point:

- **Diagonal terms** ($M_{xx}$, $M_{yy}$, $M_{zz}$): dipoles (compression/extension along axes)
- **Off-diagonal terms** ($M_{xy}$, $M_{xz}$, $M_{yz}$): shear couples

---

## 2. Diagonalization and principal axes

### 2.1 Eigen-decomposition

Because $\mathbf{M}$ is symmetric, it is always **diagonalizable** with real eigenvalues and orthogonal eigenvectors:

$$\mathbf{M} = \mathbf{V}\,\text{diag}(\lambda_1, \lambda_2, \lambda_3)\,\mathbf{V}^T$$

where:
- **Eigenvectors** (columns of $\mathbf{V}$) = **principal axes** → encode **orientation**
- **Eigenvalues** ($\lambda_1 \geq \lambda_2 \geq \lambda_3$) → encode **source type** (ratios determine DC vs ISO vs CLVD content)

### 2.2 Separating orientation from source type

This is the key insight: diagonalization **separates geometry from physics**.

- **Orientation** (eigenvectors): relates to fault strike, dip, slip direction
- **Source type** (eigenvalue ratios): tells us whether the source is pure shear, explosive, or something more complex

Two moment tensors can have identical eigenvalues (same source type) but different eigenvectors (different fault orientations), or vice versa.

📖 *Shearer reference:* Section 9.2 (principal axes discussion)

---

## 3. The double couple: shear faulting

### 3.1 Canonical double couple

The most common seismic source — a **shear fault** — corresponds to a **double couple (DC)**. In its principal-axis frame, a DC has eigenvalues:

$$(\lambda_1, \lambda_2, \lambda_3) = (+M_0,\ 0,\ -M_0)$$

where $M_0$ is the **scalar seismic moment**:

$$\boxed{M_0 = \mu A \bar{D}}$$

with $\mu$ = rigidity, $A$ = fault area, $\bar{D}$ = average slip.

The middle eigenvalue is **exactly zero** — this is the defining property of a pure double couple.

### 3.2 Strike, dip, rake

The double couple can equivalently be described by **strike** ($\phi_s$), **dip** ($\delta$), and **rake** ($\lambda$):

- **Strike**: azimuth of the fault trace (0–360°)
- **Dip**: angle of fault plane from horizontal (0–90°)
- **Rake**: slip direction on the fault plane (−180° to +180°)

These three angles plus $M_0$ give 4 parameters — equivalent to the 6 tensor components minus the constraint that $\lambda_2 = 0$ and $\text{tr}(\mathbf{M}) = 0$ (2 constraints).

### 3.3 Two nodal planes: the fundamental ambiguity

A double couple produces a **four-lobed radiation pattern** with two orthogonal nodal planes:
- One is the **fault plane** (actual rupture surface)
- One is the **auxiliary plane** (geometrically required by symmetry)

```
+ (compression)                − (dilatation)
       \                          /
        \           |            /
    _____|__________|___________|_____
   /                |                 \
  /     (P)    +    |    −    (T)      \
 |                  |                   |
-|-----------------★-------------------|-- ← nodal plane 1
 |                  |                   |
  \     (T)    −    |    +    (P)      /
   \________________|_________________/
        /           |            \
       /                          \
− (dilatation)                + (compression)

                    ↑ nodal plane 2
```

**Why two planes?** Far-field P-wave radiation depends on the product $(\hat{n} \cdot \hat{s})$, where $\hat{n}$ is fault normal and $\hat{s}$ is slip direction. Swapping $\hat{n} \leftrightarrow \hat{s}$ gives **identical radiation** — so far-field data alone cannot distinguish the fault plane from the auxiliary plane.

Additional information is needed to resolve this ambiguity:
- Aftershock distributions
- Surface rupture mapping
- Geological knowledge of existing faults

📖 *Shearer reference:* Section 9.2 (double couple and nodal planes)

---

## 4. Isotropic and deviatoric decomposition

Any moment tensor can be split into two parts with distinct physical meaning:

### 4.1 Isotropic part (volume change)

$$\boxed{\mathbf{M}_\text{ISO} = \frac{\text{tr}(\mathbf{M})}{3}\,\mathbf{I}}$$

where $\text{tr}(\mathbf{M}) = M_{xx} + M_{yy} + M_{zz}$ is the trace.

**Physical interpretation:**
- $\text{tr}(\mathbf{M}) > 0$: **explosive** / volumetric expansion (e.g., nuclear explosion, opening crack)
- $\text{tr}(\mathbf{M}) < 0$: **implosive** / volumetric contraction (e.g., mine collapse)
- $\text{tr}(\mathbf{M}) = 0$: **pure shear** — no net volume change

### 4.2 Deviatoric part (shear + CLVD)

$$\boxed{\mathbf{M}_\text{DEV} = \mathbf{M} - \mathbf{M}_\text{ISO}}$$

By construction, $\text{tr}(\mathbf{M}_\text{DEV}) = 0$ — the deviatoric part has no volumetric component.

**Key property:** Tectonic earthquakes on faults should be purely deviatoric ($\text{tr}(\mathbf{M}) = 0$). A significant isotropic component indicates something beyond simple shear faulting.

📖 *Shearer reference:* Section 9.2

---

## 5. DEV → DC + CLVD decomposition

The deviatoric part can be further decomposed into a **best-fitting double couple** and a **compensated linear vector dipole (CLVD)** remainder.

### 5.1 Algorithm (the key procedure)

Given $\mathbf{M}$:

1. **Compute deviatoric part:** $\mathbf{M}_\text{DEV} = \mathbf{M} - \frac{\text{tr}(\mathbf{M})}{3}\mathbf{I}$
2. **Eigen-decompose $\mathbf{M}_\text{DEV}$:** eigenvalues $\varphi_1 \geq \varphi_2 \geq \varphi_3$ with $\varphi_1 + \varphi_2 + \varphi_3 = 0$, eigenvectors $\mathbf{V}$
3. **Best-fitting DC amplitude:** $M_0^\text{DC} = (\varphi_1 - \varphi_3)/2$
4. **DC in principal axes:** $\mathbf{M}_\text{DC}^\text{diag} = \text{diag}(M_0^\text{DC},\ 0,\ -M_0^\text{DC})$
5. **CLVD remainder:** $\mathbf{M}_\text{CLVD}^\text{diag} = \text{diag}(\varphi_2/2,\ -\varphi_2,\ \varphi_2/2)$
6. **Rotate back:** $\mathbf{M}_\text{DC} = \mathbf{V}\,\mathbf{M}_\text{DC}^\text{diag}\,\mathbf{V}^T$, similarly for CLVD.

**Verification:** $\mathbf{M}_\text{DEV} = \mathbf{M}_\text{DC} + \mathbf{M}_\text{CLVD}$ (exact).

### 5.2 The δ diagnostic

The **middle eigenvalue** $\varphi_2$ controls how much CLVD is present:

$$\boxed{\delta = \frac{\varphi_2}{\max(|\varphi_1|, |\varphi_3|)}}$$

**Interpretation:**
- $\delta = 0$ → **pure double couple** (middle eigenvalue is zero)
- $|\delta| = 0.5$ → **pure CLVD** (two eigenvalues equal and opposite to the third)
- $0 < |\delta| < 0.5$ → mixture of DC and CLVD

### 5.3 What does CLVD mean physically?

A CLVD has eigenvalues in ratio $(2 : -1 : -1)$ or $(1 : 1 : -2)$, representing a source that extends in one direction while contracting in the other two (or vice versa).

**Physical sources that produce CLVD:**
- Simultaneous slip on non-parallel faults
- Complex rupture geometry (curved or kinked faults)
- Volcanic ring-faulting
- Artifacts of inversion (noise, poor station coverage, incorrect Earth model)

> **Caution:** Significant CLVD components in tectonic earthquakes are often **artifacts** of poor data coverage or an incorrect velocity model, not real physics.

📖 *Shearer reference:* Section 9.2

---

## 6. Source-process mapping

Different geophysical processes produce characteristic moment tensor signatures:

### 6.1 Tectonic earthquake (shear faulting)
- **Mostly DC** ($\delta \approx 0$)
- **tr(M) ≈ 0** (no volume change)
- This is the vast majority of earthquakes in global catalogs

### 6.2 Hydrofracture / dike injection
- **Significant ISO component** (opening creates volume increase, $\text{tr}(\mathbf{M}) > 0$)
- **Deviatoric part has CLVD-like character** (opening + shear)
- Non-zero trace is the diagnostic signature

### 6.3 Caldera collapse / ring-faulting
- **Non-DC deviatoric** (vertical CLVD-like pattern)
- **Sometimes implosive ISO** ($\text{tr}(\mathbf{M}) < 0$, volume decrease from collapse)
- Ring-fault geometry produces radiation incompatible with a single DC

### 6.4 Landslide / mass movement
- **Often not well described by a moment tensor at all**
- Better captured by a **single force** $\mathbf{f}(t)$ (Kanamori & Given, 1982)
- The force history tracks acceleration and deceleration of the sliding mass
- Moment tensors assume internal deformation; landslides involve translation

📖 *Shearer reference:* Section 9.2

---

## 7. Source-type plots

After diagonalization, the **source type** depends only on **eigenvalue ratios**, not on orientation or absolute magnitude.

### 7.1 Coordinate systems for source type

Two widely used representations:

**Hudson plot** (Hudson et al., 1989):
- Horizontal axis: $k = \text{tr}(\mathbf{M}) / (3M_0)$ (isotropic fraction)
- Vertical axis: related to $\delta$ (CLVD fraction)
- DC is at the origin; ISO endpoints at left/right edges

**Tape lune** (Tape & Tape, 2012):
- Maps eigenvalue triplets onto a **lune** (spherical triangle)
- DC is a point; CLVD is a line; ISO is another point
- Provides a uniform, distortion-free parameterization

Both plots encode the same physics — they are different projections of eigenvalue-ratio space:
- **DC** corresponds to $\varphi_2 = 0$ and $\text{tr}(\mathbf{M}) = 0$
- **CLVD** endpoints at $|\delta| = 0.5$, $\text{tr}(\mathbf{M}) = 0$
- **ISO** axis controlled by $\text{tr}(\mathbf{M})$

---

## 8. How moment tensors are estimated

Moment tensor inversion methods form a **ladder of increasing data requirements and model dependence**:

### 8.1 First-motion polarity
- Use P-wave first motions (up = compression, down = dilatation) at many stations
- Fit a **DC focal mechanism** (strike, dip, rake) to the polarity pattern
- **Limitation:** DC only — cannot detect ISO or CLVD components

### 8.2 Amplitude ratios
- Use amplitude ratios (e.g., P/S, SV/SH) in addition to polarity
- Adds constraints on mechanism, can partially resolve non-DC components

### 8.3 W-phase / long-period waveform inversion
- Fit long-period waveforms (periods > 50 s) using 1-D Earth models
- **Rapid** (minutes after large event) and **robust** for moderate-to-large events
- Standard method for USGS/GCMT solutions

### 8.4 Regional waveform inversion
- Fit full waveforms at regional distances (< 1000 km)
- More sensitive to **Earth structure** (3-D effects)
- Can resolve smaller events and non-DC components

### 8.5 Full waveform inversion (research frontier)
- Fit waveforms at all frequencies using 3-D Earth models
- Most **complete** but most **model-sensitive**
- Active area of research; computationally expensive

📖 *Shearer reference:* Section 9.2

---

## 9. Check-your-understanding (conceptual)

**Q1.** A moment tensor has eigenvalues $(3, 0, -3) \times 10^{18}$ N·m. What is the source type? Compute $\text{tr}(\mathbf{M})$ and $\delta$.

**Q2.** You observe that all P-wave first motions from an earthquake are compressional (up). What can you say about the moment tensor? Is this consistent with a pure DC?

**Q3.** A catalog reports an earthquake with 90% DC, 5% CLVD, 5% ISO. Is the CLVD component necessarily "real" physics? What factors could produce spurious non-DC content?

**Q4.** Why can't far-field seismic data alone distinguish between the fault plane and the auxiliary plane of a double couple? What additional information would you need?

**Q5.** You are studying a volcanic earthquake swarm. Events near the summit have large ISO components ($\text{tr}(\mathbf{M}) > 0$), while events on the flanks are nearly pure DC. Propose a physical interpretation.

Students should answer these *before* the companion notebook exercises.

---

## 10. What we deliberately did not do

- **Full radiation pattern derivation**: We stated the far-field dependence on $\hat{n}^T \mathbf{M} \hat{n}$ but did not derive it from elastodynamic Green's functions.
- **Stereographic projection (beach balls)**: Focal mechanism plotting is covered in the companion notebook; here we focused on the underlying tensor algebra.
- **Finite-source effects**: Real earthquakes have spatial extent; the point-source (MT) approximation breaks down when wavelength ≈ fault dimension.
- **Moment rate function**: The temporal history $M_0(t)$ and its relationship to rupture propagation.
- **Centroid vs hypocenter**: The moment tensor describes forces at the **centroid** (center of moment release), which may differ from the **hypocenter** (rupture initiation point).

---

## 11. Looking ahead

In the companion notebook (Lab 7a), we will:
- **Build** moment tensors from scratch and verify symmetry and eigenproperties
- **Implement** the ISO/DEV and DC/CLVD decomposition algorithm step by step
- **Visualize** P-wave radiation patterns for pure DC, CLVD, and ISO sources
- **Fetch** a real USGS moment tensor and decompose it using our tools
- **Classify** source types and connect eigenvalue diagnostics to physical processes

**Connections to other modules:**
- **Module 3 (Ray Theory):** Takeoff angles determine which part of the radiation pattern each station samples.
- **Module 5 (Surface Waves):** Long-period surface waves are the primary data for global MT inversion.
- **Module 6 (Earthquake Location):** Accurate locations are a prerequisite for MT inversion; location errors propagate into mechanism errors.

---

## Reading

**Textbook:**
- Shearer, P. M. (2009), *Introduction to Seismology*, 2nd ed.
  - **Chapter 9.2**: Moment tensor representation, DC, ISO/DEV, CLVD

**Classic references:**
- Jost, M. L., & Herrmann, R. B. (1989). A student's guide to and review of moment tensors. *Seismological Research Letters*, 60(2), 37–57.
- Aki, K., & Richards, P. G. (2002). *Quantitative Seismology*, 2nd ed. Chapter 4: Representation theorems.

**Source-type plots:**
- Hudson, J. A., Pearce, R. G., & Rogers, R. M. (1989). Source type plot for moment tensor inversion. *Journal of Geophysical Research*, 94(B1), 765–774.
- Tape, W., & Tape, C. (2012). A geometric setting for moment tensors. *Geophysical Journal International*, 190(1), 499–514.
