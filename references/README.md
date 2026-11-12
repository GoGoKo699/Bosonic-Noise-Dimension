# Bibliography and imported ingredients

[Scientific comparison](../science/06-related-work.md) · [Structured bibliography](references.bib) · [Science route](../science/README.md)

The capacity statements in this repository combine established coding, continuity and simulation tools with the displacement-resolution argument proved in the scientific account. The entries below identify the specific role of each source. Citation does not mean that a source proves the new combination or the circular-noise conclusions.

<a id="wilde-qi"></a>
## Wilde–Qi: energy-constrained coding

Mark M. Wilde and Haoyu Qi, **Energy-constrained private and quantum capacities of quantum channels**, *IEEE Transactions on Information Theory* **64**, 7802–7827 (2018). [DOI](https://doi.org/10.1109/TIT.2018.2854766) · [arXiv:1609.01997v2](https://arxiv.org/abs/1609.01997v2).

Theorem 5 supplies the regularized coherent-information characterization used for ordinary energy-constrained quantum communication. Its Gibbs and finite-output-entropy hypotheses are checked for the model. The single thermal input in the achievable argument is not assumed to optimize capacity.

<a id="winter"></a>
## Winter: energy-constrained capacity continuity

Andreas Winter, **Energy-constrained diamond norm with applications to the uniform continuity of continuous variable channel capacities**, [arXiv:1712.10267v1](https://arxiv.org/abs/1712.10267v1) (2017).

Theorem 9 gives the quantum-capacity continuity estimate used in the converse. The source is an arXiv preprint, not presented here as a journal article. The proof uses its explicit modulus with a common affine output-energy bound and an energy-constrained diamond-distance estimate; the selected smoothing scale keeps the resulting capacity error bounded.

<a id="shirokov"></a>
## Shirokov: related continuity bounds

M. E. Shirokov, **Uniform continuity bounds for information characteristics of quantum channels depending on input dimension and on input energy**, *Journal of Physics A: Mathematical and Theoretical* **52**, 014001 (2019). [DOI](https://doi.org/10.1088/1751-8121/aaebac) · [arXiv:1610.08870v5](https://arxiv.org/abs/1610.08870v5).

Theorem 2 provides a complementary published energy-constrained continuity treatment. The quantitative coefficient in this repository is derived using Winter's displayed bound, rather than silently substituting a different distance convention or modulus from this paper.

<a id="plob"></a>
## PLOB: teleportation simulation and entanglement bounds

Stefano Pirandola, Riccardo Laurenza, Carlo Ottaviani and Leonardo Banchi, **Fundamental limits of repeaterless quantum communications**, *Nature Communications* **8**, 15043 (2017). [DOI and journal](https://doi.org/10.1038/ncomms15043) · [arXiv:1510.08863](https://arxiv.org/abs/1510.08863).

Teleportation covariance, channel simulation and relative-entropy-of-entanglement bounds are inherited tools. The converse applies them through finite-squeezing resource states, compares those states to an entanglement-breaking Gaussian channel, and makes the simulation-limit order explicit. It does not assume that a singular noise law has a finite classical relative entropy or that assisted and unassisted capacities are equal.

<a id="braunstein-kimble"></a>
## Braunstein–Kimble: continuous-variable teleportation

Samuel L. Braunstein and H. J. Kimble, **Teleportation of Continuous Quantum Variables**, *Physical Review Letters* **80**, 869–872 (1998). [DOI and journal](https://doi.org/10.1103/PhysRevLett.80.869).

The finite-squeezing teleportation protocol supplies the Gaussian simulation noise used in the converse. Its variance is translated to this repository's complex-displacement convention before taking the squeezing limit for a fixed code.

<a id="conditional-simulation"></a>
## Conditional channel simulation

Stefano Pirandola, Riccardo Laurenza and Leonardo Banchi, **Conditional channel simulation**, *Annals of Physics* **400**, 289–302 (2019). [DOI](https://doi.org/10.1016/j.aop.2018.11.014) · [arXiv:1807.00784v2](https://arxiv.org/abs/1807.00784v2).

Sections II, IV and V treat channel mixtures, asymptotic simulations, continuous ensembles and non-Gaussian examples. Non-Gaussian channel simulation itself is therefore not claimed as a new method here.

<a id="renyi"></a>
## Rényi: information dimension

Alfréd Rényi, **On the dimension and entropy of probability distributions**, *Acta Mathematica Academiae Scientiarum Hungaricae* **10**, 193–215 (1959). [Original paper, Rényi Institute archive](https://static.renyi.hu/renyi_cikkek/1959_on_the_dimension_and_entropy_of_probability_distributions.pdf).

The entropy growth of progressively finer quantizations defines information dimension. The present theorem identifies its coefficient in an energy-constrained quantum communication problem; the classical concept itself is inherited.

<a id="huber-koenig"></a>
## Huber–König: non-Gaussian classical communication

Stefan Huber and Robert König, **Coherent state coding approaches the capacity of non-Gaussian bosonic channels**, *Journal of Physics A: Mathematical and Theoretical* **51**, 184001 (2018). [DOI](https://doi.org/10.1088/1751-8121/aab7ff) · [arXiv:1710.06734v2](https://arxiv.org/abs/1710.06734v2).

This work treats classical communication over general bosonic noise models, including random displacement noise, and bounds the advantage beyond coherent-state coding. Its operational task differs from unassisted quantum communication.

<a id="de-palma-huber"></a>
## De Palma–Huber: additive-noise entropy power inequalities

Giacomo De Palma and Stefan Huber, **The conditional entropy power inequality for quantum additive noise channels**, *Journal of Mathematical Physics* **59**, 122201 (2018). [DOI](https://doi.org/10.1063/1.5027495) · [arXiv:1803.00470v2](https://arxiv.org/abs/1803.00470v2).

The paper develops conditional entropy inequalities for additive noise. Section 8.3 gives an entanglement-assisted classical-capacity application for noise densities. That statement is distinct from the present energy-dependent, unassisted quantum-capacity law for arbitrary finite-moment Borel measures.

<a id="lami-wilde"></a>
## Lami–Wilde: bosonic dephasing

Ludovico Lami and Mark M. Wilde, **Exact solution for the quantum and private capacities of bosonic dephasing channels**, *Nature Photonics* **17**, 525–530 (2023). [DOI and journal](https://doi.org/10.1038/s41566-023-01190-4).

The channel applies random number-generated phase rotations. Those commuting errors differ from planar Weyl displacements. The exact dephasing solution is an important nearby capacity result, not a specialization of the channel studied here.

<a id="wolf"></a>
## Wolf–Pérez-García–Giedke: Gaussian quantum capacities

Michael M. Wolf, David Pérez-García and Géza Giedke, **Quantum Capacities of Bosonic Channels**, *Physical Review Letters* **98**, 130501 (2007). [DOI and journal](https://doi.org/10.1103/PhysRevLett.98.130501).

Gaussian channel structure and covariance-based bounds provide context. A Gaussian benchmark does not supply a general covariance-only upper bound on every non-Gaussian channel with the same second moments.

<a id="lin-noh"></a>
## Lin–Noh: explicit GKP coding for Gaussian noise

Mao Lin and Kyungjoo Noh, **Exploring the quantum capacity of a Gaussian random-displacement channel using Gottesman–Kitaev–Preskill codes and maximum-likelihood decoding**, *Physical Review A* **111**, 052445 (2025). [DOI and journal](https://doi.org/10.1103/PhysRevA.111.052445) · [arXiv:2411.04277](https://arxiv.org/abs/2411.04277).

Explicit multimode GKP codes and decoding thresholds address implementable Gaussian-noise communication. This repository establishes unrestricted capacity bounds; it does not provide a comparable explicit decoder or an exact finite-energy Gaussian-capacity solution.

<a id="skellam"></a>
## Skellam distribution

J. G. Skellam, **The Frequency Distribution of the Difference between Two Poisson Variates Belonging to Different Populations**, *Journal of the Royal Statistical Society* **109**(3), 296 (1946). [Publisher](https://doi.org/10.1111/j.2397-2335.1946.tb04670.x).

The difference of independent Poisson variables is the classical Skellam distribution. The circle calculation derives why that distribution gives the spectrum of a displaced-purification twirl.

<a id="integer-entropy"></a>
## Integer-valued entropy bound

James L. Massey, **On the Entropy of Integer-Valued Random Variables**, *Proceedings of the Beijing International Workshop on Information Theory*, Beijing, 4–7 July 1988. [Author's archived paper](https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI527.pdf).

Adding an independent unit-width uniform variable converts discrete entropy to differential entropy and adds variance $`1/12`$. The resulting variance-based entropy bound is reproduced in the circle and broadening arguments, so the finite witness can be checked directly.

<a id="phase-project"></a>
## Related entropy-resolution project

**Bosonic Phase Noise Capacity**, [source at commit `2080352d5c356b3a87d8cc8780b787bc3ca0fc5f`](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/tree/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f).

The [phase quantization](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/blob/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f/science/02-phase-quantization.md) and [capacity](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/blob/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f/science/03-capacity.md) accounts are the closest conceptual antecedent: capacity loss is expressed through noise entropy at the energy-dependent resolution. The different commutative model, resolution and proof tools are compared explicitly in [Related work](../science/06-related-work.md). This is a source-revision citation, not a claim of peer-reviewed publication or an adopted joint project.
