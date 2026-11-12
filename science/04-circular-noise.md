# Fixed-radius random displacements

[Overview](../README.md) · [Capacity law](02-capacity-law.md) · [Gaussian broadening](05-broadening.md)

A displacement of fixed magnitude and uniformly random direction perturbs both oscillator quadratures. Its covariance is isotropic, but its distribution is supported on a circle. This distinction has an operational consequence: its quantum capacity grows as one half of the logarithm of the available input energy, even when Gaussian noise with the same covariance is entanglement breaking.

## Model and conventions

Write

**(C1)**

```math
D(z)=\exp(za^\dagger-\overline z a),\qquad
Z=r e^{i\Theta},\qquad
\Theta\sim\mathrm{Unif}[0,2\pi),\qquad r\gt 0.
```

The channel independently samples a new angle on every use:

**(C2)**

```math
\mathcal C_r(\rho)
=\frac1{2\pi}\int_0^{2\pi}
D(r e^{i\theta})\rho D(r e^{i\theta})^\dagger\,d\theta.
```

The realized angle is unavailable to the sender and receiver. The capacity $`Q_r(E)`$ is the ordinary unassisted quantum capacity with unconditional mean input photon number at most $`E`$, averaged across uses, as in the [model](01-model.md). Encoding and decoding may be collective; no efficient encoder is asserted.

For $`q=(a+a^\dagger)/\sqrt2`$ and $`p=(a-a^\dagger)/(i\sqrt2)`$, the displacement changes the quadrature means by $`(\sqrt2\mathrm{Re}Z,\sqrt2\mathrm{Im}Z)`$. Consequently the added classical quadrature covariance is $`r^2 I_2`$, and the mean added photon number is $`r^2`$.

Although the angle is one real parameter, this is not photon-number dephasing. Displacements in different directions do not have a common eigenbasis; the degrading-map argument for commuting phase rotations does not apply.

## The circle's quantized entropy

Let $`\mu_r`$ be the law in (C1), and retain the main theorem's definition

**(C3)**

```math
H_t(\mu_r)
=H\!\left(\left\lfloor t\mathrm{Re}Z\right\rfloor,
           \left\lfloor t\mathrm{Im}Z\right\rfloor\right).
```

There are universal constants $`c_0,c_1`$ such that, for every $`t,r\gt 0`$,

**(C4)**

```math
\log_2(1+tr)-c_0
\le H_t(\mu_r)
\le \log_2(1+tr)+c_1.
```

In particular, at each fixed $`r\gt 0`$, $`H_t(\mu_r)=\log_2t+O_r(1)`$ as $`t\to\infty`$.

**Upper bound.** Rescale the circle to radius $`R=tr`$ and partition the plane into unit squares. Every square that intersects the circle lies inside the annulus

```math
(R-\sqrt2)_+\le |z|\le R+\sqrt2.
```

The squares have disjoint interiors and unit area. The annulus area is at most a universal constant times $`1+R`$, so at most $`C(1+R)`$ squares can have positive probability. Their entropy is at most $`\log_2[C(1+R)]`$.

**Lower bound.** For $`R\ge2`$, all points of the circle in any one square are at Euclidean distance at most $`\sqrt2`$ from any chosen point in that square. If their shorter angular separation is $`\phi`$, their chord length is $`2R\sin(\phi/2)`$. Hence all these angles lie within an interval of length at most $`4\arcsin(\sqrt2/(2R))\le C'/R`$. A square therefore has probability at most $`C''/R`$. Shannon entropy is at least minus the logarithm of the largest probability. The bounded range $`R\lt 2`$ is absorbed into the universal constants, proving (C4). Boundary points have zero angular measure.

Applying the [capacity theorem](02-capacity-law.md) with $`t_E=\sqrt{E+1}`$ gives

**(C5)**

```math
\boxed{
Q_r(E)=\frac12\log_2(E+1)
       +O_r\!\bigl(1+\log_2\log_2(E+2)\bigr).
}
```

Thus the optimized, regularized capacity satisfies

**(C6)**

```math
\lim_{E\to\infty}\frac{Q_r(E)}{\log_2E}=\frac12.
```

The constants can be chosen uniformly when $`r`$ ranges over any compact interval $`[r_-,r_+]\subset(0,\infty)`$. They are not uniform as $`r\to0`$ or $`r\to\infty`$.

## Exact entropy exchange for a thermal input

An explicit achievable rate makes the mechanism concrete. Define

**(C7)**

```math
\tau_E=\frac1{E+1}\sum_{n=0}^\infty
\left(\frac E{E+1}\right)^n|n\rangle\langle n|,
\qquad
g(E)=(E+1)\log_2(E+1)-E\log_2E,
```

with $`g(0)=0`$. A purification is the two-mode-squeezed state

**(C8)**

```math
|\psi_E\rangle_{RB}
=\frac1{\sqrt{E+1}}\sum_{n=0}^\infty
\left(\frac E{E+1}\right)^{n/2}|n\rangle_R|n\rangle_B.
```

Let $`J=N_B-N_R`$ and $`|\phi_0\rangle=(I_R\otimes D(r))|\psi_E\rangle`$. Since $`J|\psi_E\rangle=0`$ and rotation conjugates $`D(r)`$ into $`D(r e^{i\theta})`$,

**(C9)**

```math
(I_R\otimes D(r e^{i\theta}))|\psi_E\rangle
=e^{i\theta J}|\phi_0\rangle.
```

If $`P_k`$ is the spectral projector of $`J`$ with eigenvalue $`k\in\mathbb Z`$, angular averaging produces

**(C10)**

```math
\rho_{RB}^{\rm out}
=\sum_{k\in\mathbb Z}P_k|\phi_0\rangle\langle\phi_0|P_k.
```

Each nonzero summand has rank one, and different summands have orthogonal support. Therefore the nonzero eigenvalues of $`\rho_{RB}^{\rm out}`$ are exactly $`p_k=\|P_k\phi_0\|^2`$. This reduces its entropy to a classical charge distribution without asserting that the channel itself is degradable.

The characteristic function of this distribution is

**(C11)**

```math
\begin{aligned}
\sum_k p_k e^{itk}
&=\langle\psi_E|D(-r)D(r e^{it})|\psi_E\rangle\\
&=\exp\!\left[-r^2(2E+1)(1-\cos t)+i r^2\sin t\right]\\
&=\exp\!\left[\lambda_+(e^{it}-1)+\lambda_-(e^{-it}-1)\right],\\
\lambda_+&=r^2(E+1),\qquad\lambda_-=r^2E.
\end{aligned}
```

Here the thermal displacement identity is $`\mathrm{Tr}(\tau_E D(z))=\exp[-(E+1/2)|z|^2]`$. Equation (C11) identifies $`J`$ with the difference of two independent Poisson variables, the [Skellam distribution](../references/README.md#skellam). In particular,

**(C12)**

```math
\mathbb EJ=r^2,\qquad
\mathrm{Var}J=r^2(2E+1),\qquad
S(\rho_{RB}^{\rm out})=H\!\left(\mathrm{Skellam}(r^2(E+1),r^2E)\right).
```

For $`E\gt 0`$, its probabilities can be written as

**(C13)**

```math
p_k=e^{-(\lambda_++\lambda_-)}
\left(\frac{\lambda_+}{\lambda_-}\right)^{k/2}
I_{|k|}(2\sqrt{\lambda_+\lambda_-}),
```

where $`I_j`$ is the modified Bessel function. At $`E=0`$, the distribution is Poisson with mean $`r^2`$, supported on nonnegative integers. This limiting case should not be evaluated by dividing by $`\lambda_-=0`$ in (C13).

## An achievable half-logarithmic rate

The receiver output is a mixture of displaced copies of $`\tau_E`$. Entropy concavity and the maximum entropy at a fixed mean photon number give

**(C14)**

```math
g(E)\le S(\mathcal C_r(\tau_E))\le g(E+r^2).
```

Consequently,

**(C15)**

```math
\begin{aligned}
g(E)-H(J)
&\le I_c(\tau_E,\mathcal C_r)
\le g(E+r^2)-H(J),\\
Q_r(E)&\ge\max\{0,g(E)-H(J)\}.
\end{aligned}
```

These are coherent-information achievable rates under the [energy-constrained coding theorem](../references/README.md#wilde-qi). A negative displayed lower bound is uninformative; it is not a negative capacity.

The order of $`H(J)`$ can be proved without a normal approximation. Set $`V=\lambda_++\lambda_-=r^2(2E+1)`$. Fourier inversion and $`1-\cos t\ge2t^2/\pi^2`$ on $`[-\pi,\pi]`$ yield

**(C16)**

```math
p_k\le\frac1{2\pi}\int_{-\pi}^{\pi}e^{-V(1-\cos t)}\,dt
\le\frac{\sqrt\pi}{2\sqrt{2V}}.
```

Thus $`H(J)\ge\tfrac12\log_2V-O(1)`$. For the other direction, the [integer entropy bound](../references/README.md#integer-entropy) gives

**(C17)**

```math
H(J)\le\frac12\log_2\!\left[2\pi e\left(V+\frac1{12}\right)\right].
```

For completeness, if $`U`$ is independent and uniform on $`[-1/2,1/2]`$, the translated intervals are disjoint, so $`h(J+U)=H(J)`$. Its variance is $`V+1/12`$, and the continuous Gaussian maximum-entropy bound proves (C17).

At fixed $`r\gt 0`$, equations (C14)–(C17) show

**(C18)**

```math
I_c(\tau_E,\mathcal C_r)
=\frac12\log_2E+O_r(1).
```

The [general converse](03-converse.md), rather than this single input calculation, establishes optimality of the coefficient against arbitrary collective codes.

## Comparison with covariance-matched Gaussian noise

Let $`G`$ be standard circular complex Gaussian, with density $`\pi^{-1}e^{-|z|^2}`$ and $`\mathbb E|G|^2=1`$. The Gaussian channel with displacement $`rG`$ has the same added covariance $`r^2 I_2`$ and the same added mean photon number as (C2).

In this convention, additive Gaussian displacement noise is entanglement breaking when $`r^2\ge1`$. At $`r^2=1`$, it is the heterodyne measure-and-prepare channel; larger variances add further classical displacement noise. Hence its quantum capacity is zero at every energy in that range. The Gaussian channel facts and converse framework are reviewed in [PLOB](../references/README.md#plob).

By contrast, (C6) holds for every fixed $`r\gt 0`$, including $`r^2\ge1`$. Covariance does not decide whether increasing the photon budget provides an unbounded quantum communication rate. This is not a claim that Gaussian noise is a faithful model of the circular channel: the distinction between their probability laws is the result's subject.

## Boundaries and verification

At $`r=0`$, the channel is the identity and its capacity is exactly $`g(E)`$; its logarithmic coefficient is one. The limit $`r\to0`$ therefore cannot be interchanged with the fixed-$`r`$ large-energy limit. Equation (C4) locates the resolution scale $`r\sqrt{E+1}\sim1`$.

Fixed full-dimensional broadening removes the asymptotic half-logarithmic growth. The [next page](05-broadening.md) proves a finite-energy rate with nonzero Gaussian jitter and states the corresponding saturation law and order of limits.

The [verification program](../verification/README.md) evaluates the Skellam entropy with a controlled tail bound and compares the charge probabilities to independent finite-Fock matrix calculations. These numerical checks verify conventions and finite examples; (C5) and (C18) follow from the analytical arguments above.
