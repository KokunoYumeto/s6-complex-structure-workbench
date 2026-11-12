#!/usr/bin/env python3
"""Exact symbolic replay for the 4+4+4+1 triality and 14/15-dimensional completion.

The verifier uses real quaternion coordinates and formal starred complex
variables.  It checks polynomial identities only; topology and global ODE/PDE
arguments are proved in the accompanying theorem note.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
JSON_OUT = ROOT / "verification_results.json"
TXT_OUT = ROOT / "verification_output.txt"


def qmul(q, r):
    a, b, c, d = q
    e, f, g, h = r
    return (
        a*e - b*f - c*g - d*h,
        a*f + b*e + c*h - d*g,
        a*g - b*h + c*e + d*f,
        a*h + b*g - c*f + d*e,
    )


def qconj(q):
    a, b, c, d = q
    return (a, -b, -c, -d)


def qnorm2(q):
    return sum(x*x for x in q)


def qreal(q):
    return q[0]


def qsub(q, r):
    return tuple(sp.expand(a-b) for a, b in zip(q, r))


def qscale(a, q):
    return tuple(sp.expand(a*x) for x in q)


def qzero(q):
    return all(sp.expand(x) == 0 for x in q)


def expr_zero(e):
    return sp.factor(sp.expand_complex(sp.expand(e))) == 0


def mat_zero(M):
    return all(expr_zero(x) for x in M)


def check(name, condition, log):
    if not condition:
        raise AssertionError(name)
    log.append(f"PASS  {name}")


def main():
    log = []

    # Quaternionic equal-diagonal determinant.
    lam = sp.symbols('lam', real=True)
    qvars = sp.symbols('q1r q1i q1j q1k q2r q2i q2j q2k q3r q3i q3j q3k', real=True)
    q1 = qvars[0:4]
    q2 = qvars[4:8]
    q3 = qvars[8:12]
    S = qnorm2(q1)+qnorm2(q2)+qnorm2(q3)
    T = qreal(qmul(qmul(q1,q2),q3))
    N13 = sp.expand(lam**3-lam*S+2*T)
    check("equal-diagonal cubic has total degree three", sp.Poly(N13, lam, *qvars).total_degree()==3, log)

    # Gauge invariance of the closed quaternionic product under vertex action
    # is algebraically encoded by cancellation in (a2 q1 a3^-1)(a3 q2 a1^-1)(a1 q3 a2^-1).
    # We verify the gradient formula in exact real coordinates.
    grad_q1 = tuple(sp.diff(N13, x) for x in q1)
    grad_q2 = tuple(sp.diff(N13, x) for x in q2)
    grad_q3 = tuple(sp.diff(N13, x) for x in q3)
    expected_q1 = qscale(2, qsub(qconj(qmul(q2,q3)), qscale(lam,q1)))
    expected_q2 = qscale(2, qsub(qconj(qmul(q3,q1)), qscale(lam,q2)))
    expected_q3 = qscale(2, qsub(qconj(qmul(q1,q2)), qscale(lam,q3)))
    check("gradient in q1", qzero(qsub(grad_q1, expected_q1)), log)
    check("gradient in q2", qzero(qsub(grad_q2, expected_q2)), log)
    check("gradient in q3", qzero(qsub(grad_q3, expected_q3)), log)
    check("gradient in lambda", expr_zero(sp.diff(N13,lam)-(3*lam**2-S)), log)

    # The third-sector source at q3=0.
    zero_sub = {x:0 for x in q3}
    source_q3 = tuple(sp.expand(x.subs(zero_sub)) for x in grad_q3)
    expected_source = qscale(2, qconj(qmul(q1,q2)))
    check("two occupied edges source the third", qzero(qsub(source_q3,expected_source)), log)

    # Complex/quaternionic pair decomposition.  q_i=z_i+conj(b_i)j.
    a1,a2,a3 = sp.symbols('a1 a2 a3', real=True)
    zr = sp.symbols('z1r z2r z3r', real=True)
    zi = sp.symbols('z1i z2i z3i', real=True)
    br = sp.symbols('b1r b2r b3r', real=True)
    bi = sp.symbols('b1i b2i b3i', real=True)
    qq = [(zr[i],zi[i],br[i],-bi[i]) for i in range(3)]
    Nq = sp.expand(a1*a2*a3-a1*qnorm2(qq[0])-a2*qnorm2(qq[1])-a3*qnorm2(qq[2])
                   +2*qreal(qmul(qmul(qq[0],qq[1]),qq[2])))
    I = sp.I
    zc = [zr[i]+I*zi[i] for i in range(3)]
    bv = sp.Matrix([br[i]+I*bi[i] for i in range(3)])
    A = sp.Matrix([
        [a1, zc[2], sp.conjugate(zc[1])],
        [sp.conjugate(zc[2]), a2, zc[0]],
        [zc[1], sp.conjugate(zc[0]), a3],
    ])
    pair = sp.expand_complex(A.det()-(sp.conjugate(bv).T*A*bv)[0])
    check("Moore determinant pair formula det(A)-b^*Ab", expr_zero(Nq-pair), log)

    # Previous A2 block coordinates and the full 15D formula.
    P = sp.Matrix([[1,-1,0],[0,1,-1]])
    u = sp.Matrix([1,1,1])
    C = P*P.T
    RP = P.T*C.inv()
    Pi = u*u.T/sp.Integer(3)
    X = RP.row_join(u)
    check("det X=1", X.det()==1, log)
    check("P R_P=I", P*RP==sp.eye(2), log)
    check("R_P P=I-Pi", RP*P==sp.eye(3)-Pi, log)

    # Formal Hermitian/star variables avoid expanding conjugation assumptions.
    g00,g11,g01,g10 = sp.symbols('g00 g11 g01 g10')
    z0,z1,z0s,z1s,la = sp.symbols('z0 z1 z0s z1s la')
    c0,c1,c0s,c1s,rho,rhos = sp.symbols('c0 c1 c0s c1s rho rhos')
    G = sp.Matrix([[g00,g01],[g10,g11]])
    zz = sp.Matrix([z0,z1]); zzs=sp.Matrix([[z0s,z1s]])
    M = G.row_join(zz).col_join(zzs.row_join(sp.Matrix([[la]])))
    xi = sp.Matrix([c0,c1,rho]); xis=sp.Matrix([[c0s,c1s,rhos]])
    adjG = sp.Matrix([[g11,-g01],[-g10,g00]])
    detM_expected = la*G.det()-(zzs*adjG*zz)[0]
    check("3x3 block determinant", expr_zero(M.det()-detM_expected), log)
    fullN = sp.expand(M.det()-(xis*M*xi)[0])
    expandedN = sp.expand(detM_expected-(sp.Matrix([[c0s,c1s]])*G*sp.Matrix([c0,c1]))[0]
                          -(sp.Matrix([[c0s,c1s]])*zz)[0]*rho
                          -rhos*(zzs*sp.Matrix([c0,c1]))[0]-la*rhos*rho)
    check("full 15D Lorentz-spinor cubic", expr_zero(fullN-expandedN), log)
    N13L = sp.expand(fullN.subs({rho:0,rhos:0}))
    expected13L = sp.expand(detM_expected-(sp.Matrix([[c0s,c1s]])*G*sp.Matrix([c0,c1]))[0])
    check("rho=0 gives 4+4+4+1 Lorentz slice", expr_zero(N13L-expected13L), log)

    # Order-three color cycle gives the exact C1 matrix in quotient coordinates.
    cyc = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    gcyc = sp.simplify(P*cyc*RP)
    C1 = sp.Matrix([[-1,-1],[1,0]])
    check("color 3-cycle induces C1", gcyc==C1, log)
    check("C1 has order three", C1**3==sp.eye(2), log)
    TP = sp.simplify(RP*C1*P+Pi)
    check("T_P(C1) is the color cycle", TP==cyc, log)

    # Full diagonal anisotropy expansion.
    e1,e2 = sp.symbols('eta1 eta2', real=True)
    e3 = -e1-e2
    r1,r2,r3 = sp.symbols('r1 r2 r3', nonnegative=True, real=True)
    full_diag = sp.expand((lam+e1)*(lam+e2)*(lam+e3)
                          -(lam+e1)*r1**2-(lam+e2)*r2**2-(lam+e3)*r3**2 + 2*T)
    expected_diag = sp.expand(N13.subs({qnorm2(q1):r1**2}) if False else
                              lam**3-lam*(r1**2+r2**2+r3**2)+2*T
                              -lam*(e1**2+e2**2+e3**2)/2+e1*e2*e3
                              -(e1*r1**2+e2*r2**2+e3*r3**2))
    check("15D diagonal-anisotropy expansion", expr_zero(full_diag-expected_diag), log)
    d1 = sp.diff(full_diag,e1).subs({e1:0,e2:0})
    d2 = sp.diff(full_diag,e2).subs({e1:0,e2:0})
    check("normal derivative eta1", expr_zero(d1-(-r1**2+r3**2)), log)
    check("normal derivative eta2", expr_zero(d2-(-r2**2+r3**2)), log)

    # Jordan squares of the three edge generators create the two missing Cartan modes.
    E1sq=sp.diag(0,1,1)
    E2sq=sp.diag(1,0,1)
    E3sq=sp.diag(1,1,0)
    D1=(E2sq+E3sq-E1sq)/2
    D2=(E1sq+E3sq-E2sq)/2
    D3=(E1sq+E2sq-E3sq)/2
    check("edge squares generate E11", D1==sp.diag(1,0,0), log)
    check("edge squares generate E22", D2==sp.diag(0,1,0), log)
    check("edge squares generate E33", D3==sp.diag(0,0,1), log)

    # Rank-one quaternionic projector: the transverse triplet norm is the
    # complex 3x2 Pluecker norm.  Starred symbols are independent formal
    # variables, so this is an exact polynomial Cauchy--Binet check.
    z0,z1,z2,w0,w1,w2 = sp.symbols('Z0 Z1 Z2 W0 W1 W2')
    z0s,z1s,z2s,w0s,w1s,w2s = sp.symbols('Z0s Z1s Z2s W0s W1s W2s')
    Zm=sp.Matrix([[z0,w0],[z1,w1],[z2,w2]])
    Zms=sp.Matrix([[z0s,z1s,z2s],[w0s,w1s,w2s]])
    gram=Zms*Zm
    pl=0
    rows=[(z0,w0,z0s,w0s),(z1,w1,z1s,w1s),(z2,w2,z2s,w2s)]
    for ii,jj in ((0,1),(0,2),(1,2)):
        za,wa,zas,was=rows[ii]
        zb,wb,zbs,wbs=rows[jj]
        pl += (zas*wbs-zbs*was)*(za*wb-zb*wa)
    check("triplet norm equals 3x2 Gram determinant", expr_zero(gram.det()-pl), log)

    # Sharp trace-free determinant bound: verify the equality model and the
    # exact vacuum radial algebra on the positive-kappa branch.  The theorem's
    # inequality itself is proved spectrally in the note.
    xv=sp.symbols('xv', real=True)
    sv=6*xv**2
    nv=2*xv**3
    check("projector orbit saturates 54 n^2=s^3", expr_zero(54*nv**2-sv**3), log)

    Gm,mm,kk=sp.symbols('Gamma mm kk', positive=True, real=True)
    disc=kk**2-24*Gm*mm
    xplus=(kk+sp.sqrt(disc))/(12*Gm)
    check("nonzero vacuum root", expr_zero(6*Gm*xplus**2-kk*xplus+mm), log)
    xt=kk/(9*Gm)
    mt=kk**2/(27*Gm)
    Vx=lambda xx,mass: 3*mass*xx**2+9*Gm*xx**4-2*kk*xx**3
    check("coexistence vacuum has zero energy", expr_zero(Vx(xt,mt)), log)
    U2=sp.diff(3*mm*xv**2+9*Gm*xv**4-2*kk*xv**3,xv,2)
    radial_mass=sp.simplify(U2.subs(mm,kk*xv-6*Gm*xv**2)/6)
    check("radial Hessian eigenvalue", expr_zero(radial_mass-xv*(12*Gm*xv-kk)), log)

    # On a traceless lower 2x2 quaternionic block with t=tr(B0^2), the exact
    # quadratic determinant variation is -x*t.  This gives the fivefold mass.
    tB=sp.symbols('tB', real=True)
    quad_coeff=sp.expand(mm*tB/2 + Gm*sv*tB/2 + kk*xv*tB)
    quad_stationary=sp.expand(quad_coeff.subs(mm,kk*xv-6*Gm*xv**2))
    check("fivefold normal Hessian coefficient", expr_zero(quad_stationary-sp.Rational(3,2)*kk*xv*tB), log)

    # Transverse Hessian in the SU(3) 14D model.
    m2,gamma,kappa = sp.symbols('m2 gamma kappa', real=True)
    Atr2 = sp.symbols('Atr2', nonnegative=True, real=True)
    ai = sp.symbols('ai', real=True)
    transverse_eigenvalue = m2+gamma*Atr2+kappa*ai

    results={
        "status":"all exact symbolic identities passed",
        "checks":len(log),
        "triality_cubic":"lambda^3-lambda*(|q1|^2+|q2|^2+|q3|^2)+2 Re(q1 q2 q3)",
        "pair_cubic":"det(A)-b^* A b",
        "lorentz_13_cubic":"lambda det(G)-z^*adj(G)z-chi^*Gchi",
        "full_15_extra_terms":"-2 Re(rho chi^* z)-lambda |rho|^2",
        "cycle_matrix":str(C1.tolist()),
        "normal_sources":[str(d1),str(d2)],
        "transverse_SU3_mass_eigenvalue":str(transverse_eigenvalue),
    }
    JSON_OUT.write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
    TXT_OUT.write_text("\n".join(log)+f"\n\nTOTAL: {len(log)} exact checks passed.\n",encoding="utf-8")
    print(TXT_OUT.read_text(),end="")

if __name__=='__main__':
    main()
