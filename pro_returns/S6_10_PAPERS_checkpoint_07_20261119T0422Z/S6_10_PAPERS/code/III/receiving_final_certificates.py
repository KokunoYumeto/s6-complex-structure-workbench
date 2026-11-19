#!/usr/bin/env python3
"""Exact finite certificates used after the current full Paper III proof reading.

This program does not confer proof credit. It independently reconstructs the
dessin peripheral words from its half-edge graph, compares the archived marked
data, and checks the finite cohomology lattices used in the displayed argument.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

OUT = Path(__file__).resolve().parents[2]
I = s.eye(2)
S = s.Matrix([[0,-1],[1,0]])
T = s.Matrix([[1,1],[0,1]])
R = S*T
H = S*R.inv()*S.inv()
V = R.inv()*T*R
B = V**3
C = (R*S*R.inv())*T**2*(R*S*R.inv()).inv()

def cycles(p):
    unseen=set(range(len(p))); result=[]
    while unseen:
        a=min(unseen); cycle=[]; q=a
        while q in unseen:
            unseen.remove(q);cycle.append(q);q=p[q]
        assert q==a
        result.append(cycle)
    return result

def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out

def inverse_word(w):
    return ''.join({'s':'s','r':'R','R':'r'}[x] for x in w[::-1])

def path_word(sp,rp,non_tree,word):
    # All black half-edges are in the tree. The punctured fixed black
    # vertex contributes e=3, while listed white half-edges contribute a,b.
    ri=[rp.index(i) for i in range(len(rp))]
    q=0; w=[]
    for x in word:
        if x=='s':
            if q in non_tree:w.append(non_tree[q])
            q=sp[q]
            if q in non_tree:w.append(-non_tree[q])
        else:
            if rp[q]==q:w.append(3 if x=='r' else -3)
            q=(rp if x=='r' else ri)[q]
    return q,reduce_word(w)

def wedge(u,v):return (u[0]*v[1]-u[1]*v[0])

archive=json.loads((OUT/'code/III/explorer/collision_profiles.json').read_text())
data={50:([1,0,3,2],[2,1,3,0],{3:1},[('',3),('R',1)],[[3,-1],[1],[-3]],
          [H,T**3,-V],V,[[-5,2],[-8,4],[0,1]],[[1,-1],[-s.Rational(4,3),0],[s.Rational(1,4),-s.Rational(3,4)]],s.Rational(1,12)),
      56:([1,0,4,5,2,3,9,8,7,6],[2,1,3,0,6,8,7,4,9,5],{8:1,9:2},[('',5),('R',3),('rsR',2)],[[3,-2],[1],[-1,2],[-3]],
          [C,H,T**5,B],B,[[-2,1],[0,0],[4,-3],[1,-1]],[[-s.Rational(1,2),0],[0,0],[-s.Rational(1,5),s.Rational(1,5)],[s.Rational(1,3),0]],s.Rational(1,30))}
results={}
for number,(sp,rp,non_tree,peripherals,expected,base_tuple,conjugator,qs,zs,height) in data.items():
    n=len(sp)
    assert all(sp[sp[i]]==i and rp[rp[rp[i]]]==i for i in range(n))
    seen={0};todo=[0]
    while todo:
        q=todo.pop()
        for p in (sp,rp):
            if p[q] not in seen:seen.add(p[q]);todo.append(p[q])
    assert len(seen)==n
    cr=cycles(rp);cs=cycles(sp);ct=cycles([rp[sp[i]] for i in range(n)])
    assert sum(len(c)-1 for c in cr+cs+ct)==2*n-2
    words=[]
    for stem,width in peripherals:
        end,w=path_word(sp,rp,non_tree,stem+'sr'*width+inverse_word(stem))
        assert end==0; words.append(w)
    end,w=path_word(sp,rp,non_tree,'sRs');assert end==0;words.append(w)
    assert words==expected,(number,words,expected)
    assert reduce_word(sum(words,[]))==[]
    matrices=[conjugator*A*conjugator.inv() for A in base_tuple]
    archived=next(p for p in archive['profiles'] if p['os_entry']==number and p['profile']=='II')
    assert [A.tolist() for A in matrices]==archived['matrices']
    assert qs in archived['cocycles']
    Q=list(map(s.Matrix,qs));Z=list(map(s.Matrix,zs));prefix=I;prefixes=[];Y=[];K=[]
    for A,q,z in zip(matrices,Q,Z):
        assert A.det()==1 and (A-I)*z==q
        prefixes.append(prefix);Y.append(prefix*q);K.append(prefix*A.inv()*prefix.inv());prefix=prefix*A
    assert prefix==I and sum(Y,s.zeros(2,1))==s.zeros(2,1)
    p=I
    for k in K:p=p*k
    assert p==I
    for i,(A,P,q,z,k) in enumerate(zip(matrices,prefixes,Q,Z,K)):
        assert (I-k)*P*(z+q)==P*q
        assert (I-k)*P*A==P*(A-I)
    diagonal=sum(wedge(z,q) for z,q in zip(Z,Q))
    cross=sum(wedge(Y[i],Y[j]) for i in range(len(Y)) for j in range(i+1,len(Y)))
    assert -(diagonal-cross)==height
    if number==50:
        v=(matrices[0]-I).inv()*Q[0]; assert list(v)==[1,-1]
        reduced=[q-(A-I)*v for A,q in zip(matrices,Q)]
        assert [list(q) for q in reduced]==[[0,0],[-2,1],[2,-1]]
        assert (matrices[0]-I).det()==1
    else:
        assert (matrices[1]-I).det()==1
        local=[s.Matrix(v) for v in [[-2,1],[4,-3],[1,-1]]]
        cols=s.Matrix.hstack(*[prefixes[i]*v for i,v in zip([0,2,3],local)])
        assert cols==s.Matrix([[-2,1,1],[1,0,-1]])
        assert cols[:,0:2].det()==-1 and cols*s.ones(3,1)==s.zeros(2,1)
    results[str(number)]={'index':n,'cycles_s':cs,'cycles_r':cr,'cusp_cycles':ct,'free_peripheral_words':words,
                         'archive_marking_exact':True,'diagonal':str(diagonal),'cross':str(cross),'height':str(height)}

t=s.symbols('t');c4=t**2*(t+27)*(t+3);c6=t**3*(t+27)*(t*t+18*t-27);delta=t**7*(t+27)**2
assert s.expand(c4**3-c6**2-1728*delta)==0

# The finite surfaces are mapping tori of these exact integral matrices.
# All exterior differentials have primitive image, hence their homology
# and the Wang extension groups are free, including H^3.
finite=[]
for B0 in [s.Matrix([[0,1,0],[-1,-1,0],[1,0,1]]),s.Matrix([[0,-1,0],[1,0,0],[0,1,1]])]:
    forms=[]
    for k in range(4):
        inds=list(combinations(range(3),k))
        E=s.Matrix([[B0.extract(a,b).det() if k else 1 for b in inds] for a in inds])
        D=smith_normal_form(E-s.eye(len(inds)),domain=s.ZZ)
        diag=[abs(D[i,i]) for i in range(len(inds)) if D[i,i]]
        assert all(x==1 for x in diag)
        forms.append([int(x) for x in diag])
    finite.append(forms)
alpha=s.Matrix([[1,0,0,0],[0,-4,-2,1],[-2,0,0,0],[0,3,3,-1]])
assert alpha.rank()==3 and alpha*s.Matrix([0,1,1,6])==s.zeros(4,1)
g=s.gcd_list([alpha.extract(a,b).det() for a in combinations(range(4),3) for b in combinations(range(4),3)])
assert abs(g)==1
results['finite_degree_three']={'exterior_smith_nonzero':finite,'alpha3_rank':3,'maximal_minor_gcd':1,'kernel':[0,1,1,6]}
dest=OUT/'analysis/III_final_exact_certificates.json'
dest.write_text(json.dumps({'status':'PASS','scope':'Finite exact checks only; mathematical review events are recorded separately.','results':results},indent=2)+'\n')
print(json.dumps({'status':'PASS','file':str(dest),'collision_profiles':[50,56],'finite_degree_three':'PASS'}))
