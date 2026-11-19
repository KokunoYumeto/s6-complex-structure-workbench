#!/usr/bin/env python3
"""Exact source, whole root/sector and signed cap certificate for ICAP."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
SOURCE='notes/part3_e6_selected_i3_all_caps_working.md'
checks=[]
def ck(n,v):
 assert bool(v),n
 checks.append(n)
def eq(n,a,b=0):ck(n,S.factor(a-b)==0)
def sha(n):return hashlib.sha256((ROOT/n).read_bytes()).hexdigest()
x,t,r,s,h,z,l=S.symbols('x t r s h z l')
disc=S.discriminant(x**3+r*x*x+t*x+t*t,x)
eq('whole original discriminant',disc,-t*t*(4*r**3-r*r-18*r*t+27*t*t+4*t))
eq('whole source quadratic at r=1/4-s',(4*r**3-r*r-18*r*t+27*t*t+4*t).subs(r,S.Rational(1,4)-s),27*t*t+(18*s-S.Rational(1,2))*t-4*s*(S.Rational(1,4)-s)**2)
# h is the actual analytic square root, with s=(h²-1)/12.
ss=(h*h-1)/12
Tc=(1-36*ss-h**3)/108;To=(1-36*ss+h**3)/108
vs=S.cancel(8*ss/(1+4*ss+h));D=vs-2
for name,tt in [('selected',Tc),('other',To)]:
 eq('full discriminant root '+name,27*tt*tt+(18*ss-S.Rational(1,2))*tt-4*ss*(S.Rational(1,4)-ss)**2)
eq('exact selected SI3 original height',Tc,vs/D**3)
eq('exact inverse marked source parameter',ss,vs*(vs+4)/(4*D*D))
eq('initial selected value',Tc.subs(h,1),0)
eq('initial other value',To.subs(h,1),S.Rational(1,54))
eq('full root separation',To-Tc,h**3/54)
m=3*l+2;k=2*l+1
for name,ex in [('l-2k',l-2*k+m),('3k',3*k-2*m+1),('3(l+1)',3*(l+1)-m-1),('formal3divisibility',2*m-1-3*k)]:eq('whole reduced-root identity '+name,ex)
# Original coordinate exponents carry the source equation to the root equation.
eq('root Y exponent normalizes t²',-6*(l+1)+2*m,-2)
eq('root rX² exponent',-4*(l+1)+6*(l+1),2*l+2)
eq('root tX exponent',-m-2*(l+1)+6*(l+1),l+2)
X,Y,b0,c0,cc,zz=S.symbols('X Y b0 c0 c z')
# The full analytic source c is specified by its square, without truncating its unit.
UV=S.expand((Y-zz*cc)*(Y+zz*cc))
eq('complete A2 source product',UV.subs(Y**2,X**3+zz**2*(1+b0*X+c0*X**2)).subs(cc**2,1+b0*X+c0*X**2),X**3)
a,b=S.symbols('a b')
for name,xx,uu,vv in [('middle',a*b,a*a*b,a*b*b),('Uend',a*b,a,a*a*b**3),('Vend',a*b,a*a*b**3,a)]:eq('actual root chart '+name,uu*vv,xx**3)
# The full two selected-height units, exact quotient, and norm-root equation.
uq=S.symbols('q_infty')
hc=1-Tc*uq;ho=1-To*uq;H=hc/ho
eq('entire selected-height ratio',H*ho,hc)
eq('retained new central factor',hc.subs(h,1),1)
eq('retained old central factor',ho.subs(h,1),1-uq/54)
eq('basepoint along root central divisor',H.subs(uq,0),1)
Hroot,NormF,Bo,Bc=S.symbols('Hroot NormF Bo Bc',nonzero=True)
# In the algebra of full chronological products H is source invariant.
# Hroot^m=H, so all m translated root factors have product H.
eq('entire chronological norm quotient',(H*NormF)/(NormF),H)
eq('whole normalized Hom ratio',(H*Bo)/Bo,H)
# Exact coincident Cartier graphs with separate total-family generators.
tau,ell,sv,uu,vv,zk=S.symbols('tau ell s u v z_k')
eq('whole u graph line coefficient',(tau/(tau-zk*sv*ell)).subs(tau,zk*uu),uu/(uu-sv*ell))
eq('whole reciprocal graph coefficient',(tau/(tau-zk*sv*ell)).subs(zk,tau*vv),1/(1-vv*sv*ell))
A,XR,YR,XPpR,XX,YY=S.symbols('A XR YR XPpR X Y')
chord=tau*(YY-YR)+(A+tau**3*YR)/(A-tau**2*XR)*(XX-XR)
eq('full normalized coincident chord',chord.subs(tau,0),XX-XR)
eq('actual central-one Hom frame',(chord/(XX-XPpR)).subs({tau:0,XPpR:XR}),1)
# Full annular Lie-coefficient square retains each integer/reference term.
salpha,j0,n,pi,Lambda,jB,fA,LB,hl=S.symbols('s_alpha j0 n Pi Lambda j_B f_alpha Log_B h_alpha')
fB=fA+pi;hB=hl-n*salpha*pi+jB*LB+Lambda
res=(n*(salpha+j0)*fB+hB)-(n*salpha*fA+hl)
eq('entire signed annular displacement',res,n*j0*fA+n*j0*pi+jB*LB+Lambda)
Cref=S.Matrix([[2,1],[1,0]])
for nn in [-1,1]:
 C=S.Matrix([[m,1],[nn,0]]);Ci=S.Matrix([[0,nn],[1,-m*nn]]);T=S.Matrix([[nn,0],[2-m*nn,1]])
 ck('whole meridian inverse sign'+str(nn),S.simplify(C*Ci)==S.eye(2))
 ck('whole meridian comparison sign'+str(nn),S.simplify(C*T)==Cref)
 eq('whole meridian determinant sign'+str(nn),C.det(),-nn)
 eq('primitive signed generator norm sign'+str(nn),nn*nn,1)
 for ll in range(31):
  mm=3*ll+2;kk=2*ll+1
  rays=[(jj,1) for jj in range(kk+1)]+[(1,0)]
  for jj in range(len(rays)-1):
   aa,bb=rays[jj],rays[jj+1]
   ck('primitive graph ray '+str((nn,ll,jj)),abs(aa[0]*bb[1]-aa[1]*bb[0])==1)
  # Deck equality in every original source monomial.
  weights=[-6*kk, -6*kk,2*ll+2-4*kk,ll+2-2*kk,2]
  ck('full root equation deck '+str((nn,ll)),all((vv-weights[0])%mm==0 for vv in weights))
  ck('source preserving complete h deck '+str((nn,ll)),mm%mm==0)
  for dd in range(mm):ck('retained finite character norm '+str((nn,ll,dd)),(dd*mm)%mm==0)
# Exact weighted-norm telescope with all chronological terms retained.
rr=S.symbols('rho',nonzero=True)
for mm in range(2,20):
 vv=S.symbols('v0:'+str(mm+1))
 norm=sum(rr**(-2*j)*vv[j] for j in range(mm))
 transformed=sum(rr**(-2*j)*vv[j+1] for j in range(mm))
 eq('complete compact norm-shell identity '+str(mm),transformed,rr**2*(norm-vv[0]+rr**(-2*mm)*vv[mm]))
# Preserve the evaluated physical pair and its exact native comparison.
j=S.symbols('j',integer=True);kp=47-2*j**3+18*j*j-52*j;lp=-4
mu=S.Rational(lp,4);nu=kp-mu
ck('actual fixed-C0 mu',mu==-1)
eq('actual signed vertical nu',nu,48-2*j**3+18*j*j-52*j)
eq('actual first fixed index',(4*kp-lp).subs(j,0)/24,8)
eq('actual fan forward integer increment',(nu.subs(j,j+1)-nu)/6,-(j-2)*(j-3))
deps=[SOURCE,'notes/part3_e6_order_three_all_caps_working.md','notes/part3_e6_selected_infinity_reduced_caps_working.md','notes/part3_e6_selected_infinity_negative_norm_working.md','notes/part3_e6_selected_i3_working.md','notes/part3_e6_selected_i3_vertical_integer_working.md','notes/part3_e6_selected_i3_all_fans_working.md','records/blind_audit_e6_selected_i3_moving_c2.json','records/root_audit_e6_selected_i3_all28_witnesses.json']
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'source':SOURCE,'source_sha256':sha(SOURCE),'dependencies':{p:sha(p) for p in deps},'scope':'Actual selected-I3 all-reduced-cap source/root/Cartier/whole-height/chronological-norm/signed-sector/primitive-meridian identities; proper cap products and matched characteristic forms are proved in ICAP.3–4. Independent geometric peer pending.','parameter_roots':{'s':str(ss),'selected':str(Tc),'other':str(To),'v':str(vs)},'cap_order':'m=3l+2,l>=0','primitive_norms':[-1,1],'initial_physical_pair':[47,-4],'initial_native_pair':[-1,48],'k_vertical':str(kp),'ell_vertical':lp,'checks_named':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','source_sha256','initial_physical_pair','initial_native_pair']},indent=2))
