# Radiation Patterns in a Homogeneous Whole Space
### Far-Field Body Waves and Focal Geometry

---

## Learning Objectives

By the end of this lecture and lab, students should be able to:

- Derive and interpret the **far-field P and S displacement expressions** for a point moment tensor.
- Explain how the radiation pattern emerges from tensor–geometry interactions.
- Predict nodal planes and polarity quadrants for a double-couple source.
- Distinguish P and S radiation symmetries.
- Connect radiation patterns to focal mechanisms (“beach balls”).

---

## 1. From Moment Tensor to Far-Field Waves

For a homogeneous whole space, the **far-field P-wave displacement** from a moment tensor source is:

$$
u_i^P(\mathbf{x}, t) =
\frac{1}{4\pi \rho \alpha^3}
\frac{x_i x_j x_k}{r^3}
\frac{1}{r}
\dot{M}_{jk}(t - r/\alpha)
$$

(ITS Eq. 9.21)

### Assumptions

- Homogeneous, isotropic medium
- Point source
- Far-field (1/r term retained, 1/r² neglected)
- Body waves only

### What breaks this?

- Near-field observations
- Strong heterogeneity
- Extended finite fault sources
- Surface wave dominance

---

## 2. Geometry Controls Amplitude

For a double-couple in the (x₁,x₂) plane with slip in x₁:

$$
u_P \propto \sin 2\theta \cos \phi
$$

(ITS Eq. 9.24)

### Immediate Observations

- Nodal planes occur where amplitude = 0
- Four quadrants (compressional/dilatational)
- Purely geometric dependence
- Independent of distance (after 1/r scaling)

---

## 3. S-Wave Radiation

Far-field S displacement:

$$
u_i^S =
\frac{1}{4\pi \rho \beta^3}
(\delta_{ij} - \gamma_i \gamma_j)
\gamma_k
\frac{1}{r}
\dot{M}_{jk}(t - r/\beta)
$$

(ITS Eq. 9.25)

Key difference:

- No nodal planes
- Six nodal points
- Vector polarization matters

---

## 4. Physical Interpretation

Radiation pattern is:

> A projection of the moment tensor onto the takeoff direction.

It reflects:

- Fault normal
- Slip direction
- Symmetry of M
- Not Earth structure (in this ideal case)

---

## 5. Beach Balls as Projections

Beach balls are:

- Lower hemisphere projections
- Shaded = compressional quadrant
- Defined by nodal planes

Important:

> Radiation pattern → polarity map → focal mechanism

---

## Check Your Understanding

1. Why does far-field displacement scale as 1/r?
2. Why do double-couples produce four quadrants?
3. Why does isotropic source have no nodal planes?
4. Why are S-wave nodal structures fundamentally different?
