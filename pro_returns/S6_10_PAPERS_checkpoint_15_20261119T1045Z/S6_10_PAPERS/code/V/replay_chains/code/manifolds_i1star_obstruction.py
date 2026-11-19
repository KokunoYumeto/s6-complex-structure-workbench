"""Exact integral I1* cap certificates and complete natural sphere profile table.
No multiplicity cutoff: the geometric proof restricts a sphere cap to m=2
or a component-swapping m=4; normalization and index calculations are exact.
"""
from pathlib import Path
import json,csv,sympy as s
from math import gcd
from collections import Counter
from manifolds_rankone_families import decomp,ikernel,wedge,biv,bezout
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']
initial=json.loads((ROOT/'records/manifolds_sphere_initial.json').read_text())['candidates']
ini={(r['entry'],r['profile'],r['a'],r['b'],r['zero_index']):r for r in initial}

def solve(M,v):
    D,U,V,r=decomp(M);z=U*v;y=s.zeros(M.cols,1)
    for j in range(r):
        assert z[j]%D[j,j]==0
        y[j]=z[j]/D[j,j]
    assert all(z[j]==0 for j in range(r,M.rows))
    out=V*y;assert M*out==v;return out

def group(M):
    D,U,V,r=decomp(M)
    return M.rows-r,[int(abs(D[j,j])) for j in range(r) if abs(D[j,j])>1]

Ac=s.Matrix([[-1,0,-1,0],[0,-1,0,0],[0,-1,1,0],[0,0,0,1]])
assert Ac**2-s.eye(4)==s.Matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
cert=[]
for row in rows:
    slots=[j for j,v in enumerate(row['local']) if v['type']=='I1*']
    if not slots:continue
    j=slots[0];A=s.Matrix(row['local'][j]['matrix']);N=A*A-s.eye(4)
    D,U,V,r=decomp(N);assert r==1 and abs(D[0,0])==1 and N*N==s.zeros(4)
    alpha=U.inv()[:,0];assert A*alpha==-alpha
    Ab=(U*A*U.inv())[1:,1:];gamma=(s.eye(4)[3,:]*U.inv())[:,1:]
    fixbar=ikernel(Ab-s.eye(3));gi=gcd(*map(int,list(gamma*fixbar)))
    rec={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']}
    rec.update(relative_gamma_index=gi,collapsed_matrix=Ab.tolist(),vanishing=alpha.tolist())
    old=ini[(row['entry'],row['profile'],row['a'],row['b'],row['zero_index'])]['local'][j]
    assert not(old['P_component']==0 and old['component_orbits']==1)
    if gi==1:
        assert (row['a'],row['b']) in [(1,4),(1,12),(3,4)]
        lam=(s.eye(4)[:,2]+alpha)/2;assert all(x.q==1 for x in lam)
        beta=solve((A+s.eye(4)).col_join(s.eye(4)[3,:]),(-lam).col_join(s.zeros(1,1)))
        fix=ikernel(A-s.eye(4));ell=fix*bezout(list(fix[3,:]))[0]
        B=s.Matrix.hstack(alpha,beta,lam,ell)
        assert abs(B.det())==1 and B.inv()*A*B==Ac
        assert B.inv()*s.eye(4)[:,2]==s.Matrix([-1,0,2,0])
        assert (wedge(A)-s.eye(6)).rank()==4 and group(wedge(A)-s.eye(6))==(2,[])
        for local in row['local']:
            assert group(s.Matrix(local['matrix'])-s.eye(4))[1]==[]
        omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]])
        assert (omega*biv(beta,lam))[0]==-row['a']
        assert (omega*biv(beta,ell))[0]==s.Rational(row['b'],4)
        rec.update(normal_form_basis=B.tolist(),normal_form=Ac.tolist(),boundary_H2=[4,[]])
    else:
        assert gi==2 and (row['a'],row['b']) in [(4,1),(4,3),(12,1)]
    cert.append(rec)
assert len(cert)==16 and Counter(x['relative_gamma_index'] for x in cert)=={1:8,2:8}

# m=2: normalization generators sigma,f,D. Odd section parity reduced to e=1.
rel2=s.Matrix([2,-1,-2]);x2=s.Matrix([-1,0,1]);y2=s.Matrix([0,0,-1])
assert group(rel2)==(2,[])
assert group(s.Matrix.hstack(rel2,x2,y2))==(0,[])
assert s.Matrix([0,1,0])+2*x2==-rel2
assert s.Matrix([2,-1,0])+2*y2==rel2
# m=4 swap: f,sigma,D0,D1 and equal normalization sections.
rel4=s.Matrix([[0,0],[1,1],[-2,0],[0,-2]])
assert group(rel4)==(2,[2])
indices=[]
for eps in range(2):
 for eta in range(2):
    tau=s.Matrix([0,0,-1,1])
    x4=s.Matrix([-1,0,0,0])+eps*tau
    y4=s.Matrix([0,0,-2,0])+eta*tau
    Q=s.Matrix.hstack(rel4,x4,y4)
    assert abs(Q.det())==4
    indices.append(dict(epsilon=eps,eta=eta,group=group(Q)))

# Exact symbolic determinant: arbitrary full normal projection matrices and
# arbitrary longitudinal fibre coefficients disappear from the result.
b,e,n1,n2,m1,m2,h1,h2=s.symbols('b e n1 n2 m1 m2 h1 h2',nonzero=True)
p,q,r,t,u,v,w,z=s.symbols('p q r t u v w z')
P1=s.Matrix([[p,q],[r,t]]);P2=s.Matrix([[u,v],[w,z]])
# Exterior generators s,d1,l1,l2; diagonal relation d2=-d1-b*e*s.
K1=s.Matrix.vstack(-s.Matrix([[b*n1/m1,h1]])*P1,P1,s.zeros(1,2))
K2=s.Matrix.vstack(s.Matrix([[b*e-b*n2/m2,-h2]])*P2,-P2[0,:],s.zeros(1,2),P2[1,:])
assert s.factor(s.Matrix.hstack(K1,K2).det()-b*(e-n1/m1-n2/m2)*P1.det()*P2.det())==0

# All21 natural profile outcomes: finite marked cap patterns, not a count of
# complex structures. The non-star list was proved in D.2.26.
pat=json.loads((ROOT/'records/manifolds_nonstar_sphere_patterns.json').read_text())['sphere_patterns']
counts=Counter((x['entry'],x['profile']) for x in pat)
profiles={}
for r0 in rows:profiles[(r0['entry'],r0['profile'])]=[v['type'] for v in r0['local']]
table=[]
for key,fibres in profiles.items():
    star=any(x.startswith('I') and x.endswith('*') and x[1:-1].isdigit() for x in fibres)
    additive=any(not(x.startswith('I') and x[1:].isdigit()) for x in fibres)
    count=counts[key]
    assert bool(count)==(not star)
    table.append(dict(entry=key[0],profile=key[1],fibres=fibres,sphere_patterns=count,
        unbounded_sphere_multiplicities=bool(count and additive),
        outcome='none' if star else ('unbounded' if additive else 'all orders one')))
assert len(table)==21 and sum(x['sphere_patterns'] for x in table)==59
assert Counter(x['outcome'] for x in table)=={'unbounded':12,'all orders one':4,'none':5}
print('I1* marked initial rows:',len(cert),'relative gamma indices:',dict(Counter(x['relative_gamma_index'] for x in cert)))
print('All8 good rows have the exact integral canonical block; boundary H2 is free rank4.')
print('m2 cap H2: Z^2; full normal projection index1.')
print('m4 swapped cap H2: Z^2 + Z2; full normal projection index4 in all4 torsion-marking cases.')
print('Symbolic full normal determinant identity: PASS.')
print('All21 profile outcomes:',dict(Counter(x['outcome'] for x in table)))
print('Total marked sphere cap patterns:',sum(x['sphere_patterns'] for x in table))
(ROOT/'records/manifolds_i1star_obstruction.json').write_text(json.dumps(dict(scope=__doc__,certificates=cert,m4_indices=indices,profiles=table),indent=2,default=int)+'\n')
with (ROOT/'records/manifolds_complete_natural_sphere_profiles.csv').open('w',newline='') as f:
    W=csv.DictWriter(f,fieldnames=list(table[0]));W.writeheader();W.writerows(table)
