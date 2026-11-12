# Model, resource and operational question

[Science route](README.md) · [Capacity law](02-capacity-law.md) · [Related work](06-related-work.md)

## Why noise geometry matters

A covariance matrix records the average size and directional spread of an oscillator's random kicks. It does not record how many distinguishable kick values remain at a finer resolution. A fixed-radius kick with a uniformly random angle and an isotropic Gaussian kick can have the same covariance while occupying very different subsets of phase space. This project asks how that distinction affects the ultimate rate of transmitting quantum information as the input energy increases.

The question concerns the full quantum capacity of the channel, allowing arbitrarily long collective codes. A rate computed for one thermal input is an achievable lower bound; a separate converse is required before identifying the capacity's asymptotic growth. Both parts are supplied in the [capacity law](02-capacity-law.md) and [converse](03-converse.md).

## One oscillator and a fixed noise law

Let $`a`$ be the annihilation operator, $`N=a^\dagger a`$ the photon-number observable, and

```math
D(z)=\exp(za^\dagger-\bar z a),\qquad z\in\mathbb C.
```

Write $`q=(a+a^\dagger)/\sqrt2`$ and $`p=(a-a^\dagger)/(i\sqrt2)`$, so $`[q,p]=i`$ and the vacuum quadrature covariance is $`I_2/2`$. The displacement changes the quadrature means by $`(\sqrt2\mathrm{Re}z,\sqrt2\mathrm{Im}z)`$. Every energy and Gaussian variance in this account uses this convention.

Fix a known Borel probability measure $`\mu`$ on $`\mathbb C`$ with

```math
M=\int_{\mathbb C}|z|^2\,\mu(dz)\lt\infty.
```

The random-displacement channel is

```math
\mathcal N_\mu(\rho)
=\int_{\mathbb C}D(z)\rho D(z)^\dagger\,\mu(dz).
```

The integral defines a normal quantum channel on trace-class states. The law may be discrete, continuous, singular continuous, or a mixture of these. Different channel uses have independent fresh draws from the same law. The actual draw is not supplied to the sender or receiver, and no classical flag identifying it is part of the output. The law itself is known and can be used in code design.

The Weyl operators need not commute. Their projective phases cancel in conjugation, giving displacement covariance and the convolution identity

```math
\mathcal N_\mu\circ\mathcal N_\nu
=\mathcal N_{\mu*\nu}
=\mathcal N_\nu\circ\mathcal N_\mu.
```

Commutativity of these random-unitary channels under composition does not turn their individual errors into commuting dephasing operators. In particular, no degrading map or single-letter capacity formula is assumed.

## What the capacity counts

For fixed $`E\ge0`$, a block code uses $`\mathcal N_\mu^{\otimes n}`$ to transmit one half of a maximally entangled state of Schmidt rank $`K_n`$. The encoder and decoder are arbitrary local quantum operations; the entanglement fidelity tends to one as $`n\to\infty`$. If $`\rho_{A^n}`$ is the encoded maximally mixed logical input, the constraint is

```math
\mathrm{Tr}\!\left[\rho_{A^n}\sum_{j=1}^{n}N_j\right]\le nE.
```

This is an unconditional average input-photon constraint. It is not a hard Fock-space cutoff, a maximum energy per codeword, or a promise that every mode has energy at most $`E`$. Uneven allocation across modes is allowed. The capacity $`Q_\mu(E)`$ is the supremum of achievable rates $`\liminf_n n^{-1}\log_2 K_n`$, in qubits per channel use.

There is no free preshared entanglement or communication side channel in this definition. Auxiliary systems used locally by the code do not provide a channel between sender and receiver. The results account for input photons and channel uses; they do not bound the computation, precision, ancilla energy or laboratory complexity of implementing an optimal code.

For this oscillator Hamiltonian the Gibbs condition holds. The finite noise moment also gives, for any input with mean energy at most $`E`$,

```math
\mathrm{Tr}[N\mathcal N_\mu(\rho)]
\le E+2\sqrt{EM}+M
\le2E+2M.
```

Thus output entropy is finite at every finite input-energy bound. These conditions allow application of the [Wilde–Qi energy-constrained coding theorem](../references/README.md#wilde-qi): capacity equals the regularized energy-constrained coherent information, and the coherent information of any admissible input gives an achievable rate. For centered noise the exact energy increase is $`M`$.

The code blocklength tends to infinity at fixed $`E`$ and fixed $`\mu`$. The high-energy statements then take $`E\to\infty`$ while holding the noise law fixed. The [small-broadening crossover](05-broadening.md) explicitly specifies its different two-parameter limit.

## Entropies and phase-space resolution

All logarithms, Shannon entropies, von Neumann entropies and relative entropies are in bits. Let

```math
g(x)=(x+1)\log_2(x+1)-x\log_2x,\qquad g(0)=0.
```

This is the entropy of a one-mode thermal state of mean photon number $`x`$. The noiseless constrained quantum capacity is $`g(E)`$; its leading high-energy growth is $`\log_2 E`$.

For $`Z\sim\mu`$, define the square-bin entropy

```math
H_t(\mu)
=H\!\left(\lfloor t\mathrm{Re}Z\rfloor,
           \lfloor t\mathrm{Im}Z\rfloor\right),\qquad t\gt0.
```

Finite second moment makes this discrete entropy finite. The bin side length is $`1/t`$. Changes of grid origin or fixed scale change the entropy by at most a bounded amount at comparable resolutions; the theorem nevertheless uses the displayed grid exactly. The physically relevant resolution is

```math
t_E=\sqrt{E+1}.
```

The upper and lower information dimensions are

```math
\overline d(\mu)=\limsup_{t\to\infty}\frac{H_t(\mu)}{\log_2t},
\qquad
\underline d(\mu)=\liminf_{t\to\infty}\frac{H_t(\mu)}{\log_2t}.
```

They lie in $`[0,2]`$. When they coincide, their common value $`d(\mu)`$ is the [Rényi information dimension](../references/README.md#renyi). It measures the growth in noise information resolved by finer bins. It is not the rank of the covariance matrix, the dimension of the affine span, or merely the dimension of the support.

The standard complex Gaussian used throughout is

```math
g_1(z)=\pi^{-1}e^{-|z|^2},\qquad \mathbb E|G|^2=1.
```

A Gaussian displacement $`\sigma G`$ has complex variance $`\sigma^2`$ and adds $`\sigma^2I_2`$ to the quadrature covariance. Classical relative entropy $`D(\mu\Vert g_1)`$ is infinite if $`\mu`$ is not absolutely continuous with respect to this Gaussian measure. When it has density $`f`$ and finite differential entropy, it equals

```math
D(f\Vert g_1)=-h(f)+\log_2\pi+M\log_2 e.
```

## Boundaries of the physical comparison

The channel contains additive displacement noise only. Photon loss, damping, a finite-resolution side channel identifying the kick, correlated uses and an energy-dependent noise law define different problems. A known deterministic displacement can be inverted by the decoder and costs no communication rate in this resource model.

The [circle example](04-circular-noise.md) compares laws with the same mean and covariance under these conventions. Its conclusion concerns ultimate unassisted communication rates, not a prescribed family of Gaussian codes. The [broadened circle](05-broadening.md) gives an explicit positive finite-energy rate while also showing why fixed nonzero broadening changes the infinite-energy limit.
