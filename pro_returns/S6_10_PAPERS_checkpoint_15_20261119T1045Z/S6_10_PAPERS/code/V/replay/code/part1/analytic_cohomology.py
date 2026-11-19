"""Exact orbifold degrees and cusp cohomology maps for the fourfold."""
from pathlib import Path
from itertools import combinations
import sympy as s,json
root=Path(__file__).parent
def degree(j):return (4*j)//5+(-3*j)//4
G=[0,-1,-2]
def cohom(weights):
    h=[0]*5;terms=[]
    for q in range(4):
        for I in combinations(range(3),q):
            for w in weights:
                k=w+sum(G[i] for i in I);d=degree(k)
                h[q]+=max(d+1,0);h[q+1]+=max(-d-1,0)
                terms.append({'q':q,'weight':w,'G_indices':I,'exponent':k,'degree':d})
    return h,terms
data={'degrees':{str(i):degree(i) for i in range(-20,21)},'bundles':{}}
for name,weights in [('O',[0]),('E',[0,-1,-2]),('F',[0,1,2]),('G',[0,-1,-2]),('K',[-6]),('base_tangent',[9]),('base_cotangent',[-9]),('base_log_cotangent',[11]),('base_log_tangent',[-11]),('wedge2F',[1,2,3]),('log_base_times_F',[11,12,13])]:
    h,terms=cohom(weights);data['bundles'][name]={'weights':weights,'h':h,'terms':terms};print(name,weights,h)
N=s.Matrix([[s.sympify(x) for x in row] for row in json.loads((root/'cusp_residue_weight_bases.json').read_text())['F_to_G']])
z=s.Symbol('z');pairs=list(combinations(range(3),2))
def wedge_one_pair(v,pair):
    out=s.zeros(3,1)
    for j in range(3):
        i=pair[0]
        if j==i:continue
        out[pairs.index(tuple(sorted((j,i)))),0]+=v[j]*(1 if j<i else -1)
    return out
# Connecting map F tensor G -> wedge2 G, on the three weight-zero sections.
D1=s.zeros(3)
for i in range(3):
    for j in range(3):
        if j==i:continue
        D1[pairs.index(tuple(sorted((j,i)))),i]+=N[j,i]*(1 if j<i else -1)
# Connecting map wedge2 F tensor wedge2 G -> F tensor wedge3 G.
D2=s.zeros(3)
for col,(i,j) in enumerate(pairs):
    k=3-i-j
    # N f_i wedge g_i wedge g_j gives the coefficient of f_j;
    # minus N f_j wedge g_i wedge g_j gives that of f_i.
    sign=(-1)**sum(a>b for a,b in combinations((k,i,j),2))
    D2[j,col]+=sign*N[k,i];D2[i,col]-=sign*N[k,j]
data['N']=[[str(v) for v in row] for row in N.tolist()]
for name,M in [('D1_FG',D1),('D2_wedge2F_wedge2G',D2)]:
    determinant=s.factor(M.det());data[name]={'matrix':[[str(v) for v in row] for row in M.tolist()],'determinant':str(determinant),'zeros':[str(v) for v in s.solve(determinant,z)]};print(name,M,'det',determinant,'zeros',s.solve(determinant,z))
assert s.factor(D1.det()+D2.det())==0
assert s.solve(D1.det(),z)==[-s.Rational(3125,384)]
hodges=[[1,1,0,0,0],[0,2,1,0,0],[0,1,6,1,0],[0,0,1,2,0],[0,0,0,1,1]]
for p in range(5):
    for q in range(5):assert hodges[p][q]==hodges[4-p][4-q]
assert [sum((-1)**q*hodges[p][q] for q in range(5)) for p in range(5)]==[0,-1,4,-1,0]
assert sum((-1)**(p+q)*hodges[p][q] for p in range(5) for q in range(5))==6
data['hodge_table_rows_p_columns_q']=hodges
y=s.Symbol('y')
coefficient_c2_squared=(1+y)**4/s.Integer(240)
coefficient_c4=(-1+10*y-y*y)**2/s.Integer(144)-2*coefficient_c2_squared
chi_y=s.factor(2*coefficient_c2_squared+6*coefficient_c4)
assert s.expand(chi_y)==-y+4*y*y-y**3
data['chi_y_genus']={'c2_squared_coefficient':str(coefficient_c2_squared),'c4_coefficient':str(coefficient_c4),'evaluated':str(chi_y)}
data['proof_dependencies']='Global bundle and residue proofs in notes/part1_analytic.tex; rank-jump exclusion certified separately in certified_lift_bound.py.'
(root/'analytic_cohomology.json').write_text(json.dumps(data,indent=2)+'\n')
print('hodge_table',hodges)
