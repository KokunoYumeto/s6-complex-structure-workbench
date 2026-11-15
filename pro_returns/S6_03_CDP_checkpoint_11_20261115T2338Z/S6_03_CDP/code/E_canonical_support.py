"""Exact coefficient and singular-block checks for C.2.UN.17.

The all-size matrix proof is in C.CA.7--9.  These exact examples
record the distinction between numerical and torsion canonical data.
"""
import sympy as s

mi, mj, ai, aj, ej = s.symbols('mi mj ai aj ej')
normal_i = -mj * ej / mi
adjunction_power = s.expand(mi*((ai+1)*normal_i+aj*ej))
assert s.simplify(adjunction_power-(mi*aj-mj*(ai+1))*ej) == 0
print('Raised adjunction coefficient:',s.factor(adjunction_power/ej))

negative = s.Matrix([[-2,1,0],[1,-3,1],[0,1,-2]])
assert all(x <= 0 for x in negative.inv())
v = s.Matrix([0,1,2])
c = negative.inv()*v
assert all(x <= 0 for x in c)
assert negative*c == v
print('Negative-definite block coefficient solution:',list(c))

cycle = s.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
u = s.ones(3,1)
assert cycle*u == s.zeros(3,1)
assert cycle.rank() == 2
assert all(x <= 0 for x in cycle.eigenvals())
print('Singular cycle block: positive kernel',list(u),'; rank',cycle.rank())

# An elliptic negative block and a homologically trivial cycle block.
# K=-E+q*C has K^2=-3 for every q; the numerical construction keeps E
# and discards the cycle.  The resulting twist may be flat, not torsion.
q = s.symbols('q')
matrix = s.diag(s.Matrix([[-3]]),cycle)
canonical = s.Matrix([-1,q,q,q])
effective = s.Matrix([1,0,0,0])
assert matrix*canonical == s.Matrix([3,0,0,0])
assert (canonical.T*matrix*canonical)[0] == -3
assert matrix*(canonical+effective) == s.zeros(4,1)
print('Mixed block: K^2=-3, effective A=E, K+A lies in the cycle kernel.')
print('The kernel is discarded numerically; no torsion conclusion is inferred.')
print('All exact checks passed.')
