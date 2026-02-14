# Travel-Time Tomography: From Rays to Inversion

## Learning Objectives

After this lecture, students should be able to:

* Explain how **travel-time residuals** encode Earth structure
* Write travel-time tomography as a **linear inverse problem**
* Construct the **tomography matrix (G)** from ray geometry
* Explain **why the problem is ill-posed**
* Describe the role of **regularization**
* Understand why **ray bending makes tomography nonlinear**

This lecture builds directly on:

* ray tracing and ray bending
* Snell’s law and Fermat’s principle
* linear inverse problems

---

## 1. What Are We Measuring? (5 min)

### On the board

Draw:

* a source
* a receiver
* a ray path
* a layered or heterogeneous medium

Write:

$$
t_i^{\text{obs}}
\quad\text{and}\quad
t_i^0
$$

Define the **data**:

$$
d_i \equiv \delta t_i = t_i^{\text{obs}} - t_i^0
$$

### Say explicitly

* We **do not invert absolute travel times**
* We invert **residuals relative to a reference model**

### Physical meaning

* ($\delta t > 0$): slower than reference
* ($\delta t < 0$): faster than reference

### Concept check (ask students)

> If all arrivals at one station are late, what could that mean?

(velocity anomaly? station term? origin time?)

---

## 2. Forward Problem: Travel Time as an Integral (5–7 min)

### On the board

Start from ray theory:

$$
t = \int_{\Gamma} u(\mathbf{x})\, ds
\quad\text{with}\quad
u(\mathbf{x}) = \frac{1}{v(\mathbf{x})}
$$

Split the model:

$$
u(\mathbf{x}) = u_0(\mathbf{x}) + \delta u(\mathbf{x})
$$

Linearize:

$$
\delta t = \int_{\Gamma} \delta u(\mathbf{x})\, ds
$$

### Critical assumption (circle this)

**Rays are frozen in the reference model**

$$
\Gamma \approx \Gamma_0
$$

### Say out loud

* This is a **first-order (Born-like) approximation**
* Valid for **small perturbations**
* Ray bending enters later

### Concept check

> Why does Fermat’s principle justify freezing the ray path at first order?

---

## 3. Discretization: From Integrals to Sums (8 min)

### On the board

Draw:

* the domain divided into rectangular cells
* one ray crossing several cells

Write:

$$
\delta t_i
\approx
\sum_{j=1}^{M} L_{ij}\,\delta u_j
$$

Where:

* ($\delta u_j$): slowness perturbation in cell $j$
* ($L_{ij}$): path length of ray $i$ in cell $j$

### Matrix form (box this)

$$
\mathbf{d} = \mathbf{G}\mathbf{m}
$$

with:

* ($d_i = \delta t_i$)
* ($m_j = \delta u_j$)
* ($G_{ij} = L_{ij}$)

### Emphasize

* **All the physics is in $G$**
* $G$ is **geometry + ray paths**
* The inverse problem is bookkeeping, not magic

### Concept check

> What happens to $G$ in a cell that no ray crosses?

---

## 4. Why Tomography Is Hard (Ill-posedness) (6–8 min)

### On the board

Write the least-squares problem:

$$
\min_{\mathbf{m}} \|\mathbf{Gm} - \mathbf{d}\|_2^2
$$

Then the normal equations:

$$
(\mathbf{G}^T\mathbf{G})\mathbf{m} = \mathbf{G}^T\mathbf{d}
$$

### Discuss three failure modes

1. **Poor coverage**

   * columns of $G$ nearly zero
2. **Similar ray paths**

   * rows nearly linearly dependent
3. **Limited ray angles**

   * directional smearing

Draw elongated resolution kernels aligned with ray directions.

### Key message (underline)

> Tomography is limited by **ray geometry**, not by inversion technique.

---

## 5. Regularization: Making the Problem Solvable (8 min)

### Damping (minimum-norm)

Write:

$$
\min_{\mathbf{m}}
\|\mathbf{Gm}-\mathbf{d}\|^2
+
\lambda^2 \|\mathbf{m}\|^2
$$

Say:

* favors **small-amplitude anomalies**
* fills gaps with **zeros**

### Smoothness (minimum-roughness)

Write:

$$
\min_{\mathbf{m}}
\|\mathbf{Gm}-\mathbf{d}\|^2
+
\lambda^2 \|\mathbf{L}\mathbf{m}\|^2
$$

where $\mathbf{L}$ is a discrete Laplacian.

Say:

* favors **smooth Earth**
* fills gaps with **interpolation**

### Ask students

> Which regularization would you trust more in the mantle?
> In sedimentary basins?

---

## 6. P vs S Tomography (2–3 min)

### On the board

Write:

$$
\delta t_P = \int \delta u_P\, ds
\quad\text{and}\quad
\delta t_S = \int \delta u_S\, ds
$$

### Emphasize

* Mathematics is **identical**
* Differences are:

  * ray coverage
  * picking quality
  * sensitivity to fluids

### Key point

> P and S tomography differ in **data**, not in formulation.

---

## 7. Why Ray Bending Makes Tomography Nonlinear (5–7 min)

### On the board

Draw:

* straight ray through a low-velocity anomaly
* bent ray avoiding slow region

Write:

$$
t(u) = \int_{\Gamma(u)} u(\mathbf{x})\, ds
$$

Say clearly:

* $t$ depends on $u$
* **and** $\Gamma$ depends on $u$

### Linearization with iteration

At iteration $k$:

$$
\delta t^{(k)}
\approx
\int_{\Gamma^{(k)}} \delta u^{(k)}\, ds
$$

### Algorithm sketch (numbered)

1. Start with $u^{(0)}$
2. Trace rays $\Gamma^{(0)}$
3. Build $G^{(0)}$
4. Solve for $\delta u^{(0)}$
5. Update $u^{(1)} = u^{(0)} + \alpha \delta u^{(0)}$
6. Repeat

Circle:

$$
\text{model} \rightarrow \text{rays} \rightarrow G \rightarrow \text{update}
$$

---

## 8. Connection to the Notebook

### Tell students

* Part A notebook = **straight-ray tomography**
* Part B notebook = **iterative bent-ray tomography**
* PyKonal solves:

  * eikonal equation
  * ray tracing via $\nabla T$

### Prediction question

> What failure mode of straight-ray tomography does ray bending fix best?

---

## 9. Take-Home Messages (Final 2 min)

* Travel-time tomography is a **geometric inverse problem**
* $G$ is built from **ray paths**
* Ill-posedness is unavoidable → **regularization is physics**
* Straight-ray tomography is **linear but approximate**
* Bent-ray tomography is **more accurate but nonlinear**
* Resolution is controlled by **coverage, not clever math**

---

## What Comes Next

* Joint inversion with:

  * event locations
  * origin times
  * station terms
* Finite-frequency sensitivity kernels
* Comparison with surface-wave tomography

---

If you want next, I can:

* convert this into **ADA-compliant slides** with figures + alt-text
* add **marginal instructor notes** (what to emphasize live vs skip)
* write a **one-page student summary** that complements the notebook without duplicating it
# Travel-Time Tomography: From Rays to Inversion

## Learning Objectives

After this lecture, students should be able to:

* Explain how **travel-time residuals** encode Earth structure
* Write travel-time tomography as a **linear inverse problem**
* Construct the **tomography matrix (G)** from ray geometry
* Explain **why the problem is ill-posed**
* Describe the role of **regularization**
* Understand why **ray bending makes tomography nonlinear**

This lecture builds directly on:

* ray tracing and ray bending
* Snell’s law and Fermat’s principle
* linear inverse problems

---

## 1. What Are We Measuring? (5 min)

### On the board


* a source
* a receiver
$$
t^{\text{obs}}_i
\quad\text{and}\quad
t^0_i
$$
* a layered or heterogeneous medium

$$
d_i \equiv \delta t_i = t^{\text{obs}}_i - t^0_i
$$
\quad\text{and}\quad
t^0_i


Define the **data**:
$$
d_i \equiv \delta t_i = t^{\text{obs}}_i - t^0_i
$$

### Say explicitly

* We **do not invert absolute travel times**
* We invert **residuals relative to a reference model**

### Physical meaning

* ( $\delta t > 0$ ): slower than reference

### Concept check (ask students)

> If all arrivals at one station are late, what could that mean?

(velocity anomaly? station term? origin time?)
---

## 2. Forward Problem: Travel Time as an Integral (5–7 min)
$$
t = \int_{\Gamma} u(\mathbf{x})\, ds
\quad\text{with}\quad
u(\mathbf{x}) = \frac{1}{v(\mathbf{x})}
$$
### On the board


$$
u(\mathbf{x}) = u_0(\mathbf{x}) + \delta u(\mathbf{x})
\quad\text{with}\quad
u(\mathbf{x}) = \frac{1}{v(\mathbf{x})}
$$

Split the model:
$$
\delta t
= \int_{\Gamma} \delta u(\mathbf{x})\, ds
u(\mathbf{x}) = u_0(\mathbf{x}) + \delta u(\mathbf{x})
$$

Linearize $\delta t$:
$$
 \Gamma \approx \Gamma_0
$$


### Critical assumption (circle this)

Rays are frozen in the reference model
$$
\Gamma \approx \Gamma_0
$$

### Say out loud

* Valid for **small perturbations**
* Ray bending enters later

### Concept check

> Why does Fermat’s principle justify freezing the ray path at first order?

---

## 3. Discretization: From Integrals to Sums (8 min)
Draw:

$$
\delta t_i
\approx
\sum_{j=1}^{M} L_{ij}\,\delta u_j
$$
* one ray crossing several cells

Write:
$$
\delta t_i
\approx
\sum_{j=1}^{M} L_{ij},\delta u_j
$$
Where:
$$
\mathbf{d} = \mathbf{G}\mathbf{m}
$$
* $ \delta u_j $: slowness perturbation in cell (j)
* $ L_{ij} $: path length of ray (i) in cell (j)

### Matrix form (box this)

$$
\mathbf{d} = \mathbf{G}\mathbf{m}
$$

with:

*  $ d_i = \delta t_i $
*  $ m_j = \delta u_j $
*  $ G_{ij} = L_{ij} $

### Emphasize

* (G) is **geometry + ray paths**
* The inverse problem is bookkeeping, not magic

### Concept check

> What happens to (G) in a cell that no ray crosses?
---

## 4. Why Tomography Is Hard (Ill-posedness) (6–8 min)

Goal is to minimize the difference between observed and predicted data:
$$
\min_{\mathbf{m}} \|\mathbf{Gm} - \mathbf{d}\|_2^2
$$
$G$ is not square and full rank, so we calculate the *normal equation*:
$$
\mathbf{G}\mathbf{m} = \mathbf{d}
$$

$$
(\mathbf{G}^T\mathbf{G})\mathbf{m} = \mathbf{G}^T\mathbf{d}
$$

Then the normal equations:
$$
\mathbf{m} = (\mathbf{G}^T\mathbf{G})^{-1}\mathbf{G}^T\mathbf{d}
$$

### Discuss three failure modes

1. **Poor coverage**

   * columns of (G) nearly zero
2. **Similar ray paths**

   * rows nearly linearly dependent
3. **Limited ray angles**


Draw elongated resolution kernels aligned with ray directions.

### Key message (underline)

> Tomography is limited by **ray geometry**, not by inversion technique.
---


## 5. Regularization: Making the Problem Solvable (8 min)
$$
\min_{\mathbf{m}}
\|\mathbf{Gm}-\mathbf{d}\|^2
+
\lambda^2 \|\mathbf{m}\|^2
$$
### Damping (minimum-norm)

Write:
$$
\min_{\mathbf{m}}
|\mathbf{Gm}-\mathbf{d}|^2
+
\lambda^2 |\mathbf{m}|^2
$$
Say: Damping favors **small-amplitude anomalies**

### Smoothness (minimum-roughness)

Write:
$$
\min_{\mathbf{m}}
|\mathbf{Gm}-\mathbf{d}|^2
+
\lambda^2 |\mathbf{L}\mathbf{m}|^2
$$

where $ \mathbf{L} $ is a discrete Laplacian.


* favors **smooth Earth**
* fills gaps with **interpolation**


---

## 6. P vs S Tomography (2–3 min)

### On the board

Write:
$$
\delta t_P = \int \delta u_P, ds
\quad\text{and}\quad
\delta t_S = \int \delta u_S, ds
$$

### Emphasize

* Mathematics is **identical**

  * ray coverage
  * picking quality
  * sensitivity to fluids

### Key point

> P and S tomography differ in **data**, not in formulation.

---


$$
t(u) = \int_{\Gamma(u)} u(\mathbf{x})\, ds
$$

Draw:

* straight ray through a low-velocity anomaly
* bent ray avoiding slow region

Write:
$$
t(u) = \int_{\Gamma(u)} u(\mathbf{x}), ds
$$
Say clearly:

$$
\delta t^{(k)}
\approx
\int_{\Gamma^{(k)}} \delta u^{(k)}\, ds
$$
* **and** $\Gamma$ depends on $u$

### Linearization with iteration

At iteration (k):
$$
\delta t^{(k)}
\approx
\int_{\Gamma^{(k)}} \delta u^{(k)}, ds
$$


$$
	ext{model} \rightarrow \text{rays} \rightarrow G \rightarrow \text{update}
$$
2. Trace rays $\Gamma^{(0)}$
4. Solve for $\delta u^{(0)}$
5. Update $u^{(1)} = u^{(0)} + \alpha \delta u^{(0)}$
6. Repeat

Circle:
$$
\text{model} \rightarrow \text{rays} \rightarrow G \rightarrow \text{update}
$$

---

## 8. Connection to the Notebook

### Tell students

* Part A notebook = **straight-ray tomography**
* PyKonal solves:

  * eikonal equation
  * ray tracing via $\nabla T$

### Prediction question

> What failure mode of straight-ray tomography does ray bending fix best?

---
## 9. Take-Home Messages (Final 2 min)

* Travel-time tomography is a **geometric inverse problem**
* (G) is built from **ray paths**
* Ill-posedness is unavoidable → **regularization is physics**
* Straight-ray tomography is **linear but approximate**
* Bent-ray tomography is **more accurate but nonlinear**
* Resolution is controlled by **coverage, not clever math**

---


* Joint inversion with:

  * event locations
  * origin times
  * station terms
* Finite-frequency sensitivity kernels
* Comparison with surface-wave tomography
