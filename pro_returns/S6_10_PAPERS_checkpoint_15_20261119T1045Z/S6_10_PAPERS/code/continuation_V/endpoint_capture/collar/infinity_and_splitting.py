#!/usr/bin/env python3
"""Independent root-series evaluation and exact-path splitting constant.
Reuses only the newly authored period_balls tools, not any prior-run program.
"""
from pathlib import Path
import json,sys
import sympy as S
import period_balls as pb
from flint import acb,arb,acb_mat,ctx
u=S.symbols('u');data=json.loads(Path(__file__).with_name('fuchsian_model.json').read_text())
C=S.Matrix([[S.sympify(v,locals={'u':u}) for v in r] for r in data['root_connection_matrices']['infinity']])
P=(C*(3125+256*u**5)).applyfunc(S.cancel)
assert all(S.fraction(v)[1].is_number for v in P)
degree=max(S.degree(v,u) if v!=0 else 0 for v in P)
polys=[acb_mat([[acb(str(S.expand(P[i,j]).coeff(u,k))) for j in range(6)] for i in range(6)]) for k in range(degree+1)]
radius=arb('5/4');den=3125-256*radius**5
K=sum((pb.norm(polys[k])*radius**k for k in range(len(polys))),arb(0))/den
ORDER=1600;rho=1/radius;tail=((K*radius).exp()*rho**(ORDER+1)/(1-rho)).upper()
coeff=[pb.I]
for n in range(ORDER):
 q=acb_mat(6,6)
 for j,M in enumerate(polys):
  if n>=j:q+=coeff[n-j]*M
 if n>=5:q-=coeff[n-4]*(256*(n-4))
 coeff.append(q/(3125*(n+1)))
K1=sum(coeff,acb_mat(6,6));err=acb(arb(0,tail),arb(0,tail));K1=acb_mat([[K1[i,j]+err for j in range(6)] for i in range(6)])
Hinf=K1.inv();Yinf=pb.X*Hinf
constant=-arb(96)/(625*arb.pi())*Yinf[0,3].real
# Exact rational centre/endpoints represented by enclosing complex balls.
def local(z,d):
 d0=z.abs_lower();da=(z-pb.a).abs_lower();R=min(d0,da,key=float)/2
 ratio=d.abs_upper()/R;assert ratio<arb('0.3')
 bound=pb.k0/(d0-R)+pb.ka/(da-R)
 remainder=((bound*R).exp()*ratio**(pb.ORDER+1)/(1-ratio)).upper()
 p0=z*(z-pb.a);p1=2*z-pb.a;q0=pb.Q1*z-pb.R0*pb.a
 cs=[pb.I];prev=acb_mat(6,6)
 for n in range(pb.ORDER):
  current=cs[-1];nxt=(current*(q0-pb.I*(n*p1))+prev*(pb.Q1-pb.I*(n-1)))/(p0*(n+1));cs.append(nxt);prev=current
 v=cs[-1]
 for q in reversed(cs[:-1]):v=v*d+q
 er=acb(arb(0,remainder),arb(0,remainder));return acb_mat([[v[i,j]+er for j in range(6)] for i in range(6)])
def edge(H,z,w):
 d=w-z;dist=min(z.abs_lower(),(z-pb.a).abs_lower(),key=float)
 if not d.abs_upper()<dist/10:
  mid=(z+w)/2;return edge(edge(H,z,mid),mid,w)
 return H*local(z,d)
end=pb.a/2;points=[acb(1),acb(1,1),end+acb(0,1),end];H=pb.I
for z,w in zip(points,points[1:]):H=edge(H,z,w)
# w0 has gauge exponent0, so no final D correction enters column3.
Y=pb.X*H;split=96/(625*acb(0,arb.pi()))*Y[0,3]
shifted=constant-split.imag
out={'method':'ordinary infinity-root polynomial recurrence; exact-path Fuchsian balls for splitting','root_series_order':ORDER,'root_majorant_radius':str(radius),'root_majorant_K':str(K),'root_series_tail':str(tail),'H_infinity':pb.mat(Hinf),'Y_infinity':pb.mat(Yinf),'h_b_infinity':str(constant),'a_split':str(split),'h_original_infinity':str(shifted),'scope':'Encloses the claimed infinity value and the splitting translation. Global minimality and uniqueness have not been inferred from these point enclosures.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['H_infinity','Y_infinity']},indent=2))
