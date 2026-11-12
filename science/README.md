# Scientific account

**How does the fine-scale geometry of random phase-space kicks control bosonic quantum capacity?** The answer is expressed through the classical entropy of the kick law at the resolution reached by an energy-constrained oscillator.

| Question | Authoritative account |
|---|---|
| Which channel, code and energy constraint are being studied? | [Model and operational question](01-model.md) |
| What is the finite-resolution capacity law, and what follows for information dimension? | [Capacity law and achievability](02-capacity-law.md) |
| Why does the upper bound hold for arbitrary collective codes? | [Converse and capacity finiteness](03-converse.md) |
| Can two quadratures have isotropic noise while capacity still diverges? | [Circular noise](04-circular-noise.md) |
| What survives when the circle is broadened by Gaussian jitter? | [Broadening, finite-energy witness and crossover](05-broadening.md) |
| Which mechanisms are inherited, and what differs from existing results? | [Related work](06-related-work.md) and [bibliography](../references/README.md) |
| Which numerical statements can be reproduced? | [Finite verification](../verification/README.md) |

## The connected argument

The model fixes the noise law and constrains mean input photons, while permitting arbitrary block codes. A thermal input resolves phase-space displacements on a scale proportional to the inverse square root of its energy. Grouping nearby displacements bounds the entropy exchanged with the environment and gives an achievable rate.

That rate becomes a capacity law only after a converse. Gaussian smoothing connects an arbitrary Borel noise law to a density. A separable Gaussian reference bounds the smooth channel's communication rate through classical relative entropy, and an energy-constrained continuity theorem returns to the original channel. The smoothing scale is chosen so that the continuity cost stays bounded; it introduces the logarithmic-logarithmic remainder in the general upper bound.

The resulting leading coefficient is one minus half the information dimension of the noise. A circle has dimension one even though its covariance has rank two. It therefore gives an explicit separation from a covariance-matched entanglement-breaking Gaussian. The circular model also permits an exact expression for thermal-input exchange entropy, strengthening the finite-energy interpretation. Gaussian broadening has full dimension, but a quantitative finite-energy witness and a crossover theorem explain which part of the separation survives.

The theorem concerns an optimal asymptotic communication rate. Its finite computations check stated examples and analytical identities; they do not optimize over all codes or replace the written converse.
