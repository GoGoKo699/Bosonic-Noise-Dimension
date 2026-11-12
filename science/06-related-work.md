# Relation to prior work

[Science route](README.md) · Previous: [Gaussian broadening](05-broadening.md) · [References](../references/README.md)

The contribution is an energy-resolved capacity law for random Weyl displacements whose probability distribution can be singular, discrete, continuous, or mixed. The noise law is fixed and known, successive draws are independent, and the actual displacement is not disclosed. Under a finite noise second moment and an unconditional mean input photon-number constraint, the result concerns the regularized, unassisted quantum capacity. It does not assume degradability or restrict the encoder to Gaussian states.

The central estimate identifies the noise entropy at phase-space resolution proportional to $`E^{-1/2}`$. If the two-dimensional Rényi information dimension $`d_I`$ exists, the resulting coefficient of $`\log_2 E`$ is $`1-d_I/2`$. The generic additive error is $`O(\log\log E)`$, with constants controlled by the noise moment. Information dimension, noise quantization, coherent-information coding, and teleportation-based capacity bounds are established ideas. Their roles and the additional conclusion are separated below.

## The closest antecedent: energy-resolved phase noise

The companion [Bosonic-Phase-Noise-Capacity result](../references/README.md#phase-project) already establishes the shared organizing principle: quantum capacity can be governed by the entropy of the noise at the resolution accessible with a given oscillator energy. The comparison here is with its [capacity proof at commit `2080352d5c356b3a87d8cc8780b787bc3ca0fc5f`](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/blob/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f/science/03-capacity.md), rather than with its repository title alone.

That project treats random number rotations. It proves a constant-gap expression $`\log_2 E-H_{\lceil E\rceil}(\mu)+O(1)`$, where the noise entropy is taken over angular bins. Its constant is uniform in the phase distribution. Degradability reduces the capacity problem to one use and a diagonal photon-number distribution; a finite cyclic dephasing comparison and a photon-number shell argument control the full mean-energy constraint.

| Feature | Number-rotation noise | Weyl-displacement noise here |
| --- | --- | --- |
| Random unitary | $`e^{-i\theta N}`$ | $`D(z)=e^{za^\dagger-z^*a}`$ |
| Error algebra | Commuting rotations in a common number basis | Generally noncommuting displacements in two quadratures |
| Noise coordinates | One angular coordinate | Two real phase-space coordinates |
| Relevant resolution | Angular scale proportional to $`E^{-1}`$ | Spatial scale proportional to $`E^{-1/2}`$ |
| Capacity reduction | Degradability and a single-use optimization | Arbitrary-block converse without a degradability assumption |
| Generic remainder | A noise-uniform constant | A logarithmic-logarithmic error with moment-dependent constants |

The phase proof does not transfer merely by replacing the angular variable with two Cartesian coordinates. The displacement channel lacks the common eigenbasis and degrading map used there. Its converse instead requires an energy-controlled smoothing step and a separable Gaussian comparison. Thus the shared entropy-resolution principle is inherited explicitly; the additional bridge is to a noncommuting displacement channel with general quantum coding allowed.

The earlier external result of [Lami and Wilde](../references/README.md#lami-wilde) gives exact unconstrained quantum and private capacities for bosonic dephasing channels, expressed through the phase distribution's relative entropy to the uniform law. It is an important antecedent for entropy-based capacity statements in non-Gaussian oscillator noise. Its commuting random-rotation model and unconstrained exact formula differ from the finite-energy, two-dimensional displacement statement here.

## General additive noise was already studied

[Huber and König](../references/README.md#huber-koenig) explicitly study bosonic channels with general probabilistic displacement noise; their Eq. (9) is the same additive-noise construction when the noise has a density. Their operational task is classical communication. They show that coherent-state modulation approaches classical capacity within a noise-dependent constant independent of the input energy. Neither the model of non-Gaussian additive noise nor the use of entropy bounds for it originates here.

[De Palma and Huber](../references/README.md#de-palma-huber) establish the conditional entropy power inequality for quantum additive noise channels. Section 8.3 applies it to an entanglement-assisted classical-capacity converse for a general noise density. This supplies substantial antecedent work on the interplay between classical noise entropy and quantum channel outputs. It does not state the present singular-measure quantization law for unassisted quantum capacity.

The distinction between communication tasks matters. A classical-capacity estimate or an entanglement-assisted classical converse does not, by itself, determine the regularized unassisted quantum rate. Also, a singular probability law need not have a differential entropy. The finite-bin entropy in the present theorem remains defined in that case, and Gaussian smoothing is introduced only inside the converse.

## Which proof ingredients are inherited

The operational meaning of regularized coherent information under a mean-energy constraint comes from [Wilde and Qi](../references/README.md#wilde-qi). The oscillator Hamiltonian satisfies their Gibbs condition, and the finite noise second moment supplies finite output entropy on every energy-bounded input set. This is the coding foundation for the thermal-input achievable rate; the repository does not introduce a new general coding theorem.

The capacity-continuity step uses [Winter's energy-constrained theorem](../references/README.md#winter). Related general continuity results are due to [Shirokov](../references/README.md#shirokov). This step is needed at the level of capacity: a small one-use approximation error alone would not justify an interchange with arbitrarily large blocklength. The displacement estimate and affine output-energy bound verify the hypotheses for the noise laws compared here.

Teleportation covariance, stretching, and relative entropy of entanglement are inherited from [Pirandola, Laurenza, Ottaviani, and Banchi](../references/README.md#plob). The applicability of simulation methods to continuous ensembles and non-Gaussian mixtures is also established in [Pirandola, Laurenza, and Banchi, *Conditional channel simulation*](../references/README.md#conditional-simulation). Non-Gaussianity alone is not a new reason those techniques apply.

The application here compares each finite-squeezing channel resource state with the resource state produced by an entanglement-breaking Gaussian displacement channel. Classical-to-quantum data processing bounds their relative entropy by the classical relative entropy between the noise laws. For any fixed finite-block code, the simulation limit is taken before the coding limit. A test against the finite-dimensional target entangled state then supplies the converse. The simulator's diverging squeezing is an auxiliary upper-bound construction, not an uncharged resource in an achievable communication protocol.

The additional argument connects that smooth-noise bound to the original, possibly singular distribution at the input-energy resolution. The lower bound makes the same connection directly: conditional on a square noise bin, inverse two-mode squeezing leaves a uniformly bounded residual energy and hence bounded entropy. Combining those two estimates controls arbitrary codes while using a thermal state only for achievability.

## Gaussian coding results and the covariance comparison

The Gaussian bosonic-capacity literature, including [Wolf, Pérez-García, and Giedke](../references/README.md#wolf), supplies essential benchmarks and methods. More recently, [Lin and Noh](../references/README.md#lin-noh) examine quantum communication through Gaussian random-displacement noise using Gottesman–Kitaev–Preskill codes and maximum-likelihood decoding. The theorem here does not determine the exact quantum capacity of a Gaussian additive-noise channel, optimize such a decoder, or establish Gaussian-code optimality. A zero logarithmic coefficient leaves the finite capacity value undetermined.

The [circular-noise example](04-circular-noise.md) gives a concrete consequence beyond a formal change of channel class. A uniform kick of fixed nonzero amplitude has an isotropic, full-rank covariance, yet its support is one-dimensional. Its capacity grows with coefficient one half. The Gaussian law with the same covariance can be entanglement breaking and therefore have zero quantum capacity at every energy. The point is the proved scalable-versus-zero separation for a specified pair of channels; there is no claim that the general insufficiency of second moments was previously unknown.

## Robustness and the boundary of the result

The [bounded-capacity criterion](03-converse.md#when-is-the-unconstrained-capacity-finite) is a further consequence of the same proof: at finite noise second moment, capacity stays bounded as energy increases exactly when the noise law has finite relative entropy to a full-support Gaussian. The finite-relative-entropy upper bound uses the inherited simulation machinery; the other direction follows from the thermal lower bound and convergence of relative entropy under nested partitions. This is a finiteness criterion, not an equality between quantum capacity and classical relative entropy. It distinguishes bounded rates from unbounded sublogarithmic growth when the information dimension is two.

Exact singular support is an idealization. Adding any fixed positive Gaussian jitter makes the circular law full-dimensional and removes its asymptotic logarithmic growth. The [broadening analysis](05-broadening.md) states the two-parameter regime explicitly: the half-logarithmic behavior persists up to an energy scale proportional to the inverse jitter variance, followed by a bounded-capacity regime. Its finite-energy positive-rate witness includes the jitter and compares against a covariance-matched entanglement-breaking Gaussian channel. It does not exchange the zero-jitter and infinite-energy limits.

The result is a capacity statement for independent random displacements without photon loss or access to a classical noise flag. It provides neither an efficient encoder nor a finite-block error guarantee. The reviewed primary sources and the pinned phase-noise comparison do not state the same finite-resolution theorem; this comparison supports the specified contribution without asserting an exhaustive priority claim.
