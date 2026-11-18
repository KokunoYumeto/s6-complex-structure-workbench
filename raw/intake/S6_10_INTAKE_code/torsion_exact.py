# Intake check (Claude Opus 5.5 at effort max), 18 Nov 2026.
# Exact check of the torsion table of S6_10_PAPERS Paper I (ari:C.4.2-C.4.4 opening table)
# Model of Paper I, line 2085: y^2 = x^3 + A x + B, A=-(3/4)t^3(t-1), B=(1/4)t^4(t-1)^2, P=(0,t^2(t-1)/2)
import sympy as sp
t, x = sp.symbols('t x')
A = -sp.Rational(3,4)*t**3*(t-1); B = sp.Rational(1,4)*t**4*(t-1)**2
yP = t**2*(t-1)/2
Delta = sp.factor(-16*(4*A**3+27*B**2))
print("Delta =", Delta)
print("j/1728 =", sp.simplify(4*A**3/(4*A**3+27*B**2)))
assert sp.simplify(yP**2 - (0 + A*0 + B)) == 0
# division polynomials at x=0, y=yP, using the standard recursion (psi1=1, psi2=2y)
def psis(N):
    y = sp.Symbol('y')
    ps = {0: sp.Integer(0), 1: sp.Integer(1), 2: 2*y,
          3: 3*x**4+6*A*x**2+12*B*x-A**2,
          4: 4*y*(x**6+5*A*x**4+20*B*x**3-5*A**2*x**2-4*A*B*x-8*B**2-A**3)}
    for n in range(5, N+1):
        m = n//2
        if n % 2 == 1:
            ps[n] = ps[m+2]*ps[m]**3 - ps[m-1]*ps[m+1]**3
        else:
            ps[n] = ps[m]*(ps[m+2]*ps[m-1]**2 - ps[m-2]*ps[m+1]**2)/(2*y)
    out = {}
    for n in range(1, N+1):
        e = sp.expand(ps[n])
        # reduce y^2 -> x^3+Ax+B
        e = sp.expand(e.subs(y**2, x**3+A*x+B)) if False else e
        e = e.subs(x, 0)
        e = sp.expand(e)
        # replace powers of y using y^2 = B at x=0
        e = sp.expand(e.subs(y, yP))
        out[n] = sp.factor(e)
    return out
ps = psis(8)
for n in range(2, 9):
    print(f"psi_{n}(P) =", ps[n])
# order-n locus: psi_n(P)=0 with psi_d(P) != 0 for d|n, d<n
def locus(n):
    f = sp.factor(ps[n])
    num = sp.Poly(sp.numer(sp.together(f)), t)
    fac = sp.factor_list(num.as_expr())[1]
    res = []
    for g, e in fac:
        if g.free_symbols and not any(sp.rem(sp.Poly(ps[d], t) if sp.numer(sp.together(ps[d]))==ps[d] else sp.Poly(sp.numer(sp.together(ps[d])), t), sp.Poly(g, t)).is_zero for d in range(2, n) if n % d == 0):
            if sp.degree(g, t) > 0 and g not in (t, t-1):
                res.append(g)
    return res
for n in range(2, 9):
    print(f"order-{n} locus factors:", locus(n))
# norm values from N(P)^{m^2} = N(mP) |Delta|^{(m^2-1)/12} / |psi_m(P)| with mP = +-P (N even)
def N12(n, tval):
    m = n - 1  # mP = -P
    val = sp.Abs(Delta.subs(t, tval))**sp.Rational(m*m-1, 12) / sp.Abs(ps[m].subs(t, tval))
    # N^{m^2-1} = val  =>  N^12 = val^(12/(m^2-1))
    return sp.nsimplify(sp.simplify(val**sp.Rational(12, m*m-1)))
r3 = sp.sqrt(3)
for n, tv, claim in [(4, sp.Rational(32,5), 10), (6, 64*(47-27*r3)/11, 17+10*r3), (6, 64*(47+27*r3)/11, 10*r3-17)]:
    v = N12(n, tv)
    print(f"order {n}, t={tv}: N^12 = {sp.radsimp(v)}  claim {claim}  equal: {sp.simplify(sp.radsimp(v)-claim)==0}")
# general formulas on the order-3 and order-4/2 loci and limits at t=0,1
print("N^12 on 3-torsion locus (m=2): ", sp.simplify((sp.Abs(Delta)**sp.Rational(3,12)/sp.Abs(ps[2]))**4))
print("N^12 on 4-torsion locus (m=3): ", sp.simplify((sp.Abs(Delta)**sp.Rational(8,12)/sp.Abs(ps[3]))**sp.Rational(12,8)))
print("domain constant exp(-pi*M), M=(6/pi)log(sqrt2/(2sqrt3)):", sp.simplify(sp.exp(-sp.pi*(6/sp.pi)*sp.log(sp.sqrt(2)/(2*sp.sqrt(3))))))
