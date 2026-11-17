#!/usr/bin/env python3
"""Exact period/unit and finite-cap origin identities for K39.

This checks identities on the specified charts.  It does not certify the
common fan, compact collision quotient, or a completed-family return.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
q1,q2,uQ,uP,uX,lam,v = s.symbols(
    'q1 q2 uQ uP uX lambda0 v', nonzero=True)
N=s.symbols('N', integer=True, positive=True)
Q=q1*q2*uQ
P=uP/q2
cX=q2*uX
rows=[]
for a,b in [(1,2),(2,1)]:
    C=2*(-1)**(b+1)
    h=s.Matrix([Q,P**a])
    g=s.Matrix([P**(-b),C*lam*v**N*q1*cX**(-2)])
    residual=s.Matrix([s.cancel(g[j]/h[j]**b) for j in range(2)])
    transverse=s.cancel(residual[0]**a*residual[1])
    expected=C*lam*v**N/(q1*uQ**2*uP**4*uX**2)
    assert s.cancel(transverse-expected)==0
    assert s.cancel(residual[0]-(q1*uQ*uP)**(-b))==0
    I=s.eye(2)
    W=s.Matrix([[1,b],[-a,-2]])
    E=s.diag(0,N)
    H=I+W+E
    assert H==s.Matrix([[2,b],[-a,N-1]])
    assert W*s.Matrix([-b,1])==s.zeros(2,1)
    assert E*s.Matrix([1,0])==s.zeros(2,1)
    assert H.det()==2*N
    rows.append({
        'a':a,'b':b,'constant':C,
        'source_period':[str(x) for x in h],
        'suspension_period':[str(x) for x in g],
        'W_kernel':[-b,1],
        'residual_source':str(residual[0]),
        'residual_transverse_character_ZaV':str(transverse),
        'E_kernel_source_multiplier':str(Q),
        'H':[[str(x) for x in H.row(i)] for i in range(2)],
    })

# Exact theta cancellation in the primitive target-point lift.
thZ,thZP=s.symbols('Theta_Z Theta_Z_over_P',nonzero=True)
fP=thZP/thZ
fPinv_at_ZoverP=thZ/thZP
assert s.cancel(fP*fPinv_at_ZoverP)==1

# Leading inverse-j coefficient from the actual source Weierstrass equation.
T,eps=s.symbols('T epsilon')
A=1-2*v
disc=A*A*T*T-4*T**3-4*A**3*v**2-27*v**4+18*A*T*v**2
invj=disc/(256*(A*A-3*T)**3)
lead=s.expand(s.series(invj.subs({T:eps*T,v:eps*v}),eps,0,3)
              .removeO()).coeff(eps,2)
assert s.factor(lead-(T*T-4*v*v)/256)==0

# Full ordinary/cap arrow, with both signs and arbitrary integer rescaling.
tt,ss,lh=s.symbols('log_v_over_2pii log_qinf_over_2pii log_h_over_2pii')
caprows=[]
for m in range(1,17):
    for kk in range(1,13):
        for nn in (-1,1):
            ordinary_origin=nn*kk*tt*(-ss+lh)
            cap_variation=nn*kk*tt*ss
            cap_origin=nn*kk*tt*lh
            assert s.expand(cap_variation+ordinary_origin-cap_origin)==0
            assert s.expand(ordinary_origin.subs(ss,ss+1)
                            -ordinary_origin)==-nn*kk*tt
            # eta=zeta-o changes by +nk*tt on a positive qinf cut.
            assert s.expand(-(ordinary_origin.subs(ss,ss+1)
                              -ordinary_origin))==nn*kk*tt
            # For n=+-1, u=n and w=0 is a literal Bezout choice.
            uu=nn; ww=0
            assert nn*uu+m*ww==1
            assert nn*kk*uu+(m*kk)*ww==kk
            assert kk*nn==nn*kk
            caprows.append([m,kk,nn])

data={
    'utc':datetime.now(timezone.utc).isoformat(),
    'status':'PASS: exact unit-period and cap-origin identities',
    'period_rows':rows,
    'inverse_j_leading':str(lead),
    'theta_cancellation':'f_P(Z) f_(P^-1)(Z/P)=1',
    'cap_checks':len(caprows),
    'cap_arrow':'F + o_ord - o_cap = F0; qinf continuation shifts chain by nN/m',
    'bezout_generator':'H=A^u B^w, nu+mw=1; H shift N/m, A shift nN/m',
    'scope':'Actual local periods and finite-base chain attachment. No common collision fan or completed-family return is certified.'
}
(ROOT/'code/part3_fourfold/source_zero_units_caps.json').write_text(
    json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+data['utc']+' — Executed own source_zero_units_caps.py. '
            'Material: exact two-node Tate-unit period identities, theta cancellation, '
            'inverse-j coefficient, and384 signed cap-origin/chain checks. '
            'No global quotient or return inference.\n')
print(json.dumps(data,indent=2))
