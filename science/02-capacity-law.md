# Capacity from the resolved noise entropy

The quantum information retained by a random displacement channel depends on how many displacement alternatives become distinguishable at the available input energy. This page states that relation and proves its achievable side. The [converse](03-converse.md) treats unrestricted encoders and collective decoding.

We use the [model and conventions](01-model.md): one oscillator, independent unobserved displacements with a fixed Borel law $`\mu`$ on $`\mathbb C`$, and a finite second moment

```math
M=\int_{\mathbb C}|z|^2\,\mu(dz)\lt \infty.
```

The mean input photon number per channel use is at most $`E`$. The quantity $`Q_\mu(E)`$ is the ordinary unassisted quantum capacity, in qubits per use. No record of the sampled displacement is supplied to the receiver.

For $`Z\sim\mu`$ and $`t\gt 0`$, define the square-grid entropy

```math
H_t(\mu)
=H\!\left(\lfloor t\,\operatorname{Re}Z\rfloor,
          \lfloor t\,\operatorname{Im}Z\rfloor\right).
```

All logarithms and entropies are in bits. Finite second moment makes this discrete entropy finite at every fixed $`t`$: the quantized vector has finite second moment, and comparison with a discrete Gaussian bounds its entropy. The single-mode thermal entropy is

```math
g(x)=(x+1)\log_2(x+1)-x\log_2x,\qquad g(0)=0.
```

## The finite-resolution capacity law

**Theorem 1.** There is a universal finite constant $`C_0`$, and for every finite $`M`$ a finite constant $`C_M`$, such that every law with second moment at most $`M`$ and every $`E\ge1`$ obey

```math
\begin{aligned}
A_\mu(E)-C_0
&\le Q_\mu(E)\\
&\le A_\mu(E)
   +4\log_2\log_2(E+2)+C_M,
\end{aligned}
```

where

```math
A_\mu(E)=\log_2(E+1)-H_{\sqrt{E+1}}(\mu).
```

The lower bound can be replaced by its maximum with zero. One valid choice is $`C_0=2g(2)`$. The proof of the upper bound gives an explicit $`C_M`$ in [the converse](03-converse.md#collecting-the-finite-resolution-upper-bound); the constants are not optimized.

The theorem is uniform over the stated second-moment class. It does not require a density, a regular support, an information dimension, or a decomposition into independent quadrature noises. It also does not require a single-letter formula for quantum capacity.

The relevant displacement resolution is $`(E+1)^{-1/2}`$. The number $`\log_2(E+1)`$ is the leading entropy available to an energy-constrained oscillator, while $`H_{\sqrt{E+1}}(\mu)`$ measures the noise uncertainty at that resolution. The remainder is sublogarithmic in $`E`$.

## Why one thermal input suffices for the lower bound

Let

```math
\tau_E=\sum_{n=0}^{\infty}
\frac{E^n}{(E+1)^{n+1}}|n\rangle\langle n|
```

be the thermal state with mean photon number $`E`$, and purify it as

```math
|\phi_E\rangle_{RA}
=\sum_{n=0}^{\infty}
\sqrt{\frac{E^n}{(E+1)^{n+1}}}\,
|n\rangle_R|n\rangle_A.
```

The energy-constrained coherent-information coding theorem gives

```math
Q_\mu(E)\ge
I_{\mathrm c}(\tau_E,\mathcal N_\mu)
=S(\mathcal N_\mu(\tau_E))-S(\omega_E^\mu),
```

with

```math
\omega_E^\mu
=\int
(I_R\otimes D(z))|\phi_E\rangle\langle\phi_E|
(I_R\otimes D(z)^\dagger)\,\mu(dz).
```

This is the usual achievable-rate statement, with arbitrary block coding allowed; it does not assert that a product input and separate decoding are capacity optimal. The relevant mean-energy coding framework is given by [Wilde–Qi 2018](../references/README.md#wilde-qi).

The output entropy satisfies

```math
S(\mathcal N_\mu(\tau_E))
\ge\int S(D(z)\tau_ED(z)^\dagger)\,\mu(dz)
=g(E).
```

Here entropy concavity is legitimate: the random-unitary output has finite mean energy and hence finite entropy. The joint reference-output state also has finite entropy.

It remains to control the entropy exchange $`S(\omega_E^\mu)`$ without assigning a differential entropy to a possibly singular noise law.

### Resolve the displacement only to the energy scale

Set

```math
\Delta=(E+1)^{-1/2},\qquad
B=\left(
\lfloor \operatorname{Re}Z/\Delta\rfloor,
\lfloor \operatorname{Im}Z/\Delta\rfloor
\right).
```

Let $`p_b=\Pr(B=b)`$, let $`c_b=\Delta(b_1+ib_2)`$ be the lower-left corner of cell $`b`$, and let $`\omega_{E,b}`$ be the normalized joint state conditional on that cell. The countable-mixture entropy inequality yields

```math
S(\omega_E^\mu)
\le H(B)+\sum_b p_b S(\omega_{E,b}).
```

There is no need to discretize the channel itself. Only the proof groups the original continuous ensemble into cells.

Let $`S_E`$ denote a two-mode squeezing unitary with
$`S_E|0,0\rangle=|\phi_E\rangle`$. On the conditional state, apply the fixed unitary

```math
S_E^\dagger(I_R\otimes D(-c_b)).
```

For every displacement $`z`$ in cell $`b`$, put $`w=z-c_b`$. Up to a global phase and the immaterial sign convention of the squeezing operation, the transformed pure state is a product of coherent states with amplitudes
$`-\sqrt E\,\overline w`$ and $`\sqrt{E+1}\,w`$. Its total photon number is

```math
(2E+1)|w|^2
\le (2E+1)\,2\Delta^2
\le4.
```

The conditional mixture has the same total mean-energy bound. Entropy is invariant under the fixed unitary, and the maximum entropy of two oscillator modes with total mean photon number at most four is $`2g(2)`$. Thus

```math
S(\omega_{E,b})\le2g(2)
```

for every cell of nonzero probability. Consequently,

```math
S(\omega_E^\mu)
\le H_{\sqrt{E+1}}(\mu)+2g(2).
```

Combining the output-entropy and entropy-exchange estimates proves the stronger explicit lower bound

```math
\boxed{
Q_\mu(E)\ge
g(E)-H_{\sqrt{E+1}}(\mu)-2g(2).
}
```

Since $`g(E)\ge\log_2(E+1)`$, this implies the lower half of Theorem 1.

This derivation uses the Weyl displacement law directly. Displacements in different directions generally do not commute as operators, and no diagonal dephasing representation is assumed.

## Information dimension fixes the leading energy dependence

Define the lower and upper information dimensions of the noise law by

```math
\underline d(\mu)
=\liminf_{t\to\infty}\frac{H_t(\mu)}{\log_2t},
\qquad
\overline d(\mu)
=\limsup_{t\to\infty}\frac{H_t(\mu)}{\log_2t}.
```

Under the finite-second-moment assumption these lie in $`[0,2]`$. For example, comparison with the probabilities of a two-dimensional Gaussian on the same grid gives
$`H_t(\mu)\le2\log_2t+O_M(1)`$ for $`t\ge1`$.

**Corollary 2.** For a fixed noise law,

```math
\begin{aligned}
\liminf_{E\to\infty}
\frac{Q_\mu(E)}{\log_2E}
&=1-\frac{\overline d(\mu)}2,\\
\limsup_{E\to\infty}
\frac{Q_\mu(E)}{\log_2E}
&=1-\frac{\underline d(\mu)}2.
\end{aligned}
```

In particular, if $`d(\mu)=\underline d(\mu)=\overline d(\mu)`$ exists, then

```math
\boxed{
\lim_{E\to\infty}
\frac{Q_\mu(E)}{\log_2E}
=1-\frac{d(\mu)}2.
}
```

To obtain this statement, substitute $`t=\sqrt{E+1}`$ in Theorem 1, divide by $`\log_2E`$, and use
$`\log_2t/\log_2E\to1/2`$. The constant and double-logarithmic remainders vanish. This passage does not interchange a variable noise law with a fixed-law asymptotic limit.

### Consequences

**A fixed-radius kick.** For $`Z=r e^{i\Theta}`$ with fixed $`r\gt 0`$ and uniform angle, grid entropy is
$`H_t(\mu)=\log_2t+O_r(1)`$. Therefore

```math
Q_\mu(E)=\frac12\log_2E+O_r(\log\log E).
```

Although its covariance is isotropic and nonzero in both quadratures, its noise measure has dimension one. The [circular-noise analysis](04-circular-noise.md) gives the model-specific argument and a finite-energy coherent-information witness.

**Finite random kick alphabets.** For a fixed finite set of distinct displacements, $`H_t(\mu)`$ equals the entropy of the finite alphabet once the grid is sufficiently fine. The capacity consequently has leading term $`\log_2E`$. This conclusion allows noncommuting displacement errors.

**A noiseless component mixed with smooth displacement noise.** If

```math
\mu=p\delta_0+(1-p)\nu
```

and $`\nu`$ is an absolutely continuous finite-second-moment law, then $`d(\mu)=2(1-p)`$ and the leading capacity coefficient is $`p`$. The dimension identity follows by introducing the binary component label: the entropy of the quantized mixture differs from the component-averaged entropy by at most the entropy of that label. No component label is supplied to the communicating parties.

The dimension-two assertion for $`\nu`$ does not require finite differential entropy. Restrict its density to a bounded region and a bounded density level so that the retained mass is $`a`$, arbitrarily close to one. The normalized retained density is bounded, so every grid-cell probability is at most $`C/t^2`$ and its grid entropy is at least $`2\log_2t-\log_2C`$. Concavity of the mixture entropy gives $`\liminf H_t(\nu)/\log_2t\ge2a`$. Let $`a`$ tend to one and combine with the finite-second-moment upper bound.

This last channel is not a flagged erasure channel. Its noisy branch still transmits physical oscillator degrees of freedom, and applying an erasure-channel no-cloning threshold would change the model.

## Boundedness requires more than a zero leading coefficient

The information-dimension law concerns the coefficient of $`\log E`$. It does not decide whether a zero-coefficient capacity stays bounded.

Let $`\gamma`$ denote the standard complex Gaussian measure with density

```math
g_1(z)=\pi^{-1}e^{-|z|^2}.
```

The [bounded-capacity criterion](03-converse.md#when-is-the-unconstrained-capacity-finite) proves

```math
\boxed{
\sup_{E\lt \infty}Q_\mu(E)\lt \infty
\quad\Longleftrightarrow\quad
D(\mu\|\gamma)\lt \infty.
}
```

If the relative entropy is finite, it is an upper bound on the unrestricted capacity. If it is infinite, the thermal-input lower bound already becomes arbitrarily large along a sequence of energies.

Every singular component therefore forces unbounded capacity. An absolutely continuous law can also have unbounded capacity when its differential entropy is $`-\infty`$, even though its information dimension is two and its logarithmic coefficient is zero. Conversely, a regular full-dimensional density with finite differential entropy has bounded capacity. None of these statements gives the exact bounded value.

## What is established and what is not

The finite-resolution theorem constrains the fully regularized unassisted capacity. Its lower bound is an achievable coherent-information rate, and its upper bound permits arbitrary encoders and collective decoding. The result does not identify a computationally efficient code, determine the exact finite-energy optimum, or solve the fixed-noise Gaussian quantum-capacity problem.

The fixed-law assumption matters. The [broadening analysis](05-broadening.md) separately treats a circular law with additional Gaussian noise and identifies the energy range over which the singular-law growth remains useful. At every fixed positive broadening, the unrestricted capacity is finite.
