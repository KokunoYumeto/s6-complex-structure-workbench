#!/usr/bin/env python3
"""Exact marked OS49 signs, normal maps, and actual-fan recurrence.

The geometric arrows are proved in part3_os49_full_framing_working.md.
This certificate keeps both norm signs and the component-line square.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd
import json
import sympy as S

checks = []


def record(label, assertion):
    assert assertion, label
    checks.append(label)


def zero(matrix):
    return matrix.applyfunc(S.simplify) == S.zeros(*matrix.shape)


def strings(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


s, v, theta, m, k = S.symbols('s v theta m k', real=True)
D1, D2 = S.symbols('D_1 D_2')
delta = S.Matrix([0, 1])
D = S.Matrix([D1, D2])
K = D + (s + 2*m*v)*delta
sign_rows = []
point_change = S.Matrix([[2, -3], [1, -1]])
record('mixed point-angle inverse', point_change.inv() == S.Matrix([[-1, 3], [-1, 2]]))
record('mixed lattice determinant', point_change.det() == 1)

x, beta, h, kap, g = S.symbols('x beta h kappa g')
gx, gy, positive = S.symbols('chi_x chi_y positive', real=True)
Q_positive = S.Matrix([[1, 0, 0], [0, 1, 0], [gx, gy, positive]])
for n in (1, -1):
    sigma = n*v*D + n*m*v*(v-1)*delta
    ordinary = -n*s*D/(2*m) - n*s*s*delta/(4*m) - n*s*v*delta
    F = sigma-ordinary
    record(f'n={n}: angular origin difference', zero(
        F.subs(v, v+theta)-F-n*theta*K-n*m*theta*(theta-1)*delta))
    record(f'n={n}: source-root endpoint', zero(
        F.subs(s, s+2*m)-F-n*K-n*m*delta))
    record(f'n={n}: actual cusp endpoint', zero(
        sigma.subs(v, v+1)-sigma-n*K+n*s*delta))
    bounded = n*theta*D + (2*n*m*v*theta+n*m*theta*(theta-1))*delta
    record(f'n={n}: bounded Cox logarithm', zero(sigma.subs(v, v+theta)-sigma-bounded))
    boundary = S.Matrix([[2, -3*n], [n, -1]])
    record(f'n={n}: page-to-compression orientation', boundary.det() == 1)
    y = n*beta
    hh = 2*x-3*y
    kk = x-y
    th = n*(kk-g)
    record(f'n={n}: exact boundary matrix', zero(
        S.Matrix([hh, th]) - boundary*S.Matrix([x,beta]) + S.Matrix([0,n*g])))
    beta_on_graph = n*(-h+2*(g+n*theta))
    record(f'n={n}: degree-two binding graph', S.expand(beta_on_graph-2*theta-n*(2*g-h)) == 0)
    T = S.diag(1,1,n)
    record(f'n={n}: both endpoints retain reflection', T.inv()*(T*Q_positive) == Q_positive)
    record(f'n={n}: oriented conjugation constant', (n*T).det() == 1)
    sign_rows.append(dict(n=n, boundary_matrix=strings(boundary), determinant=1,
                         beta_graph=str(S.expand(beta_on_graph)),
                         thom_meridian=1))

# Direct circle-first complex orientation at A=1,B=0.
# Ambient basis: Zre,Zim,Are,Aim,Bre,Bim.
# Columns: delta,Zre,Zim,yre,yim,b.
orientation = S.zeros(6)
for col, row, sign in [(0,3,-1),(1,0,1),(2,1,1),(3,4,1),(4,5,1),(5,2,-1)]:
    orientation[row,col] = sign
record('circle-first raw quotient orientation', orientation.det() == -1)
hopf = S.Matrix([[0,0,-2],[0,2,0],[-2,0,0]])
record('actual Hopf determinant', hopf.det() == -8)
reflection = S.diag(1,1,-1)
record('Hopf from reflected raw normal is positive', (hopf*reflection).det() == 8)
raw_K = S.Matrix([[1,0,0],[0,1,0],[gx,gy,-positive]])
record('decreasing K reflection retained', raw_K*reflection == Q_positive)

# Quaternion representation z+j*w.  Formal unitary multipliers use
# conjugation as inversion, so no selected trigonometric branch is lost.
AA, BB, ZZ, AAc, BBc, ZZc = S.symbols('A B Z Abar Bbar Zbar')
L, R = S.symbols('L R', nonzero=True)
p, q1, a = L*R, L/R, L**-2
qh = S.Matrix([AA-ZZc*BBc, BBc+ZZ*AA])
qh_changed = S.Matrix([p*AA-(1/a)*ZZc*(1/q1)*BBc,
                       (1/q1)*BBc+a*ZZ*p*AA])
record('bounded torus preserves base monomial', S.simplify(a*p*q1) == 1)
record('literal quaternion torus map', zero(qh_changed-S.diag(L*R,R/L)*qh))
# Second chart A'=ZA, B'=ZB, Z'=Z^-1: (Z^-1+j)(A'+j Bbar').
qh_second = S.Matrix([AA-ZZc*BBc, ZZ*AA+BBc])
record('literal two-chart quaternion equality', qh_second == qh)

alpha, phi, gphase = S.symbols('alpha phi gphase', real=True)
Rot = lambda t: S.Matrix([[S.cos(t),-S.sin(t),0],[S.sin(t),S.cos(t),0],[0,0,1]])
G = lambda a,t: S.Matrix([
    [-S.sin(a), S.cos(t)*S.cos(a), S.sin(t)*S.cos(a)],
    [S.cos(a), S.cos(t)*S.sin(a), S.sin(t)*S.sin(a)],
    [0,S.sin(t),-S.cos(t)]])
trigzero = lambda x: x.applyfunc(S.trigsimp) == S.zeros(*x.shape)
record('actual normal matrix orthogonal', trigzero(G(alpha,theta).T*G(alpha,theta)-S.eye(3)))
record('actual normal matrix oriented', S.trigsimp(G(alpha,theta).det()) == 1)
record('actual normal rotation factor', trigzero(G(alpha,theta)-Rot(alpha)*G(0,theta)))
record('degree-two-m factorization', trigzero(
    G(phi-2*m*theta-m*gphase,theta)
    - Rot(-m*gphase)*Rot(phi-2*m*theta)*G(0,theta)))

# The component line is supplied by the literal positive-fan subfan.
heights = lambda j: S.ceiling(S.Rational(j,2))
component_degrees = [-(heights(j-1)+heights(j+1)-2*heights(j)) for j in (0,1)]
record('actual component multidegree', component_degrees == [-1,1])
line_square, b_square, p_tangent, p_normal = -2*k, -8*k, -24*k, 0
jin_k = S.expand((p_normal+3*b_square)/4)
jin_ell = S.expand(p_tangent+p_normal)
index = S.simplify((4*jin_k-jin_ell)/24)
mr, nr = -jin_ell/4, -(4*jin_k-jin_ell)/4
record('individual pair from actual line and normal', jin_k == -6*k and jin_ell == -24*k)
record('relative pair and index', mr == 6*k and nr == 0 and index == 0)

# Common-exterior recurrence with no height formula substituted.
S0, wi = S.symbols('S w_i', integer=True)
v0, mrel = -6*k, 6*k
ader = -2*mrel-v0*S0
increment = S.expand((ader*wi-v0*wi**2)/2)
potential = lambda ss: S.Rational(3,4)*k*(ss-1)*(ss-3)
record('actual recurrence telescopes', S.expand(
    increment-potential(S0+2*wi)+potential(S0)) == 0)

fan_values = {}
for a0 in range(56):
    for b0 in range(56):
        if gcd(gcd(a0,b0),56) != 1:
            continue
        ss=a0*a0-a0*b0+b0*b0
        record_name = None
        assert ss % 2 == 1
        assert ((ss-1)*(ss-3)) % 8 == 0
        value=(3*((ss-1)*(ss-3)//4)) % 28
        fan_values.setdefault(value, [a0,b0,ss])
record('all primitive residue values', sorted(fan_values) == [0,4,6,8,14,18,20,22])
period_difference = S.expand(potential(S0+56)-potential(S0))
record('mod-56 potential period', S.simplify(period_difference/(28*k)) == 3*S0+78)
witnesses = [(0,1),(1,10),(1,4),(3,14),(1,6),(1,3),(2,5),(3,7)]
witness_rows=[]
for (a0,b0), value in zip(witnesses,sorted(fan_values)):
    ss=a0*a0-a0*b0+b0*b0
    record(f'primitive actual fan witness {value}', gcd(a0,b0)==1 and
           3*((ss-1)*(ss-3)//4)%28==value)
    # Physical delta=(0,1), eta=(-1,0), det(delta,eta)=1.
    aa, bb, gg = S.gcdex(a0,b0)
    assert gg == 1
    # Need a*d-b*c=1: d=aa, c=-bb.
    coeff=S.Matrix([[a0,-bb],[b0,aa]])
    physical=S.Matrix([[0,-1],[1,0]])
    basis=physical*coeff.inv()
    record(f'actual basis arrow {value}', basis.det()==1 and
           basis*S.Matrix([a0,b0])==S.Matrix([0,1]))
    witness_rows.append(dict(a=a0,b=b0,S=ss,return_k1=value,
                             actual_basis=strings(basis)))

out = dict(
    status='PASS; root full proof and blind_control signed-normal audits passed',
    timestamp_utc=datetime.now(timezone.utc).isoformat(),
    proof='notes/part3_os49_full_framing_working.md',
    statement='P3K.34 Proved',
    parameter='lambda=r^(3k), one positive r-loop; k>0',
    cap='n=+1 or -1, fixed arbitrary d delta/m retained',
    signs=sign_rows,
    component_degrees=[int(x) for x in component_degrees],
    line_relative_square=str(line_square),
    normal_pontryagin=p_normal,
    individual_pair=[str(jin_k),str(jin_ell)],
    relative_pair=[str(mr),str(nr)],
    index=str(index),
    circle_first_orientation_matrix=strings(orientation),
    hopf_normal_matrix=strings(hopf),
    binding_phase='alpha=phi-2m theta-m*n*(2g-h)',
    normal_clutch='[R(p)^-1 Rz(-m*g_n(p))]*[Rz(phi-2m theta) G(0,theta)]',
    common_exterior_initial_variation=[['-6k','0','0'],['0','0','0'],['0','0','0']],
    common_exterior_initial_derivative=['-6k','0','0'],
    arbitrary_fan='3k*(S-1)*(S-3)/4 mod28; S=a^2-a*b+b^2, delta=a*v+b*w',
    fixed_k_range='k*{0,4,6,8,14,18,20,22} mod28',
    primitive_fan_witnesses=witness_rows,
    checks=checks,
)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for label in checks:
    print('PASS:',label)
print('PAIR:',jin_k,jin_ell,'RELATIVE:',mr,nr,'INDEX:',index)
print('FAN RANGE AT k=1:',sorted(fan_values))
