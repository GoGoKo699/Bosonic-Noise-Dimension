# Thirty milestones for Bosonic Noise Dimension

[Project overview](../README.md) · [Scientific account](../science/README.md)

This map follows one scientific question: **how does the amount of classical noise resolved by an energy-constrained oscillator determine its ability to transmit quantum information?** Its thirty understanding targets connect the channel model, the capacity proof, the circular-noise example and the effect of Gaussian broadening. They identify the load-bearing ideas; the canonical scientific pages contain the complete derivations and technical qualifications.

## One educational anchor

The sole educational anchor is Alexander S. Holevo, [*Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (2019)](https://doi.org/10.1515/9783110642490). Section numbers and printed starting pages below refer to that edition and were checked against its [publisher-origin preview, contents pp. XI–XV](https://api.pageplace.de/preview/DT0400.9783110642490_A39059069/preview-9783110642490_A39059069.pdf).

The anchor supplies foundations in entropy, quantum channels, coding, infinite-dimensional constraints and Gaussian systems. A section pointer identifies the relevant foundation, not a claim that the book contains this project's result. In particular, the energy-constrained coding and continuity theorems, teleportation-simulation converse and local derivations retain their research-level attribution in the [scientific account](../science/README.md) and [research bibliography](../references/README.md). These research dependencies are not additional educational anchors.

## Allocation and dependency structure

**Background/preliminaries comprises M01–M12.** It begins with a single oscillator and displacement, then connects quantum and classical entropy to channel comparisons, coding and infinite-dimensional limits. Its final milestone assembles the operational setting and the two proof obligations.

**Narrative/innovation comprises M13–M30.** It begins with the entropy cost of a small displacement cell, combines the lower and upper bounds into a capacity law, and then develops classification, explicit examples and robustness. Its final milestones connect those results to their antecedents and to the physical question.

The twelve/eighteen allocation reflects the project's structure: several kinds of background must meet, but the main explanatory work lies in the noncommuting-noise proof and its consequences. Within each phase, the order moves from individual objects and mechanisms to the global argument. Dependencies below name earlier milestones; they do not impose a separate reading programme.

| ID | Phase | Understanding focus |
|---|---|---|
| M01 | Background/preliminaries | One oscillator, quantum states and photon number |
| M02 | Background/preliminaries | Weyl displacements and their noncommutativity |
| M03 | Background/preliminaries | Entropy under a mean-energy constraint |
| M04 | Background/preliminaries | Purification, a reference system and entropy exchange |
| M05 | Background/preliminaries | What Gaussian calculations do and do not determine |
| M06 | Background/preliminaries | Classical noise viewed through a finite grid |
| M07 | Background/preliminaries | Relative entropy and loss of distinguishability |
| M08 | Background/preliminaries | Entanglement-breaking channels and separable comparisons |
| M09 | Background/preliminaries | Coherent information as an achievable quantum rate |
| M10 | Background/preliminaries | Collective codes and regularized capacity |
| M11 | Background/preliminaries | Mean energy, convergence and continuity in infinite dimension |
| M12 | Background/preliminaries | The complete operational model and proof obligations |
| M13 | Narrative/innovation | Why the relevant displacement scale is inverse square-root energy |
| M14 | Narrative/innovation | A thermal lower bound from resolved noise entropy |
| M15 | Narrative/innovation | A smooth-law resource comparison with Gaussian noise |
| M16 | Narrative/innovation | Turning finite-resource simulation into an arbitrary-code converse |
| M17 | Narrative/innovation | The bridge between smoothing and quantization entropy |
| M18 | Narrative/innovation | Choosing a smoothing scale compatible with capacity continuity |
| M19 | Narrative/innovation | The finite-resolution capacity sandwich |
| M20 | Narrative/innovation | Information dimension and the coefficient of logarithmic growth |
| M21 | Narrative/innovation | Finite alphabets and mixed discrete–continuous laws |
| M22 | Narrative/innovation | The exact criterion for bounded unconstrained capacity |
| M23 | Narrative/innovation | A circle's one-dimensional noise and two-dimensional covariance |
| M24 | Narrative/innovation | Exact circular entropy exchange through charge sectors |
| M25 | Narrative/innovation | A capacity separation at matched covariance |
| M26 | Narrative/innovation | A positive finite-energy rate with nonzero Gaussian jitter |
| M27 | Narrative/innovation | The finite ceiling created by fixed broadening |
| M28 | Narrative/innovation | The joint energy–broadening crossover |
| M29 | Narrative/innovation | How the mechanism relates to existing capacity results |
| M30 | Narrative/innovation | The complete contribution and its operational boundaries |

## Phase I — Background/preliminaries

### M01 — One oscillator and the photon resource

- **Central question.** What is the physical system carrying the quantum information, and what does its energy budget count?
- **Understanding target.** Connect a density operator, the Fock basis, the annihilation operator and photon number $`N=a^\dagger a`$. Interpret $`\mathrm{Tr}\rho N`$ as a mean rather than a maximum occupied photon level, and distinguish an oscillator from a finite-dimensional message register.
- **Dependencies and story role.** No earlier milestone. This fixes the local carrier and observable from which the resource constraint is built.
- **Conceptual connection.** The oscillator's unbounded Hilbert space makes energy a necessary part of the communication question.
- **Sources.** **Holevo:** §§2.2 (p. 13), 12.1.2 (p. 258), 12.2.3 (p. 269). **Science:** [one oscillator and a fixed noise law](../science/01-model.md#one-oscillator-and-a-fixed-noise-law); [what capacity counts](../science/01-model.md#what-the-capacity-counts).

### M02 — Phase-space translations

- **Central question.** How can classical random kicks produce a genuinely quantum channel?
- **Understanding target.** Interpret $`D(z)=\exp(za^\dagger-\bar z a)`$ as a translation of the two conjugate quadratures. Explain why Weyl operators generally do not commute, while their phases cancel under conjugation so that independent displacement channels compose by classical convolution.
- **Dependencies and story role.** M01. Introduces the elementary error before any averaging or coding is considered.
- **Conceptual connection.** A classical probability law can govern noncommuting errors; commutative composition of averaged channels does not supply a common error eigenbasis.
- **Sources.** **Holevo:** §§12.2.1–12.2.2 (pp. 265, 267), 6.7 (p. 119). **Science:** [one oscillator and a fixed noise law](../science/01-model.md#one-oscillator-and-a-fixed-noise-law).

### M03 — Entropy and the thermal benchmark

- **Central question.** How much quantum entropy can a fixed mean photon budget support?
- **Understanding target.** Distinguish entropy of a quantum state from energy and from uncertainty in a classical noise label. Understand the thermal maximum-entropy benchmark $`g(E)`$ and its growth $`g(E)=\log_2E+O(1)`$, without treating all states of the same energy as thermal.
- **Dependencies and story role.** M01. Converts the local energy resource into the entropy scale used throughout the capacity argument.
- **Conceptual connection.** The available entropy grows logarithmically with energy; the proof will compare it with the entropy lost to resolved displacement noise.
- **Sources.** **Holevo:** §§7.1 (p. 126), 11.2 (p. 237), 12.3.3–12.3.4 (pp. 279, 281). **Science:** [entropies and phase-space resolution](../science/01-model.md#entropies-and-phase-space-resolution); [thermal-input lower bound](../science/02-capacity-law.md#why-one-thermal-input-suffices-for-the-lower-bound).

### M04 — Purification and entropy exchange

- **Central question.** How can noise be evaluated without selecting a particular ensemble decomposition of the input state?
- **Understanding target.** Purify a mixed input with a reference system and apply the channel only to the transmitted mode. Interpret the entropy of the reference–output state as entropy exchange, and understand why a two-mode squeezed vacuum purifies a one-mode thermal state.
- **Dependencies and story role.** M01 and M03. Enlarges the local carrier into the bipartite description needed to track preserved quantum correlations.
- **Conceptual connection.** A reference distinguishes transmission of quantum information from reproduction of ordinary output statistics.
- **Sources.** **Holevo:** §§3.1.1 (p. 33), 3.1.3 (p. 37), 6.6 (p. 115), 7.6 (p. 141), 12.3.5 (p. 284). **Science:** [thermal input and purification](../science/02-capacity-law.md#why-one-thermal-input-suffices-for-the-lower-bound).

### M05 — The Gaussian toolkit and its limits

- **Central question.** When do first and second moments determine a quantum state's entropy?
- **Understanding target.** Relate Gaussian characteristic functions, covariance matrices and symplectic eigenvalues to Gaussian-state entropy. Recognize that a thermal input can acquire a non-Gaussian joint output under non-Gaussian displacement noise, so its covariance alone need not determine entropy exchange.
- **Dependencies and story role.** M02–M04. Supplies a tractable class of states while making its boundary explicit.
- **Conceptual connection.** Gaussian structure is used both for a comparison channel in the converse and for an exact intermediate state in the broadening calculation.
- **Sources.** **Holevo:** §§12.3.1–12.3.2 (pp. 273, 274), 12.3.4–12.3.5 (pp. 281, 284). **Science:** [finite-energy broadening bound, (B3)–(B5)](../science/05-broadening.md#a-quantitative-finite-energy-lower-bound); [physical comparison](../science/01-model.md#boundaries-of-the-physical-comparison).

### M06 — Classical noise at finite resolution

- **Central question.** How can one compare the uncertainty of a discrete, singular or continuous displacement law using the same quantity?
- **Understanding target.** Define the integer cell label obtained by placing a grid over the complex plane and interpret its Shannon entropy $`H_t(\mu)`$. Distinguish this finite-resolution entropy from differential entropy, support dimension and covariance rank.
- **Dependencies and story role.** M02 and M03. Introduces the classical quantity that can be matched to the quantum entropy budget.
- **Conceptual connection.** Coarse graining describes what is resolved at a chosen scale without requiring a density for the noise.
- **Sources.** **Holevo:** §§4.1–4.2 (pp. 55, 57), for discrete and conditional entropy. **Science:** [entropies and phase-space resolution](../science/01-model.md#entropies-and-phase-space-resolution). Grid quantization and information dimension are defined locally in the project.

### M07 — Relative entropy and comparison

- **Central question.** Why can replacing an explicit noise label by the resulting quantum state only reduce distinguishability?
- **Understanding target.** Interpret classical and quantum relative entropy as comparison quantities and use data processing for the map from a classical displacement label to a displaced quantum state. Recognize that a comparison measure must assign nonzero weight wherever the original measure does.
- **Dependencies and story role.** M03, M04 and M06. Connects classical probability comparisons to quantum-state bounds.
- **Conceptual connection.** The converse will bound a quantum entanglement resource by the classical relative entropy between two displacement laws.
- **Sources.** **Holevo:** §§7.1–7.2 (pp. 126, 127), 11.2 (p. 237). **Science:** [a separable comparison at finite squeezing](../science/03-converse.md#a-separable-comparison-state-at-every-finite-squeezing).

### M08 — Entanglement breaking and separable references

- **Central question.** Why is a measure-and-prepare channel a useful zero-capacity reference?
- **Understanding target.** Explain how an entanglement-breaking channel destroys entanglement with every reference and why a separable state can bound relative entropy of entanglement from above. Distinguish this comparison method from asserting that the channel of interest is itself entanglement breaking.
- **Dependencies and story role.** M04 and M07. Turns distinguishability into an operational obstruction to transmitting quantum correlations.
- **Conceptual connection.** Unit-variance complex Gaussian displacement noise supplies the separable comparison used later, even for a non-Gaussian target law.
- **Sources.** **Holevo:** §§6.4 (p. 110), 11.7 (p. 248), 12.4.4 (p. 294), 12.6.2 (p. 324). **Science:** [smooth-noise comparison lemma](../science/03-converse.md#smooth-noise-admits-a-classical-relative-entropy-upper-bound). The relative-entropy-of-entanglement converse is attributed there to the research literature.

### M09 — Coherent information as a rate

- **Central question.** When does an entropy difference imply that quantum communication is possible?
- **Understanding target.** Read coherent information as output entropy minus entropy exchange for a chosen input. Explain why a positive value provides an achievable asymptotic quantum rate, while a negative value from that input does not establish zero capacity.
- **Dependencies and story role.** M03 and M04. Connects the entropy accounting to the communication task.
- **Conceptual connection.** The thermal state is useful because its coherent information can be controlled, not because thermal inputs are assumed globally optimal.
- **Sources.** **Holevo:** §§10.1.4 (p. 191), 10.3.2 (p. 206), 10.4.4 (p. 222). **Science:** [thermal-input achievability](../science/02-capacity-law.md#why-one-thermal-input-suffices-for-the-lower-bound); [constrained coding foundation](../science/01-model.md#what-the-capacity-counts).

### M10 — Collective coding and the meaning of capacity

- **Central question.** Why is evaluating one input on one channel use insufficient for a general capacity formula?
- **Understanding target.** Distinguish an achievable rate, a one-use coherent-information expression and the capacity optimized over arbitrary collective codes. Understand regularization and the extra structural assumption needed to simplify it through degradability.
- **Dependencies and story role.** M04 and M09. Expands a local rate calculation into the full optimization that a converse must cover.
- **Conceptual connection.** The project proves a leading capacity law without declaring the displacement channel degradable or its capacity single-letter.
- **Sources.** **Holevo:** §§10.2.1–10.2.2 (pp. 195, 197), 10.3.1–10.3.3 (pp. 202, 206, 208). **Science:** [what capacity counts](../science/01-model.md#what-the-capacity-counts); [established scope](../science/02-capacity-law.md#what-is-established-and-what-is-not).

### M11 — Energy constraints and infinite-dimensional limits

- **Central question.** What must be controlled before a small channel perturbation implies a small capacity change?
- **Understanding target.** Distinguish trace convergence, energy-constrained channel distance and continuity of a regularized communication rate. Explain why a total mean-energy bound allows uneven allocation across modes, and why a common output-energy bound is needed in the infinite-dimensional argument.
- **Dependencies and story role.** M01, M03 and M10. Adds the analytical conditions under which local approximations remain operationally useful.
- **Conceptual connection.** A finite energy constraint controls entropy without replacing the oscillator by an exact finite-dimensional cutoff.
- **Sources.** **Holevo:** §§7.4 (p. 134), 11.1–11.2 (pp. 233, 237), 11.5 (p. 243). **Science:** [operational energy constraint](../science/01-model.md#what-the-capacity-counts); [energy-constrained continuity ingredients](../science/03-converse.md#smoothing-below-the-energy-resolution-changes-capacity-little). The needed capacity continuity theorem is a separately cited research ingredient.

### M12 — The complete problem and its proof obligations

- **Central question.** What exactly must be proved to turn the geometry of random kicks into an unassisted quantum-capacity statement?
- **Understanding target.** Assemble a fixed known IID displacement law, unobserved noise draws, finite second moment and a mean-photon constraint. Separate the blocklength limit at fixed energy from the later high-energy limit, and identify the required achievable-rate and arbitrary-code upper bounds.
- **Dependencies and story role.** M01–M11. Integrates the background into the complete operational framework.
- **Conceptual connection.** The project must connect quantum coding, classical resolution entropy and an infinite-dimensional converse while retaining the same channel and resource model.
- **Sources.** **Holevo:** §§10.3.1–10.3.2 (pp. 202, 206), 11.5 (p. 243), 12.6.3–12.6.4 (pp. 325, 328). **Science:** [model and operational question](../science/01-model.md); [connected argument](../science/README.md#the-connected-argument).

## Phase II — Narrative/innovation

### M13 — The displacement scale selected by energy

- **Central question.** Why are cells of side $`(E+1)^{-1/2}`$ natural for the lower-bound proof?
- **Understanding target.** Follow a thermal purification after subtracting a cell's corner displacement and undoing its two-mode squeezing. Explain why the residual displacement becomes a two-mode coherent state with total photon number at most four when the kick stays inside such a cell.
- **Dependencies and story role.** M02, M04, M05, M06 and M12. Starts the new argument with one cell and a bounded residual quantum state.
- **Conceptual connection.** The square-root energy resolution comes from the displacement's action on the purification, rather than from the dimension of its covariance matrix.
- **Sources.** **Holevo:** §§12.2.1 (p. 265), 12.3.2 (p. 274), 12.3.5 (p. 284). **Science:** [resolve the displacement only to the energy scale](../science/02-capacity-law.md#resolve-the-displacement-only-to-the-energy-scale).

### M14 — From cell entropy to an achievable rate

- **Central question.** How does the uncertainty between cells become the leading entropy cost of the noise?
- **Understanding target.** Combine the cell-label entropy with the bounded conditional entropy to obtain exchange entropy at most $`H_{\sqrt{E+1}}(\mu)+2g(2)`$. Use concavity of output entropy and coherent-information coding to obtain the thermal lower bound without needing a density for $`\mu`$.
- **Dependencies and story role.** M03, M06, M09 and M13. Converts the local cell estimate into the first operational half of the capacity theorem.
- **Conceptual connection.** Large-scale classical uncertainty costs resolved entropy; uncertainty left inside a cell costs only a constant.
- **Sources.** **Holevo:** §§4.2 (p. 57), 7.6 (p. 141), 10.4.4 (p. 222), 12.3.4 (p. 281). **Science:** [thermal-input lower-bound derivation](../science/02-capacity-law.md#why-one-thermal-input-suffices-for-the-lower-bound).

### M15 — The smooth-law comparison resource

- **Central question.** How can a classical density comparison bound entanglement in a bosonic channel resource?
- **Understanding target.** Compare finite-squeezing channel resource states generated by a smooth density $`f`$ and by the unit-variance Gaussian density $`g_1`$. Combine classical-to-quantum data processing with the Gaussian reference's separability to bound the resource's relative entropy of entanglement by $`D(f\|g_1)`$.
- **Dependencies and story role.** M05, M07, M08 and M12. Builds a finite, normalizable comparison before any infinite-squeezing limit.
- **Conceptual connection.** The Gaussian channel is a calculable reference for arbitrary smooth displacement noise; Gaussian optimality of the target channel is not assumed.
- **Sources.** **Holevo:** §§7.1–7.2 (pp. 126, 127), 11.7 (p. 248), 12.4.4 (p. 294). **Science:** [finite-squeezing separable comparison](../science/03-converse.md#a-separable-comparison-state-at-every-finite-squeezing); [Gaussian reference variance](../science/03-converse.md#gaussian-reference-variance-can-be-optimized).

### M16 — From simulation to a full converse

- **Central question.** How does a bound on a finite-squeezing resource constrain every reliable finite-energy code?
- **Understanding target.** Explain the teleportation simulation, its residual Gaussian noise and the resulting bound on output entanglement. Keep the limit order explicit: fix a finite code, remove simulation error by increasing squeezing, and only then take the coding limit. Understand how a Bell-state test converts the entanglement bound into a rate bound.
- **Dependencies and story role.** M08, M10, M11 and M15. Expands the resource comparison into $`Q_f(E)\le D(f\|g_1)`$ for arbitrary collective codes.
- **Conceptual connection.** Allowing local operations and classical communication in an upper-bound simulation does not add assistance to the rate claimed achievable by the original channel.
- **Sources.** **Holevo:** §§3.3.2 (p. 46), 3.3.4 (p. 48), 10.3.1 (p. 202), 11.1 (p. 233). **Science:** [fixed finite code simulation limit](../science/03-converse.md#the-simulation-limit-is-taken-for-a-fixed-finite-code), including the cited simulation and entanglement-converse literature.

### M17 — Smoothing entropy equals resolved entropy up to scale

- **Central question.** What does a narrow Gaussian convolution preserve about a possibly singular noise law?
- **Understanding target.** Decompose the rescaled kick into an integer cell label and a remainder in a unit square. Explain why Gaussian smoothing produces differential entropy equal to $`2\log_2\sigma+H_{1/\sigma}(\mu)`$ up to universal additive constants, using bounded conditional uncertainty in both directions.
- **Dependencies and story role.** M06 and M07. Supplies the classical bridge from the smooth-law converse to the original arbitrary probability measure.
- **Conceptual connection.** Differential entropy becomes useful only after its smoothing scale is matched to a discrete resolution; the relation remains meaningful for singular measures.
- **Sources.** **Holevo:** §§4.1–4.2 (pp. 55, 57), 7.1 (p. 126). **Science:** [smoothing and quantization lemma](../science/03-converse.md#smoothing-entropy-and-quantization-entropy-differ-by-a-constant); [relative entropy after smoothing](../science/03-converse.md#relative-entropy-of-the-smoothed-law).

### M18 — A smoothing scale that controls capacity

- **Central question.** How small must the artificial Gaussian noise be so that the converse transfers back with a bounded continuity cost?
- **Understanding target.** Connect the energy-constrained diamond-distance estimate to a common output-energy bound and the imported capacity continuity theorem. Understand the choice $`\sigma=[\log_2(E+2)]^{-2}/\sqrt{4E+2}`$: it leaves a bounded continuity correction while refining the noise grid by a logarithmic factor.
- **Dependencies and story role.** M02, M11, M16 and M17. Makes the smooth approximation operationally uniform at the energy being considered.
- **Conceptual connection.** Small one-use disturbance alone is insufficient; the continuity theorem controls the already regularized capacity.
- **Sources.** **Holevo:** §§7.4 (p. 134), 11.1–11.2 (pp. 233, 237), 11.5 (p. 243). **Science:** [smoothing below the energy resolution](../science/03-converse.md#smoothing-below-the-energy-resolution-changes-capacity-little); [collecting the upper bound](../science/03-converse.md#collecting-the-finite-resolution-upper-bound).

### M19 — The finite-resolution capacity law

- **Central question.** What survives after the achievable rate and arbitrary-code converse are combined?
- **Understanding target.** State the two-sided bound around $`\log_2(E+1)-H_{\sqrt{E+1}}(\mu)`$: a universal constant loss below and an upper error $`4\log_2\log_2(E+2)+C_M`$ for $`E\ge1`$. Track which constants are uniform over laws with bounded second moment and why the result is not an exact finite-energy formula.
- **Dependencies and story role.** M14 and M18. Integrates the two proof branches into the main theorem.
- **Conceptual connection.** The same resolved classical entropy controls both what a thermal input achieves and what arbitrary codes can exceed.
- **Sources.** **Holevo:** §§10.3.2 (p. 206), 11.5 (p. 243), for the capacity framework. **Science:** [finite-resolution theorem](../science/02-capacity-law.md#the-finite-resolution-capacity-law); [explicit converse constants](../science/03-converse.md#collecting-the-finite-resolution-upper-bound).

### M20 — Information dimension becomes a capacity coefficient

- **Central question.** How does increasingly fine classical resolution determine the leading energy dependence?
- **Understanding target.** Derive $`Q_\mu(E)/\log_2E\to1-d(\mu)/2`$ when information dimension exists. Explain the factor one-half from $`t=\sqrt{E+1}`$ and the exchange of lower/upper limits when the noise has different lower and upper information dimensions.
- **Dependencies and story role.** M06 and M19. Converts a finite-scale theorem into a global asymptotic classification.
- **Conceptual connection.** Information dimension measures entropy growth with resolution; it need not equal support dimension or the number of nonzero covariance eigenvalues.
- **Sources.** **Holevo:** §§4.1 (p. 55), 10.3.2 (p. 206), as entropy and capacity foundations. **Science:** [dimension corollary](../science/02-capacity-law.md#information-dimension-fixes-the-leading-energy-dependence); [dimension definitions](../science/01-model.md#entropies-and-phase-space-resolution).

### M21 — Discrete and mixed laws

- **Central question.** Which features of a noise distribution determine its dimension when qualitatively different components coexist?
- **Understanding target.** Explain why a finite kick alphabet has full logarithmic capacity growth and why $`p\delta_0+(1-p)\nu`$, with an absolutely continuous finite-moment $`\nu`$, has coefficient $`p`$. Keep the mixture label unobserved and distinguish this conclusion from an erasure-channel model with a receiver flag.
- **Dependencies and story role.** M06, M12 and M20. Tests the classification on laws for which support alone is misleading.
- **Conceptual connection.** Probability weights affect resolved entropy and hence capacity growth even when a continuous component fills two-dimensional phase space.
- **Sources.** **Holevo:** §§4.1–4.2 (pp. 55, 57), 6.3 (p. 108), 10.3.2 (p. 206). **Science:** [dimension-law consequences](../science/02-capacity-law.md#consequences); [unobserved-noise model](../science/01-model.md#one-oscillator-and-a-fixed-noise-law).

### M22 — Boundedness beyond the leading coefficient

- **Central question.** When does capacity remain finite as the photon budget is removed?
- **Understanding target.** Explain the equivalence between finite $`Q_\mu(\infty)`$ and finite relative entropy $`D(\mu\|\gamma)`$ to the standard Gaussian measure, under the finite-second-moment assumption. Follow why nested dyadic partitions detect infinite relative entropy and why the thermal lower bound then diverges.
- **Dependencies and story role.** M07, M14, M16 and M20. Refines the leading-coefficient classification to distinguish bounded capacity from slower unbounded growth.
- **Conceptual connection.** Dimension two is compatible with unbounded sublogarithmic capacity; the full entropy deficit, not only its slope, decides boundedness.
- **Sources.** **Holevo:** §§7.1–7.2 (pp. 126, 127), 11.2 (p. 237), for relative-entropy foundations. **Science:** [bounded-capacity criterion and proof](../science/03-converse.md#when-is-the-unconstrained-capacity-finite); [why zero coefficient is insufficient](../science/02-capacity-law.md#boundedness-requires-more-than-a-zero-leading-coefficient).

### M23 — Circular geometry with isotropic covariance

- **Central question.** How can noise act on both quadratures yet have only one dimension of resolved uncertainty?
- **Understanding target.** Describe a uniformly random fixed-radius displacement and explain $`H_t(\mu_r)=\log_2(1+tr)+O(1)`$. Relate its one-dimensional probability law to its rank-two isotropic covariance, keeping $`r\gt0`$ fixed.
- **Dependencies and story role.** M02, M06 and M20. Begins the explicit physical example from its local geometry.
- **Conceptual connection.** The circle separates the entropy accumulated along a curve from the spread measured by a covariance matrix.
- **Sources.** **Holevo:** §§12.2.1–12.2.2 (pp. 265, 267), 12.3.1 (p. 273). **Science:** [circular model](../science/04-circular-noise.md#model-and-conventions); [circle quantized entropy](../science/04-circular-noise.md#the-circles-quantized-entropy).

### M24 — Exact exchange entropy from circular symmetry

- **Central question.** Why does circular randomization reduce a quantum entropy calculation to a classical integer distribution?
- **Understanding target.** Use the charge $`J=N_B-N_R`$ to describe the circular twirl of a displaced thermal purification. Explain why projecting this pure state into each nonzero charge sector gives a rank-one state block, with different blocks supported on orthogonal subspaces. The charge eigenspaces themselves need not be one-dimensional. This makes the exchange entropy exactly the entropy of a Skellam law with parameters $`r^2(E+1)`$ and $`r^2E`$.
- **Dependencies and story role.** M04, M05, M09 and M23. Adds an exact entropy mechanism to the geometric example.
- **Conceptual connection.** Symmetry resolves the mixed state into orthogonal sectors even though the underlying displacement errors do not commute.
- **Sources.** **Holevo:** §§7.6 (p. 141), 12.2.3 (p. 269), 12.3.1 (p. 273), 12.3.5 (p. 284). **Science:** [exact circular exchange entropy](../science/04-circular-noise.md#exact-entropy-exchange-for-a-thermal-input). The Skellam identification is derived locally.

### M25 — The covariance-matched capacity separation

- **Central question.** What operational difference remains invisible to the added covariance?
- **Understanding target.** Connect the circle's exact exchange entropy to an achievable half-logarithmic rate and the general converse to the same leading capacity coefficient. Compare with the Gaussian law of the same covariance, whose channel is entanglement breaking when $`r^2\ge1`$.
- **Dependencies and story role.** M08, M19, M23 and M24. Integrates geometry, an explicit thermal witness and a converse into the central physical separation.
- **Conceptual connection.** Equal second moments can coexist with zero capacity for one channel and unbounded capacity for the other.
- **Sources.** **Holevo:** §§12.6.2–12.6.4 (pp. 324, 325, 328). **Science:** [achievable circular rate](../science/04-circular-noise.md#an-achievable-half-logarithmic-rate); [matched Gaussian comparison](../science/04-circular-noise.md#comparison-with-covariance-matched-gaussian-noise).

### M26 — Nonzero jitter and a finite-energy witness

- **Central question.** Can the communication separation survive a nonzero broadening of the circle?
- **Understanding target.** Follow independent Gaussian jitter through a thermal purification, first using its Gaussian entropy and then a charge-twirling entropy bound. Interpret the certified rate above $`1.05`$ qubits per use at $`r=2`$, $`E=100`$, $`\sigma=0.01`$ while the covariance-matched Gaussian channel remains entanglement breaking.
- **Dependencies and story role.** M05, M09, M24 and M25. Moves from ideal singular noise to a quantitative finite-energy example with a smooth density.
- **Conceptual connection.** The mixed charge-sector inequality gives a rigorous achievable bound, not an exact broadened-channel capacity or an efficient code.
- **Sources.** **Holevo:** §§7.3 (p. 132), 12.3.4–12.3.5 (pp. 281, 284), 12.6.2 (p. 324). **Science:** [broadening bound](../science/05-broadening.md#a-quantitative-finite-energy-lower-bound); [nonzero-jitter example](../science/05-broadening.md#a-nonzero-jitter-example); [numerical verification](../verification/README.md).

### M27 — A fixed background creates a finite ceiling

- **Central question.** Why does every fixed positive Gaussian broadening change the large-energy conclusion?
- **Understanding target.** Explain why the broadened ring has a smooth finite-entropy density and a finite Gaussian-reference relative-entropy bound. Conclude that its capacity approaches a finite ceiling as energy increases, without identifying the ceiling's exact value.
- **Dependencies and story role.** M16, M22 and M26. Places the finite-energy witness inside the correct fixed-channel asymptotic regime.
- **Conceptual connection.** Positive finite-energy transmission and a zero coefficient of logarithmic growth are compatible; the amount of broadening determines which question is being answered.
- **Sources.** **Holevo:** §§7.1 (p. 126), 11.2 (p. 237), 12.6.2–12.6.3 (pp. 324, 325). **Science:** [capacity saturation at fixed background noise](../science/05-broadening.md#capacity-saturation-at-fixed-background-noise).

### M28 — The joint energy–broadening crossover

- **Central question.** Which scale controls capacity when energy increases while Gaussian jitter decreases?
- **Understanding target.** Interpret the effective energy $`E_*=\min\{E,\sigma^{-2}\}`$ and the two-sided half-logarithmic bound in $`E_*`$ for fixed positive radius. Explain why the upper remainder after saturation cannot grow with unused input energy and how $`\sigma(E)=E^{-\alpha}`$ gives coefficient $`\min\{1/2,\alpha\}`$.
- **Dependencies and story role.** M19 and M25–M27. Integrates the ideal circle, finite witness and fixed-background ceiling into a two-parameter account.
- **Conceptual connection.** Input energy sets an improving resolution until it resolves the thickness of the broadened ring.
- **Sources.** **Holevo:** §§11.5 (p. 243), 12.3.4 (p. 281), 12.6.4 (p. 328), as constraint and entropy foundations. **Science:** [joint crossover theorem](../science/05-broadening.md#the-joint-energybroadening-crossover); [orders of limits](../science/05-broadening.md#orders-of-limits-and-scope).

### M29 — Relation to existing capacity mechanisms

- **Central question.** Which parts of the argument are inherited, and what changes when the errors are noncommuting displacements?
- **Understanding target.** Relate the resolved-entropy principle to the commuting phase-noise antecedent while distinguishing its resolution scale and degradability route. Separate earlier classical or entanglement-assisted capacity results from this unassisted quantum-capacity theorem, and identify coding, continuity and simulation as imported proof ingredients.
- **Dependencies and story role.** M10, M12, M19, M22 and M28. Places the integrated contribution in the correct scientific landscape.
- **Conceptual connection.** The contribution is the extension to arbitrary finite-moment Weyl noise, its arbitrary-code converse and consequences, rather than a new invention of every method it uses.
- **Sources.** **Holevo:** §§9.1 (p. 173), 10.3.2–10.3.3 (pp. 206, 208), 12.6.4 (p. 328). **Science:** [relation to prior work](../science/06-related-work.md), which supplies the primary research references.

### M30 — The complete operational conclusion

- **Central question.** What does the project establish about quantum communication through random phase-space noise, and where does the conclusion stop?
- **Understanding target.** Connect the finite-resolution law, dimension coefficient, boundedness criterion, circular separation and broadening crossover into one account. Keep the assumptions visible: IID unobserved kicks, fixed-law limits when specified, finite second moment, ordinary unassisted coding and a mean-photon resource. Distinguish capacity achievability from an explicit efficient implementation and from claims about loss or correlated drift.
- **Dependencies and story role.** M12, M19–M22 and M25–M29. Synthesizes the narrative rather than adding another independent result.
- **Conceptual connection.** The physically relevant description is noise uncertainty at the resolution supported by the carrier, with smoothing setting a second scale when present.
- **Sources.** **Holevo:** §§10.3.1–10.3.2 (pp. 202, 206), 11.5 (p. 243), 12.6.4 (p. 328). **Science:** [connected scientific account](../science/README.md#the-connected-argument); [theorem scope](../science/02-capacity-law.md#what-is-established-and-what-is-not); [physical boundaries](../science/01-model.md#boundaries-of-the-physical-comparison); [broadening limits](../science/05-broadening.md#orders-of-limits-and-scope).
