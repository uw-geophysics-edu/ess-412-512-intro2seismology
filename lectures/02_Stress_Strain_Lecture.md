# Stress and Strain: Elastic Properties of Earth Materials

**Duration:** 30 minutes
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


## 2. Geometry of Forces in a Continuum: Traction and Stress

Before introducing elastic constants or constitutive laws, we must understand **how forces act inside a continuous medium**. Stress is not defined on volumes or points in isolation, but on **oriented surfaces** embedded within the material.


---

### 2.1 Traction: Force Acting on an Oriented Surface

Consider an infinitesimal surface element of area ΔA inside a solid. This surface is characterized by a **unit normal vector**
 $$
 \hat{\mathbf{n}}
 $$
which defines its orientation.

The **traction vector** \(\mathbf{t}(\hat{\mathbf{n}})\) is defined as the force per unit area exerted across that surface:
$$
\mathbf{t}(\hat{\mathbf{n}}) = \lim_{\Delta A \to 0} \frac{\Delta \mathbf{F}}{\Delta A}
$$

Key properties:
- Traction is a **vector quantity**
- Traction **depends on surface orientation**
- For the opposite face, $\mathbf{t}(-\hat{\mathbf{n}}) = -\mathbf{t}(\hat{\mathbf{n}})$

This orientation dependence is fundamental: the same material point experiences **different tractions on differently oriented planes**.


---

### 2.2 Decomposition of Traction: Normal and Shear Stress

The traction vector can be decomposed into:

Normal stress:
$$
t_N = \mathbf{t} \cdot \hat{\mathbf{n}}
$$

Shear traction:
$$
\mathbf{t}_S = \mathbf{t} - t_N \hat{\mathbf{n}}
$$

By convention in seismology:
- **Extension is positive**
- **Compression is negative**


---

### 2.3 Stress Tensor as a Linear Mapping

Experiments and force balance arguments (Cauchy's theorem) show that the traction vector varies **linearly** with the surface normal. This motivates the definition of the **Cauchy stress tensor** $\boldsymbol{\sigma}$:

$$
\boxed{
\mathbf{t}(\hat{\mathbf{n}}) = \boldsymbol{\sigma}\,\hat{\mathbf{n}}
}
$$

In Cartesian coordinates:
$$
\boldsymbol{\sigma} =
\begin{pmatrix}
\sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\
\sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz}
\end{pmatrix}
$$

Interpretation:

Force balance (no net torque) requires:
$$
\sigma_{ij} = \sigma_{ji}
$$
so the stress tensor is **symmetric** and has six independent components.


---

### 2.4 Worked Example: Stress Acting on an Inclined Plane (2-D)

Consider a two-dimensional stress tensor:
$$
\boldsymbol{\sigma} =
\begin{pmatrix}
\sigma_{xx} & \sigma_{xy} \\
\sigma_{xy} & \sigma_{yy}
\end{pmatrix}
$$

Let a fault plane be oriented such that its unit normal is:
$$
\hat{\mathbf{n}} = (\cos\theta, \sin\theta)
$$

The traction acting across the fault is:
$$
\mathbf{t} = \boldsymbol{\sigma}\hat{\mathbf{n}}
$$

The normal and shear stresses on the fault are obtained by projection:
$$
t_N = \mathbf{t} \cdot \hat{\mathbf{n}}, \quad
t_S = \mathbf{t} \cdot \hat{\mathbf{f}}
$$
where $\hat{\mathbf{f}}$ is a unit vector parallel to the fault.

This geometric procedure—**stress → traction → normal/shear decomposition**—is central to fault mechanics, Coulomb stress, and earthquake triggering.


---
## 3. Geometry of Deformation: Strain vs. Motion

Stress describes internal forces. **Strain describes internal deformation.** The two are related, but conceptually distinct.

### 3.1 Displacement vs. Strain

The **displacement field** $\mathbf{u}(\mathbf{x})$ describes how points move:
$$
\mathbf{u} = (u_x, u_y, u_z)
$$

Strain measures **relative deformation**, not absolute motion. It is defined from spatial gradients of displacement.

Example: A 100 m long bar stretched uniformly to 101 m
$$
\epsilon = \frac{\Delta L}{L} = 0.01
$$


### 3.2 Infinitesimal Strain Tensor

The displacement gradient tensor can be decomposed into:

The infinitesimal strain tensor is:
$$
\boxed{
\epsilon_{ij} = \tfrac{1}{2}
\left(
\frac{\partial u_i}{\partial x_j}
 +
\frac{\partial u_j}{\partial x_i}
\right)
}
$$

- Only strain (not rigid rotation) produces stress
---

### 3.3 Physical Interpretation of Strain Components
- $\epsilon_{xy}$: shear strain (change in right angles)

Important geometric insight:
> Even “pure extension” produces shear strain when viewed in a rotated coordinate system.

This is why **principal strains** and eigenvectors play a central role in seismology.

---

### 3.4 Volumetric Strain and Rotation

The **dilatation** (relative volume change) is given by:
$$
\epsilon_v = \text{tr}(\boldsymbol{\epsilon})
= \epsilon_{xx} + \epsilon_{yy} + \epsilon_{zz}
= \nabla \cdot \mathbf{u}
$$

The antisymmetric part of the displacement gradient corresponds to **rigid-body rotation** and does **not** contribute to stress.
---

### Preview: Why This Geometry Matters
- Seismic waves, fault slip, and moment tensors all follow directly from these definitions

With this geometric foundation established, we can now introduce **constitutive relations** that link stress and strain in elastic materials.


---

## 4. Elastic Constants and Seismic Velocities
### 4.1 The Lamé Parameters

For **isotropic, linearly elastic** materials, two parameters fully describe elastic behavior:
- **μ (mu)**: Shear modulus (Pa)

These relate to seismic wave velocities:

$$v_p = \sqrt{\frac{\lambda + 2\mu}{\rho}}$$

$$v_s = \sqrt{\frac{\mu}{\rho}}$$

- $\rho$ = density (kg/m³)

### 4.2 Deriving Lamé Parameters from Velocities

Starting from the S-wave equation:

$$\mu = \rho v_s^2$$

Substituting into the P-wave equation and solving for λ:

$$\lambda = \rho v_p^2 - 2\mu = \rho v_p^2 - 2\rho v_s^2$$

$$\boxed{\lambda = \rho(v_p^2 - 2v_s^2)}$$

- $\lambda = 2700 \times (6000^2 - 2 \times 3500^2) = 3.08 \times 10^{10}$ Pa = **30.8 GPa**

**Physical Insight:** Typical crustal rocks have μ ≈ 30 GPa, comparable to structural steel!

---

## 5. The Stress-Strain Relationship (Hooke's Law)

### 5.1 General 3D Form

For small deformations, stress and strain are linearly related:

$$\sigma_{ij} = \lambda \epsilon_{kk} \delta_{ij} + 2\mu \epsilon_{ij}$$

- $\delta_{ij}$ = Kronecker delta (1 if i=j, 0 otherwise)

### 5.2 Simplification to 2D (Horizontal Deformation)

For **horizontal plane strain** (neglecting vertical stress), we work with 2×2 tensors:

$$\sigma_{11} = \lambda(\epsilon_{11} + \epsilon_{22}) + 2\mu\epsilon_{11}$$

$$\sigma_{22} = \lambda(\epsilon_{11} + \epsilon_{22}) + 2\mu\epsilon_{22}$$

$$\sigma_{12} = 2\mu\epsilon_{12} = \sigma_{21}$$

- 12 = shear component
---

## 6. Physical Meaning of Strain Measurements

### 6.1 Geodetic Strain: GPS/GNSS Networks

Modern seismology uses **Global Navigation Satellite Systems** (GPS/GNSS) to measure ground displacements with millimeter precision:
- Convert to **strain rates** using spatial gradients: $\epsilon_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)$

### 6.2 Typical Strain Values

- **Tectonic strain rates:** ~$10^{-7}$ to $10^{-8}$ per year
  - Example: 0.1 μstrain/yr = $0.1 \times 10^{-6}$/yr
  - Over 1000 years: ~$10^{-4}$ total strain
- **Earthquake-induced strain:** ~$10^{-6}$ to $10^{-4}$ (sudden)
  - Example: 1992 Landers M7.3 earthquake caused strains of $-0.26 \times 10^{-6}$ (compression) to $+0.92 \times 10^{-6}$ (extension) 80 km away

- A 1 m rock sample changes by **1 μm**

### 6.3 InSAR: Imaging Earthquakes from Space

- Creates 2D strain maps across entire fault zones
---

## 7. Principal Stresses: The Eigenvalue Problem

### 7.1 Why Eigenvalues?

- These are the **principal stress directions**

Mathematically, we seek eigenvectors $\mathbf{v}$ such that:

$$\sigma_{ij} v_j = \lambda_{\text{eig}} v_i$$

or in matrix form: $\mathbf{\sigma}\mathbf{v} = \lambda_{\text{eig}}\mathbf{v}$

### 7.2 Physical Meaning
- **Eigenvalues** $\lambda_1, \lambda_2$: magnitudes of principal stresses (Pa)
  - $\lambda_1 > \lambda_2$: maximum and minimum principal stresses
- **Eigenvectors** $\mathbf{v}_1, \mathbf{v}_2$: orientations of principal stresses
  - Express as **azimuth** (angle from North, clockwise)

### 7.3 Example: Landers Earthquake Stress Field

From measured strain at Pinon Flat:
$$\epsilon = \begin{pmatrix} -0.26 & -0.69 \\ -0.69 & 0.92 \end{pmatrix} \times 10^{-6}$$

Calculate stress using $\sigma = \lambda \text{tr}(\epsilon) \mathbf{I} + 2\mu \epsilon$:
$$\sigma \approx \begin{pmatrix} -9.5 & -45.6 \\ -45.6 & 50.3 \end{pmatrix} \text{ kPa}$$

- **Orientation:** $\sigma_1$ at ~N30°E (NE-SW extension, typical for Landers)

### 7.4 Computing Eigenvalues in Python

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

## 8. Applications to Earthquake Cycle

* Interseismic Strain Accumulation

- When stress exceeds fault strength (~10-100 MPa), rupture occurs

* Coseismic Stress Changes

- Can trigger aftershocks where stress increased

* 6.3 Postseismic Relaxation

- Measured by continuous GPS networks
---

## 9. Key Takeaways

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

## 10. References & Further Reading
- **1992 Landers Earthquake:** Wald & Heaton (1994), *BSSA*
