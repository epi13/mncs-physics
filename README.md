# mncs-physics

Scientifically accurate machine-native physics for MNCS.

`mncs-physics` is a reusable scientific physics substrate for systems such as `mncs-engine`, robotics, simulation, digital twins, and scientific workloads. It is also a deliberate low-level correctness and numerical-precision pressure project for `mncs-language`.

## Initial scope

- physical quantities, dimensions, units, and constants
- classical mechanics and rigid-body foundations
- numerical integration and dynamical systems
- thermodynamic, electromagnetic, optical, and orbital foundations
- conservation-law and reference-case verification
- CPU/GPU execution with explicit numerical contracts
- reproducibility, tolerances, uncertainty, and evidence

## Design direction

Scientific correctness outranks convenience. Fast/approximate execution may exist, but it must be explicit and must not silently weaken strict, reproducible, or validated modes.

## Repository layout

- `docs/ARCHITECTURE.md` — layers and staged build plan
- `docs/rfcs/0001-foundation.md` — foundational scientific-computing contract
- `docs/LANGUAGE_PRESSURES.md` — MNCS language/compiler/runtime pressure ledger
- `AGENTS.md` — contributor and agent operating contract
