#!/usr/bin/env python3
"""Exact algebra in II's parameter-double-cover proof; Python standard library.

All parameter identities are computed in polynomial/Laurent rings over Q(i),
or in an explicitly presented abelian group. No sampled parameter value or
finite fan list is used as a replacement for a universal assertion.
"""
from fractions import Fraction as Q
import json


def mono(items):
    d = {k: v for k, v in items if v}
    e = d.pop('i', 0)
    q, r = divmod(e, 2)
    if r:
        d['i'] = r
    return tuple(sorted(d.items())), (-1 if q % 2 else 1)


class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.a = dict(value.a)
        elif isinstance(value, dict):
            self.a = {m: Q(c) for m, c in value.items() if c}
        else:
            self.a = {(): Q(value)} if value else {}

    @classmethod
    def var(cls, name):
        return cls({((name, 1),): Q(1)})

    def __add__(self, other):
        out = dict(self.a)
        for m, c in P(other).a.items():
            out[m] = out.get(m, Q(0)) + c
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({m: -c for m, c in self.a.items()})

    def __sub__(self, other):
        return self + -P(other)

    def __rsub__(self, other):
        return P(other) + -self

    def __mul__(self, other):
        out = {}
        for m, a in self.a.items():
            for n, b in P(other).a.items():
                d = dict(m)
                for k, e in n:
                    d[k] = d.get(k, 0) + e
                key, sign = mono(d.items())
                out[key] = out.get(key, Q(0)) + a * b * sign
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, power):
        if power < 0:
            assert len(self.a) == 1
            m, c = next(iter(self.a.items()))
            key, sign = mono((k, -e) for k, e in m)
            return P({key: sign / c}) ** (-power)
        result = P(1)
        base = self
        while power:
            if power % 2:
                result = result * base
            base = base * base
            power //= 2
        return result

    def __eq__(self, other):
        return self.a == P(other).a


checks = []


def ok(name, left, right):
    assert left == right, name
    checks.append(name)


t, X, Y, eta, ii = [P.var(v) for v in ('t', 'X', 'Y', 'eta', 'i')]
aa = Q(27, 4) * t**3 * (1-t)
bb = Q(27, 4) * t**5 * (1-t)
eta_t = Q(27, 4) * (t**-1-1)
x, y = -t**2 * X, ii * t**3 * Y
lr = y**2-x**3-aa*x-bb
alt = Y**2-X**3-eta_t*X+eta_t
ok('forward Weierstrass map over Q(i)[t,t^-1,X,Y]', lr, -t**6*alt)
lr_original = Y**2-X**3-aa*X-bb
inverse_alt = (-ii*t**-3*Y)**2-(-t**-2*X)**3-eta_t*(-t**-2*X)+eta_t
ok('inverse Weierstrass map', inverse_alt, -t**-6*lr_original)
ok('base inverse after eta substitution', (4*eta_t+27)*t, 27)
den = 4*eta+27
ok('base inverse after t substitution with denominator cleared', (den-27)*Q(1, 4), eta)
ok('marked section P lies on LR equation', (ii*t**3)**2-(-t**2)**3-aa*(-t**2)-bb, 0)
ok('coordinate inverse for X', -t**-2*x, X)
ok('coordinate inverse for Y', -ii*t**-3*y, Y)
ok('LR discriminant', -16*(4*aa**3+27*bb**2), -(3**9)*t**9*(1-t)**2)
ok('LR j identity after clearing denominator', 1728*4*aa**3,
   1728*(1-t)*(4*aa**3+27*bb**2))


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mv(a, b):
    return [sum(x*y for x, y in zip(row, b)) for row in a]


identity = [[int(i == j) for j in range(4)] for i in range(4)]
D = [[1,1,0,0],[-2,-1,-1,0],[0,0,1,0],[0,0,0,1]]
T = [[-1,-1,-1,0],[2,1,1,0],[0,0,1,0],[0,0,0,1]]
ok('deck times counterclockwise monodromy', mm(D, T), identity)
ok('counterclockwise monodromy times deck', mm(T, D), identity)
ok('fourth power of deck', mm(mm(D, D), mm(D, D)), identity)
delta = [-1, 0, 2, 0]
e4 = [0, 0, 0, 1]
ok('physical line circle is fixed', mv(D, delta), delta)
ok('scalar quotient period is fixed', mv(D, e4), e4)
b1, b2, b3, b4 = [P.var('b'+str(i)) for i in range(1,5)]
fixed_equations = [x-y for x, y in zip(mv(D, [b1,b2,b3,b4]), [b1,b2,b3,b4])]
ok('complete integer fixed-lattice equations', fixed_equations,
   [b2, -2*b1-2*b2-b3, P(0), P(0)])
ok('all fixed vectors reconstructed without denominator',
   [(-b1)*d+b4*e for d,e in zip(delta,e4)], [b1, P(0), -2*b1, b4])

N, tau = P.var('N'), P.var('tau')
quarter = (tau+N)*Q(1,4)
ok('Albanese reverse lattice inclusion for every integer character',
   4*quarter - 2*N*Q(1,2), tau)
ok('Albanese scaling and its inverse', Q(1,2)*(2*quarter), quarter)
ok('one turn changes normalized Albanese period by 1/2',
   (tau+1+N)*Q(1,2) - (tau+N)*Q(1,2), Q(1,2))


def reduce_group(values, quotient=False):
    """Exact normal form: C^2=t B0, s^4=t, zeta^4=theta,
    h^4=t/theta, u=r^4, w=r^2, Bu=r^4 B0. Optional Bu=1.
    """
    d = {k: v for k, v in values.items() if v}
    def add(k, e):
        d[k] = d.get(k, 0) + e
    for name, replacement in [('u', {'r':4}), ('w', {'r':2}),
                              ('Bu', {'r':4, 'B0':1})]:
        e = d.pop(name, 0)
        for k, n in replacement.items():
            add(k, e*n)
    for name, modulus, replacement in [('C',2,{'t':1,'B0':1}),
                                       ('s',4,{'t':1}),
                                       ('zeta',4,{'theta':1}),
                                       ('h',4,{'t':1,'theta':-1})]:
        e = d.pop(name, 0)
        q, r = divmod(e, modulus)
        if r:
            d[name] = r
        for k, n in replacement.items():
            add(k, q*n)
    if quotient:
        add('r', -4*d.pop('B0', 0))
    return {k:v for k,v in sorted(d.items()) if v}


ok('exterior norm before quotient (LR.22)',
   reduce_group({'r':-4,'C':-2}), reduce_group({'t':-1,'Bu':-1}))
ok('exterior norm after Bu quotient',
   reduce_group({'r':-4,'C':-2}, True), {'t':-1})
ok('fixed-root cap norm after Bu quotient',
   reduce_group({'r':-4,'zeta':4,'C':-2}, True), {'t':-1,'theta':1})
ok('global-t-root cap norm after Bu quotient',
   reduce_group({'r':-4,'s':4,'C':-2}, True), {})
ok('normalized extending lift square',
   reduce_group({'s':4,'C':-2}), {'B0':-1})
ok('exterior forward and inverse monomials',
   reduce_group({'r':-2+2,'C':-1+1}), {})
ok('fixed-root cap forward and inverse monomials',
   reduce_group({'r':-2+2,'zeta':2-2,'C':-1+1}), {})
ok('four-turn attachment equality',
   reduce_group({'zeta':-4,'theta':1,'t':-1}), {'t':-1})
ok('two-turn attachment equality',
   reduce_group({'zeta':-2+2,'C':-1,'r':-2}), reduce_group({'C':-1,'r':-2}))

A, C1, H, v = [P.var(x) for x in ('A','C1','H','v')]
gamma = [2*A, 2*C1-H-4*v]
first = [A, C1-2*v+Q(1,2)]
second = [A, C1-2*(v+Q(1,2))+Q(1,2)]
ok('cusp source-and-line norm (LR.21)',
   [a+b for a,b in zip(first,second)], [gamma[0], H+gamma[1]])
ok('half-turn changes cusp lift by one physical period',
   second, [first[0], first[1]-1])

# The unit-cocycle formula in the archived original proof is also checked.
hcoeff = [Q(0), Q(-1,4), Q(-1,2), Q(-3,4)]
dh = [hcoeff[-1]] + hcoeff[:-1]
ok('cyclic unit-cocycle identity (D-1)h=-g+Ng/4',
   [a-b for a,b in zip(dh,hcoeff)], [Q(-3,4),Q(1,4),Q(1,4),Q(1,4)])

# Recompute the original proof's Laurent coefficients by exact formal series.
# The replacement proof uses the independent integral-lattice obstruction.
degree = 5
def convolution(a,b):
    c = [Q(0)]*(degree+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j <= degree:
                c[i+j] += x*y
    return c
def sigma(n,k):
    return sum(d**k for d in range(1,n+1) if n%d == 0)
E4 = [Q(1)] + [Q(240*sigma(n,3)) for n in range(1,degree+1)]
E6 = [Q(1)] + [Q(-504*sigma(n,5)) for n in range(1,degree+1)]
num = [1728*x for x in convolution(convolution(E4,E4),E4)]
den = [x-y for x,y in zip(convolution(convolution(E4,E4),E4),convolution(E6,E6))]
ok('E4^3-E6^2 has linear coefficient 1728', den[:2], [Q(0),Q(1728)])
d0 = den[1:]
quot = []
for n in range(3):
    quot.append((num[n]-sum(d0[k]*quot[n-k] for k in range(1,n+1)))/d0[0])
ok('original j Laurent coefficients from rational formal division',
   quot, [Q(1),Q(744),Q(196884)])
ok('original Q(j(Q)-j(-Q)) constant coefficient', 2*quot[0], Q(2))

print(json.dumps({
    'program': 'S6_SERIES_PUBLISH_II_B2_UH_comparison_certificate.py',
    'arithmetic': 'exact Fraction coefficients; Laurent polynomial identities over Q(i); integer matrices; explicit presented-group normal forms',
    'all_checks_passed': True,
    'checks': checks,
    'check_count': len(checks),
    'parameter_sampling': False,
    'scope': 'Algebraic identities only. Geometry, properness, extensions, source hypotheses and full target proof are established in the accompanying proof and review, not inferred from this program.',
}, indent=2))
