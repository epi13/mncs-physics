# RFC 0001: Scientific physics foundation

Status: Draft

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
