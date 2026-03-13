# Lecture: Earthquake Nucleation and Dynamic Rupture

```{note}
This lecture was AI generated with scanned images of hand written notes, but it has not been iterated on. I noticed hallucinations in the graph and remaining challenges in explaining the flow. I will iterate on it.
```

## Learning objectives

- **Instability**: Explain why earthquakes nucleate as a frictional instability on faults.
- **Spring–slider model**: Describe how elastic stiffness and frictional weakening interact to produce runaway slip.
- **Nucleation zone**: Define the critical patch size required for dynamic rupture to begin.
- **Propagation vs. arrest**: Explain why some ruptures grow while others stop, using an energy-balance argument.

📖 *Shearer reference:* Chapter 10 (earthquake mechanics), handwritten notes from *Eric Dunham*, chapters 9-12 of *Source Mechanisms of Earthquakes* from Udias, Madariaga, Buforn.

---

## Context and scope

In Module 7d we quantified stress drop $\Delta\sigma$, radiated energy $E_R$, and fracture energy $G$ from seismic spectra. Those are **observational summaries** of what the source did. Here we ask: *what physical mechanism makes slip unstable in the first place?*

This lecture moves from **kinematics** (prescribing slip) to **dynamics** (predicting slip from first principles). We introduce the simplest models that capture fault instability and use them to build intuition for nucleation, propagation, and arrest.

**Connections to other modules:**

- **Module 2 (Stress & Strain):** The elastic stiffness $k$ of the spring–slider is the 1-D analog of the shear modulus $\mu$ and fault geometry that govern stress transfer.
- **Module 7d (Source Dynamics):** The energy budget $\Delta E_\text{strain} = E_R + E_G + E_H$ and the slip-weakening fracture energy $G = \tfrac{1}{2}(\tau_s - \tau_d)\,D_c$ were introduced there; here we use them to derive an instability criterion.
- **Module 7a (Moment Tensors):** Seismic moment $M_0 = \mu A \bar{D}$ quantifies the *result* of rupture; this lecture explains why $\bar{D}$ is not zero.

---

## 1. From kinematics to dynamics

Students already know how to describe earthquake sources:

- **Stress drop** $\Delta\sigma$ — the difference between initial and final stress on the fault.
- **Seismic moment** $M_0 = \mu A \bar{D}$.
- **Source time functions** $\dot{M}(t)$ — the moment-rate history.
- **Rupture velocity** $V_r$ — how fast the rupture front propagates.

These are all *kinematic* quantities: they tell us **what happened** but not **why it happened**.

```{note}
Kinematic source models prescribe slip as a function of space and time.
Dynamic models solve for slip from the equations of motion plus a friction law —
the slip history is an *output*, not an input.
```

**Key question:** Why did slip start in the first place?

To answer this, we need to understand the competition between two processes:

1. **Elastic loading** — tectonic forces that increase stress on the fault.
2. **Frictional resistance** — the fault's strength that resists slip.

---

## 2. Energy budget revisited

Recall from Module 7d that the energy released during an earthquake partitions as:

$$
\boxed{\Delta E_\text{strain} = E_R + E_G + E_H}
$$

where $E_R$ is radiated seismic energy, $E_G$ is fracture (breakdown) energy at the rupture tip, and $E_H$ is frictional heat.

Stress drop describes the **change in stress state**, but stress drop alone does **not determine whether rupture starts**. A fault can have high stress without slipping — what matters is whether the system is **mechanically unstable**.

**Conceptual question:**

> *What determines whether slip accelerates or stops?*

The answer: the competition between the rate at which friction weakens during slip and the rate at which elastic stress drops as the fault relaxes. The simplest model that captures this competition is the **spring–slider system**.

---

## 3. The spring–slider instability

```{figure} scripts/figures/fig_spring_slider_schematic.png
---
name: fig-spring-slider
alt: Schematic of a spring-slider model showing a rigid plate driving a block through a spring on a frictional surface.
---
The spring–slider model: a rigid plate moving at velocity $v_{pl}$ loads a frictional block through a spring of stiffness $k$. Slip $\delta$ relieves elastic stress.
```

The block-on-a-spring is the simplest mechanical analog of a fault loaded by tectonic motion. The **driving stress** on the block is:

$$
\boxed{\tau = k\,(v_{pl}\,t - \delta)}
$$

where $k$ is the elastic stiffness of the spring, $v_{pl}$ is the plate velocity, and $\delta$ is the accumulated slip. The spring stores elastic energy; slip releases it.

The block slips when the driving stress exceeds the frictional strength $\tau_f$. The key insight is what happens *during* slip.

### Stability depends on the interplay of two slopes

```{figure} scripts/figures/fig_weakening_vs_unloading.png
---
name: fig-weakening-unloading
alt: Two-panel diagram comparing unstable and stable fault behavior based on the relative slopes of frictional weakening and elastic unloading.
---
**(a)** When friction weakens faster than elastic stress drops (weak spring), slip is unstable — it runs away. **(b)** When the spring is stiff enough, elastic unloading outpaces frictional weakening and slip is stable. The instability criterion is $|d\tau_f/d\delta| > k$.
```

As the block slips by an increment $d\delta$:

- **Friction** decreases at rate $d\tau_f / d\delta$ (frictional weakening).
- **Elastic stress** decreases at rate $k$ (spring unloading).

If friction drops **faster** than elastic stress:

$$
\left|\frac{d\tau_f}{d\delta}\right| > k \quad \Longrightarrow \quad \text{runaway instability (earthquake)}
$$

If the spring is stiff enough that elastic unloading outpaces weakening:

$$
\left|\frac{d\tau_f}{d\delta}\right| < k \quad \Longrightarrow \quad \text{stable sliding (creep)}
$$

```{note}
Instability is not just about friction — it depends on the **elastic stiffness of the loading system**. The same friction law can produce earthquakes or stable creep depending on the fault's elastic environment.
```

This is the **fundamental instability criterion** that governs earthquake nucleation.

---

## 4. Slip-weakening friction

The simplest friction law that produces instability is the **linear slip-weakening model** {cite:p}`Ida1972`:

```{figure} scripts/figures/fig_slip_weakening_law.png
---
name: fig-slip-weakening
alt: Shear stress versus slip showing linear decrease from static strength to dynamic strength over critical slip distance Dc, with fracture energy G shaded.
---
Linear slip-weakening friction: strength drops from peak $\tau_s$ to residual $\tau_d$ over a characteristic slip distance $D_c$. The shaded area is the fracture energy $G$.
```

Two strength levels define the model:

- $\tau_s$ — **static (peak) strength**: the stress required to initiate slip.
- $\tau_d$ — **dynamic (residual) strength**: the stress during sustained sliding.

The transition occurs over a characteristic **critical slip distance** $D_c$. The fracture energy per unit area is the work done against friction in excess of the dynamic level:

$$
\boxed{G = \frac{1}{2}(\tau_s - \tau_d)\,D_c}
$$

This is exactly the fracture energy $G$ that appeared in the energy budget of Module 7d {cite:p}`Cocco2023`.

**Physical interpretation:** Slip must accumulate over $D_c$ before the fault fully weakens. This delay controls *how large* a patch must slip before instability can develop.

**Conceptual question:**

> *What happens if $D_c$ is large?*

A large $D_c$ means more slip is needed before full weakening — it becomes **harder to nucleate** an earthquake. The fault is "tougher" and requires a larger initial slipping region to go unstable.

---

## 5. The nucleation process

Real faults are not zero-dimensional spring-sliders — they are spatially extended. Earthquakes do not start everywhere on the fault simultaneously. Instead, nucleation proceeds through distinct stages {cite:p}`Dieterich1992`:

```{figure} scripts/figures/fig_nucleation_stages.png
---
name: fig-nucleation-stages
alt: Four-panel diagram showing the stages of earthquake nucleation from a locked fault to dynamic rupture.
---
Stages of earthquake nucleation: (1) the fault is locked under tectonic loading; (2) a small patch begins to slip; (3) the slipping region expands to a critical size $L_c$; (4) dynamic rupture initiates and propagates rapidly.
```

### Stage 1 — Locked fault
The fault is loaded by tectonic motion. Stress builds uniformly (or nearly so).

### Stage 2 — Small slipping patch
A localized region begins to slip where stress is highest or friction is lowest. Slip is slow and quasi-static.

### Stage 3 — Critical size
The slipping patch expands as it transfers stress to its edges. When it reaches a **critical nucleation length** $L_c$, the energy released by further growth exceeds the fracture cost.

### Stage 4 — Dynamic rupture
The patch transitions to rapid, dynamic rupture. Seismic waves are radiated.

```{warning}
The critical nucleation length $L_c$ depends on material properties ($\mu$), the friction parameters ($\tau_s$, $\tau_d$, $D_c$), and the stress state. It is typically estimated as:

$$L_c \propto \frac{\mu\, D_c}{(\tau_s - \tau_d)^2}$$

For typical crustal parameters, $L_c$ ranges from meters to hundreds of meters.
```

**Key idea:** Earthquakes start locally, within a finite nucleation zone. The entire fault does not fail at once.

---

## 6. Propagation versus arrest

Once nucleation succeeds, the rupture front propagates outward. Whether it continues to grow or stops depends on an energy balance at the crack tip {cite:p}`Andrews1976`:

```{figure} scripts/figures/fig_energy_release_vs_fracture.png
---
name: fig-energy-balance
alt: Plot of energy release rate increasing with crack length, crossing a horizontal line representing fracture energy, defining the critical nucleation size.
---
The energy release rate $\mathcal{G}(a)$ increases with crack half-length $a$. Below the critical size $a_c$, the fracture energy $G_c$ exceeds the energy available and rupture arrests. Above $a_c$, energy release exceeds fracture cost and rupture propagates.
```

The **energy release rate** $\mathcal{G}$ measures how much stored elastic energy is liberated per unit advance of the crack front. For a mode-II (shear) crack of half-length $a$ under uniform stress drop $\Delta\sigma$:

$$
\mathcal{G} \propto \frac{\Delta\sigma^2 \, a}{\mu}
$$

Rupture propagates when:

$$
\boxed{\mathcal{G}(a) \geq G_c \quad \Longrightarrow \quad \text{rupture grows}}
$$

Below the critical size $a_c$ (defined by $\mathcal{G}(a_c) = G_c$):

- energy release is insufficient → **rupture arrests**

Above $a_c$:

- energy release exceeds cost → **rupture propagates**

**Implication for earthquake size:** Small slip patches arrest frequently. Only patches that reach the critical size $a_c$ can grow into large earthquakes. This is one reason why small earthquakes vastly outnumber large ones.

---

## 7. Real faults: beyond simple models

The homogeneous models above capture the core physics, but real faults are far more complex:

| Feature | Effect on nucleation and rupture |
|---|---|
| **Asperities** | Stress concentrations that can trigger local nucleation |
| **Heterogeneous stress** | Non-uniform initial conditions; rupture may jump or cascade |
| **Fluids and pore pressure** | Reduce effective normal stress; can promote or inhibit slip |
| **Fault geometry** | Bends, branches, and step-overs can arrest or redirect rupture |
| **Rate-and-state friction** | More realistic friction law; velocity- and state-dependent |

```{warning}
The spring–slider and slip-weakening models are pedagogical idealizations. Real earthquake nucleation may involve slow slip, foreshocks, cascading micro-failures, or fluid-driven transients. But the **core instability mechanism** — frictional weakening outpacing elastic unloading — remains the same.
```

---

## Check your understanding

1. Two faults have the same stress drop $\Delta\sigma$. Fault A has $D_c = 0.1$ m and Fault B has $D_c = 1.0$ m. Which fault is harder to nucleate an earthquake on, and why?

2. A fault has slip-weakening friction with $\tau_s - \tau_d = 5$ MPa. If the elastic stiffness of the surrounding rock (per unit fault area) is 10 MPa/m, and the weakening rate is $(\tau_s - \tau_d)/D_c = 6$ MPa/m, is the system stable or unstable?

3. Explain in one sentence why stress drop alone does not predict whether a fault will produce an earthquake.

4. Using the energy balance framework, explain why small earthquakes are far more common than large ones.

5. In the spring–slider model, what happens if you *increase* the spring stiffness $k$ while keeping the friction law fixed?

---

## What we deliberately did not cover

- **Rate-and-state friction** — the more complete friction framework that includes velocity and state dependence {cite:p}`Dieterich1979,Ruina1983`
- **Dynamic rupture simulation** — numerical methods for solving the full elastodynamic problem on heterogeneous faults
- **Supershear rupture** — ruptures that exceed the shear wave speed
- **Thermal pressurization** — feedback between frictional heating, pore fluid pressure, and weakening
- **Crack-like vs. pulse-like rupture** — different modes of rupture propagation

---

## Looking ahead

The companion notebook (Lab 8) lets you simulate the spring–slider instability, visualize slip-weakening friction for different parameter choices, and explore how the critical nucleation size $L_c$ depends on fault properties.

In the final lecture (Module 9) we step back to see the full architecture of the course — how every module connects — and survey five research frontiers (ML/AI, DAS, earthquake early warning, slow earthquakes, and planetary seismology) that directly extend the concepts developed here.

---

## Reading

📖 *Shearer:* Chapter 10 (earthquake mechanics overview)

- {cite:t}`Scholz2019` — comprehensive textbook treatment of earthquake mechanics, friction, and faulting
- {cite:t}`Ida1972` — the original slip-weakening cohesive zone model for shear cracks
- {cite:t}`Andrews1976` — dynamic rupture solutions with slip-weakening friction
- {cite:t}`Dieterich1992` — earthquake nucleation on faults with rate- and state-dependent friction
- {cite:t}`Cocco2023` — comprehensive review of fracture energy and breakdown work (bridges to Module 7d)

---

## References

```{bibliography}
:filter: docname in docnames
```
