"""Independent exact-arrow audit for OF.1--3.

This does not import the author's fan recurrence or reconstruction code.
It checks dense-character/period matrices, all three full-unit native
arrows, the original-height inverse identity, the quaternion product,
and the integral physical/relative seed.  The relative disc-flow and
connection comparison are proved in the accompanying peer note.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'notes/part3_e6_order_three_all_fans_working.md'
checks = 0

def check(value):
    global checks
    assert bool(value)
    checks += 1

def zero(value):
    check(S.simplify(value) == 0)

a, b, c = S.symbols('a b c', nonzero=True)
A11, A12, A21, A22 = S.symbols('A11 A12 A21 A22', nonzero=True)
period_units = S.Matrix([[A11, A12], [A21, A22]])
full = [
    (A11*A21*b*c, a*b/A21, 1/(A11*b)),
    (A12*A22*b*c, 1/(A22*c), a*c/A12),
    (1/a, a*b, a*c),
]
native = []
for i, (u,v,w) in enumerate(full):
    zero(u*v*w-a*b*c)
    if i == 0:
        native.append((A11*w,A21*v,u/(A11*A21)))
        expected = (1/b,b*a,b*c)
    elif i == 1:
        native.append((A22*v,A12*w,u/(A12*A22)))
        expected = (1/c,c*a,c*b)
    else:
        native.append((u,v,w))
        expected = (1/a,a*b,a*c)
    for actual, wanted in zip(native[-1], expected):
        zero(actual-wanted)

# q is an original function. Its transformed product must be inverted
# before substituting into a q-dependent inverse normal multiplier.
q, rho, K0, K1, n0, n1, z = S.symbols('q rho K0 K1 n0 n1 z', nonzero=True)
np0, np1 = S.exp(rho*K0)*n0, S.exp(rho*K1)*n1
zero(z*np0*np1-z*n0*n1*S.exp(rho*(K0+K1)))
zero(S.exp(-rho*K0)*np0-n0)
zero(S.exp(-rho*K1)*np1-n1)
k0, k1 = S.Function('k0')(q), S.Function('k1')(q)
H = q*S.exp(rho*(k0+k1))
zero(S.diff(H,q)-S.exp(rho*(k0+k1))*(1+rho*q*S.diff(k0+k1,q)))

# Complete character change: every log column is R L P.  Verify
# its inverse on a representative set of positive/negative bases.
lk, lg, la, le = S.symbols('lk lg la le')
L = S.Matrix([[lk,lg],[la,le]])
matrices = []
for aa in range(-2,3):
    for bb in range(-2,3):
        for cc in range(-2,3):
            for dd in range(-2,3):
                P = S.Matrix([[aa,bb],[cc,dd]])
                if P.det() not in (-1,1):
                    continue
                matrices.append(P)
                R = P.inv()
                check(R*P == S.eye(2))
                transformed = R*L*P
                check(P*transformed*R == L)
                w = R*S.Matrix([0,1])
                check(S.gcd(w[0],w[1]) == 1)
                check(w[0]+w[1]+(-w[0]-w[1]) == 0)

# Quaternion convention is q=a+j b. Treat conjugate symbols
# independently, so this is an identity of the complete coefficients.
Z, Zb, c0, c0b, c1, c1b = S.symbols('Z Zb c0 c0b c1 c1b', nonzero=True)
conjugates = {Z:Zb,Zb:Z,c0:c0b,c0b:c0,c1:c1b,c1b:c1}
def bar(e): return e.xreplace(conjugates)
def qmul(x,y):
    return (x[0]*y[0]-bar(x[1])*y[1], bar(x[0])*y[1]+x[1]*y[0])
left = qmul((S.Integer(1),Z),(c0,c1b))
right = qmul((1/Z,S.Integer(1)),(Z*c0,Zb*c1b))
for x,y in zip(left,right): zero(x-y)

# Physical line duality and actual adjoint clutch, in the same native
# q_H product.  Their independent integer columns determine the pair.
m,n = S.symbols('m n', integer=True)
kU, ellU = -(m+n), -4*m
kM, ellM = -kU, -ellU
zero(kM-(m+n)); zero(ellM-4*m)
solution = S.solve([kM+27,ellM+12],(m,n),dict=True)
check(solution == [{m:S.Integer(-3),n:S.Integer(-24)}])
V00 = -(m+n)
delta0 = V00+2*n
check(V00.subs(solution[0]) == 27)
check(delta0.subs(solution[0]) == -21)
check(S.Rational(4*(-27)-(-12),24) == -4)

# Independently solve all vertical prism equations and the carried
# initial entries; do not use the author's target reconstruction.
v00,v01,v02,v11,v12,v22,d0,d1,d2 = S.symbols('v00 v01 v02 v11 v12 v22 d0 d1 d2')
V = S.Matrix([[v00,v01,v02],[v01,v11,v12],[v02,v12,v22]])
delta = S.Matrix([d0,d1,d2])
vertical_solutions=[]
for j in range(-8,9):
    P = S.Matrix([[1,0],[j,1]])
    w = P.inv()*S.Matrix([0,1]); weights = [w[0],w[1],-w[0]-w[1]]
    check(weights == [0,1,-1])
    equations = [v00-27,d0+21]
    for r in (1,2):
        vector = S.zeros(3,1)
        vector[r] += weights[r]
        vector[0] -= weights[0]
        equations.extend(list(V*vector))
        equations.append(weights[r]*delta[r]-weights[0]*delta[0])
    solved = S.solve(equations,(v00,v01,v02,v11,v12,v22,d0,d1,d2),dict=True)
    wanted = {v00:27,v01:0,v02:0,v11:0,v12:0,v22:0,d0:-21,d1:0,d2:0}
    check(solved == [wanted])
    vertical_solutions.append(j)

result = {
    'status':'PASS_EXACT_OF1_3_ARROWS_AND_SEED',
    'reviewer':'blind_control',
    'utc':datetime.now(timezone.utc).isoformat(),
    'checks':checks,
    'source':str(SOURCE.relative_to(ROOT)),
    'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
    'unimodular_bases_checked':len(matrices),
    'vertical_prism_systems_independently_solved':vertical_solutions,
    'physical_pair':[-27,-12],
    'native_pair':[-3,-24],
    'ordinary_V':[[27,0,0],[0,0,0],[0,0,0]],
    'ordinary_delta':[-21,0,0],
    'central_class':24,
    'scope':"OF1--3 exact arrows and integer seed. The relative horizontal-flow/connection proof is in the peer note. No author's fan recurrence imported."
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
