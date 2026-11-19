"""Exact integral checks for the explicit rank-two specialization proof.

This checks the displayed lattices, not the analytic compactness/flow argument.
Those steps are read and rederived separately in the current proof record.
"""
from pathlib import Path
from itertools import combinations
from datetime import datetime, timezone
import hashlib, json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'analysis/IV/rank_two_specialization_check.json'
PROOF = ROOT / 'papers/IV/rank_two_specialization.tex'
started = datetime.now(timezone.utc).isoformat()

rays = [s.Matrix(v) for v in [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]]
for i in range(6):
    assert s.Matrix.hstack(rays[i], rays[(i+1)%6]).det() == 1
    assert rays[(i-1)%6]+rays[(i+1)%6] == rays[i]
degree = s.zeros(6,4)
for j in range(4):
    a = [s.Integer(0)]*6
    a[j+2] = 1
    for i in range(6):
        degree[i,j] = a[(i-1)%6]+a[(i+1)%6]-a[i]
C2 = s.Matrix.vstack(*(degree[i,:]-degree[i+3,:] for i in range(3)))
assert C2 == s.Matrix([[-1,1,-1,1],[1,-1,1,-1],[-1,1,-1,1]])
C0 = s.Matrix([[1,-1,1],[-1,1,-1]])
assert C0.rank()==C2.rank()==1
for c in [C0,C2]:
    sn = smith_normal_form(c,domain=ZZ)
    assert [abs(sn[i,i]) for i in range(min(sn.shape)) if sn[i,i]] == [1]

# Ordered one-form basis a1,b1,a2,b2.  Matrices act on column vectors.
T = s.Matrix([[1,1,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]])
def exterior_matrix(mat,k):
    basis=list(combinations(range(4),k))
    return s.Matrix([[mat.extract(I,J).det() for J in basis] for I in basis])
def wedge(indices,k):
    basis=list(combinations(range(4),k))
    v=s.zeros(len(basis),1)
    if len(set(indices))<len(indices):
        return v
    sign=(-1)**sum(indices[i]>indices[j] for i in range(k) for j in range(i+1,k))
    v[basis.index(tuple(sorted(indices))),0]=sign
    return v
generators = {
  0:[s.ones(1,1)],
  1:[wedge([0],1),wedge([2],1)],
  2:[wedge([0,2],2),wedge([0,1],2),wedge([2,3],2),wedge([0,3],2)+wedge([2,1],2)],
  3:[wedge([0,2,1],3),wedge([0,2,3],3)],
  4:[wedge([0,1,2,3],4)],
}
exterior_checks=[]
for k in range(5):
    tk=exterior_matrix(T,k)
    g=s.Matrix.hstack(*generators[k])
    assert (tk-s.eye(tk.rows))*g == s.zeros(tk.rows,g.cols)
    assert g.rank()==tk.rows-(tk-s.eye(tk.rows)).rank()
    sn=smith_normal_form(g,domain=ZZ)
    diagonal=[abs(sn[i,i]) for i in range(min(sn.shape)) if sn[i,i]]
    assert diagonal==[1]*g.cols
    # Kernel of an integral map is saturated.  The displayed primitive lattice
    # has its full rational span, hence is the whole integral kernel.
    exterior_checks.append({'degree':k,'rank':g.cols,'primitive_smith':list(map(int,diagonal)),
                            'monodromy':list(map(list,tk.tolist()))})

v1,v2,n1,n2,m1,m2=s.symbols('v1 v2 n1 n2 m1 m2',integer=True)
phi=lambda x,y:x*y
assert s.expand(phi(v1+n1,v2+n2)-phi(v1,v2)-v1*n2-v2*n1-n1*n2)==0
assert s.expand(m1*n2+m2*n1+phi(m1,m2)+phi(n1,n2)-phi(m1+n1,m2+n2))==0
x,y=s.symbols('x y')
lower=v2*x+v1*y-v1*v2
upper=(v2+1)*x+(v1+1)*y-v1*v2-v1-v2-1
for P in [(v1,v2),(v1+1,v2),(v1,v2+1)]:
    assert s.expand(lower.subs({x:P[0],y:P[1]})-phi(*P))==0
for P in [(v1+1,v2),(v1,v2+1),(v1+1,v2+1)]:
    assert s.expand(upper.subs({x:P[0],y:P[1]})-phi(*P))==0
for affine in [lower,upper]:
    translated=affine.subs({v1:v1+n1,v2:v2+n2,x:x+n1,y:y+n2}, simultaneous=True)
    assert s.expand(translated-affine-x*n2-y*n1-n1*n2)==0

now=datetime.now(timezone.utc).isoformat()
report={'started_utc':started,'completed_utc':now,'verdict':'all exact algebraic assertions passed',
        'proof_path':str(PROOF.relative_to(ROOT)),'proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'C0':C0.tolist(),'C2':C2.tolist(),'exterior_checks':exterior_checks,
        'cross_line_checks':'Integral Cartier slopes on both triangles; full period and group cocycle identities for arbitrary integer vectors.',
        'limitations':'Analytic properness, the q-preserving stratified flow, and the actual toric comparison map are proof-reading checks, not conclusions of this program.'}
OUT.write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps({'completed_utc':now,'verdict':report['verdict'],'ranks':[g['rank'] for g in exterior_checks],'output':str(OUT)}))
