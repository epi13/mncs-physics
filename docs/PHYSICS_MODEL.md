# Physics model

## What mncs-physics means

Classical physical semantics layered over mathematics: dimensions,
units, quantities, reference constants, and generic mechanics
relationships. This repository is explicitly NOT:

- CPU atomic operations or concurrency primitives;
- quantum chemistry or spectroscopy (Atomic's domain);
- fluid mechanics (Fluid's domain);
- finite-element machinery (FEM's domain);
- a game-physics shortcut layer (non-goal per RFC 0001).

## Ownership boundary

| Concept | Owner | Physics' use |
|---|---|---|
| Numeric representation, precision, rounding, `approx`, `safe_div`, `sqrt` | Numerics | Consumed; never re-implemented |
| Algebra, dot products, generic operators | Math | Consumed via Geometry/Numerics; `work = F·d` assigns meaning to Math's dot |
| Points, displacement vectors, transforms, frames | Geometry | Consumed; `Disp2/Vel2/Acc2/Force2/Mom2` wrap `Vec2`, never re-derive vector algebra |
| Viscosity, pressure/flow formulations | Fluid | Fluid consumes pressure/stiffness/energy dimensions; equations stay in Fluid |
| Meshes, elements, DOFs, assembly | FEM | FEM consumes force/length dimensions; machinery stays in FEM |
| Species, potentials, thermostats | Atomic | Atomic consumes energy (eV) and mass dimensions; state models stay in Atomic |
| Persistence, execution, derivation graphs | Store/Forge/Lineage | Not integrated in this slice (plain records; see pressures) |
| Test execution, assertions | mncs-test | Consumed |

Physics owns: the 7-vector SI dimension, named units as
scale+dimension, quantities (SI value + dimension), pinned constants
with provenance, checked scalar mechanics relations, physical vector
wrappers with cross-kind conversions, and the constant-force 1D
result model. Physics knows nothing of any neighbor's application
semantics: the consumer fixtures in `model1d_tests` prove dimension
identities (pressure, stiffness, eV energy) that Fluid/FEM/Atomic
need, without importing or coupling to those repositories.

## Quantity model

`Quantity { value: f64 (SI), dim: Dim }`. Construction from a
value-in-unit scales once at the boundary (`quantity_in`); all later
computation is SI with structural dimension tracking. `Quantity` is
nominally distinct from `f64`, so bare scalars never mix implicitly.

## Enforcement model

- Static: nominal separation (Quantity vs f64; Force2 vs Disp2 —
  no function exists that adds them, as `point + point` is
  unspellable in Geometry).
- Runtime (structural data, never traps): `BadDim` on
  add/sub/convert/extract/relation mismatch; `DivByZero` on zero
  divisors; `BadValue` on negative energy under the root.
- Impossible today: type-level dimensions (`Quantity<Length, f64>`)
  and general integer powers (see `docs/LANGUAGE_PRESSURES.md`).

## Vertical slice

Typed mass + position + velocity + duration + applied force
→ `step_const_force` (exact constant-force update)
→ momentum/energy bookkeeping + work
→ free-motion bitwise conservation, work-energy agreement,
   two-step composition, 1 kg drop under weight.

## What is NOT claimed

No rigid bodies, no thermodynamics/EM equations (unit names only),
no general integrator suite, no uncertainty arithmetic, no
serialization/store/lineage integration, no cross-backend bitwise
claims, no performance optimization beyond honest wrappers.
