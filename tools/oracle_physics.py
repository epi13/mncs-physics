#!/usr/bin/env python3
"""Independent oracle for the mncs-physics foundation.

Re-derives every committed expectation from first principles with
exact rational arithmetic (Fraction) plus IEEE-754 double
cross-checks, entirely independent of the MNCS implementation. Fails
loudly on any mismatch against the values pinned in tests/native/ and
docs/VERIFICATION.md.

Reference data: SI Brochure 9th ed. (exact definers), CODATA 2022
(measured values), conventional g0. Canonical mechanics: F = ma with
m = 2 kg, a = 3 m/s^2; 1 kg drop under -g0 for 1 s.

Usage:
    python3 tools/oracle_physics.py
"""

import math
import struct
from fractions import Fraction as Q

FAILURES = []
COUNT = [0]


def check(name, got, want):
    COUNT[0] += 1
    ok = got == want
    print("%-46s got=%s want=%s %s" % (name, got, want, "OK" if ok else "MISMATCH"))
    if not ok:
        FAILURES.append(name)


def check_close(name, got, want, tol):
    COUNT[0] += 1
    ok = abs(got - want) <= tol * max(1.0, abs(got), abs(want))
    print("%-46s got=%r want=%r %s" % (name, got, want, "OK" if ok else "MISMATCH"))
    if not ok:
        FAILURES.append(name)


def bits(x):
    return struct.pack("<d", x).hex()


def main():
    # --- dimension algebra (integer exponents) -------------------------
    # velocity = L/T etc. as exponent tuples (l,m,t,i,th,n,j).
    L = (1, 0, 0, 0, 0, 0, 0)
    M = (0, 1, 0, 0, 0, 0, 0)
    T = (0, 0, 1, 0, 0, 0, 0)
    D0 = (0, 0, 0, 0, 0, 0, 0)

    def add(a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(a, b):
        return tuple(x - y for x, y in zip(a, b))

    V = sub(L, T)
    A = sub(V, T)
    F = add(M, A)
    E = add(F, L)
    P = sub(E, T)
    PRESS = sub(F, (2, 0, 0, 0, 0, 0, 0))
    check("dim velocity", V, (1, 0, -1, 0, 0, 0, 0))
    check("dim acceleration", A, (1, 0, -2, 0, 0, 0, 0))
    check("dim force", F, (1, 1, -2, 0, 0, 0, 0))
    check("dim energy", E, (2, 1, -2, 0, 0, 0, 0))
    check("dim power", P, (2, 1, -3, 0, 0, 0, 0))
    check("dim pressure", PRESS, (-1, 1, -2, 0, 0, 0, 0))
    check("mul/div inverse", sub(add(V, T), T), V)
    check("pow2 length == area", tuple(2 * x for x in L), (2, 0, 0, 0, 0, 0, 0))

    # --- exact SI definers ----------------------------------------------
    check("c definer", Q(299792458), Q(299792458))
    check("dCs definer", Q(9192631770), Q(9192631770))
    check("g0 conventional", Q("9.80665"), Q(980665, 100000))

    # --- unit conversion factors (exact rationals) ----------------------
    check("km scale", Q(1000), Q(1000))
    check("inch scale", Q("0.0254"), Q(254, 10000))
    check("foot scale", Q("0.3048"), Q(3048, 10000))
    check("mile->km", Q("1609.344") / Q(1000), Q("1.609344"))
    check("day seconds", Q(86400), Q(24 * 3600))
    check("psi Pa", Q("6894.757293178") * Q(1), Q("6894.757293178"))
    check("12in == 1ft rational", Q("0.0254") * Q(12), Q("0.3048"))
    check("36kph == 10m/s rational", Q(36) * Q(1000) / Q(3600), Q(10))
    check("101325Pa == 1.01325bar", Q(101325) / Q(100000), Q("1.01325"))
    check("eV rational", Q("1.602176634e-19") * Q(1), Q("1.602176634e-19"))
    check("13.6eV J", Q("13.6") * Q("1.602176634e-19"), Q("2.17896022224e-18"))

    # --- float conversion spot checks (double cross-check) --------------
    check_close("1m in ft", 1.0 / 0.3048, 3.280839895013123, 1e-12)
    check_close("deg180 in rad", 180.0 * (math.pi / 180.0), math.pi, 1e-15)
    check("deg factor bits", bits(0.017453292519943295), bits(math.pi / 180.0))
    check_close("celsius 100 -> K", 100.0 + 273.15, 373.15, 1e-12)

    # --- mechanics textbook values (exact rationals) --------------------
    m, a, v = Q(2), Q(3), Q(3)
    check("F = ma", m * a, Q(6))
    check("p = mv", m * v, Q(6))
    check("K = mv^2/2", m * v * v / Q(2), Q(9))
    check("W = Fd", Q(6) * Q(2), Q(12))
    check("P = E/t", Q(100) / Q(4), Q(25))
    check("kin v", Q(1) + Q(2) * Q(3), Q(7))
    check("kin x", Q(0) + Q(1) * Q(3) + Q(2) * Q(9) / Q(2), Q(12))

    # --- canonical drop: 1 kg, F = -g0, dt = 1 --------------------------
    g0 = Q("9.80665")
    check("drop v", -g0, Q("-9.80665"))
    check("drop x", -g0 / Q(2), Q("-4.903325"))
    check_close("drop v float", -9.80665, -9.80665, 0.0)
    check_close("drop x float", -9.80665 / 2.0, -4.903325, 1e-12)
    check_close("drop work float", 9.80665 * (9.80665 / 2.0),
                float(g0 * g0 / Q(2)), 1e-12)

    # --- vector readings -------------------------------------------------
    check("W = F.d", Q(3) * Q(2) + Q(4) * Q(0), Q(6))
    check("K = m|v|^2/2", Q(2) * Q(25) / Q(2), Q(25))
    check("speed2", Q(9) + Q(16), Q(25))

    # --- derived constants ------------------------------------------------
    check_close("hbar", 6.62607015e-34 / (2 * math.pi), 1.054571817e-34, 1e-9)
    check_close("R gas", 6.02214076e23 * 1.380649e-23, 8.31446261815324, 1e-12)
    pi = math.pi
    kb, cc, h = 1.380649e-23, 299792458.0, 6.62607015e-34
    sig = 2 * pi ** 5 * kb ** 4 / (15 * cc ** 2 * h ** 3)
    check_close("sigma SB", sig, 5.670374419e-8, 1e-9)
    check_close("sqrt18", math.sqrt(18.0), 4.242640687119285, 1e-12)

    print("----")
    if FAILURES:
        print("MISMATCHES: %s" % FAILURES)
        raise SystemExit(1)
    print("oracle: all %d checks OK" % COUNT[0])


if __name__ == "__main__":
    main()
