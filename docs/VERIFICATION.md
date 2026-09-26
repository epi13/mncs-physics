# Verification

Canonical parameters: m = 2 kg, a = 3 m/s², v = 3 m/s;
canonical drop: 1 kg from rest, F = −g0, dt = 1 s.
51 native `mncs test` declarations across 7 suites, all PASS,
plus a 46-check independent oracle (`tools/oracle_physics.py`,
exact rationals + IEEE-754 cross-checks), all PASS.

## Dimensions (dim, 5 tests)

- Base dimensions pairwise distinct; dimensionless distinct.
- velocity = L/T, acceleration = V/T, force = M·A, energy = F·L,
  power = E/T, pressure = F/A, charge = I·T, voltage = P/I = E/Q,
  density = M/V, stiffness = F/L, momentum = M·V — all exact.
- mul/div invert; pow(0) is dimensionless; negative powers cancel.
- force ≠ energy, pressure ≠ energy, temperature ≠ dimensionless.

## Units (unit, 10 tests)

- Metric conversions exact `==` (km/cm/mm/Å).
- Imperial definitions exact (inch 0.0254, foot 0.3048, mile).
- 12 in = 1 ft holds to stated tolerance (two inexact scales).
- Cross-system (m↔ft, km/h) and round trips (ft, psi) via `approx`.
- Incompatible conversions are `BadDim` (m→s, J→N).
- joule == force·length dimensionally; watt, pascal, hertz, eV named.
- eV scale pinned; 1000 eV conversion (caught a 100× test-literal
  typo during development — the assertion did its job).
- 180° = π rad bitwise against `math.pi/180`; degree dimensionless.
- Celsius affine: 0 °C = 273.15 K exact, triple point, round trip.
- day/hour/tonne/gram exact.

## Quantities (quantity, 9 tests)

- SI boundary storage; compatible add/sub exact; incompatible
  add/sub/approx are `BadDim`/false data, never traps.
- length/time → velocity; mass·acceleration → force;
  force·distance → energy — all exact values with composed dims.
- Zero-divisor division is `DivByZero`.
- q_pow2/q_pow3 compose; q_inv refuses zero; scalar extraction
  checks the expected dimension.

## Constants (constant, 7 tests)

- c, dCs, g0, π pinned exact with dimensions and exactness flags.
- h/kB/e/NA within 1e-12 relative; hbar computed (6.1e-10 from
  reference, tol 1e-9); R computed bitwise; σ_SB computed (3.3e-11).
- G/m_e/m_p/u/eps0 measured: values within 1e-12, `exact == false`,
  uncertainties stated; dimensions compose (G, eps0, action).

## Mechanics (mech, 7 tests)

- F = 6 N, p = 6, K = 9 J; W = 12 J, P = 25 W; a/v inverses exact.
- Zero-time power is `DivByZero`; wrong-dimension inputs `BadDim`.
- Weight 1 kg = 9.80665 N exact; kinematics v = 7, x = 12 exact.
- sqrt(18) ≈ 4.242640687119285; rest energy gives 0; negative
  energy `BadValue`; zero mass `DivByZero`.

## Physical vectors (vecmech, 6 tests)

- Displacement/velocity/force algebra exact via Geometry.
- Unit-scaled construction checks length dimension.
- v = d/dt and a = dv/dt with `BadDim` (mass-typed duration) and
  `DivByZero` arms; F = ma and p = mv componentwise with `BadDim`.
- W = F·d = 6 J exact; K = 25 J; speed-squared dim L²/T².

## Model slice (model1d, 7 tests)

- Body construction dimension arms; zero force typed.
- Free motion: v/x/ke/momentum bitwise conserved, work exactly 0.
- Drop: v ≈ −g0, x ≈ −g0/2, K1 ≈ W (tol 1e-12).
- Work-energy residual ≈ 0 on a driven step.
- Two half-steps match one full step (tol 1e-12).
- Force-as-energy and duration-as-length `BadDim`; zero mass
  constructs (dimension-valid) but steps `DivByZero`.
- Consumer fixtures: 101325 Pa atmosphere ↔ 1.01325 bar,
  N/m stiffness dimension, 13.6 eV H ionization energy.

## Reproduction

`python3 scripts/run_tests.py` (native suites + oracle + evidence
JSON under `target/`). Full run ≈2 min (toolchain invocations
dominate; physics cost is negligible).
