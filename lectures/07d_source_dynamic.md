# Lecture: Earthquake Source Dynamics

## Learning objectives

- **Directivity**: Explain how rupture velocity $V_r$ deforms observed STFs and biases inferred corner frequency with azimuth.
- **Stress drop from spectra**: Connect corner frequency $f_c$ to source radius $r$ and show why the Brune $k$-factor and $V_r$ contaminate $\Delta\sigma$.
- **Radiated energy & apparent stress**: Define $E_R$ and $\sigma_a = \mu E_R / M_0$ as dynamic measures of the energy budget.
- **Energy budget**: Write the balance $\Delta E_\text{strain} = E_R + E_G + E_H$ and identify where fracture energy $G$ enters.
- **Modern context**: Recognize that much scatter in catalog stress drops reflects inversion assumptions and STF complexity rather than physical variability.

📖 *Shearer reference:* Sections 9.7 (source spectra) and 10.3 (radiated energy)

---

## 1. The observable: source time function and source spectrum

The **source time function (STF)** $\dot{M}(t)$ is the moment-rate function recovered after removing path and site effects from observed waveforms. Its Fourier transform is the **source spectrum**:

$$
\tilde{\dot{M}}(f) = \int_{-\infty}^{\infty} \dot{M}(t)\, e^{-2\pi i f t}\, dt.
$$

The **$\omega$-square (Brune) model** predicts that the displacement spectrum $|\tilde{u}(f)|$ is flat below the corner frequency $f_c$ and falls as $f^{-2}$ above it. The long-period plateau gives $M_0$; the corner frequency $f_c$ encodes source size.

```{note}
The mapping STF duration → source size is only valid under the simplest rupture models.
Real STFs are more complex.  The companion notebook lets you explore what "complexity"
does to $f_c$ estimates.
```

---

## 2. Rupture velocity and directivity

For a unilateral rupture propagating at velocity $V_r$, observers in different directions see different STF durations. A minimal Doppler-like relation is:

$$
\boxed{T_\text{obs}(\theta) \approx T_0\!\left(1 - \frac{V_r}{c}\cos\theta\right),
\qquad f_{c,\text{obs}}(\theta) \sim \frac{1}{T_\text{obs}(\theta)}}
$$

where $c$ is the relevant wave speed ($\beta$ for S-wave intuition) and $\theta$ is the angle from the rupture propagation direction.

| $V_r$ | $\theta = 0°$ (forward) | $\theta = 180°$ (backward) |
|---|---|---|
| $V_r \to 0$ | $T_\text{obs} \approx T_0$, no bias | same |
| $V_r = 0.6\,c$ | $T_\text{obs} = 0.4\,T_0$ (compressed) | $T_\text{obs} = 1.6\,T_0$ (stretched) |

```{warning}
If you ignore directivity, a higher $f_c$ observed in the forward direction will be
misinterpreted as a **smaller source radius and higher stress drop**.
This is one of the most common sources of systematic error in spectral stress-drop
studies {cite:p}`Ji2022`.
```

The directivity signature is **azimuthal variation of $f_c$**: a single event shows systematically higher $f_c$ in the forward direction and lower $f_c$ in the backward direction, while the long-period plateau ($M_0$) remains the same.

---

## 3. Stress drop from corner frequency

For a **circular rupture** the Brune-style scaling relates $M_0$, source radius $r$, and stress drop $\Delta\sigma$:

$$
\Delta\sigma \approx \frac{7}{16}\,\frac{M_0}{r^3}, \qquad r \approx k\,\frac{\beta}{f_c}.
$$

Because $\Delta\sigma \propto f_c^3$, a 20% overestimate of $f_c$ inflates $\Delta\sigma$ by $(1.20)^3 \approx 1.7\times$.

```{note}
{cite:t}`Kilgore2025` showed using laboratory experiments that frictional slip unsteadiness
introduces apparent scatter in spectral stress-drop even when the true on-fault stress drop
is controlled.  {cite:t}`Lin2025` demonstrated numerically that for rate-and-state fault
simulations the Brune $k$ factor is not constant — it depends on the dynamic rupture trajectory.
```

**Key message:** Spectral stress drop is powerful but is systematically sensitive to the choice of $k$, $V_r$, and the assumed spectral model. {cite:t}`Ji2022` showed that incorporating radiated energy $E_R$ constrains this degeneracy.

---

## 4. Radiated energy and apparent stress

**Radiated energy** $E_R$ is the total seismic energy carried away in far-field waves. To avoid the full wavefield integral we define the **apparent stress**:

$$
\boxed{\sigma_a \equiv \mu\,\frac{E_R}{M_0}.}
$$

$\sigma_a$ is a *dynamic* measure: it is sensitive to high-frequency radiation and to energy partitioning at the fault. Two earthquakes with the same $M_0$ but different rupture styles can have very different $\sigma_a$.

```{note}
Observations consistently show $\sigma_a \ll \overline{\Delta\sigma}$ for natural earthquakes,
implying most released strain energy goes to heat and fracture rather than radiation.
Laboratory stick-slip events with controlled friction can approach higher radiation
efficiencies {cite:p}`Kilgore2025`.
```

---

## 5. Energy budget

A minimal energy balance for a seismic rupture is:

$$
\boxed{\Delta E_\text{strain} = E_R + E_G + E_H}
$$

where $E_G$ is **fracture energy** (breakdown work at the rupture front) and $E_H$ is **frictional heat** (far-field dissipation). The **radiation efficiency** $\eta_R = E_R / (E_R + E_G)$ quantifies how much of the non-heat energy is radiated.

In the **slip-weakening framework**, fracture energy per unit area is:

$$
G = \int_0^{D_c} \!\left[\tau(\delta) - \tau_r\right] d\delta,
$$

where $D_c$ is the weakening distance, $\tau(\delta)$ is the shear strength as slip accumulates, and $\tau_r$ is the residual (dynamic) frictional stress. {cite:t}`Cocco2023` provides a comprehensive review of how $G$ is measured and how it scales with event size.

```{warning}
"Missing energy" in the budget — the gap between $\Delta E_\text{strain}$ and $E_R$ — is
often large and poorly constrained.  It reflects our incomplete knowledge of $D_c$ and
the friction law operating during rapid, large-amplitude slip.
```

---

## 6. STF complexity and its observational consequences

Natural STFs are rarely simple Brune pulses. Sub-event complexity (multiple asperity ruptures, stopping phases, healing fronts) modifies the spectrum above $f_c$:

- Adding a second sub-event separated by $\Delta t$ creates spectral notches at $f = n / \Delta t$.
- The apparent $f_c$ estimated from a single-corner fit may be biased high or low.
- {cite:t}`Neely2024` showed that STF complexity systematically biases stress-drop estimates and can generate apparent magnitude trends that are in fact complexity trends.

**Implication:** reported trends of increasing $\Delta\sigma$ with magnitude in some catalogs may partly reflect the greater complexity of large events rather than physical variation in on-fault conditions.

---

## Check your understanding

1. A network observes $f_c = 0.5$ Hz in the forward direction and $f_c = 0.2$ Hz in the backward direction for the same event. Estimate $V_r / c$ assuming unilateral rupture.
2. $f_c$ is overestimated by 30% due to directivity. By what factor is $\Delta\sigma$ overestimated?
3. Two $M_w\, 6$ earthquakes share the same $M_0$ but one has $\sigma_a$ three times larger. What must differ?
4. In the energy budget, if $E_G$ increases while $M_0$ is held fixed, what happens to $\eta_R$?
5. Explain in one sentence why catalog scatter in $\Delta\sigma$ does not necessarily imply physical variability in on-fault stress release.

---

## What we deliberately did not cover

- Full waveform inversion for dynamic rupture parameters
- Rate-and-state friction derivations and thermal pressurization models of $D_c$
- Off-fault damage effects on the energy budget
- Finite-fault slip models and their relationship to spectral $f_c$

---

## Looking ahead

The companion notebook (Lab 7d) lets you build synthetic STFs, apply the toy-directivity warp, estimate $f_c$ from spectra, compute a radiated-energy proxy, and explore the energy-budget sandbox — all with the equations developed here.

---

## Reading

📖 *Shearer:* Sections 9.7, 10.3

- {cite:t}`Cocco2023` — fracture energy and breakdown work (comprehensive review)
- {cite:t}`Ji2022` — reconciling spectral stress-drop variability via $E_R$
- {cite:t}`Kilgore2025` — laboratory stress drop and spectral estimates
- {cite:t}`Lin2025` — dynamic simulation stress-drop estimates on rate-and-state faults
- {cite:t}`Neely2024` — STF complexity and stress-drop bias

---

## References

```{bibliography}
:filter: docname in docnames
```
