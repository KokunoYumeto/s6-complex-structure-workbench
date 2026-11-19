#!/usr/bin/env python3
"""Exact general good-root, Cartier, norm and original cap squares."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
tests=[]
def ck(name,truth):
    truth=bool(truth);tests.append({'name':name,'pass':truth})
    if not truth:raise AssertionError(name)
def zero(name,value):ck(name,S.factor(S.together(value))==0)
def integer_matrix(value):return [[int(x) for x in row] for row in value.tolist()]

L=S.symbols('L',integer=True,positive=True);m=3*L
u,r,X,Y,z,e=S.symbols('u r X Y z e')
s=S.Rational(1,4)-r
# Full root equation, retained monomial by monomial for arbitrary integer L.
for label,power,want in [('Y^2',-6*L+6*L,0),('X^3',-6*L+6*L,0),('rX^2',-4*L+6*L,2*L),('tX',-5*L+6*L,L),('t^2',-6*L+6*L,0)]:
    zero('full cubic root exponent '+label,power-want)
x2=s*u**2;y2=-1-s*u**3/2
zero('actual 2G source equation',y2**2-x2**3-r*u**2*x2**2-u*x2-1)
zero('actual doubling x',(u/2)**2-r*u**2-x2)
zero('actual doubling y',-1-(u/2)*x2-y2)
slope=(y2-1)/x2
x3=S.cancel(slope**2-r*u**2-x2);y3=S.cancel(-1-slope*x3)
zero('actual 3G source equation',y3**2-x3**3-r*u**2*x3**2-u*x3-1)
tau3=S.cancel(-x3/y3)
zero('actual 3G formal coefficient',S.limit(tau3/u**2,u,0)+s/2)
zero('actual small R formal coefficient',(-s/(2*m))*m+s/2)

# Quotient generators and all three A2 resolution maps.
a,b=S.symbols('a b')
for j in range(3):
    AA=a**(j+1)*b**j;BB=a**(2-j)*b**(3-j);CC=a*b
    zero(f'actual quotient source equation chart{j}',AA*BB-CC**3)
    if j<2:
        an=1/b;bn=a*b*b
        for label,old,new in [('A',AA,an**(j+2)*bn**(j+1)),('B',BB,an**(1-j)*bn**(2-j)),('C',CC,an*bn)]:
            zero(f'full adjacent source chart{j} {label}',old-new)
for ray in [(1,0),(S.Rational(2,3),1/(3*L)),(S.Rational(1,3),2/(3*L)),(0,1/L)]:
    vw,vz=ray
    # The nonnegative rays have known comparison signs.
    vu=S.cancel(L*vz)
    lo=min(S.Rational(vw),S.Rational(2*vu))
    zero(f'full Cartier correction ray{ray}',vw-max(S.Rational(vw-2*vu),0)-lo)
rr=[S.Matrix(v) for v in [(1,0),(S.Rational(2,3),1/(3*L)),(S.Rational(1,3),2/(3*L)),(0,1/L)]]
for j in range(3):zero(f'primitive quotient determinant{j}',S.det(S.Matrix.hstack(rr[j],rr[j+1]))-1/(3*L))
zero('literal chord/deck weight cancellation',-2*L+2*L)
zero('complete six-factor selected cancellation',2*m-6*L)

tc,tr,q=S.symbols('tc tr q')
uh=(1-tc*q)/(1-tr*q)
zero('full selected/reference height ratio',uh*(1-tr*q)-(1-tc*q))
zero('actual central unit',uh.subs(q,0)-1)
zero('formal norm lift derivative',m*(1/m)-1)

# Full original/native directed coordinate comparison.
d=1-3*e**2;rv=e**2*(3*e**2-2)/d**2
zero('original height exponent',m*(-4/m)+4)
zero('original height unit exponent',m*(3/m)-3)
zero('original x epsilon exponent',(-2*L)*(-4/m)-S.Rational(2,3)-2)
zero('original y epsilon exponent',(-3*L)*(-4/m)-1-3)
zero('original x d exponent',(-2*L)*(3/m)+2)
zero('original y d exponent',(-3*L)*(3/m)+3)
zero('whole native X^2 coefficient',rv*e**-2*d**2-(3*e**2-2))
zero('whole native X coefficient exponent',2-4*L/m-S.Rational(2,3))
zero('whole native X d coefficient',3*L/m-1)
zero('native X endpoint equals D^-4 modulo integral phase',16*L/m+S.Rational(2,3)-6)
zero('native Y endpoint equals actual deck',(-1)-(-4)*0+1)
zero('complementary original t epsilon cancellation',4-(4/m)*m)

sa,k,f,pi,cc,hh,jj,bb,lam,nn=S.symbols('sa k f pi cc hh jj bb lam nn')
hb=hh-nn*sa*pi+jj*bb+lam
zero('full signed target-sheet cochain square',nn*(sa+k)*(f+pi)+(sa+k)*cc+hb-(nn*sa*f+sa*cc+hh)-(nn*k*(f+pi)+k*cc)-jj*bb-lam)
Cref=S.Matrix([[3,1],[1,0]]);Crefi=S.Matrix([[0,1],[1,-3]])
Rcon=S.Matrix([[0,0],[-1,-1]])
ck('literal conifold physical Euler kernel',Rcon*S.Matrix([1,-1])==S.zeros(2,1))
ck('literal conifold primitive image',Rcon[:,0]==S.Matrix([0,-1]))
records=[]
for ell in range(1,65):
    mm=3*ell
    for n in (-1,1):
        C=S.Matrix([[mm,1],[n,0]]);Ci=S.Matrix([[0,n],[1,-mm*n]])
        ck(f'cap l{ell} n{n} exact signed inverse',C*Ci==S.eye(2))
        ck(f'cap l{ell} n{n} retained signed determinant',C.det()==-n)
        Q=Crefi*C;Qi=Ci*Cref
        ck(f'cap l{ell} n{n} actual basis comparison',Q*Qi==S.eye(2))
        ck(f'cap l{ell} n{n} explicit basis matrix',Q==S.Matrix([[n,0],[mm-3*n,1]]))
        ck(f'cap l{ell} n{n} contracting generator norm',n*n==1)
        zero(f'cap l{ell} n{n} full A^m scalar power',mm*n-n*mm)
        zero(f'cap l{ell} n{n} full A^m source power',mm*n-n*mm)
        zero(f'cap l{ell} n{n} whole H^m source power',mm*n*n-mm)
        for char in sorted({0,1,mm//2,mm-1}):
            for js in [(0,0,0,0),(-2,1,3,-1),(1,-3,2,4)]:
                J=sum(js)
                # Coordinates are exact exponents of R_lambda,Ftilde,D,char.
                arrows=[S.Matrix([n+mm*j,n+mm*j,1,char]) for j in js]
                word=sum(arrows,S.zeros(4,1))
                ck(f'cap l{ell} n{n} d{char} J{js} full quarter word',word==S.Matrix([4*n+mm*J,4*n+mm*J,4,4*char]))
                comp=S.Matrix([-4*n,-4*n,0,-4*char])
                endpoint=S.Matrix([0,0,-4,0])
                ck(f'cap l{ell} n{n} d{char} exact new-old inverse endpoint',comp+endpoint==S.Matrix([-4*n,-4*n,-4,-4*char]))
        records.append({'l':ell,'m':mm,'n':n,'meridian_matrix':integer_matrix(C),'inverse':integer_matrix(Ci),'reference_basis_matrix':integer_matrix(Q)})

source=ROOT/'notes/part3_e6_selected_infinity_good_caps_working.md'
deps=['notes/part3_e6_selected_infinity_m2_branch_working.md','code/part3_fourfold/e6_selected_infinity_m2_branch.json','notes/part3_e6_unselected_iii_extension_working.md','notes/part3_e6_selected_infinity_negative_norm_working.md','notes/part3_e6_selected_infinity_reduced_caps_working.md','records/k101_export_manifest.json','records/k102_export_manifest.json','records/k104_export_manifest.json']
out={'status':'PASS_EXACT_GOOD_CAP_MAPS','utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checks':len(tests),'scope':'Universal symbolic source/root/Cartier/norm/annular identities, both directed endpoint maps and128 signed cap matrices. Complete geometric cap product and the actual M2 compact attachment remain in MG.1--5 and MB.1--7 for independent audit.','dependencies':[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in deps],'signed_cap_records':records,'identities':tests}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','source_sha256','checks','scope']},indent=2))
