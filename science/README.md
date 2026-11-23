# Scientific account

**How does the fine-scale geometry of random phase-space kicks control bosonic quantum capacity?** The entropy of the noise resolved by the energy budget determines both ordinary and adaptive two-way-assisted rates to an additive constant.

| Question | Authoritative account |
|---|---|
| Which displacement channel, codes and energy constraint are being studied? | [Model and operational question](01-model.md) |
| What rate does thermal coding attain, and what does information dimension tell us? | [Capacity law and achievability](02-capacity-law.md) |
| Why does the upper bound hold for adaptive two-way communication? | [Energy-resolution converse and capacity finiteness](03-converse.md) |
| Can isotropic kicks in two quadratures give a divergent capacity? | [Circular noise](04-circular-noise.md) |
| Can full information dimension also give a divergent capacity? | [A full-dimensional density with triple-logarithmic growth](02-capacity-law.md#a-full-dimensional-noise-density-with-unbounded-capacity) |
| How do energy and Gaussian jitter jointly determine the usable resolution? | [General crossover and the broadened-circle witness](05-broadening.md) |
| Which mechanisms are inherited, and what differs from existing results? | [Related work](06-related-work.md) and [bibliography](../references/README.md) |
| Can identical photon-number transitions give different capacities? | [Cyclic phase and weak displacement](07-cyclic-phase.md) |
| Which numerical statements can be reproduced? | [Finite verification](../verification/README.md) |

## The connected argument

The model fixes the noise law and constrains mean input photons over the coding block. A thermal input resolves displacements on a scale proportional to the inverse square root of its energy. Grouping nearby kicks bounds the entropy exchanged with the environment and gives an achievable unassisted rate.

The converse smooths the noise at that same scale. A comparison with an entanglement-breaking Gaussian reference bounds the smoothed channel's two-way-assisted rate through classical relative entropy. The smoothing can be removed at a constant cost per use by controlling the entropy of the auxiliary vacuum modes that realize it. This keeps the resolution used in the upper bound at the one reached by the attaining thermal input.

Both capacities have leading coefficient one minus half the noise information dimension. A circle has dimension one despite isotropic covariance and separates from a covariance-matched entanglement-breaking Gaussian. For a concrete density of dimension two the subleading entropy still leaves triple-logarithmic communication growth. Adding independent Gaussian jitter limits the resolution available at high energy. The broadened-circle calculation gives an explicit achievable rate at finite energy.

In the [cyclic-phase comparison](07-cyclic-phase.md), adding a growing phase twirl before weak Gaussian displacement changes the logarithmically growing rate into a finite limiting rate at the same input budget and displacement scale. The comparison isolates an environment contribution that remains invisible to photon-number transition probabilities.

The theorem concerns unrestricted asymptotic communication. The finite computations check the stated examples and identities, while the written converse treats arbitrary allowed codes.
