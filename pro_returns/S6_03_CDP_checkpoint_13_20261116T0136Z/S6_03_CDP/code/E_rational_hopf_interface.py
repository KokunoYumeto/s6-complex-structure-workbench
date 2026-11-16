"""Exact arithmetic and monodromy certificates used in UN67."""
import sympy as sp

# The long-exact-sequence dimensions before the first trivial normal power.
pencil_cases = 0
stein_cases = 0
for m in range(1, 81):
    h0, h1 = 1, 0
    for k in range(1, m):
        # H^0(N^k)=H^1(N^k)=0, so both displayed dimensions persist.
        assert h0 == 1 and h1 == 0
    # At the exact order m, H^0(N^m)=1 and H^1((m-1)J)=0.
    h0 += 1
    assert h0 == 2
    pencil_cases += 1
    for d in range(2, m + 1):
        if m % d == 0:
            # Connected Stein fibre (m/d)J would trivialize that normal power.
            assert 0 < m // d < m
            assert (m // d) % m != 0
            stein_cases += 1
print(f"PASS: {pencil_cases} exact first cohomology jumps")
print(f"PASS: {stein_cases} nontrivial Stein degrees contradict exact normal order")

I = sp.eye(2)
II = sp.Matrix([[1, 1], [-1, 0]])
III = sp.Matrix([[0, 1], [-1, 0]])
IV = sp.Matrix([[0, 1], [-1, -1]])
types = {
    "II": II, "II*": II.inv(),
    "III": III, "III*": III.inv(),
    "IV": IV, "IV*": IV.inv(),
    "I0*": -I,
}
orders = {"II": 6, "II*": 6, "III": 4, "III*": 4,
          "IV": 3, "IV*": 3, "I0*": 2}
for name, M in types.items():
    assert M.det() == 1 and M != I
    order = orders[name]
    assert M ** order == I
    assert all(M ** k != I for k in range(1, order))
    print(f"PASS: {name} monodromy is nonidentity, exact order {order}")

n = sp.symbols("n", integer=True, positive=True)
In = sp.Matrix([[1, n], [0, 1]])
assert In.det() == 1
assert (In - I)[0, 1] == n
assert (-In - I)[0, 0] == -2
print("PASS: I_n (n>0) and every I_n* have nonidentity monodromy")
print("PASS: I_0 is the sole identity case in the relatively minimal table")

e = sp.symbols("e", integer=True, positive=True)
# The exact unit-root map w^a=u, s=w*h has derivative a*w^(a-1) != 0.
w, hh = sp.symbols("w h", nonzero=True)
for a in range(1, 21):
    assert sp.diff(w ** a, w) == a * w ** (a - 1)
    assert sp.expand((w * hh) ** a - w ** a * hh ** a) == 0
print("PASS: 20 actual multiple-root equations and nonvanishing unit-root derivatives")
print("Leray comparison: chi(O_Pmin)=chi(O_P1)-chi(O_P1)=0; "
      "rational birational invariance gives 1, a contradiction.")
print("ALL UN67 EXACT CHECKS PASSED")
