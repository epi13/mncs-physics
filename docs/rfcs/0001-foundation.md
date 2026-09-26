# RFC 0001: Scientific physics foundation

Status: Partially implemented (foundation 2026-09-26)

## Purpose

Define the correctness model for `mncs-physics` before broad implementation.

## Core contracts

- Physical quantities carry dimensions and units through computation.
- Numerical behavior is selectable and inspectable: fast, reproducible, strict, and eventually validated/bounded modes should not be conflated.
- Solvers expose tolerance, convergence, iteration and failure information.
- Results intended for scientific use include enough evidence to reproduce and validate the computation.
- Conservation laws and known invariants are first-class tests.
- CPU/GPU acceleration must preserve the declared numerical contract.

## Initial pressure objectives

Units at compile time, generic numeric types, vector/tensor ergonomics, deterministic reductions, IEEE behavior, FMA/reassociation control, high-precision types, interval/error bounds, structured solver failures, CUDA parity and efficient memory layouts.

## Non-goals

This repository is not a game-physics shortcut layer and does not initially attempt every branch of physics. Breadth follows verified foundations.

## Implementation record (foundation 2026-09-26)

Retained: quantities carry dimensions through computation (runtime
`Dim` vectors + outcome enums); precision/tolerance discipline
consumed from Numerics (`approx`, `safe_div`, `sqrt_newton`);
conservation as first-class tests (bitwise free-motion, work-energy);
reference-data provenance on constants (SI Brochure 9e / CODATA 2022).

Redesigned: compile-time unit algebra → runtime structural checks
(P-PHYSICS-DIM); generic numeric-type polymorphism → concrete f64
quantities with i64 exponents; universal `PhysicalSystem`/
interaction taxonomy → one concrete `Body1` + checked relations;
solver-tolerance framework → per-relation outcome enums.

Delegated: numeric representation to Numerics; vector algebra to
Geometry (via `Vec2`); test execution to mncs-test.

Excluded: rigid bodies, thermo/EM/optics/orbital equations,
uncertainty arithmetic, Store/Lineage integration, cross-backend
claims — each with a pressure or boundary note, not silent omission.
