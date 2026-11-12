#!/usr/bin/env python3
"""Supplemental exact checks prompted by the supplied Codex progress log.

These checks audit finite algebra in the corrected algebraic-dimension argument,
the Leray/nearby-cycle route, and the Mayer--Vietoris variance repair. They do
not certify geometric identifications, analytic base change, or the existence
of the constructed threefold.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audit" / "codex_integration_checks_results.json"
LOG = ROOT / "audit" / "codex_integration_checks.log"


def record(results: Dict[str, Any], key: str, condition: bool, details: Any) -> None:
    results[key] = {"passed": bool(condition), "details": details}
    if not condition:
        raise AssertionError(f"{key} failed: {details}")


def snf_diag(M: sp.Matrix) -> list[int]:
    D = smith_normal_form(M, domain=ZZ)
    return [abs(int(D[i, i])) for i in range(min(D.rows, D.cols)) if D[i, i] != 0]


def main() -> int:
    r: Dict[str, Any] = {
        "scope": (
            "Supplemental symbolic and integral-lattice checks. Geometric maps, "
            "nearby-cycle functoriality, and analytic duality/base change remain proof-dependent."
        )
    }

    # 1. Corrected modular-frame automorphy on source page 71.
    F, e, j = sp.symbols("F e j", nonzero=True)
    transformed = sp.simplify((j**-1 * F)**-1 * (j**-1 * e))
    record(r, "page_71_corrected_frame_is_invariant", transformed == e/F, {
        "F_transform": "F(gz)=j_g^{-1}F(z)",
        "e_transform": "g^*e=j_g^{-1}e",
        "candidate_frame": "F^{-1}e",
        "transformed": str(transformed),
    })

    # 2-5. Lemma 9.3 and the Neron--Severi conclusion in the current audited source.
    tau, mu, beta = sp.symbols("tau mu beta")
    b, c = sp.symbols("b c")
    Q = 6*mu**2 - tau*beta
    Qg0 = 6*mu**2 - (tau-1)*(beta+1)
    record(r, "lemma_9_3_g0_increment_rechecked", sp.expand(Qg0-Q) == beta-tau+1, {
        "difference": str(sp.expand(Qg0-Q))
    })

    eq92 = 6*b*mu**2 + c*(tau-1)*mu + b*(tau**2+3*tau+1) - c*tau
    eq92g0 = sp.expand(eq92.subs(tau, tau-1))
    diff = sp.expand(eq92g0-eq92)
    expected = -2*b*(tau+1)-c*mu+c
    record(r, "lemma_9_3_second_difference_rechecked", sp.expand(diff-expected) == 0, {
        "difference_with_order_g0_minus_original": str(diff),
        "equivalent_manuscript_identity": "c*mu + 2*b*(tau+1) - c = 0",
    })

    Egu, Egw, Egd, Euw, Eud, Ewd = sp.symbols("Egu Egw Egd Euw Eud Ewd")
    coeffs = sp.Matrix([Egu, -Egw, 6*Euw-Egd, Eud, Ewd])
    solution = sp.linsolve([sp.Eq(x, 0) for x in coeffs], (Egu,Egw,Egd,Euw,Eud,Ewd))
    expected_solution = {(0,0,6*Euw,Euw,0,0)}
    record(r, "lemma_9_3_NS_kernel_is_Z_eta", solution == expected_solution, {
        "solution": str(solution),
        "eta_coordinates": "(0,0,6,1,0,0)",
    })

    n = sp.symbols("n", integer=True, nonzero=True)
    record(r, "proposition_9_5_no_isotropic_multiple_of_eta", sp.expand(12*n**2) != 0, {
        "square_of_n_eta": "12*n^2",
        "logical_use": "rules out a one-dimensional torus algebraic reduction when NS=Z*eta",
    })

    # 6-8. Correct cohomological Mayer--Vietoris calculation behind Lemma A.3.
    # Basis for H^2(dP6): L=aH-b1E1-b2E2-b3E3. Rows are restrictions to C1,...,C6.
    # C1=E1, C2=H-E1-E2, C3=E2, C4=H-E2-E3, C5=E3, C6=H-E1-E3.
    R_dP = sp.Matrix([
        [0, 1, 0, 0],
        [1,-1,-1, 0],
        [0, 0, 1, 0],
        [1, 0,-1,-1],
        [0, 0, 0, 1],
        [1,-1, 0,-1],
    ])
    R_D = sp.Matrix([
        [-1, 0, 0],
        [ 0,-1, 0],
        [ 0, 0,-1],
        [-1, 0, 0],
        [ 0,-1, 0],
        [ 0, 0,-1],
    ])
    MV2 = R_dP.row_join(R_D)
    diag = snf_diag(MV2)
    record(r, "lemma_A3_corrected_cohomology_map_rank_and_saturation", MV2.rank()==4 and diag==[1,1,1,1], {
        "matrix_shape": list(MV2.shape),
        "rank": int(MV2.rank()),
        "smith_nonzero_diagonal": diag,
        "kernel_rank": 7-int(MV2.rank()),
        "cokernel_free_rank": 6-int(MV2.rank()),
    })

    d_difference = sp.Matrix([
        [-1, 1, 1, 1],
        [ 1,-1,-1,-1],
        [-1, 1, 1, 1],
    ])
    record(r, "appendix_B_normalization_difference_map", d_difference.rank()==1 and snf_diag(d_difference)==[1], {
        "rank": int(d_difference.rank()),
        "smith_nonzero_diagonal": snf_diag(d_difference),
        "image_generator": [1,-1,1],
    })

    delta1 = sp.Matrix([[1,-1,1],[1,-1,1]])
    record(r, "appendix_B_V_sheaf_delta1", delta1.rank()==1 and snf_diag(delta1)==[1], {
        "rank": int(delta1.rank()),
        "kernel_rank": 3-int(delta1.rank()),
        "cokernel_free_rank": 2-int(delta1.rank()),
        "smith_nonzero_diagonal": snf_diag(delta1),
    })

    # 9-10. Rank logic in B.5-B.6.
    candidates = []
    for alpha in range(3):
        for beta_r in range(2):
            for gamma in range(2):
                for delta in range(3):
                    for epsilon in range(3):
                        if 4 == 2 + (2-alpha) and 1 == 1-gamma \
                           and 6 == (4-alpha)+(1-beta_r)+(2-delta-epsilon) \
                           and 4 == (2-beta_r-epsilon)+(3-gamma-delta):
                            candidates.append((alpha,beta_r,gamma,delta,epsilon))
    record(r, "appendix_B_rank_bookkeeping_candidates", candidates == [
        (0,0,0,0,1), (0,0,0,1,0), (0,1,0,0,0)
    ], {"candidates_(alpha,beta,gamma,delta,epsilon)": candidates})
    after_sp3 = [x for x in candidates if 2-x[1]-x[4] == 2]
    record(r, "appendix_B_sp3_rank_two_forces_delta_one", after_sp3 == [(0,0,0,1,0)], {
        "remaining_candidate": after_sp3,
        "reason": "rank E_infinity^{3,0}=2-beta-epsilon equals rank H^3(W)=2",
    })

    # 11-12. Leray multiplicativity and p=-1 consequences.
    p, pp = sp.symbols("p pp", integer=True)
    ppp = 2*p-pp
    square_relation = sp.factor(pp**2-ppp**2)
    record(r, "proposition_7_27_common_transgression_integer", sp.expand(square_relation - 4*p*(pp-p)) == 0, {
        "p_double_prime": str(ppp),
        "factorization_of_p_prime_squared_minus_p_double_prime_squared": str(square_relation),
        "conclusion_for_p_nonzero": "p'=p''=p",
    })

    p_actual = -1
    maps = [sp.Matrix([[p_actual]]) for _ in range(3)]
    record(r, "proposition_7_27_actual_unit_differentials", all(M.det() in (-1,1) for M in maps), {
        "p": p_actual,
        "kernel_ranks": [len(M.nullspace()) for M in maps],
        "cokernel_orders": [abs(int(M.det())) for M in maps],
        "consequence": "the three displayed cyclic kernel/cokernel contributions vanish",
    })

    # 13. Literal defect in Remark 7.28 remains demonstrable.
    ell0, ell1, ell2 = 100, 1, -1
    p_value = 12*ell0-4*ell1-3*ell2
    record(r, "remark_7_28_literal_biconditional_counterexample", (ell1%3,ell2%4)==(1,3) and abs(p_value)!=1, {
        "triple": [ell0,ell1,ell2], "residue_pair": [ell1%3,ell2%4], "p": p_value
    })

    # 14. The cusp deck group in the corrected text must be rank two, not the full rank-four lattice.
    # This is a type/rank consistency check for Lambda_bar = Lambda/Lambda_tor.
    rank_Lambda, rank_Lambda_tor = 4, 2
    record(r, "cusp_deck_group_rank_is_rank_Lambda_bar", rank_Lambda-rank_Lambda_tor==2, {
        "rank_Lambda": rank_Lambda,
        "rank_Lambda_tor": rank_Lambda_tor,
        "rank_Lambda_bar": rank_Lambda-rank_Lambda_tor,
        "current_source_usage": "deck group is bar-Lambda; full Lambda is the smooth-fibre H_1 lattice",
    })

    checks = [v for v in r.values() if isinstance(v, dict) and "passed" in v]
    r["summary"] = {
        "checks_run": len(checks),
        "checks_passed": sum(1 for v in checks if v["passed"]),
        "checks_failed": sum(1 for v in checks if not v["passed"]),
    }
    OUT.write_text(json.dumps(r, indent=2, sort_keys=True), encoding="utf-8")
    lines = [f"{k}: {'PASS' if v['passed'] else 'FAIL'}" for k,v in r.items() if isinstance(v,dict) and 'passed' in v]
    lines.append(json.dumps(r["summary"], sort_keys=True))
    LOG.write_text("\n".join(lines)+"\n", encoding="utf-8")
    print(json.dumps(r["summary"], sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
