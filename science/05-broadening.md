# Gaussian broadening and the finite-energy window

[Overview](../README.md) · [Circular noise](04-circular-noise.md) · [Verification](../verification/README.md)

An independent Gaussian background coarsens the phase-space resolution in the capacity law. For a circular displacement, the same background eventually caps the half-logarithmic growth with energy. The finite-energy example below certifies a positive unassisted rate in this window.

## Independently broadened circular kicks

Use the displacement convention of the [model](01-model.md), and define

**(B1)**

```math
Z=r e^{i\Theta}+\sigma G,\qquad
\Theta\sim\mathrm{Unif}[0,2\pi),\qquad
p_G(z)=\pi^{-1}e^{-|z|^2},\qquad
v=\sigma^2.
```

The angle and $`G`$ are independent, and both are independently resampled at every channel use. Thus $`\mathbb E|\sigma G|^2=v`$, and the total added quadrature covariance is $`(r^2+v)I_2`$. The symbol $`\sigma`$ is a complex-amplitude scale; each real component of $`\sigma G`$ has variance $`\sigma^2/2`$.

Denote the resulting channel by $`\mathcal C_{r,\sigma}`$. Its unassisted and two-way-assisted mean-energy capacities are $`Q_{r,\sigma}(E)`$ and $`Q_{2,r,\sigma}(E)`$. The convolution identity for Weyl conjugations gives

**(B2)**

```math
\mathcal C_{r,\sigma}
=\mathcal N_{\sigma G}\circ\mathcal C_r
=\mathcal C_r\circ\mathcal N_{\sigma G}.
```

## A quantitative finite-energy lower bound

Choose a thermal input of mean photon number $`E_0\le E`$, with purification $`|\psi_{E_0}\rangle`$ as in (C8).

First apply only the Gaussian displacement. The resulting two-mode Gaussian state has symplectic eigenvalues

**(B3)**

```math
\nu_\pm(E_0,v)
=\frac{\sqrt{1+(4E_0+2)v+v^2}\pm v}{2}.
```

They follow from the covariance blocks

**(B4)**

```math
A=(E_0+1/2)I_2,\qquad
B=(E_0+1/2+v)I_2,\qquad
C=\sqrt{E_0(E_0+1)}\mathrm{diag}(1,-1),
```

in the convention $`[q,p]=i`$. Its entropy is

**(B5)**

```math
S_G(E_0,v)
=g(\nu_+(E_0,v)-1/2)+g(\nu_-(E_0,v)-1/2).
```

The Gaussian state is invariant under $`e^{i\theta(N_B-N_R)}`$. Apply a fixed displacement $`D(r)`$ to its second mode and then average over this rotation. This is exactly the noisy-circle output on the purification, because the Gaussian displacement law is isotropic.

For any state $`\rho`$ and integer-charge projectors $`\{P_k\}`$, let $`p_k=\mathrm{Tr}(P_k\rho)`$. Charge dephasing obeys

**(B6)**

```math
S\!\left(\sum_kP_k\rho P_k\right)\le S(\rho)+H(p).
```

One proof coherently records the charge in an auxiliary register. The recording is an isometry, and the register's entropy is $`H(p)`$; the entropy triangle inequality then gives (B6). Countably many sectors follow by finite grouping and the finite entropy bounds used below. No rank-one claim is made for these mixed-state charge sectors.

For a fixed complete displacement $`z`$, the charge $`J=N_B-N_R`$ has the Skellam distribution derived on the [circular-noise page](04-circular-noise.md). Its conditional moments are

**(B7)**

```math
\mathbb E[J\mid Z=z]=|z|^2,\qquad
\mathrm{Var}(J\mid Z=z)=(2E_0+1)|z|^2.
```

Under (B1), $`\mathbb E|Z|^2=r^2+v`$ and $`\mathrm{Var}(|Z|^2)=v^2+2r^2v`$. The law of total variance gives

**(B8)**

```math
V_J(E_0,r,v)
=(2E_0+1)(r^2+v)+v^2+2r^2v.
```

Combining (B5), (B6), and the integer entropy bound (C17) controls the entropy exchange. Meanwhile, the receiver output is a random-displacement mixture of the same thermal input, so its entropy is at least $`g(E_0)`$. Therefore

**(B9)**

```math
\boxed{
Q_{r,\sigma}(E)\ge
\sup_{0\le E_0\le E}
\left[
g(E_0)-S_G(E_0,\sigma^2)
-\frac12\log_2\!\left(2\pi\mathrm e
\left[V_J(E_0,r,\sigma^2)+\frac1{12}\right]\right)
\right]_+ .
}
```

The charge-twirling inequality can be strict, so (B9) certifies an achievable rate. The supremum lets the encoder choose the thermal energy that gives the strongest bound.

### A nonzero-jitter example

Take $`r=2`$, $`E=E_0=100`$, and $`\sigma=0.01`$, so $`v=10^{-4}`$. Evaluating the terms in (B9) gives:

| Quantity | Value in bits, except the variance |
|---|---:|
| Thermal entropy $`g(100)`$ | 8.0937407805 |
| Gaussian entropy exchange $`S_G`$ | 0.1612213484 |
| Charge variance $`V_J`$ | 804.02090001 |
| Integer entropy upper bound | 6.8727149427 |
| Achievable-rate lower bound | **1.0598044894 qubits/use** |

Thus the analytic bound certifies a rate greater than $`1.05`$ qubits per use at these parameters. The bound uses the unconstrained choice of coding operations in the model.

The Gaussian displacement law with the same covariance has mean squared amplitude $`r^2+v=4.0001`$. It is entanglement breaking and has zero capacity even with two-way classical communication. The distinction therefore persists at finite input energy with nonzero Gaussian jitter; exact singular support is not required for this particular separation.

## Capacity saturation at fixed background noise

For every fixed $`\sigma\gt 0`$, the distribution in (B1) has a bounded smooth density and finite second moment. Write its density as $`p_{r,\sigma}`$; its differential entropy is finite. The [relative-entropy converse](03-converse.md) yields

**(B10)**

```math
Q_{r,\sigma}(E)\le Q_{2,r,\sigma}(E)
\le D\!\left(p_{r,\sigma}\middle\|g_w\right)\lt \infty
\quad\text{for every }E,
\qquad w\ge1,
```

where $`g_w(z)=(\pi w)^{-1}e^{-|z|^2/w}`$ is the circular complex Gaussian density of mean squared amplitude $`w`$. Such a Gaussian additive-noise channel is entanglement breaking. The right side equals

**(B11)**

```math
\log_2(\pi w)
+\frac{r^2+\sigma^2}{w\ln2}
-h(p_{r,\sigma}).
```

Choosing $`w=\max\{1,r^2+\sigma^2\}`$ is convenient but not required. Both capacities are nondecreasing in $`E`$ and bounded above by (B10), so each has a finite large-energy limit. The bound leaves their exact limits open.

In particular,

**(B12)**

```math
\lim_{E\to\infty}\frac{Q_{r,\sigma}(E)}{\log_2E}
=\lim_{E\to\infty}\frac{Q_{2,r,\sigma}(E)}{\log_2E}=0
\qquad(\sigma\gt 0\text{ fixed}).
```

## The general energy–broadening crossover

Let $`Z\sim\mu`$ be any displacement with $`\mathbb E|Z|^2\le M`$. Write $`\mu_\sigma`$ for the law of $`Z+\sigma G`$, with independent standard complex Gaussian $`G`$ and $`0\le\sigma\le1`$. Define the effective bin side length by

**(B13)**

```math
\ell(E,\sigma)=\sqrt{\sigma^2+(E+1)^{-1}}.
```

For either of the two capacity definitions, use $`Q^\ast_{\mu_\sigma}(E)`$ to denote the corresponding rate. The estimate

```math
\boxed{
Q^\ast_{\mu_\sigma}(E)
=2\log_2(1/\ell(E,\sigma))-H_{1/\ell(E,\sigma)}(\mu)+O_M(1)
}
```

holds uniformly over $`E\ge1`$, $`0\le\sigma\le1`$ and every law with the stated second-moment bound. The two capacities may have different bounded errors. The expression resolves the original law $`\mu`$ at the coarser scale set jointly by the physical jitter and the available energy.

To prove it, set $`\delta=(E+1)^{-1/2}`$ and let $`G'`$ be a standard complex Gaussian independent of $`(Z,G)`$. The [smoothing lemma](03-converse.md#smoothing-entropy-and-quantization-entropy-differ-by-a-constant) applied to $`\mu_\sigma`$ gives

```math
h(Z+\sigma G+\delta G')
=2\log_2\delta+H_{1/\delta}(\mu_\sigma)+O(1).
```

The two Gaussian terms sum to a Gaussian of variance $`\ell(E,\sigma)^2`$. Applying the same lemma at that scale to the original law gives

```math
h(Z+\sigma G+\delta G')
=2\log_2\ell(E,\sigma)+H_{1/\ell(E,\sigma)}(\mu)+O(1).
```

The constants in the smoothing lemma are independent of the smoothing scale and the law. Since $`\mu_\sigma`$ has second moment at most $`M+1`$, applying the [capacity law](02-capacity-law.md#the-finite-resolution-capacity-law) to $`\mu_\sigma`$ proves the claimed estimate.

## The joint energy–broadening crossover

For circular noise at fixed radius $`r\gt0`$, the [arc-length bound](04-circular-noise.md) gives $`H_t(\mu_r)=\log_2t+O_r(1)`$ for $`t\ge1`$. For $`E\ge2`$ and $`0\lt\sigma\le\min\{1/2,r/2\}`$, the inverse squared bin side length in (B13) is within fixed factors of $`E_*=\min\{E,\sigma^{-2}\}`$. Hence either capacity obeys

**(B14)**

```math
Q^\ast_{r,\sigma}(E)=\frac12\log_2 E_*+O_r(1).
```

The two error bounds can be taken uniformly on every compact radius interval within $`(0,\infty)`$. Below the crossover, the bound grows as $`\tfrac12\log_2 E`$. Above it, the bound is within a radius-dependent constant of $`\log_2(1/\sigma)`$, independently of any further increase in energy. The quantitative witness (B9) supplies a direct lower bound at specified finite parameters.

## Orders of limits and scope

For each fixed $`r\gt 0`$, the following distinctions are essential:

| Limit or regime | Established consequence |
|---|---|
| Exactly $`\sigma=0`$, then $`E\to\infty`$ | Both capacity coefficients are $`1/2`$ in front of $`\log_2E`$. |
| Fixed $`\sigma\gt 0`$, then $`E\to\infty`$ | Both capacities are bounded, with logarithmic coefficient zero. |
| $`E\to\infty`$ and $`\sigma\to0`$ jointly | The circular effective energy is $`\min\{E,\sigma^{-2}\}`$ as in (B14). |
| Fixed finite $`E`$ and $`\sigma\to0`$ | The channel approaches the circular channel in energy-constrained diamond norm, and its unassisted capacity converges by the cited [continuity theorem](../references/README.md#winter). |

For example, if $`\sigma(E)=E^{-\alpha}`$ with fixed $`\alpha\gt 0`$, then (B14) gives

**(B15)**

```math
\lim_{E\to\infty}
\frac{Q^\ast_{r,\sigma(E)}(E)}{\log_2E}
=\min\{1/2,\alpha\}.
```

The estimates describe known iid displacement laws under the input-photon constraint. The finite-energy witness concerns the specified Gaussian perturbation. The costs of preparing the noise law or implementing the encoder lie outside the model.
