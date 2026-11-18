# Bosonic Noise Dimension

**How does the fine-scale geometry of random phase-space kicks determine an oscillator's quantum communication rate?** For independent, unobserved displacements with a fixed finite-second-moment law, both ordinary and two-way-assisted quantum capacity are determined, to bounded additive error, by the entropy of the noise at the resolution reached by the input energy.

Write $`Q_\mu(E)`$ for ordinary quantum capacity and $`Q_{2,\mu}(E)`$ for capacity with adaptive local operations and unlimited two-way classical communication. Both use an unconditional mean input-photon budget $`E`$ per channel use, and start with no preshared entanglement. For $`Z\sim\mu`$, define

```math
H_t(\mu)=H\!\left(\lfloor t\mathrm{Re}Z\rfloor,
                   \lfloor t\mathrm{Im}Z\rfloor\right),
\qquad
A_\mu(E)=\log_2(E+1)-H_{\sqrt{E+1}}(\mu).
```

For every $`E\ge1`$, the [finite-resolution theorem](science/02-capacity-law.md) gives

```math
\boxed{
A_\mu(E)-C_0
\le Q_\mu(E)
\le Q_{2,\mu}(E)
\le A_\mu(E)+C_M.
}
```

Here $`C_0`$ is universal, and $`C_M`$ depends only on a bound on the noise second moment. A thermal input gives the lower bound. The [adaptive converse](science/03-converse.md#adaptive-converse-at-the-energy-resolution) compares an energy-matched smoothed channel to a separable Gaussian reference and bounds the entanglement lost to smoothing by a constant per use.

If the Rényi information dimension $`d(\mu)`$ exists, then both capacities have the same leading coefficient.

```math
\lim_{E\to\infty}\frac{Q_\mu(E)}{\log_2E}
=\lim_{E\to\infty}\frac{Q_{2,\mu}(E)}{\log_2E}
=1-\frac{d(\mu)}2.
```

## What the law reveals

| Result | Consequence |
|---|---|
| [Circular kicks](science/04-circular-noise.md) of any fixed nonzero radius have information dimension one. | Both capacities grow as half the logarithm of energy up to bounded error, despite isotropic noise in both quadratures. |
| The centered, covariance-matched Gaussian channel is entanglement breaking when the circle's squared kick radius is at least one. | Both Gaussian-channel capacities vanish at every input energy, while the circular channel's capacities diverge. |
| [Gaussian-broadened circular noise](science/05-broadening.md) admits an explicit finite-energy lower bound. | At radius $`r=2`$, input energy $`E=100`$ and jitter width $`\sigma=0.01`$, the unassisted achievable rate exceeds **1.05 qubits per use**. The covariance-matched Gaussian remains entanglement breaking. |
| A [bounded-support, absolutely continuous noise law](science/02-capacity-law.md#a-full-dimensional-noise-density-with-unbounded-capacity) has information dimension two. | Both capacities diverge as $`\Theta(\log_2\log_2\log_2 E)`$. |
| The [bounded-capacity criterion](science/03-converse.md#when-is-the-unconstrained-capacity-finite) uses relative entropy to a standard complex Gaussian $`\gamma`$. | The energy-unconstrained capacities are finite exactly when $`D(\mu\Vert\gamma)\lt\infty`$. |

The circular channel has an exact thermal-input exchange entropy. It equals the entropy of a Skellam distribution with Poisson parameters $`r^2(E+1)`$ and $`r^2 E`$.

The [Gaussian-broadening theorem](science/05-broadening.md#the-general-energybroadening-crossover) applies to every admissible base law. For $`E\ge1`$ and independent complex Gaussian jitter of variance $`b=\sigma^2\in[0,1]`$, the resolution for both capacities is $`t_{\mathrm{eff}}=(b+(E+1)^{-1})^{-1/2}`$. Their common estimate, up to bounded error, is $`2\log_2 t_{\mathrm{eff}}-H_{t_{\mathrm{eff}}}(\mu)`$. For a circle this gives the half-logarithmic law at effective energy $`\min\{E,\sigma^{-2}\}`$, with a finite ceiling at fixed positive jitter.

## Read the science

Start with the [scientific overview](science/README.md) and [model](science/01-model.md). The proof proceeds from [thermal achievability and information dimension](science/02-capacity-law.md) to the [adaptive converse](science/03-converse.md), followed by the [circle](science/04-circular-noise.md) and [Gaussian broadening](science/05-broadening.md).

The [related-work account](science/06-related-work.md) credits earlier bosonic dephasing, non-Gaussian communication and channel simulation. The entropy-resolution principle is shared with the pinned [Bosonic Phase Noise Capacity](references/README.md#phase-project) antecedent. The displacement argument treats noncommuting planar errors with a different energy-dependent resolution. The [bibliography](references/README.md) identifies the imported coding, entanglement and classical-entropy results.

[The LLM reading guide](llms.txt) maps scientific questions to their authoritative pages.

## Learn the mechanism

The [learning route](learning/README.md) connects the physical question to the proof and examples. Its [thirty-milestone map](learning/MILESTONES.md) develops twelve foundation targets and eighteen targets covering the argument and its consequences. The single educational anchor is Holevo's *Quantum Systems, Channels, Information*, second revised and expanded edition (2019). The [source bridge](learning/HOLEVO_BRIDGE.md) translates conventions, identifies the additional research ingredients and works through the nonzero-jitter example.

## Reproduce the finite calculations

From the repository root, run the commands in [verification](verification/README.md). The program evaluates the circular entropy and the nonzero-jitter witness, and checks the charge-distribution formula against a separate finite-Fock calculation. It documents truncation and numerical error controls. The general capacity law follows from the analytical proofs.

## Scope

The noise law is fixed and known, with finite second moment. Each channel use draws an independent hidden displacement. The model treats additive noise without photon loss. The photon budget constrains the mean encoded input across channel uses, averaging over adaptive histories when applicable. The capacities describe unrestricted asymptotic communication rates.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
