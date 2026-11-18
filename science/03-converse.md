# Converse and bounded-capacity criterion

This page proves the upper bound in the [finite-resolution law](02-capacity-law.md) for arbitrary adaptive protocols. A comparison with an entanglement-breaking channel bounds the entanglement added by the smoothed displacement law. The two discarded modes of a Gaussian smoothing operation bound what is lost in passing from the original law to that smoothed law.

Write $`g_1(z)=\pi^{-1}e^{-\lvert z\rvert^2}`$ for the density of the standard complex Gaussian law $`\gamma`$. Let $`G\sim\gamma`$ be independent of the original kick $`Z\sim\mu`$, and write $`M=\mathbb E\lvert Z\rvert^2`$. The entropy of a thermal mode with mean photon number $`x`$ is $`g(x)`$. All logarithms are base two.

## Smooth noise admits a classical relative-entropy upper bound

Let $`Q_{2,f}(E)`$ denote the adaptive two-way assisted quantum capacity for displacement density $`f`$, with the [unconditional transmitted-photon budget](01-model.md). For a bipartite state $`\rho`$, let $`E_{\mathrm R}(\rho)`$ be the infimum of its relative entropy to a separable state across the current Alice–Bob cut.

**Lemma 1.** If $`D(f\Vert g_1)\lt\infty`$, a single use of the channel with law $`f`$ increases the relative entropy of entanglement by at most $`D(f\Vert g_1)`$, including arbitrary prior Alice–Bob correlations. In particular,

```math
Q_f(E)\le Q_{2,f}(E)\le D(f\Vert g_1).
```

### Compare the two displacement laws on each use

Immediately before a use, let $`A'A`$ belong to Alice and $`B'`$ to Bob. The sent oscillator is $`A`$. Write $`\rho`$ for the actual input and $`\omega`$ for any separable comparison state across $`A'A:B'`$. The two displacement channels can be realized by the same processor controlled by classical kicks with different laws. Relative-entropy data processing gives

```math
D\!\left((\mathrm{id}\otimes\mathcal N_f)(\rho)\,\Vert\,
          (\mathrm{id}\otimes\mathcal N_{g_1})(\omega)\right)
\le D(\rho\Vert\omega)+D(f\Vert g_1).
```

Here the identity acts on both memories. To justify the comparison for continuous kicks, partition a growing square into finitely many cells of shrinking diameter and take one additional tail cell. Replace each kick by the fixed representative of its cell, using the same representatives for both laws. The finite classical registers have relative entropy at most $`D(f\Vert g_1)`$ by coarse-graining. Tensoring each register with its respective input, applying the controlled displacement, and tracing out the register proves the inequality for the two discrete approximations. The channel outputs converge in trace norm on each fixed input by strong continuity of the displacements and dominated convergence. Joint lower semicontinuity of relative entropy gives the displayed bound for the exact channels. This is the displacement version of the [environment-parametrized comparison argument](../references/README.md#environment-parametrized).

The channel with density $`g_1`$ has the heterodyne-and-prepare form

```math
\mathcal N_{g_1}(\rho_A)
=\int_{\mathbb C}\frac{\langle\alpha|\rho_A|\alpha\rangle}{\pi}
  |\alpha\rangle\langle\alpha|\,\mathrm d^2\alpha.
```

For example, both expressions multiply the Weyl characteristic function by $`e^{-\lvert\xi\rvert^2}`$. The channel is entanglement breaking. Its output on the separable comparison input is therefore separable across $`A':BB'`$, where $`B`$ is the received mode. Taking the infimum over $`\omega`$ gives Lemma 1's one-use inequality. This separability is needed for the exact comparison channel.

### From entanglement accounting to a rate bound

Local operations and classical communication do not increase $`E_{\mathrm R}`$. If the initial state is separable and the one-use increments sum to at most $`nL`$, the final state has relative entropy of entanglement at most $`nL`$. To transmit a $`d`$-dimensional quantum system, test the decoded state against a maximally entangled state $`\Phi_d`$. Write $`F`$ for the test acceptance probability on the actual state; a separable state passes with probability at most $`1/d`$. Relative entropy under this binary test gives

```math
F\log_2 d-h_2(F)\le E_{\mathrm R}(\rho_{\mathrm{dec}})\le nL.
```

Along a reliable sequence, $`F\to1`$, so its asymptotic rate is at most $`L`$. Applying this with $`L=D(f\Vert g_1)`$ proves the capacity statement. The argument uses the states of the actual adaptive code.

### Gaussian reference variance can be optimized

For any variance $`w\ge1`$, the density

```math
g_w(z)=\frac{1}{\pi w}e^{-\lvert z\rvert^2/w}
```

describes the heterodyne-and-prepare channel followed by independent Gaussian displacement of variance $`w-1`$. The same comparison therefore yields

```math
Q_{2,f}(E)\le D(f\Vert g_w)
=\log_2(\pi w)+\frac{\mathbb E_f\lvert Z\rvert^2}{w}\log_2e-h(f).
```

The main proof uses $`w=1`$. Optimizing $`w`$ is useful for a [finite bound on a broadened circle](05-broadening.md).

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
D(f_\sigma\Vert g_1)
=-h(f_\sigma)+\log_2\pi
 +(M+\sigma^2)\log_2e.
```

Lemma 2 therefore implies

```math
\boxed{
D(f_\sigma\Vert g_1)
\le 2\log_2(1/\sigma)-H_{1/\sigma}(\mu)
 +C_{\mathrm{int}}+(M+\sigma^2-1)\log_2e.
}
```

In particular, when $`0\lt \sigma\le1`$, the last two terms are at most
$`C_{\mathrm{int}}+M\log_2e`$. This estimate applies equally to atomic, singular-continuous, and absolutely continuous original laws.

## Adaptive converse at the energy resolution

### The two modes discarded by Gaussian smoothing

For $`E\ge1`$, set $`v=(E+1)^{-1}`$ and $`\sigma=\sqrt v`$. The smoothing channel $`\mathcal N_{\sigma G}`$ can be realized as vacuum attenuation with transmissivity $`\eta=1/(1+v)`$ followed by quantum-limited vacuum amplification with gain $`1+v`$. If the input mode has annihilation operator $`a`$ and auxiliary independent vacuum modes have operators $`e_1,e_2`$, the signal output is

```math
b=a+\sqrt v(e_1+e_2^\dagger).
```

The vacuum expectation of the Weyl operator on these two auxiliary modes contributes the factor $`e^{-v\lvert\xi\rvert^2}`$. Thus the signal channel is precisely the Gaussian displacement of complex variance $`v`$. If its input has mean photon number $`x`$, the two unused outputs have mean photon numbers

```math
x_1=(1-\eta)x,
\qquad
x_2=v(\eta x+1).
```

The first output is the unused beam-splitter port. The second is the idler output of the amplifier, whose mean includes the vacuum term. This decomposition is a [standard Gaussian-channel tool](../references/README.md#sharma-wilde).

### Discarding the modes costs at most twice their entropy

For any state with a finite-entropy subsystem $`F`$ on Bob's side,

```math
E_{\mathrm R}(A:BF)
\le E_{\mathrm R}(A:B)+2S(F).
```

In finite dimensions, use a separable comparator $`\omega_{AB}\otimes\rho_F`$. Its relative entropy from the state on $`ABF`$ equals $`D(\rho_{AB}\Vert\omega_{AB})+I(AB:F)_\rho`$. Infimize over comparisons and use $`I(AB:F)\le2S(F)`$. The same inequality holds in the oscillator setting with arbitrary local memories. Compress each local system onto increasing finite-rank subspaces, resetting the discarded tail to one local flag. Choose the projectors for $`F`$ in the eigenbasis of its marginal, so grouping tail eigenvalues cannot increase $`S(F)`$. The finite-dimensional inequalities then have right sides bounded by the original right side by local monotonicity. The compressed states converge in trace norm, and [lower semicontinuity of the relative entropy of entanglement](../references/README.md#lami-shirokov) yields the claim. This argument never forms a difference of possibly infinite marginal entropies.

Apply the attenuation and amplification isometry locally at Bob, keeping the two unused modes together as $`F`$. The isometry preserves the original relative entropy of entanglement across the Alice–Bob cut. Tracing out $`F`$ gives the output for the smoothed noise density $`f_\sigma`$ by composition of the Weyl conjugations. The preceding inequality, subadditivity of entropy and the thermal maximum-entropy bound give a per-use loss of at most

```math
2 S(F)\le 2g((1-\eta)x)+2g(v(\eta x+1)).
```

The two modes are local auxiliaries in the converse. The communicating parties are not required to run the smoother.

### Collecting the finite-resolution upper bound

Let $`e_j`$ and $`x_j`$ be the actual mean photon numbers before and after the original channel in use $`j`$, unconditioned over all earlier outcomes. The displacement identity for the number operator and Cauchy–Schwarz give

```math
x_j\le e_j+2\sqrt{Me_j}+M\le2e_j+2M.
```

Since $`\sum_j e_j\le nE`$, the average of $`x_j`$ is at most $`2E+2M`$. Hence for each of the two auxiliary outputs its mean photon number, averaged over uses, is bounded by $`2+2M`$. Concavity of $`g`$ gives

```math
\sum_{j=1}^{n}\left[2g((1-\eta)x_j)+2g(v(\eta x_j+1))\right]
\le4n g(2+2M).
```

Lemma 1 charges at most $`D(f_\sigma\Vert g_1)`$ to the smoothed output at each actual input. Adding the entropy cost just proved bounds the entanglement increment of each original use. The adaptive rate test consequently yields

```math
Q_{2,\mu}(E)\le D(f_\sigma\Vert g_1)+4g(2+2M).
```

Finally apply [the smoothing entropy estimate](#relative-entropy-of-the-smoothed-law) with $`\sigma=(E+1)^{-1/2}`$:

```math
\boxed{
Q_{2,\mu}(E)\le\log_2(E+1)-H_{\sqrt{E+1}}(\mu)+C_M,
\qquad
C_M=C_{\mathrm{int}}+M\log_2e+4g(2+2M).
}
```

The input constraint has been imposed only on the average of the actual transmitted photon numbers. No per-use or per-outcome cutoff is needed. At this smoothing scale the two discarded modes carry a bounded entropy per use even when the code reallocates energy adaptively. Combining the converse with the [ordinary thermal-input lower bound](02-capacity-law.md#why-one-thermal-input-suffices-for-the-lower-bound) proves Theorem 1 for both capacities.

## When is the unconstrained capacity finite?

Define

```math
Q_\mu(\infty)=\sup_{E\lt\infty}Q_\mu(E),\qquad Q_{2,\mu}(\infty)=\sup_{E\lt\infty}Q_{2,\mu}(E).
```

**Theorem 3.** Under $`M\lt \infty`$,

```math
\boxed{
Q_\mu(\infty)\lt\infty\quad\Longleftrightarrow\quad Q_{2,\mu}(\infty)\lt\infty
\quad\Longleftrightarrow\quad
D(\mu\Vert\gamma)\lt \infty.
}
```

Moreover, when the relative entropy is finite,
$`Q_\mu(\infty)\le Q_{2,\mu}(\infty)\le D(\mu\Vert\gamma)`$.

### Finite relative entropy implies finite capacity

Finite $`D(\mu\Vert\gamma)`$ implies that $`\mu`$ has a density with respect to the strictly positive Gaussian density $`g_1`$, and hence with respect to Lebesgue measure. Lemma 1 bounds $`Q_{2,\mu}(E)`$ by the same finite number for every $`E`$. Taking the supremum proves this direction.

### Infinite relative entropy is detected by resolved thermal inputs

For $`t=2^m`$, let $`\mathcal P_m`$ be the countable partition of $`\mathbb R^2`$ into dyadic squares of side $`1/t`$. Write $`p_{m,k}`$ and $`q_{m,k}`$ for the probabilities of cell $`k`$ under $`\mu`$ and $`\gamma`$, and set

```math
D_m=D(p_m\Vert q_m).
```

These are relative entropies of classical noise distributions. The partitions are nested and generate the Borel sigma algebra. Classical relative-entropy approximation therefore gives

```math
D_m\uparrow D(\mu\Vert\gamma),
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

If $`D(\mu\Vert\gamma)=\infty`$, the right-hand side tends to infinity. Thus the capacity is unbounded as input energy increases. This argument does not depend on whether the information dimension exists.

### Equivalent density criterion and its limits

For an absolutely continuous law with density $`f`$ and finite second moment,

```math
D(\mu\Vert\gamma)
=\log_2\pi+M\log_2e-h(f),
```

with the extended value $`+\infty`$ when $`h(f)=-\infty`$. Finite second moment bounds differential entropy from above, so the criterion can be stated as follows: unrestricted capacity is finite exactly for absolutely continuous noise with differential entropy greater than $`-\infty`$.

Every nonzero singular component gives infinite relative entropy and unbounded capacity. A fully absolutely continuous law can also have differential entropy $`-\infty`$ and unbounded capacity. Such examples may have information dimension two and hence zero logarithmic coefficient. Boundedness and the coefficient of $`\log E`$ are separate conclusions.

The finite-relative-entropy bound is generally an upper bound, not an exact capacity formula. In particular, applying it to a Gaussian density recovers a relative-entropy bound without resolving the remaining fixed-noise Gaussian quantum-capacity gap.
