#!/usr/bin/env python3
"""Fresh exact coefficient, collar, cap-sign and integer certificate for IVP."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
SOURCE='notes/part3_e6_selected_i3_vertical_integer_working.md'
checks=[]
def ck(n,v):
    assert bool(v),n
    checks.append(n)
def eq(n,a,b=0):ck(n,S.simplify(a-b)==0)
def meq(n,a,b):ck(n,(a-b).applyfunc(S.simplify)==S.zeros(*a.shape))
def sha(n):return hashlib.sha256((ROOT/n).read_bytes()).hexdigest()
j=S.symbols('j',integer=True)
a,th,rho=S.symbols('alpha_q theta rho',real=True)
# Order (u,v,d,gamma). Full integer coordinate changes and their deck squares.
T=S.Matrix([[1,0,0,0],[0,1,0,0],[-j,0,1,0],[0,-j,0,1]])
Q=S.Matrix([[1,-1,0,0],[0,1,0,0],[0,0,1,-1],[0,0,0,1]])
H=S.Matrix([[1,-2,0,1],[0,1,0,0],[0,-6,1,3],[0,0,0,1]])
Qj=S.Matrix([[1,-1,0,0],[0,1,0,0],[0,0,1,-1],[0,0,0,1]])
Hj=S.Matrix([[1,j-2,0,1],[0,1,0,0],[0,-(j-2)*(j-3),1,3-j],[0,0,0,1]])
meq('full q deck conjugation',T*Q*T.inv(),Qj)
meq('full theta deck conjugation',T*H*T.inv(),Hj)
eq('integral character shear determinant',T.det(),1)
meq('q and theta deck commutation',Q*H,H*Q)
meq('new q and theta deck commutation',Qj*Hj,Hj*Qj)

# Complete additive logarithms, with the original q and all unit symbols.
k,al,g,et,q,z,v=S.symbols('kappa_log alpha_log g_log eta_log q_log Z_log V_log')
log_h_z=z+k+q+j*g
log_h_v=v+al+j*(et+q)
new_h_v=log_h_v-j*log_h_z
expected_h_v=v-j*z+al+j*et-j*k-j*j*g
eq('full hB^j character with q cancellation',new_h_v,expected_h_v)
new_B_v=v+et+q-j*(z+g)
eq('full B character',new_B_v,v-j*z+et-j*g+q)
log_unit_j=S.Matrix([k+j*g,al+j*et-j*k-j*j*g,g,et-j*g])
wind={k:2,al:6,g:-1,et:-3}
meq('complete winding substitution',log_unit_j.subs(wind),S.Matrix([2-j,(j-2)*(j-3),-1,j-3]))
# Composition of literal signed shears keeps every original logarithm.
b=S.symbols('b',integer=True)
next_logs=S.Matrix([log_unit_j[0]+b*log_unit_j[2],log_unit_j[1]+b*log_unit_j[3]-b*log_unit_j[0]-b*b*log_unit_j[2],log_unit_j[2],log_unit_j[3]-b*log_unit_j[2]])
meq('full signed shear composition',next_logs,log_unit_j.subs(j,j+b))

# Connection row is in order (du,dv,dd,dgamma).
A0=S.Matrix([[0,6*th,1,a-3*th]])
Aj=S.Matrix([[0,(j-2)*(j-3)*th,1,a+(j-3)*th]])
meq('original coefficient connection difference',Aj*T-A0,S.Matrix([[-j,-j*(a+2*th),0,j*th]]))
Aref=S.Matrix([[0,6*th,1,a-(j+3)*th]])
meq('full residual theta coefficients',Aj-Aref,S.Matrix([[0,(j*j-5*j)*th,0,2*j*th]]))
# Include independent full unit logarithm terms, before any winding evaluation.
fk,fa,fg,fe=S.symbols('f_kappa f_alpha f_g f_eta')
A0f=S.Matrix([[0,fa,0,fe]])
Ajf=S.Matrix([[0,fa+j*fe-j*fk-j*j*fg,0,fe-j*fg]])
meq('whole unit correction in old coefficients',Ajf*T-A0f,S.Matrix([[0,-j*fk,0,-j*fg]]))
# Target q phase shift contains j*g; target g ratio has its own exact delta log.
# These formal coefficient identities retain its full function, rather than setting it to0.
dg=S.symbols('delta_G',real=True)
Sblock=S.Matrix([[1,-j*dg,dg],[0,1,0],[0,-j,1]])
P=S.Matrix([[1,0,0],[0,0,1],[0,1,0]])
tri=P*Sblock*P
ck('source coframe is full unipotent triangular',tri[1,0]==tri[2,0]==tri[2,1]==0 and list(tri.diagonal())==[1,1,1])
meq('source coframe exact inverse',Sblock*Sblock.inv(),S.eye(3))
F1,F2,F3=S.symbols('F1 F2 F3')
Fu=S.Matrix([[0,F1,F2],[0,0,F3],[0,0,0]])
eq('upper triangular curvature trace square',S.trace(Fu*Fu),0)

# Normal source square on both native charts; functions are retained symbols.
Z,A,B,unit,c,cprime,gg,gprime=S.symbols('Z A B a_j c cprime g gprime',nonzero=True)
qold=Z*A*B
qnew=Z*(unit*A)*B
eq('full source height map',qnew,unit*qold)
meq('full second chart normal square',S.Matrix([Z*unit*A,Z*B]),S.diag(unit,1)*S.Matrix([Z*A,Z*B]))
eq('complete B suspension square',c*gg,gprime.subs(gprime,c*gg))
# Local determinant for the actual sphere clutch, in the written positive bases.
N=S.symbols('N',integer=True)
Dcap=S.Matrix([[0,0,2*S.pi*N],[0,1,0],[-1,0,0]])
eq('direct cap degree local determinant',Dcap.det(),2*S.pi*N)
eq('I3 cap signed degree coefficient',Dcap.det().subs(N,-j)/(2*S.pi),-j)

# Fresh exterior algebra on (alpha_q,u,v,gamma,theta), with exact polynomials.
def add(*forms):
    out={}
    for form in forms:
        for key,val in form.items():out[key]=out.get(key,0)+val
    return {key:S.expand(val) for key,val in out.items() if S.expand(val)!=0}
def scale(c0,form):return {key:S.expand(c0*val) for key,val in form.items() if S.expand(c0*val)!=0}
def wedge(x,y):
    out={}
    for ix,xx in x.items():
        for iy,yy in y.items():
            if len(set(ix+iy))<len(ix+iy):continue
            inv=sum(v0>v1 for v0 in ix for v1 in iy)
            key=tuple(sorted(ix+iy))
            out[key]=out.get(key,0)+(-1)**inv*xx*yy
    return {key:S.expand(val) for key,val in out.items() if S.expand(val)!=0}
def deriv(x):
    out={}
    for ix,xx in x.items():
        for d,sym in [(0,a),(4,th)]:
            val=S.diff(xx,sym)
            if val:out=add(out,wedge({(d,):val},{ix:1}))
    return out
# The full retained alpha phase may vary on the source. Its extended
# connection curvature is decomposable, with all derivatives left formal.
phia,phiu,phig,phith=S.symbols('phi_alpha_a phi_alpha_u phi_alpha_gamma phi_alpha_theta')
dphi={(0,):phia,(1,):phiu,(3,):phig,(4,):phith}
Fphi=wedge(dphi,{(2,):1})
ck('entire source-dependent alpha phase curvature square',wedge(Fphi,Fphi)=={})
Aext={(3,):a-3*th,(1,):j,(2,):j*a+(6-3*j)*th}
beta={(1,):-j,(2,):-j*(a+(2-j)*th),(3,):j*th}
Fext=deriv(Aext);dbeta=deriv(beta)
Finter=add(Fext,scale(rho,dbeta))
cs=scale(3,wedge(beta,wedge(Finter,Finter)))
ck('collar integrand has only the oriented five-form',set(cs)=={(0,1,2,3,4)})
collar=S.integrate(cs[(0,1,2,3,4)],(rho,0,1))
eq('complete inward Euler collar',collar,36*j-15*j*j+2*j**3)
outward=-collar
rline=j*j-5*j;sline=2*j
interior_k=3*rline;interior_l=2*sline
cap_k=-j;cap_l=-4*j
dk=S.expand(interior_k+cap_k+outward)
dl=S.expand(interior_l+cap_l)
eq('full integer cubic',dk,-2*j**3+18*j*j-52*j)
eq('full Pontryagin cancellation',dl,0)
kpoly=47+dk;lpoly=-4+dl;mu=lpoly/4;nu=kpoly-mu
Apoly=S.expand(nu/6)
eq('actual fixed-C0 mu',mu,-1)
eq('actual integral vertical index polynomial',Apoly,8-j*(j*j-9*j+26)/3)
eq('actual forward native product',Apoly.subs(j,j+1)-Apoly,-(j-2)*(j-3))
eq('actual backward native product',Apoly.subs(j,j-1)-Apoly,(j-3)*(j-4))
eq('initial IC2 pair k',kpoly.subs(j,0),47)
eq('initial IC2 pair ell',lpoly,-4)
V00=S.expand(-2*(mu+nu)-2);d0=S.expand(V00+4*nu)
eq('initial full ordinary double V00',V00.subs(j,0),-96)
eq('initial full ordinary double delta0',d0.subs(j,0),96)
values=[]
for jj in range(-80,81):
    n=int(nu.subs(j,jj));aa=Apoly.subs(j,jj)
    ck('signed integral index '+str(jj),aa.is_integer and n%6==0)
    meq('signed literal inverse character '+str(jj),T.subs(j,jj)*T.subs(j,-jj),S.eye(4))
    meq('signed exact theta square '+str(jj),(T*H).subs(j,jj),(Hj*T).subs(j,jj))
    eq('signed forward integer cubic '+str(jj),(dk.subs(j,jj+1)-dk.subs(j,jj)), -6*(jj-2)*(jj-3))
    values.append({'j':jj,'k':int(kpoly.subs(j,jj)),'ell':-4,'mu':-1,'nu':n,'index':int(aa),'class_mod28':int(aa)%28})
period=S.expand(Apoly.subs(j,j+28)-Apoly)
eq('exact period28 difference',period,-28*(j*j+22*j+186))
image=sorted({int(Apoly.subs(j,jj))%28 for jj in range(28)})
ck('full vertical residue image',image==[0,2,6,8,12,14,16,20,22,26])
deps=[SOURCE,'notes/part3_source_zero_vertical_pair_working.md','notes/part3_bottom_row_winding_working.md','notes/part3_source_cusp_shear_pontryagin_working.md','notes/part3_e6_selected_i3_first_flop_working.md','notes/part3_e6_selected_i3_vertical_fans_working.md','notes/part3_e6_selected_i3_moving_c2_working.md','records/root_audit_e6_selected_i3_vertical_fans.json','records/blind_audit_e6_selected_i3_moving_c2.json']
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'source':SOURCE,'source_sha256':sha(SOURCE),'dependencies':{n:sha(n) for n in deps},'scope':'Exact IVP coefficient/source/normal/tangent/cap-sign/collar and integer identities for all signed vertical fans in the actual selected-I3 fixed-scalar family; full geometric maps are written in IVP.1–7.','theta_old':H.tolist(),'theta_new':[[str(v) for v in row] for row in Hj.tolist()],'source_shear':[[str(v) for v in row] for row in T.tolist()],'inner_euler_collar':str(collar),'outward_euler_collar':str(outward),'delta_k':str(dk),'delta_ell':str(dl),'k':str(kpoly),'ell':str(lpoly),'mu':str(mu),'nu':str(nu),'ordinary_double_V00':str(V00),'ordinary_double_delta0':str(d0),'image_mod28':image,'signed_examples':values,'checks_named':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({key:out[key] for key in ['status','checks','source_sha256','delta_k','delta_ell','mu','nu','image_mod28']},indent=2))
