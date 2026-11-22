#!/usr/bin/env python3
"""Exact marking/boundary audit of C's new R13 construction research.

Supporting construction exposure is disclosed in the accompanying audit.
The original R13 target proof remains unopened.  No analytic existence or
whole-target check event is certified by this finite symbolic calculation.
"""
from itertools import combinations
import json
import sympy as sp

Q=sp.Rational
A=sp.Matrix([[1,0,0,0],[0,1,0,0],[-1,0,-1,-1],[0,0,0,-1]])
direct=sp.Matrix([[1,0,0,0],[0,1,0,0],[-1,0,-1,1],[0,0,0,-1]])
assert direct==A.inv()
assert A*A==sp.eye(4)+sp.Matrix([[0,0,0,0],[0,0,0,0],[0,0,0,2],[0,0,0,0]])

ell,tau,aa,bb,gg=sp.symbols('ell tau alpha beta gamma')
R=sp.diag(1,-1)
period=sp.Matrix([[Q(1,2),tau,0,aa],[Q(1,2),bb,1,2*ell+gg]])
half=sp.Matrix([[Q(1,2),tau,0,-aa],[Q(1,2),-bb,1,2*ell+1+gg]])
assert half==R*period*A
v=sp.Matrix([-ell/2,-ell/2+Q(1,8)])
delta=sp.Matrix([Q(1,4),ell])
assert sp.simplify(v.subs(ell,ell+Q(1,2))-R*v+delta)==sp.zeros(2,1)
assert v.subs(ell,ell+1)-v==sp.Matrix([-Q(1,2),-Q(1,2)])
assert (-v).subs(ell,ell+Q(1,2))-R*(-v)==delta

P=sp.Matrix([[Q(1,2),Q(1,2),Q(1,2),1],[Q(1,2),0,0,0],
             [0,Q(1,2),0,0],[0,0,Q(1,2),0]])
assert P.det()==-Q(1,8)
tr,ti,lr,li=sp.symbols('tau_real tau_imag ell_real ell_imag',real=True)
lim=sp.Matrix([[Q(1,2),tr+sp.I*ti,0,0],
               [Q(1,2),0,1,2*(lr+sp.I*li)]])
local_det=sp.factor(lim.col_join(sp.conjugate(lim)).det())
assert local_det==4*ti*li

As=[sp.Matrix(x) for x in [
 [[1,0,0,0],[0,-1,2,0],[0,0,-1,0],[0,1,0,1]],
 [[-1,0,0,0],[0,1,0,0],[2,0,-1,0],[0,0,1,1]],
 [[-1,0,0,0],[0,-1,-2,0],[-2,0,1,0],[2,1,1,1]]]]
Cs=[sp.Matrix(x) for x in [
 [[0,-1,0,0],[-1,0,-2,-1],[0,0,0,1],[0,0,1,0]],
 [[0,0,0,1],[0,-1,0,0],[-1,0,-2,-1],[0,0,1,0]],
 [[0,0,0,1],[1,-1,2,-2],[0,1,0,1],[0,0,-1,0]]]]
assert As[0]*As[1]*As[2]==sp.eye(4)
for B,C in zip(As,Cs):
    assert B*C==C*A and B.det()==C.det()==1
alpha=sp.Matrix([1,1,1,2])
pullbacks=[C.T*alpha for C in Cs]
expected=[sp.Matrix([-1,-1,0,0]),sp.Matrix([-1,-1,0,0]),sp.Matrix([1,0,0,0])]
assert pullbacks==expected
for B in As:assert B.inv().T*alpha==alpha
assert sp.gcd_list(list(alpha))==1

# Actual rational matching equations after the zero-section splitting.
x1,x2,c,u1,v1,u2,v2,u3,v3=sp.symbols('x1 x2 c u1 v1 u2 v2 u3 v3')
unknowns=[x1,x2,c,u1,v1,u2,v2,u3,v3]
equations=[]
for (u,w),local in zip([(u1,v1),(u2,v2),(u3,v3)],pullbacks):
    equations.extend([u-c*local[0],w-c*local[1]])
equations.extend([x1-u1/2,x2-u2/2,-x1-x2-u3/2])
matching=sp.Matrix([[sp.diff(e,z) for z in unknowns] for e in equations])
assert matching.rank()==9
obstruction=sum(p[0]/2 for p in pullbacks)
assert obstruction==-Q(1,2)
assert 2*obstruction==-1

def exterior(B,q):
    ids=list(combinations(range(4),q))
    return sp.Matrix([[B.extract(I,J).det() for J in ids] for I in ids])
def invdim(Bs):
    size=Bs[0].rows
    return size-sp.Matrix.vstack(*[B-sp.eye(size) for B in Bs]).rank()
rows=[]
for q in range(5):
    Bs=[exterior(B.inv().T,q) for B in As]
    rank=Bs[0].rows
    local=[rank-(B-sp.eye(rank)).rank() for B in Bs]
    glob=invdim(Bs)
    dual=invdim([B.inv().T for B in Bs])
    chi=-rank+sum(local)
    h1=glob+dual-chi
    assert h1==0
    rows.append({'q':q,'rank':rank,'local_invariants':local,
                 'common_invariants':glob,'dual_common_invariants':dual,
                 'chi_jstar':chi,'h1_jstar':h1})
assert rows[1]['common_invariants']==1
assert rows[2]['common_invariants']==0

print(json.dumps({
 'scope':'Exact finite marking and boundary algebra only; original target unopened; zero events.',
 'parallel_monodromy':A.tolist(),'direct_endpoint_deck_matrix':direct.tolist(),
 'period_half_turn_identity':True,'Phi_descent_identity':True,
 'full_root_loop_translation':[-Q(1,2),-Q(1,2)],
 'quotient_square_order':'The coefficient vector (1/2,0,1/2,0) in the real-independent basis (p,b,c,d) has exact order two modulo Z^4.',
 'det_P':P.det(),'local_period_determinant':str(local_det),
 'orientation_conclusion':'Positive e-marking determinant and det(D P C_i)<0 force Im(tau(0))<0 when Im(ell)>0; use the same signed norm denominator and an absolute lower bound.',
 'alpha_pullbacks':[list(p) for p in pullbacks],
 'local_base_loop_values':[p[0]/2 for p in pullbacks],
 'rational_obstruction':obstruction,'integral_generator_obstruction':2*obstruction,
 'matching_matrix':matching.tolist(),'matching_rank':matching.rank(),
 'matching_determinant':matching.det(),
 'exterior_cohomology_dimensions':rows,
 'not_automated':['Holomorphic period-bundle construction and transversality',
                  'Properness and Hausdorff property of the chain quotient',
                  'Integral tube/fibre and zero-section boundary identifications',
                  'The local invariant-cycle maps and global compactification'],
 'events_added':0},indent=2,default=str)+'\n')
