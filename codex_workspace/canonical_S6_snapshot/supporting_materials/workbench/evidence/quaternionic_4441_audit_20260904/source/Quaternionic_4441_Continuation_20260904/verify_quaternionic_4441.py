#!/usr/bin/env python3
"""Exact symbolic verification for the 4+4+4+1 quaternionic continuation.

The calculation uses formal starred variables.  The 2x2 complex symplectic
realisation rho(z+w j)=[[z,w],[-w*,z*]] converts quaternionic identities to
ordinary polynomial identities.  No floating-point sampling is used.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT_JSON = ROOT / "verification_results.json"
OUT_TXT = ROOT / "verification_output.txt"


def zexpr(e: sp.Expr) -> bool:
    return sp.factor(sp.together(sp.expand(e))) == 0


def zmat(M: sp.Matrix) -> bool:
    return all(zexpr(x) for x in M)


def check_expr(name: str, lhs: sp.Expr, rhs: sp.Expr, log: list[str]) -> None:
    if not zexpr(lhs-rhs):
        raise AssertionError(f"{name}: {sp.factor(lhs-rhs)}")
    log.append(f"PASS  {name}")


def check_matrix(name: str, lhs: sp.Matrix, rhs: sp.Matrix, log: list[str]) -> None:
    if not zmat(lhs-rhs):
        raise AssertionError(f"{name}:\n{lhs-rhs}")
    log.append(f"PASS  {name}")


def rho_q(z, w, zs, ws):
    """Complex 2x2 representation of q=z+w*j."""
    return sp.Matrix([[z, w], [-ws, zs]])


def rho_q_star(z, w, zs, ws):
    """Formal conjugate transpose of rho_q."""
    return sp.Matrix([[zs, -w], [ws, z]])


def rho_c(x, xs):
    return sp.diag(x, xs)


def main() -> None:
    log: list[str] = []

    # Retained A2 observation data.
    P = sp.Matrix([[1,-1,0],[0,1,-1]])
    u = sp.Matrix([1,1,1])
    C = P*P.T
    R = P.T*C.inv()
    Pi = u*u.T/sp.Integer(3)
    X = R.row_join(u)
    Y = P.col_join(u.T/sp.Integer(3))
    check_matrix("P R=I2",P*R,sp.eye(2),log)
    check_matrix("R P=I3-Pi",R*P,sp.eye(3)-Pi,log)
    check_expr("det X=1",X.det(),sp.Integer(1),log)
    check_matrix("X inverse",Y*X,sp.eye(3),log)

    # Generic complex-Hermitian Lorentz vector and two quaternionic spinor columns.
    a,b,c,cs,lam = sp.symbols('a b c cs lam')
    z1,z2,w1,w2 = sp.symbols('z1 z2 w1 w2')
    z1s,z2s,w1s,w2s = sp.symbols('z1s z2s w1s w2s')
    G = sp.Matrix([[a,c],[cs,b]])
    Adj = G.adjugate()
    z = sp.Matrix([z1,z2]); zs = sp.Matrix([[z1s,z2s]])
    w = sp.Matrix([w1,w2]); ws = sp.Matrix([[w1s,w2s]])
    N13 = sp.expand(lam*G.det()-(zs*Adj*z)[0]-(ws*Adj*w)[0])

    # Quaternionic quadratic form decomposes as two complex Weyl terms.
    A00,A11,A01,A10 = sp.symbols('A00 A11 A01 A10')
    AH = sp.Matrix([[A00,A01],[A10,A11]])
    q1 = rho_q(z1,w1,z1s,w1s)
    q2 = rho_q(z2,w2,z2s,w2s)
    q1s = rho_q_star(z1,w1,z1s,w1s)
    q2s = rho_q_star(z2,w2,z2s,w2s)
    qform = q1s*rho_c(A00,A00)*q1 + q1s*rho_c(A01,A10)*q2 \
          + q2s*rho_c(A10,A01)*q1 + q2s*rho_c(A11,A11)*q2
    qform_scalar = (zs*AH*z)[0]+(ws*AH*w)[0]
    check_matrix("quaternionic form = two complex forms",qform,qform_scalar*sp.eye(2),log)

    # Full 6x6 complex representation of the quaternionic Hermitian 3x3 block.
    blocks = [
        [rho_c(a,a), rho_c(c,cs), q1],
        [rho_c(cs,c), rho_c(b,b), q2],
        [q1s, q2s, lam*sp.eye(2)],
    ]
    rhoM = sp.Matrix.vstack(*[sp.Matrix.hstack(*row) for row in blocks])
    check_expr("complex determinant is Moore determinant squared",rhoM.det(),N13**2,log)

    # Dirac rewrite w=epsilon conjugate(chi_R).
    xr,xs_,yr,ys_ = sp.symbols('xr xs yr ys')
    # chi=(x,y), chi-star=(xs,ys); w=epsilon*bar(chi)=(ys,-xs).
    eps2 = sp.Matrix([[0,1],[-1,0]])
    chi = sp.Matrix([xr,yr]); chis = sp.Matrix([[xs_,ys_]])
    w_dirac = sp.Matrix([ys_,-xs_])
    ws_dirac = sp.Matrix([yr,-xr])
    check_matrix("epsilon^* adj(G) epsilon = G^T",eps2.T*Adj*eps2,G.T,log)
    check_expr("right-spinor rewrite",(ws_dirac.T*Adj*w_dirac)[0],(chis*G*chi)[0],log)

    # SL2 covariance with formal inverse and starred inverse.
    ga,gb,gc,gd = sp.symbols('ga gb gc gd')
    gas,gbs,gcs,gds = sp.symbols('gas gbs gcs gds')
    g = sp.Matrix([[ga,gb],[gc,gd]])
    gs = sp.Matrix([[gas,gcs],[gbs,gds]])  # formal g^*
    detg = g.det(); detgs = gs.det()
    Gp = g*G*gs
    # General 2x2 adjugate covariance includes determinant factors.
    rhs_adj = detg*detgs*gs.inv()*Adj*g.inv()
    check_matrix("adjugate congruence",Gp.adjugate(),rhs_adj,log)

    # Internal SU2 trace invariance written algebraically for det(k)=1 and k^*k=I
    # is verified on the standard generic unit-quaternion parameterisation.
    alpha,beta,alphas,betas = sp.symbols('alpha beta alphas betas')
    k = sp.Matrix([[alphas,-beta],[betas,alpha]])
    ks = sp.Matrix([[alpha,beta],[-betas,alphas]])
    Z = sp.Matrix.hstack(z,w)
    Zs = sp.Matrix.vstack(zs,ws)
    trace_before = sp.trace(Zs*Adj*Z)
    trace_after = sp.trace(ks*Zs*Adj*Z*k)
    check_expr("right SU2 trace covariance",trace_after,
               (alpha*alphas+beta*betas)*trace_before,log)

    # Old 9D restriction and determinant correction.
    N9 = sp.expand(lam*G.det()-(zs*Adj*z)[0])
    check_expr("w=0 restriction is old cubic",N13.subs({w1:0,w2:0,w1s:0,w2s:0}),N9,log)
    check_expr("retraction determinant correction",N9-N13,(ws*Adj*w)[0],log)

    # Complex rank-four 13D model with the same coordinates.
    Zc = sp.Matrix([[z1,w1],[z2,w2]])
    Zcs = sp.Matrix([[z1s,z2s],[w1s,w2s]])
    K4 = sp.Matrix.vstack(
        sp.Matrix.hstack(G,Zc),
        sp.Matrix.hstack(Zcs,lam*sp.eye(2)),
    )
    detZstarZ = (z1*w2-z2*w1)*(z1s*w2s-z2s*w1s)
    D4 = sp.expand(lam**2*G.det()-lam*sp.trace(Zcs*Adj*Zc)+detZstarZ)
    check_expr("complex rank-four determinant",K4.det(),D4,log)
    check_expr("quartic-cubic comparison",D4,lam*N13+detZstarZ,log)

    # Jordan nonclosure example in the canonical 2+1 quaternionic block.
    one = sp.eye(2); zero = sp.zeros(2)
    jmat = rho_q(0,1,0,1)  # j
    # psi=(1,0), phi=(0,j)
    psi_blocks = [one, zero]
    phi_blocks = [zero, jmat]
    def offdiag_matrix(vblocks):
        top = sp.Matrix.hstack(sp.zeros(4), sp.Matrix.vstack(*vblocks))
        bottom = sp.Matrix.hstack(sp.Matrix.hstack(*[v.T.conjugate() for v in vblocks]), sp.zeros(2))
        # formal numeric blocks here are real except j; use actual conjugate transpose instead.
        V = sp.Matrix.vstack(*vblocks)
        return sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(4),V),sp.Matrix.hstack(V.conjugate().T,sp.zeros(2)))
    Uq = offdiag_matrix(psi_blocks)
    Vq = offdiag_matrix(phi_blocks)
    Jprod = sp.simplify((Uq*Vq+Vq*Uq)/2)
    # The (1,2) quaternionic entry in the upper 2x2 block is -j/2, not complex.
    check_matrix("Jordan nonclosure witness block",Jprod[0:2,2:4],-jmat/2,log)

    results = {
        "status":"all exact symbolic identities passed",
        "tests_passed":len(log),
        "dimension":"4+4+4+1=13",
        "cubic":"lambda det(G)-z^*adj(G)z-w^*adj(G)w",
        "dirac_cubic":"lambda det(G)-psi_L^*adj(G)psi_L-psi_R^*G psi_R",
        "old_slice":"w=0",
        "quartic_comparison":"det K4 = lambda N13 + |det[z,w]|^2",
        "compactified_boundary":"S^12 (topological theorem, proved in note)",
    }
    OUT_JSON.write_text(json.dumps(results,indent=2)+"\n",encoding='utf-8')
    OUT_TXT.write_text("\n".join(log)+f"\n\nTOTAL: {len(log)} exact checks passed.\n",encoding='utf-8')
    print(OUT_TXT.read_text(encoding='utf-8'),end='')

if __name__=='__main__':
    main()
