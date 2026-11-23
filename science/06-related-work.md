# Relation to prior work

[Science route](README.md) · Previous: [Gaussian broadening](05-broadening.md) · [References](../references/README.md)

The [capacity law](02-capacity-law.md) identifies the quantum communication rate up to an additive constant for a known iid Weyl-displacement law with finite second moment. The law may be discrete, absolutely continuous, singular continuous or mixed. The same estimate controls the unassisted capacity and the capacity with adaptive two-way classical communication. Its error depends only on the bound on the noise second moment. In particular, two-way communication can add at most a constant independent of input energy.

The estimate retains the full bin entropy at phase-space resolution $`(E+1)^{-1/2}`$. When the two-dimensional Rényi information dimension $`d_I`$ exists, the coefficient of $`\log_2 E`$ is $`1-d_I/2`$. Keeping the bin entropy also distinguishes rates below the logarithmic scale. Information dimension, noise quantization, coherent-information coding and relative-entropy bounds for adaptive protocols are established ingredients.

## The closest antecedent: energy-resolved phase noise

The companion Bosonic-Phase-Noise-Capacity result establishes that quantum capacity can be governed by the entropy of the noise at the resolution accessible with a given oscillator energy. [Capacity proof at commit `2080352d5c356b3a87d8cc8780b787bc3ca0fc5f`](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/blob/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f/science/03-capacity.md)

That project treats random number rotations. It proves a constant-gap expression $`\log_2 E-H_{\lceil E\rceil}(\mu)+O(1)`$, where the noise entropy is taken over angular bins. Its constant is uniform in the phase distribution. Degradability reduces the capacity problem to one use and a diagonal photon-number distribution; a finite cyclic dephasing comparison and a photon-number shell argument control the full mean-energy constraint.

| Feature | Number-rotation noise | Weyl-displacement noise here |
| --- | --- | --- |
| Random unitary | $`e^{-i\theta N}`$ | $`D(z)=e^{za^\dagger-z^*a}`$ |
| Error algebra | Commuting rotations in a common number basis | Generally noncommuting displacements in two quadratures |
| Noise coordinates | One angular coordinate | Two real phase-space coordinates |
| Relevant resolution | Angular scale proportional to $`E^{-1}`$ | Spatial scale proportional to $`E^{-1/2}`$ |
| Capacity proof | Degradability and a single-use optimization | Thermal-input lower bound and adaptive relative-entropy converse |
| Additive error | A noise-uniform constant | A constant depending only on the noise second-moment bound |

The phase proof relies on the common eigenbasis of number rotations and their dephasing structure. The displacement proof compares the noise with a separable Gaussian reference after smoothing at the energy resolution. It bounds the entanglement gained per use while accounting for the memory carried between uses.

The earlier external result of [Lami and Wilde](../references/README.md#lami-wilde) gives exact unconstrained quantum and private capacities for bosonic dephasing channels, expressed through the phase distribution's relative entropy to the uniform law. It is an important antecedent for entropy-based capacity statements in non-Gaussian oscillator noise. Its commuting random-rotation model and unconstrained exact formula differ from the finite-energy, two-dimensional displacement statement here.

## General additive noise was already studied

[Huber and König](../references/README.md#huber-koenig) explicitly study bosonic channels with general probabilistic displacement noise; their Eq. (9) is the same additive-noise construction when the noise has a density. Their operational task is classical communication. They show that coherent-state modulation approaches classical capacity within a noise-dependent constant independent of the input energy. Neither the model of non-Gaussian additive noise nor the use of entropy bounds for it originates here.

De Palma and Huber establish the conditional entropy power inequality for quantum additive-noise channels. Section 8.3 applies it to an entanglement-assisted classical-capacity converse for a general noise density. [De Palma and Huber](../references/README.md#de-palma-huber)

The present theorem addresses quantum communication with optional two-way classical messages. Its bin entropy remains defined for singular laws. The converse introduces a Gaussian smoothing operation whose effect on entanglement can be bounded directly.

## Which proof ingredients are inherited

The operational meaning of regularized coherent information under a mean-energy constraint comes from [Wilde and Qi](../references/README.md#wilde-qi). The oscillator Hamiltonian satisfies their Gibbs condition, and the finite noise second moment supplies finite output entropy on every energy-bounded input set. This is the coding foundation for the thermal-input achievable rate; the repository does not introduce a new general coding theorem.

The [converse](03-converse.md#adaptive-converse-at-the-energy-resolution) bounds the relative entropy of entanglement generated in each actual use. The smoothed noise and the Gaussian reference can drive the same displacement operation. Comparing the two classical laws bounds the relative entropy added by this operation. Proposition 33 of Wilde, Berta, Hirche and Kaur gives the shared-interaction comparison for environment-parametrized channels. Here the displacement law is continuous, and a finite-partition limit gives the comparison on the oscillator and its retained memories. [Wilde et al.](https://arxiv.org/abs/1808.01498)

The smoothing operation is the established pure-loss and quantum-limited-amplifier factorization of a phase-insensitive Gaussian channel. Both discarded outputs have finite mean energy when the input does. The proof bounds the reduction of relative entropy of entanglement by twice their joint entropy and then averages over the actual use energies. This is an entropy bound for oscillator environments, related to the finite-dimensional non-lockability result of Horodecki, Horodecki, Horodecki and Oppenheim. The capacity proof uses the factorization as a local receiver operation in the converse. [Sharma et al.](https://arxiv.org/abs/1708.07257) · [Horodecki et al.](https://arxiv.org/abs/quant-ph/0404096)

The use of relative entropy of entanglement to bound arbitrary adaptive protocols builds on the PLOB framework. Conditional channel simulation establishes related upper-bound methods for continuous ensembles and non-Gaussian mixtures. The earlier displacement argument used finite-squeezing simulation for the smooth-noise bound and energy-constrained capacity continuity to compare the original and smoothed channels. The finer smoothing scale required in that argument gave a double-logarithmic error. Bounding the entanglement change directly makes smoothing at the energy resolution possible. [PLOB](../references/README.md#plob) · [Conditional channel simulation](../references/README.md#conditional-simulation) · [Winter](../references/README.md#winter) · [Shirokov](../references/README.md#shirokov)

The lower bound links the same resolution to the original law directly. Conditional on a square noise bin, inverse two-mode squeezing leaves a uniformly bounded residual energy in the two modes and hence a bounded entropy. The thermal input is used for achievability. The upper bound applies to all codes permitted by the corresponding energy constraint.

## Gaussian coding results and the covariance comparison

The Gaussian bosonic-capacity literature, including [Wolf, Pérez-García, and Giedke](../references/README.md#wolf), supplies essential benchmarks and methods. More recently, [Lin and Noh](../references/README.md#lin-noh) examine quantum communication through Gaussian random-displacement noise using Gottesman–Kitaev–Preskill codes and maximum-likelihood decoding. The theorem here does not determine the exact quantum capacity of a Gaussian additive-noise channel, optimize such a decoder, or establish Gaussian-code optimality. A zero logarithmic coefficient leaves the finite capacity value undetermined.

For Gaussian channels, Pirandola derives adaptive two-way converses under the same unconditional constraint on mean transmitted photons. They cover thermal attenuation, amplification and additive Gaussian noise and give finite-energy comparisons specific to those Gaussian families. Barber and Pirandola obtain exact finite-mean-energy capacities for those families under PPT-preserving assistance, which includes a larger class of operations than LOCC. These results provide Gaussian benchmarks for the present question. The phase-space bin-entropy law applies across arbitrary displacement laws, with the finite-error estimate under LOCC. [Pirandola](https://arxiv.org/abs/2610.08786v2) · [Barber and Pirandola](https://arxiv.org/abs/2610.26783v1)

The [circular-noise example](04-circular-noise.md) gives a concrete consequence beyond a formal change of channel class. A uniform kick of fixed nonzero amplitude has an isotropic, full-rank covariance, yet its support is one-dimensional. Its capacity grows with coefficient one half. The Gaussian law with the same covariance can be entanglement breaking and therefore have zero quantum capacity at every energy. The pair therefore separates a growing unassisted rate from zero even with two-way classical communication.

## Robustness and the boundary of the result

At finite noise second moment, capacity stays bounded as energy increases exactly when the noise law has finite relative entropy to a full-support Gaussian. The smooth-noise comparison bounds both capacities when that relative entropy is finite. In the other direction, the thermal lower bound and convergence of relative entropy under nested partitions imply that both rates are unbounded. This distinguishes bounded rates from unbounded sublogarithmic growth when the information dimension is two. [Bounded-capacity criterion](03-converse.md#when-is-the-unconstrained-capacity-finite)

Adding fixed positive Gaussian jitter gives the circular law a density and caps its capacity. The [broadening analysis](05-broadening.md) gives a joint bound for every displacement law with finite second moment. The effective bin scale combines jitter and input-energy resolution. For a circle this leads to half-logarithmic growth up to an energy scale proportional to the inverse jitter variance. The finite-energy witness gives a positive unassisted rate at explicit nonzero jitter against a covariance-matched entanglement-breaking Gaussian channel.

The displacement-resolution estimate concerns asymptotic communication through independent, undisclosed displacements. Efficient code construction, finite-block guarantees and correlated noise are separate problems.

## Combining weak displacement with cyclic phase noise

The [cyclic-phase comparison](07-cyclic-phase.md) adds a growing finite phase alphabet and optional weak physical loss. It uses the standard [Gaussian operator sums](../references/README.md#ivan-sabapathy-simon) to retain coherence between attenuator and amplifier counts with the same net shift. [Arqand and Smith](../references/README.md#arqand-smith) obtain an adaptive converse by comparing number-preserving dephasing to complete dephasing. The [phase-loss companion theorem](https://github.com/GoGoKo699/Discrete-Phase-Loss-Capacity/blob/16be1722f0b2b9a1a020f6d74b37a7a7824d2f11/science/critical-displacement.md) uses this comparison on a channel with the exact shift supplied to the receiver and controls the loss from keeping only the modular syndrome. This leads to an exact limiting capacity and a strict optimized gap between channels that have the same Fock transition law.

