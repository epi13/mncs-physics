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

## Discovered pressures (foundation campaign, 2026-09-26)

### P-PHYSICS-DIM — no type-level dimension algebra (non-blocking)

Workload: `Quantity<Length, f64>`-style static dimensional typing.
Current behavior: dimensions are runtime `Dim` records; `q_add` of
force and energy returns `BadDim` data instead of a compile error.
Required semantic: exponent arithmetic visible to the type checker.
Reproducer: `src/physics/dim.mncs` + `src/physics/quantity.mncs`.
Likely owner: mncs-language. Workaround: nominal `Quantity` type
plus outcome enums (honest, tested). Verification to close: a
`Quantity<D, T>` spelling that rejects `add(force, energy)` before
execution. Note: this is the same gap behind P-FLUID-UNITS and
P-ATOMIC-UNITS — one language fix serves all three.

### P-PHYSICS-POW — general integer powers inexpressible (non-blocking)

Workload: `q_pow(q, k: i64)` over quantities.
Current behavior: MNE130 rejects the countdown recursion
(observed while building `quantity.mncs`: "recursive call cycles
are rejected"); `iterate x up_to N` requires a literal bound, so no
exponent-driven loop either.
Reproducer: removed `q_pos_pow`/`q_inv_pow` (see module comment).
Likely owner: mncs-language. Workaround: named `q_pow2`/`q_pow3`/
`q_inv` compositions — exactly the powers the slice needs, nothing
more. Verification to close: bounded iteration over a dynamic count
or admitted structural recursion on integers.

### P-PHYSICS-VEC — nested generic composition untested (non-blocking)

Workload: `Vector<Quantity<Force>>`-style nesting of semantic types
over generic containers.
Current behavior: not attempted; one nominal wrapper per physical
vector kind (`Disp2/Vel2/Acc2/Force2/Mom2` in `vecmech.mncs`).
The set is small (5) and each operation is explicit, but every new
kind needs a new record — the manual-enumeration smell the mission
warns about, kept minimal rather than generated.
Likely owner: mncs-language. Verification to close: a single
`PhysVec<D>` composing with Geometry vectors without overload debt.

### P-PHYSICS-UNITS — no static unit metadata (non-blocking)

Workload: compile-time unit scales and zero-cost dimension erasure.
Current behavior: scales are runtime `f64` in constructor
functions; whether the compiler erases `Dim`/`Unit` records is
UNKNOWN (no backend introspection performed).
Likely owner: mncs-compiler. Workaround: none needed — suite
runtimes are toolchain-dominated; physics arithmetic cost is
negligible. Verification to close: backend evidence on wrapper
representation.

### P-PHYSICS-SQRT — root domain inherited from Numerics (non-blocking)

Workload: `speed_from_ke` for very small/large energies.
Current behavior: `sqrt_newton` guarantees accuracy only on
1e-12 <= x <= 1e24; the guard ordering (BadValue before root) is
correct, but energies outside the domain carry no accuracy promise.
Likely owner: mncs-numerics (already owns the routine and its
contract). No workaround in Physics beyond documenting the domain.

### P-PHYSICS-SERIAL — no Data/Store/Lineage path (non-blocking)

Workload: persisting a `Quantity`/`Const` without losing dimension
or provenance.
Current behavior: plain records; serialization round-trip
UNVERIFIED; no Store/Lineage integration attempted.
Likely owner: physics + mncs-data (future slice). Not a gap in the
language — a scope boundary of this campaign.

### P-PHYSICS-UNC — uncertainty is metadata, not arithmetic (non-blocking)

Workload: propagating `rel_unc` through calculations.
Current behavior: constants carry `rel_unc` (0.0 for exact); no
uncertainty arithmetic exists.
Likely owner: future generic capability (Math interval? Numerics?).
Deliberately not built: no workload in this slice needs it.

## Observed language facts (pinned by this campaign)

- MNE130: only direct self-calls consuming a match-bound
  structural descendant are admitted; integer-countdown and mutual
  recursion are rejected.
- `iterate x up_to N` requires a literal bound (dynamic trip
  counts inexpressible).
- Long decimal literals (34+ digits) parse correctly rounded:
  verified bitwise against Python floats for all constant/unit
  scales in this repo.
- `0.0 - x` negative-literal idiom; no trailing commas in enum
  payloads; test names must not shadow (MNE132).
