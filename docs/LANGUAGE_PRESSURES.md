# MNCS language pressure ledger

Record each discovered pressure with workload, current behavior, required semantic, reproducer, likely owning repo, workaround and verification needed to close it.

## Initial pressure targets

- dimensioned quantities and compile-time unit algebra
- strict and reproducible floating-point semantics
- NaN, infinity, signed-zero and subnormal behavior
- FMA/reassociation and optimization control
- deterministic parallel reductions
- generic scalar/vector/matrix abstractions without performance collapse
- SIMD and CUDA-friendly layouts
- arbitrary/high precision and interval arithmetic integration
- structured solver convergence/error reporting
- cross-backend reproducibility and ULP/tolerance comparison
- compile-time constants and reference-frame typing

A pressure item remains open until the real scientific workload works cleanly without relying on an undocumented semantic compromise.
