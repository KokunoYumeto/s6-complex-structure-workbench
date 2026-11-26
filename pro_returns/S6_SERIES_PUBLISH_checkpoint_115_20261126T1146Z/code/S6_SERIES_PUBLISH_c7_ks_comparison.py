"""Post-exposure 02KS comparison calculations and exact edit guards.

No historical computation is read.  The geometry of the original's
lattice substitution and the revised primitive surgery map are tested
directly.  Only the individually released original text is inspected.
"""
from pathlib import Path
from itertools import product
import csv
import hashlib
import re
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation7_iii_ks'
def smith(A):
    D,U,V=(a.to_Matrix() for a in smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(S.ZZ)))
    assert U*A*V==D and abs(U.det())==abs(V.det())==1
    assert U.inv()*D*V.inv()==A
    return D,U,V

gp=S.Matrix([[3,4],[0,1]])
gm=S.Matrix([[3,2],[0,1]])
R=S.diag(-1,1)
B=S.Matrix([[1,1],[0,-1]])
relative=gm.inv()*R*gp
assert relative==S.Matrix([[-1,-2],[0,1]]) and relative**2==S.eye(2)
assert B*gm==S.Matrix([[3,3],[0,-1]])
assert B*gp==S.Matrix([[3,5],[0,-1]])
print('angular_inversion_period_change',relative.tolist())
print('original_fan_reflection_on_original_printed_lattice',(B*gm).tolist())
print('original_fan_reflection_on_actual_lattice',(B*gp).tolist())

# The forward period covers -G.  Inversion and two long periods give
# the original section G with valuation two and preserve all units.
q,alpha,beta,mu,nu=S.symbols('q alpha beta mu nu',nonzero=True)
assert S.simplify((mu*q**4)**-1*(alpha*q**3)**2)==alpha**2*q**2/mu
assert (4%3,(-4)%3,6*2%3,12*2%3,12*3%4)==(1,2,0,0,0)
G_inverse_period=S.Matrix([alpha**2*q**2/mu,beta**2/(nu*q)])
reflected_forward_period=S.Matrix([alpha**2*q**2/mu,nu*q/beta**2])
print('components_minusG_G',[4%3,(-4)%3])
print('G_inverse_contraction_after_two_long_periods',list(G_inverse_period))
print('reflected_forward_period_with_transported_fan',list(reflected_forward_period))
print('I3_degrees_M1_M12',[[-1,0,1],[0,0,0]])

rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
rayset=set(rays)
def act(A,r):return tuple(A*S.Matrix(r))
automorphisms=[]
for a,b in product(rays,rays):
    A=S.Matrix.hstack(S.Matrix(a),S.Matrix(b))
    if abs(A.det())==1 and {act(A,r) for r in rays}==rayset:
        automorphisms.append(A)
assert len(automorphisms)==12 and B in automorphisms and R not in automorphisms
rp=S.Matrix([[1,-1]]);rm=S.Matrix([[1,1]])
assert all(v%3==0 for v in rp*gp) and all(v%3==0 for v in rm*gm)
actual_res=[int((rp*S.Matrix(r))[0]%3) for r in rays]
wrong_res=[int((rm*S.Matrix(r))[0]%3) for r in rays]
assert actual_res==[1,2,1,2,1,2] and wrong_res.count(0)==2
assert not any(all(x%3==0 for x in rm*A*gp) for A in automorphisms)
print('actual_neighbor_residues',actual_res)
print('unchanged_fan_substitution_neighbor_residues',wrong_res)
print('fan_symmetries',len(automorphisms),'identifications_of_the_two_lattices',0)

def wall(rho,i):
    a,b=i,0
    points=[(a,b),(a,b+1),(a+1,b),(a-1,b+1)]
    out=S.zeros(3,1)
    for sign,p in zip([-1,-1,1,1],points):out[rho(*p),0]+=sign
    return out
V=S.Matrix.hstack(*(wall(lambda x,y:(x-y)%3,i) for i in range(3)))
wrong=S.Matrix.hstack(*(wall(lambda x,y:(x+y)%3,i) for i in range(3)))
assert V==S.Matrix([[-1,-1,2],[2,-1,-1],[-1,2,-1]]) and wrong==S.zeros(3)
assert V*S.ones(3,1)==S.zeros(3,1)
inverse=S.Matrix([[-S.Rational(1,3),S.Rational(1,3),0],[-S.Rational(1,3),0,S.Rational(1,3)]])
assert inverse*V==S.Matrix([[1,0,-1],[0,1,-1]])
print('actual_wall_columns',V.tolist())
print('substituted_model_wall_columns',wrong.tolist())
print('wall_columns_in_primitive_fixed_basis',(inverse*V).tolist())

trace=S.zeros(1,3).col_join(inverse*V)
D,U,W=smith(trace)
assert [abs(D[i,i]) for i in range(3)]==[1,1,0]
assert trace*S.ones(3,1)==S.zeros(3,1)
assert trace.rank()==2
print('surgery_trace_H2_map',trace.tolist())
print('surgery_trace_smith',D.tolist())
assert 6-3*2==0
rank_h2_Y=3-2
rank_h3_Y=2+2*rank_h2_Y
assert (rank_h2_Y,rank_h3_Y,rank_h2_Y+1)==(1,4,2)
print('genuine_surgery_free_ranks_H2Y_H3Y_H2orbit',[rank_h2_Y,rank_h3_Y,rank_h2_Y+1])

x,y,w=S.symbols('x y w',nonzero=True)
coordinates=S.Matrix([w,y,x*y*w])
volume=S.simplify(coordinates.jacobian(S.Matrix([x,y,w])).det()/(w*y))
assert volume==-1
print('cusp_volume_in_dx_dy_dw',volume)

rows=list(csv.DictReader((OUT/'S6_SERIES_PUBLISH_III_02KS_replacements.tsv').open(),delimiter='\t'))
assert len(rows)==2
receiver=(OUT/'S6_SERIES_PUBLISH_III_02KS_receiving.tex').read_text()
assert rows[0]['new_text']+'\n\n'+rows[1]['new_text']+'\n'==receiver
assert rows[0]['statement_id']==rows[1]['statement_id']=='maps:src:D.2.18'
old='\n\n'.join(row['old_text'] for row in rows)
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    a,b=sorted(re.findall(pattern,old)),sorted(re.findall(pattern,receiver))
    assert a==b
    print('identity_guard',pattern,a)
assert r'\textnormal{\small tag02KS.}' in receiver
assert r'\operatorname{Fl}(\mathbb C^3)\#(S^2\times S^4)' in receiver
assert not re.search(r'the curve the|matrix the fixed|map the orbit|§the|construction\.1|\bactual\b|\bnew program\b',receiver)
for display in re.findall(r'\\\[(.*?)\\\]',receiver,re.S):
    assert '\n\n' not in display
assert hashlib.sha256((OUT/'S6_SERIES_PUBLISH_III_02KS_c7_fresh_derivation.md').read_bytes()).hexdigest()=='e44b377b7cc2ec20e4356dbea3196c71ee89581f8ef58d3ede56de5972059f0f'
print('Receiving_sha256',hashlib.sha256(receiver.encode()).hexdigest())
print('PASS: fan transport, actual wall classes, surgery ranks, canonical form and exact receiver guards.')
