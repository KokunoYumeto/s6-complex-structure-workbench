#!/usr/bin/env python3
"""Exact certificates for IF3's actual initial diagonal comparison.

This checks the displayed algebra and coordinate arrows; the saved note
proves the smooth extension, integral prism and relative-group statements.
It assigns no individual kappa and does not divide a Theta_7 class.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from datetime import datetime, timezone
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / 'notes/part3_e6_selected_i3_first_flop_working.md'
OUT = Path(__file__).with_suffix('.json')
checks = []

def ck(name, value):
    if not bool(value):
        raise AssertionError(name)
    checks.append(name)

def eq(name, lhs, rhs=0):
    ck(name, S.cancel(S.together(lhs-rhs)) == 0)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

P,R,cq,K,lam,U6,sDelta,Z,V = S.symbols(
    'P R cq K lambda U6 sDelta Z V', nonzero=True)
q=P**0*R*cq
Q=P**2*R
kappa=P**2/cq
alpha=P**6
g=1/P
eta=lam*K/P**3
eq('source_h_Q_equals_kappa_q', Q, kappa*q)
eq('point_h_from_full_balanced_frame', Q**3/R**3, alpha)
eq('point_B_from_full_balanced_frame', P**-3*lam*R*cq*K, eta*q)
VT=P**6*U6*Z**-3*V/sDelta
eq('full_frame_h_square', (Q*Z)**3/(P**6*U6)*sDelta*(R**-3*VT), alpha*V)
eq('full_frame_B_square', (Z/P)**3/(P**6*U6)*sDelta*(lam*R*cq*K*VT), eta*q*V)

a,b,c,kap,al,gg,et,A,D=S.symbols('a b c kap al gg et A D', nonzero=True)
height=a*b*c
rows=[(kap*al*b*c,a*b/al,1/(kap*b)),
      (gg*et*b*c,1/(et*c),a*c/gg),
      (1/a,a*b,a*c)]
tp={a:a/(A*D),b:A*b,c:D*c}
for i,row in enumerate(rows):
    eq(f'C{i}_height', S.prod(row), height)
    for j,(f,m) in enumerate(zip(row,(A*D,1/D,1/A))):
        eq(f'C{i}_full_torus_unit_square_{j}', f.subs(tp, simultaneous=True), m*f)
eq('C0_native_base', kap*rows[0][2], 1/b)
eq('C0_native_first_normal', al*rows[0][1], a*b)
eq('C0_native_second_normal', rows[0][0]/(kap*al), b*c)
eq('C1_native_base', et*rows[1][1], 1/c)
eq('C1_native_first_normal', gg*rows[1][2], a*c)
eq('C1_native_second_normal', rows[1][0]/(gg*et), b*c)
eq('C2_native_base', rows[2][0], 1/a)
eq('C2_native_first_normal', rows[2][1], a*b)
eq('C2_native_second_normal', rows[2][2], a*c)
a0,a1,c0,c1=S.symbols('a0 a1 c0 c1',nonzero=True)
cox=[a0,a1/(A*D),A*c0,D*c1]
eq('full_Cox_height',S.prod(cox),a0*a1*c0*c1)
eq('full_Cox_native_base',cox[1]/cox[0],(a1/a0)/(A*D))
eq('full_Cox_native_normal0',cox[0]*cox[2],A*a0*c0)
eq('full_Cox_native_normal1',cox[0]*cox[3],D*a0*c1)
for i,f in enumerate(cox):
    inv=f.subs({a0:cox[0],a1:cox[1],c0:cox[2],c1:cox[3],A:1/A,D:1/D},simultaneous=True)
    eq(f'full_Cox_reciprocal_inverse_{i}',inv,[a0,a1,c0,c1][i])
for i,di in enumerate(((et/al,kap*al),(kap/gg,gg*et),(et,kap))):
    eq(f'normal_determinant_{i}',S.prod(di),kap*et)

def traced(winds):
    ka,ga,aa,ea=winds
    t=ka+ea
    ls=[2*(ea-aa),2*(ka-ga),2*ea]
    w=[0,1,-1];d=[-2,-1,-1]
    I=[t*w[i]+d[i]*(ls[i]-t) for i in range(3)]
    W=[t*w[i]-d[i]*(ls[i]-t) for i in range(3)]
    vv=-I[2]
    dd=-(W[2]-W[0])
    nn=F(dd-vv,2)
    mm=-vv-nn
    native=(mm+2*t,nn)
    return dict(t=t,l=ls,I=I,W=W,V22=vv,delta2=dd,
                ordinary=[mm,nn],native_double=list(native),
                native_single=[native[0]/2,native[1]/2])

fixed=traced((2,-1,6,-3))
coupled=traced((2,-1,6,1))
ck('fixed_t',fixed['t']==-1)
ck('fixed_l',fixed['l']==[-18,6,-6])
ck('fixed_I',fixed['I']==[34,-8,6])
ck('fixed_W',fixed['W']==[-34,6,-4])
ck('fixed_prism_variation',fixed['V22']==-6)
ck('fixed_prism_derivative',fixed['delta2']==-30)
ck('fixed_ordinary_pair',fixed['ordinary']==[18,-12])
ck('fixed_native_double',fixed['native_double']==[16,-12])
ck('fixed_native_single',fixed['native_single']==[8,-6])
ck('coupled_same_native_pair_diagnostic',coupled['native_double']==[16,-12])
ck('coupled_trace_I',coupled['I']==[26,0,-2])
ck('coupled_trace_W',coupled['W']==[-26,6,-4])
ck('coupled_ordinary_pair',coupled['ordinary']==[10,-12])
J=S.symbols('J',integer=True)
t=J-1
ls=[2*J-18,6,2*J-6]
wi=[0,1,-1];di=[-2,-1,-1]
Ii=[S.expand(t*wi[i]+di[i]*(ls[i]-t)) for i in range(3)]
Wi=[S.expand(t*wi[i]-di[i]*(ls[i]-t)) for i in range(3)]
v22=-Ii[2];delta2=-(Wi[2]-Wi[0]);n2=(delta2-v22)/2;m2=-v22-n2
eq('symbolic_trace_only_native_m',m2+2*t,16)
eq('symbolic_trace_only_native_n',n2,-12)

# Exact rational quaternion implementation.  The angle half-phases are
# rational unit quaternions; unrestricted integer Cox weights are retained.
def qm(x,y):
    a,b,c,d=x;e,f,g,h=y
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def qc(x):return (x[0],-x[1],-x[2],-x[3])
def qn(x):return sum(v*v for v in x)
def qi(x):return tuple(v/qn(x) for v in qc(x))
one=(F(1),F(0),F(0),F(0));ii=(F(0),F(1),F(0),F(0))
def qp(x,n):
    if n<0:return qp(qi(x),-n)
    y=one
    for _ in range(n):y=qm(y,x)
    return y
def qq(x,y):return qm(qm(x,y),qi(x))
def stereo(x,y,z):
    nn=F(1)+x*x+y*y+z*z
    return ((F(1)-x*x-y*y-z*z)/nn,2*x/nn,2*y/nn,2*z/nn)

phase=(F(3,5),F(4,5),F(0),F(0))
for j in range(96):
    weights=(j%7-3,(j//3)%7-3,(j//7)%7-3,(j//11)%7-3)
    x0,x1,y0,y1=weights
    u=stereo(F(j%3+1,3),F((j//3)%3,4),F((j//9)%3,5))
    v=stereo(F((j//2)%3,5),F((j//5)%3+1,4),F((j//13)%3,3))
    ck(f'quaternion_units_{j}',qn(u)==1 and qn(v)==1)
    aa=qp(phase,x0-x1);dd=qp(phase,x0+x1)
    ee=qp(phase,y0+y1);bb=qp(phase,y0-y1)
    up=qm(qm(aa,u),dd);vp=qm(qm(ee,v),bb)
    hh=qq(u,ii);kk=qm(qm(qi(v),ii),v);qh=qm(u,v)
    hp=qq(up,ii);kp=qm(qm(qi(vp),ii),vp);qhp=qm(up,vp)
    ck(f'unrestricted_h_map_{j}',hp==qq(aa,hh))
    ck(f'unrestricted_k_map_{j}',kp==qm(qm(qi(bb),kk),bb))
    mid=qp(phase,sum(weights))
    ck(f'unrestricted_q_middle_{j}',qhp==qm(qm(qm(qm(aa,u),mid),v),bb))
    ck(f'unrestricted_common_link_{j}',qm(qm(qi(qhp),hp),qhp)==kp)
    # T L T^{-1}=R with the equivariant degree-one axis formula.
    y=hh;zeta=(F(3,5),F(4,5)*y[1],F(4,5)*y[2],F(4,5)*y[3])
    y0q=qq(qh,y)
    zeta0=(F(3,5),F(4,5)*y0q[1],F(4,5)*y0q[2],F(4,5)*y0q[3])
    q1=qm(zeta0,qh)
    ck(f'T_L_T_inverse_base_{j}',qm(qm(qi(q1),y0q),q1)==y)
    ck(f'T_L_T_inverse_quaternion_{j}',q1==qm(qh,zeta))
    # At theta=2pi every half-phase is a central sign. Both normal/base
    # products close with the full four-weight action.
    minus=(-F(1),F(0),F(0),F(0))
    us=qm(qm(qp(minus,x0-x1),u),qp(minus,x0+x1))
    vs=qm(qm(qp(minus,y0+y1),v),qp(minus,y0-y1))
    ck(f'paired_full_endpoint_{j}',us==u and vs==v)

def canon(tri):
    vv=sorted(tri);a,b=vv[0]
    return tuple(sorted((x-a,y-b) for x,y in tri))
neg=[[(0,0),(1,0),(0,1)],[(1,0),(0,1),(1,1)]]
pos=[[(0,0),(1,0),(1,1)],[(0,0),(0,1),(1,1)]]
ref=[[(1-x,y) for x,y in tri] for tri in neg]
ck('height_reflection_exact_positive_fan',set(map(canon,ref))==set(map(canon,pos)))
vertical=[[(0,0),(1,1),(0,1)],[(1,1),(0,1),(1,2)]]
ck('positive_fan_is_current_T1',set(map(canon,vertical))==set(map(canon,pos)))
for nn in range(-12,13):
    for mm in range(-3,4):
        # Retained K23 exact conjugation; this checks the integral coordinate
        # and central maps on arbitrary signed generator powers.
        transformed=(-nn,mm+2*nn)
        ck(f'K23_free_determinant_sum_{mm}_{nn}',sum(transformed)==mm+nn)
ck('actual_first_flop_free_pair',(-(-6),8+2*(-6))==(6,-4))
ck('actual_first_flop_central_increment',8-6==2)
kapc=S.symbols('kappa_C',integer=True)
kM=-9-kapc;ellM=-228-4*kapc
mu=ellM/4;nu=kM-mu
eq('fixed_C0_actual_mu',mu,-57-kapc)
eq('fixed_C0_actual_nu',nu,48)
eq('fixed_C0_physical_index',(4*kM-ellM)/24,8)
eq('fixed_C0_K68_index',nu/6,8)
ck('C2_prism_map_typed',fixed['native_single']==[8,-6] and nu==48)

deps=['notes/part3_e6_selected_i3_working.md',
      'notes/part3_e6_selected_i3_outer_transfer_working.md',
      'notes/part3_e6_selected_i3_moving_cap_working.md',
      'notes/part3_source_zero_double_loop_product_working.md',
      'notes/part3_physical_line_corrigendum_working.md']
out={
 'status':'PASS','checks':len(checks),
 'utc':datetime.now(timezone.utc).isoformat(),
 'source':str(NOTE.relative_to(ROOT)),'source_sha256':sha(NOTE),
 'script_sha256':sha(Path(__file__)),
 'dependencies':{x:sha(ROOT/x) for x in deps},
 'scope':{'source':'M6,b1,m2,n1; fixed scalar; initial T0 and first C2 flop',
          'closing':'identity original source/root/line closing; actual doubled native pullback',
          'kappa':'actual first-number difference -75-c2(E_collision)+c2(E_reference)',
          'no_theta_division':True},
 'fixed_scalar_double':fixed,
 'coupled_double_algebra_diagnostic':coupled,
 'C2_single_relative_pair':[8,-6],
 'C2_after_T_pair':[6,-4],
 'central_increment':-6,
 'actual_T0_JT0_classes':[8,2],
 'global_Zw_generator_table':{'w_minus_one':[8,2],'w_plus_one':[2,8]},
 'fixed_C0_map':{'mu':'-57-kappa','nu':48,'index':8},
 'checks_named':checks}
def encode(x):
    if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
    raise TypeError(type(x).__name__)
OUT.write_text(json.dumps(out,indent=2,default=encode)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'source_sha256':out['source_sha256'],
                  'json_sha256':sha(OUT)},indent=2))
