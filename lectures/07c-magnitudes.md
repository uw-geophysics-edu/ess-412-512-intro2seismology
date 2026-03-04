# Earthquake Magnitudes

## Learning objectives
After this lecture, students should be able to:

- Explain magnitude as an **empirically calibrated regression** from seismogram observables to event size, not a single physical property.
- State what is measured for **$M_L$, $m_b$, $M_s$, $M_d/M_c$, $M_w$** and identify the typical band, phase, and distance regime for each.
- Predict when and why **saturation** occurs for amplitude-based magnitudes using the omega-square source spectrum.
- Interpret **magnitude disagreements** across catalogs in terms of band limits, depth, path/site corrections, and network calibration.
- Use magnitude *differences* as diagnostics for **source characterization** (e.g., explosion discrimination, harmonization to $M_w$).

---

## Context and scope

This lecture develops five principal magnitude estimates ($M_L$, $m_b$, $M_s$, $M_d/M_c$, $M_w$), examines their physical basis and calibration assumptions, and explains why they diverge — particularly through **saturation** of band-limited measurements. We connect these scales to the **omega-square source spectrum** to provide a unified physical framework for understanding when and why different magnitudes agree or disagree.

**Connections to other modules:**
- **Module 7 (Moment Tensors):** The scalar seismic moment $M_0$ obtained from moment tensor inversion is the observable underlying $M_w$.
- **Module 3 (Ray Theory):** Distance corrections $F(\Delta, h)$ rely on ray-theoretic models of geometrical spreading and attenuation along the propagation path.
- **Module 5 (Surface Waves):** $M_s$ is measured on Rayleigh waves; dispersion and excitation efficiency (particularly the depth dependence) directly affect surface-wave magnitude estimates.

This material corresponds primarily to **Shearer (2009), *Introduction to Seismology*, Section 9.7**.

---

## 1. Magnitude as distance calibration

Earthquake magnitude is defined through an empirical regression that maps a seismogram measurement to event size. The general form shared by most magnitude scales is:

$$M = \log_{10}(\text{measurement}) + F(\Delta, h) + S + C$$

where:
- $F(\Delta, h)$ is a **distance and depth correction** that accounts for geometrical spreading and anelastic attenuation along the propagation path
- $S$ is a **station/site term** that absorbs local amplification or deamplification effects (often implicit or averaged across the network)
- $C$ is a **reference constant** that anchors the scale to a chosen normalization
- "measurement" denotes the seismogram observable: peak amplitude, amplitude-to-period ratio $A/T$, coda duration, or seismic moment

The logarithmic form reflects the enormous dynamic range of earthquake ground motions — amplitudes span many orders of magnitude across event sizes.

```{note}
A magnitude value is meaningful only in conjunction with (i) the observable that was measured and (ii) the calibration (regression coefficients, distance corrections, station terms) that was applied. Different networks can report different values for the same nominal magnitude type because they adopt different correction functions and regression constants.
```

📖 *Shearer reference:* Section 9.7 (general magnitude framework)

---

## 2. Local magnitude $M_L$

### 2.1 Historical origin

Charles Richter introduced $M_L$ in 1935 as the first quantitative earthquake magnitude scale. The original definition was tied to a specific instrument — the **Wood–Anderson torsion seismometer** — with a natural period of approximately 0.8 s and a peak response near 1 Hz. Richter defined magnitude zero as the event that would produce a peak trace amplitude of 1 μm on a Wood–Anderson instrument at an epicentral distance of 100 km in southern California.

### 2.2 Definition

The local magnitude is defined as:

$$M_L = \log_{10}(A) - \log_{10}\!\big(A_0(\Delta)\big)$$

where:
- $A$ is the **peak displacement amplitude** measured on a Wood–Anderson seismometer (or a simulated Wood–Anderson response), typically the maximum of the two horizontal components
- $A_0(\Delta)$ is an **empirical distance correction curve** that accounts for amplitude decay with epicentral distance $\Delta$

The distance correction $A_0(\Delta)$ absorbs the combined effects of geometrical spreading and anelastic attenuation. Because attenuation varies regionally, $A_0(\Delta)$ must be **calibrated separately for each network and tectonic setting** — the original Richter curve for southern California does not apply universally.

### 2.3 Calibration considerations

Modern implementations of $M_L$ frequently include explicit station correction terms:

$$M_L = \log_{10}(A) + a \log_{10}(\Delta) + b\,\Delta + c + S_j$$

where $a$, $b$, $c$ are regression coefficients for distance correction and $S_j$ is the station term for station $j$. The coefficients are obtained by **joint regression** over a large dataset of event–station pairs, minimizing the scatter in single-station magnitude estimates. Regional differences in these coefficients are a primary source of systematic magnitude discrepancies between networks.

📖 *Shearer reference:* Section 9.7 (local magnitude)

---

## 3. Body-wave magnitude $m_b$

### 3.1 Definition

The body-wave magnitude measures the **short-period P-wave amplitude** at teleseismic distances, reported as an amplitude-to-period ratio:

$$m_b = \log_{10}(A/T) + Q(\Delta, h)$$

where:
- $A/T$ is the ratio of ground displacement amplitude to dominant period, measured on the first few cycles of the P-wave arrival
- $Q(\Delta, h)$ is an empirical correction for distance $\Delta$ and focal depth $h$, tabulated by Gutenberg and Richter and subsequently revised

### 3.2 Characteristics

The measurement is made in a narrow short-period band (typically near 1 s), which limits $m_b$ to sampling only the high-frequency portion of the source spectrum. This makes $m_b$ practical for routine monitoring of teleseismic events — the short-period P wave is among the most reliably observed phases globally — but also renders it susceptible to **saturation** for large earthquakes (Section 7).

The depth correction $Q(\Delta, h)$ accounts for the depth dependence of P-wave takeoff angle and focusing effects. However, $m_b$ estimates can vary with the radiation pattern, the specific P-wave segment selected, and the phase identification (e.g., P vs pP).

📖 *Shearer reference:* Section 9.7 (body-wave magnitude)

---

## 4. Surface-wave magnitude $M_s$

### 4.1 Definition

The surface-wave magnitude is measured on **Rayleigh waves** at periods near 20 s:

$$M_s = \log_{10}(A/T) + \Sigma(\Delta)$$

where:
- $A/T$ is the amplitude-to-period ratio of the Rayleigh wave, with $T \approx 20$ s
- $\Sigma(\Delta)$ is a distance correction appropriate for surface-wave propagation

### 4.2 Characteristics

Because Rayleigh waves sample longer periods than the P-wave measurements used for $m_b$, $M_s$ extends the linear scaling range to larger events before saturating. However, $M_s$ has two important limitations:

1. **Depth bias.** Surface-wave excitation decreases rapidly with source depth. For deep earthquakes (depth $\gg$ wavelength), Rayleigh-wave amplitudes are strongly suppressed, and $M_s$ systematically **underestimates** event size.
2. **Distance requirement.** Reliable Rayleigh-wave measurements require sufficient propagation distance for the surface wave train to develop and separate from body-wave coda, restricting $M_s$ primarily to regional-to-teleseismic distances.

$M_s$ has been widely used for historical catalogs and remains important for large, shallow earthquakes.

📖 *Shearer reference:* Section 9.7 (surface-wave magnitude)

---

## 5. Duration and coda magnitude $M_d$ / $M_c$

### 5.1 Definition

Duration and coda magnitudes estimate event size from the **temporal extent of the seismogram signal**, rather than from peak amplitudes:

$$M_d = a \log_{10}(t_{\text{coda}}) + b\,\Delta + c$$

where:
- $t_{\text{coda}}$ is the **coda duration** — the elapsed time from the origin (or first arrival) until the signal envelope decays below a prescribed threshold relative to the ambient noise level
- $a$, $b$, $c$ are empirically determined regression coefficients, calibrated regionally

### 5.2 Physical basis

Seismic coda waves arise from **scattering** of body waves by small-scale heterogeneities in the crust and upper mantle. The coda envelope decays approximately as a power law in time, modulated by the **coda quality factor** $Q_c$ that characterizes intrinsic and scattering attenuation. Larger earthquakes produce stronger initial radiation and therefore longer-duration coda above any fixed threshold — hence the correlation between $t_{\text{coda}}$ and event size.

### 5.3 Practical considerations

$M_d$ and $M_c$ are particularly attractive for **dense local networks** monitoring small-to-moderate seismicity, for several reasons:
- Duration measurements are less sensitive to instrument calibration errors than peak amplitudes.
- They do not require precise knowledge of the instrument response, making the method robust for heterogeneous station types.
- Clipped waveforms (common for nearby events on high-gain instruments) do not preclude a valid duration measurement.

The principal vulnerability is **sensitivity to the noise floor**: elevated background noise shortens the apparent coda duration and biases the magnitude downward. The precise definition of "coda end" (threshold criterion, smoothing window) must be standardized within a network for consistent results.

📖 *Shearer reference:* Section 9.7 (duration magnitude)

---

## 6. Moment magnitude $M_w$

### 6.1 Seismic moment

The scalar seismic moment $M_0$ quantifies the overall strength of a seismic source as a product of material and geometric factors:

$$\boxed{M_0 = \mu \, A \, \bar{D}}$$

where $\mu$ is the **shear modulus** of the faulted rock, $A$ is the **rupture area**, and $\bar{D}$ is the **average slip**. $M_0$ has units of N·m (force × distance) and is obtained from **long-period seismograms**, spectral analysis, or moment tensor inversion (Module 7).

Because $M_0$ is proportional to the zero-frequency (static) limit of the source spectrum, it captures the total deformation regardless of how the radiated energy is distributed across frequencies. This property is what makes $M_0$-based magnitudes immune to saturation.

### 6.2 Definition

Kanamori (1977) and Hanks & Kanamori (1979) introduced the moment magnitude:

$$\boxed{M_w = \frac{2}{3}\log_{10}(M_0) - 6.07}$$

where $M_0$ is expressed in N·m. The coefficients $2/3$ and $-6.07$ were chosen so that $M_w$ agrees numerically with $M_s$ over the magnitude range where $M_s$ scales linearly (approximately $M$ 5–7.5), providing continuity with historical catalogs.

### 6.3 Advantages

$M_w$ is the preferred magnitude for hazard assessment, scaling-law studies, and physics-based source characterization because:
- It is **directly tied to a physical source parameter** ($M_0$), not to a band-limited amplitude measurement.
- It does **not saturate** at large magnitudes, because $M_0$ tracks the long-period source strength.
- It provides a **uniform basis** for comparing events across all sizes and depth ranges.

The principal limitation is that $M_w$ requires either broadband data of sufficient quality or a moment tensor inversion, which may not be available in real time or for very small events.

📖 *Shearer reference:* Section 9.7 (moment magnitude and relation to $M_0$)

---

## 7. Saturation and the omega-square spectrum

### 7.1 The saturation problem

The most important failure mode of amplitude-based magnitudes is **saturation**: beyond a certain event size, the measured amplitude in a fixed frequency band ceases to increase proportionally with the true source strength. The magnitude estimate levels off even as $M_0$ continues to grow.

The saturation thresholds differ by scale:
- $M_L$ and $m_b$ saturate at moderate magnitudes (approximately $M$ 6–7), because the ~1 s measurement band lies well above the corner frequency of large ruptures.
- $M_s$ saturates later (approximately $M$ 8–8.5), because the ~20 s Rayleigh-wave band extends the linear range, but it too eventually falls on the high-frequency decay of the source spectrum for the largest events.
- $M_w$ does not saturate, by construction, because $M_0$ corresponds to the zero-frequency spectral level.

### 7.2 Physical explanation: the omega-square model

Saturation is a direct consequence of how earthquake source spectra scale with event size. The **Brune (1970) omega-square model** describes the far-field displacement spectrum as:

$$|\hat{u}(f)| \propto \frac{M_0}{1 + (f/f_c)^2}$$

where $f_c$ is the **corner frequency** of the source. Key features:
- At low frequencies ($f \ll f_c$), the spectral amplitude is proportional to $M_0$ — the **flat plateau**.
- At high frequencies ($f \gg f_c$), the spectrum decays as $f^{-2}$.
- As event size increases, $M_0$ grows and $f_c$ decreases (larger ruptures have longer durations).

A short-period magnitude measured at a fixed frequency $f_{\text{obs}}$ samples the spectrum at that frequency. For small events ($f_c > f_{\text{obs}}$), the measurement sits on the flat plateau and scales linearly with $M_0$. For large events ($f_c < f_{\text{obs}}$), the measurement sits on the $f^{-2}$ decay branch. As $M_0$ increases further, the spectral amplitude at $f_{\text{obs}}$ grows much more slowly than $M_0$ — this is saturation.

### 7.3 Implications

Saturation has practical consequences:
- **Underestimation of large events.** An $m_b$ of 6.5 could correspond to an $M_w$ anywhere from 6.5 to 9+. Relying on saturated magnitudes for hazard or tsunami warning is dangerous.
- **Magnitude discrepancies as diagnostics.** Systematic differences such as $m_b < M_w$ at large magnitudes are not errors — they reflect the band-limited nature of the measurement and carry information about the source spectrum shape.

---

## 8. Magnitude comparison and network dependence

### 8.1 Sources of inter-network discrepancy

When different agencies report different magnitude values for the same event (even for the same nominal scale), the discrepancy typically arises from one or more of the following:
- **Different distance correction functions** $F(\Delta, h)$ calibrated with different datasets and regional attenuation models
- **Different station/site terms**, or the absence of site corrections entirely
- **Different instrument responses** or response-simulation procedures (particularly relevant for $M_L$, which historically required a Wood–Anderson instrument)
- **Different measurement windows** or phase-picking conventions
- **Different regression datasets** used to determine the calibration coefficients

These are not pathologies but inherent features of empirically calibrated scales. Magnitude values should always be interpreted with reference to the issuing agency and its calibration.

### 8.2 Summary comparison table

| Type | Measured observable | Band / phase | Distance regime | Calibration parameters | Common failure modes | Primary application |
|---|---|---|---|---|---|---|
| **$M_L$** | Peak displacement amplitude (WA or simulated WA) | ~1 s, local phases | Local–regional | $A_0(\Delta)$ distance curve; station/site terms | Saturation; site/path bias; windowing | Local cataloging, rapid regional sizing |
| **$m_b$** | $A/T$ of teleseismic P | Short-period P (~1 s) | Teleseismic | $Q(\Delta, h)$; phase selection | Saturation; depth sensitivity; radiation pattern | Global monitoring, discrimination context |
| **$M_s$** | $A/T$ of Rayleigh wave | Surface waves (~20 s) | Regional–teleseismic | $\Sigma(\Delta)$; period window | Depth bias; saturation at very large sizes | Large shallow events; historical catalogs |
| **$M_d/M_c$** | Coda duration or coda amplitude proxy | Broadband coda | Local–regional | Threshold definition; regional $Q_c$ | Noise sensitivity; regional attenuation | Small events; dense local networks |
| **$M_w$** | Seismic moment $M_0$ | Long-period / model-based | All | Inversion/modeling choices | Data/model requirements; not always rapid | Hazard, scaling, physics-based comparisons |

---

## 9. Applications

### 9.1 Explosion–earthquake discrimination

Magnitude differences serve as discriminants between source types. Explosions radiate disproportionately strong short-period P-wave energy relative to surface waves, producing characteristically high $m_b$ relative to $M_s$. The **$m_b$–$M_s$ discriminant** — examining whether an event falls above or below the earthquake population trend in the $m_b$ vs $M_s$ plane — has been a cornerstone of nuclear test monitoring since the 1960s. More recent work extends this approach using $M_L$ and $M_c$ comparisons at local distances (Koper et al., 2021).

### 9.2 Harmonization to $M_w$

Regional and historical catalogs report magnitudes in a variety of scales ($M_L$, $M_d$, $m_b$, $M_s$). For seismic hazard analysis and scaling-law studies, a uniform magnitude measure is required. Agencies construct **empirical conversion regressions** that map network-specific magnitudes to $M_w$. These conversions must account for saturation — a linear regression of $m_b$ to $M_w$ is inappropriate if the data span the saturation regime. Studies such as Ristau (2009) and Dost et al. (2018) illustrate the care required in regional magnitude calibration and the systematic biases that arise from network-specific choices.

### 9.3 Rapid magnitude and early warning

Earthquake early warning systems require magnitude estimates within seconds of the first P-wave detection. These rapid estimates are inherently **band-limited** (only the initial portion of the rupture has been recorded) and may saturate for large events whose rupture duration exceeds the available data window. Robust algorithms must detect and flag the saturation regime to avoid underestimating hazard.

### 9.4 Source spectrum characterization

Comparing magnitudes measured at different frequencies provides a window into the **source spectrum shape**. Differences between short-period magnitudes ($M_L$, $m_b$) and $M_w$ can be related to the corner frequency and, through scaling assumptions, to **stress drop**. Events with anomalously high short-period radiation relative to their moment (high $m_b - M_w$) may indicate elevated stress drop, while events with low short-period radiation may indicate slow rupture.

---

## 10. Check-your-understanding

**Q1.** Why can two networks report different $M_L$ values for the same event?

**Q2.** What is the key physical reason that $M_L$ and $m_b$ saturate but $M_w$ does not? Frame the answer in terms of the omega-square source spectrum.

**Q3.** For a deep earthquake, which magnitude is more likely to be biased low: $M_s$ or $m_b$? Explain the physical mechanism.

**Q4.** Why are $M_d/M_c$ estimates sensitive to the noise floor and the definition of coda termination?

**Q5.** If a catalog lists $m_b < M_w$ for a large event, what is a plausible physical interpretation?

**Q6.** In what operational contexts would a fast, band-limited magnitude be preferred over $M_w$, despite the risk of saturation?

Students should attempt these questions *before* proceeding to the companion lab exercises.

---

## 11. What we deliberately did not cover

- **Full spectral fitting and stress drop estimation.** Extracting corner frequency and stress drop from spectral ratios requires detailed modeling beyond the scope of this lecture.
- **Network-specific calibration procedures.** The joint inversion of distance correction curves and station terms (e.g., Bakun & Joyner, 1984) is an important operational topic but involves regression methodology beyond what we develop here.
- **Energy magnitude $M_e$.** The energy magnitude, based on radiated seismic energy rather than moment, provides complementary information about source dynamics but requires broadband energy integration.
- **Magnitude of completeness $M_c$.** Statistical analysis of catalog completeness — determining the minimum magnitude above which all events are reliably detected — is a separate topic in seismicity analysis.
- **Historical evolution of magnitude formulas.** The iterative refinement of distance corrections and regression coefficients across agencies and decades is a rich topic in the history of seismology.

---

## 12. Looking ahead

In the companion labs, we will:
- **Measure** amplitudes on real and synthetic waveforms and compute toy $M_L$-like magnitudes to test sensitivity to distance correction and site terms (Lab 7c)
- **Compare** catalog magnitudes across types for the same events, examining $m_b$ vs $M_w$ and $M_L$ vs $M_w$ scatter (Lab 7c)
- **Demonstrate** saturation using the omega-square spectrum model, showing where short-period magnitude proxies diverge from $M_w$ (Lab 7c)
- **Explore** magnitude catalogs and network-to-network discrepancies (Lab 7b)

**Connections to other modules:**
- **Module 7 (Moment Tensors):** $M_0$ from moment tensor inversion feeds directly into the $M_w$ definition.
- **Module 3 (Ray Theory):** Takeoff angles and ray paths determine the distance correction terms $F(\Delta, h)$.
- **Module 5 (Surface Waves):** Rayleigh-wave excitation and depth sensitivity control the behavior of $M_s$.

---

## Reading

**Textbook:**
- Shearer, P. M. (2009), *Introduction to Seismology*, 2nd ed.
  - **Section 9.7**: Earthquake magnitude

**Classic references:**
- Kanamori, H. (1977). The energy release in great earthquakes. *Journal of Geophysical Research*, 82(20), 2981–2987.
- Hanks, T. C., & Kanamori, H. (1979). A moment magnitude scale. *Journal of Geophysical Research*, 84(B5), 2348–2350.

**Calibration and comparison studies:**
- Ristau, J. (2009). Comparison of magnitude estimates for New Zealand earthquakes: Moment magnitude, local magnitude, and teleseismic body-wave magnitude. *Bulletin of the Seismological Society of America*, 99(3), 1841–1852.
- Dost, B., Edwards, B., & Bommer, J. J. (2018). Local and moment magnitude calibration for the Groningen gas field. *Bulletin of the Seismological Society of America*, 108(3B), 1542–1559.
- Koper, K. D., Pankow, K. L., Pechmann, J. C., Hale, J. M., Burlacu, R., Yeck, W. L., Benz, H. M., Herrmann, R. B., Trugman, D. T., & Shearer, P. M. (2021). Discrimination of small earthquakes and buried single-fired chemical explosions at local distances (<150 km) in the western United States from comparison of local magnitude ($M_L$) and coda duration magnitude ($M_c$). *Seismological Research Letters*, 92(5), 2973–2985.
