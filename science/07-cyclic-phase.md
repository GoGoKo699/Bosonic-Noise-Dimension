# Weak displacement with a growing cyclic phase alphabet

[Scientific account](README.md) · [Gaussian broadening](05-broadening.md) · [Capacity theorem in Discrete Phase Loss Capacity](https://github.com/GoGoKo699/Discrete-Phase-Loss-Capacity/blob/16be1722f0b2b9a1a020f6d74b37a7a7824d2f11/science/critical-displacement.md)

The displacement-resolution law describes an oscillator subject to additive kicks alone. Add an independent cyclic phase twirl before the kicks, and two channels with identical photon-number transition probabilities can have different capacities. In this comparison the missing information is the overlap between the environment states that produce the same net shift.

## From logarithmic growth to a finite rate

Use one oscillator per channel use, with independent, hidden noise on each use. Choose a phase uniformly from the $`J`$ rotations by integer multiples of $`2\pi/J`$, apply pure loss of transmissivity $`\eta_J`$, and then apply an isotropic Gaussian displacement $`Z_J`$ with $`b_J=\mathbb E\lvert Z_J\rvert^2`$. In the convention of the [model](01-model.md), $`b_J`$ is the photon number the displacement adds to vacuum. The mean input budget $`E=eJ`$ averages over all channel uses and adaptive histories. The coding limit is taken at each fixed $`J`$.

With Gaussian displacement alone, take the base law $`\mu=\delta_0`$ in the [broadening crossover](05-broadening.md#the-general-energybroadening-crossover). Its grid entropy is zero at every resolution. If $`Jb_J\to\beta`$ for finite $`\beta\ge0`$ and $`e\gt 0`$, the resulting ordinary and two-way-assisted quantum capacities grow as

```math
\log_2\!\left(\frac{1}{b_J+(eJ+1)^{-1}}\right)+O(1)
=\log_2 J+O(1).
```

With the cyclic phase twirl and $`J(1-\eta_J)\to\lambda`$ for finite $`\lambda\ge0`$, the [companion theorem](https://github.com/GoGoKo699/Discrete-Phase-Loss-Capacity/blob/16be1722f0b2b9a1a020f6d74b37a7a7824d2f11/science/critical-displacement.md) gives a finite common limit for the ordinary quantum, two-way entanglement-generation and two-way secret-key capacities. This includes the comparison at exactly zero physical loss. The phase twirl removes coherence between input residues modulo $`J`$, so a code can fix the residue and carry quantum data in the photon-number quotient instead.

## What the shift discards

Use the attenuator–amplifier representation of additive Gaussian noise. After including physical loss, the attenuator has transmissivity $`\tau_J=\eta_J/(1+b_J)`$ and the amplifier has gain $`1+b_J`$. Write a photon number $`n`$ as $`JU+r`$, where $`r`$ is the input residue. At $`n/J\to x=A+U`$, with $`A`$ the normalized residue, the attenuation and amplification counts tend to conditionally independent Poisson variables,

```math
L\sim\operatorname{Pois}((\lambda+\beta)x),\qquad
G\sim\operatorname{Pois}(\beta x),\qquad
S=G-L.
```

A receiver that knows the input residue can measure the output residue to obtain $`S\bmod J`$. The uncertainty about the exact shift vanishes uniformly under the mean budget in this window. The environment still has a vector in the subspace for each shift. Its subnormalized form is

```math
v_s(x)=
\sum_{g-l=s}\sqrt{\Pr(L=l\mid x)\Pr(G=g\mid x)}\,\lvert l,g\rangle .
```

The squared norm gives $`\Pr(S=s\mid x)`$. The direction also matters. For zero shift, the ratio of the $`\lvert 1,1\rangle`$ amplitude to the $`\lvert 0,0\rangle`$ amplitude is $`x\sqrt{(\lambda+\beta)\beta}`$. Thus at positive displacement variance scale, two different inputs leave different environment states even when both induce zero shift. The overlap of their environment vectors controls how much of the input coherence survives at the receiver. Photon-number transition probabilities reveal only the squared norms.

One can construct a comparison channel with the same photon-number transitions. For each input residue and net shift, use a single operator that translates each number state by that shift with amplitude $`\sqrt{\Pr(S=s\mid n)}`$, using the exact finite-$`J`$ probabilities. The comparison environment records just the residue and shift. The companion theorem gives the following optimized limits:

| Channel after the cyclic phase twirl | Common capacity limit |
|---|---|
| Gaussian displacement with optional weak physical loss | $`\sup_{\mathbb E[A+U]\le e} H(U\mid A,S,\mathsf E)`$ |
| Comparison channel with the same Fock transition probabilities | $`\sup_{\mathbb E[A+U]\le e} H(U\mid A,S)`$ |

The register $`\mathsf E`$ represents the conditional quantum environment within each shift. For $`e\gt 0`$ and $`\beta\gt 0`$, the first optimum is strictly smaller. The two expressions coincide when $`\beta=0`$. In that case each shift corresponds to a single loss count, and the limit reduces to the pure-loss Poisson formula. [Proof and energy-tail control](https://github.com/GoGoKo699/Discrete-Phase-Loss-Capacity/blob/16be1722f0b2b9a1a020f6d74b37a7a7824d2f11/science/critical-displacement.md)

## A binary example

Take equal probabilities on input photon numbers zero and $`J`$, with $`e=1/2`$, $`\lambda=0`$ and $`\beta=1/2`$. In the limit, any nonzero shift identifies the input as the upper number state. At zero shift the probability of the shift given the upper input is $`p=\mathrm e^{-1}I_0(1)`$, where $`I_0`$ is the modified Bessel function. The two normalized zero-shift environment vectors have squared overlap $`1/I_0(1)`$. Their binary mixture has positive entropy, which subtracts from the shift-only rate.

| Fixed-input rate contribution | Bits per use |
|---|---:|
| Residual uncertainty given the shift | 0.661005 |
| Conditional quantum environment information | 0.203142 |
| Limiting coherent information | 0.457863 |

This calculation evaluates one prior. The [reproducible check](../verification/README.md#cyclic-phase-comparison) computes the small environment spectrum independently of the limiting optimization. The strict comparison of optimized capacities follows from the proof in the phase-loss project.

## What transfers from the displacement law

The common displacement convention identifies the same physical scale in both problems. At linear energy, inverse alphabet size is comparable to the variance of the resolution imposed by the carrier. In the displacement-only problem the grid law describes the capacity to an additive constant. Under the growing phase twirl the capacity itself stays finite, and overlaps inside the shift subspaces determine its value. The phase-loss proof handles those overlaps with a shift flag for the upper bound and a physical modular measurement for the lower bound.

Gaussian attenuator–amplifier operator sums are due to [Ivan, Sabapathy and Simon](../references/README.md#ivan-sabapathy-simon). The relative-entropy comparison with complete dephasing for number-preserving noise is due to [Arqand and Smith](../references/README.md#arqand-smith). The companion theorem extends that comparison through a shift-resolved channel, then controls the cost of the flag using the residue structure.
