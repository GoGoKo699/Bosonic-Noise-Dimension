# Learning the noise-dimension law

[Project overview](../README.md) · [Thirty milestones](MILESTONES.md) · [Holevo bridge](HOLEVO_BRIDGE.md) · [Scientific account](../science/README.md)

Imagine sending quantum information through an oscillator that receives a fresh, unobserved kick in phase space on every use. More input energy can make finer differences between kicks relevant. The central question is how the uncertainty in those increasingly resolved kicks competes with the oscillator's increasing capacity to carry quantum information.

The selected educational anchor is **Alexander S. Holevo, *Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (2019)**. Its [edition and source record](../references/README.md#holevo) and the [notation and proof bridge](HOLEVO_BRIDGE.md) give precise reading locations. The bridge supplies the needed project-specific steps alongside the book's foundations; it does not require reading the whole book first.

## A route through the project

The [common map](MILESTONES.md) contains exactly thirty understanding targets, organized by the scientific dependencies. Its first twelve milestones assemble the foundations; the remaining eighteen develop and interpret the contribution. The following route groups those targets without adding another curriculum.

| Milestones | Question to understand | Main explanation |
|---|---|---|
| M01–M06 | What are the carrier, its energy, the noise and the entropies being compared? | [Model](../science/01-model.md) and [convention translation](HOLEVO_BRIDGE.md#translating-canonical-variables-into-the-projects-photon-scale) |
| M07–M12 | How do entropy comparisons become operational statements about arbitrary quantum codes? | [Capacity framework](HOLEVO_BRIDGE.md#from-coherent-information-to-the-stated-capacity) |
| M13–M19 | Why do the achievable and upper bounds contain the same finite-resolution noise entropy? | [Lower bound](../science/02-capacity-law.md) and [converse](../science/03-converse.md) |
| M20–M22 | What do information dimension and relative entropy each classify? | [Dimension consequences](../science/02-capacity-law.md#consequences) and [boundedness criterion](../science/03-converse.md#when-is-the-unconstrained-capacity-finite) |
| M23–M28 | How do the circle, the finite-jitter example and the crossover express the result physically? | [Circle](../science/04-circular-noise.md), [worked example](HOLEVO_BRIDGE.md#worked-example-a-broadened-ring-versus-its-gaussian-comparator) and [broadening](../science/05-broadening.md) |
| M29–M30 | What is inherited, what is established here, and which conclusions remain outside the model? | [Related work](../science/06-related-work.md) and [scope](../science/01-model.md#boundaries-of-the-physical-comparison) |

## The mechanism in one connected account

### Energy supplies entropy and resolution

One channel use transmits one bosonic mode. The mean input photon number is bounded by $`E`$, and a thermal state with that mean has entropy

```math
g(E)=(E+1)\log_2(E+1)-E\log_2E.
```

At high energy this is $`\log_2E+O(1)`$. It sets the entropy scale available to the communication problem. It is not already the noisy channel's capacity.

Purify the thermal state with a reference mode, send the transmitted mode through the channel, and examine the joint reference–output entropy. This entropy exchange measures the noise cost in coherent information. The reference is a device for analyzing quantum correlations, not free entanglement shared by the communicating parties.

The key local calculation places displacement space into squares of side $`(E+1)^{-1/2}`$. Within one square, remove its corner displacement and undo the purification's two-mode squeezing. The remaining mixture has bounded total photon number, hence bounded entropy, independently of $`E`$. Restoring uncertainty about which square occurred costs the Shannon entropy of its cell label. Therefore the thermal input achieves available entropy minus the resolved noise entropy, up to a constant. [The full derivation](../science/02-capacity-law.md#why-one-thermal-input-suffices-for-the-lower-bound) makes both estimates explicit.

### A different argument limits arbitrary codes

The upper bound follows an adaptive protocol one channel use at a time. First smooth the noise law with Gaussian jitter and compare its output to that of an entanglement-breaking Gaussian. Relative-entropy data processing bounds how much entanglement the smoothed channel can add in one use, even when the parties already hold memories.

To use this estimate on the original channel, add the smoothing locally to each actual receiver output in the proof. The transformation can be realized by pure loss followed by vacuum amplification. The entanglement lost by discarding the two environments is bounded by twice their entropy. At smoothing variance $`(E+1)^{-1}`$, their average energy stays bounded because the actual protocol obeys an unconditional mean input constraint. Summing these one-use bounds gives a constant entropy cost per use at the physical noise resolution. See the [adaptive converse](../science/03-converse.md) for the energy accounting and its conversion to a rate.

Write

```math
A_\mu(E)=\log_2(E+1)-H_{\sqrt{E+1}}(\mu).
```

Here $`H_t(\mu)`$ is the discrete entropy of the two-dimensional grid label at scale $`t`$. Together the two arguments give, for $`E\ge1`$,

```math
A_\mu(E)-2g(2)\le Q_\mu(E)\le Q_{2,\mu}(E)\le A_\mu(E)+C_M.
```

The constant $`C_M`$ depends only on the noise second-moment bound. The unassisted and two-way quantum capacities share the same entropy law up to a bounded term.

### Geometry determines how quickly resolved uncertainty grows

If $`H_t(\mu)=d\log_2t+o(\log t)`$, substituting $`t=\sqrt{E+1}`$ converts the classical coefficient $`d`$ into the same high-energy coefficient for both quantum capacities.

```math
\lim_{E\to\infty}\frac{Q_\mu(E)}{\log_2E}
=\lim_{E\to\infty}\frac{Q_{2,\mu}(E)}{\log_2E}
=1-\frac d2.
```

For a finite kick alphabet, grid entropy eventually stops growing, so the coefficient is one. A uniformly random kick around a fixed nonzero circle has coefficient one for its grid entropy and one-half for capacity. An ordinary two-dimensional density has information dimension two and zero logarithmic capacity coefficient. These examples compare entropy growth under finer resolution; covariance rank alone cannot make the classification. [The theorem and its hypotheses](../science/02-capacity-law.md#information-dimension-fixes-the-leading-energy-dependence) also cover unequal lower and upper information dimensions.

A zero coefficient leaves open slower unbounded growth. One full-dimensional example freezes a sparse sequence of binary digits, losing one bit of resolved noise entropy for each frozen digit. The number of missing bits grows on a triple-logarithmic energy scale. The [boundedness theorem](../science/03-converse.md#when-is-the-unconstrained-capacity-finite) gives the exact alternative. Under the finite-second-moment hypothesis, bounded capacity over all finite budgets is equivalent to finite classical relative entropy to the standard complex Gaussian.

## A physical example and its limits

The exact circle has isotropic covariance in both quadratures, yet its capacity diverges with half-logarithmic growth. A Gaussian law with the same covariance is entanglement breaking once its complex displacement variance reaches one, and then has zero quantum capacity. The circle demonstrates why those second moments do not determine the communication rate.

The [worked calculation](HOLEVO_BRIDGE.md#worked-example-a-broadened-ring-versus-its-gaussian-comparator) adds nonzero Gaussian jitter. At radius $`r=2`$, energy $`E=100`$ and jitter width $`\sigma=0.01`$, it proves a lower bound of **1.0598044894 qubits per use**; the matched Gaussian still has zero capacity. The calculation follows the Gaussian intermediate state's entropy and then bounds the entropy created by averaging its charge sectors. [Verification](../verification/README.md) reproduces the numbers and documents numerical limits.

At any fixed positive jitter, the broadened circle has a finite capacity ceiling. The [general crossover](../science/05-broadening.md) adds the jitter variance to the variance $`(E+1)^{-1}`$ set by the carrier. For the circle, this gives an effective energy of order $`\min\{E,\sigma^{-2}\}`$ at small positive jitter width $`\sigma`$. The same variance rule applies to any base law with bounded second moment.

Both capacity statements use a known IID law with finite second moment, with each actual kick hidden and the mean-photon budget averaged over the block. The physical channel applies displacements only. Loss and amplification enter the converse as an auxiliary operation on the receiver's output. The capacity theorem describes asymptotic rates. Efficient implementations and guarantees at fixed blocklength are separate questions.
