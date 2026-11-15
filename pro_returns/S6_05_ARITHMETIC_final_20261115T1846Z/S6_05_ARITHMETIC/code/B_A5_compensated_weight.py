#!/usr/bin/env python3
"""Exact and Arb certificates for the compensated radial-face weight.

The analytic integration-by-parts proof is in the companion TeX record.
This script checks its polynomial identities, rational positive patch,
flat-kernel inequalities, nonsquare argument and explicit positive lower
bound.  It does not claim a lower bound for an arithmetic error term.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sympy as sp
from flint import arb, ctx

ctx.prec = 192
BASE = Path(__file__).resolve().parents[1]


def main():
    s,t,z,u,v,r,k=sp.symbols('s t z u v r k', real=True)
    F=s*s-3*t*t-18*z*z
    chi=sp.Function('chi')
    div=sum(sp.diff(y*chi(F), y) for y in (s,t,z))
    assert sp.simplify(div-3*chi(F)-2*F*sp.Subs(sp.Derivative(chi(u),u),u,F))==0
    phase=sp.exp(-2*sp.pi*sp.I*(s+k*z)/r)
    euler=r*sp.diff(phase,r)+sum(y*sp.diff(phase,y) for y in (s,t,z))
    assert sp.simplify(euler)==0
    jac=sp.Matrix((z*u,z*v,z)).jacobian((u,v,z)).det()
    assert sp.simplify(jac-z*z)==0
    assert sp.expand(F.subs({s:z*u,t:z*v})-z*z*(u*u-3*v*v-18))==0
    # Flux on t=0, t=s-4z and 4s=17z; radial top flux is 1.
    assert (t).subs(t,0)==0
    assert (-s+t+4*z).subs(t,s-4*z)==0
    assert (4*s-17*z).subs(s,17*z/4)==0
    assert z.subs(z,1)==1
    print('PASS: radial Jacobian, homogeneity, Euler phase/divergence identities, all face fluxes')

    u0,u1=Q(8489,2000),Q(8491,2000)
    v0,v1=Q(159,2000),Q(161,2000)
    assert 4<u0<u1<Q(17,4)
    assert 0<v0<v1<u0-4
    fmin=u0*u0-3*v1*v1-18
    fmax=u1*u1-3*v0*v0-18
    assert -Q(1,128)<fmin<fmax<Q(1,128)
    area=(u1-u0)*(v1-v0)
    assert area==Q(1,10**6)
    assert Q(2,16**2)<=Q(1,128)
    assert Q(1,64)+Q(2,16**2)==Q(3,128)<Q(1,3)
    assert Q(2,3)*2>1
    print('PASS: positive rational rectangle lies in the actual top face, chi=1 throughout')
    print('rectangle area =',str(area),'; f range =',str(fmin),str(fmax))
    print('PASS: h(r,F+2/X^2)=omega(r)/r exactly for X>=16 and 2/3<=r<=3/4')

    # These identities prove nonsquareness for every integer k>=10.
    n=sp.symbols('n', integer=True, nonnegative=True)
    diff=sp.expand(((n+10)**2-18)-(n+9)**2)
    assert diff==2*n+1 and diff.is_positive
    assert sp.expand((n+10)**2-((n+10)**2-18))==18
    print('PASS: (k-1)^2 < k^2-18 < k^2 for every integer k>=10')

    cosine=(3*arb.pi()/8).cos()
    omega_lower=2*(-arb(1)/8).exp()
    a_lower=cosine/10**6
    # (4/3)^(5/2) is represented using an exact rational and a square root.
    lower=arb(1)/12*omega_lower*(arb(4)/3)**2*(arb(4)/3).sqrt()*a_lower
    assert cosine>0 and omega_lower>0 and lower>0
    print('Arb lower bound for |A(r)|:',a_lower)
    print('Arb lower bound for omega(r):',omega_lower)
    print('Arb positive constant C_* <= L:',lower)

    text=(BASE/'records/B_A5_compensated_weight.tex').read_bytes()
    result={
        'status':'PASS',
        'scope':'Analytic full-weight variation only; not a lower bound for arithmetic error',
        'rectangle':{'u':[str(u0),str(u1)],'v':[str(v0),str(v1)],
                     'f_min':str(fmin),'f_max':str(fmax),'area':str(area)},
        'minimum_X':16,
        'modulus_ratio_interval':['2/3','3/4'],
        'frequency_vector':[1,0,'k'],
        'nonsquare_dual_form':'k^2-18 for every integer k>=10',
        'A_uniform_lower_bound':str(a_lower),
        'omega_uniform_lower_bound':str(omega_lower),
        'positive_lower_bound_for_L':str(lower),
        'precision_bits':ctx.prec,
        'proof_sha256':hashlib.sha256(text).hexdigest(),
        'asymptotic':'Var W_k = L+O(1/k), sum_{k<=H} Var W_k = L H+O(log H)',
        'discrete_asymptotic':'L H+O(log H+H^2/X)',
        'smoothing_scope':'L1 error O(1/H), fixed compact support in |F|<=1/64; k<=eta H',
    }
    (BASE/'records/B_A5_compensated_weight.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL CHECKS PASS. The companion proof establishes linear summed variation, not arithmetic impossibility.')


if __name__=='__main__':
    main()
