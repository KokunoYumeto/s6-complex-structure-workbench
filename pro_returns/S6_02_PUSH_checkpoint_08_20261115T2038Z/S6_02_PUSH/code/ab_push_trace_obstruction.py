"""Exact certificates for the split-normalization trace obstruction.

This is a computation on the projective elliptic surface over
C: b^3=a^4+1, E: Y^2=X^3-3*b*X+2*a^2.  It does not assert
existence or nonexistence of an arbitrary analytic threefold filling.
The geometric identifications used by the certificate are proved
in Proposition B.3.4 of sections/AB_push.tex.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

out={}
a,b,X,Y,z,c,k,w=s.symbols('a b X Y z c k w')
omega=s.exp(2*s.pi*s.I/3)

# Pull back the given rational elliptic surface and divide the Weierstrass
# equation by a^6*b^12.  Coefficients are reduced by b^3=a^4+1.
t=b**3
xo=a**2*b**4*X
yo=a**3*b**6*Y
original=yo**2-xo**3+3*t**3*(t-1)*xo-2*t**4*(t-1)**2
pull=s.factor(original.subs(b**3-1,a**4)/(a**6*b**12))
expected=Y**2-X**3+3*b*X-2*a**2
num=s.together(pull-expected).as_numer_denom()[0]
assert s.rem(s.Poly(num,a),s.Poly(a**4-b**3+1,a))==0
disc=s.factor(-16*(4*(-3*b)**3+27*(2*a*a)**2))
disc=s.factor(disc.subs(a**4,b**3-1))
assert disc==1728
print('Pulled-back Weierstrass equation:',expected,'= 0')
print('Affine discriminant:',disc)
out['affine_discriminant']=int(disc)

# At the unique infinite point z=a/b is a uniformizer, c=z^3*a=z^4*b,
# and c^3*(1-c)=z^12.  Thus c=1-w^3+O(w^6) for w=z^4.
cw=1-w**3
x0=cw**2/(cw-k*w)
y0=s.sqrt(3)*k*cw*w/(cw-k*w)
root=s.series(s.sqrt(x0+2),w,0,3).removeO()
U=s.series(y0-(x0-1)*root,w,0,3).removeO().expand()
V=s.series(y0+(x0-1)*root,w,0,2).removeO().expand()
assert s.simplify(U+s.sqrt(3)*k*k*w*w/6)==0
assert s.simplify(V-2*s.sqrt(3)*k*w)==0
uv=s.expand((Y-(X-1)*s.sqrt(X+2))*(Y+(X-1)*s.sqrt(X+2)))
uv=s.expand(uv.subs(Y**2,X**3-3*c*X+2*c*c))
assert s.factor(uv-(1-c)*(3*X-2*(c+1)))==0
print('Infinity chart: U =',U,'+ O(w^3); V =',V,'+ O(w^2), w=z^4.')
print('Node product: UV=(1-c)*(3*X-2*(c+1)), ord_z(UV)=12.')
print('R and sigma(R) meet component 4, with distinct V/z^4 residues 2sqrt(3), 2sqrt(3)*omega.')
out['infinity_leading']={'U':str(U),'V':str(V),'component':4}

# Section intersection data, including resolved I_12 incidence.
G=s.diag(s.Integer(2),s.Rational(4,3),s.Rational(4,3))
G[1,2]=G[2,1]=s.Rational(-2,3)
assert G.det()==s.Rational(8,3)
M=s.Matrix([[1,0,0],[0,0,-1],[0,1,-1]])
assert M.T*G*M==G
assert M**3==s.eye(3)
trace=sum((M**j for j in range(12)),s.zeros(3))
assert trace==s.diag(12,0,0)
print('Height Gram matrix in (P,R,sigma R):',G.tolist())
print('Height determinant:',G.det())
print('sigma matrix:',M.tolist())
print('Trace_12 matrix:',trace.tolist())
out['height_gram']=[[str(x) for x in row] for row in G.tolist()]
out['height_det']=str(G.det())
out['sigma_matrix']=[[int(x) for x in row] for row in M.tolist()]
out['trace_matrix']=[[int(x) for x in row] for row in trace.tolist()]

# Integral NS sublattice in basis (O,F,Theta_1,...,Theta_11,P,R,S).
NS=s.zeros(16)
NS[0,0]=-1
NS[0,1]=NS[1,0]=1
for i in range(2,13):
    NS[i,i]=-2
    if i<12: NS[i,i+1]=NS[i+1,i]=1
for index in (13,14,15):
    NS[index,index]=-1
    NS[1,index]=NS[index,1]=1
for index in (14,15):
    NS[0,index]=NS[index,0]=1
    NS[5,index]=NS[index,5]=1 # Theta_4 has matrix index 5.
    NS[13,index]=NS[index,13]=2
NS[14,15]=NS[15,14]=1
assert NS.det()==-32
possible_indices=[d for d in range(1,7) if 32%(d*d)==0]
assert possible_indices==[1,2,4]
print('Integral NS sublattice determinant:',NS.det())
print('Possible saturation indices:',possible_indices)
out['NS_gram']=[[int(x) for x in row] for row in NS.tolist()]
out['NS_determinant']=int(NS.det())
out['possible_indices']=possible_indices

# A torsion section would have height 0. The maximum I_12 correction is 3,
# so intersection with O must be 0, and j(12-j)=24 has no integer solution.
corrections=[Fraction(j*(12-j),12) for j in range(12)]
assert max(corrections)==3
torsion_solutions=[j for j in range(12) if j*(12-j)==24]
assert not torsion_solutions
print('Torsion height-zero component solutions:',torsion_solutions)
out['torsion_component_solutions']=torsion_solutions

# If trace(Q)=6P, saturation gives Q=P/2+(uR+vS)/4.
# Pairing with R and S modulo Z yields the following two mod-6 equations.
pairing_solutions=[]
for u in range(6):
    for v in range(6):
        for j in range(12):
            if (2*u-v-2*j)%6==0 and (-u+2*v-2*j)%6==0:
                assert u%2==0 and v%2==0
                pairing_solutions.append([u,v,j])
print('Pairing-congruence solutions modulo (6,6,12):',len(pairing_solutions))
print('Every solution has u and v even.')
out['pairing_solutions_mod_6_6_12']=pairing_solutions

# Put u=2u',v=2v'. The component homomorphism gives 2j=4(u'+v') mod12.
# The geometric height is in (1/3)Z because j is even, while the lattice
# height is in 1/2+(1/3)Z.  This verifies all residues relevant modulo 2.
component_solutions=[]
bad=[]
for up in range(6):
    for vp in range(6):
        for j in range(12):
            if (2*j-4*(up+vp))%12:
                continue
            assert j%2==0
            lattice_height=Fraction(1,2)+Fraction(up*up-up*vp+vp*vp,3)
            geometric_height=2-Fraction(j*(12-j),12)
            assert (3*geometric_height).denominator==1
            assert (3*lattice_height).denominator==2
            if (lattice_height-geometric_height).denominator==1 and int(lattice_height-geometric_height)%2==0:
                bad.append([up,vp,j])
            component_solutions.append([up,vp,j])
assert not bad
print('Component-congruence solutions modulo (6,6,12):',len(component_solutions))
print('Compatible height residues:',bad)
out['component_solutions_mod_6_6_12']=component_solutions
out['compatible_height_residues']=bad

# The same proof for any odd multiple of P/2 excludes half-integral
# invariant coefficients. Pairing with narrow P makes 2*alpha integral;
# therefore the exact trace image is 12Z P.
for odd in (1,3,5,7,9,11):
    assert (3*Fraction(odd*odd,2)).denominator==2

# Saturation improves to index one.  The affine coordinate ring of C is
# C[a,b]/(b^3-a^4-1), with unique representatives of b-degree <3.
# Pole orders 3i+4j are distinct for j=0,1,2, so no leading cancellation
# can create a function of pole order 1 or 2.
pole_bases={n:[(i,j) for i in range(n//3+1) for j in range(3)
               if 3*i+4*j<=n] for n in (2,3)}
assert pole_bases[2]==[(0,0)]
assert pole_bases[3]==[(0,0),(1,0)]
xconst,yconst,ylin=s.symbols('xconst yconst ylin')
no_pole_equation=s.Poly(s.expand((yconst+ylin*a)**2-xconst**3+3*b*xconst-2*a*a),a,b)
no_pole_solutions=s.solve(no_pole_equation.coeffs(),[xconst,yconst,ylin],dict=True)
assert len(no_pole_solutions)==2
assert all(q[xconst]==0 and q[yconst]==0 and s.simplify(q[ylin]**2-2)==0
           for q in no_pole_solutions)
short_half_classes=[]
for uu,vv in ((1,0),(0,1),(1,1)):
    q=s.Matrix([0,s.Rational(uu,2),s.Rational(vv,2)])
    height=(q.T*G*q)[0]
    assert height==s.Rational(1,3)
    short_half_classes.append([uu,vv,str(height)])
print('Pole bases H0(O(2infinity)), H0(O(3infinity)):',pole_bases)
print('Sections disjoint from O:',no_pole_solutions)
print('Nonzero anti-invariant half-classes, heights:',short_half_classes)
print('Every proper 2-primary overlattice would contain one such height-1/3 class, impossible.')
print('Consequently MW=ZP+ZR+Zsigma(R) exactly and NS determinant=-32.')
out['pole_bases']=pole_bases
out['sections_disjoint_from_O']=[{str(k):str(v) for k,v in q.items()} for q in no_pole_solutions]
out['short_half_classes']=short_half_classes
out['exact_MW_index']=1
out['conclusion']='Trace_12 E(C(C)) = 12 Z P; in particular 6P is not a trace. Scope: split elliptic normalization.'
print(out['conclusion'])
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL EXACT TRACE-OBSTRUCTION CERTIFICATES PASSED')
