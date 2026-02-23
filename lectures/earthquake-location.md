# Earthquake Location: The Inverse Problem of Finding Sources

## Learning objectives
After this lecture, students should be able to:

- Formulate **earthquake location as a nonlinear inverse problem** with travel times as data.
- Understand the **formal statistical framework** (χ², degrees of freedom, residuals).
- Apply **relative location concepts** to improve precision for clustered events.
- Define and interpret **geometric quality metrics** (azimuthal gap, DMIN, aperture).
- Predict which **station geometries** yield good depth resolution versus epicenter resolution.
- Explain why **depth is the hardest parameter to constrain** in typical seismic networks.
- Understand the **coupling between origin time and location** and how it affects uncertainty.

---

## Context and scope
This lecture introduces the **fundamental inverse problem of seismology**: locating earthquake sources from observed arrival times at seismic stations.

Earthquake location is the **dual problem to travel-time tomography**:
- **Tomography**: Known sources, unknown velocity structure → recover $v(\mathbf{x})$
- **Location**: Known velocity structure, unknown source position → recover $\mathbf{x}_0, t_0$

Despite its apparent simplicity, earthquake location reveals deep lessons about:
- Geometric sensitivity of inverse problems
- Nonlinearity and linearization strategies
- The interplay between physical constraints and data coverage

This material builds on **ray theory** (Module 3) and connects to **tomography** (Module 5). It corresponds to portions of **Introduction to Seismology, Shearer (2009), Chapter 5.7**.

Further reading: Lee & Stewart (1981), Lomax et al. (2000), Husen & Hardebeck (2010).

---

## 1. Formal statement (Shearer 5.7 framework)

Before diving into geometry and algorithm details, we establish the **formal inverse problem** following Shearer's notation.

### 1.1 Model vector and observed data

**Model vector** (Shearer notation):
$$ \mathbf{m} = (T, x, y, z) $$

where:
- $T$ is **origin time** (when rupture begins)
- $(x, y, z)$ is **hypocenter location** (3D coordinates)

> **Notation note:** For computational implementation (notebooks, code), we often reorder to $\mathbf{m} = [x, y, z,T]^T$ for consistency with spatial-first conventions. The physics is identical; only ordering differs.

**Observed data:**
$$ \mathbf{t} = \{t_i\}_{i=1}^N $$

where $t_i$ is the **observed arrival time** at station $i$ ($N$ stations total).

📖 *Shearer reference:* Section 5.7, Equation 5.27

### 1.2 Forward operator

The **forward operator** $F_i$ predicts arrival time at station $i$:

$$ t_i^p = F_i(\mathbf{m}) $$

For a **homogeneous velocity** $v$:

$$ F_i(\mathbf{m}) = T + \frac{r_i}{v} $$

where $r_i = ||\mathbf{x}_i - \mathbf{x}||$ is the source-receiver distance.

For **heterogeneous Earth**, $F_i$ requires ray tracing through $v(\mathbf{x})$ (eikonal solver, ray shooting, etc.).

### 1.3 Residuals

The **residual** at station $i$ is:

$$ r_i = t_i - F_i(\mathbf{m}) = t_i - t_i^p $$

**Physical interpretation:**
- $r_i > 0$: Observed later than predicted → ray traveled **slower** than model
- $r_i < 0$: Observed earlier than predicted → ray traveled **faster** than model

### 1.4 Misfit functions and statistical measures

**L2 norm (least squares):**
$$ \xi = \sum_{i=1}^N r_i^2 $$

This is the **objective function** we minimize. Assumes Gaussian errors.

**Weighted χ² (chi-squared) statistic:**
$$ \chi^2 = \sum_{i=1}^N \frac{r_i^2}{\tau_i^2} $$

where $\tau_i$ is the **picking uncertainty** (standard deviation) for station $i$.

**Degrees of freedom:**
$$ \nu = N - 4 $$

(4 model parameters: $x, y, z, T$)

**Reduced chi-squared:**
$$ \chi_\nu^2 = \frac{\chi^2}{\nu} $$

**Interpretation:**
- $\chi_\nu^2 \approx 1$: Good fit (residuals consistent with assumed uncertainties)
- $\chi_\nu^2 \ll 1$: **Overfit** (uncertainties overestimated, or damping too strong)
- $\chi_\nu^2 \gg 1$: **Underfit** (unmodeled errors: wrong velocity model, correlated noise, bad picks)

📖 *Shearer reference:* Equations 5.29-5.30

#### L1 vs L2 norms

**L2 (this course):**
- **Advantages:** Analytic derivatives → efficient iterative solution; natural Gaussian statistics
- **Disadvantages:** Sensitive to outliers (bad picks can dominate)

**L1 (robust alternative):**
$$ \xi_{L1} = \sum_{i=1}^N |r_i| $$

- **Advantages:** Less sensitive to outliers (robust estimator)
- **Disadvantages:** No closed-form solution → requires iterative reweighting (slower)

**Practical approach:** Most operational systems use **L2 with outlier rejection**:
1. Solve L2 problem
2. Remove arrivals with $|r_i| > 3\sigma$
3. Re-solve

This combines L2 efficiency with L1 robustness.

---

## 2. The forward problem: from source to arrival times

Consider an earthquake at position $\mathbf{x}_0 = (x_0, y_0, z_0)$ occurring at origin time $t_0 = T$.

A seismic station at position $\mathbf{x}_i$ records a P-wave arrival at observed time $t_i^{obs}$.

The **forward model** relates these quantities:

$$ t_i^{obs} = t_0 + T(\mathbf{x}_0, \mathbf{x}_i; v) + \epsilon_i $$

where:
- $t_0$ is the **origin time** (when rupture begins)
- $T(\mathbf{x}_0, \mathbf{x}_i; v)$ is the **travel time** from source to receiver through velocity model $v$
- $\epsilon_i$ is **measurement error** (picking uncertainty, timing errors)

### Key observation
Even with a **known velocity model** $v$, this is a **nonlinear** relationship:
- Travel time $T$ depends on the ray path
- Ray path depends nonlinearly on source position
- Even for straight rays: $T = |\mathbf{x}_i - \mathbf{x}_0| / v$ (involves a square root)

This nonlinearity necessitates **iterative solution** methods (unlike linear tomography with fixed sources).

📖 *Shearer reference:* Chapter 4.1 (ray paths), Chapter 11.1 (location problem)

---

## 3. The inverse problem: four unknowns, N observations

Given:
- $N$ observed arrival times: $\{t_i^{obs}\}_{i=1}^N$
- $N$ station positions: $\{\mathbf{x}_i\}_{i=1}^N$
- A velocity model: $v(\mathbf{x})$

Find:
- **Model vector**: $\mathbf{m} = [x_0, y_0, z_0, t_0]^T$ (4 unknowns)

This requires **at least 4 stations** to constrain the problem (one equation per station).

### Why 4 unknowns?
Unlike tomography, where travel times give information about velocity structure **along the ray path**, earthquake location must simultaneously solve for:
1. 3D position $(x_0, y_0, z_0)$
2. Origin time $t_0$

The origin time is **coupled to radial distance** from the array: a uniform time shift acts like changing the distance to all stations equally.

> **Note on notation:** In this lecture, we present theory using Shearer's $\mathbf{m} = (T, x, y, z)$ ordering. In computational implementation (notebooks), we reorder to $\mathbf{m} = [x, y, z, T]^T$ for convenience. The physics and mathematics are identical.

---

## 4. Geometric concepts: what determines location quality?

Earthquake location quality depends **more on geometry than on the number of stations**.

### 4.1 Azimuthal gap ($\Delta\phi$)

The **azimuthal gap** is the largest angle (in plan view) between adjacent stations as seen from the epicenter.

```
         Station 2
              ↑
              |
Station 1 ←  ★  → Station 3
          Epicenter
```

**Interpretation:**
- **Small gap** (< 90°): Good epicenter constraint
- **Medium gap** (90-180°): Acceptable, but elongated error ellipse
- **Large gap** (> 180°): Poor constraint perpendicular to array

📊 *Quality criterion:* Most seismic networks require gap < 180° for "good" locations.

### 4.2 Distance to nearest station (DMIN)

**DMIN** is the horizontal distance from epicenter to the closest station.

**Critical relationship:**
- If **DMIN >> depth**, rays exit at shallow takeoff angles → poor depth resolution
- If **DMIN ≈ depth**, rays exit steeply → good depth leverage

**Example:**
- Earthquake at 10 km depth
- Nearest station at 50 km distance
- Takeoff angle: $\theta \approx \arctan(10/50) \approx 11°$ from horizontal → almost no vertical resolution

### 4.3 Aperture (angular coverage)

**Aperture** describes the range of **takeoff angles** from the source to the seismic array.

- **Wide aperture** (rays exit in many directions): Good 3D constraint
- **Narrow aperture** (all rays nearly horizontal): Depth/origin time trade-off

**Physical picture:**
```
        Station (surface)
           ↑ steep ray
          /
         / ← good depth sensitivity
        /
       ★ Source (depth)
      /
     / ← shallow ray
    /   poor depth sensitivity
   ↓
Station (far)
```

Wide aperture requires **stations at various distances**, especially some nearby stations.

### 4.4 Coverage vs. resolution trade-off

**Many distant stations:**
- ✓ Good horizontal location (azimuthal coverage)
- ✗ Poor depth (narrow aperture, origin time coupling)

**Few nearby stations:**
- ✓ Good depth (wide aperture)
- ✗ Potential azimuthal ambiguity

**Optimal design:** Mix of nearby and distant stations for balanced 3D resolution.

---

## 5. Why depth is the hardest parameter

### 5.1 The geometric challenge

In typical regional/local networks:
- Stations are at the **surface** (z = 0)
- Earthquakes occur at **depth** (z > 0)
- Most rays propagate nearly **horizontally** (small vertical slowness component)

**Consequence:** Travel times are insensitive to depth changes unless:
- Stations are very close (DMIN < depth)
- Ray curvature is significant (refracted phases)

### 5.2 Depth/origin time coupling

For an array of distant stations, the following **trade-off** exists:

Making the source:
- **Deeper** → rays travel through faster material (if $v$ increases with depth) → shorter travel time
- **Earlier origin time** → all arrivals shift earlier by same amount

These effects can **cancel each other**, creating an elongated error ellipse in the depth–$t_0$ plane.

📖 *Shearer reference:* Fig. 11.3 (error ellipsoid)

### 5.3 Velocity model dependence

Depth estimates are **strongly sensitive** to the assumed velocity model:
- If you use a model that is too fast, you'll locate events **too shallow**
- If too slow, you'll locate events **too deep**

**Common practice in regional seismology:** Fix depth at typical crustal values (e.g., 10 km) if geometry is poor, to avoid trading off depth uncertainty into horizontal position errors.

---

## 6. Linearization: Geiger's method

Because the forward problem is **nonlinear**, we use **iterative linearization** (analogous to bent-ray tomography).

### 6.1 Taylor expansion around a reference location

Start with an initial guess $\mathbf{m}^{(0)} = [x_0^{(0)}, y_0^{(0)}, z_0^{(0)}, t_0^{(0)}]^T$.

Expand travel time to first order:

$$ t_i(\mathbf{m}) \approx t_i(\mathbf{m}^{(0)}) + \frac{\partial t_i}{\partial x_0}\Delta x_0 + \frac{\partial t_i}{\partial y_0}\Delta y_0 + \frac{\partial t_i}{\partial z_0}\Delta z_0 + \frac{\partial t_i}{\partial t_0}\Delta t_0 $$

The last term is simple: $\frac{\partial t_i}{\partial t_0} = 1$ (origin time adds uniformly to all arrivals).

### 6.2 The Jacobian (G matrix)

Define residuals: $\Delta t_i = t_i^{obs} - t_i(\mathbf{m}^{(0)})$

The **Jacobian matrix** is:

$$ G_{ij} = \frac{\partial t_i}{\partial m_j} $$

For **straight rays** with constant velocity $v$:

$$ t_i = t_0 + \frac{r_i}{v}, \quad r_i = \sqrt{(x_i-x_0)^2 + (y_i-y_0)^2 + (z_i-z_0)^2} $$

Derivatives:

$$ \frac{\partial t_i}{\partial x_0} = -\frac{x_i - x_0}{v r_i}, \quad \frac{\partial t_i}{\partial y_0} = -\frac{y_i - y_0}{v r_i}, \quad \frac{\partial t_i}{\partial z_0} = -\frac{z_i - z_0}{v r_i} $$

$$ \frac{\partial t_i}{\partial t_0} = 1 $$

These are the **direction cosines** (unit vector from source to station) divided by velocity, plus the origin time term.

### 6.3 Damped least squares update

Solve the linearized system:

$$ \mathbf{G}\,\Delta\mathbf{m} = \Delta\mathbf{t} $$

with damping for stability:

$$ \Delta\mathbf{m} = (\mathbf{G}^T\mathbf{G} + \lambda\mathbf{I})^{-1}\mathbf{G}^T\,\Delta\mathbf{t} $$

Update the model:

$$ \mathbf{m}^{(k+1)} = \mathbf{m}^{(k)} + \alpha\,\Delta\mathbf{m} $$

where $\alpha$ is a step length (often $\alpha = 1$).

**Iteration:** Re-compute travel times, residuals, Jacobian, and repeat until convergence (typically < 10 iterations).

📖 *Shearer reference:* Chapter 11.2 (Geiger's method)

---

## 7. Resolution and uncertainty

### 7.1 Model resolution matrix

From linear inverse theory:

$$ \mathbf{R} = (\mathbf{G}^T\mathbf{G} + \lambda\mathbf{I})^{-1}\mathbf{G}^T\mathbf{G} $$

**Diagonal elements** $R_{jj}$ measure how well parameter $m_j$ is resolved (0 = completely smeared, 1 = perfectly resolved).

With **poor geometry**, depth often has $R_{33} < 0.5$ (poorly resolved).

### 7.2 Error ellipsoids

The **posterior covariance matrix** is:

$$ \mathbf{C}_m = \sigma^2 (\mathbf{G}^T\mathbf{G})^{-1} $$

where $\sigma^2$ is the data variance (picking error).

**Error ellipsoid** semi-axes come from eigenvalues of $\mathbf{C}_m$.

**Catalog quality codes:**
- **ERH**: Horizontal error (km) – semi-major axis of horizontal ellipse
- **ERZ**: Vertical error (km) – vertical semi-axis
- **RMS**: Root-mean-square residual (s)

#### ⚠️ Critical assumption: uncorrelated Gaussian errors

The covariance formula $\mathbf{C}_m = \sigma^2 (\mathbf{G}^T\mathbf{G})^{-1}$ assumes:
- **Uncorrelated** Gaussian errors (each $\tau_i$ independent)
- **Correct velocity model** ($v(\mathbf{x})$ matches reality)

**Reality check:**
Unmodeled 3D structure produces **correlated residuals**:
- Rays through **slow anomaly** → systematic late arrivals at multiple stations
- Rays through **fast anomaly** → systematic early arrivals
- All stations in one azimuth affected similarly
- Violates independence assumption

**Consequence:** Formal error ellipses are often **too optimistic** by factor of 2-5.

**Mitigation strategies:**
1. **Station corrections** (empirical timing adjustments per station)
2. **3D velocity models** (ray tracing through heterogeneity)
3. **Relative location** (next section – cancels common-path errors)
4. **Increased uncertainty estimates** (inflate $\sigma$ by empirical factor)

📖 *Shearer warning:* End of Section 11.2 – discusses bias from neglected heterogeneity

### 7.3 Relative location and master event methods

For **clustered seismicity** (aftershocks, swarms, mining-induced events), **relative location** improves precision by differencing data.

#### The relative location idea

Consider two nearby earthquakes $A$ and $B$ recorded at the same stations.

**Absolute location:** Solve for $\mathbf{m}_A$ and $\mathbf{m}_B$ independently → errors dominated by velocity model and station effects.

**Relative location:** Difference arrival times:
$$ t_i^{rel} = t_i^A - t_i^B $$

If source separation $\Delta\mathbf{x} = \mathbf{x}_A - \mathbf{x}_B$ is **small** compared to source-receiver distance, rays share most of their path:

$$ t_i^{rel} \approx \frac{\partial t_i}{\partial \mathbf{x}} \cdot \Delta\mathbf{x} $$

**Key advantage:** Common-mode errors **cancel**:
- Station timing offsets → eliminated
- Velocity model bias along shared ray path → reduced
- Only **differential ray geometry** matters

#### Mathematical formulation

Linearize around master event $M$ at location $\mathbf{x}_M$:

$$ t_i^{rel} = t_i^A - t_i^M \approx \mathbf{G}_i \cdot (\mathbf{x}_A - \mathbf{x}_M) $$

where $\mathbf{G}_i$ is the derivative at event $M$.

Solve for relative position $\Delta\mathbf{x}$, then:
$$ \mathbf{x}_A = \mathbf{x}_M + \Delta\mathbf{x} $$

#### Double-difference method

The **double-difference** technique (Waldhauser & Ellsworth, 2000) extends this to **all event pairs**:

$$ t_{ij}^{AB} = (t_i^A - t_i^B) - (f_i(\mathbf{x}_A) - f_i(\mathbf{x}_B)) $$

Forms a large coupled system for **all events simultaneously** → relative positions accurate to **meters** even when absolute locations have **km-scale errors**.

**Applications:**
- Aftershock sequences (map fault geometry at meter scale)
- Volcanic swarms (track dike/conduit structure)
- Induced seismicity (injection site monitoring)

**Limitation:** Requires **repeating sources** or very similar ray paths.

📖 *Shearer reference:* Section 11.2.4
📖 *Advanced reading:* Waldhauser & Ellsworth (2000), "A double-difference earthquake location algorithm"

---

## 8. Check-your-understanding (conceptual)

Before numerical exercises, predict:

**Q1.** You have 4 stations arranged in a square around an epicenter. The earthquake is directly beneath the center at 10 km depth.
- Which location parameter(s) will have the **largest uncertainty**?
- How would adding a 5th station at the center of the square change this?

**Q2.** All your stations are west of the earthquake (gap = 270°).
- In which direction will the epicenter error be largest?
- Will this geometry provide good depth resolution? Why or why not?

**Q3.** You change the velocity model from $v = 6.0$ km/s to $v = 6.5$ km/s (faster).
- Without relocating, will your computed origin time be too early or too late?
- Will your computed depth be too shallow or too deep?

**Q4.** Two earthquakes occur at the same location, separated by 1 hour. You have excellent azimuthal coverage and 12 stations.
- If all stations show the second event arriving 0.5 seconds **later** than the first, what can you conclude?
- What if all stations show the second event arriving later, **except** one station shows it arriving earlier?

**Q5.** You are locating a cluster of aftershocks from a mainshock. With standard absolute location:
- Your locations have ERH = 2 km and ERZ = 5 km
- Using double-difference relative location, what order-of-magnitude improvement would you expect?
- What common errors are canceled by relative location methods?

Students should answer these *before* running numerical location algorithms.

---

## 9. Extensions and what we deliberately did not do

### What we covered
- Formal inverse problem framework (χ², residuals, statistical measures)
- Forward problem and nonlinearity
- Geometric sensitivity (gap, DMIN, aperture)
- Iterative linearization (Geiger's method)
- Resolution and uncertainty quantification
- Relative location concepts

### What we deliberately did not do
- **3D velocity models** (full ray tracing in heterogeneous Earth)
- **Phase identification** (distinguishing P from S, regional phases)
- **Arrival time picking algorithms** (STA/LTA, waveform cross-correlation)
- **Joint hypocenter determination** (using common source clusters to refine structure)
- **Station corrections / station terms** (absorbing local velocity errors)
- **Magnitude estimation** (amplitude-based)

These are essential for **operational seismology** but would obscure the core geometric lessons.

---

## 10. Practical implications

### Catalog quality assessment
When using published earthquake catalogs (USGS, ISC, regional networks), check:
- **Gap**: < 180° is acceptable, < 90° is good
- **DMIN**: Should be comparable to or less than depth for reliable depth
- **Number of stations**: Minimum 4, ideally > 10 for redundancy
- **RMS residual**: < 0.5 s for local, < 1.0 s for regional
- **Fixed depth indicator**: "f" or "*" means depth was not free parameter

### Network design
When designing a permanent seismic network:
- **Prioritize geometry over number**: 6 well-placed stations beat 20 poorly distributed ones
- **Include nearby stations** for depth resolution (DMIN < typical focal depth)
- **Close azimuthal gaps** to avoid elongated error ellipses
- **Consider aftershock scenarios**: Do you have stations within the rupture zone?

---

## 11. Looking ahead

In the companion notebook, we will:
- Implement grid search to visualize the nonlinear objective function
- Visualize **χ² contours** and understand misfit topology
- Code Geiger's method with **convergence diagnostics** using χ²/ν
- Systematically explore geometric failure modes (gap, depth, etc.)
- Compute and interpret error ellipsoids
- Implement a **2-event relative location example** demonstrating error cancellation
- Extend to **curved rays** using eikonal solvers (like tomography notebook)

**Connection to other modules:**
- **Module 3 (Ray Theory)**: Takeoff angles and ray parameters directly determine location resolution
- **Module 5 (Tomography)**: Location is the dual problem; identical inverse theory framework
- **Module 6 (Source Mechanisms)**: Accurate locations are prerequisite for moment tensor inversion

---

## Reading

**Textbook:**
- Shearer, P. M. (2009), *Introduction to Seismology*, 2nd ed.
  - **Chapter 4.1–4.2**: Ray theory fundamentals
  - **Chapter 5.7**: Formal inverse problems, residuals, χ², L1 vs L2 norms
  - **Chapter 11.1–11.2**: Earthquake location methods (Geiger's method)
  - **Chapter 11.2.4**: Relative location methods

**Classic papers:**
- Lee, W. H. K., & Stewart, S. W. (1981). *Principles and Applications of Microearthquake Networks*. Academic Press. (Chapter 6: Location)
- Lomax, A., Virieux, J., Volant, P., & Berge-Thierry, C. (2000). Probabilistic earthquake location in 3D and layered models. In *Advances in Seismic Event Location* (pp. 101-134). Springer.

**Modern reviews:**
- Husen, S., & Hardebeck, J. L. (2010). Earthquake location accuracy. *Community Online Resource for Statistical Seismicity Analysis*. doi:10.5078/corssa-55815573

**Advanced topics:**
- Waldhauser, F., & Ellsworth, W. L. (2000). A double-difference earthquake location algorithm: Method and application to the northern Hayward fault, California. *BSSA*, 90(6), 1353-1368.
