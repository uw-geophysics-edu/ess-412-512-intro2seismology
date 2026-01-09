# Stress and Strain: Elastic Properties of Earth Materials

**Duration:** 15-20 minutes  
**Learning Objectives:**
- Derive Lamé parameters from seismic velocities
- Apply 2D stress-strain constitutive relationships
- Interpret strain measurements from geodetic observations
- Use eigenvalue decomposition to find principal stresses

---

## 1. Introduction: Why Stress and Strain Matter in Seismology

Seismic waves propagate through Earth because rocks are **elastic materials** that deform under stress and recover their shape. Understanding the relationship between:
- **Stress** (force per unit area, Pa) — what causes deformation
- **Strain** (dimensionless fractional deformation) — the response

...allows us to connect seismic wave velocities to material properties and interpret earthquake-related ground deformation.

---

## 2. Elastic Constants and Seismic Velocities

### 2.1 The Lamé Parameters

For **isotropic, linearly elastic** materials, two parameters fully describe elastic behavior:

- **λ (lambda)**: First Lamé parameter (Pa)
- **μ (mu)**: Shear modulus (Pa)

These relate to seismic wave velocities:

$$v_p = \sqrt{\frac{\lambda + 2\mu}{\rho}}$$

$$v_s = \sqrt{\frac{\mu}{\rho}}$$

where:
- $v_p$ = P-wave velocity (m/s)
- $v_s$ = S-wave velocity (m/s)  
- $\rho$ = density (kg/m³)

### 2.2 Deriving Lamé Parameters from Velocities

Starting from the S-wave equation:

$$\mu = \rho v_s^2$$

Substituting into the P-wave equation and solving for λ:

$$\lambda = \rho v_p^2 - 2\mu = \rho v_p^2 - 2\rho v_s^2$$

$$\boxed{\lambda = \rho(v_p^2 - 2v_s^2)}$$

**Example:** At 5 km depth in California:
- $v_p = 6000$ m/s, $v_s = 3500$ m/s, $\rho = 2700$ kg/m³
- $\mu = 2700 \times (3500)^2 = 3.31 \times 10^{10}$ Pa = **33.1 GPa**
- $\lambda = 2700 \times (6000^2 - 2 \times 3500^2) = 3.08 \times 10^{10}$ Pa = **30.8 GPa**

**Physical Insight:** Typical crustal rocks have μ ≈ 30 GPa, comparable to structural steel!

---

## 3. The Stress-Strain Relationship (Hooke's Law)

### 3.1 General 3D Form

For small deformations, stress and strain are linearly related:

$$\sigma_{ij} = \lambda \epsilon_{kk} \delta_{ij} + 2\mu \epsilon_{ij}$$

where:
- $\sigma_{ij}$ = stress tensor (Pa)
- $\epsilon_{ij}$ = strain tensor (dimensionless)
- $\epsilon_{kk} = \epsilon_{11} + \epsilon_{22} + \epsilon_{33}$ = trace (volumetric strain)
- $\delta_{ij}$ = Kronecker delta (1 if i=j, 0 otherwise)

### 3.2 Simplification to 2D (Horizontal Deformation)

For **horizontal plane strain** (neglecting vertical stress), we work with 2×2 tensors:

$$\sigma_{11} = \lambda(\epsilon_{11} + \epsilon_{22}) + 2\mu\epsilon_{11}$$

$$\sigma_{22} = \lambda(\epsilon_{11} + \epsilon_{22}) + 2\mu\epsilon_{22}$$

$$\sigma_{12} = 2\mu\epsilon_{12} = \sigma_{21}$$

**Indices convention:**
- 1 = **East**
- 2 = **North**
- 12 = shear component

---

## 4. Physical Meaning of Strain Measurements

### 4.1 Geodetic Strain: GPS/GNSS Networks

Modern seismology uses **Global Navigation Satellite Systems** (GPS/GNSS) to measure ground displacements with millimeter precision:

- **Continuous stations** (like Pinon Flat Observatory) track daily positions
- Over years/decades, we measure **displacement rates** (mm/yr)
- Convert to **strain rates** using spatial gradients: $\epsilon_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)$

### 4.2 Typical Strain Values

**Order of magnitude:**
- **Tectonic strain rates:** ~$10^{-7}$ to $10^{-8}$ per year
  - Example: 0.1 μstrain/yr = $0.1 \times 10^{-6}$/yr
  - Over 1000 years: ~$10^{-4}$ total strain
  
- **Earthquake-induced strain:** ~$10^{-6}$ to $10^{-4}$ (sudden)
  - Example: 1992 Landers M7.3 earthquake caused strains of $-0.26 \times 10^{-6}$ (compression) to $+0.92 \times 10^{-6}$ (extension) 80 km away

**Key Point:** A strain of $\epsilon = 10^{-6}$ means:
- A 1 km distance changes by **1 mm**
- A 1 m rock sample changes by **1 μm**

### 4.3 InSAR: Imaging Earthquakes from Space

Interferometric Synthetic Aperture Radar (InSAR) provides spatially dense strain measurements:
- Compares satellite radar images before/after earthquakes
- Measures line-of-sight ground displacement (cm precision)
- Creates 2D strain maps across entire fault zones

---

## 5. Principal Stresses: The Eigenvalue Problem

### 5.1 Why Eigenvalues?

The stress tensor $\sigma_{ij}$ describes stress on **arbitrary orientations**. But there exist special directions where:
- **Only normal stress** acts (no shear)
- These are the **principal stress directions**

Mathematically, we seek eigenvectors $\mathbf{v}$ such that:

$$\sigma_{ij} v_j = \lambda_{\text{eig}} v_i$$

or in matrix form: $\mathbf{\sigma}\mathbf{v} = \lambda_{\text{eig}}\mathbf{v}$

### 5.2 Physical Meaning

- **Eigenvalues** $\lambda_1, \lambda_2$: magnitudes of principal stresses (Pa)
  - $\lambda_1 > \lambda_2$: maximum and minimum principal stresses
  
- **Eigenvectors** $\mathbf{v}_1, \mathbf{v}_2$: orientations of principal stresses
  - Express as **azimuth** (angle from North, clockwise)

### 5.3 Example: Landers Earthquake Stress Field

From measured strain at Pinon Flat:
$$\epsilon = \begin{pmatrix} -0.26 & -0.69 \\ -0.69 & 0.92 \end{pmatrix} \times 10^{-6}$$

Calculate stress using $\sigma = \lambda \text{tr}(\epsilon) \mathbf{I} + 2\mu \epsilon$:
$$\sigma \approx \begin{pmatrix} -9.5 & -45.6 \\ -45.6 & 50.3 \end{pmatrix} \text{ kPa}$$

Eigenvalue decomposition gives:
- **Principal stresses:** $\sigma_1 \approx 60$ kPa (tension), $\sigma_2 \approx -19$ kPa (compression)
- **Orientation:** $\sigma_1$ at ~N30°E (NE-SW extension, typical for Landers)

### 5.4 Computing Eigenvalues in Python

```python
import numpy as np
from numpy import linalg as la

# Define 2D stress tensor
sigma = np.array([[s11, s12], 
                  [s12, s22]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = la.eig(sigma)

# Convert eigenvector to azimuth (degrees clockwise from North)
azimuth = np.degrees(np.arctan2(eigenvectors[0, 0], eigenvectors[1, 0]))
```

---

## 6. Applications to Earthquake Cycle

### 6.1 Interseismic Strain Accumulation

Between earthquakes, tectonic plate motion loads stress onto locked faults:
- GPS measures **steady strain rates** (~0.1 μstrain/yr)
- Over centuries, accumulated stress $\sigma = \lambda \text{tr}(\epsilon) + 2\mu\epsilon$ can reach **MPa levels**
- When stress exceeds fault strength (~10-100 MPa), rupture occurs

### 6.2 Coseismic Stress Changes

During earthquakes:
- **Sudden strain release** on fault plane
- **Stress redistribution** to surrounding regions (static stress changes)
- Can trigger aftershocks where stress increased

### 6.3 Postseismic Relaxation

After large earthquakes:
- Viscoelastic relaxation in lower crust/upper mantle
- Time-dependent strain evolution (months to decades)
- Measured by continuous GPS networks

---

## 7. Key Takeaways

1. **Lamé parameters** (λ, μ) connect seismic velocities to elastic response:
   - $\mu = \rho v_s^2$  
   - $\lambda = \rho(v_p^2 - 2v_s^2)$

2. **Stress-strain relationship** (Hooke's Law):
   - $\sigma_{ij} = \lambda \epsilon_{kk}\delta_{ij} + 2\mu\epsilon_{ij}$

3. **Geodetic strain** from GPS/InSAR:
   - Tectonic: ~$10^{-7}$/yr  
   - Earthquake: ~$10^{-6}$ (sudden)

4. **Principal stresses** from eigenvalue decomposition:
   - Magnitudes: eigenvalues (Pa)
   - Orientations: eigenvectors (azimuth)

5. **Earthquake cycle interpretation:**
   - Interseismic accumulation → coseismic release → postseismic relaxation

---

## References & Further Reading

- **Shearer (2009):** *Introduction to Seismology*, Chapter 2 (Stress and Strain)
- **Aki & Richards (2002):** *Quantitative Seismology*, Chapter 2
- **Stein & Wysession (2003):** *An Introduction to Seismology, Earthquakes, and Earth Structure*, Chapter 3
- **Pinon Flat Observatory:** https://scripps.ucsd.edu/labs/agnew/data/pfo/
- **1992 Landers Earthquake:** Wald & Heaton (1994), *BSSA*

---

**Next:** Apply these concepts to real Pinon Flat Observatory data in today's test exercise!
