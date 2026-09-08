# Architecture

## Layers

1. **Quantities** — dimensions, units, constants, frames and conversions.
2. **Numerical contract** — precision modes, tolerances, reproducibility, error/evidence representation.
3. **Core mechanics** — vectors, kinematics, forces, energy, momentum, rigid bodies and constraints.
4. **Scientific domains** — thermodynamics, electromagnetics, optics, orbital/particle foundations.
5. **Solvers** — integration, root solving, constraints and domain-specific numerical methods.
6. **Verification** — invariants, analytic/reference cases, cross-backend comparison and convergence studies.
7. **Adapters** — integration with `mncs-engine` and other MNCS systems without coupling scientific kernels to application policy.

## First milestones

1. Units/constants and numeric contract.
2. Vector mechanics plus validated integrators.
3. Conservation-law test corpus.
4. Rigid-body and constraint foundations.
5. CPU/CUDA reproducibility and tolerance harness.
6. Additional scientific domains driven by verified reference cases.
