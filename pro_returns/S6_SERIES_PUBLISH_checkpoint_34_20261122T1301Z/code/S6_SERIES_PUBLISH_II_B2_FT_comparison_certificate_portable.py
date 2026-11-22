"""Postrelease verification of every printed order-three number and cusp chain map."""
import io,runpy,contextlib,json
from pathlib import Path
from fractions import Fraction as F
with contextlib.redirect_stdout(io.StringIO()):
 d=runpy.run_path(str(Path(__file__).with_name('S6_SERIES_PUBLISH_II_B2_FT_prereading_certificate.py')))
P,add,neg,mul,mm,eye=[d[k] for k in ['P','add','neg','mul','mm','eye']]
Z={};U=P(1);t=P(0,1);t2=mul(t,t);tm1=P(-1,1)
scale=lambda a,c:{k:v*c for k,v in a.items() if v*c}
y2=scale(mul(mul(t2,t2),mul(tm1,tm1)),F(8))
g2=scale(mul(mul(t2,t),tm1),F(12))
x2=scale(t2,F(9,8));x3=P(F(512,81),F(-592,81),F(80,81))
num=add(scale(mul(g2,x2),F(1,2)),scale(y2,F(-2)))
lhs=add(mul(num,num),scale(mul(y2,mul(mul(x2,x2),x2)),F(-4)))
rhs=scale(mul(y2,mul(mul(x2,x2),x3)),F(4))
assert lhs==rhs
# x=-2*x0,y=2*i*sqrt2*y0 transforms AC's equation by multiplying it by-8.
assert [4*(-2)**3,-12*(-2),8]==[-8*4,-8*(-3),-8*(-1)]
nu2sq=1/(9*x3[0]);assert nu2sq==F(9,512)
tau1i=F(1,2)
det=F(144)*(-tau1i*tau1i)/(6*(-8));assert det==F(3,4)
b3i=(det-24*nu2sq)/(3*tau1i);assert b3i==F(7,32)
transverse=3*(b3i+12*nu2sq/tau1i);assert transverse==F(123,64)
# Standard-square complex S -> triangular complex T, and a deformation retract.
T0=[[t],[Z],[t]];T1=[[U,add(U,t),neg(U)],[neg(U),neg(U),U]]
S0=[[t],[Z]];S1=[[Z,t]]
F0=G0=eye(1);F1=[[U,Z],[Z,U],[U,U]];G1=[[U,Z,Z],[Z,U,Z]]
F2=[[U],[Z]];G2=[[U,U]]
assert mm(F1,S0)==T0 and mm(T1,F1)==mm(F2,S1)
assert mm(G1,T0)==S0 and mm(G2,T1)==mm(S1,G1)
assert mm(G1,F1)==eye(2) and mm(G2,F2)==eye(1)
h2=[[Z,Z],[Z,Z],[Z,U]]
I3=eye(3);FG1=mm(F1,G1)
I2=eye(2);FG2=mm(F2,G2)
assert mm(h2,T1)==[[add(I3[i][j],neg(FG1[i][j])) for j in range(3)] for i in range(3)]
assert mm(T1,h2)==[[add(I2[i][j],neg(FG2[i][j])) for j in range(2)] for i in range(2)]
print(json.dumps({'method':'Cross-multiplied exact chord-and-tangent tripling; rational leading-coefficient transport; explicit chain maps and homotopy. No CAS or Smith forms.','AC_curve_map':{'x':'-2*x0','y':'2*i*sqrt(2)*y0','inverse_x0':'-x/2','inverse_y0':'y/(2*i*sqrt(2))'},'x2P':'9*t^2/8','x3P_coefficients':[str(x3[i]) for i in range(3)],'nu2_squared_over_F_squared':str(nu2sq),'tau1_over_i_pi_F_squared':str(tau1i),'determinant_s2_over_F_squared':str(det),'b3_over_i_div_pi':str(b3i),'C14_over_i_k_div_pi':str(transverse),'sign_binding':'g3(rho)=-8/F^6, W^2=8/F^6','cusp_chain_inclusion_projection_and_homotopy':True,'assertions_passed':True},indent=2)+'\n')
