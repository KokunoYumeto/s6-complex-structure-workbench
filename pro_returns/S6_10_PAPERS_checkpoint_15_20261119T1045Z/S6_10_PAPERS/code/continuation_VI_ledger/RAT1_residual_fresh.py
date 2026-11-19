#!/usr/bin/env python3
"""Fresh symbolic certificates for the RAT.1 residual review.

Written without opening the receiving proof or VI's local program/output.
Every polynomial reduction is returned as an exact identity certificate.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s

x,y,z,t,u,v,w=s.symbols('x y z t u v w')
checks=[]
def check(name, expression):
    value=s.cancel(s.expand(expression))
    assert value==0, (name,value)
    checks.append(name)

g=[y*y-x*z,y*z-x**3,z*z-x*x*y]
F=x**5+x*y**3+z**3-3*x*x*y*z
check('symbolic_defect_x',x*F-g[1]**2+g[0]*g[2])
check('symbolic_defect_y',y*F-x*g[0]**2-g[1]*g[2])
check('symbolic_defect_z',z*F-x*g[0]*g[1]-g[2]**2)
check('localized_third_generator',x*g[2]-y*g[1]+z*g[0])
relations=[F,g[0]**2,g[0]*g[1],g[1]**2]
relations=list(map(s.expand,relations))

def leading(poly):
    return max(s.Poly(s.expand(poly),y,z).terms(),
               key=lambda term:(2*term[0][0]+3*term[0][1],term[0][0],term[0][1]))

def divide(poly):
    pending=s.expand(poly)
    quotient=[s.Integer(0)]*4
    remainder=s.Integer(0)
    while pending!=0:
        m,c=leading(pending)
        for j,relation in enumerate(relations):
            n,d=leading(relation)
            if m[0]>=n[0] and m[1]>=n[1]:
                term=s.cancel(c/d)*y**(m[0]-n[0])*z**(m[1]-n[1])
                quotient[j]+=term
                pending=s.expand(pending-term*relation)
                break
        else:
            term=c*y**m[0]*z**m[1]
            remainder+=term
            pending=s.expand(pending-term)
    return list(map(s.expand,quotient)),s.expand(remainder)

pair_certificates=[]
for i,j in itertools.combinations(range(4),2):
    mi,ci=leading(relations[i]);mj,cj=leading(relations[j])
    common=tuple(max(a,b) for a,b in zip(mi,mj))
    left=y**(common[0]-mi[0])*z**(common[1]-mi[1])/ci
    right=y**(common[0]-mj[0])*z**(common[1]-mj[1])/cj
    pair=s.expand(left*relations[i]-right*relations[j])
    quot,rem=divide(pair)
    check(f'S_pair_{i+1}_{j+1}_zero_remainder',rem)
    check(f'S_pair_{i+1}_{j+1}_identity',pair-sum(a*b for a,b in zip(quot,relations)))
    pair_certificates.append({'pair':[i+1,j+1],'left_multiplier':str(left),
       'right_multiplier':str(right),'quotients':[str(q) for q in quot],'remainder':str(rem)})
for i,j in itertools.combinations_with_replacement(range(3),2):
    quot,rem=divide(g[i]*g[j])
    check(f'product_{i+1}_{j+1}_in_J',rem)
    check(f'product_{i+1}_{j+1}_identity',g[i]*g[j]-sum(a*b for a,b in zip(quot,relations)))
standard=[]
leads=[leading(r)[0] for r in relations]
for iy in range(4):
    for iz in range(3):
        if not any(iy>=a and iz>=b for a,b in leads):standard.append((iy,iz))
assert len(standard)==9
checks.append('nine_standard_monomials')

f=y*y-x**3;Fp=z*f
check('cusp_line_defect_x',x*Fp-x*z*f)
check('cusp_line_defect_y',y*Fp-y*z*f)
check('cusp_line_defect_z',z*Fp-(y*z)**2+x*(x*z)**2)

def gradient(poly):return s.Matrix([s.diff(poly,c) for c in (x,y,z)])
def along(expr,sub):return expr.subs(sub,simultaneous=True)

sub={x:t**3,y:t**4,z:t**5}
a=along(gradient(g[0]),sub)
b=along(gradient(g[1]),sub)+t*a
c=along(gradient(g[2]),sub)
A=s.Matrix([0,0,-t**-3])
B=s.Matrix([0,1/(3*t**5),2/(3*t**4)])
for j in range(3):check(f'345_third_differential_{j}',c[j]+2*t*t*a[j]-t*b[j])
for name,value in [('aA',a.dot(A)-1),('bA',b.dot(A)),('aB',a.dot(B)),('bB',b.dot(B)-1)]:check('345_dual_'+name,value)
der=s.Matrix([3*t*t,4*t**3,5*t**4])
for j in range(3):check(f'345_wedge_{j}',a.cross(b)[j]-t**6*der[j])
q=s.expand(((u*A+v*B).T*along(s.hessian(F,(x,y,z)),sub)*(u*A+v*B))[0]/2)
check('345_quadratic',q-(3*u*u/t-3*u*v/t**2+v*v/t**3))
check('345_quadratic_determinant',s.det(s.Matrix([[3/t,-s.Rational(3,2)/t**2],[-s.Rational(3,2)/t**2,1/t**3]]))-s.Rational(3,4)/t**4)

subc={x:t*t,y:t**3,z:0};ac=along(gradient(f),subc);bc=along(gradient(x*z),subc)
Ac=s.Matrix([0,1/(2*t**3),0]);Bc=s.Matrix([0,0,t**-2])
for name,value in [('aA',ac.dot(Ac)-1),('bA',bc.dot(Ac)),('aB',ac.dot(Bc)),('bB',bc.dot(Bc)-1)]:check('cusp_dual_'+name,value)
for j in range(3):
    check(f'cusp_wedge_{j}',ac.cross(bc)[j]-t**4*s.Matrix([2*t,3*t*t,0])[j])
    check(f'cusp_third_differential_{j}',along(gradient(y*z),subc)[j]-t*bc[j])
qc=s.expand(((u*Ac+v*Bc).T*along(s.hessian(Fp,(x,y,z)),subc)*(u*Ac+v*Bc))[0]/2)
check('cusp_quadratic',qc-u*v/t**2)
check('cusp_quadratic_determinant',s.det(s.Matrix([[0,s.Rational(1,2)/t**2],[s.Rational(1,2)/t**2,0]]))+s.Rational(1,4)/t**4)
subl={x:0,y:0,z:t};al=along(gradient(x*z),subl);bl=along(gradient(y*z),subl)
Al=s.Matrix([1/t,0,0]);Bl=s.Matrix([0,1/t,0])
for name,value in [('aA',al.dot(Al)-1),('bA',bl.dot(Al)),('aB',al.dot(Bl)),('bB',bl.dot(Bl)-1)]:check('line_dual_'+name,value)
for j in range(3):check(f'line_wedge_{j}',al.cross(bl)[j]-t*t*s.Matrix([0,0,1])[j])

for name,k,exponent in [('cusp',3,2),('tacnode',4,2),('ramphoid',5,4)]:
    if k%2:
        xx,yy=t*t,t**k
        residue=s.diff(xx,t)/(2*yy)
        check(name+'_residue',residue-t**(-exponent))
    else:
        for sign in (1,-1):
            xx,yy=t,sign*t**2
            residue=s.diff(xx,t)/(2*yy)
            check(name+f'_residue_{sign}',residue-sign*s.Rational(1,2)*t**(-exponent))
check('node_first_residue',s.diff(t,t)/t-1/t)
check('node_second_residue',-s.diff(t,t)/t+1/t)

aa,bb,cc,xx,yy=s.symbols('aa bb cc xx yy')
poly=x**3+yy*aa*x*x+yy**2*bb*x+yy**2*cc
shifted=s.expand(poly.subs(x,xx-yy*aa/3))
target=xx**3+yy**2*((bb-aa*aa/3)*xx+cc-yy*aa*bb/3+2*yy*aa**3/27)
check('Hirzebruch_exact_Tschirnhaus',shifted-target)
degree_data=[]
for delta in (0,1,2):
    normal=-2+2*delta;conductor=2*delta;degree=-6*normal+4*conductor
    assert degree==12-4*delta
    smax=0 if delta==0 else 1+delta
    upper=smax+degree//5
    assert upper==(2 if delta==0 else 3)
    checks.extend([f'delta_{delta}_tensor_degree',f'delta_{delta}_attachment_bound'])
    degree_data.append({'delta':delta,'det_normal_degree':normal,'conductor_degree':conductor,
       'product_degree':degree,'singular_preimages_upper':smax,'attachment_upper':upper})

root=Path(__file__).resolve().parents[2]
out=root/'analysis/continuation_VI_ledger/RAT1_residual_fresh.output.json'
result={'all_passed':True,'checks':len(checks),'check_names':checks,
 'method':'Exact symbolic differentiation, custom monic weighted polynomial division with full identities, residue maps, and algebraic coordinate changes.',
 'standard_monomials':standard,'S_pair_certificates':pair_certificates,'quadratic_345':str(q),'quadratic_cusp_line':str(qc),
 'degree_data':degree_data,'scope':'The three clean RAT1 residual packets only; this program does not establish the topological proof or the full RAT1 row by finite testing.',
 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_passed':True,'checks':len(checks),'output':str(out),'program_sha256':result['program_sha256']},indent=2))
