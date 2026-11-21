"""Independent endpoint recomputation by adaptive DOP853 integration.

This method uses no Taylor-coefficient recurrence or Arb code from the supplied
certificate. It is a floating-point comparison, not an interval certificate.
Exact rational root connections are reconstructed by the companion symbolic
script directly from the displayed Gauss--Manin data.
"""
from pathlib import Path
import json
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import qr

BASE=Path(__file__).resolve().parent.parent
u=sp.symbols('u')
raw=json.loads((BASE/'S6_SERIES_PUBLISH_V_root_connections.json').read_text())
Gs={key:sp.lambdify(u,sp.Matrix([[sp.sympify(x) for x in row] for row in val]),'numpy') for key,val in raw.items()}
A=np.array([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]],dtype=complex)
B=np.array([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]],dtype=complex)
results=[]
for tol in [1e-10,1e-12,2.3e-14]:
    UU={};evaluations={}
    for name in ['zero','infty']:
        sol=solve_ivp(lambda t,Y:(Y.reshape(6,6)@Gs[name](t)).ravel(),[0,1],np.eye(6).ravel(),method='DOP853',rtol=tol,atol=tol*1e-3,max_step=0.025)
        assert sol.success
        UU[name]=sol.y[:,-1].reshape(6,6);evaluations[name]=sol.nfev
    T0=np.diag(np.exp(-2j*np.pi*np.array([0,6,3,0,-3,-6])/4))
    TI=np.diag(np.exp(-2j*np.pi*np.array([0,-8,-4,0,4,8])/5))
    C0=np.linalg.inv(UU['zero']);CI=np.linalg.inv(UU['infty'])
    # The equations at the regular-root frames are used instead of forming
    # monodromy matrices with large conjugation condition numbers.
    def equations(X):
        return np.r_[((X@C0)@T0-B@(X@C0)).ravel(),((X@CI)@TI-A@(X@CI)).ravel()]
    Xfix=np.zeros((6,6),complex);Xfix[0,0]=1
    columns=[]
    for i in range(6):
        for j in range(1,6):
            E=np.zeros((6,6),complex);E[i,j]=1;columns.append(equations(E))
    mat=np.array(columns).T;rhs=-equations(Xfix)
    norms=np.linalg.norm(mat,axis=1);scale=np.where(norms>1e-15,norms,1)
    coeff=mat/scale[:,None];rr=rhs/scale
    vals,res,rank,svals=np.linalg.lstsq(coeff,rr,rcond=None)
    assert rank==30
    X=Xfix.copy();X[:,1:]=vals.reshape(6,5)
    Finf=X@CI;Fzero=X@C0
    factor=96/(625*np.pi)
    # Interior point height: solve the full real intersection system.
    matrix=np.stack([X[1:,1].imag,X[1:,1].real,X[1:,2].imag,X[1:,2].real],axis=1)
    vv=np.linalg.lstsq(matrix,X[1:,3].real,rcond=None)[0]
    hh=factor*(X[0,1]*(vv[0]+1j*vv[1])+X[0,2]*(vv[2]+1j*vv[3])-1j*X[0,3]).imag
    row={'rtol':tol,'evaluations':evaluations,'scaled_equation_residual':float(np.max(np.abs(coeff@vals-rr))),'least_squares_condition':float(svals[0]/svals[-1]),'c_star':float(factor*Finf[0,3].real),'h_zero':float(-factor*Fzero[0,3].real),'h_one':float(hh),'real_intersection_residual':float(np.max(np.abs(matrix@vv-X[1:,3].real)))}
    print(json.dumps(row),flush=True);results.append(row)
comparison={'published_c_star':1.0945402503114027801162682630549457037,'method':'adaptive Dormand-Prince 8(5,3), all-root-frame intertwiner least squares','rigorous_interval':False,'results':results}
(BASE/'S6_SERIES_PUBLISH_V_period_dop853.json').write_text(json.dumps(comparison,indent=2)+'\n')
(BASE/'S6_SERIES_PUBLISH_V_period_numeric_X.json').write_text(json.dumps({'real':X.real.tolist(),'imag':X.imag.tolist()},indent=2)+'\n')
assert abs(results[-1]['c_star']-comparison['published_c_star'])<2e-8
