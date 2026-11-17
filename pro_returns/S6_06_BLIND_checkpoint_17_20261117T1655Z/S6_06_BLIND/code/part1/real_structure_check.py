"""Exact and numerical comparisons for possible anti-holomorphic actions.

The fan test below is specific to the chosen cusp marking S.  It is not
by itself a theorem excluding all anti-holomorphic maps of the compact
fourfold: the based cusp comparison and translations still need checking.
"""
from pathlib import Path
import contextlib,io,json,re
with contextlib.redirect_stdout(io.StringIO()):
    exec(Path(__file__).with_name('lift_period_values.py').read_text().split("out={'normalization'")[0])
Kb=acb_mat([[X[i,j].conjugate() for j in range(6)] for i in range(6)])*X.inv()
K=s.Matrix([[round(float(Kb[i,j].real)) for j in range(6)] for i in range(6)])
print('conjugation_intertwiner_K',K)
print('numerical_integer_error',norm(Kb-cm(K)))
assert K*K==s.eye(6)
assert K*t.A*K==t.A.inv() and K*t.B*K==t.B.inv()
G=-K.T
print('candidate_homology_G',G)
M0=t.M0;N=M0-s.eye(6)
S=s.Matrix.hstack(N[:,0],N[:,3],N[:,4],s.eye(6)[:,0],s.eye(6)[:,3],s.eye(6)[:,4])
for tag,H in [('G',G),('M2_inv_G',t.M2.inv()*G),('M1_G',t.M1*G)]:
    Hs=S.inv()*H*S
    anti=H*M0*H.inv()==M0.inv()
    print(tag,'anti_cusp',anti,'in_S',Hs)
    if anti:
        P=Hs[:3,:3]
        rays={tuple(sign*x for x in v) for v in __import__('itertools').product([0,1],repeat=3) if any(v) for sign in [-1,1]}
        images={tuple(P*s.Matrix(v)) for v in rays}
        print('fan_ray_preservation',images==rays,'first_bad',next((x for x in images if x not in rays),None))
