"""Exact quaternion identities on the actual charged-link overlap."""
from pathlib import Path
from datetime import datetime,timezone
import json,sympy as s

root=Path(__file__).resolve().parents[2]
w=tuple(s.symbols('w0:4',real=True));u=tuple(s.symbols('u0:4',real=True))
def mul(a,b):
    return (a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],
            a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
            a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],
            a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0])
def conj(a):return(a[0],-a[1],-a[2],-a[3])
def norm(a):return sum(x*x for x in a)
def scale(a,t):return tuple(t*x for x in a)
def inv(a):return scale(conj(a),1/norm(a))
checks=[]
def eq(name,a,b):
    assert all(s.cancel(x-y)==0 for x,y in zip(a,b)),name
    checks.append(name)
wu=mul(w,u)
eq('quaternion inverse reconstructs actual source chart',mul(wu,inv(u)),w)
eq('other base coordinate is inverse',mul(u,inv(wu)),inv(w))
eq('Hopf transition retains full conjugation',
   mul(mul(wu,(0,1,0,0)),inv(wu)),
   mul(mul(w,mul(mul(u,(0,1,0,0)),inv(u))),inv(w)))
eq('norm multiplicativity',(s.expand(norm(wu)),),(s.expand(norm(w)*norm(u)),))
c,t=s.symbols('c t',real=True);phase=(c,t,0,0)
eq('full Hopf lift commutes with physical right phase',mul(w,mul(u,phase)),mul(wu,phase))
eq('right complex phase preserves Hopf i',mul(phase,(0,1,0,0)),mul((0,1,0,0),phase))
eq('residual sign is carried',mul(w,scale(u,-1)),scale(wu,-1))
eq('other chart reconstructs second quaternion',mul(inv(w),wu),u)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':len(checks),
     'identities':checks,'scope':'Exact overlap, full Hopf lift, phase/sign action and source-coordinate reconstruction on the charged link. The finite period-strip native-quaternion identification remains a separate map obligation.'}
(root/'code/part3_root/source_zero_charged_quaternion.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
