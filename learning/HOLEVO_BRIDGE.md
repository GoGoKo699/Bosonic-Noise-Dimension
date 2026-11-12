# From Holevo's oscillator foundations to noise-resolution capacity

[Learning route](README.md) · [Milestone map](MILESTONES.md) · [Scientific account](../science/README.md)

The project's central question is how much quantum communication survives when a bosonic mode receives a random displacement whose probability law may be singular. Holevo supplies the language of channels, entropy, coding and canonical variables. The project combines that foundation with energy-constrained coding, continuity and simulation results, then supplies the displacement-resolution arguments needed for its capacity law.

## Selected edition and source map

The anchor is Alexander S. Holevo, *Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition, De Gruyter, 2019, DOI [10.1515/9783110642490](https://doi.org/10.1515/9783110642490), PDF ISBN 978-3-11-064249-0. The [publisher's record](https://www.degruyterbrill.com/document/doi/10.1515/9783110642490/html) identifies this edition. The matching [publisher-produced preview](https://api.pageplace.de/preview/DT0400.9783110642490_A39059069/preview-9783110642490_A39059069.pdf) includes its front matter and detailed contents; the [publisher's contents record](https://www.degruyterbrill.com/document/doi/10.1515/9783110642490-toc/html) provides the chapter listing.

The table uses paraphrased topic labels for this bridge and verified section/page pointers. Page numbers are the book's printed pages, as listed in its contents on pp. XI–XV.

| Chapter and topic | Verified reading locations | Role here |
|---|---|---|
| 7: Entropic tools, p. 126 | §§7.1–7.3, pp. 126–132; §7.6, p. 141 | Relative entropy, its monotonicity, entropy inequalities and the entropy transferred to a channel environment. |
| 10: Quantum coding, p. 187 | §§10.3.1–10.3.3, pp. 202, 206, 208; §10.4.4, p. 222 | Achievable rates, the coherent-information characterization, the special role of degradability and quantum coding. |
| 11: Energy restrictions in infinite dimensions, p. 233 | §§11.1–11.2, pp. 233, 237; §11.5, p. 243; §11.7, p. 248 | Infinite-dimensional states and entropies, input restrictions and entanglement breaking. |
| 12: Bosonic Gaussian formalism, p. 255 | §12.2, p. 265; §§12.3.4–12.3.5, pp. 281, 284; §12.4.4, p. 294; §§12.6.2–12.6.4, pp. 324, 325, 328 | Canonical variables, Gaussian entropy and purification, additive-noise channels and Gaussian capacity bounds. |

Earlier foundations can be located at §2.2, p. 13, for states; §3.1.3, p. 37, for purification; §§4.1–4.2, pp. 55–57, for classical entropy; and §§6.6–6.7, pp. 115–119, for channel complements and covariance. These pointers identify reading locations, not textbook theorem numbers for the project's new results.

## Three layers of the argument

| Layer | What it contributes | Where the contribution enters |
|---|---|---|
| Textbook foundations | States, purifications, channels, entropy, coherent information, canonical variables and Gaussian states. | Definitions and calculations throughout the [model](../science/01-model.md), lower bound and examples. |
| Primary research tools | [Wilde–Qi](../references/README.md#wilde-qi) for the mean-energy coding theorem; [Winter](../references/README.md#winter) for capacity continuity; [Braunstein–Kimble](../references/README.md#braunstein-kimble) and [PLOB](../references/README.md#plob) for finite-squeezing simulation and entanglement bounds; [Rényi](../references/README.md#renyi) for information dimension. | The operational lower bound, the converse and the meaning of the limiting dimension. |
| Derivations supplied here | Bin-conditioned entropy exchange, inverse squeezing at the energy resolution, smoothing-versus-quantization entropy, the resulting capacity law, the boundedness criterion, and the circular and broadened examples. | [Capacity law](../science/02-capacity-law.md), [converse](../science/03-converse.md), [circle](../science/04-circular-noise.md) and [broadening](../science/05-broadening.md). |

The distinction matters in infinite dimensions. Chapter 10 provides the quantum-coding foundation; the precise average-photon operational theorem used here is the Wilde–Qi result. The finite-dimensional continuity material in §7.4, p. 134, supplies useful background, while the needed channel-capacity modulus comes from Winter. Likewise, the teleportation introduction at §3.3.4, p. 48, is supplemented by the continuous-variable finite-squeezing protocol and its channel-simulation analysis.

## Translating canonical variables into the project's photon scale

The real-coordinate language of Chapter 12 and this project's complex displacement can be compared by fixing the conventions explicitly. For one mode, set

```math
R=(q,p)^T,\qquad
\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
[R_j,R_k]=i\Omega_{jk},\qquad
W(\xi)=e^{i\xi^T R}.
```

The project uses

```math
a=\frac{q+ip}{\sqrt2},\qquad
D(z)=e^{za^\dagger-\bar z a}
=W\!\left(\sqrt2\mathrm{Im}z,-\sqrt2\mathrm{Re}z\right).
```

Thus the real vector labeling a Weyl characteristic function is not the vector by which the quadrature means move. For $`z=x+iy`$,

```math
D(z)^\dagger(q,p)^T D(z)
=(q,p)^T+(\sqrt2x,\sqrt2y)^T.
```

This translation fixes the signs and the factors of two before any noise variance is interpreted. The Weyl relation is

```math
D(z)D(w)
=e^{(z\bar w-\bar z w)/2}D(z+w).
```

Its scalar phase disappears in $`D(z)D(w)\rho D(w)^\dagger D(z)^\dagger`$. Random-displacement channels consequently compose by convolving their classical laws even though the displacement operators themselves need not commute. This gives covariance and a convolution rule; it does not give degradability.

The remaining translations are:

| Quantity | Convention in this project | Consequence |
|---|---|---|
| Photon observable | $`N=a^\dagger a=(q^2+p^2-1)/2`$ | The vacuum has zero photons. A physical oscillator Hamiltonian is $`\hbar\omega(N+1/2)`$, so its zero-point energy is not part of the photon budget. |
| Covariance | $`V_{jk}=\tfrac12\langle\{R_j-m_j,R_k-m_k\}\rangle`$, with $`m_j=\langle R_j\rangle`$ | The vacuum covariance is $`I_2/2`$. |
| Thermal state with mean $`E`$ | $`V=(E+1/2)I_2`$ | Its entropy is $`g(E)`$, with $`g(x)=(x+1)\log_2(x+1)-x\log_2x`$. |
| Gaussian symplectic eigenvalues | $`\nu_j\ge1/2`$ in this covariance convention | A Gaussian state's entropy is $`\sum_j g(\nu_j-1/2)`$. |
| Standard complex Gaussian | $`p_G(z)=\pi^{-1}e^{-\lvert z\rvert^2}`$ | $`\mathbb E\lvert G\rvert^2=1`$, and each real component has variance $`1/2`$. |
| Gaussian displacement $`\sigma G`$ | $`\mathbb E\lvert\sigma G\rvert^2=\sigma^2`$ | It adds $`\sigma^2I_2`$ to the quadrature covariance and $`\sigma^2`$ to the mean photon number. |
| Information units | Base-two logarithms throughout | A formula written with natural logarithms must be divided by $`\ln2`$ to give bits or qubits per use. |

Gaussian entropy and purification are the Chapter 12 concepts used in these calculations. Their application to the present conventions is developed in the [model](../science/01-model.md) and [broadening derivation](../science/05-broadening.md). Once the noise law is non-Gaussian, covariance alone generally does not determine the state entropy.

## From coherent information to the stated capacity

The project's channel is

```math
\mathcal N_\mu(\rho)
=\int_{\mathbb C}D(z)\rho D(z)^\dagger\,\mu(dz),
\qquad M=\int|z|^2\mu(dz)\lt\infty.
```

The assumptions that carry the argument are concrete:

- The probability law is known, is fixed as energy increases, and is independently sampled on each use.
- The realized displacement is unobserved. No classical flag telling the receiver which error occurred accompanies the channel output.
- A block of $`n`$ uses satisfies $`\mathrm{Tr}\rho_{A^n}\sum_jN_j\le nE`$ on the encoded maximally mixed logical input. This is an unconditional average input constraint.
- The task is unassisted quantum communication with arbitrary block encoders and collective decoders. Blocklength tends to infinity at fixed $`E`$ and fixed $`\mu`$ before the high-energy limit is taken.

For a purification $`\psi_{RA}`$ of an input $`\rho_A`$, coherent information is

```math
I_{\mathrm c}(\rho,\mathcal N)
=S(\mathcal N(\rho))
-S\!\left((\mathrm{id}_R\otimes\mathcal N)(\psi_{RA})\right).
```

The second entropy is the entropy exchange: a pure dilation gives the reference-output system and the environment the same nonzero spectrum. A purification is a mathematical way to evaluate the channel's preservation of quantum correlations; introducing it does not grant the sender and receiver free preshared entanglement.

Under the model's hypotheses, [Wilde–Qi](../references/README.md#wilde-qi) gives

```math
Q_\mu(E)
=\lim_{n\to\infty}\frac1n
\sup_{\mathrm{Tr}\rho_{A^n}\sum_jN_j\le nE}
I_{\mathrm c}(\rho_{A^n},\mathcal N_\mu^{\otimes n}).
```

The required finiteness conditions are visible here. The oscillator satisfies
$`\mathrm{Tr}e^{-\beta N}=(1-e^{-\beta})^{-1}\lt\infty`$ for $`\beta\gt0`$. Moreover,

```math
\mathrm{Tr}N\mathcal N_\mu(\rho)
\le E+2\sqrt{EM}+M
\le2E+2M.
```

Finite-energy oscillator states therefore have finite input and output entropy. The thermal maximum-entropy bound can be seen directly from positivity of $`D(\rho\Vert\tau_E)`$: for $`\mathrm{Tr}\rho N\le E`$, expanding the logarithm of the geometric thermal spectrum gives $`S(\rho)\le g(E)`$. These facts make the coherent-information expression well defined and permit the coding theorem's use; an unbounded Hilbert space is not treated as an unspecified finite-dimensional limit.

Evaluating coherent information on one thermal input gives a lower bound on this regularized capacity. The capacity theorem does not require a proof that the thermal state optimizes every blocklength. Nor does it use the degradable-channel simplification associated with §10.3.3.

## Where the displacement-resolution argument enters

### Resolving the law without assuming a density

Let $`Z\sim\mu`$. At resolution $`t`$, define

```math
H_t(\mu)
=H\!\left(\lfloor t\mathrm{Re}Z\rfloor,
           \lfloor t\mathrm{Im}Z\rfloor\right).
```

This is a discrete Shannon entropy, meaningful for atoms, curves, fractal measures and ordinary densities alike. The finite second moment bounds the entropy of the quantized integer vector by comparison with a discrete Gaussian. The classical entropy background does not by itself identify the physically relevant $`t`$; that scale comes from the purified oscillator calculation.

Use a two-mode-squeezed purification of the thermal input, and divide displacement space into squares of side $`\Delta=(E+1)^{-1/2}`$. Conditional on a bin with corner $`c`$, remove $`D(c)`$ and undo the two-mode squeezing. A residual displacement $`w=z-c`$ then becomes a product of coherent states with amplitudes, up to the squeezing sign convention,

```math
-\sqrt E\,\bar w,\qquad\sqrt{E+1}\,w.
```

Their total photon number is bounded by

```math
(2E+1)|w|^2
\le (2E+1)\,2\Delta^2\le4.
```

The transformed conditional mixture consequently has entropy at most $`2g(2)`$. Undoing a unitary preserves entropy, while restoring the bin label costs at most its Shannon entropy. Thus

```math
S(\omega_E^\mu)
\le H_{\sqrt{E+1}}(\mu)+2g(2),
\qquad
Q_\mu(E)\ge g(E)-H_{\sqrt{E+1}}(\mu)-2g(2).
```

This is the local use of purification, Gaussian transformations and entropy inequalities. The binning and its bounded residual energy are proved in the [capacity-law page](../science/02-capacity-law.md#why-one-thermal-input-suffices-for-the-lower-bound); they are additional arguments beyond the textbook foundations.

### Obtaining an upper bound for arbitrary codes

For a smooth noise density $`f`$, the simulation argument compares its channel resource state to that of the entanglement-breaking Gaussian density $`g_1(z)=\pi^{-1}e^{-|z|^2}`$. Classical-to-quantum relative-entropy data processing gives the useful upper bound

```math
Q_f(E)\le D(f\Vert g_1).
```

The relative entropy here is between classical displacement laws. Its connection to quantum communication uses the separable comparison state and the inherited simulation framework; classical data processing alone is insufficient. The simulation limit is taken at fixed finite blocklength and code before the reliable-code sequence is considered. Using local operations and classical communication to construct a converse does not add such resources to the operational definition of $`Q_\mu(E)`$. See the [finite-squeezing argument](../science/03-converse.md#the-simulation-limit-is-taken-for-a-fixed-finite-code).

For a singular law, $`D(\mu\Vert g_1)`$ is infinite and this direct bound is uninformative. Introduce $`f_\sigma`$, the density of $`Z+\sigma G`$. The locally proved classical lower estimate needed for the converse is

```math
h(f_\sigma)
\ge2\log_2\sigma+H_{1/\sigma}(\mu)
   +\log_2(\pi e)-C_{\mathrm{int}},
```

with a universal constant $`C_{\mathrm{int}}`$. The entropy on the left is differential entropy; the entropy on the right is discrete, and $`2\log_2\sigma`$ accounts for the two-dimensional change of scale. The bound is established by controlling the uncertainty of the integer bin after adding unit Gaussian noise, without assigning a differential entropy to the original singular measure.

Smoothing is a channel postprocessing, so by itself it gives $`Q_{f_\sigma}(E)\le Q_\mu(E)`$. To obtain an upper bound on the original capacity, the proof also needs the quantitative continuity estimate. The displacement-generator calculation yields

```math
\frac12\|\mathcal N_\mu-\mathcal N_{f_\sigma}\|_{\diamond,E}
\le\sigma\sqrt{4E+2}.
```

For $`E\ge1`$, taking $`L=\log_2(E+2)`$ and $`\sigma=L^{-2}/\sqrt{4E+2}`$ lets [Winter's theorem](../references/README.md#winter) keep the capacity difference bounded at fixed second-moment bound. Combining this with the entropy estimate yields

```math
A_\mu(E)-2g(2)\le Q_\mu(E)
\le A_\mu(E)+4\log_2\log_2(E+2)+C_M,
\qquad
A_\mu(E)=\log_2(E+1)-H_{\sqrt{E+1}}(\mu).
```

The [converse](../science/03-converse.md) supplies the common output-energy bound, continuity constants and comparison of nonnested grids. The double-logarithmic remainder belongs to this proof; it has not been replaced by a uniform constant for arbitrary laws.

When the information dimension $`d(\mu)`$ exists, the capacity coefficient is $`1-d(\mu)/2`$. The separate [boundedness argument](../science/03-converse.md#when-is-the-unconstrained-capacity-finite) proves

```math
\sup_{E\lt\infty}Q_\mu(E)\lt\infty
\quad\Longleftrightarrow\quad
D(\mu\Vert g_1)\lt\infty.
```

These are different conclusions. A zero logarithmic coefficient does not imply bounded capacity; an absolutely continuous finite-moment law can have differential entropy $`-\infty`$.

## Worked example: a broadened ring versus its Gaussian comparator

Consider one known iid noise law

```math
Z=2e^{i\Theta}+0.01G,
\qquad\Theta\sim\mathrm{Unif}[0,2\pi),
\qquad \Theta\text{ independent of }G.
```

Take a thermal input of mean $`E=100`$. The displacement variance is
$`\mathbb E|Z|^2=4.0001`$, so the added quadrature covariance is $`4.0001I_2`$.

The Gaussian part can first be handled exactly with the Chapter 12 machinery. Put $`v=0.01^2=10^{-4}`$. Applying this noise to one half of the thermal purification gives covariance blocks

```math
A=(E+1/2)I_2,\qquad
B=(E+1/2+v)I_2,\qquad
C=\sqrt{E(E+1)}\mathrm{diag}(1,-1).
```

Its symplectic eigenvalues and entropy are

```math
\nu_\pm=\frac{\sqrt{1+(4E+2)v+v^2}\pm v}{2},
\qquad
S_G=g(\nu_+-1/2)+g(\nu_--1/2).
```

The circular part requires an additional step. Apply a fixed displacement of radius $`r=2`$ and average rotations generated by $`J=N_B-N_R`$. For a pure displaced purification with a fixed displacement $`z`$, the [circle derivation](../science/04-circular-noise.md#exact-entropy-exchange-for-a-thermal-input) gives the charge's characteristic function

```math
\mathbb E[e^{itJ}\mid z]
=\exp\!\left[|z|^2(E+1)(e^{it}-1)
                 +|z|^2E(e^{-it}-1)\right].
```

It is a Skellam law. Its conditional mean is $`|z|^2`$ and conditional variance is $`(2E+1)|z|^2`$. Mixing over the Gaussian displacement and using total variance gives

```math
V_J=(2E+1)(r^2+v)+v^2+2r^2v.
```

Charge averaging increases entropy by at most the charge entropy: coherently record the integer charge in an auxiliary register, then use the entropy triangle inequality. The [integer entropy inequality](../references/README.md#integer-entropy), obtained by adding an independent unit-width uniform variable and maximizing differential entropy at fixed variance, gives

```math
S(\rho_{RB}^{\mathrm{out}})
\le S_G+H(J)
\le S_G+\frac12\log_2[2\pi e(V_J+1/12)].
```

The receiver output is a mixture of displaced thermal states, so entropy concavity gives $`S(\rho_B^{\mathrm{out}})\ge g(E)`$. All ingredients of the achievable rate are now explicit:

| Term | Value |
|---|---:|
| $`g(100)`$ | 8.0937407805 bits |
| $`S_G`$ | 0.1612213484 bits |
| $`V_J`$ | 804.02090001 |
| $`\tfrac12\log_2[2\pi e(V_J+1/12)]`$ | 6.8727149427 bits |
| Coherent-information lower bound | **1.0598044894 qubits/use** |

The [broadening proof](../science/05-broadening.md#a-nonzero-jitter-example) establishes the bound, and the [reproducible calculation](../verification/README.md) evaluates it. Because coherent information is achievable under the stated energy constraint, this certifies a strictly positive unassisted communication rate. The rate does not assert that this input optimizes the finite-energy capacity.

Now replace the noise by a centered Gaussian with the same added covariance. Its complex displacement variance is also $`4.0001`$. Variance one already gives the heterodyne measure-and-prepare channel in these units; larger variance follows it with extra displacement noise. The matched Gaussian is therefore entanglement breaking and has zero quantum capacity. The comparison depends on the full probability law, even though its second moments agree.

The broadened ring itself has a bounded smooth density and finite second moment, so its unrestricted capacity is finite. For an exact ring, the circle's grid entropy instead obeys $`H_t=\log_2t+O_r(1)`$, giving capacity coefficient $`1/2`$. The [joint crossover](../science/05-broadening.md#the-joint-energybroadening-crossover) reconciles the two: for small $`\sigma`$, the effective energy is $`\min(E,\sigma^{-2})`$. Holding positive $`\sigma`$ fixed while increasing $`E`$ eventually reaches saturation; setting $`\sigma=0`$ first gives a different limiting problem.

## What the bridge leaves to the scientific account

The textbook concepts organize the calculations, while the linked scientific pages retain the full hypotheses, constants and limit order. In particular, the non-Gaussian capacity law does not follow from a Gaussian entropy formula, a covariance matrix, or a degradability assertion. Its decisive steps are the bounded entropy inside a displacement bin and the upper bound obtained by combining smoothing, energy-constrained continuity and simulation. The circle and nonzero-jitter example then show how those abstract bounds distinguish physically different noise laws with identical covariance.
