#!/usr/bin/env python3
"""Independent sparse exterior-algebra check of the actual cap normal zero.

The code is written from the oriented seven-dimensional frame, without
importing or executing earlier cap programs. It expands wedge products
directly, rather than invoking a matrix determinant routine.
"""
import sympy as s


def wedge(left, right):
    result = {}
    for I, a in left.items():
        for J, b in right.items():
            if set(I).intersection(J):
                continue
            inversions = sum(i > j for i in I for j in J)
            index = tuple(sorted(I + J))
            result[index] = s.expand(result.get(index, 0) + (-1)**inversions*a*b)
    return {I: a for I, a in result.items() if a != 0}


def vector(entries):
    return {(j,): a for j, a in enumerate(entries) if a != 0}


def determinant_by_top_wedge(columns):
    result = {(): s.Integer(1)}
    for column in columns:
        result = wedge(result, vector(column))
    return s.factor(result.get(tuple(range(len(columns))), 0))


U, V, r, cphi, Kc = s.symbols('U V r cphi Kc', nonzero=True, real=True)
cs, ct, rs, rt, Ks, Kt, Kr = s.symbols('cs ct rs rt Ks Kt Kr', real=True)

# Coordinates: (Re x, Im x, Re y, Im y, c, Re zeta, Im zeta).
# At the chosen core minimum, r_phi=0. The other derivatives are free.
Ws = [U, 0, V, 0, cs, rs, 0]
Wt = [0, U, 0, -V, ct, rt, 0]
Wphi = [0, 0, 0, 0, cphi, 0, 0]
Xtheta = [0, 0, 0, 0, Kc, 0, 2*s.pi*r]
nball = [0, 0, 0, 0, 0, -1, 0]
N1 = [V, 0, -U, 0, 0, 0, 0]
N2 = [0, V, 0, U, 0, 0, 0]
frame = [nball, N1, N2, [-a for a in Ws], Wt, Wphi, Xtheta]
coordinate_det = determinant_by_top_wedge(frame)
ambient_det = -coordinate_det
expected = -2*s.pi*r*cphi*(U**2+V**2)**2
assert s.expand(ambient_det-expected) == 0
assert not ambient_det.has(cs, ct, rs, rt, Kc)
print('Normal-first ambient determinant:', ambient_det)
print('All page-height, radial and circle-height derivatives cancel.')

# Quotient relation, to first order at the core:
# W_phi = -s0*N1-t0*N2+cphi*dc + a real-radius term.
# X_theta = Kc*dc+2*pi*r*I. The ball normal removes the radius term.
# Thus the local section I has the same first jet as the following map.
s0, t0 = s.symbols('s0 t0', real=True)
coefficient = -Kc/(2*s.pi*r*cphi)
section = [coefficient*s0, coefficient*t0]
jacobian_columns = [
    [s.diff(section[i], variable) for i in range(2)]
    for variable in (s0,t0)
]
zero_det = determinant_by_top_wedge(jacobian_columns)
assert s.simplify(zero_det-coefficient**2) == 0
print('Local zero determinant in (N1,N2):', zero_det)
print('It is strictly positive; oriented Euler index is -sign(cphi).')
print('The disjoint spanning ball gives x=0 on its inward push.')
print('From e_v=2x-pi^*b: b(D_W-D_P)=sign(cphi).')

# Independent source-line involution divisor identity on regular/II chart.
x,y,t = s.symbols('x y t')
cubic = x**3-3*t**3*(t-1)*x+2*t**4*(t-1)*(t-s.Rational(1,2))
assert s.expand(cubic.subs(x,t**2)-t**4) == 0
print('At x=t^2 the cubic is t^4; zeros are G=(t^2,t^2), -G=(t^2,-t^2).')

# Positive-fan involution sends each first triangle to the second.
i,j,a,b = s.symbols('i j a b', integer=True)
triangle = [(i,j),(i+1,j),(i+1,j+1)]
image = [(2*a-u,2*b-v) for u,v in triangle]
A,B = 2*a-i,2*b-j
assert image == [(A,B),(A-1,B),(A-1,B-1)]
print('Positive-diagonal cone reflection verified symbolically for all lattice translates.')
print('All independent local checks passed. Global geometric comparison is recorded separately.')
