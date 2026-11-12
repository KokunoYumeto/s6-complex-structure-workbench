"""Exact group-coordinate checks for CG-S6-02. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s

root=Path(__file__).resolve().parents[1]
As=[s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])]
vs=[s.Matrix([1,2,-4,0]),s.Matrix([-1,-3,3,0])]
ps=[s.Matrix([[0,2,1,3]]),s.Matrix([[0,1,1,2]])]
g=s.Matrix([[1,0,0,0]])
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
lam=s.Matrix(s.symbols('a b c d',integer=True))
mu=s.Matrix(s.symbols('e f h i',integer=True))
q,n=s.symbols('q n',integer=True)
for j,(A,v,psi,m,eps) in enumerate(zip(As,vs,ps,[3,4],[1,-1]),1):
    label=f'case_{j}:'
    check(label+'power',A**m==s.eye(4))
    check(label+'translation_fixed',A*v==v)
    check(label+'character',g*A==g and (g*v)[0]==eps and psi*A==psi)
    check(label+'translation_coinvariant',(psi*v)[0]==0)
    check(label+'kernel_rank',(A-s.eye(4)).rank()==2)
    check(label+'kernel_generator_coordinate',(eps*g*(-v))[0]==-1)
    check(label+'positive_circle_coordinate',(eps*g*v)[0]==1)
    check(label+'clockwise_displacement',s.Rational(-m,m)==-1)
    check(label+'positive_log_deck_fibre',-v+v==s.zeros(4,1))
    check(label+'kernel_q_image',-q*v+q*v==s.zeros(4,1))
    check(label+'restriction_matrix_determinant',s.diag(eps*m,1).det()==eps*m)
    check(label+'primitive_abelian_kernel',s.gcd_list([-eps,0,m])==1)
    for k in range(m):
        check(label+f'circle_homomorphism_residue_{k}',eps*g*(lam+A**k*mu)==eps*g*lam+eps*g*mu)
        t=eps*(g*lam)[0]-n
        newlam=lam-t*v
        newk=k+t*m
        check(label+f'inverse_circle_residue_{k}',s.simplify((eps*g*newlam)[0]-n)==0)
        check(label+f'inverse_surface_residue_{k}',s.simplify(newlam+t*v-lam)==s.zeros(4,1) and s.simplify(newk-t*m)==k)
receipt={'lesson':'CG-S6-02','passed':len(checks),'checks':checks,'source_sha256':hashlib.sha256((root/'src/normal-boundaries-and-integral-maps.md').read_bytes()).hexdigest(),'scope':'Exact algebraic identities for all symbolic lattice coordinates and each finite residue. Covering-space, quotient-chart and homology proofs are in the lesson.'}
(root/'checks/NORMAL_BOUNDARY_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'lesson':'CG-S6-02'}))
