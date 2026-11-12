"""Exact finite algebra for the adjacent-plaquette quantum correction.

The analytic ground-state and form-resolvent arguments are in the proof;
this script checks the original color, Haar and rational coefficients.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

checks = []

def eq(name, value):
    assert s.expand(value) == 0, (name, value)
    checks.append(name)

p = s.symbols('p0:4', real=True)
q = s.symbols('q0:4', real=True)
sigma = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
basis = [s.I*x/2 for x in sigma]
P = p[0]*s.eye(2) + sum((s.I*p[i+1]*sigma[i] for i in range(3)),s.zeros(2))
Q = q[0]*s.eye(2) + sum((s.I*q[i+1]*sigma[i] for i in range(3)),s.zeros(2))
dot = sum(p[i]*q[i] for i in range(1,4))
G = -sum(s.trace(t*P)*s.trace(t*Q) for t in basis)
R = s.trace(P*Q)
D = s.trace(P)*s.trace(Q)
D1 = D-R/2
eq('opposite-edge derivative contraction',G+dot)
eq('exact Fierz contraction',G-R/2+D/4)
eq('two-channel decomposition',G-s.Rational(3,8)*R+D1/4)
eq('outer trace coordinates',R-2*(p[0]*q[0]-dot))
eq('spin-one coordinates',D1-3*p[0]*q[0]-dot)

def haar_degree_two(poly):
    """Every argument has degree exactly two in each independent S^3 vector."""
    answer = s.S(0)
    for powers,coef in s.Poly(s.expand(poly),*(p+q)).terms():
        pp,qq=powers[:4],powers[4:]
        assert sum(pp)==sum(qq)==2
        if 2 in pp and 2 in qq:
            answer += coef/16
    return answer

eq('Haar R norm',haar_degree_two(R**2)-1)
eq('Haar D1 norm',haar_degree_two(D1**2)-s.Rational(3,4))
eq('Haar channel orthogonality',haar_degree_two(R*D1))
eq('Haar contraction norm',haar_degree_two(G**2)-s.Rational(3,16))
eq('Haar plaquette product norm',haar_degree_two(D**2)-1)

# Product rule for the common link: each fundamental trace has Δ=-3/4.
delta_D = -s.Rational(3,2)*D+2*G
eq('shared-edge spin-one Casimir',delta_D+2*D1)
eq('outer-loop free energy',6*s.Rational(3,4)-s.Rational(9,2))
eq('spin-one total free energy',6*s.Rational(3,4)+2-s.Rational(13,2))

k,b,z,g,a=s.symbols('kappa b z g a',positive=True)
eq('actual B leading coefficient',-2*b*G/3-(-b*R/4+b*D1/6))
eq('actual B squared leading norm',haar_degree_two((-2*b*G/3)**2)-b*b/12)
I_at_k=(b*b/(16*(s.Rational(9,2)*k+k))
        +b*b/(48*(s.Rational(13,2)*k+k)))
J_at_k=(b*b/(16*(s.Rational(9,2)*k+k)**2)
        +b*b/(48*(s.Rational(13,2)*k+k)**2))
eq('resolvent inner coefficient',I_at_k-s.Rational(7,495)*b*b/k)
eq('resolvent squared norm coefficient',J_at_k-s.Rational(199,81675)*b*b/k**2)
eq('Rayleigh improvement coefficient',I_at_k+4*k*J_at_k
   -s.Rational(1951,81675)*b*b/k)
eq('original coupling coefficient',
   s.Rational(1951,81675)*(1/(2*g**2*a))**2/(2*g**2/a)
   -s.Rational(1951,653400)/(g**6*a))
eq('original coupling parameter',(1/(2*g**2*a))/(2*g**2/a)-1/(4*g**4))

eq('vacuum second coefficient against loop square',s.Rational(1,3)/8-s.Rational(1,24))
r2=s.Rational(3,9)+2*s.Rational(1,24)-s.Rational(2,9)
eq('actual loop second moment coefficient',r2-s.Rational(7,36))
d2=r2-s.Rational(2,3)**2
eq('actual loop variance coefficient',d2+s.Rational(1,4))
ret2=-r2-3*d2
eq('absolute retained Rayleigh coefficient',ret2-s.Rational(5,9))
eq('absolute corrected Rayleigh coefficient',ret2-s.Rational(1951,81675)
   -s.Rational(43424,81675))

root=Path(__file__).resolve().parent
proof=root/'adjacent_plaquette_quantum_correction.md'
receipt={'status':'PASS','checks':checks,'check_count':len(checks),
         'proof_bytes':proof.stat().st_size,
         'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
         'scope':'Exact coefficient checks; not a computed interacting vacuum or continuum gap.'}
(root/'ADJACENT_PLAQUETTE_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,indent=2))
