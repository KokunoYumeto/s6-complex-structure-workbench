"""Fresh exact arithmetic for UN24 and UN39, authored after receiving proof access.

Uses Python's standard library only. No previous producer is imported. Input
tables are compared only after the integer-matrix results have been derived.
This is a finite/algebraic certificate, not a new proof of geometric inputs.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm
from pathlib import Path
import hashlib
import json
import re

OUT = Path(__file__).resolve().parents[1]
CHECKS = 0

def check(truth, description):
    global CHECKS
    CHECKS += 1
    if not truth:
        raise AssertionError(description)

def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def pdiv(p, q):
    p = list(map(F, p)); q = list(map(F, q))
    r = [F(0)] * max(1, len(p) - len(q) + 1)
    while len(p) >= len(q) and any(p):
        k = len(p) - len(q); c = p[-1] / q[-1]
        r[k] += c
        for i, a in enumerate(q):
            p[k+i] -= c*a
        trim(p)
    check(not any(p), "cyclotomic division exact")
    check(all(c.denominator == 1 for c in r), "integral cyclotomic coefficients")
    return trim([int(c) for c in r])

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def mobius(n):
    primes = 0
    for p in range(2, n+1):
        if n % p == 0:
            n //= p; primes += 1
            if n % p == 0:
                return 0
    return (-1)**primes

def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n+1))

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mm(A, B):
    return [[sum(a*b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

def mpow(A, k):
    B = ident(len(A))
    while k:
        if k % 2:
            B = mm(B, A)
        A = mm(A, A); k //= 2
    return B

def det(A):
    B = [list(map(F, r)) for r in A]
    ans = F(1)
    for i in range(len(B)):
        j = next((j for j in range(i, len(B)) if B[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            B[i], B[j] = B[j], B[i]; ans = -ans
        pivot = B[i][i]; ans *= pivot
        for j in range(i+1, len(B)):
            ratio = B[j][i]/pivot
            for k in range(i+1, len(B)):
                B[j][k] -= ratio*B[i][k]
            B[j][i] = F(0)
    return ans

def companion(p):
    n = len(p)-1
    check(p[-1] == 1, "monic companion input")
    A = [[0]*n for _ in range(n)]
    for i in range(1, n):
        A[i][i-1] = 1
    for i in range(n):
        A[i][-1] = -p[i]
    return A

def block_diagonal(blocks):
    n = sum(map(len, blocks)); A = [[0]*n for _ in range(n)]; start = 0
    for B in blocks:
        for i, row in enumerate(B):
            for j, x in enumerate(row):
                A[start+i][start+j] = x
        start += len(B)
    return A

def fixed_number(A, k):
    B = mpow(A, k)
    value = det([[int(i == j)-B[i][j] for j in range(len(A))] for i in range(len(A))])
    check(value.denominator == 1, "integral determinant")
    return int(value)

# Complete small cyclotomic list: a prime divisor p must have p-1<=4,
# hence p in{2,3,5}; the prime-power totient bound gives these finite ranges.
indices = sorted({2**a*3**b*5**c for a in range(4) for b in range(2) for c in range(2) if phi(2**a*3**b*5**c) <= 4})
check(indices == [1,2,3,4,5,6,8,10,12], "complete phi<=4 list")
cyclo = {}
for n in range(1, 13):
    p = [-1]+[0]*(n-1)+[1]
    for d in divisors(n)[:-1]:
        p = pdiv(p, cyclo[d])
    cyclo[n] = p
    check(len(p)-1 == phi(n), "cyclotomic degree")

rows = []
for exps in product(*(range(4//phi(n)+1) for n in indices)):
    if sum(a*phi(n) for n, a in zip(indices, exps)) != 4:
        continue
    if (-1)**exps[0] != 1:
        continue
    factors = {n: a for n, a in zip(indices, exps) if a}
    M = lcm(*factors)
    A = block_diagonal([companion(cyclo[n]) for n, a in factors.items() for _ in range(a)])
    check(det(A) == 1, "orientation-preserving rank-four matrix")
    check(mpow(A, M) == ident(4), "semisimple model has asserted period")
    check(all(mpow(A, d) != ident(4) for d in divisors(M)[:-1]), "semisimple period exact")
    values = [fixed_number(A, k) for k in range(1, M+1)]
    average = F(sum(values), M)
    check(average.denominator == 1, "integral average")
    aa = {}
    for d in divisors(M):
        ad = F(sum(mobius(d//e)*values[e-1] for e in divisors(d)), d)
        check(ad.denominator == 1, "integral Mobius coefficient")
        if ad:
            aa[d] = int(ad)
    for k in range(1, M+1):
        check(values[k-1] == sum(d*a for d,a in aa.items() if k % d == 0), "all-period Mobius reconstruction")
    check(sum(aa.values()) == average, "average equals sum of signature coefficients")
    rows.append({"factors": factors, "order": M, "matrix": A, "one_period_determinants": values, "signature_coefficients": aa, "average": int(average), "zero_index": str(average/2)})
check(len(rows) == 19, "all nineteen degree-four patterns")

# Compare the entire actual UN39 display, after deriving the matrix results.
receiving39 = OUT / "UN39_current_full_receiving_08.tex"
text39 = receiving39.read_text()
display = text39[text39.index("\\begin{array}"):text39.index("\\end{array}")]
printed = []
for line in display.splitlines():
    if not line.startswith("\\Phi_"):
        continue
    parts = line.rstrip("\\").split("&")
    factors = {int(n): int(a or 1) for n,a in re.findall(r"\\Phi_\{(\d+)\}(?:\^\{?(\d+)\}?)?", parts[0])}
    printed.append((factors, *map(int, parts[1:])))
check(len(printed) == 19, "all nineteen printed rows parsed")
for factors, M, j, zero in printed:
    r = next(r for r in rows if r["factors"] == factors)
    check((r["order"], r["average"], F(r["zero_index"])) == (M,j,zero), "exact printed UN39 row")

# Also compare the actual UN11 table already used in the current run.
blocks = json.loads((OUT / "blocks.json").read_text())
statement11 = next(b["statement"] for b in blocks if b["label"] == "cdp:st:C.2.UN.11")
seen11 = 0
for line in statement11.splitlines():
    if not line.startswith("$\\Phi_"):
        continue
    factors = {int(n): int(a or 1) for n,a in re.findall(r"\\Phi_\{(\d+)\}(?:\^\{?(\d+)\}?)?", line.split("&")[0])}
    aa = {int(n): int(v) for n,v in re.findall(r"a_\{(\d+)\}=(-?\d+)", line)}
    r = next(r for r in rows if r["factors"] == factors)
    check(r["signature_coefficients"] == aa, "entire UN11 signature row agrees")
    seen11 += 1
check(seen11 == 19, "nineteen UN11 input rows")

# UN24: exact fixed-point sets, exact stabilizers, orbit counts, ADE ranks,
# Burnside quotient Euler and exceptional resolution Euler for every order.
quotients = []
for n in [2,3,4,6]:
    polys = [cyclo[n]] * (4//phi(n))
    A = block_diagonal([companion(p) for p in polys])
    check(mpow(A,n) == ident(4), "cyclic K3 matrix order divides n")
    values = [0]+[fixed_number(A,k) for k in range(1,n)]
    # For every divisor d>1, Fix(g^(n/d)) contains exactly the points whose
    # stabilizer contains the subgroup of order d. Subtract larger stabilizers.
    exact = {}
    for d in reversed(divisors(n)[1:]):
        full = fixed_number(A,n//d)
        exact[d] = full-sum(v for e,v in exact.items() if e % d == 0)
        check(exact[d] >= 0, "nonnegative exact-stabilizer point count")
    orbits = {}
    for d, count in exact.items():
        number = F(count,n//d)
        check(number.denominator == 1, "integral stabilizer orbit count")
        orbits[d-1] = int(number)
    for k in range(1,n):
        check(values[k] == sum(count for d,count in exact.items() if k % (n//d) == 0), "all powers recovered from exact stabilizers")
    euler = F(sum(values),n)
    rank = sum(a*m for a,m in orbits.items())
    check(euler.denominator == 1, "integral Burnside quotient Euler")
    check(euler+rank == 24, "exceptional chain correction gives K3 Euler24")
    quotients.append({"order":n,"matrix":A,"nonidentity_fixed_numbers":values[1:],"exact_stabilizer_points":exact,"A_rank_multiplicities":orbits,"quotient_Euler":int(euler),"exceptional_rank":rank,"resolution_Euler":int(euler+rank)})
expected = {2:({1:16},16,8),3:({2:9},18,6),4:({3:4,1:6},18,6),6:({5:1,2:4,1:5},18,6)}
for r in quotients:
    check((r["A_rank_multiplicities"],r["exceptional_rank"],r["quotient_Euler"]) == expected[r["order"]], "entire printed UN24 quotient row")

# Universal formal orthogonal-projection and isotropic-class identities.
# Sparse multivariate polynomials over Q in (H2,h1,...,h4,x1,...,x4).
NV = 9; ZERO = (0,)*NV
def scalar(c):
    return {} if c == 0 else {ZERO:F(c)}
def var(i):
    e = list(ZERO);e[i]=1
    return {tuple(e):F(1)}
def add(*pp):
    out={}
    for p in pp:
        for e,c in p.items():out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def neg(p):
    return {e:-c for e,c in p.items()}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            ef=tuple(a+b for a,b in zip(e,f));out[ef]=out.get(ef,F(0))+c*d
    return {e:c for e,c in out.items() if c}
def dot(v,w,G):
    return add(*(mul(mul(v[i],w[j]),G[i][j]) for i in range(5) for j in range(5)))
G=[[{} for _ in range(5)] for _ in range(5)];G[0][0]=var(0)
for i in range(1,5):
    G[0][i]=G[i][0]=var(i);G[i][i]=scalar(-2)
hp=[scalar(1)]+[mul(scalar(F(1,2)),var(i)) for i in range(1,5)]
dv=[scalar(1)]+[add(hp[i],neg(var(i+4))) for i in range(1,5)]
hp2=add(var(0),*(mul(scalar(F(1,2)),mul(var(i),var(i))) for i in range(1,5)))
for i in range(1,5):
    ci=[scalar(int(i==j)) for j in range(5)]
    check(dot(hp,ci,G)=={}, "universal Hprime orthogonal to Ci")
check(dot(hp,hp,G)==hp2, "universal Hprime squared")
check(dot(dv,hp,G)==hp2, "universal D dot Hprime")
check(dot(dv,dv,G)==add(hp2,*(mul(scalar(-2),mul(var(i),var(i))) for i in range(5,9))), "universal D squared before four-square substitution")

result={
    "status":"PASS", "checks":CHECKS,
    "reading_order":"New standard-library certificate written after the receiving proofs and old current small programs had been read. No new before-reading proof credit.",
    "algorithm":"Cyclotomic polynomials are obtained by exact monic division of x^n-1. Integer block-companion matrices supply every one-period determinant. Exact Mobius inversion and rational averaging are independent of the old SymPy implementation. Exact stabilizer subtraction and Burnside averaging supply the complete cyclic quotient table. Sparse formal polynomials certify the universal four-curve projection identities.",
    "monodromy_morphism_scope":"The block matrices are explicit finite-order models for the characteristic polynomials. They do not identify an actual monodromy matrix with its semisimple part. Over C, upper triangularization of the actual matrix gives det(I-T^k)=product over its eigenvalues of(1-lambda^k), including every multiplicity. This exact determinant identity connects the finite models to the actual T, even with nontrivial unipotent part.",
    "UN39_all19":rows,
    "UN39_printed_table_all_rows_match":True,
    "UN11_signature_all19_match":True,
    "UN24_all4":quotients,
    "UN24_universal_projection":"Hprime.Ci=0; Hprime²=H²+sum(hi²)/2; D.Hprime=Hprime²; D²=Hprime²-2sum(xi²). These identities hold in Q[H²,h1,...,h4,x1,...,x4]. Lagrange's cited four-square theorem supplies the actual rational xi; its theorem is not inferred from finite samples.",
    "scope_limit":"These calculations prove the stated arithmetic and polynomial identities. They do not reprove analytic resolution, root-cover/fibration descent, the A'Campo proper nearby-cycle theorem, the K3 elliptic-pencil theorem or compact occurrence geometry. Those remain covered by the exact full proof/source records.",
    "receiving39_sha256":hashlib.sha256(receiving39.read_bytes()).hexdigest(),
    "receiving24_sha256":hashlib.sha256((OUT/"UN24_current_full_receiving_08.tex").read_bytes()).hexdigest(),
    "code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(OUT/"UN24_UN39_exact_certificate_08.json").write_text(json.dumps(result,indent=2)+"\n")
print(f"PASS {CHECKS} exact checks; all19 monodromy rows; all4 cyclic K3 rows; all7 universal projection identities")
