# Thirty milestones for Bosonic Noise Dimension

[Project overview](../README.md) · [Scientific account](../science/README.md)

This map follows one scientific question: **how does the amount of classical noise resolved by an energy-constrained oscillator determine its ability to transmit quantum information?** Its thirty understanding targets connect the channel model, the capacity proof, the circular-noise example and the effect of Gaussian broadening. They identify the load-bearing ideas; the canonical scientific pages contain the complete derivations and technical qualifications.

## One educational anchor

The sole educational anchor is Alexander S. Holevo, [*Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (2019)](https://doi.org/10.1515/9783110642490). Section numbers and printed starting pages below refer to that edition and were checked against its [publisher-origin preview, contents pp. XI–XV](https://api.pageplace.de/preview/DT0400.9783110642490_A39059069/preview-9783110642490_A39059069.pdf).

The anchor supplies foundations in entropy, quantum channels, coding, infinite-dimensional constraints and Gaussian systems. Each section pointer identifies a foundation used in the proof. The energy-constrained coding theorem, relative-entropy converse and local derivations retain their research-level attribution in the [scientific account](../science/README.md) and [research bibliography](../references/README.md).

## Allocation and dependency structure

**Background/preliminaries comprises M01–M12.** It begins with a single oscillator and displacement, then connects quantum and classical entropy to channel comparisons, coding and infinite-dimensional limits. Its final milestone assembles the operational setting and the two proof obligations.

**Narrative/innovation comprises M13–M30.** It begins with the entropy cost of a small displacement cell, combines the lower and upper bounds into a capacity law, and then develops classification, explicit examples and robustness. Its final milestones test how the result changes under a growing cyclic phase alphabet and connect that comparison to the original physical question.

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
| M11 | Background/preliminaries | Unconditional mean energy and entropy in infinite dimension |
| M12 | Background/preliminaries | The complete operational model and proof obligations |
| M13 | Narrative/innovation | Why the relevant displacement scale is inverse square-root energy |
| M14 | Narrative/innovation | A thermal lower bound from resolved noise entropy |
| M15 | Narrative/innovation | A one-use smooth-law comparison with Gaussian noise |
| M16 | Narrative/innovation | Tracking entanglement through an adaptive protocol |
| M17 | Narrative/innovation | The bridge between smoothing and quantization entropy |
| M18 | Narrative/innovation | Charging the smoothing environments at the physical resolution |
| M19 | Narrative/innovation | The shared finite-resolution law and the additive value of feedback |
| M20 | Narrative/innovation | Information dimension and the coefficient of logarithmic growth |
| M21 | Narrative/innovation | Finite alphabets and mixed discrete–continuous laws |
| M22 | Narrative/innovation | Bounded capacity and triple-logarithmic growth at dimension two |
| M23 | Narrative/innovation | A circle's one-dimensional noise and two-dimensional covariance |
| M24 | Narrative/innovation | Exact circular entropy exchange through charge sectors |
| M25 | Narrative/innovation | A capacity separation at matched covariance |
| M26 | Narrative/innovation | A positive finite-energy rate with nonzero Gaussian jitter |
| M27 | Narrative/innovation | The finite ceiling created by fixed broadening |
| M28 | Narrative/innovation | The general joint energy–broadening crossover |
| M29 | Narrative/innovation | The growing cyclic phase alphabet and the quantum environment of a shift |
| M30 | Narrative/innovation | What photon statistics and resolved displacement entropy determine |

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
- **Sources.** **Holevo:** §§7.1–7.2 (pp. 126, 127), 11.2 (p. 237). **Science:** [compare the two displacement laws](../science/03-converse.md#compare-the-two-displacement-laws-on-each-use).

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
- **Conceptual connection.** The unassisted coding theorem provides a regularized benchmark. The adaptive model allows classical messages and local operations between uses.
- **Sources.** **Holevo:** §§10.2.1–10.2.2 (pp. 195, 197), 10.3.1–10.3.3 (pp. 202, 206, 208). **Science:** [what capacity counts](../science/01-model.md#what-the-capacity-counts); [scope of the capacity law](../science/02-capacity-law.md#scope-of-the-capacity-law).

### M11 — Energy constraints and infinite-dimensional limits

- **Central question.** How can a mean constraint control the entropy of many modes whose energies may vary widely?
- **Understanding target.** Distinguish unconditional mean photon number from per-branch and per-mode maxima. Use the thermal entropy bound $`g(x)`$ for a mode of mean energy $`x`$, then use concavity to control the sum over a block. Connect trace-norm convergence and lower semicontinuity of relative entropy to finite approximations of a displacement law.
- **Dependencies and story role.** M01, M03, M07 and M10. Establishes the tools needed to account for the actual inputs and compare channels.
- **Conceptual connection.** A mean constraint bounds total entropy even when some uses or measurement histories carry large energy.
- **Sources.** **Holevo:** §§7.1–7.2 (pp. 126, 127), 11.1–11.2 (pp. 233, 237), 11.5 (p. 243). **Science:** [operational energy constraint](../science/01-model.md#what-the-capacity-counts) and [converse](../science/03-converse.md).

### M12 — The complete problem and its proof obligations

- **Central question.** Which rate claims require an unassisted code and which require an adaptive converse?
- **Understanding target.** Assemble a fixed known IID displacement law, unobserved kicks, finite second moment and an unconditional mean-photon constraint. Distinguish unassisted quantum capacity from two-way quantum capacity, which allows adaptive local operations and two-way classical communication from a separable initial state. Take the coding limit at fixed channel and energy before considering the high-energy limit.
- **Dependencies and story role.** M01–M11. Integrates the background into the complete operational framework.
- **Conceptual connection.** A thermal input supplies the lower bound for both tasks. The converse follows the entanglement generated in an adaptive protocol with its actual energy budget.
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

- **Central question.** How can a classical density comparison bound the entanglement generated on one channel use?
- **Understanding target.** Compare the actual input and a separable input with the same displacement processor, driven by a smooth density $`f`$ and the unit-variance Gaussian density $`g_1`$, respectively. Track the input relative entropy and the classical cost $`D(f\Vert g_1)`$ through data processing. Explain why the exact Gaussian output remains separable across the new sender–receiver split.
- **Dependencies and story role.** M05, M07, M08, M11 and M12. Turns classical relative entropy into a bound on the relative entropy of entanglement gained per use.
- **Conceptual connection.** Sender and receiver memories can be present in both inputs, so the comparison applies inside an adaptive protocol.
- **Sources.** **Holevo:** §§7.1–7.2 (pp. 126, 127), 11.7 (p. 248), 12.4.4 (p. 294). **Science:** [smooth-noise comparison](../science/03-converse.md#compare-the-two-displacement-laws-on-each-use).

### M16 — From a one-use estimate to an adaptive converse

- **Central question.** Why does a one-use entanglement bound constrain the rate of a feedback protocol?
- **Understanding target.** Begin with a separable state, sum the entanglement gained at channel uses and apply monotonicity under the local operations and classical communication between them. Convert the final bound into a rate with a maximally entangled-state test whose acceptance probability on any separable comparison is at most the reciprocal of the target dimension.
- **Dependencies and story role.** M08, M10, M11 and M15. Shows why the smooth-law upper bound covers adaptive codes.
- **Conceptual connection.** The rate bound follows the actual protocol, even when inputs correlate with earlier messages and channel outputs.
- **Sources.** **Holevo:** §§3.3.2 (p. 46), 7.1–7.2 (pp. 126, 127), 10.3.1 (p. 202), 11.1 (p. 233). **Science:** [adaptive converse](../science/03-converse.md#from-entanglement-accounting-to-a-rate-bound).

### M17 — Smoothing entropy equals resolved entropy up to scale

- **Central question.** What does a narrow Gaussian convolution preserve about a possibly singular noise law?
- **Understanding target.** Decompose the rescaled kick into an integer cell label and a remainder in a unit square. Explain why Gaussian smoothing produces differential entropy equal to $`2\log_2\sigma+H_{1/\sigma}(\mu)`$ up to universal additive constants, using bounded conditional uncertainty in both directions.
- **Dependencies and story role.** M06 and M07. Supplies the classical bridge from the smooth-law converse to the original arbitrary probability measure.
- **Conceptual connection.** Differential entropy becomes useful only after its smoothing scale is matched to a discrete resolution; the relation remains meaningful for singular measures.
- **Sources.** **Holevo:** §§4.1–4.2 (pp. 55, 57), 7.1 (p. 126). **Science:** [smoothing and quantization lemma](../science/03-converse.md#smoothing-entropy-and-quantization-entropy-differ-by-a-constant); [relative entropy after smoothing](../science/03-converse.md#relative-entropy-of-the-smoothed-law).

### M18 — Charging the smoothing environments

- **Central question.** Why can the converse smooth at the physical resolution and still incur only a constant loss per use?
- **Understanding target.** Set the Gaussian displacement variance to $`v=(E+1)^{-1}`$. Follow receiver-side pure loss and vacuum amplification with net gain one. Compare the relative entropy of entanglement before and after discarding the two environments. Bound their mean energies using the actual transmitted energies and the noise moment, then apply the thermal entropy bound and concavity.
- **Dependencies and story role.** M02, M03, M11, M16 and M17. Transfers the smooth-law upper bound to the actual channel at the same resolution as achievability.
- **Conceptual connection.** The environments belong to a local comparison operation in the proof. Their entropy budget is averaged over actual uses and their histories.
- **Sources.** **Holevo:** §§7.3 (p. 132), 7.6 (p. 141), 11.5 (p. 243), 12.3.4 (p. 281), 12.6.2 (p. 324). **Science:** [smoothing comparison and environment budget](../science/03-converse.md#adaptive-converse-at-the-energy-resolution).

### M19 — The finite-resolution capacity law

- **Central question.** How much can adaptive two-way communication improve the rate?
- **Understanding target.** State that the unassisted and two-way quantum capacities both lie within a bounded additive term of $`\log_2(E+1)-H_{\sqrt{E+1}}(\mu)`$ for $`E\ge1`$. Use the unassisted lower bound and adaptive upper bound to bound the gap by a constant depending only on the noise second-moment bound.
- **Dependencies and story role.** M14 and M18. Integrates the two proof branches into the main theorem.
- **Conceptual connection.** Both tasks have the same resolved classical entropy cost up to a bounded term. The theorem permits an additive benefit from feedback.
- **Sources.** **Holevo:** §§10.3.2 (p. 206), 11.5 (p. 243), for the capacity framework. **Science:** [finite-resolution theorem](../science/02-capacity-law.md#the-finite-resolution-capacity-law); [explicit converse constants](../science/03-converse.md#collecting-the-finite-resolution-upper-bound).

### M20 — Information dimension becomes a capacity coefficient

- **Central question.** How does increasingly fine classical resolution determine the leading energy dependence?
- **Understanding target.** Derive the high-energy coefficient $`1-d(\mu)/2`$ for both quantum capacities when information dimension exists. Explain the factor one-half from $`t=\sqrt{E+1}`$ and the exchange of lower and upper limits when the two information dimensions differ.
- **Dependencies and story role.** M06 and M19. Converts a finite-scale theorem into a global asymptotic classification.
- **Conceptual connection.** Information dimension measures entropy growth with resolution; it need not equal support dimension or the number of nonzero covariance eigenvalues.
- **Sources.** **Holevo:** §§4.1 (p. 55), 10.3.2 (p. 206), as entropy and capacity foundations. **Science:** [dimension corollary](../science/02-capacity-law.md#information-dimension-fixes-the-leading-energy-dependence); [dimension definitions](../science/01-model.md#entropies-and-phase-space-resolution).

### M21 — Discrete and mixed laws

- **Central question.** Which features of a noise distribution determine its dimension when qualitatively different components coexist?
- **Understanding target.** Explain why a finite kick alphabet has full logarithmic capacity growth and why $`p\delta_0+(1-p)\nu`$, with an absolutely continuous finite-moment $`\nu`$, has coefficient $`p`$. Keep the mixture label unobserved and distinguish this conclusion from an erasure-channel model with a receiver flag.
- **Dependencies and story role.** M06, M12 and M20. Tests the classification on laws for which support alone is misleading.
- **Conceptual connection.** Probability weights affect resolved entropy and hence capacity growth even when a continuous component fills two-dimensional phase space.
- **Sources.** **Holevo:** §§4.1–4.2 (pp. 55, 57), 6.3 (p. 108), 10.3.2 (p. 206). **Science:** [dimension-law consequences](../science/02-capacity-law.md#consequences); [unobserved-noise model](../science/01-model.md#one-oscillator-and-a-fixed-noise-law).

### M22 — Boundedness and very slow divergence

- **Central question.** What can happen to capacity at full information dimension?
- **Understanding target.** Explain why finite relative entropy $`D(\mu\Vert\gamma)`$ to the standard Gaussian gives bounded capacity, and how nested dyadic grids detect infinite relative entropy in the thermal lower bound. For the full-dimensional mixture of nested squares, relate the entropy deficit at dyadic grid depth $`m`$ to the truncated mean of the random square depth. The slowly decaying tail produces triple-logarithmic growth in energy.
- **Dependencies and story role.** M07, M14, M16, M19 and M20. Refines the slope classification and uses the constant-error theorem to resolve a slow growth law.
- **Conceptual connection.** Full information dimension permits either bounded capacity or unbounded sublogarithmic growth. The resolved entropy deficit decides which occurs.
- **Sources.** **Holevo:** §§7.1–7.2 (pp. 126, 127), 11.2 (p. 237), for relative-entropy foundations. **Science:** [bounded-capacity criterion and proof](../science/03-converse.md#when-is-the-unconstrained-capacity-finite) and [full-dimensional example](../science/02-capacity-law.md#a-full-dimensional-noise-density-with-unbounded-capacity).

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

- **Central question.** Which scale controls capacity when energy increases and Gaussian jitter decreases?
- **Understanding target.** For jitter variance $`b`$, combine the independent Gaussian variances into $`b+(E+1)^{-1}`$. Use the smoothing entropy comparison to identify that effective variance for an arbitrary finite-second-moment noise law. Recover the circular result with effective energy $`\min\{E,\sigma^{-2}\}`$ for $`b=\sigma^2`$ and the coefficient $`\min\{1/2,\alpha\}`$ for $`\sigma(E)=E^{-\alpha}`$ with positive $`\alpha`$.
- **Dependencies and story role.** M17, M19 and M25–M27. Reconciles the ideal circle and its finite-jitter limits using the general crossover law.
- **Conceptual connection.** Input energy improves resolution until it reaches the thickness created by independent Gaussian jitter.
- **Sources.** **Holevo:** §§11.5 (p. 243), 12.3.4 (p. 281), 12.6.4 (p. 328), as constraint and entropy foundations. **Science:** [general crossover](../science/05-broadening.md#the-general-energybroadening-crossover) and [order of limits](../science/05-broadening.md#orders-of-limits-and-scope).

### M29 — A growing cyclic phase alphabet changes the rate

- **Central question.** What changes when weak Gaussian displacement follows a cyclic phase twirl with a growing alphabet?
- **Understanding target.** Use the displacement-only estimate with base law $`\delta_0`$ to obtain $`\log_2 J+O(1)`$ at energy $`eJ`$ and variance $`\beta/J`$. Explain how the twirl leaves a code within one residue, how the output residue resolves the net shift modulo $`J`$, and why different loss and gain alternatives can still contribute to the same environmental vector.
- **Dependencies and story role.** M04, M09, M17, M24 and M28. Compares a new noise composition with the displacement-only result under the same energy and Gaussian variance.
- **Conceptual connection.** The two vacuum modes in the Gaussian dilation can retain conditional quantum information within a single observed shift.
- **Sources.** **Holevo:** §§6.6–6.7 (pp. 115, 119), 10.3.2–10.3.3 (pp. 206, 208), 12.6.2–12.6.4 (pp. 324–328). **Science:** [cyclic phase and weak displacement](../science/07-cyclic-phase.md).

### M30 — The complete operational conclusion

- **Central question.** What does the project establish about quantum communication through random phase-space noise, and where does the conclusion stop?
- **Understanding target.** Connect the finite-resolution law, dimension coefficient, boundedness criterion, circular separation and broadening crossover. Keep the model and input budget explicit. In the cyclic comparison, explain the strict gap between two limiting capacities with identical Fock transitions. Attribute the coding, Gaussian dilation and relative-entropy comparison to their sources and identify the distinct scope of the two capacity laws.
- **Dependencies and story role.** M12, M19–M22 and M25–M29. Synthesizes the narrative rather than adding another independent result.
- **Conceptual connection.** Resolved noise entropy controls the displacement-only law. Under the growing cyclic twirl, the overlaps within each shift determine the order-one rate as well.
- **Sources.** **Holevo:** §§7.1–7.3 (pp. 126–132), 10.3.2–10.3.3 (pp. 206, 208), 11.5 (p. 243), 12.6.4 (p. 328). **Science:** [connected scientific account](../science/README.md#the-connected-argument), [related work](../science/06-related-work.md), and [same-transition comparison](../science/07-cyclic-phase.md#what-the-shift-discards).
