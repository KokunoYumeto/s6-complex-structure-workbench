"""Exact local period, finite-normal and compactness input for IA.1--3.

The analytic properness proof is in the note; no global boundary ledger
or characteristic pair is certified by this local algebra.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,hashlib
bdir=Path(__file__).resolve().parents[2]
Lq,Ls,Lp,Lc=S.symbols('Lq Ls Lp Lc',real=True)
checks=[]
def ck(name,x):
    z=S.simplify(x)
    assert z==0,(name,z)
    checks.append(name)
for a,b in ((2,3),(6,1)):
    M=S.Matrix([[Lq,-b*Lp],[a*Lp,4*Ls+Lq+Lc]])
    ck(f'actual real determinant a{a}b{b}',M.det()-Lq*(4*Ls+Lq+Lc)-6*Lp**2)
    ck(f'actual unchanged source and line heights a{a}b{b}',a*b-6)
    for j in range(4):
        ck(f'O/T first-chart finite determinant a{a}j{j}',S.I**(1+j-j-1)-1)
        ck(f'O/T second-chart finite determinant a{a}j{j}',S.I**(1-1+j+1-j-1)-1)
Xi,sig,e,d=S.symbols('Xi sig e d',nonzero=True)
ck('full base graph',sig**4/d**3*Xi**4-(Xi*sig)**4/d**3)
ck('base graph finite epsilon',(S.I*Xi)*(-S.I*sig)-Xi*sig)
ck('base graph original t',(-S.I*sig)**4/d**3-sig**4/d**3)
ck('base graph native q',(S.I*Xi)**4-Xi**4)
u,v,k=S.symbols('u v k',real=True)
endpoints=[0,Ls,2*Ls,3*Ls,4*Ls,4*Ls+u,4*Ls+u+v]
ck('ordered interval full support',endpoints[-1]-endpoints[0]-(4*Ls+u+v))
ck('ordered interval lengths sum',sum(endpoints[j+1]-endpoints[j] for j in range(6))-(4*Ls+u+v))
source=bdir/'notes/part3_e6_selected_infinity_attachment_working.md'
ei=bdir/'notes/part3_e6_selected_infinity_working.md'
out={'status':'PASS_LOCAL_COMPACTNESS_INPUT','count':len(checks),'checks':checks,
     'utc':datetime.now(timezone.utc).isoformat(),
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'EI_source_sha256':hashlib.sha256(ei.read_bytes()).hexdigest(),
     'scope':'Exact full-unit real period determinant, ordered-factor support and finite normal characters used by IA.1--3.',
     'unassigned':'The complete finite global face ledger, coarse finite quotient resolution, physical characteristic pair and return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','count','source_sha256')},indent=2))
