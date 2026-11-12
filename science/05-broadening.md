# Gaussian broadening and the finite-energy window

[Overview](../README.md) · [Circular noise](04-circular-noise.md) · [Verification](../verification/README.md)

The exact circular law has a half-logarithmic capacity growth. Any fixed Gaussian background smooths that law and gives a finite unconstrained capacity bound. Both statements can hold together with a positive finite-energy communication rate: a small nonzero background leaves a useful energy window before saturation.

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

Denote the resulting channel by $`\mathcal C_{r,\sigma}`$ and its unassisted mean-energy capacity by $`Q_{r,\sigma}(E)`$. Since phases from Weyl composition disappear under conjugation,

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

This is a sufficient achievable-rate bound. It is not an exact coherent-information formula for broadened noise, because the charge-twirling entropy inequality can be strict. The supremum permits using less than the available energy; sending more photons need not improve this particular lower-bound expression.

### A nonzero-jitter example

Take $`r=2`$, $`E=E_0=100`$, and $`\sigma=0.01`$, so $`v=10^{-4}`$. Evaluating the terms in (B9) gives:

| Quantity | Value in bits, except the variance |
|---|---:|
| Thermal entropy $`g(100)`$ | 8.0937407805 |
| Gaussian entropy exchange $`S_G`$ | 0.1612213484 |
| Charge variance $`V_J`$ | 804.02090001 |
| Integer entropy upper bound | 6.8727149427 |
| Achievable-rate lower bound | **1.0598044894 qubits/use** |

Thus the analytic bound certifies a rate greater than $`1.05`$ qubits per use at these parameters. This is a capacity achievability statement under unrestricted coding, not an implementation benchmark.

The Gaussian displacement law with the same covariance has mean squared amplitude $`r^2+v=4.0001`$. It is entanglement breaking and has zero quantum capacity. The distinction therefore persists at finite input energy with nonzero Gaussian jitter; exact singular support is not required for this particular separation.

## Capacity saturation at fixed background noise

For every fixed $`\sigma\gt 0`$, the distribution in (B1) has a bounded smooth density and finite second moment. Write its density as $`p_{r,\sigma}`$; its differential entropy is finite. The [relative-entropy converse](03-converse.md) yields

**(B10)**

```math
Q_{r,\sigma}(E)
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

Choosing $`w=\max\{1,r^2+\sigma^2\}`$ is convenient but not required. The capacity is nondecreasing in $`E`$ and bounded above by (B10), so it has a finite large-energy limit. The limit's exact value is not determined here.

In particular,

**(B12)**

```math
\lim_{E\to\infty}\frac{Q_{r,\sigma}(E)}{\log_2E}=0
\qquad(\sigma\gt 0\text{ fixed}).
```

## The joint energy–broadening crossover

Fix $`r\gt 0`$. Uniformly for $`E\ge2`$ and

**(B13)**

```math
0\lt \sigma\le\min\{1/2,r/2\},\qquad
E_*:=\min\{E,\sigma^{-2}\},
```

the bounds above imply

**(B14)**

```math
\boxed{
\frac12\log_2E_*-c_r
\le Q_{r,\sigma}(E)
\le\frac12\log_2E_*
+4\log_2\log_2(E_*+2)+C_r.
}
```

The constants depend on $`r`$ but can be chosen uniformly on every compact interval $`[r_-,r_+]\subset(0,\infty)`$. No uniform statement as $`r\to0`$ is implied.

**Lower bound.** Use thermal energy $`E_0=E_*`$ in (B9). Then $`E_0v\le1`$ and $`v\le1/4`$, so both symplectic eigenvalues in (B3), and hence $`S_G(E_0,v)`$, are bounded by constants independent of $`E`$ and $`\sigma`$. Also $`V_J(E_0,r,v)\le C'_r(E_0+1)`$. Since $`g(E_0)\ge\log_2(E_0+1)`$, (B9) gives $`Q_{r,\sigma}(E)\ge\tfrac12\log_2E_*-c_r`$.

**Upper bound before saturation.** If $`E\le\sigma^{-2}`$, (B2) and data processing give $`Q_{r,\sigma}(E)\le Q_r(E)`$. Equation (C5), with the explicit logarithmic remainder from the main theorem, gives the upper bound in (B14) with $`E_*=E`$.

**Upper bound after saturation.** If $`E\ge\sigma^{-2}`$, it remains to control (B11) independently of $`E`$. The broadened ring density at $`z`$ with $`\rho=|z|`$ is

**(B15)**

```math
p_{r,\sigma}(z)
=\frac{e^{-(\rho-r)^2/\sigma^2}}{2\pi^2\sigma^2}
\int_{-\pi}^{\pi}
\exp\!\left[-\frac{2\rho r(1-\cos\theta)}{\sigma^2}\right]d\theta.
```

For $`\rho\ge r/2`$, use $`1-\cos\theta\ge2\theta^2/\pi^2`$ and extend the Gaussian integral to the real line. This gives

**(B16)**

```math
p_{r,\sigma}(z)
\le\frac1{4\sqrt\pi\,\sigma\sqrt{\rho r}}
\le\frac{\sqrt2}{4\sqrt\pi\,r\sigma}
\le\frac1{r\sigma}.
```

For $`\rho\lt r/2`$, the Gaussian density itself gives

**(B17)**

```math
p_{r,\sigma}(z)
\le\frac1{\pi\sigma^2}e^{-r^2/(4\sigma^2)}
\le\frac1{r\sigma},
```

where the last inequality follows by setting $`x=r/\sigma\ge2`$ and using $`x e^{-x^2/4}/\pi\le1`$. Thus $`h(p_{r,\sigma})\ge\log_2(r\sigma)`$. Inserting this into (B11) gives

**(B18)**

```math
Q_{r,\sigma}(E)\le\log_2(1/\sigma)+C''_r
=\frac12\log_2E_*+C''_r.
```

This is stronger than the displayed upper bound in the saturated regime and completes (B14). The proof does not allow a remainder growing with the unused energy $`E`$ once $`E_* =\sigma^{-2}`$.

## Orders of limits and scope

For each fixed $`r\gt 0`$, the following distinctions are essential:

| Limit or regime | Established consequence |
|---|---|
| Exactly $`\sigma=0`$, then $`E\to\infty`$ | Capacity coefficient $`1/2`$ in front of $`\log_2E`$. |
| Fixed $`\sigma\gt 0`$, then $`E\to\infty`$ | A finite capacity ceiling; coefficient zero. |
| $`E\to\infty`$ and $`\sigma\to0`$ jointly | The effective energy is $`\min\{E,\sigma^{-2}\}`$ as in (B14). |
| Fixed finite $`E`$ and $`\sigma\to0`$ | The channel approaches the circular channel in energy-constrained diamond norm, and its unassisted capacity converges by the cited [continuity theorem](../references/README.md#winter). |

For example, if $`\sigma(E)=E^{-\alpha}`$ with fixed $`\alpha\gt 0`$, then (B14) gives

**(B19)**

```math
\lim_{E\to\infty}
\frac{Q_{r,\sigma(E)}(E)}{\log_2E}
=\min\{1/2,\alpha\}.
```

All these statements concern a known iid displacement channel and an input-photon constraint. They do not price preparation of the noise law or the computational cost of an encoder, include photon loss, or apply to one fixed unknown kick reused across transmissions. The finite-jitter lower bound addresses one explicit perturbation family; it is not robustness against arbitrary additional noise.
