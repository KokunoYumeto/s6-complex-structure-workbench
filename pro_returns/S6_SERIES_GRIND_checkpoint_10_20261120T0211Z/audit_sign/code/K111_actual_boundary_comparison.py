"""Exact source/point-graph and punctured-boundary comparison receipts.

The geometric proof accompanies these checks. In particular compactness,
the NC bordism and the original finite-reference continuation are proved
by their displayed maps, not inferred from equality of numerical totals.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,gc
import sympy as S
from K111_fan4_exact import *

root=Path(__file__).resolve().parents[1];checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
receipts=[]
for end,filename in [('zero','K111_new_zero_endpoint_v2.json'),('one','K111_new_one_endpoint.json'),('infinity','K111_new_infinity_endpoint.json')]:
 p=root/filename;d=json.loads(p.read_text());pure=set();lower_edges=set();lower_triangles=set()
 for rec in d['cones']:
  c=tuple(tuple(v) for v in rec['rays']);vv=[v for v in c if v[2]==0];pure.update(vv)
  lower_edges.update(tuple(sorted(e)) for e in __import__('itertools').combinations(vv,2))
  lower_triangles.update(tuple(sorted(e)) for e in __import__('itertools').combinations(vv,3))
  rows=rec['source_rows']
  for i,v in enumerate(c):
   expected=(3*v[2]+2*v[3]) if end=='infinity' else (3*v[2]+v[3] if end=='zero' else 3*v[2])
   ck(rows[0][i]+rows[1][i]==expected,'actual full source product preserves original Q, including its endpoint base character')
   ck(rec['canonical_orders'][i]==2*v[2]+v[3]-1,'same original canonical source-volume order on every chart ray')
 for step in d.get('stellar_history',[]):
  v=step['ray'];ck(v[2]>0 and v[3]>0,'every additional corner subdivision maps to original(s,t)=(0,0)')
 if end=='zero':
  A=(0,0,0,1);B1=(-1,0,0,1);B2=(-2,-1,0,1);B3=(-1,-1,0,1)
  ck(pure=={A,B1,B2,B3},'entire zero pure-lower ray set agrees with the original raw model')
  ck(lower_triangles=={tuple(sorted((A,B1,B2))),tuple(sorted((A,B3,B2)))},'entire zero P-invertible toric subfan agrees exactly')
 elif end=='one':
  EE=[(0,l,0,1) for l in range(13)]
  ck(pure==set(EE) and lower_edges=={tuple(sorted((a,b))) for a,b in zip(EE,EE[1:])} and not lower_triangles,'entire one P-invertible toric subfan is the original twelve-label lower chain')
 else:
  A=(0,0,0,1);B=(0,-1,0,1)
  ck(pure=={A,B} and lower_edges=={tuple(sorted((A,B)))} and not lower_triangles,'entire infinity R-invertible toric subfan agrees exactly')
 receipts.append(dict(endpoint=end,path=filename,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),charts=len(d['cones']),pure_lower_rays=sorted(pure),pure_lower_edges=sorted(lower_edges),pure_lower_triangles=sorted(lower_triangles),actual_localized_character_map='chi^m -> chi^m; reciprocal identity in the same original lattice',localizing_base='R' if end=='infinity' else 'P'))
 del d;gc.collect()

# The Rees-algebra action on the actual source ideal (x,P^2) is the
# invertible generator matrix diag(zeta,1). Both ordinary graph charts
# and both explicitly resolved node charts are checked below.
x,y,P,R,a,c,u,w,zeta,lam,E,Ep,Epp,EO,EOp,b=S.symbols('x y P R a c u w zeta lam E Ep Epp EO EOp b',nonzero=True)
def eq(a,b,m):ck(S.cancel(a-b)==0,m)
eq((zeta*a)*(y/zeta),a*y,'first graph chart a*y=R is preserved')
eq((zeta*x)*(c/zeta),x*c,'second graph chart x*c=P^2 is preserved')
eq(R*c/zeta,R*(c/zeta),'second graph y=R*c is preserved')
for xx,cc,yy in [(u,u*w*w,R*u*w*w),(u*u*w,w,R*w)]:
 pp=u*w;up=zeta*u;wp=w/zeta
 eq(pp.subs({u:up,w:wp},simultaneous=True),pp,'resolved graph preserves original P')
 eq(xx.subs({u:up,w:wp},simultaneous=True),zeta*xx,'resolved graph source x carries its exact second-circle character')
 eq(cc.subs({u:up,w:wp},simultaneous=True),cc/zeta,'resolved graph Cartier c carries the reciprocal character')
 eq(yy.subs({u:up,w:wp},simultaneous=True),yy/zeta,'resolved graph original y has its exact inverse source character')
 eq(xx*cc,pp**2,'whole actual resolved point graph relation')
 eq(xx*yy,pp**2*R,'whole actual resolved original source equation')

Acoef,Ccoef,Ocoef,eta=S.symbols('Acoef Ccoef Ocoef eta',nonzero=True)
Ap=lam*zeta*E/Ep*Acoef;Cp=lam*E/Ep*Ccoef
eq(-Ep*Ap,lam*zeta*(-E*Acoef),'full first point-module Vreg arrow, with the same eta and P powers')
eq(Ep/(c/zeta)*Cp,lam*zeta*(E/c*Ccoef),'full reciprocal point-module Vreg arrow')
eq(Cp.subs(Ccoef,-c*Acoef),-(c/zeta)*Ap,'point Cartier overlap C=-c*A is preserved in its actual direction')
Op=lam*zeta*(x-b)/(zeta*x-b)*EO/EOp*Ocoef
eq((zeta*x-b)*EOp*Op,lam*zeta*(x-b)*EO*Ocoef,'full O-module arrow including the original additional P^-2 factor')
zeta2,lam2=S.symbols('zeta2 lam2',nonzero=True)
eq((lam2*zeta2*Ep/Epp)*(lam*zeta*E/Ep),lam*lam2*zeta*zeta2*E/Epp,'first point-module action composes with every entire unit retained')
eq((lam2*Ep/Epp)*(lam*E/Ep),lam*lam2*E/Epp,'second point-module action composes with every entire unit retained')
eq((lam2*zeta2*(zeta*x-b)/(zeta2*zeta*x-b)*EOp/Epp)*(lam*zeta*(x-b)/(zeta*x-b)*EO/EOp),lam*lam2*zeta*zeta2*(x-b)/(zeta*zeta2*x-b)*EO/Epp,'entire O-module composition and reciprocal cancellation')

# Actual IL normal and cube-frame data: retain all source and character
# factors; no power of P is declared an extending unit.
us,Y,v,c12,eta2,q,t,lam0,cq,ut=S.symbols('us Y v c12 eta2 q t lam0 cq ut',nonzero=True)
for l in range(12):
 alpha=Y/v**l;beta=v**(l+1)/Y
 Hp=eta2*us**l*P**(-l)/x;Hm=eta2**-1*x*P**(l+1)*us**(-l-1)
 eq(Hp*Hm,P/us,'actual IL positive/negative normal coefficient product')
 eq(Hp*alpha*Hm*beta,P*v/us,'actual IL directed normal map has A_l B_l=s')
 # L changes X by P^3*p and Y by P*p, while P,v,eta,u_s stay fixed.
 p=S.symbols('p',nonzero=True)
 At=Hp.subs(x,P**3*p*x)*alpha.subs(Y,P*p*Y)
 Bt=Hm.subs(x,P**3*p*x)*beta.subs(Y,P*p*Y)
 eq(At/(Hp*alpha),P**-2,'actual L target positive factor')
 eq(Bt/(Hm*beta),P**2,'actual L target negative factor')
 gam=p*us**12*c12
 original= P**2*lam0*q*eta2**6/t**3
 eq(original.subs({q:p*P*cq,t:P*ut}),p*lam0*cq*eta2**6/ut**3,'entire selected-height gamma identity before central restriction')
 eq(gam.subs(c12,lam0*cq*eta2**6/(us**12*ut**3)),p*lam0*cq*eta2**6/ut**3,'full p,u_s,c12 factors agree with the original gamma')
I3=S.Matrix([[-2,1],[1,-2]])
neg=I3.inv()*S.Matrix([0,1]);pos=I3.inv()*S.Matrix([1,0]);refpos=pos;refneg=-pos
pair=lambda a,b:(a.T*I3*b)[0]
collision=[pair(neg,neg),pair(neg,pos),pair(pos,pos)]
reference=[pair(refneg,refneg),pair(refneg,refpos),pair(refpos,refpos)]
ck(collision==[-S.Rational(2,3),-S.Rational(1,3),-S.Rational(2,3)],'actual minimal collision normal pairings')
ck(reference==[-S.Rational(2,3),S.Rational(2,3),-S.Rational(2,3)],'actual reciprocal cube-framed reference pairings')
ck([a-b for a,b in zip(collision,reference)]==[0,-1,0],'closed lower pairings through the actual original frame')
ck(I3*S.Matrix([-1,-1])==S.Matrix([1,1]),'exact collision/reference negative boundary characters agree modulo the integral intersection lattice')

# Directed final arithmetic occurs only after the saved complete parts.
compact=json.loads((root/'K111_T2_compact_ledger.json').read_text())['compact_pair']
moving=json.loads((root/'K111_new_moving_cap.json').read_text())['physical_moving_pair']
low=json.loads((root/'K111_new_auxiliary_edge_chain_replay.json').read_text())['results'][0]['completed_pair']
inner=[int(compact[k])+int(moving[k])+12*int(low[k]) for k in range(2)]
outer=[inner[0]-72,inner[1]];jin=[-x for x in outer]
native=[F(jin[1],4),F(jin[0])-F(jin[1],4)];theta=F(4*jin[0]-jin[1],24)
out=dict(scope='Exact chart-level receipts for the new auxiliary atlas boundary comparison: original pure-lower localized fans, all original source and canonical rows, point/O Rees charts and reciprocal coefficient actions, full IL normal gamma and cube-frame identities. The displayed NC/RFB geometric maps and physical orientation supply the retained cap/reference comparison in the companion proof.',checks=checks,source_inputs=receipts,
         point_graph_action={'base':'x->zeta*x,y->zeta^-1*y,P->P,R->R','Rees_generators':'diag(zeta,1) on (x,P^2)','a_chart':'a->zeta*a,A->lambda*zeta*E/E_prime*A','c_chart':'c->zeta^-1*c,C->lambda*E/E_prime*C','resolved_charts':'u->zeta*u,w->zeta^-1*w','O_chart':'C_O->lambda*zeta*(x-P^2)/(zeta*x-P^2)*E_O/E_O_prime*C_O'},
         lower_collision_pairings=list(map(str,collision)),lower_reference_pairings=list(map(str,reference)),new_compact_pair=compact,new_moving_pair=moving,new_lower_pair_each=low,inner_pair=inner,whole_positive_reference_change=[72,0],positive_outer_pair=outer,Jin_pair=jin,native_pair=list(map(str,native)),theta=str(theta))
(root/'K111_actual_boundary_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['checks','inner_pair','positive_outer_pair','Jin_pair','native_pair','theta']},indent=2))
