#!/usr/bin/env python3
"""Exact algebra supporting K41's actual cap-data endpoint proof."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as sp

root = Path(__file__).resolve().parents[2]
l,k=sp.symbols('l k', integer=True, nonnegative=True)
checks=[]
root_rows=[
 ('III* reduced',4*l+3,3*l+2,0),('III* good',4*l,3*l,1),
 ('IV* reduced',3*l+2,2*l+1,0),('IV* good',3*l,2*l,1),
 ('III reduced',4*l+1,l,0),('III good',4*l,l,1),
 ('IV reduced',3*l+1,l,0),('IV good',3*l,l,1),
 ('II reduced',6*l+1,l,0),('II good',6*l,l,1),
 ('I1* quadratic',sp.Integer(2),sp.Integer(1),0)]
lie_rows=[]
for name,m,weight,lower in root_rows:
 for label,p,positive in [('k',weight,False),('m-k',m-weight,True)]:
  shifted=sp.Poly(sp.expand(p.subs(l,l+lower)),l)
  assert all(c>=0 for c in shifted.all_coeffs())
  if positive: assert shifted.eval(0)>0
 checks.append(name+': 0<=root Lie weight<m on full progression')
 lie_rows.append({'name':name,'m':str(m),'k':str(weight),'lower_l':lower,
                  'invariant_frame':'z^k * root vector = original source vector'})

# The actual source vector 2y*d/dx becomes z^k(2Y*d/dX).
z,Y,kk=sp.symbols('z Y kk', nonzero=True)
assert sp.simplify(2*z**(3*kk)*Y/z**(2*kk)-z**kk*2*Y)==0
checks.append('exact dual-Weierstrass source Lie substitution')

# The cyclic averaging identity is exact before reducing x^m=1.
x=sp.symbols('x');m=sp.symbols('m',integer=True,positive=True)
norm=(1-x**m)/(1-x)
weighted=x*sp.diff(norm,x)
assert sp.simplify((1-x)*weighted-norm+m-(m-1)*(1-x**m))==0
checks.append('cyclic weighted-sum identity with retained x^m-1 term')

b,K,J,ell,M,eps,Ec,Es,Ns=sp.symbols('b K J ell M eps Ec Es Ns',nonzero=True)
deg=-J-K*(Ec+Es)-ell*Ns
reduced=sp.expand(deg.subs({Es:-sp.Rational(1,1)/b-Ec,Ns:eps/M}))
assert sp.simplify(reduced-(-J+K/b-eps*ell/M))==0
checks.append('full endpoint divisor degree equals -j+k/b-epsilon*ell/M')
assert sp.simplify(reduced.subs(J,K/b-eps*ell/M))==0
checks.append('exact cusp reindexing solution')
assert sp.simplify((K-b*(K/b-eps*ell/M))-eps*b*ell/M)==0
checks.append('integer endpoint obstruction k-bj=epsilon*b*ell/M')
alpha,ni=sp.symbols('alpha ni')
assert sp.simplify((M*alpha*ni).subs(alpha,ell/M)-ell*ni)==0
checks.append('actual ordinary-to-cap scalar exponent ell*n_i')

# Every symbolic root branch, rather than samples of the root orders.
catalogue=json.loads((root/'code/part3/canonical_scalar_catalogue.json').read_text())
branches=[]
for row in catalogue['branches']:
 if row['status']!='proved_canonical_scalar_branch': continue
 expr=sp.sympify(row['M'],locals={'l':l,'k':k})
 short=sp.cancel(expr/sp.Integer(row['b']))
 assert all(c.is_Integer for c in sp.Poly(short,l,k).coeffs())
 assert sp.simplify(short-sp.sympify(row['M_over_b'],locals={'l':l,'k':k}))==0
 checks.append(row['id']+': exact shorter scalar period M/b is integral')
 branches.append({'id':row['id'],'M':str(expr),'b':row['b'],'minimal_closed_scalar_winding':str(short)})
assert len(branches)==30

# Free-group computation of the physical-return arrow, without commuting maps.
def red(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return tuple(out)
def inv(w):return tuple(-a for a in reversed(w))
def mul(*ws):return red(sum((tuple(w) for w in ws),()))
I0,I1,C,E,P=(1,),(2,),(3,),(4,),(5,)
EX=mul(inv(I1),C,E,I0)
PX=mul(inv(I1),P,I0)
physical=mul(I0,inv(EX),PX,inv(I0))
assert physical==mul(inv(E),inv(C),P)
checks.append('literal physical return E_Y^-1 C^-1 P_Y, with no commutation assumed')

result={'status':'PASS','statement':'P3K.41','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'identities':checks,'root_lie_rows':lie_rows,'branches':branches,
 'fixed_scalar_endpoint_group':'physical C*; finite root kernels retained before global valuation',
 'physical_return_arrow':'Phi=E^{-1}P, for E:X_start->X_end',
 'scope':'Exact algebra and symbolic catalogue; geometric atlas, covering, line and toric maps are proved in the note and independently audited by root.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
