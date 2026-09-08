# Agent and contributor contract

`mncs-physics` is both a scientific library and an MNCS-language pressure test.

- Implement core work in `mncs-language` whenever possible.
- Never trade scientific correctness for an undocumented workaround.
- Every solver/model must state assumptions, units, precision expectations, tolerances, and validation strategy.
- Prefer published reference cases, analytic solutions, invariants, conservation laws, or independent high-precision references.
- Record language/compiler/runtime blockers in `docs/LANGUAGE_PRESSURES.md` instead of permanently routing around them.
- Keep approximate/game-oriented behavior separate from scientific contracts.
- Cross-backend differences must be measured and explained, especially CPU versus CUDA and across hardware generations.
