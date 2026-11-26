#!/usr/bin/env python3
"""Fresh LB enumeration and actual-fan equivariant line computation.

Reads the authorized raw A_i,g_i/component fixture only.  In particular,
no target catalogue, target program, released target proof, or held root
calculation is read or imported.  All integer maps used below are retained.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product, combinations
from math import gcd, lcm
from functools import reduce
from collections import Counter
import hashlib
import json
import csv
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_conic'
RAW=ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
raw=json.loads(RAW.read_text())
assert hashlib.sha256(RAW.read_bytes()).hexdigest()=='6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
J=s.Matrix([[0,1],[-1,0]])
I2=s.eye(2); I4=s.eye(4)
delta=s.Matrix([0,0,1,0]); gamma=s.Matrix([0,0,0,1])

def egcd(a,b):
    oldr,r,oldx,x,oldy,y=a,b,1,0,0,1
    while r:
        q=oldr//r
        oldr,r=r,oldr-q*r; oldx,x=x,oldx-q*x; oldy,y=y,oldy-q*y
    if oldr<0:oldr,oldx,oldy=-oldr,-oldx,-oldy
    assert oldx*a+oldy*b==oldr
    return oldr,oldx,oldy

def integers(v):
    assert all(x.q==1 for x in v)
    return [int(x) for x in v]

def arr(M):return [[int(x) if x.q==1 else str(x) for x in row] for row in M.tolist()]

def quadratic(v):return int(v[0]*v[1]+v[0]+v[1])%2

def multiplicative(name):return name.startswith('I') and name[1:].isdigit()

def local_transvection(A,g):
    nu=reduce(gcd,(abs(int(x)) for x in A-I2),0)
    assert nu>0
    col=next((A-I2)[:,j] for j in range(2) if (A-I2)[:,j]!=s.zeros(2,1))
    content=reduce(gcd,(abs(int(x)) for x in col),0)
    u=col/content
    if next(x for x in u if x)!=abs(next(x for x in u if x)):u=-u
    assert A-I2==nu*u*(u.T*J)
    ix=next(j for j in range(2) if u[j])
    kappa=g[ix]/u[ix]
    assert kappa.q==1 and g==kappa*u
    gg,x,y=egcd(int(u[0]),int(u[1]));assert gg==1
    r=s.Matrix([-y,x]);assert s.det(s.Matrix.hstack(u,r))==1
    return nu,u,r,int(kappa)

def narrow(row,i,k):
    component=row['component_coordinates'][i]
    return all((k*coord[0])%mod==0 for coord,mod in zip(component['rows'],component['moduli']))

def selected_equation(nu,kappa,a,b):
    left=[0]*nu
    for index,coefficient in [(a*kappa,1),(0,-1),((a-b)*kappa,-1),(-b*kappa,1)]:left[index%nu]+=coefficient
    right=[0]*nu
    for index,coefficient in [(0,-2),(1,1),(-1,1)]:right[index%nu]+=coefficient
    return left==right

natural=[]
profile_counts=[]
for row in raw['rows']:
    height=Fraction(row['height_of_generator']);assert height.numerator==1
    d=height.denominator
    As=[s.Matrix(x) for x in row['elliptic_matrices']]
    gs=[s.Matrix(x) for x in row['generator_section_cocycle']]
    local=[local_transvection(A,g) if multiplicative(kind) else None for A,g,kind in zip(As,gs,row['fibers'])]
    count=0
    for zero,datum in enumerate(local):
        if datum is None:continue
        nu,u,r,kappa=datum
        if d%nu:continue
        total=d//nu
        for a in range(1,total+1):
            if total%a:continue
            b=total//a
            if gcd(a,b)!=1 or gcd(b*kappa,nu)!=1:continue
            if not selected_equation(nu,kappa,a,b):continue
            if any(not(narrow(row,i,a) or narrow(row,i,b)) for i in range(len(As)) if i!=zero):continue
            natural.append(dict(row=row,As=As,gs=gs,local=local,zero=zero,a=a,b=b))
            count+=1
    profile_counts.append([row['OS'],row['profile'],count])
assert len(natural)==172

finite_orders={'II':6,'III':4,'IV':3,'III*':4,'IV*':3}
component_orders={'II':1,'III':2,'IV':3,'III*':2,'IV*':3}
patterns=[]
for item in natural:
    row=item['row'];a=item['a'];b=item['b'];options=[]
    if any('*' in kind and kind.startswith('I') and kind[1:-1].isdigit() for kind in row['fibers']):continue
    for i,kind in enumerate(row['fibers']):
        if multiplicative(kind):continue
        opt=[]
        if kind in ['II','III','IV'] and narrow(row,i,a) and gcd(b,component_orders[kind])==1:opt.append(('O',i,1,1))
        z=(item['As'][i]-I2).inv()*item['gs'][i]
        if all((b*x).q==1 for x in z):opt.append(('F',i,component_orders[kind],finite_orders[kind]))
        options.append(opt)
    for choices in product(*options):
        finite=[x for x in choices if x[0]=='F']
        if any(gcd(x[3],y[3])!=1 for x,y in combinations(finite,2)):continue
        qf=reduce(lambda x,y:x*y,(x[2] for x in finite),1)
        if b!=2*qf:continue
        assert len(finite)<=1
        patterns.append((item,choices))
assert len(patterns)==15
assert len({(p['row']['OS'],p['row']['profile'],p['a'],p['b'],p['zero']) for p,c in patterns})==13

def primitive_right_inverse(M):
    n=M.rows
    total=0; coeffs=[]
    for ix in combinations(range(M.cols),n):
        B=M[:,list(ix)];det=int(B.det())
        if det==0:continue
        g,x,y=egcd(total,det)
        coeffs=[(oldix,oldB,oldc*x) for oldix,oldB,oldc in coeffs]
        coeffs.append((ix,B,y));total=g
        if total==1:break
    assert total==1
    out=s.zeros(M.cols,n)
    for ix,B,c in coeffs:
        for j,col in enumerate(ix):out[col,:]+=c*B.adjugate()[j,:]
    assert M*out==s.eye(n)
    return out

def omega_matrix(a,b):
    O=s.zeros(4);O[:2,:2]=a*J;O[2,3]=-b;O[3,2]=b
    return O

def lifted_matrix(item,i):
    A=item['As'][i];g=item['gs'][i];a=item['a'];b=item['b']
    if item['local'][i] is None:z=(A-I2).inv()*g
    else:
        nu,u,r,kappa=item['local'][i];z=s.Rational(kappa,nu)*r
    w=s.Rational(1,item['local'][i][0]) if i==item['zero'] else 0
    beta=-a*g.T*J*A
    T=s.eye(4);T[:2,:2]=A;T[:2,3]=b*g;T[2,:2]=beta;T[2,3]=(beta*(b*z))[0]+w
    integers(T)
    return T

data=[]
for number,(item,choices) in enumerate(patterns,1):
    row=item['row'];a=item['a'];b=item['b'];zero=item['zero']
    O=omega_matrix(a,b);Ts=[lifted_matrix(item,i) for i in range(len(row['fibers']))]
    prodT=I4
    for T in Ts:
        prodT=prodT*T
        assert T.T*O*T==O and T*delta==delta
        for v in product([0,1],repeat=4):assert quadratic(T*s.Matrix(v))==quadratic(v)
    assert prodT==I4
    for x in product([0,1],repeat=4):
        for y in product([0,1],repeat=4):
            X=s.Matrix(x);Y=s.Matrix(y)
            assert (quadratic(X+Y)-quadratic(X)-quadratic(Y)-int((X.T*O*Y)[0]))%2==0
    nu,u,r,kappa=item['local'][zero]
    short=s.Matrix.hstack(s.Matrix([*u,0,0]),delta)
    long=s.Matrix.hstack(s.Matrix([*r,0,0]),gamma)
    C=s.Matrix([[nu,b*kappa],[-a*kappa,s.Rational(1-a*b*kappa*kappa,nu)]])
    assert C.det()==1
    H=s.Matrix.hstack(short*C[:,0],long[:,0],short*C[:,1],long[:,1])
    assert H.det() in [-1,1] and H.inv()*Ts[zero]*H==I4+s.eye(4)[:,0]*s.eye(4)[1,:]+s.eye(4)[:,2]*s.eye(4)[3,:]
    K=(short*C).T*O*long;assert K==K.T
    dvec=C.inv()*s.Matrix([0,1]);assert K*dvec==s.Matrix([0,-b])
    epsilon=s.Matrix([quadratic((short*C)[:,j]) for j in range(2)])
    assert all((K[j,j]-epsilon[j])%2==0 for j in range(2))
    assert integers(dvec)==[-b*kappa,nu] and dvec[0]%2==0 and dvec[1]%2==1
    slopes=s.Matrix([(K[j,j]-epsilon[j])/2 for j in range(2)])
    phase=(epsilon.T*dvec)[0]/2;assert phase.q==1
    character=(slopes.T*dvec)[0]+phase
    assert character.q==1 and character==(K[0,0]*dvec[0]+K[1,1]*dvec[1])/2
    degreeC=K[0,0]-K[0,1]
    assert degreeC%2==1
    # Literal toric ray interpolation, including forward fibre characters.
    vertices=[s.Matrix([0,0]),s.Matrix([1,0]),s.Matrix([0,1])]
    phi=lambda v:((v.T*K*v-epsilon.T*v)[0]/2)
    for v in vertices:assert phi(v)==(slopes.T*v)[0]
    assert phi(s.Matrix([1,0]))+phi(s.Matrix([-1,1]))-phi(s.Matrix([0,1]))==degreeC
    other_slopes=s.Matrix([phi(s.Matrix([0,1]))-phi(s.Matrix([-1,1])),phi(s.Matrix([0,1]))])
    other_character=(other_slopes.T*dvec)[0]+phase
    assert (other_character-character)%2==0
    fixed=[];kill=[short[:,0],delta]
    for i,datum in enumerate(item['local']):
        if datum is None or i==zero:continue
        ni,ui,ri,ki=datum;di=gcd(ni,a*ki)
        ell=s.Matrix([ni*ui[0]/di,ni*ui[1]/di,-a*ki/di,0])
        ell=ell.applyfunc(s.Rational);integers(ell)
        f=s.Matrix([[di*(ui.T*J)[0],di*(ui.T*J)[1],0,s.Rational(b*ki*di,ni)]])
        integers(f);assert Ts[i]-I4==ell*f
        assert reduce(gcd,(abs(int(x)) for x in f),0)==1
        kill.append(ell)
        Nis=s.Rational(a*ni,di*di)
        assert Nis.q==1 and ell.T*O==Nis*f
        is_fixed=all((delta[j]-ell[j])%2==0 for j in range(4))
        if is_fixed:
            assert ni==2 and di==1 and abs(ki)==1
            correction=(delta-ell)/2;integers(correction)
            assert Nis%2==0 and quadratic(ell)==0
            deg=s.Rational(-a*b,Nis);assert deg.q==1 and deg%2==1
            weight=(int(Nis)//2+quadratic(correction))%2
            assert weight==0
            sr=s.Matrix.hstack(s.Matrix([*ui,0,0]),delta)
            lr=s.Matrix.hstack(s.Matrix([*ri,0,0]),gamma)
            Snode=s.Matrix([[2,1],[-a*ki,s.Rational(1-a*ki,2)]])
            Lnode=s.Matrix([[1,-s.Rational(b*ki,2)],[0,1]])
            assert Snode.det()==Lnode.det()==1
            SN=sr*Snode;LN=lr*Lnode
            Hnode=s.Matrix.hstack(SN[:,0],LN[:,0],SN[:,1],LN[:,1])
            Kn=SN.T*O*LN
            assert Kn==s.Matrix([[2*a,0],[a,-s.Rational(b,2)]])
            assert Hnode.inv()*Ts[i]*Hnode==I4+s.eye(4)[:,0]*s.eye(4)[1,:]
            assert Snode.inv()*s.Matrix([0,1])==s.Matrix([-1,2])
            fixed.append(dict(position=i,type=row['fibers'][i],vanishing=integers(ell),row=integers(f),
                              nodal_polarization=int(Nis),phase_correction=integers(correction),
                              phase_sign=quadratic(correction),degree=int(deg),weight=weight,
                              nodal_H=arr(Hnode),nodal_H_inverse=arr(Hnode.inv()),nodal_K=arr(Kn)))
    assert len(fixed)==1
    killM=s.Matrix.hstack(*kill)[:3,:]
    right=primitive_right_inverse(killM)
    cube=(int(degreeC)*int(character)+sum(x['degree']*x['weight'] for x in fixed))%2
    assert cube==(kappa+1)%2
    rec=dict(number=number,OS=row['OS'],profile=row['profile'],a=a,b=b,zero=zero,
             choices=[dict(kind=k,position=i,q=q,order=d) for k,i,q,d in choices],
             forward_matrices=[arr(T) for T in Ts],
             nu=nu,u=integers(u),r=integers(r),kappa=kappa,C=arr(C),C_inverse=arr(C.inv()),
             H=arr(H),H_inverse=arr(H.inv()),K=arr(K),delta_jordan=integers(dvec),
             epsilon=integers(epsilon),slopes=integers(slopes),dense_half_character=int(phase),
             cusp_character=int(character),other_chart_character=int(other_character),
             cusp_degree=int(degreeC),cusp_weight=int(character)%2,
             fixed_elliptic=fixed,cube=cube,kill_matrix=arr(killM),kill_right_inverse=arr(right))
    data.append(rec)

# Independent symbolic gauge checks, with the full two-variable unit matrix.
u1,u2,w1,w2,k11,k12,k22,ep1,ep2,o11,o12,o21,o22=s.symbols('u1 u2 w1 w2 k11 k12 k22 ep1 ep2 o11 o12 o21 o22')
U=s.Matrix([u1,u2]);W=s.Matrix([w1,w2]);K=s.Matrix([[k11,k12],[k12,k22]])
Om=s.Matrix([[o11,o12],[o21,o22]]);eps=s.Matrix([ep1,ep2]);Z=U+Om*W
F=-(U.T*K*W)[0]-(W.T*K*Om*W)[0]+(eps.T*Z)[0]
symmetry=k11*o12+k12*o22-k12*o11-k22*o21
for j in range(2):
    ej=s.eye(2)[:,j]
    phase_delta=s.expand(F.subs({u1:u1+ej[0],u2:u2+ej[1]},simultaneous=True)-F+(ej.T*K*W)[0]+eps[j])
    assert s.simplify(phase_delta-2*eps[j])==0
    log_delta=s.expand(F.subs({w1:w1+ej[0],w2:w2+ej[1]},simultaneous=True)-F-(ej.T*K*U)[0])
    target=-2*(ej.T*K*Z)[0]-(ej.T*K*Om*ej)[0]+(eps.T*Om*ej)[0]
    remainder=s.expand(log_delta-target)
    assert s.rem(remainder,symmetry,o12)==0
monodromy=s.expand(F.subs({o11:o11+1,o22:o22+1},simultaneous=True)-F.subs({u1:u1+w1,u2:u2+w2},simultaneous=True))
assert monodromy==0

# Rank-one gauges use K^t Omega; retain the nonzero lower off-diagonal.
NN,kk,DD=s.symbols('N k D')
KN=s.Matrix([[NN,0],[kk,DD]])
FN=-(U.T*KN*W)[0]-(W.T*KN.T*Om*W)[0]+(eps.T*Z)[0]
nodal_symmetry=NN*o12+kk*o22-DD*o21
for j in range(2):
    ej=s.eye(2)[:,j]
    pdelta=s.expand(FN.subs({u1:u1+ej[0],u2:u2+ej[1]},simultaneous=True)-FN+(ej.T*KN*W)[0]+eps[j])
    assert pdelta==2*eps[j]
    ldelta=s.expand(FN.subs({w1:w1+ej[0],w2:w2+ej[1]},simultaneous=True)-FN-(ej.T*KN.T*U)[0])
    expected=-2*(ej.T*KN.T*Z)[0]-(ej.T*KN.T*Om*ej)[0]+(eps.T*Om*ej)[0]
    assert s.rem(s.expand(ldelta-expected),nodal_symmetry,o12)==0
assert s.expand(FN.subs(o11,o11+1)-FN.subs(u1,u1+w1))==0

# The exact Cartier translation law, without discarding the unit matrix.
v1,v2,h1,h2=s.symbols('v1 v2 h1 h2')
V=s.Matrix([v1,v2]);HV=s.Matrix([h1,h2])
psi=lambda v:(v.T*K*v-eps.T*v)[0]/2
assert s.expand(psi(V+HV)-psi(V)-(HV.T*K*V)[0]-(HV.T*K*HV-eps.T*HV)[0]/2)==0

# Uniform ordinary/finite clutching elimination; sigma records either sign.
mm,ee,rr,aa,et,sigma=s.symbols('m e r alpha eta sigma',integer=True)
for q in [1,3]:
    bb=2*q;nn=mm*ee-sigma
    relation=s.expand(s.Rational(bb,q)*nn-(mm/q)*bb*ee)
    assert relation==-2*sigma
    D=-bb*ee
    tell=s.expand(aa*bb*rr-et*rr*D)
    assert s.expand(tell-bb*rr*(aa+et*ee))==0

def exterior_product(p,q):
    out={}
    for (u,v,t),c in p.items():
        for (uu,vv,tt),cc in q.items():
            if u+uu>1 or v+vv>1:continue
            key=(u+uu,v+vv,t+tt)
            out[key]=(out.get(key,0)+c*cc)%2
    return {k:v for k,v in out.items() if v}

localization_rows=[]
for B1,B2,Cc in product([0,1],repeat=3):
    A={(1,1,0):1,(1,0,1):B1,(0,1,1):B2,(0,0,2):Cc}
    cube_poly=exterior_product(exterior_product(A,A),A)
    coefficient=cube_poly.get((1,1,4),0)
    assert coefficient==Cc
    localization_rows.append([B1,B2,Cc,coefficient])

# Explicit mod-two fixed-curve algebra, including both common shifts.
for rec in data:
    for shift in [0,1]:
        localized=((rec['cusp_weight']+shift)*rec['cusp_degree']+
                   sum((x['weight']+shift)*x['degree'] for x in rec['fixed_elliptic']))%2
        assert localized==rec['cube']

out=dict(raw_sha256=hashlib.sha256(RAW.read_bytes()).hexdigest(),natural_count=len(natural),
         profile_natural_counts=profile_counts,pattern_count=len(data),marked_row_count=13,
         cube_counts=dict(Counter(x['cube'] for x in data)),
         localization_exterior_rows=localization_rows,patterns=data)
LANE.mkdir(exist_ok=True)
jsonpath=LANE/'S6_SERIES_PUBLISH_III_02LB_fresh_data.json'
jsonpath.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
tsvpath=LANE/'S6_SERIES_PUBLISH_III_02LB_fresh_patterns.tsv'
fields=['number','OS','profile','a','b','zero','choices','nu','kappa','cusp_degree','cusp_character','cube']
with tsvpath.open('w',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader()
    for rec in data:
        row={k:rec[k] for k in fields};row['choices']=';'.join(f"{x['position']}:{x['kind']}" for x in rec['choices']) or 'none';writer.writerow(row)
print('AUTHORIZED RAW FIXTURE',out['raw_sha256'])
print('NATURAL ROWS',len(natural))
for line in profile_counts:print('PROFILE',*line)
print('MINIMAL c=2 PATTERNS',len(data),'MARKED ROWS',13,'CUBE COUNTS',out['cube_counts'])
for rec in data:
    print('PATTERN',rec['number'],rec['OS'],rec['profile'],'a,b=',(rec['a'],rec['b']),'zero=',rec['zero'],'choices=',rec['choices'])
    for key in ['forward_matrices','nu','u','r','kappa','C','C_inverse','H','H_inverse','K','delta_jordan','epsilon','slopes','dense_half_character','cusp_character','other_chart_character','cusp_degree','cusp_weight','fixed_elliptic','kill_matrix','kill_right_inverse','cube']:
        print(' ',key,rec[key])
print('UNIFORM FINITE CLUTCHING: q=1,3; b=2q; n=me-sigma gives -2sigma*s; D=-be*s and t(ell)=br(alpha+eta*e)*s are even.')
for row in localization_rows:print('LOCALIZED ELLIPTIC ALGEBRA B1,B2,c,coefficient',*row)
print('PASS: every natural candidate and all 15 patterns; all raw forward matrices, quadratic refinements, actual Jordan fans, both literal chart characters, nodal bases and inverses, integral fibre-killing inverses, symbolic gauges with units, all-parameter clutching, full elliptic cohomology algebra and both Borel common shifts.')
print('No target original, historical target catalogue, historical target program, or held root calculation was read.')
