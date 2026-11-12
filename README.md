# Bosonic Noise Dimension

**How does the fine-scale geometry of random phase-space kicks determine an oscillator's quantum communication rate?** For independent, unobserved displacements with a fixed finite-second-moment law, quantum capacity is governed by the entropy of the noise at the resolution reached by the input energy.

Write $`Q_\mu(E)`$ for the ordinary unassisted quantum capacity with an unconditional mean input-photon budget $`E`$ per channel use. For $`Z\sim\mu`$, define

```math
H_t(\mu)=H\!\left(\lfloor t\mathrm{Re}Z\rfloor,
                   \lfloor t\mathrm{Im}Z\rfloor\right).
```

The [finite-resolution theorem](science/02-capacity-law.md) proves, for every $`E\ge1`$,

```math
\begin{aligned}
\log_2(E+1)-H_{\sqrt{E+1}}(\mu)-C_0
&\le Q_\mu(E)\\
&\le\log_2(E+1)-H_{\sqrt{E+1}}(\mu)
 +4\log_2\log_2(E+2)+C_M.
\end{aligned}
```

Here $`C_0`$ is universal, while $`C_M`$ depends only on a bound on the noise second moment. If the Rényi information dimension $`d(\mu)`$ exists, then

```math
\boxed{\displaystyle
\lim_{E\to\infty}\frac{Q_\mu(E)}{\log_2E}
=1-\frac{d(\mu)}2.}
```

The lower bound uses a thermal input. The separate converse applies to arbitrary encoders and collective block decoding; it assumes neither Gaussian-code optimality nor degradability.

## What the law reveals

| Result | Consequence |
|---|---|
| [Circular kicks](science/04-circular-noise.md) of any fixed nonzero radius have information dimension one. | Capacity grows with coefficient $`1/2`$ in front of $`\log_2E`$, despite isotropic noise in both quadratures. |
| A covariance-matched Gaussian channel is entanglement breaking when the mean squared kick amplitude is at least one. | It has zero quantum capacity at every input energy, while the circular channel's capacity diverges. |
| [Gaussian-broadened circular noise](science/05-broadening.md) admits an explicit finite-energy lower bound. | At radius $`r=2`$, input energy $`E=100`$ and jitter width $`\sigma=0.01`$, the bound exceeds **1.05 qubits per use**; the covariance-matched Gaussian remains entanglement breaking. |
| The [bounded-capacity criterion](science/03-converse.md#when-is-the-unconstrained-capacity-finite) uses classical relative entropy to a standard complex Gaussian $`\gamma`$. | $`\sup_E Q_\mu(E)\lt\infty`$ exactly when $`D(\mu\Vert\gamma)\lt\infty`$. Zero information-dimension slope alone does not establish bounded capacity. |

The circle has an exact thermal-input exchange entropy: the entropy of a Skellam distribution with Poisson parameters $`r^2(E+1)`$ and $`r^2E`$. This gives a direct finite-energy calculation in addition to the general asymptotic law.

Fixed nonzero Gaussian jitter smooths the noise and bounds its unlimited-energy capacity. In the small-jitter regime, the useful energy scale is $`E_* = \min\{E,\sigma^{-2}\}`$: the half-logarithmic growth persists up to that scale. The zero-jitter and infinite-energy limits are kept distinct in the [crossover theorem](science/05-broadening.md#the-joint-energybroadening-crossover).

## Read the science

Start with the [scientific overview](science/README.md) and [model](science/01-model.md). The main proof proceeds from [achievability and information dimension](science/02-capacity-law.md) to the [arbitrary-code converse](science/03-converse.md), followed by the [circle](science/04-circular-noise.md) and its [Gaussian broadening](science/05-broadening.md).

The [related-work account](science/06-related-work.md) separates the contribution from earlier bosonic dephasing, non-Gaussian classical communication and channel-simulation results. In particular, the entropy-resolution principle is shared with the pinned [Bosonic Phase Noise Capacity](references/README.md#phase-project) antecedent. The new displacement argument treats noncommuting planar errors and a different energy-dependent resolution. See the [bibliography](references/README.md) for the coding, continuity, simulation and classical-entropy ingredients.

[The LLM reading guide](llms.txt) maps scientific questions to their authoritative pages.

## Learn the mechanism

The [learning route](learning/README.md) connects the physical question to the proof and examples. Its [thirty-milestone map](learning/MILESTONES.md) develops twelve foundation targets and eighteen targets covering the argument and its consequences. The single educational anchor is Holevo's *Quantum Systems, Channels, Information*, second revised and expanded edition (2019); the [source bridge](learning/HOLEVO_BRIDGE.md) translates conventions, identifies the additional research ingredients and works through the nonzero-jitter example.

## Reproduce the finite calculations

From the repository root, run the commands in [verification](verification/README.md). The program evaluates the circular entropy and the nonzero-jitter witness, and checks the charge-distribution formula against a separate finite-Fock calculation. It documents truncation and numerical error controls.

Finite computations verify these examples and conventions. The general capacity theorem and asymptotic statements follow from the analytical proofs and their stated hypotheses.

## Scope

The noise law is fixed and known, with finite second moment; each use draws an independent displacement that is not revealed to either party. The channel contains no photon loss. The photon budget constrains the average encoded input across the whole coding block, without imposing a hard photon cutoff or a per-mode maximum.

The results concern unrestricted asymptotic coding rates. They do not give an efficient encoder, a finite-block error guarantee or an exact finite-energy capacity formula. The simulator's squeezing is an auxiliary tool in the converse, not a resource supplied to the communicating parties.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
