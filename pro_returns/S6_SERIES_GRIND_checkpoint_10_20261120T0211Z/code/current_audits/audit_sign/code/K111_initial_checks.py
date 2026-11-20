import sympy as s,json
from pathlib import Path
x,t,z=s.symbols('x t z'); r=s.Rational(1,4)-z
f=x**3+r*x**2+t*x+t**2
Disc=s.factor(s.discriminant(f,x)); Q=s.factor(Disc/t**2)
a,b,c,d=s.symbols('a b c d')
Tc=a*z+b*z*z+c*z**3+d*z**4
R=s.Poly(s.expand(Q.subs(t,Tc)),z)
sol={}
for j,v in enumerate([a,b,c,d],1):sol[v]=s.solve(R.coeff_monomial(z**j).subs(sol),v)[0]
weights=[1,2,2,1]; divisor={}
for j,w in enumerate(weights):
 for k,c in [(j+1,2),(j+2,-1),(j,-1)]:divisor[k]=divisor.get(k,0)+w*c
divisor={k:v for k,v in sorted(divisor.items()) if v}
P=s.Matrix([[1,-1],[-1,2]])
assert divisor=={0:-1,2:1,3:1,5:-1}
assert s.expand((t+x/2)**2-f+x**2*(x-z))==0
assert P.det()==1
out={'source_discriminant':str(Disc),'selected_root_series_through_s4':str(Tc.subs(sol)),'double_point':{'x':'s','y':'-t-s/2'},'tangent_numerator_restriction':str(s.factor((t+x/2)**2-f)),'Miller_divisor_in_jG':divisor,'source_vs_translated_point_divisor':'div B23 = D_M2 - (T_G^3)^*D_M2','native_point_matrix_determinant':str(P.det()),'native_point_matrix_inverse':str(P.inv()),'stated_pair_arithmetic':{'k':71,'ell':-4,'A_M':(4*71+4)//24,'theta_class':12%28,'mu':-4//4,'nu':71-(-4//4)},'scope':'Statements-only derivation. Does not verify the completed geometric characteristic pair or the original fixed-scalar endpoint identification.'}
p=Path(__file__).resolve().parents[1];(p/'K111_initial_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
