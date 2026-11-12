# D1 sanity checks: Erdos-Straus shell counts, selector census, D4 cubic image, eta/Fricke numerics.
from fractions import Fraction as Fr
from itertools import product
from math import gcd, isqrt
import cmath, math


def isprime(n):
    if n < 2:
        return False
    for q in range(2, isqrt(n) + 1):
        if n % q == 0:
            return False
    return True


def divisors(n):
    ds = [1]
    m = n
    q = 2
    while q * q <= m:
        if m % q == 0:
            e = 0
            while m % q == 0:
                m //= q
                e += 1
            ds = [d * q ** k for d in ds for k in range(e + 1)]
        q += 1
    if m > 1:
        ds = [d * m ** k for d in ds for k in range(2)]
    return ds


def A_R(p, R):
    a = (p + R) // 4
    assert 4 * a == p + R
    Nsh = p * a
    gg = gcd(R, Nsh)
    R0, N0 = R // gg, Nsh // gg
    return [d for d in divisors(N0 * N0) if (d + N0) % R0 == 0], R0, N0


for p in (2521, 3361):
    ds, R0, N0 = A_R(p, 3)
    print("p =", p, "prime:", isprime(p), "p mod 840 =", p % 840, "a =", (p + 3) // 4, "A_3 =", len(ds),
          "pairs:", sorted(((N0 + d) // R0, (N0 + N0 * N0 // d) // R0) for d in ds)[:6])
print("4/3361 identity:", Fr(1, 841) + Fr(1, 974690) + Fr(1, 28266010) == Fr(4, 3361))
# is 2521 solvable on other shells (it must be: ES verified to huge bounds)
def census(p):
    E = M = 0
    sols = set()
    L = (p - 1) // 4
    for j in range(L):
        R = 4 * j + 3
        a = (p + R) // 4
        for u in divisors(a * a):
            for eps in (0, 1):
                if (4 * u + p ** eps) % R == 0:
                    T = (4 * u + p ** eps) // R
                    K = (p ** (1 - eps) * T + 1) // 4
                    x, y, z = a, p * K, p ** eps * a * K // u
                    assert Fr(1, x) + Fr(1, y) + Fr(1, z) == Fr(4, p)
                    sols.add(tuple(sorted((x, y, z))))
                    if eps == 0:
                        E += 1
                    else:
                        M += 1
    return E, M, len(sols)


for p in (1201, 4561, 8761, 9601, 2521, 3361):
    print("census p =", p, "mod 840 =", p % 840, "(#E, #M, #unordered triples) =", census(p))
# first-half lemma brute force for small p = 1 mod 4: smallest denominator in (p/4, p/2]
def all_solutions(p):
    out = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        # 1/y + 1/z = 4/p - 1/x = (4x-p)/(px)
        num, den = 4 * x - p, p * x
        if num <= 0:
            continue
        for y in range(max(x, den // num + 1), 2 * den // num + 1):
            # z = den*y/(num*y - den)
            dn = num * y - den
            if dn > 0 and (den * y) % dn == 0:
                z = den * y // dn
                if z >= y:
                    out.append((x, y, z))
    return out


for p in (13, 17, 29, 37, 73):
    sols = all_solutions(p)
    print("p =", p, "all sorted solutions have p/4 < x <= p/2:", all(p / 4 < s[0] <= p / 2 for s in sols), len(sols))
# affine gate (6.6): u_j | a_j^2 iff (j=0 and 2|m) or (j=2 and 8|m), 0<=j<3m-3, p=12m-11 prime
bad = 0
for m in range(2, 400):
    p = 12 * m - 11
    if not isprime(p):
        continue
    for j in range(0, 3 * m - 3):
        u = 2 + j * (4 * m - 1)
        a = 3 * m + j - 2
        lhs = (a * a) % u == 0
        rhs = (j == 0 and m % 2 == 0) or (j == 2 and m % 8 == 0)
        if lhs != rhs:
            bad += 1
print("affine gate (6.6) violations for m<400:", bad)
# D4 cubic image
vals = set()
B = 9
for a in product(range(-B, B + 1), repeat=4):
    if sum(a) % 2 == 0:
        vals.add(a[0] * (a[0] ** 2 - 3 * (a[1] ** 2 + a[2] ** 2 + a[3] ** 2)))
S_ok = all((n % 2 == 0) and (n % 3 != 0 or n % 9 == 0) for n in vals)
print("P(D4) box |a_i|<=9: all values in S:", S_ok, " 6 attained:", 6 in vals, " -6:", -6 in vals, " 12:", 12 in vals,
      " missing elements of S in [-60,60]:",
      [n for n in range(-60, 61) if n % 2 == 0 and (n % 3 != 0 or n % 9 == 0) and n not in vals])
# residues of P mod 9 over all of Z^4 with even sum mod 18
res = set()
for a in product(range(18), repeat=4):
    if sum(a) % 2 == 0:
        res.add((a[0] * (a[0] ** 2 - 3 * (a[1] ** 2 + a[2] ** 2 + a[3] ** 2))) % 18)
print("P(D4) residues mod 18:", sorted(res))
# eta quotient T6 and Fricke
def eta(tau, terms=400):
    q = cmath.exp(2j * cmath.pi * tau)
    pr = 1
    for n in range(1, terms):
        pr *= (1 - q ** n)
    return cmath.exp(2j * cmath.pi * tau / 24) * pr


def T6(tau):
    return eta(tau) ** 5 * eta(3 * tau) / (eta(2 * tau) * eta(6 * tau) ** 5)


for tau in (0.13 + 0.41j, -0.3 + 0.25j):
    print("T6(tau)*T6(-1/(6tau)) =", T6(tau) * T6(-1 / (6 * tau)))
# Lambert identity: alpha = (0,5,4,6,4,5) vs 5 - [2|n] + [3|n] - 5[6|n]
al = [0, 5, 4, 6, 4, 5]
print("alpha identity:", all(al[n % 6] == 5 - (n % 2 == 0) + (n % 3 == 0) - 5 * (n % 6 == 0) for n in range(1, 13)))
# Fricke constant vs glue index for all 23 Niemeier root systems: sqrt(det R)
comp_det = {"A": lambda n: n + 1, "D": lambda n: 4, "E": lambda n: {6: 3, 7: 2, 8: 1}[n]}
niem = ["D24", "D16 E8", "E8 E8 E8", "A24", "D12 D12", "A17 E7", "D10 E7 E7", "A15 D9", "D8 D8 D8", "A12 A12",
        "A11 D7 E6", "E6 E6 E6 E6", "A9 A9 D6", "D6 D6 D6 D6", "A8 A8 A8", "A7 A7 D5 D5", "A6 A6 A6 A6",
        "A5 A5 A5 A5 D4", "D4 D4 D4 D4 D4 D4", "A4 A4 A4 A4 A4 A4", "A3 " * 8, "A2 " * 12, "A1 " * 24]
out = []
for s in niem:
    d = 1
    for c in s.split():
        d *= comp_det[c[0]](int(c[1:]))
    out.append((s.split()[0] + ("..." if len(s.split()) > 1 else ""), isqrt(d), isqrt(d) ** 2 == d))
print("glue index = sqrt(det R) for the 23 root systems:", out)
