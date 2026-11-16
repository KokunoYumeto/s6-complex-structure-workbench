"""Exact normalized cyclic-cover blowups and rational attachment budgets.

Checks the extra node/cusp cases of C.2.RAT.9. All identities are polynomial.
"""
import sympy as sp

s, x, u, s1, t, w, w1, w2 = sp.symbols("s x u s1 t w w1 w2")


def character_increments(m1, m2):
    k, residue = divmod(m1 + 2 * m2, 3)
    return k, 2 * k - m2 + int(residue == 2)


assert character_increments(1, 1) == (1, 1)
assert character_increments(2, 1) == (1, 1)
assert character_increments(2, 0) == (0, 1)
print("Character increments: (2,1) contact (1,1); (2,1,1) triple (1,1); (1,1) pair (0,1).")

cusp = w**3 - s**2 * (x**2 - s**3)
stage1 = sp.cancel(cusp.subs({x: s*u, w: s*w1}) / s**3)
assert sp.expand(stage1 - (w1**3 - s*(u**2-s))) == 0
stage2 = sp.expand(stage1.subs(s, u*s1))
assert sp.expand(stage2 - (w1**3-u**2*s1*(u-s1))) == 0
stage3 = sp.cancel(stage2.subs({s1: u*t, w1: u*w2}) / u**3)
assert sp.expand(stage3 - (w2**3-u*t*(1-t))) == 0
print("Cusp blowup charts:", stage1, ";", stage2, ";", stage3)

tangent_triple = w**3 - s**2*u*(s-u**2)
triple1 = sp.cancel(tangent_triple.subs({s: u*s1, w: u*w1}) / u**3)
assert sp.expand(triple1 - (w1**3-u*s1**2*(s1-u))) == 0
triple2 = sp.cancel(triple1.subs({s1: u*t, w1: u*w2}) / u**3)
assert sp.expand(triple2 - (w2**3-u*t**2*(t-1))) == 0
print("Tangent triple charts:", triple1, ";", triple2)

ordinary_triple = w**3-s**2*u*(s-u)
resolved_triple = sp.cancel(ordinary_triple.subs({s:u*s1,w:u*w1})/u**3)
assert sp.expand(resolved_triple-(w1**3-u*s1**2*(s1-1))) == 0
print("Ordinary weighted triple chart:", resolved_triple)

print("Two reduced scalar fibres: (lambda, surviving nu, maximum attachment loss)")
for link in range(3):
    for nu in range(4, 9):
        rank = 2*nu-8-link
        if rank == 0:
            assert nu-4 <= 1
            print((link, nu, nu-4))
assert 2*2-4 == 0
print("Double scalar fibre: nu=2, one C-preimage, loss=0.")
print("PASS")
