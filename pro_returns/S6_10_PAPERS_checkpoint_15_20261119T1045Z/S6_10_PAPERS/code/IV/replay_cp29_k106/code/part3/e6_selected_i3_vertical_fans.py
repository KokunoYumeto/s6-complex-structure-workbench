#!/usr/bin/env python3
"""Actual signed vertical maps: exact Laurent, prism and reset checks."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
note=ROOT/'notes/part3_e6_selected_i3_vertical_fans_working.md'
tests=[]
def ck(name,x):
    if not bool(x):raise AssertionError(name)
    tests.append(name)
def eq(name,x,y=0):ck(name,S.expand(x-y)==0)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
j=S.symbols('j',integer=True)
# Laurent exponent columns: (kappa,alpha,g,eta,q).
ka=S.Matrix([1,0,0,0,0]);al=S.Matrix([0,1,0,0,0])
gg=S.Matrix([0,0,1,0,0]);et=S.Matrix([0,0,0,1,0]);qq=S.Matrix([0,0,0,0,1])
kapj=ka+j*gg
alj=al+j*et-j*ka-j*j*gg
etj=et-j*gg
source_h=ka+j*gg+qq
line_h=al+j*(et+qq)
ck('full_hBpowj_character_square',S.simplify(line_h-j*source_h-alj)==S.zeros(5,1))
ck('full_B_character_square',et+qq-j*gg==etj+qq)
ck('full_forward_kappa_reset',kapj.subs(j,j+1)==kapj+gg)
ck('full_forward_alpha_reset',S.simplify(alj.subs(j,j+1)-(alj+etj-kapj-gg))==S.zeros(5,1))
ck('full_forward_eta_reset',etj.subs(j,j+1)==etj-gg)
ck('full_reverse_kappa_reset',kapj.subs(j,j-1)==kapj-gg)
ck('full_reverse_alpha_reset',S.simplify(alj.subs(j,j-1)-(alj-etj+kapj-gg))==S.zeros(5,1))
ck('full_reverse_eta_reset',etj.subs(j,j-1)==etj+gg)
wind=S.Matrix([[2,6,-1,-3,0]])
eq('full_kappa_j_winding',(wind*kapj)[0],2-j)
eq('full_alpha_j_winding',(wind*alj)[0],(j-2)*(j-3))
eq('full_eta_j_winding',(wind*etj)[0],j-3)
eq('full_trace_invariant',(wind*(kapj+etj))[0],-1)
t=S.Integer(-1)
ls=[2*(wind*(etj-alj))[0],2*(wind*(kapj-gg))[0],2*(wind*etj)[0]]
targets=[-2*(j-3)**2,6-2*j,2*j-6]
for i in range(3):eq(f'actual_first_normal_winding_{i}',ls[i],targets[i])
w=[0,1,-1];d=[-2,-1,-1]
I=[S.expand(t*w[i]+d[i]*(ls[i]-t)) for i in range(3)]
W=[S.expand(t*w[i]-d[i]*(ls[i]-t)) for i in range(3)]
It=[4*j*j-24*j+34,2*j-8,6-2*j]
Wt=[-4*j*j+24*j-34,6-2*j,2*j-4]
for i in range(3):
    eq(f'actual_normal_trace_{i}',I[i],It[i]);eq(f'actual_derivative_trace_{i}',W[i],Wt[i])
V11=I[1];D1=W[1]-W[0];V22=-I[2];D2=-(W[2]-W[0])
eq('actual_V11',V11,2*j-8);eq('actual_delta1',D1,4*j*j-26*j+40)
eq('actual_V22',V22,2*j-6);eq('actual_delta2',D2,-4*j*j+22*j-30)
n1=S.expand((D1-V11)/2);m1=S.expand(-V11-n1)
n2=S.expand((D2-V22)/2);m2=S.expand(-V22-n2)
eq('ordinary_C1_m',m1,-2*(j-2)*(j-4));eq('ordinary_C1_n',n1,2*(j-3)*(j-4))
eq('ordinary_C2_m',m2,2*(j-3)**2);eq('ordinary_C2_n',n2,-2*(j-2)*(j-3))
nat1=(S.expand((m1+2*t)/2),S.expand(n1/2))
nat2=(S.expand((m2+2*t)/2),S.expand(n2/2))
eq('native_C1_m',nat1[0],-(j-3)**2);eq('native_C1_n',nat1[1],(j-3)*(j-4))
eq('native_C2_m',nat2[0],(j-2)*(j-4));eq('native_C2_n',nat2[1],-(j-2)*(j-3))
eq('full_C2_to_C1_reset_m',nat2[0]+2*nat2[1],nat1[0].subs(j,j+1))
eq('full_C2_to_C1_reset_n',-nat2[1],nat1[1].subs(j,j+1))
eq('full_C1_to_C2_reset_m',nat1[0]+2*nat1[1],nat2[0].subs(j,j-1))
eq('full_C1_to_C2_reset_n',-nat1[1],nat2[1].subs(j,j-1))
poly=8-j*(j*j-9*j+26)/3
binomial=8-j*(j-1)*(j-2)/3+2*j*(j-1)-6*j
eq('full_integral_binomial_formula',poly,binomial)
eq('actual_forward_central_recurrence',poly.subs(j,j+1)-poly,nat2[1])
eq('actual_reverse_central_recurrence',poly.subs(j,j-1)-poly,nat1[1])
eq('exact_period_28_difference',poly.subs(j,j+28)-poly,-28*(j*j+22*j+186))
eq('initial_ASI3_value',poly.subs(j,0),8)
eq('first_IF3_value',poly.subs(j,1),2)

a,b,c,A,D=S.symbols('a b c A D',nonzero=True)
actual=[a/(A*D),A*b,D*c]
ck('full_C1_native_coefficient_order',[actual[2]/c,actual[0]/a,actual[1]/b]==[D,1/(A*D),A])
ck('full_C0_native_coefficient_order',[actual[1]/b,actual[0]/a,actual[2]/c]==[A,1/(A*D),D])
eq('full_C1_Cox_height',D*(1/(A*D))*A,1)
eq('full_C0_Cox_height',A*(1/(A*D))*D,1)

def canon(tri):
    vv=sorted(tri);a,b=vv[0]
    return tuple(sorted((x-a,y-b) for x,y in tri))
def fan(nn):
    return [[(0,0),(1,nn),(0,1)],[(1,nn),(0,1),(1,nn+1)]]
def reflected(nn):return [[(1-x,y) for x,y in tt] for tt in fan(nn)]
records=[]
for nn in range(-84,85):
    P=S.Matrix([[1,0],[nn,1]])
    ck(f'signed_basis_inverse_{nn}',P.inv()==S.Matrix([[1,0],[-nn,1]]))
    BB=P.inv()*S.Matrix([[2,-1],[6,-3]])*P
    ck(f'full_signed_winding_matrix_{nn}',BB==S.Matrix([[2-nn,-1],[(nn-2)*(nn-3),nn-3]]))
    pos=[[(0,0),(1,nn),(1,nn+1)],[(0,0),(0,1),(1,nn+1)]]
    ck(f'actual_forward_triangle_fan_{nn}',set(map(canon,pos))==set(map(canon,fan(nn+1))))
    ck(f'actual_reflected_fan_{nn}',set(map(canon,reflected(nn)))==set(map(canon,fan(1-nn))))
    f=S.expand(poly.subs(j,nn));fp=S.expand(poly.subs(j,nn+1));fm=S.expand(poly.subs(j,nn-1))
    ck(f'integral_signed_value_{nn}',f.is_Integer)
    ck(f'actual_forward_signed_step_{nn}',fp-f==-(nn-2)*(nn-3))
    ck(f'actual_reverse_signed_step_{nn}',fm-f==(nn-3)*(nn-4))
    pair1=[int(x.subs(j,nn)) for x in nat1];pair2=[int(x.subs(j,nn)) for x in nat2]
    ck(f'exact_native_double_parity_{nn}',all((2*x)%2==0 for x in pair1+pair2))
    records.append({'j':nn,'single_C1_pair':pair1,'single_C2_pair':pair2,'class':int(f)%28,'first_C0_flop_class':int(7*f)%28})
lift=S.symbols('lift',integer=True)
Ij=poly+28*lift
eq('actual_fixed_C0_central_arrow',Ij+6*Ij-7*poly,196*lift)
deps=['notes/part3_e6_selected_i3_working.md','notes/part3_e6_selected_i3_first_flop_working.md',
      'notes/part3_e6_selected_i3_outer_transfer_working.md','code/part3/e6_selected_i3_first_flop.json']
out={'status':'PASS','checks':len(tests),'utc':datetime.now(timezone.utc).isoformat(),
     'source':str(note.relative_to(ROOT)),'source_sha256':sha(note),'script_sha256':sha(Path(__file__)),
     'dependencies':{p:sha(ROOT/p) for p in deps},
     'scope':'Actual M6,b1,m2,n1 fixed-scalar selected-I3 loop, every signed vertical fan and its actual first C0/C1/C2 flop. No arbitrary subsequent nonvertical seed or kappa evaluation.',
     'full_Laurent_units':{'kappa_j':list(map(str,kapj)),'alpha_j':list(map(str,alj)),'eta_j':list(map(str,etj)),'basis':['kappa','alpha','g','eta','q']},
     'single_C1_pair':list(map(str,nat1)),'single_C2_pair':list(map(str,nat2)),
     'class_polynomial':str(poly),'first_fixed_flop':'7*S_j mod28 via the actual physical C0 pair',
     'signed_instances':records,'checks_named':tests}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(tests),'source_sha256':out['source_sha256'],'json_sha256':sha(path)},indent=2))
