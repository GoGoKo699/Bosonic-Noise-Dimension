#!/usr/bin/env python3
"""Reproduce finite examples and independent Fock-space checks.

Run from the repository root:
    python3 verification/verify_examples.py

The scalar witness is an evaluation of an analytic lower bound. Finite Fock and
quadrature calculations are numerical consistency checks, not capacity proofs.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.special import logsumexp
from scipy.stats import poisson, skellam


LOG2 = math.log(2.0)


def g(x: float) -> float:
    """Thermal entropy in bits; stable at large x and continuous at zero."""
    if x < -1e-13:
        raise ValueError(f"Negative thermal occupation: {x}")
    if x <= 0:
        return 0.0
    return (math.log1p(x) + x * math.log1p(1.0 / x)) / LOG2


def entropy(weights: np.ndarray) -> float:
    p = np.asarray(weights, dtype=float)
    if np.min(p, initial=0.0) < -2e-12:
        raise AssertionError("A numerical probability/eigenvalue is negative")
    p = p[p > 0]
    return float(-np.dot(p, np.log2(p)))


def jitter_bound(E: float, r: float, sigma: float) -> dict:
    v = sigma * sigma
    # Evaluate sqrt(1+x)-1 as x/(sqrt(1+x)+1).
    x = (4 * E + 2) * v + v * v
    root_minus_one = x / (math.sqrt(1 + x) + 1)
    n_plus = (root_minus_one + v) / 2
    n_minus = (root_minus_one - v) / 2
    S_G = g(n_plus) + g(n_minus)
    variance = (2 * E + 1) * (r * r + v) + v * v + 2 * r * r * v
    H_upper = 0.5 * math.log2(2 * math.pi * math.e * (variance + 1 / 12))
    lower = g(E) - S_G - H_upper
    return {
        "input_energy": E,
        "circle_radius": r,
        "gaussian_amplitude_scale": sigma,
        "gaussian_mean_squared_amplitude": v,
        "thermal_entropy_bits": g(E),
        "gaussian_entropy_exchange_bits": S_G,
        "charge_variance": variance,
        "charge_entropy_upper_bits": H_upper,
        "coherent_information_lower_bits": lower,
        "achievable_rate_lower_bits": max(0.0, lower),
        "matched_gaussian_mean_squared_amplitude": r * r + v,
        "matched_gaussian_is_entanglement_breaking": r * r + v >= 1,
    }


def log_chernoff_right(a: float, b: float, threshold: int) -> float:
    """log upper bound for Pr[Pois(a)-Pois(b) >= threshold]."""
    if threshold <= a - b:
        return 0.0
    if a == 0:
        return -math.inf if threshold > 0 else 0.0
    if b == 0:
        u = threshold / a
    else:
        u = (threshold + math.hypot(threshold, 2 * math.sqrt(a * b))) / (2 * a)
    t = math.log(u)
    return min(0.0, a * math.expm1(t) + b * math.expm1(-t) - threshold * t)


def skellam_entropy(E: float, r: float) -> dict:
    """Finite PMF sum with analytic bounds on its omitted mass and entropy.

    If omitted mass is p and the full second moment is M2, its entropy
    contribution is at most -p log2 p + p/2 log2(2*pi*e*(M2/p+1/12)).
    The returned analytic bound excludes floating-point evaluation errors.
    """
    a, b = r * r * (E + 1), r * r * E
    mean, variance = a - b, a + b
    second_moment = variance + mean * mean
    cutoff = max(8, math.ceil(abs(mean) + 9 * math.sqrt(variance + 1) + 20))
    while True:
        log_tail = float(logsumexp([
            log_chernoff_right(a, b, cutoff + 1),
            log_chernoff_right(b, a, cutoff + 1),
        ]))
        if log_tail < math.log(1e-18):
            break
        cutoff = math.ceil(1.25 * cutoff + 8)
    tail_upper = max(math.exp(log_tail), 1e-300)
    k = np.arange(-cutoff, cutoff + 1)
    if b == 0:
        probabilities = poisson.pmf(k, a)
    else:
        probabilities = skellam.pmf(k, a, b)
    H_partial = entropy(probabilities)
    tail_entropy_upper = (
        -tail_upper * math.log2(tail_upper)
        + 0.5 * tail_upper
        * math.log2(2 * math.pi * math.e * (second_moment / tail_upper + 1 / 12))
    )
    H_variance = 0.5 * math.log2(2 * math.pi * math.e * (variance + 1 / 12))
    if abs(float(np.sum(probabilities)) - 1.0) > 3e-10:
        raise AssertionError("PMF normalization outside floating-point tolerance")
    if H_partial > H_variance + 3e-10:
        raise AssertionError("Skellam entropy exceeds the analytic variance bound")
    return {
        "input_energy": E,
        "circle_radius": r,
        "lambda_plus": a,
        "lambda_minus": b,
        "symmetric_integer_cutoff": cutoff,
        "retained_probability": float(np.sum(probabilities)),
        "omitted_probability_upper": tail_upper,
        "omitted_entropy_upper_bits": tail_entropy_upper,
        "entropy_partial_bits": H_partial,
        "variance_entropy_upper_bits": H_variance,
        "thermal_coherent_information_lower_bits": g(E) - H_partial - tail_entropy_upper,
    }


def thermal_probabilities(E: float, dimension: int) -> tuple[np.ndarray, float]:
    if E == 0:
        p = np.zeros(dimension)
        p[0] = 1
        return p, 0.0
    q = E / (E + 1)
    p = (1 - q) * q ** np.arange(dimension)
    omitted = q ** dimension
    return p / np.sum(p), omitted


def displacement_matrix(dimension: int, z: complex, cache: dict | None = None) -> np.ndarray:
    """Independent truncated-oscillator exponential, not a Skellam formula."""
    radius = abs(z)
    if cache is not None and radius in cache:
        real_displacement = cache[radius]
    else:
        annihilation = np.diag(np.sqrt(np.arange(1, dimension)), 1)
        real_displacement = expm(radius * (annihilation.T - annihilation))
        if cache is not None:
            cache[radius] = real_displacement
    indices = np.arange(dimension)
    theta = math.atan2(z.imag, z.real) if radius else 0.0
    return np.exp(1j * theta * (indices[:, None] - indices[None, :])) * real_displacement


def check_fock_charge(E: float, r: float, dimension: int) -> dict:
    p, omitted = thermal_probabilities(E, dimension)
    D = displacement_matrix(dimension, complex(r))
    # Rows index the receiver photon number, columns the reference number.
    amplitudes = D * np.sqrt(p)[None, :]
    receiver, reference = np.indices((dimension, dimension))
    charge = receiver - reference
    weights = np.bincount(
        (charge + dimension - 1).ravel(),
        weights=(np.abs(amplitudes) ** 2).ravel(),
        minlength=2 * dimension - 1,
    )
    k = np.arange(1 - dimension, dimension)
    a, b = r * r * (E + 1), r * r * E
    expected = skellam.pmf(k, a, b) if b else poisson.pmf(k, a)
    l1 = float(np.sum(np.abs(weights - expected)) + max(0.0, 1 - np.sum(expected)))
    mean = float(np.dot(k, weights))
    variance = float(np.dot((k - mean) ** 2, weights))
    if l1 > 1e-8:
        raise AssertionError(f"Fock charge distribution failed: L1={l1}")
    if abs(mean - r * r) > 2e-8:
        raise AssertionError("Fock charge mean disagrees with the displacement convention")
    return {
        "input_energy": E,
        "circle_radius": r,
        "fock_dimension_per_mode": dimension,
        "omitted_input_thermal_probability": omitted,
        "fock_vs_skellam_l1_difference": l1,
        "fock_charge_mean": mean,
        "fock_charge_variance": variance,
        "analytic_charge_variance": a + b,
    }


def fock_broadened_circle(E: float, r: float, sigma: float, dimension: int, order: int) -> dict:
    """Gauss-Hermite displacement integration plus exact finite charge twirl.

    This constructs all charge-sector density matrices from oscillator
    displacement exponentials. It does not use the Skellam identity or the
    Gaussian symplectic-entropy formula to construct the state.
    """
    p, omitted = thermal_probabilities(E, dimension)
    nodes, weights = np.polynomial.hermite.hermgauss(order)
    receiver, reference = np.indices((dimension, dimension))
    charge = receiver - reference
    sectors = [np.where(charge == k) for k in range(1 - dimension, dimension)]
    blocks = [np.zeros((len(rows), len(rows)), complex) for rows, _ in sectors]
    output_probabilities = np.zeros(dimension)
    cache: dict = {}
    for i, x in enumerate(nodes):
        for j, y in enumerate(nodes):
            weight = float(weights[i] * weights[j] / math.pi)
            z = r + sigma * complex(x, y)
            D = displacement_matrix(dimension, z, cache)
            amplitudes = D * np.sqrt(p)[None, :]
            output_probabilities += weight * ((np.abs(D) ** 2) @ p)
            for block, (rows, cols) in zip(blocks, sectors):
                vector = amplitudes[rows, cols]
                block += weight * np.outer(vector, vector.conjugate())
    eigenvalues = np.concatenate([np.linalg.eigvalsh(block) for block in blocks])
    S_exchange = entropy(eigenvalues)
    S_output = entropy(output_probabilities)
    numerical_ic = S_output - S_exchange
    analytic = jitter_bound(E, r, sigma)
    if numerical_ic < analytic["coherent_information_lower_bits"] - 2e-7:
        raise AssertionError("Independent Fock coherent information violates the lower bound")
    return {
        "input_energy": E,
        "circle_radius": r,
        "gaussian_amplitude_scale": sigma,
        "fock_dimension_per_mode": dimension,
        "hermite_order_per_real_component": order,
        "omitted_input_thermal_probability": omitted,
        "computed_trace": float(np.sum(eigenvalues)),
        "computed_entropy_exchange_bits": S_exchange,
        "computed_receiver_entropy_bits": S_output,
        "computed_coherent_information_bits": numerical_ic,
        "analytic_coherent_information_lower_bits": analytic["coherent_information_lower_bits"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()

    witness = jitter_bound(100.0, 2.0, 0.01)
    if witness["achievable_rate_lower_bits"] <= 1.05:
        raise AssertionError("The finite-jitter witness no longer certifies 1.05 qubits/use")
    if not witness["matched_gaussian_is_entanglement_breaking"]:
        raise AssertionError("The matched Gaussian is outside the claimed EB region")

    circle_table = [skellam_entropy(E, 2.0) for E in (0.0, 1.0, 10.0, 100.0, 1000.0)]
    fock_checks = [
        check_fock_charge(0.4, 0.7, 48),
        check_fock_charge(1.0, 1.1, 80),
    ]
    jitter_checks = [
        fock_broadened_circle(1.0, 0.4, 0.1, 40, 8),
        fock_broadened_circle(1.0, 0.4, 0.1, 48, 12),
    ]
    convergence = abs(
        jitter_checks[0]["computed_coherent_information_bits"]
        - jitter_checks[1]["computed_coherent_information_bits"]
    )
    if convergence > 2e-7:
        raise AssertionError(f"Fock/quadrature refinement did not converge: {convergence}")

    # At r=0 the independently integrated state is Gaussian, furnishing a
    # separate check of the vacuum-noise and symplectic-eigenvalue conventions.
    gaussian_check = fock_broadened_circle(0.5, 0.0, 0.25, 32, 12)
    gaussian_exact_entropy = jitter_bound(0.5, 0.0, 0.25)["gaussian_entropy_exchange_bits"]
    gaussian_entropy_difference = abs(
        gaussian_check["computed_entropy_exchange_bits"] - gaussian_exact_entropy
    )
    if gaussian_entropy_difference > 2e-7:
        raise AssertionError("Direct Gaussian mixture and symplectic entropy disagree")

    result = {
        "status": "passed",
        "conventions": {
            "displacement": "D(z)=exp(z a†-conj(z) a)",
            "standard_complex_gaussian": "density exp(-|z|^2)/pi; E|G|^2=1",
            "capacity_energy": "unconditional mean input photon number per use",
            "entropy_unit": "bits",
        },
        "finite_jitter_witness": witness,
        "circle_entropy_table": circle_table,
        "independent_fock_charge_checks": fock_checks,
        "independent_broadened_circle_checks": jitter_checks,
        "broadened_circle_refinement_difference_bits": convergence,
        "gaussian_entropy_check": gaussian_check,
        "gaussian_exact_entropy_exchange_bits": gaussian_exact_entropy,
        "gaussian_entropy_difference_bits": gaussian_entropy_difference,
        "limits": [
            "The asymptotic capacity theorems are analytic, not numerical conclusions.",
            "The Skellam omitted-tail bound is analytic; floating-point errors are separate.",
            "Fock-space and quadrature refinement are numerical checks, not rigorous truncation certificates.",
            "No numerical optimization of regularized quantum capacity is performed.",
        ],
    }
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
