"""Independent numerical comparison of rank-four and rank-six normalizations.

The algebraic proof uses the residue pairing and cusp-extension coordinate.
This check integrates the rank-four connection separately, finds its companion
period frame and verifies the predicted scalar against the independently
computed rank-six frame. It is not an interval certificate.
"""
from pathlib import Path
import json,itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
BAS=Path(__file__).resolve().parent.parent
u=sp.symbols('u')
raw=json.loads((BAS/'S6_SERIES_PUBLISH_V_rank4_root_connections.json').read_text())
Gs={k:sp.lambdify(u,sp.Matrix([[sp.sympify(x) for x in row] for row in val]),'numpy') for k,val in raw.items()}
Cf=np.array([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]],complex)
Cg=np.array([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]],complex)
UU={}
for name in ['zero','infty']:
    sol=solve_ivp(lambda t,Y:(Y.reshape(4,4)@Gs[name](t)).ravel(),[0,1],np.eye(4).ravel(),method='DOP853',rtol=2.3e-14,atol=1e-17,max_step=.015)
    assert sol.success;UU[name]=sol.y[:,-1].reshape(4,4)
C0=np.linalg.inv(UU['zero']);CI=np.linalg.inv(UU['infty'])
T0=np.diag(np.exp(-2j*np.pi*np.array([9,3,-3,-9])/8))
TI=np.diag(np.exp(-2j*np.pi*np.array([-6,-2,2,6])/5))
def eq(P):return np.r_[((P@C0)@T0-Cg@P@C0).ravel(),((P@CI)@TI-np.linalg.inv(Cf)@P@CI).ravel()]
cols=[]
for k in range(16):
    E=np.zeros((4,4),complex);E.flat[k]=1;cols.append(eq(E))
CC=np.array(cols).T
_,sv,vh=np.linalg.svd(CC)
Pi=vh[-1,:].conjugate().reshape(4,4)
Jc=np.array([[0,1,-1,1],[-1,0,1,-1],[1,-1,0,1],[-1,1,-1,0]],complex)
Jres=np.array([[0,0,0,4/3],[0,0,4,0],[0,-4,0,0],[-4/3,0,0,0]],complex)
pair=Pi.T@Jc@Pi;scalar=pair[0,3]/Jres[0,3]
assert np.max(np.abs(pair-scalar*Jres))<1e-12
Pi*=np.sqrt(2j*np.pi/scalar)
assert np.max(np.abs(Pi.T@Jc@Pi-2j*np.pi*Jres))<1e-10
pairs=list(itertools.combinations(range(4),2))
wedge=np.array([[np.linalg.det(Pi[np.ix_(ij,kl)]) for kl in pairs] for ij in pairs])
Q=np.eye(6);Q[:,0]=1
five=(np.linalg.inv(Q)@wedge)[1:,:][:,[0,1,2,4,5]]
xx=json.loads((BAS/'S6_SERIES_PUBLISH_V_period_numeric_X.json').read_text())
X=np.array(xx['real'])+1j*np.array(xx['imag']);xx5=X[1:,1:]
t=np.vdot(five.ravel(),xx5.ravel())/np.vdot(five.ravel(),five.ravel())
res=np.max(np.abs(xx5-(625/256)*five))
omegaalg=np.array([0,0,3,1,0,0],complex)
omegac=np.ones(6)
omegaresult=(625/256)*wedge@omegaalg*(16/(625j*np.pi))
data={'smallest_singular_values':sv[-3:].tolist(),'quotient_scale':{'real':float(t.real),'imag':float(t.imag)},'expected_scale':625/256,'rank5_comparison_max_error':float(res),'normalized_bivector_error_to_half_omega_c':float(np.max(np.abs(omegaresult-omegac/2))),'rigorous_interval':False}
print(json.dumps(data,indent=2));(BAS/'S6_SERIES_PUBLISH_V_normalization_compare.json').write_text(json.dumps(data,indent=2)+'\n')
assert res<1e-9
