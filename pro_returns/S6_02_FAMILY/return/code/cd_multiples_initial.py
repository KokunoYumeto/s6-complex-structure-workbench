# Sanity check for candidate F-3 (reader's cross-check, not a workbench computation).
# Rational elliptic surface with fibres IV* (t=0), III (t=1), I_1 (t=infinity), j = 1728 t:
#     Y^2 = X^3 + a4(t) X + a6(t),  a4 = -(3/4) t^3 (t-1),  a6 = (1/4) t^4 (t-1)^2
# (obtained from y^2 = x^3 - 3 t^3 (t-1) x + 2 t^4 (t-1)^2 by x = 2X, y = 2*sqrt(2)*Y).
# Section P = (0, t^2 (t-1)/2).  Compute nP for n <= 6 and the t-values where 6P = O.
from sympy import symbols, Rational, cancel, factor, together, fraction, discriminant, Poly, degree, simplify

t = symbols('t')
a4 = -Rational(3, 4) * t**3 * (t - 1)
a6 = Rational(1, 4) * t**4 * (t - 1)**2

disc = cancel(4 * a4**3 + 27 * a6**2)
print('4 a4^3 + 27 a6^2 =', factor(disc))
print('j/1728 = 4 a4^3/(4 a4^3 + 27 a6^2) =', cancel(4 * a4**3 / disc))

P = (0 * t, t**2 * (t - 1) / 2)
assert cancel(P[1]**2 - (P[0]**3 + a4 * P[0] + a6)) == 0


def add(A, B):
    if A is None:
        return B
    if B is None:
        return A
    x1, y1 = A
    x2, y2 = B
    if cancel(x1 - x2) == 0:
        if cancel(y1 + y2) == 0:
            return None
        lam = cancel((3 * x1**2 + a4) / (2 * y1))
    else:
        lam = cancel((y2 - y1) / (x2 - x1))
    x3 = cancel(lam**2 - x1 - x2)
    y3 = cancel(lam * (x1 - x3) - y1)
    return (x3, y3)


Q = None
for n in range(1, 7):
    Q = add(Q, P)
    if Q is None:
        print(n, 'P = O identically')
        break
    num, den = fraction(together(Q[0]))
    print(f'--- {n}P:  x = ({factor(num)}) / ({factor(den)})')
    print(f'    deg num = {degree(num, t)}, deg den = {degree(den, t)}')
    assert cancel(Q[1]**2 - (Q[0]**3 + a4 * Q[0] + a6)) == 0

# behaviour of 6P at t = infinity: in the chart t = 1/s the minimal model is
#   Y'^2 = X'^3 + s^4 a4(1/s) X' + s^6 a6(1/s),   X = X'/s^2
num, den = fraction(together(Q[0]))
print('x(6P) ~ t^%d at infinity; X\' = s^2 X ~ s^%d' % (degree(num, t) - degree(den, t), 2 - (degree(num, t) - degree(den, t))))
from sympy import sqrt, solve, N
print('denominator of x(6P):', factor(den))
roots = solve(11*t**2 - 6016*t + 8192, t)
print('6P = O exactly at t =', roots, '=', [N(r, 12) for r in roots])
print('check closed form 64(47 +- 27 sqrt 3)/11:', [simplify(r - 64*(47 + sg*27*sqrt(3))/11) for r, sg in zip(roots, (-1, 1))])
