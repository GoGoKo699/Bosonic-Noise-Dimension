# Capacity from the resolved noise entropy

The quantum information retained by a random displacement channel depends on how many displacement alternatives become distinguishable at the available input energy. This page states that relation and proves its achievable side. The [converse](03-converse.md) treats unrestricted encoders and collective decoding.

We use the [model and conventions](01-model.md): one oscillator, independent unobserved displacements with a fixed Borel law $`\mu`$ on $`\mathbb C`$, and a finite second moment

```math
M=\int_{\mathbb C}|z|^2\,\mu(dz)\lt \infty.
```

The mean input photon number per channel use is at most $`E`$. The quantities $`Q_\mu(E)`$ and $`Q_{2,\mu}(E)`$ are the ordinary and adaptive two-way assisted quantum capacities, in qubits per use. No record of the sampled displacement is supplied to the receiver.

For $`Z\sim\mu`$ and $`t\gt 0`$, define the square-grid entropy

```math
H_t(\mu)
=H\!\left(\lfloor t\,\mathrm{Re}Z\rfloor,
          \lfloor t\,\mathrm{Im}Z\rfloor\right).
```

All logarithms and entropies are in bits. Finite second moment makes this discrete entropy finite at every fixed $`t`$: the quantized vector has finite second moment, and comparison with a discrete Gaussian bounds its entropy. The single-mode thermal entropy is

```math
g(x)=(x+1)\log_2(x+1)-x\log_2x,\qquad g(0)=0.
```

## The finite-resolution capacity law

**Theorem 1.** There is a universal finite constant $`C_0`$, and for every finite $`M`$ a finite constant $`C_M`$, such that every law with second moment at most $`M`$ and every $`E\ge1`$ obey

```math
A_\mu(E)-C_0
\le Q_\mu(E)
\le Q_{2,\mu}(E)
\le A_\mu(E)+C_M.
```

where

```math
A_\mu(E)=\log_2(E+1)-H_{\sqrt{E+1}}(\mu).
```

The lower bound can be replaced by its maximum with zero. One valid choice is $`C_0=2g(2)`$. The proof of the upper bound gives an explicit $`C_M`$ in [the converse](03-converse.md#collecting-the-finite-resolution-upper-bound); the constants are not optimized.

The theorem is uniform over the stated second-moment class. It does not require a density, a regular support, an information dimension, or a decomposition into independent quadrature noises. It also does not require a single-letter formula for quantum capacity.

The relevant displacement resolution is $`(E+1)^{-1/2}`$. The number $`\log_2(E+1)`$ is the leading entropy available to an energy-constrained oscillator, while $`H_{\sqrt{E+1}}(\mu)`$ measures the noise uncertainty at that resolution. The errors are bounded independently of $`E`$.

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
\lfloor \mathrm{Re}Z/\Delta\rfloor,
\lfloor \mathrm{Im}Z/\Delta\rfloor
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
$`\log_2t/\log_2E\to1/2`$. The constant remainders vanish. Both equalities also hold for the two-way assisted capacity. This passage does not interchange a variable noise law with a fixed-law asymptotic limit.

### Consequences

**A fixed-radius kick.** For $`Z=r e^{i\Theta}`$ with fixed $`r\gt 0`$ and uniform angle, grid entropy is
$`H_t(\mu)=\log_2t+O_r(1)`$. Therefore

```math
Q_\mu(E)=\frac12\log_2E+O_r(1).
```

Although its covariance is isotropic and nonzero in both quadratures, its noise measure has dimension one. The two-way assisted capacity satisfies the same estimate. The [circular-noise analysis](04-circular-noise.md) gives the model-specific argument and a finite-energy coherent-information witness.

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
\sup_{E\lt\infty}Q_\mu(E)\lt\infty\quad\Longleftrightarrow\quad\sup_{E\lt\infty}Q_{2,\mu}(E)\lt\infty
\quad\Longleftrightarrow\quad
D(\mu\Vert\gamma)\lt \infty.
}
```

If the relative entropy is finite, it is an upper bound on the unrestricted capacity. If it is infinite, the thermal-input lower bound already becomes arbitrarily large along a sequence of energies.

Every singular component therefore forces unbounded capacity. An absolutely continuous law can also have unbounded capacity when its differential entropy is $`-\infty`$, even though its information dimension is two and its logarithmic coefficient is zero. Conversely, a regular full-dimensional density with finite differential entropy has bounded capacity. None of these statements gives the exact bounded value.

## A full-dimensional noise density with unbounded capacity

The constant remainder distinguishes saturation from very slow growth even when the information dimension is two. Here is a bounded-support density exhibiting this distinction.

Take an integer $`J\ge0`$ with tail law

```math
\Pr(J\gt k)=\frac{c}{(k+2)\ln(k+2)},\qquad
k=0,1,\ldots,\qquad 0\lt c\le 2\ln 2.
```

Conditional on $`J=j`$, draw $`Z`$ uniformly from the square $`[0,2^{-j})^2`$ in displacement space. The resulting mixture is absolutely continuous and supported in the unit square. The mass at $`j\ge2`$ is $`O(1/(j^2\ln j))`$, so $`H(J)\lt\infty`$.

Let $`B_m`$ be the quantized displacement index at dyadic resolution $`t=2^m`$. For fixed $`j\le m`$ the grid exactly partitions the conditional square into $`2^{2(m-j)}`$ equally likely cells. When $`j\gt m`$ everything lies in one cell. Therefore,

```math
2m-H(B_m)=2\mathbb E\min(J,m)-I(J:B_m).
```

The mutual information is at most $`H(J)`$. Summing the tail and comparing with the integral of $`1/(x\ln x)`$ gives $`\mathbb E\min(J,m)=c\ln\ln m+O(1)`$. Thus the entropy divided by $`m`$ tends to two. The same limit holds between dyadic grid scales because the entropy difference between grids within a factor of two is bounded by a constant.

At energies $`E_m=2^{2m}-1`$, the capacity law now yields

```math
\begin{aligned}
Q_\mu(E_m)&=2c\ln\ln m+O(1),\\
Q_{2,\mu}(E_m)&=2c\ln\ln m+O(1).
\end{aligned}
```

Both capacities are nondecreasing in the allowed energy. Interpolate between successive $`E_m`$ to obtain growth $`2c\ln\ln\ln E+O(1)`$ for each capacity as $`E\to\infty`$. The logarithms in this explicit rate are natural, as in the definition of the tail. The rate itself is in qubits per use because the deficit above is measured in bits.

## Scope of the capacity law

The finite-resolution theorem uses a thermal-input achievable rate and a converse for adaptive local operations and two-way classical communication. The two rates lie in the same constant-width interval. Exact single-use optimality, efficient capacity-achieving codes, finite-block errors and the exact fixed-noise Gaussian capacity remain open here.

The theorem applies to a fixed known law with independent kicks. The [broadening analysis](05-broadening.md) gives a joint formula for energy and added Gaussian noise, uniform in the variance of that added noise up to one. At each fixed positive broadening the unrestricted capacity is finite.
