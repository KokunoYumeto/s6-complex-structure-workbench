#!/usr/bin/env python3
"""Rigorous 240-decimal CM archimedean norms and heights from Fourier tails.

The old floating-point roots only propose rational bracket centres. Both
endpoint signs are certified independently with explicit infinite tails.
No PARI height or floating-point equality is used as a proof step.
"""
from flint import arb,ctx
from pathlib import Path
from fractions import Fraction
from math import gcd,isqrt
import json,re

ROOT=Path(__file__).resolve().parents[1]
ctx.prec=1152
pi=arb.pi();M=350;YMAX=arb(2)/5
ds=[2,3,4,7,7,11,19,27,43,67,163]
disc=[-8,-12,-16,-28,-7,-11,-19,-27,-43,-67,-163]
finite=[[(2,'1/2'),(3,'1/2')],[(2,'2/3'),(3,'1/4')],[(2,'3/4')],[(2,'1')],[(2,'1')],[(3,'1/2')],[],[(3,'5/12')],[],[],[]]
old=json.loads((ROOT/'records/C_cm_theta_pslq.json').read_text())
out=[]
for k,row in enumerate(old):
 T=arb(ds[k]).sqrt()/(1 if k<4 else 2)
 Q=(-2*pi*T).exp();q=Q if k<4 else -Q
 coeff=[];qn=arb(1)
 for n in range(1,M+1):
  qn*=q;coeff.append((n,qn,qn/(1-qn)))
 forms=[]
 for aa in range(1,isqrt((-disc[k])//3)+1):
  for bb in range(-aa,aa+1):
   if (bb*bb-disc[k])%(4*aa):continue
   cc=(bb*bb-disc[k])//(4*aa)
   if aa>cc or ((abs(bb)==aa or aa==cc) and bb<0):continue
   if gcd(gcd(aa,bb),cc)==1:forms.append((aa,bb,cc))
 assert len(forms)==1 and forms[0][0]==1
 E4=1+240*sum((n**3*c for n,qn,c in coeff),arb(0))
 E4tail=240*(M+1)**3*Q**(M+1)*(1+4*Q+Q*Q)/(1-Q)**5
 E4+=arb(0,E4tail)
 logprod=24*sum(((1-qn).log() for n,qn,c in coeff),arb(0))
 logprodtail=24*Q**(M+1)/((1-Q)*(1-Q**(M+1)))
 Delta=q*(logprod+arb(0,logprodtail)).exp()
 jball=E4**3/Delta
 assert abs(jball-row['j'])<arb(1)/4
 a=Q*(2*pi*YMAX).exp()
 tailwp=16*pi*pi/(1-Q)*a**(M+1)*((M+1)-M*a)/(1-a)**2
 assert tailwp<arb('1e-875')
 def wp_y(y):
  val=pi*pi*(1/(pi*y).cosh()**2-arb(1)/3+
       8*sum((n*c*(1-(-1)**n*(2*pi*n*y).cosh()) for n,qn,c in coeff),arb(0)))
  return val+arb(0,tailwp)
 ytext=re.fullmatch(r'\(0\.5 - ([0-9.]+)j\)',row['mu']).group(1)
 yc=arb(ytext);eps=arb(10)**(-240)
 lo=yc-eps;hi=yc+eps
 wl=wp_y(lo);wh=wp_y(hi)
 assert lo>0 and hi<YMAX
 assert wl>0 and wh<0,(k+1,wl,wh)
 y=yc+arb(0,eps)
 # On the entire bracket every product factor is positive.
 ep=(2*pi*y).exp();em=1/ep
 logN=(2*(pi*y).cosh()).log()-pi*T/6-pi*y*y/T
 for n,qn,c in coeff:
  assert 1+qn*ep>0 and 1+qn*em>0
  logN+=(1+qn*ep).log()+(1+qn*em).log()
 # |log(1+x)| <= |x|/(1-|x|); a universal YMAX bounds both factors.
 tailN=2*(2*pi*YMAX).exp()*Q**(M+1)/((1-Q)*(1-(2*pi*YMAX).exp()*Q**(M+1)))
 assert tailN<arb('1e-1260')
 logN+=arb(0,tailN)
 finite_sum=arb(0)
 for p,c in finite[k]:
  c=Fraction(c);finite_sum+=arb(p).log()*c.numerator/c.denominator
 h=finite_sum-logN
 assert h.rad()<arb('1e-236')
 ans=dict(index=k+1,j=row['j'],cm_discriminant=disc[k],terms=M,precision_bits=ctx.prec,
   reduced_forms=forms,j_enclosure=jball.str(60),root_bracket_centre=ytext,root_bracket_radius='1e-240',
   wp_lower_endpoint=wl.str(30),wp_upper_endpoint=wh.str(30),
   wp_tail=tailwp.str(20),logN_tail=tailN.str(20),
   logN=logN.str(280),height_O=h.str(280),norm=logN.exp().str(280))
 out.append(ans)
 print('INDEX',k+1,'j',row['j'],'D',disc[k],flush=True)
 print('wp endpoint signs:',wl.str(12),wh.str(12))
 print('height_O',h.str(280))
 print('logN',logN.str(280))
 print('height radius <1e-236; explicit tails',tailwp.str(6),tailN.str(6),flush=True)
(ROOT/'records/C_cm_height_arb.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL 11 EXACT SIGN BRACKETS AND HEIGHT ENCLOSURES CERTIFIED')
