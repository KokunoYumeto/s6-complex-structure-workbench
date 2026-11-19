"""Exact E6 order-three Miller, central Cartier and two-chart flop identities.
No compact attachment or characteristic return is certified here.
"""
from pathlib import Path
import json
import sympy as S
checks=[]
def ck(name,e):
    r=S.factor(e)
    assert r==0,(name,r)
    checks.append(name)
s,t,x,y=S.symbols('s t x y')
r=S.Rational(1,4)-s
Delta=8*t*t+6*s*t+s*s-s**3
N=48*t**3+48*s*t*t+2*s*s*(7-4*s)*t+s**3*(1-3*s)
x3=2*t*(2*t+s)/s**2
y3=t*Delta/s**3
lam=(3*x3*x3+2*r*x3+t)/(2*y3)
ck('actual_tangent_slope',lam-N/(2*s*Delta))
ck('Delta_discriminant',S.discriminant(Delta,t)-4*s*s*(1+8*s))
ck('Delta_N_resultant',S.resultant(Delta,N,t)+256*s**9)
x6=lam*lam-r-2*x3
f23=(y-y3-lam*(x-x3))/(x-x6)
f23full=2*s*Delta*(2*s*Delta*(y-y3)-N*(x-x3))/(4*s*s*Delta*Delta*(x+r+2*x3)-N*N)
ck('full_tangent_factor',f23-f23full)
# Central Cartier divisors: order C0,C1,C2 and horizontal D1.
C=S.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
D=S.Matrix([3,2,4]); U=S.Matrix([0,2,1]); F=S.ones(3,1)
ck('central_vertical_coefficients',sum((3*F-2*U+S.Matrix([0,3,3])-D)[i]**2 for i in range(3)))
ck('central_square',(D.T*C*D)[0]+6)
for i,expected in enumerate([0,3,-3]):ck('central_component_degree_'+str(i),(C*D)[i]-expected)
ck('Hom_vertical_pole',sum((-F+S.Matrix([4,3,2])-D-S.Matrix([0,0,-3]))[i]**2 for i in range(3)))
# Source U chart and literal O(-1)^2 normals.
z,w,x=S.symbols('z w x')
ss=x-z*w;tt=x*(w-z-1)/2
a,ww,xx=S.symbols('a ww xx')
ck('source_other_chart_parameter',(a*xx-ww).subs({a:1/z,ww:z*w,xx:z*x})-ss)
ck('source_other_chart_U',xx.subs(xx,z*x)-z*x)
# Full finite flop/translation.
h,al,be=S.symbols('h al be')
s0=h*al-be
zN=-al;wN=h-al+1;xN=al*al-al-be
t0=h*xN/2
ck('finite_target_source_equation',xN-s0-zN*wN)
ck('finite_target_t',xN*(wN-zN-1)/2-t0)
ck('finite_target_translation_z',zN.subs({h:x/w,al:w,be:z*w})+w)
ck('finite_target_translation_w',wN.subs({h:x/w,al:w,be:z*w})-(ss/w+z-w+1))
ck('finite_target_translation_x',xN.subs({h:x/w,al:w,be:z*w})-2*tt*w/x)
ck('finite_target_preserves_s',s0.subs({h:x/w,al:w,be:z*w})-ss)
ck('finite_target_preserves_t',t0.subs({h:x/w,al:w,be:z*w})-tt)
ck('finite_inverse_alpha',(-zN)-al)
ck('finite_inverse_h',wN-zN-1-h)
ck('finite_inverse_beta',(wN-zN-1)*(-zN)-s0-be)
# Full target h=infinity chart and inverse.
k,A,B=S.symbols('k A B'); DD=1+k-k*k*A
aa=k/DD;bb=DD*(-B-A+k*A*A);cc=-DD*A
EE=S.factor(1-aa-aa*aa*cc)
ck('target_endpoint_units',DD*EE-1)
ck('target_endpoint_source_parameter',aa*bb-cc-(A-k*B))
ck('target_endpoint_base',bb*(1-aa-aa*aa*cc)/2-(-B-A+k*A*A)/2)
ck('target_endpoint_normal_transition_x',aa*bb-(k*k*A*A-k*A-k*B))
ck('target_endpoint_normal_transition_z',aa*cc+k*A)
ck('target_endpoint_inverse_k',aa/EE-k)
ck('target_endpoint_inverse_A',-cc*EE-A)
ck('target_endpoint_inverse_B',(cc+aa*cc*cc-bb)*EE-B)
a,b,c=S.symbols('a b c')
E=1-a-a*a*c
ki=a/E;Ai=-c*E;Bi=(c+a*c*c-b)*E;Di=S.factor(1+ki-ki*ki*Ai)
ck('inverse_then_forward_a',ki/Di-a)
ck('inverse_then_forward_b',Di*(-Bi-Ai+ki*Ai*Ai)-b)
ck('inverse_then_forward_c',-Di*Ai-c)
# Full line coefficients, independent of the point/tensor r6 values.
rp,rt,dd,lam0,q,v=S.symbols('rp rt dd lam0 q v',nonzero=True)
f2=x/w;xn=2*tt*w/x
xi=s*dd*rp*x**3*v
vnext=lam0*q/tt**3*f2**6*rp/rt*v
xinext=s*dd*rt*xn**3*vnext
ck('full_Delta_point_tensor_line_arrow',xinext-8*lam0*q*w**(-3)*xi)
ck('target_endpoint_Cartier_ratio',(a**(-6)*b**(-3))/(a*b)**(-3)-a**(-3))
ck('source_Cartier_normal_transition',(z*x)**(-3)/x**(-3)-z**(-3))
# Associated node has reciprocal scalar and unchanged original q.
xi,xd=S.symbols('xi xd')
mult=8*lam0*q*w**(-3)
ck('associated_node_reciprocal_line',mult*xi*(xd/mult)-xi*xd)
out={'status':'PASS','count':len(checks),'checks':checks,
     'scope':'Exact Miller scalar/Cartier divisor and both actual translation-flop endpoint charts with full line coefficient; no compact attachment, oriented free pair or return assigned.',
     'central_divisor':[3,2,4],'central_square':-6,
     'source_component_degree':-3,
     'full_line_map':'xi_target=8*lambda*q*w^(-3)*xi_source',
     'Delta_resultant':'-256*s^9'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
