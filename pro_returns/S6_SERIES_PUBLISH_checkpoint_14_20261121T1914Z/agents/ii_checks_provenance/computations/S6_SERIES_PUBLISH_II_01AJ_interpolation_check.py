"""Postrelease integer-evaluation identity certificates, distinct from SymPy.

Each tested difference has degree at most 6 separately in u and v.  Vanishing
on a 7 by 7 exact grid therefore proves the polynomial identity by successive
univariate interpolation.  No old program is imported or executed.
"""
import json
checked=0
for u in range(1,8):
 for v in range(1,8):
  x,y,z=u*u*v**3,u,v*v
  grad=[2*x,-4*y**3*z**3,-3*y**4*z**2]
  generator=[2*y*z,-4*x*z,-3*x*y]
  vertical=[2*y*y*z,-4*x*y*z,-3*x*y*y]
  # Clear the displayed multipliers, avoiding division entirely.
  assert [u*v*a-b for a,b in zip(generator,grad)]==[0,0,0]
  assert [v*a-b for a,b in zip(vertical,grad)]==[0,0,0]
  for coeffs in (generator,vertical):
   assert coeffs[0]*2*u*v**3+coeffs[1]==0
   assert coeffs[0]*3*u*u*v*v+coeffs[2]*2*v==0
  assert x*x-y**4*z**3==0
  checked+=1
print(json.dumps({'method':'exact integer evaluation plus degree-bounded tensor-product interpolation',
 'grid_size':[7,7],'points_checked':checked,'all_assertions_passed':True,
 'degree_bound_note':'Gradient, multiplier and pullback differences have separate degree <=6. The normalization equation has degree 6 in v and 4 in u.',
 'timing_scope':'Different-method supplement after release and old-method inspection; original preproof module derivation remains unchanged.'},indent=2))
