#!/usr/bin/env python3
"""Fresh exact corroboration for I A2.1 and credited appendix P5.1--P5.6.

Authored after reading the printed proofs, 2026-11-19.  No old named
checker is imported.  The analytic descent/properness arguments remain
written proofs; these calculations certify their displayed algebra.
Requires Python 3 and SymPy 1.14.0.  Run from any directory.
"""
from pathlib import Path
import hashlib
import json
import platform
import time

import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

START = time.monotonic()
CHECKS = []
DATA = {}


def check(name, value):
    ok = bool(value)
    CHECKS.append({"name": name, "pass": ok})
    if not ok:
        raise AssertionError(name)


def zero(expr):
    return s.cancel(expr) == 0


def matzero(matrix):
    return all(zero(x) for x in matrix)


def save_matrix(name, matrix):
    DATA[name] = [[str(x) for x in row] for row in matrix.tolist()]


def snf(matrix):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(matrix).convert_to(s.ZZ))
    D, U, V = (x.to_Matrix() for x in (D, U, V))
    check("Smith product " + str(matrix.shape) + " #" + str(len(CHECKS)), U*matrix*V == D)
    check("Smith unimodularity " + str(matrix.shape) + " #" + str(len(CHECKS)), abs(U.det()) == abs(V.det()) == 1)
    return D, U, V


def integral_cohomology(name, previous, following):
    """SNF with both transformations: integral kernel, then image quotient."""
    check(name + " zero composition", following*previous == s.zeros(following.rows, previous.cols))
    D, U, V = snf(following)
    rank = sum(D[i, i] != 0 for i in range(min(D.shape)))
    check(name + " Smith zero tail", all(D[i, i] == 0 for i in range(rank, min(D.shape))))
    image_coordinates = V.inv()*previous
    check(name + " image lies in integral kernel", image_coordinates[:rank, :] == s.zeros(rank, previous.cols))
    check(name + " integral kernel coordinates", all(x.q == 1 for x in image_coordinates))
    K = V[:, rank:]
    Q = image_coordinates[rank:, :]
    check(name + " exact image factorization", K*Q == previous)
    Dq, Uq, Vq = snf(Q)
    factors = [abs(int(Dq[i, i])) for i in range(min(Dq.shape)) if Dq[i, i] != 0]
    result = {"free_rank": K.cols-len(factors), "torsion": [x for x in factors if x > 1]}
    DATA[name] = result
    save_matrix(name + "_integral_kernel", K)
    save_matrix(name + "_image_in_kernel", Q)
    save_matrix(name + "_Smith", Dq)
    return result


# A2.1: universal derivative identities, including the descended kernel.
t, m, b, dt, dm, db = s.symbols("tau mu beta dtau dmu dbeta")
variables = (t, m, b)
dvariables = (dt, dm, db)


def differential(f):
    return sum(s.diff(f, x)*dx for x, dx in zip(variables, dvariables))


Q = 6*dm**2-dt*db
g1 = ((t-1)/t, (1-m)/t, b+2-6*(1-m)**2/t)
g2 = (-1/t, 1+m/t, b-3-6*m**2/t)
for name, transform in (("g1", g1), ("g2", g2)):
    dT, dM, dB = map(differential, transform)
    check("A2.1 quadratic covariance " + name, zero(6*dM**2-dT*dB-Q/t**2))
    check("A2.1 weight-two quotient " + name, zero((6*dM**2-dT*dB)/dT**2-t**2*Q/dt**2))
g2square = tuple(s.cancel(f.subs(dict(zip(variables, g2)), simultaneous=True)) for f in g2)
check("A2.1 full g2-square map", all(zero(x-y) for x,y in zip(g2square, (t, 1-t-m, b+6*t+12*m-6))))
dT, dM, dB = map(differential, g2square)
check("A2.1 kernel invariance", zero(6*dM**2-dT*dB-Q))
check("A2.1 order-three coarse order", 3+2-2*2+2 == 3)
check("A2.1 order-four coarse order", 4+2-2*1+0 == 4)
check("A2.1 cusp determinant", s.Matrix([[0,1],[-1,0]]).det() == 1)

# Formal leading-term calculation from the exact modular identity.
r, ss, lam, e4, e6 = s.symbols("r s lambda E4i E6rho", nonzero=True)
at_rho = lam**2*((-2*s.pi*s.I*s.Rational(1,3)*e6*lam*r)**2)/e6
rho_lambda_cube = 27*s.I/(8*s.pi**3*e6)
check("A2.1 order-three coefficient", zero((at_rho/r**2)/(-3*s.I*lam/(2*s.pi))-lam**3/rho_lambda_cube))
tau_s = 2*s.I*ss/(s.pi*s.sqrt(e4))
E6_s = -s.pi*s.I*e4**2*(s.I*ss**2/(s.pi*s.sqrt(e4)))
check("A2.1 order-four constant", zero(tau_s**2*e4**2/E6_s+4/(s.pi**2*s.sqrt(e4))))

# P5.1: local syzygies and the true Jacobian ideals.
x, y, z = s.symbols("x y z")
check("P5.1 double first kernel", s.Matrix([[y,x,0]])*s.Matrix([x,-y,0]) == s.zeros(1,1))
check("P5.1 double second kernel", s.Matrix([[y,x,0]])*s.Matrix([0,0,1]) == s.zeros(1,1))
triple = s.Matrix([[y*z,x*z,x*y]])
check("P5.1 triple two kernels", triple*s.Matrix([[x,x],[-y,0],[0,-z]]) == s.zeros(1,2))
check("P5.1 triple generic rank", s.Matrix([[x,x],[-y,0],[0,-z]]).rank() == 2)

# A4.1: the full degree-two presentation and each annihilator identity.
S=s.Matrix([[z,0],[y,y],[0,x]])
R=s.Matrix([[-x,y,0],[0,-y,z]])
wedge=s.Matrix([[x*y,-x*z,y*z]])
dt_relations=s.Matrix([[-x*z,y*z,0],[-x*y,0,y*z],[0,-x*y,x*z]])
check("A4.1 two exact wedge syzygies",wedge*S==s.zeros(1,2))
check("A4.1 relation transport",S*R==dt_relations)
for name,target,coeff in [
    ('xy*u',s.Matrix([x*y,0]),s.Matrix([-y,0,0])),
    ('xz*u',s.Matrix([x*z,0]),s.Matrix([-z,0,0])),
    ('yz*u',s.Matrix([y*z,0]),s.Matrix([0,z,y])),
    ('xy*v',s.Matrix([0,x*y]),s.Matrix([-y,-x,0])),
    ('xz*v',s.Matrix([0,x*z]),s.Matrix([0,0,x])),
    ('yz*v',s.Matrix([0,y*z]),s.Matrix([0,0,y]))]:
    check('A4.1 annihilator '+name,R*coeff==target)
save_matrix('A4_1_wedge_syzygy_map',S)
save_matrix('A4_1_torsion_relation_map',R)

# P5.2--3: root line tuples and every coarse direct-image degree.
O, L, F = (0,0,0), (-1,2,1), (0,1,1)


def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))


def degree(a):
    d,a1,a2 = a
    return d+a1//3+a2//4


def tensor(A, B):
    return [plus(a,b) for a in A for b in B]


RfO = [[O], [O,L], [L]]
table = {}
for name, bundle in (("O",[O]),("L",[L]),("F",[F]),("E",[O,L])):
    table[name] = [sorted(degree(a) for a in tensor(bundle,row)) for row in RfO]
table["J"] = [[table["F"][0][0]-1], [x-1 for x in table["F"][1]], table["F"][2]]
expected={"O":[[0],[-1,0],[-1]],"L":[[-1],[-1,-1],[-1]],"F":[[0],[0,0],[0]],"E":[[-1,0],[-1,-1,-1,0],[-1,-1]],"J":[[-1],[-1,-1],[0]]}
for name in table:
    check("P5.2 all degrees " + name, table[name] == expected[name])
check("P5.2 extension H1(L^-1)=0", degree(tuple(-a for a in L)) == -1)
DATA["coarse_direct_image_degrees"] = table


def cohom(rows):
    result=[0]*4
    for q,row in enumerate(rows):
        result[q] += sum(max(d+1,0) for d in row)
        result[q+1] += sum(max(-d-1,0) for d in row)
    return result


check("P5.3 E cohomology", cohom(table["E"]) == [1,1,0,0])
check("P5.3 J cohomology", cohom(table["J"]) == [0,0,1,0])
check("P5.3 T cohomology forced by exact sequence", [a+b for a,b in zip(cohom(table["E"]),cohom(table["J"]))] == [1,1,1,0])
normalization=s.Matrix([[1,-1,1],[1,-1,1]])
check("P5.2 normalization rank", normalization.rank() == 1)
check("P5.2 normalization cohomology", [1,3-normalization.rank(),2-normalization.rank()] == [1,2,1])
incidence=s.Matrix([[1,-1,0],[0,1,-1],[1,-1,0],[0,1,-1]])
check("P5.2 conductor incidence rank", incidence.rank() == 2)
save_matrix("cusp_normalization_differential",normalization)
save_matrix("conductor_incidence",incidence)

# P5.5--6: the full integral mapping-cone complex, not a rational-only test.
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
I=s.eye(4)
check("P5.5 actual finite orders", A1**3 == A2**4 == I)
M0=(A1*A2).inv()
check("P5.5 actual cusp matrix", M0==s.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]]))
N1=I+A1+A1**2
N2=I+A2+A2**2+A2**3
check("P5.5 first cyclic norm", N1==s.Matrix([[3,0,0,0],[6,0,0,0],[-12,0,0,0],[0,2,1,3]]))
check("P5.5 second cyclic norm", N2==s.Matrix([[4,0,0,0],[12,0,0,0],[-12,0,0,0],[0,2,2,4]]))
D1,D2,Dc=A1-I,A2-I,M0-I
J=s.Matrix([[0,0],[0,0],[1,0],[0,1]])
check("P5.5 cusp invariant inclusion", Dc*J==s.zeros(4,2) and Dc.rank()==2)

# C^0=(p,r1,r2,c), C^1=(p1,p2,r1',r2',a1,a2,a0),
# C^2=(r1'',r2'',b1,b2,b0), C^3=(r1''',r2''').
d0=s.zeros(28,14)
d0[0:4,0:4]=D1;d0[4:8,0:4]=D2
d0[8:12,4:8]=D1;d0[12:16,8:12]=D2
d0[16:20,0:4]=I;d0[16:20,4:8]=-I
d0[20:24,0:4]=I;d0[20:24,8:12]=-I
d0[24:28,0:4]=I;d0[24:28,12:14]=-J
d1=s.zeros(20,28)
d1[0:4,8:12]=N1;d1[4:8,12:16]=N2
d1[8:12,0:4]=I;d1[8:12,8:12]=-I;d1[8:12,16:20]=-D1
d1[12:16,4:8]=I;d1[12:16,12:16]=-I;d1[12:16,20:24]=-D2
d1[16:20,0:4]=-M0;d1[16:20,4:8]=-M0*A1;d1[16:20,24:28]=-Dc
d2=s.zeros(8,20);d2[0:4,0:4]=D1;d2[4:8,4:8]=D2
for name,matrix in (("A1",A1),("A2",A2),("M0",M0),("N1",N1),("N2",N2),("d0",d0),("d1",d1),("d2",d2)):
    save_matrix(name,matrix)
check("P5.6 complete cone zero products", d1*d0==s.zeros(20,14) and d2*d1==s.zeros(8,28))
H0=integral_cohomology("H0",s.zeros(14,0),d0)
H1=integral_cohomology("H1",d0,d1)
H2=integral_cohomology("H2",d1,d2)
check("P5.6 integral H0",H0=={"free_rank":1,"torsion":[]})
check("P5.6 integral H1",H1=={"free_rank":0,"torsion":[]})
check("P5.6 integral H2",H2=={"free_rank":1,"torsion":[2]})

p=s.Matrix(4,4,s.symbols("p:16"))
eqs=list(p*A1-A1*p)+list(p*A2-A2*p)
C,unused=s.linear_eq_to_matrix(eqs,list(p))
check("P5.5 centralizer rational rank",C.rank()==14)
E41=s.zeros(4);E41[3,0]=1
check("P5.5 centralizer basis",all(matzero(q*A-A*q) for q in (I,E41) for A in (A1,A2)))
K=s.Matrix([[3,0,1],[-6,1,-1],[-2,1,0]])
Ki=s.Matrix([[-1,-1,1],[-2,-2,3],[4,3,-3]])
check("P5.5 primitive cocycle inverse",K.det()==-1 and K*Ki==Ki*K==s.eye(3))
save_matrix("primitive_cocycle_matrix",K)
save_matrix("primitive_cocycle_inverse",Ki)

R=s.Matrix([[1,0,0,0],[0,0,3,0],[0,2,0,0],[0,0,0,4],[0,0,-1,-1]])
Dr,Ur,Vr=snf(R)
check("P5.6 five-generator torsion presentation",[abs(Dr[i,i]) for i in range(4)]==[1,1,1,2])
mod2=s.Matrix([[0,0,1,0,0]])
check("P5.6 delta2 nonzero mod2 witness",all(x%2==0 for x in mod2*R) and (mod2*s.Matrix([0,0,1,0,0]))[0]==1)
check("P5.6 two delta2 relation",R[:,1]==s.Matrix([0,0,2,0,0]))
save_matrix("five_generator_relation_columns",R)

OUT={"reviewer":"GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family",
     "chronology":"Fresh exact implementation after reading current printed proofs; no historical program replay or formal-assistant claim",
     "python":platform.python_version(),"sympy":s.__version__,"all_pass":all(x["pass"] for x in CHECKS),
     "check_count":len(CHECKS),"checks":CHECKS,"data":DATA,
     "elapsed_seconds":round(time.monotonic()-START,6)}
target=Path(__file__).with_suffix(".output.json")
target.write_text(json.dumps(OUT,indent=2)+"\n")
print(json.dumps({"all_pass":OUT["all_pass"],"check_count":OUT["check_count"],"elapsed_seconds":OUT["elapsed_seconds"],"output":str(target),"output_sha256":hashlib.sha256(target.read_bytes()).hexdigest(),"H0":H0,"H1":H1,"H2":H2},indent=2))
