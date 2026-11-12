import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from lat import *
BN = basis(g)
for d, t in ((2, 3), (3, 2), (6, 1)):
    # K_d = {x in N : (rho,x) = 0 mod d};  w = rho/d - t*alpha
    gens = [sc(d, alpha)] + [sub(x, sc(int(ip(rho, x)), alpha)) for x in g[1:]]
    w = tuple(Fr(a, d) - t * b for a, b in zip(rho, alpha))
    assert all(x.denominator == 1 for x in w)
    w = tuple(int(x) for x in w)
    B = basis(gens + [w])
    sv = short_vectors(B, 2)
    rt = [x for x, n in sv if n == 2]
    print("d =", d, "norm of w:", ip(w, w), "det:", det_true(B), "even:", is_even_integral(B), "roots:", 2 * len(rt), root_system(rt) if rt else {})
