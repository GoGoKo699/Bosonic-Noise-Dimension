# Reproducing the finite examples

[Overview](../README.md) · [Circular noise](../science/04-circular-noise.md) · [Gaussian broadening](../science/05-broadening.md)

The scientific statements are proved analytically. The program here reproduces the finite-jitter rate and checks the displacement, charge, and Gaussian conventions through independent finite-dimensional calculations.

## Run

The recorded output was produced with Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. Use Python 3.11 or later for the pinned package versions. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_examples.py
```

To retain the machine-readable output:

```bash
python3 verification/verify_examples.py --output verification/example_results.json
```

The script exits unsuccessfully if a declared numerical check fails. The calculations use only Python's standard library, NumPy, and SciPy. No dataset, network connection, random seed, or specialized quantum package is required.

## What is checked

| Calculation | Scientific issue addressed |
|---|---|
| Closed-form broadened-circle lower bound | Reproduces the positive finite-energy, nonzero-jitter rate and the covariance-matched entanglement-breaking Gaussian comparison. |
| Skellam entropy at several input energies | Checks the exact charge probabilities, handles the Poisson boundary at zero input energy, and bounds the omitted probability and entropy analytically. |
| Displacement-matrix calculations in finite Fock spaces | Constructs the purified state directly, then compares its charge probabilities to the Skellam formula; this checks signs, factors of two, and the reference charge. |
| Gaussian quadrature of actual displacement matrices, followed by charge twirling | Computes a broadened-circle coherent information independently of the entropy upper bound; refines both the Fock cutoff and quadrature order. |
| Zero-radius Gaussian specialization | Compares the directly integrated state's entropy to the two-mode symplectic-eigenvalue expression. |

For the highlighted witness, the script evaluates

```math
r=2,\qquad E=100,\qquad\sigma=0.01,
\qquad Q_{r,\sigma}(E)\ge1.0598044893\ldots
```

The Gaussian amplitude scale obeys $`\mathbb E|\sigma G|^2=\sigma^2`$. It is not the variance of a single real component. The matched Gaussian has added mean photon number $`4.0001`$, above the entanglement-breaking threshold of one in this convention.

## Entropy-tail control

For the exact circular channel, the script sums the Skellam probabilities over a finite integer range. It bounds the two omitted tails with the Chernoff moment-generating function, rather than estimating them from a normal approximation.

If the omitted probability is $`p`$ and the full second moment of the integer charge is $`M_2`$, the omitted entropy is at most

```math
-p\log_2p+
\frac p2\log_2\!\left[2\pi\mathrm e
\left(\frac{M_2}{p}+\frac1{12}\right)\right].
```

This follows by applying the integer entropy bound to the conditional tail law and using its second moment at most $`M_2/p`$. The script reports the analytic tail allowance separately from the finite floating-point sum. That allowance is not a certificate for floating-point rounding errors.

## Interpretation of the output

The finite-jitter rate is an achievable lower bound supplied by the [analytical proof](../science/05-broadening.md). The program evaluates its terms; it does not construct a capacity-achieving encoder or establish a finite-blocklength error guarantee.

The Fock-space and Gaussian-quadrature checks are finite numerical consistency checks. Increasing both resolutions tests a concrete truncation concern, but the observed agreement is not a rigorous infinite-dimensional simulation error bound. It also does not certify the general capacity converse, information-dimension law, or joint crossover. Those conclusions depend on the mathematical arguments in `science/`.

The program never labels a single-input coherent information as an optimized capacity. Negative coherent-information lower bounds are retained in the detailed output and clipped to zero only when reporting an achievable nonnegative rate.
