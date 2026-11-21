from fractions import Fraction as F
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'agents/i_provenance/S6_SERIES_PUBLISH_I_invB10_primary_inputs.json').read_text())
T=[data['T0'],data['T1']]
A=[[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]],[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]]
P=[[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]]
Q=[[2,-1,0,-2],[2,-1,0,-1],[0,2,1,3],[1,0,0,0]]
def rref(rows):
    a=[[F(x) for x in row] for row in rows]
    piv=[]; r=0
    for c in range(len(a[0])):
        hit=next((i for i in range(r,len(a)) if a[i][c]),None)
        if hit is None: continue
        a[r],a[hit]=a[hit],a[r]
        d=a[r][c]; a[r]=[x/d for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                d=a[i][c]; a[i]=[x-d*y for x,y in zip(a[i],a[r])]
        piv.append(c); r+=1
        if r==len(a):break
    return a,piv
def constraints(reverse=False):
    rows=[]
    for t,a in zip(T,A):
        for i in range(4):
            for j in range(4):
                row=[0]*16
                if not reverse:
                    for k in range(4):
                        row[4*k+j]+=t[i][k]
                        row[4*i+k]-=a[k][j]
                else:
                    for k in range(4):
                        for l in range(4):row[4*k+l]+=t[i][k]*a[l][j]
                    row[4*i+j]-=1
                rows.append(row)
    return rows
def clean(x):
    if isinstance(x,list):return [clean(v) for v in x]
    if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
    return x
for reverse,candidate in [(False,P),(True,Q)]:
    rr,piv=rref(constraints(reverse)); free=[c for c in range(16) if c not in piv]
    vals=[F(x) for row in candidate for x in row]
    recon=[F(0)]*16
    for f in free:recon[f]=vals[f]
    for i,p in enumerate(piv):recon[p]=-sum(rr[i][f]*vals[f] for f in free)
    print(json.dumps({'reverse':reverse,'rank':len(piv),'free_indices':free,'free_values':clean([vals[i] for i in free]),'rref':clean(rr[:len(piv)]),'reconstructed':clean([recon[4*i:4*i+4] for i in range(4)]),'candidate_equal':vals==recon}))
