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

1. Units/constants and numeric contract — DONE (foundation
   2026-09-26: dimensions, units, quantities, pinned constants;
   numeric contract consumed from Numerics, not re-owned).
2. Vector mechanics plus validated integrators — HALF DONE
   (checked scalar/vector mechanics + constant-force slice verified;
   no general integrator suite; rigid bodies not started).
3. Conservation-law test corpus — STARTED (bitwise free-motion
   conservation, work-energy agreement; no universal framework).
4. Rigid-body and constraint foundations — DEFERRED (no workload).
5. CPU/CUDA reproducibility and tolerance harness — DEFERRED
   (single-backend slice; no cross-backend claims).
6. Additional scientific domains driven by verified reference
   cases — INTENTIONALLY OUT (thermo/EM/optics/orbital stay in
   specialized repositories; Physics keeps unit/dimension names
   for fixtures only).

See `docs/PHYSICS_MODEL.md` for the ownership boundary and
`docs/VERIFICATION.md` for what the foundation proves.
