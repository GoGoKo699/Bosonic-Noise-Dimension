# Converse and bounded-capacity criterion

This page proves the upper half of the [finite-resolution law](02-capacity-law.md) and the criterion for finite unrestricted capacity. The argument has three parts: compare smooth displacement noise with an entanglement-breaking reference channel, smooth an arbitrary noise law only below the energy resolution, and control the resulting change in quantum capacity.

The inherited quantum tools are the relative-entropy and teleportation-simulation framework of [PLOB 2017](../references/README.md#plob) and the energy-constrained capacity-continuity theorem of [Winter 2017](../references/README.md#winter). The entropy-resolution estimates below supply the link to arbitrary, including singular, displacement laws.

Throughout, $`D(z)=\exp(za^\dagger-\overline z a)`$, $`g_1(z)=\pi^{-1}e^{-|z|^2}`$, $`G`$ has density $`g_1`$, and $`M=\mathbb E|Z|^2\lt \infty`$. A Gaussian displacement $`\sigma G`$ has complex variance $`\sigma^2`$. We use the [mean-photon coding model](01-model.md) and base-two relative entropy.

## Smooth noise admits a classical relative-entropy upper bound

**Lemma 1.** If a displacement law has a density $`f`$ satisfying $`D(f\|g_1)\lt \infty`$, then

```math
Q_f(E)\le D(f\|g_1)
```

for every finite $`E`$. In particular, the same bound holds after taking the supremum over all finite input energies.

### A separable comparison state at every finite squeezing

Let $`\Phi_R=|\phi_R\rangle\langle\phi_R|`$ be a two-mode squeezed vacuum with mean photon number $`R`$ in each mode. Define

```math
\omega_R^f=(\operatorname{id}\otimes\mathcal N_f)(\Phi_R),
\qquad
\omega_R^\gamma=(\operatorname{id}\otimes\mathcal N_{g_1})(\Phi_R).
```

The unit-variance Gaussian displacement channel is the heterodyne-and-prepare channel

```math
\mathcal N_{g_1}(\rho)
=\int_{\mathbb C}
\frac{\langle\alpha|\rho|\alpha\rangle}{\pi}
|\alpha\rangle\langle\alpha|\,d^2\alpha.
```

For example, both sides multiply the input Weyl characteristic function by $`e^{-|\xi|^2}`$. Thus this channel is entanglement breaking, and $`\omega_R^\gamma`$ is separable for every finite $`R`$.

The map that prepares
$`(I\otimes D(z))\Phi_R(I\otimes D(z)^\dagger)`$ from the classical value $`z`$ is the same for $`f`$ and $`g_1`$. Relative-entropy data processing therefore gives

```math
D(\omega_R^f\|\omega_R^\gamma)\le D(f\|g_1).
```

Writing $`E_{\mathrm R}`$ for relative entropy of entanglement,

```math
E_{\mathrm R}(\omega_R^f)\le D(f\|g_1).
```

This bound is uniform in $`R`$. It uses a finite-energy separable comparison state, without treating an infinitely squeezed state as a density operator.

### The simulation limit is taken for a fixed finite code

[Braunstein–Kimble continuous-variable teleportation](../references/README.md#braunstein-kimble) using resource $`\Phi_R`$ implements an additive Gaussian displacement with variance

```math
\xi_R=(\sqrt{R+1}-\sqrt R)^2.
```

Every random displacement channel is teleportation covariant:

```math
\mathcal N_f(D(\beta)\rho D(\beta)^\dagger)
=D(\beta)\mathcal N_f(\rho)D(\beta)^\dagger.
```

Consequently, the same teleportation protocol with resource $`\omega_R^f`$ implements

```math
\mathcal N_f\circ\mathcal N_{\sqrt{\xi_R}G}.
```

This is the finite-squeezing form of the simulation used in the PLOB framework. The additional Gaussian noise tends to zero as $`R\to\infty`$.

Fix a finite $`n`$-use unassisted code with average input energy at most $`nE`$. Replacing its channel calls by these simulations turns the protocol into local operations and classical communication acting on $`(\omega_R^f)^{\otimes n}`$ and local initial systems. Monotonicity and subadditivity of relative entropy of entanglement imply that its decoded state $`\rho_R`$ obeys

```math
E_{\mathrm R}(\rho_R)\le nD(f\|g_1).
```

For this fixed code, $`\rho_R`$ converges in trace norm to the actual decoded state as $`R\to\infty`$. One direct bound uses the displacement estimate proved below: if $`E_j`$ are the input marginals' energies, the half trace-norm error is at most

```math
\sqrt{\xi_R}\sum_{j=1}^n\sqrt{4E_j+2}
\le n\sqrt{\xi_R}\sqrt{4E+2}.
```

The first inequality follows by telescoping the product channels; local trace-preserving maps on other factors do not change the relevant input marginal. The second uses concavity and $`\sum_jE_j\le nE`$.

Suppose the decoded target is a maximally entangled state $`\Phi_d`$, with squared fidelity
$`F=\operatorname{Tr}(\Phi_d\rho)`$. A separable state has overlap at most $`1/d`$ with $`\Phi_d`$. Applying the binary measurement $`\{\Phi_d,I-\Phi_d\}`$ to the relative entropy gives, for $`F\ge1/d`$,

```math
E_{\mathrm R}(\rho)\ge F\log_2d-h_2(F).
```

Apply this inequality to $`\rho_R`$, then let $`R\to\infty`$ while holding the finite code fixed. Its actual decoded fidelity therefore satisfies

```math
F\log_2d-h_2(F)\le nD(f\|g_1).
```

Only after this step do we take a sequence of reliable codes with $`n\to\infty`$ and $`F\to1`$. Their rates cannot exceed $`D(f\|g_1)`$, proving Lemma 1. No uniform finite-squeezing approximation to an infinite coding block is assumed.

### Gaussian reference variance can be optimized

The same comparison is valid with any Gaussian density

```math
g_w(z)=\frac{1}{\pi w}e^{-|z|^2/w},
\qquad w\ge1.
```

For $`w=1`$ its channel is heterodyne-and-prepare. For $`w\gt1`$, it is that channel followed by independent Gaussian displacement noise of variance $`w-1`$, and is therefore still entanglement breaking. Replacing $`\omega_R^\gamma`$ by the corresponding separable channel state in the same finite-squeezing proof gives

```math
Q_f(E)\le D(f\|g_w)
=\log_2(\pi w)
 +\frac{\mathbb E_f|Z|^2}{w}\log_2e-h(f).
```

The statement holds whenever the relative entropy is finite and is vacuous otherwise; taking the supremum over finite $`E`$ preserves it. The main finite-resolution proof uses $`w=1`$. A different $`w`$ can improve finite constants in the [broadened-circle bound](05-broadening.md).

## Smoothing entropy and quantization entropy differ by a constant

Let $`f_\sigma`$ be the density of $`Z+\sigma G`$, with $`\sigma\gt 0`$. It has finite second moment $`M+\sigma^2`$, is bounded by $`1/(\pi\sigma^2)`$, and has finite differential entropy.

**Lemma 2.** There is a universal constant $`C_{\mathrm{int}}`$ such that

```math
h(f_\sigma)
\ge 2\log_2\sigma
  +H_{1/\sigma}(\mu)
  +\log_2(\pi e)-C_{\mathrm{int}}.
```

The complementary bound is

```math
h(f_\sigma)
\le2\log_2\sigma+H_{1/\sigma}(\mu)+\log_2(3\pi e).
```

Thus $`h(f_\sigma)=2\log_2\sigma+H_{1/\sigma}(\mu)+O(1)`$ with universal constants, although the capacity converse only needs the lower bound.

One explicit choice is

```math
C_{\mathrm{int}}
=2\log_2(1+\sqrt\pi)+10\log_2e.
```

Here $`h`$ denotes differential entropy in bits; $`h_2`$ elsewhere on this page denotes binary entropy.

### Proof

Set

```math
X=Z/\sigma,\qquad B=\lfloor X\rfloor,\qquad
U=X-B\in[0,1)^2,\qquad Y=X+G.
```

Conditional on $`B`$, the density of $`Y`$ is a mixture of translates of the standard Gaussian. Differential-entropy concavity gives

```math
h(Y\mid B)\ge h(G)=\log_2(\pi e).
```

Moreover,

```math
H(B\mid Y)
\le H(B-\lfloor Y\rfloor)
=H(-\lfloor U+G\rfloor).
```

The integer vector $`K=\lfloor U+G\rfloor`$ has a bounded second moment. Independence and zero mean of $`G`$ give

```math
\mathbb E|U+G|^2\le3,\qquad
\mathbb E|K|^2\le10.
```

Comparison with the discrete Gaussian proportional to $`e^{-|k|^2}`$ on $`\mathbb Z^2`$ yields

```math
H(K)\le
2\log_2(1+\sqrt\pi)+10\log_2e
=C_{\mathrm{int}}.
```

The normalizing bound used here is
$`\sum_{j\in\mathbb Z}e^{-j^2}\le1+\sqrt\pi`$.
The chain rule then gives

```math
\begin{aligned}
h(Y)
&=h(Y\mid B)+H(B)-H(B\mid Y)\\
&\ge \log_2(\pi e)+H_{1/\sigma}(\mu)-C_{\mathrm{int}}.
\end{aligned}
```

For the upper bound, the conditional variable $`U+G`$ has second moment at most three for every value of $`B`$. The two-dimensional Gaussian maximum-entropy bound therefore gives $`h(Y\mid B)\le\log_2(3\pi e)`$, and $`h(Y)\le H(B)+h(Y\mid B)`$ gives the claimed estimate.

Rescaling from $`Y`$ to $`\sigma Y=Z+\sigma G`$ proves both sides of Lemma 2. All terms are finite under the second-moment assumption, so the calculation contains no subtraction of infinite entropies.

### Relative entropy of the smoothed law

Since $`\mathbb E|Z+\sigma G|^2=M+\sigma^2`$,

```math
D(f_\sigma\|g_1)
=-h(f_\sigma)+\log_2\pi
 +(M+\sigma^2)\log_2e.
```

Lemma 2 therefore implies

```math
\boxed{
D(f_\sigma\|g_1)
\le 2\log_2(1/\sigma)-H_{1/\sigma}(\mu)
 +C_{\mathrm{int}}+(M+\sigma^2-1)\log_2e.
}
```

In particular, when $`0\lt \sigma\le1`$, the last two terms are at most
$`C_{\mathrm{int}}+M\log_2e`$. This estimate applies equally to atomic, singular-continuous, and absolutely continuous original laws.

## Smoothing below the energy resolution changes capacity little

### Energy-constrained diamond distance

For an input with arbitrary reference system and oscillator mean photon number at most $`E`$, purify the joint state if necessary. Write $`z=x+iy`$ and

```math
D(z)=e^{iA_z},\qquad A_z=\sqrt2(yq-xp),
\qquad q^2+p^2=2\hat n+1.
```

The spectral inequality $`|e^{iu}-1|\le|u|`$ and Cauchy–Schwarz give

```math
\begin{aligned}
\frac12\|
(I\otimes D(z))\rho(I\otimes D(z)^\dagger)-\rho
\|_1
&\le \|(D(z)-I)|\psi\rangle\|\\
&\le \sqrt{\langle A_z^2\rangle}\\
&\le |z|\sqrt{4E+2}.
\end{aligned}
```

The quadratic-form estimate uses
$`\|(yq-xp)\psi\|^2\le(x^2+y^2)(\|q\psi\|^2+\|p\psi\|^2)`$.
It remains valid for entangled inputs because only the oscillator's energy enters.

Average this bound over $`\sigma G`$, use $`\mathbb E|G|\le1`$, and then use trace-norm contractivity under $`\mathcal N_\mu`$. The convolution identity for Weyl conjugations gives

```math
\boxed{
\frac12\|\mathcal N_\mu-\mathcal N_{f_\sigma}\|_{\diamond,E}
\le \sigma\sqrt{4E+2}.
}
```

The phases in the Weyl multiplication law cancel in conjugation; this identity does not require the displacement operators themselves to commute.

### A common output-energy bound

For an input of mean photon number $`x`$,

```math
\operatorname{Tr}\!\left[\hat n\,\mathcal N_\mu(\rho)\right]
\le x+M+2\sqrt{xM}
\le2x+2M.
```

For $`\sigma\le1`$, the original and smoothed channels consequently share the affine energy bound

```math
\operatorname{Tr}\!\left[\hat n\,\mathcal N(\rho)\right]
\le 2x+2M+2.
```

The oscillator number Hamiltonian is grounded and satisfies the Gibbs condition required for capacity continuity.

### The inherited continuity estimate

[Winter 2017, Theorem 9](../references/README.md#winter) states that two channels with common affine output-energy bound $`\alpha E+E_0`$ and half energy-constrained diamond distance at most $`\varepsilon\lt 1`$ satisfy

```math
\begin{aligned}
|Q_1(E)-Q_2(E)|
&\le
56\sqrt\varepsilon\,
g\!\left(\frac{4(\alpha E+E_0)}{\sqrt\varepsilon}\right)\\
&\quad+6g(4\sqrt\varepsilon).
\end{aligned}
```

The theorem already concerns the regularized mean-energy-constrained quantum capacity. Thus its use here controls arbitrary coding blocks, rather than only a single coherent-information expression.

For $`E\ge1`$, choose

```math
L=\log_2(E+2),\qquad
\varepsilon=L^{-2},\qquad
\sigma=\frac{L^{-2}}{\sqrt{4E+2}}.
```

Then $`0\lt \sigma\lt 1`$, the diamond-distance condition holds, and

```math
|Q_\mu(E)-Q_{f_\sigma}(E)|
\le W_M(E),
```

where

```math
W_M(E)=
\frac{56}{L}\,g\!\left(8(E+M+1)L\right)
+6g(4/L).
```

This function is bounded uniformly over $`E\ge1`$ at fixed $`M`$. For an explicit, deliberately nonoptimal bound, use
$`g(x)\le\log_2(e(x+1))`$,
$`E+M+1\le(E+2)(M+1)`$, and
$`(\log_2L)/L\le1`$. They give

```math
W_M(E)\le
56\!\left[2+\log_2(M+1)+\log_2(9e)\right]+6g(4).
```

## Collecting the finite-resolution upper bound

Apply Lemma 1 to the smoothed law, Lemma 2 to its relative entropy, and the preceding continuity estimate:

```math
\begin{aligned}
Q_\mu(E)
&\le 2\log_2(1/\sigma)-H_{1/\sigma}(\mu)\\
&\quad+C_{\mathrm{int}}+M\log_2e+W_M(E).
\end{aligned}
```

The scale $`1/\sigma`$ is finer than $`t_E=\sqrt{E+1}`$. Each cell of the finer grid intersects at most four cells of the coarser grid, even when the two grids are not nested. Hence

```math
H_{1/\sigma}(\mu)\ge H_{t_E}(\mu)-2.
```

Also,

```math
\begin{aligned}
2\log_2(1/\sigma)
&=\log_2(4E+2)+4\log_2L\\
&\le\log_2(E+1)+4\log_2L+2.
\end{aligned}
```

It follows that

```math
Q_\mu(E)\le
\log_2(E+1)-H_{t_E}(\mu)
+4\log_2\log_2(E+2)+C_M,
```

with the explicit admissible constant

```math
\begin{aligned}
C_M={}&C_{\mathrm{int}}+M\log_2e+4\\
&+56\!\left[2+\log_2(M+1)+\log_2(9e)\right]
+6g(4).
\end{aligned}
```

Together with the thermal-input argument, this proves Theorem 1 of the [capacity-law page](02-capacity-law.md#the-finite-resolution-capacity-law).

The double-logarithmic remainder comes from smoothing slightly below the energy resolution so that the capacity-continuity cost stays bounded. This proof does not establish a constant remainder for arbitrary noise laws.

## When is the unconstrained capacity finite?

Define

```math
Q_\mu(\infty)=\sup_{E\lt \infty}Q_\mu(E).
```

**Theorem 3.** Under $`M\lt \infty`$,

```math
\boxed{
Q_\mu(\infty)\lt \infty
\quad\Longleftrightarrow\quad
D(\mu\|\gamma)\lt \infty.
}
```

Moreover, when the relative entropy is finite,
$`Q_\mu(\infty)\le D(\mu\|\gamma)`$.

### Finite relative entropy implies finite capacity

Finite $`D(\mu\|\gamma)`$ implies that $`\mu`$ has a density with respect to the strictly positive Gaussian density $`g_1`$, and hence with respect to Lebesgue measure. Lemma 1 bounds $`Q_\mu(E)`$ by the same finite number for every $`E`$. Taking the supremum proves this direction.

### Infinite relative entropy is detected by resolved thermal inputs

For $`t=2^m`$, let $`\mathcal P_m`$ be the countable partition of $`\mathbb R^2`$ into dyadic squares of side $`1/t`$. Write $`p_{m,k}`$ and $`q_{m,k}`$ for the probabilities of cell $`k`$ under $`\mu`$ and $`\gamma`$, and set

```math
D_m=D(p_m\|q_m).
```

These are relative entropies of classical noise distributions. The partitions are nested and generate the Borel sigma algebra. Classical relative-entropy approximation therefore gives

```math
D_m\uparrow D(\mu\|\gamma),
```

including when $`\mu`$ has a singular component or the limit is infinite.

For completeness, the convergence can be seen from the variational formula for relative entropy. For any bounded continuous function $`u`$, replace $`u(z)`$ by its value at the lower-left corner of the dyadic cell containing $`z`$. The resulting bounded functions are measurable with respect to $`\mathcal P_m`$ and converge pointwise to $`u`$. Dominated convergence applies to their expectations and exponentials. The discrete variational formula consequently gives
$`\liminf_mD_m\ge\int u\,d\mu-\log_2\int2^u\,d\gamma`$.
Taking the supremum over bounded continuous $`u`$ gives the full relative entropy; data processing gives the opposite inequality and monotonicity.

It remains to compare $`D_m`$ with the thermal lower bound. For every $`z`$ in a grid cell $`k`$, the Gaussian probability of that cell obeys

```math
q_{m,k}
\ge
\frac{1}{\pi t^2}
\exp\!\left(-2|z|^2-\frac4{t^2}\right).
```

Indeed, every point $`w`$ of the cell satisfies
$`|w|^2\le2|z|^2+4/t^2`$. Therefore its cross entropy satisfies, for $`t\ge1`$,

```math
\begin{aligned}
\sum_kp_{m,k}[-\log_2q_{m,k}]
&\le2\log_2t+\log_2\pi\\
&\quad+(2M+4)\log_2e.
\end{aligned}
```

The quantities are finite, and

```math
D_m
=\sum_kp_{m,k}[-\log_2q_{m,k}]-H_t(\mu).
```

Set $`E_m=t^2-1`$. The thermal-input lower bound gives

```math
\begin{aligned}
Q_\mu(E_m)
&\ge2\log_2t-H_t(\mu)-2g(2)\\
&\ge D_m-\log_2\pi-(2M+4)\log_2e-2g(2).
\end{aligned}
```

If $`D(\mu\|\gamma)=\infty`$, the right-hand side tends to infinity. Thus the capacity is unbounded as input energy increases. This argument does not depend on whether the information dimension exists.

### Equivalent density criterion and its limits

For an absolutely continuous law with density $`f`$ and finite second moment,

```math
D(\mu\|\gamma)
=\log_2\pi+M\log_2e-h(f),
```

with the extended value $`+\infty`$ when $`h(f)=-\infty`$. Finite second moment bounds differential entropy from above, so the criterion can be stated as follows: unrestricted capacity is finite exactly for absolutely continuous noise with differential entropy greater than $`-\infty`$.

Every nonzero singular component gives infinite relative entropy and unbounded capacity. A fully absolutely continuous law can also have differential entropy $`-\infty`$ and unbounded capacity. Such examples may have information dimension two and hence zero logarithmic coefficient. Boundedness and the coefficient of $`\log E`$ are separate conclusions.

The finite-relative-entropy bound is generally an upper bound, not an exact capacity formula. In particular, applying it to a Gaussian density recovers a relative-entropy bound without resolving the remaining fixed-noise Gaussian quantum-capacity gap.
