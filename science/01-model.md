# Model, resource and operational question

[Science route](README.md) · [Capacity law](02-capacity-law.md) · [Related work](06-related-work.md)

## Why noise geometry matters

A covariance matrix records the average size and directional spread of an oscillator's random kicks. It does not record how many distinguishable kick values remain at a finer resolution. A fixed-radius kick with a uniformly random angle and an isotropic Gaussian kick can have the same covariance while occupying very different subsets of phase space. This project asks how that distinction affects the ultimate rate of transmitting quantum information as the input energy increases.

The [capacity law](02-capacity-law.md) describes two communication settings. In the first, the parties use a block code. In the second, they may adapt each use to their quantum memories and public classical messages. A thermal input supplies the achievable rate, and the [converse](03-converse.md) bounds even the adaptive setting at the same resolution.

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

### Unassisted quantum capacity

For fixed $`E\ge0`$, a block code uses $`\mathcal N_\mu^{\otimes n}`$ to transmit one half of a maximally entangled state of Schmidt rank $`K_n`$. The encoder and decoder are arbitrary local quantum operations; the entanglement fidelity tends to one as $`n\to\infty`$. If $`\rho_{A^n}`$ is the encoded maximally mixed logical input, the constraint is

```math
\mathrm{Tr}\!\left[\rho_{A^n}\sum_{j=1}^{n}N_j\right]\le nE.
```

This unconditional average treats the whole block as one budget and allows uneven allocation across input modes. The capacity $`Q_\mu(E)`$ is the supremum of achievable rates $`\liminf_n n^{-1}\log_2 K_n`$, in qubits per channel use. The parties start with local auxiliary systems and transmit through the displacement channel alone.

### Quantum capacity with two-way classical communication

In the assisted setting, Alice and Bob start with a separable state across their laboratories. They may use arbitrary local quantum operations, quantum memories and public classical messages in both directions before, between and after the $`n`$ channel uses. Each use transmits one oscillator from Alice to Bob. The protocol generates a state with fidelity tending to one to a shared maximally entangled state of Schmidt rank $`K_n`$. The same rate applies to quantum transmission with this classical assistance. Quantum transmission can distribute entanglement, and shared entanglement can transmit a state by teleportation.

If $`\rho_{A_j}`$ is the marginal of the actual oscillator entering use $`j`$, averaged over all prior outcomes, write $`e_j=\mathrm{Tr}(N\rho_{A_j})`$. The energy budget is

```math
\sum_{j=1}^n e_j\le nE.
```

The protocol may choose its inputs using the available classical messages and may allocate energy unevenly over uses and outcomes. This is an expectation constraint on the actual transmitted modes. Local memory energies and the amount of classical communication are unrestricted. The two-way-assisted capacity $`Q_{2,\mu}(E)`$ is the supremum of achievable rates $`\liminf_n n^{-1}\log_2 K_n`$ in this setting. An unassisted code is an allowed assisted protocol, so $`Q_\mu(E)\le Q_{2,\mu}(E)`$.

### Energy and the order of limits

For this oscillator Hamiltonian the Gibbs condition holds. The finite noise moment also gives, for any input with mean energy at most $`E`$,

```math
\mathrm{Tr}[N\mathcal N_\mu(\rho)]
\le E+2\sqrt{EM}+M
\le2E+2M.
```

Thus each output oscillator has finite entropy under a finite input-energy bound. These conditions allow application of the [Wilde–Qi energy-constrained coding theorem](../references/README.md#wilde-qi) to the unassisted capacity. It equals the regularized energy-constrained coherent information, and the coherent information of any admissible input gives an achievable rate. For centered noise the exact increase in mean photon number is $`M`$.

For both capacities, the number of channel uses tends to infinity at fixed $`E`$ and fixed $`\mu`$. The high-energy statements then take $`E\to\infty`$ while holding the noise law fixed. The [small-broadening crossover](05-broadening.md) explicitly specifies its different two-parameter limit.

## Entropies and phase-space resolution

All logarithms, Shannon entropies, von Neumann entropies and relative entropies are in bits. Let

```math
g(x)=(x+1)\log_2(x+1)-x\log_2x,\qquad g(0)=0.
```

This is the entropy of a one-mode thermal state of mean photon number $`x`$. The noiseless constrained quantum capacity is $`g(E)`$, with leading high-energy growth $`\log_2 E`$.

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

The [circle example](04-circular-noise.md) compares laws with the same mean and covariance under these conventions. Its separation holds for the unrestricted unassisted and assisted rates. The [Gaussian-broadening page](05-broadening.md) gives an explicit positive rate at finite energy for a broadened circle and locates the crossover in energy for general displacement laws.
