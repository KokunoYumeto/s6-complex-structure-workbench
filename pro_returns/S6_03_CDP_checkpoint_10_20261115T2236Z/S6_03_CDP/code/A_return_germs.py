"""Exact formal coefficient certificates for C.2.UN.29.

The geometric proof constructs actual holomorphic return germs.  This
script checks only the two coefficient extractions from their exact
preservation identities; it does not substitute a formal germ for that
geometric construction.

For arbitrary d >= 1, Delta = phi-z has order d and A has order d.
Consequently Taylor terms of order Delta**2 in A(phi) have order >= 3d,
strictly above 2d.  In h(phi)-h the analogous terms have order >= 2d,
strictly above d.  These inequalities justify the finite jet algebra
used below for every d.  Executed values d=1,...,8 additionally check
that all higher unknown coefficients cancel as claimed.
"""

import sympy as sp

s = sp.Symbol("s")

for d in range(1, 9):
    a = sp.symbols(f"a0:{d+1}")
    az = sp.symbols(f"az0:{d+1}")
    p = sp.symbols(f"p{d}:{2*d+1}")
    pz = sp.symbols(f"pz{d}:{2*d+1}")
    delta = sum(p[k-d]*s**k for k in range(d, 2*d+1))
    phi_z = 1 + sum(pz[k-d]*s**k for k in range(d, 2*d+1))
    A = sum(a[j]*s**(d+j) for j in range(d+1))
    # Taylor expansion modulo s**(2d+1); its omitted terms have order >=3d.
    A_phi = sum((a[j]+az[j]*delta)*s**(d+j)
                for j in range(d+1))
    difference_A = sp.Poly(sp.expand(A_phi-A*phi_z), s)
    assert all(difference_A.coeff_monomial(s**k) == 0
               for k in range(2*d))
    first = sp.factor(difference_A.coeff_monomial(s**(2*d)))
    expected_first = az[0]*p[0]-a[0]*pz[0]
    assert sp.expand(first-expected_first) == 0

    hz = sp.symbols(f"hz0:{d+1}")
    delta_z = sp.symbols(f"delta_z0:{d+1}")
    h_phi_minus_h = sum(hz[j]*s**j*delta for j in range(d+1))
    A_delta_z = A*sum(delta_z[j]*s**j for j in range(d+1))
    difference_h = sp.Poly(sp.expand(h_phi_minus_h-A_delta_z), s)
    assert all(difference_h.coeff_monomial(s**k) == 0
               for k in range(d))
    second = sp.factor(difference_h.coeff_monomial(s**d))
    expected_second = hz[0]*p[0]-a[0]*delta_z[0]
    assert sp.expand(second-expected_second) == 0
    print(f"d={d}: orders below 2d/d cancel; "
          "[s^(2d)] = a' psi - a psi'; "
          "[s^d] = H' psi - a delta_0'.")

z, k, d0 = sp.symbols("z k d0")
a_fun = sp.Function("a")(z)
H = sp.Function("H")(z)
psi = k*a_fun
lam = d0-k*H
assert sp.simplify(sp.diff(a_fun,z)*psi-a_fun*sp.diff(psi,z)) == 0
assert sp.simplify(sp.diff(H,z)*psi+a_fun*sp.diff(lam,z)) == 0
assert sp.simplify(sp.diff(lam,z)+k*sp.diff(H,z)) == 0
print("Exact integration check: psi=k*a and lambda=d0-k*H satisfy both identities.")
print("PASS: all symbolic assertions.")
