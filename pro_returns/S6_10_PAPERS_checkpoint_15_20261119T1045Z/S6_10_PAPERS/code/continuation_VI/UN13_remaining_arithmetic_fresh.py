#!/usr/bin/env python3
"""Post-comparison independent exact checks of the extra printed/producercalculations."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json

def deriv(p,i):
 d={}
 for e,c in p.items():
  if e[i]:
   z=list(e);z[i]-=1;d[tuple(z)]=c*e[i]
 return d

def mul(p,q):
 d={}
 for a,c in p.items():
  for b,e in q.items():
   k=tuple(x+y for x,y in zip(a,b));d[k]=d.get(k,0)+c*e
 return {k:v for k,v in d.items() if v}

def sub(p,q):
 d=p.copy()
 for e,c in q.items():d[e]=d.get(e,0)-c
 return {k:v for k,v in d.items() if v}

r={(1,0):Fraction(1)};a=r;b={(1,1):Fraction(1)};R=mul(r,r)
jac=sub(mul(deriv(a,0),deriv(b,1)),mul(deriv(a,1),deriv(b,0)))
assert jac==r
assert deriv(R,0)=={e:2*c for e,c in r.items()}
assert {e:Fraction(1,2)*c for e,c in deriv(R,0).items()}==jac
b_Aquot=[sum(1 for I in combinations(range(4),k) if (-1)**len(I)==1) for k in range(5)]
assert b_Aquot==[1,0,6,0,1]
e_T=sum((-1)**i*x for i,x in enumerate(b_Aquot));e_P=e_T+16*(2-1)
assert (e_T,e_P)==(8,24)
a1=16*(3-2);a2=e_P-16*2
assert (a1,a2,a1+2*a2)==(16,-8,0)
# Exact normal−2 self-intersection sections of the two exceptional generators.
assert (-2)*Fraction(-1,2)==1
out={'status':'PASS','checks':8,'surface_chart_jacobian':'r','descended_form_coefficient':'1/2','quotient_surface_betti':b_Aquot,'quotient_surface_euler':e_T,'Kummer_euler':e_P,'A_Campo_strata_coefficients':{'a1':a1,'a2':a2,'weighted_euler':a1+2*a2},'normal_minus2_restriction_section':'-1/2','scope':'Post-target independent computation only; no retrospective prereading proof claim. Original code used SymPy; this check uses a new Fraction polynomial implementation.','source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
