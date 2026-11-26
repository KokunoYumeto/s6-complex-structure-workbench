#!/usr/bin/env python3
"""Universal root-degree, cup-matrix and Chern-root identities for inv:E2.2.

Every formula is symbolic in m. No sampled m is used as a proof.
The geometry and exact sequences are proved separately in the derivation.
"""
import json
import sympy as s

m=s.Symbol('m',integer=True,positive=True)
def coarse(alpha,beta):
    assert alpha%12==0
    r3=beta%3; r4=(3*beta)%4
    return s.Integer(alpha//12)*m+s.Rational(beta-4*r3-3*r4,12)

weights={'O':(0,0),'L':(0,-5),'Ldual':(0,5),'A':(24,-1),
 '2A':(48,-2),'LA':(24,-6),'LdualA':(24,4),'Adual':(-24,1),
 'canonical':(-24,-6),'basecanonical':(0,-7)}
degrees={k:coarse(*v) for k,v in weights.items()}
expected={'O':0,'L':-1,'Ldual':-1,'A':2*m-1,'2A':4*m-1,
 'LA':2*m-1,'LdualA':2*m,'Adual':-2*m-1,
 'canonical':-2*m-1,'basecanonical':-2}
for k,v in expected.items(): assert s.expand(degrees[k]-v)==0,k

# On each listed positive line, H0 is degree+1 and H1 is zero.
# The sign claims hold for every m>=1 by nonnegative coefficients in m-1.
for k in ('O','A','2A','LA','LdualA'):
    p=s.Poly(s.expand(degrees[k].subs(m,m+1)),m)
    assert all(x>=0 for x in p.all_coeffs()),k
h0E=1+(degrees['A']+1)
h0EG=h0E+(degrees['A']+1)+(degrees['2A']+1)
domain_deg=degrees['L']+degrees['LA']
target_deg=degrees['A']+degrees['2A']
qlength=s.expand(target_deg-domain_deg)
omega_length=s.expand((degrees['Ldual']+degrees['LdualA'])-degrees['Adual'])
assert qlength==omega_length==4*m
H=[s.expand(h0E),s.expand(h0EG),s.expand(degrees['LA']+2+qlength),s.Integer(0)]
assert H==[2*m+1,8*m+1,6*m+1,0]

# Cup product by a general logarithmic Kodaira--Spencer tensor.
a,b,c,d=s.symbols('a b c d')
tensor=s.Matrix([[a,b],[c,d]])
tangent_delta1=s.Matrix([[-b,a],[-d,c]])
cotangent_delta0=tensor.T
assert s.expand(tangent_delta1.det()-tensor.det())==0
assert s.expand(cotangent_delta0.det()-tensor.det())==0

# Independent HRR calculation by multiplication in the Chern-root ring.
x,y,z,t=s.symbols('x y z t')
roots=[x,y,z]
td=s.prod(1+r*t/2+r*r*t*t/12 for r in roots)
ch=sum(1-r*t+r*r*t*t/2-r*r*r*t*t*t/6 for r in roots)
top=s.expand(td*ch).coeff(t,3)
c1=x+y+z; c2=x*y+x*z+y*z; c3=x*y*z
assert s.expand(top-(c1*c2/s.Integer(24)-c3/2))==0

out={'method':'symbolic root residues, exact cup matrices, independent Chern-root multiplication',
 'domain':'all constructed positive combs, m>=12; arithmetic identities already hold for every integer m>=1',
 'coarse_degrees':{k:str(v) for k,v in degrees.items()},
 'tangent_delta1_matrix':str(tangent_delta1),'cotangent_delta0_matrix':str(cotangent_delta0),
 'common_determinant':str(s.expand(tensor.det())),
 'torsion_lengths':{'Q_m':str(qlength),'cotangent_cokernel':str(omega_length)},
 'tangent_dimensions':[str(v) for v in H],
 'chi_Omega1':'c1*c2/24-c3/2; on S6 this is -1',
 'hodge_relation':'h11-h12=1 after the separately proved h10=h13=0',
 'all_assertions_passed':True,'finite_parameter_sweep_used':False}
print(json.dumps(out,indent=2))
