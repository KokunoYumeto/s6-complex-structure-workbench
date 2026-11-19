#!/usr/bin/env python3
"""Exact lower-arm defining function, not a radial coordinate replacement."""
import json
from pathlib import Path
import sympy as s
x2,z2,t2=s.symbols('x2 z2 t2', nonnegative=True)
H=x2+z2
rho2=H*t2+H**2
sigma2=x2+z2+t2
# In the V=1 chart b=H*t2,c=H**2 and rho=sigma2*sqrt(1-u).
b=H*t2;c=H**2;u=b/(b+c)
check=s.factor(sigma2**2*(1-u)-rho2)
assert check==0
# The diagonal chart arrow is identity on (w,S1,T1,T0), so all
# these full defining functions pull back without a coordinate approximation.
out={'status':'PASS','identity':'rho = sigma^2 sqrt(1-u)',
 'squared_residual':str(check),
 'shape':'sigma^2 f=rho0, f=1-chi(1-sqrt(1-u)), chi=1 near lower arm, supported u<1/2',
 'compact_annulus':'rho0/2 <= sigma^2 <= rho0/f',
 'scope':'Actual ambient inclusion with q,v and line unchanged; no global period-strip closure inferred.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact lower-arm defining-function identity')
