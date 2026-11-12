#!/usr/bin/env python3
"""Independent exact-arithmetic checks for the supplied S6 packet 06 (pp. 56--66).

The script verifies only algebra that is fully specified in the supplied slice.  It
cannot validate geometric inputs, local models, specialization maps, or results
contained in missing packets.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "computational_checks" / "results.json"
LOG = ROOT / "computational_checks" / "verification.log"


def gcd_list(values: Sequence[int]) -> int:
    g = 0
    for value in values:
        g = math.gcd(g, abs(int(value)))
    return g


def minors(matrix: sp.Matrix, order: int) -> List[int]:
    vals: List[int] = []
    for rows in itertools.combinations(range(matrix.rows), order):
        for cols in itertools.combinations(range(matrix.cols), order):
            vals.append(int(matrix.extract(rows, cols).det()))
    return vals


def wedge_matrix(A: sp.Matrix, k: int) -> Tuple[sp.Matrix, List[Tuple[int, ...]]]:
    """Matrix for wedge^k A in the lexicographically ordered exterior basis."""
    n = A.rows
    assert A.cols == n
    basis = list(itertools.combinations(range(n), k))
    W = sp.zeros(len(basis), len(basis))
    for j, cols in enumerate(basis):
        for i, rows in enumerate(basis):
            W[i, j] = A.extract(rows, cols).det()
    return W, basis


def canonical_snf_diagonal(M: sp.Matrix) -> List[int]:
    D = smith_normal_form(M, domain=ZZ)
    diag: List[int] = []
    for i in range(min(D.rows, D.cols)):
        d = int(D[i, i])
        if d != 0:
            diag.append(abs(d))
    return diag


def assertion(result: Dict, key: str, condition: bool, details) -> None:
    result[key] = {"passed": bool(condition), "details": details}
    if not condition:
        raise AssertionError(f"{key} failed: {details}")


def main() -> int:
    results: Dict[str, object] = {
        "scope": (
            "Exact arithmetic and linear-algebra checks for mathematical formulas "
            "fully specified in packet 06; no claim about missing geometric inputs."
        )
    }

    # ------------------------------------------------------------------
    # Theorem 7.17: relation matrix and admissibility arithmetic.
    # ------------------------------------------------------------------
    l0, l1, l2 = sp.symbols("ell_0 ell_1 ell_2", integer=True)
    R = sp.Matrix([[3, -l1], [4, l2 - 4*l0]])
    assertion(results, "theorem_7_17_determinant", sp.expand(R.det()) == -(12*l0 - 4*l1 - 3*l2), {
        "det_R": str(sp.expand(R.det())),
        "minus_p": str(-(12*l0 - 4*l1 - 3*l2)),
    })

    sample_R = sp.Matrix([[3, -1], [4, -1]])  # (ell0,ell1,ell2)=(0,1,-1)
    assertion(results, "theorem_7_17_sample_snf", canonical_snf_diagonal(sample_R) == [1, 1], {
        "matrix": [list(map(int, sample_R.row(i))) for i in range(sample_R.rows)],
        "snf_nonzero_diagonal": canonical_snf_diagonal(sample_R),
    })
    comparison_R = sp.Matrix([[3, -1], [4, 1]])
    assertion(results, "theorem_7_17_comparison_snf", canonical_snf_diagonal(comparison_R) == [1, 7], {
        "matrix": [list(map(int, comparison_R.row(i))) for i in range(comparison_R.rows)],
        "snf_nonzero_diagonal": canonical_snf_diagonal(comparison_R),
    })

    residue_checks = []
    admissibility_ok = True
    for a in range(12):
        for b in range(12):
            if a % 3 != 0 and b % 2 == 1:
                pmod = (-4*a - 3*b) % 12
                g = math.gcd(pmod, 12)
                residue_checks.append({"ell1_mod12": a, "ell2_mod12": b, "p_mod12": pmod, "gcd": g})
                admissibility_ok &= (g == 1)
    assertion(results, "theorem_7_17_gcd_p_12", admissibility_ok, residue_checks)

    # Lemma 7.19(a): relation matrix minors and primitive functional.
    # Exhaust all admissible residue classes mod 12.
    rel_ok = True
    rel_data = []
    for a in range(12):
        for b in range(12):
            if a % 3 != 0 and b % 2 == 1:
                M = sp.Matrix([[-a, 3, 0], [-b, 0, 4]])
                two_min = minors(M, 2)
                gcd2 = gcd_list(two_min)
                phi = sp.Matrix([[12, 4*a, 3*b]])
                kills = phi * M.T == sp.zeros(1, 2)
                primitive = gcd_list([12, 4*a, 3*b]) == 1
                rel_ok &= (gcd2 == 1 and kills and primitive)
                rel_data.append({
                    "ell1_mod12": a,
                    "ell2_mod12": b,
                    "gcd_2x2_minors": gcd2,
                    "functional_kills_relations": bool(kills),
                    "functional_primitive": primitive,
                })
    assertion(results, "lemma_7_19_relation_lattice", rel_ok, rel_data)

    # ------------------------------------------------------------------
    # Lemma 7.18: M0 exterior powers and Wang ranks.
    # Basis: (hat_gamma, hat_u, hat_w, hat_delta), vectors as columns.
    # ------------------------------------------------------------------
    M0 = sp.Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [-1, 0, 0, 1],
    ])
    assertion(results, "m0_unimodular", int(M0.det()) == 1, {"det": int(M0.det())})

    wedge_data = {}
    wang_ranks = []
    wedge_mats = {}
    for k in range(0, 5):
        W, basis = wedge_matrix(M0, k)
        wedge_mats[k] = (W, basis)
        D = W - sp.eye(W.rows)
        ker_rank = len(D.nullspace())
        coker_free_rank = D.rows - D.rank()
        snf = canonical_snf_diagonal(D)
        torsion = [d for d in snf if d > 1]
        wedge_data[str(k)] = {
            "basis": basis,
            "rank_difference": int(D.rank()),
            "kernel_rank": ker_rank,
            "cokernel_free_rank": coker_free_rank,
            "cokernel_torsion_invariants": torsion,
        }
    # Wang: rank H_k(M)=rank coker on wedge^k + rank ker on wedge^(k-1).
    for k in range(0, 6):
        coker_rank = 0
        ker_prev = 0
        if 0 <= k <= 4:
            Dk = wedge_mats[k][0] - sp.eye(wedge_mats[k][0].rows)
            coker_rank = Dk.rows - Dk.rank()
        if 0 <= k-1 <= 4:
            Dp = wedge_mats[k-1][0] - sp.eye(wedge_mats[k-1][0].rows)
            ker_prev = len(Dp.nullspace())
        wang_ranks.append(coker_rank + ker_prev)
    assertion(results, "lemma_7_18_wang_ranks", wang_ranks == [1, 3, 6, 6, 3, 1], {
        "computed": wang_ranks,
        "claimed": [1, 3, 6, 6, 3, 1],
        "exterior_power_data": wedge_data,
    })

    W2, basis2 = wedge_mats[2]
    D2 = W2 - sp.eye(W2.rows)
    # Claimed generators in basis (gamma u, gamma w, gamma delta, u w, u delta, w delta):
    # w delta and gamma w + u delta.
    G = sp.Matrix.hstack(
        sp.Matrix([0, 0, 0, 0, 0, 1]),
        sp.Matrix([0, 1, 0, 0, 1, 0]),
    )
    # Equality of image lattices: every column of D2 belongs to G Z^2, and G's
    # generators belong to image(D2). Solve over integers by checking augmented SNF indices.
    def lattice_rank_and_gcdmax(A: sp.Matrix) -> Tuple[int, int]:
        r = A.rank()
        if r == 0:
            return 0, 1
        return r, gcd_list(minors(A, r))

    rank_D2, gcd_D2 = lattice_rank_and_gcdmax(D2)
    rank_G, gcd_G = lattice_rank_and_gcdmax(G)
    rank_union, gcd_union = lattice_rank_and_gcdmax(sp.Matrix.hstack(D2, G))
    image_equal = rank_D2 == rank_G == rank_union == 2 and gcd_D2 == gcd_G == gcd_union
    assertion(results, "lemma_7_18_wedge2_image", image_equal, {
        "basis": basis2,
        "difference_matrix": [list(map(int, D2.row(i))) for i in range(D2.rows)],
        "rank_and_determinantal_divisor_image": [rank_D2, gcd_D2],
        "rank_and_determinantal_divisor_claimed": [rank_G, gcd_G],
        "rank_and_determinantal_divisor_union": [rank_union, gcd_union],
    })

    # ------------------------------------------------------------------
    # Remark 7.20: alpha_2 matrix.
    # ------------------------------------------------------------------
    alpha2 = sp.Matrix([
        [2, 1, 3, 0, 0, 0],
        [-4, -2, 0, 1, 0, 0],
        [-2, -2, -4, 0, 0, 0],
        [3, 3, 0, -1, 0, 0],
    ])
    m3 = minors(alpha2, 3)
    left_kernel = alpha2.T.nullspace()
    left_gen = sp.Matrix([4, 2, 3, 2])
    assertion(results, "remark_7_20_alpha2", alpha2.rank() == 3 and gcd_list(m3) == 1 and alpha2.T * left_gen == sp.zeros(6, 1), {
        "rank": int(alpha2.rank()),
        "gcd_3x3_minors": gcd_list(m3),
        "nonzero_3x3_minors": sorted(set(v for v in m3 if v != 0)),
        "left_kernel_basis_rational": [[str(x) for x in v] for v in left_kernel],
        "claimed_left_generator_annihilates": bool(alpha2.T * left_gen == sp.zeros(6, 1)),
    })

    # ------------------------------------------------------------------
    # Remark 7.28: quantifier defect.
    # ------------------------------------------------------------------
    counterexample = {"ell0": 100, "ell1": 1, "ell2": -1}
    p_counter = 12*counterexample["ell0"] - 4*counterexample["ell1"] - 3*counterexample["ell2"]
    residue_pair = (counterexample["ell1"] % 3, counterexample["ell2"] % 4)
    assertion(results, "remark_7_28_literal_biconditional_false", residue_pair in {(1, 3), (2, 1)} and abs(p_counter) != 1, {
        **counterexample,
        "residue_pair": residue_pair,
        "p": p_counter,
        "interpretation": "Counterexample to the literal fixed-triple biconditional; the intended existential statement in ell0 is true.",
    })
    existential_ok = True
    existential_data = []
    for a in range(3):
        for b in range(4):
            possible = False
            witnesses = []
            for l1v in range(-12, 13):
                for l2v in range(-12, 13):
                    if l1v % 3 == a and l2v % 4 == b:
                        for sign in (-1, 1):
                            numerator = sign + 4*l1v + 3*l2v
                            if numerator % 12 == 0:
                                possible = True
                                witnesses.append((numerator//12, l1v, l2v, sign))
                                break
                        if possible:
                            break
                if possible:
                    break
            target = (a, b) in {(1, 3), (2, 1)}
            existential_ok &= (possible == target)
            existential_data.append({"residue_pair": [a,b], "exists_ell0_with_abs_p_1": possible, "target": target, "witness": witnesses[:1]})
    assertion(results, "remark_7_28_corrected_existential", existential_ok, existential_data)

    # ------------------------------------------------------------------
    # Lemmas 9.2--9.4: exterior algebra and period transformations.
    # ------------------------------------------------------------------
    tau, mu, beta = sp.symbols("tau mu beta")
    # Coefficient vectors for sigma1, sigma2 in (gamma,u,w,delta).
    s1 = sp.Matrix([6*mu, tau, 1, 0])
    s2 = sp.Matrix([beta, mu, 0, 1])
    # Wedge coefficient dictionary.
    wedge_coeff = {}
    one_basis = ["gamma", "u", "w", "delta"]
    for i, j in itertools.combinations(range(4), 2):
        wedge_coeff[f"{one_basis[i]}^{one_basis[j]}"] = sp.expand(s1[i]*s2[j] - s1[j]*s2[i])
    claimed_wedge = {
        "gamma^u": 6*mu**2 - tau*beta,
        "gamma^w": -beta,
        "gamma^delta": 6*mu,
        "u^w": -mu,
        "u^delta": tau,
        "w^delta": 1,
    }
    assertion(results, "lemma_9_2_sigma_wedge", all(sp.simplify(wedge_coeff[k]-v)==0 for k,v in claimed_wedge.items()), {
        "computed": {k: str(v) for k,v in wedge_coeff.items()},
        "claimed": {k: str(v) for k,v in claimed_wedge.items()},
    })

    # P_E coefficient check via complementary wedge pairing.
    Egu, Egw, Egd, Euw, Eud, Ewd = sp.symbols("E_gu E_gw E_gd E_uw E_ud E_wd")
    P_claimed = Egu - Egw*tau - Egd*mu + 6*Euw*mu + Eud*beta + Ewd*(6*mu**2-tau*beta)
    # Pairing matrix in 2-form basis lexicographic.
    # Compute via permutation sign.
    basis_pairs = list(itertools.combinations(range(4), 2))
    Evec = sp.Matrix([Egu, Egw, Egd, Euw, Eud, Ewd])
    Sve = sp.Matrix([wedge_coeff[f"{one_basis[i]}^{one_basis[j]}"] for i,j in basis_pairs])
    P_computed = 0
    for a, pair_a in enumerate(basis_pairs):
        for b, pair_b in enumerate(basis_pairs):
            if set(pair_a).isdisjoint(pair_b):
                seq = list(pair_a + pair_b)
                inv = sum(1 for i in range(4) for j in range(i+1,4) if seq[i] > seq[j])
                P_computed += Evec[a]*Sve[b]*((-1)**inv)
    P_computed = sp.expand(P_computed)
    assertion(results, "lemma_9_2_PE_formula", sp.simplify(P_computed-P_claimed)==0, {
        "computed": str(P_computed), "claimed": str(P_claimed)
    })

    # Lemma 9.3 transformation identities.
    Q = 6*mu**2 - tau*beta
    g0 = {tau: tau-1, mu: mu, beta: beta+1}
    Q_g0 = sp.expand(Q.subs(g0, simultaneous=True))
    assertion(results, "lemma_9_3_g0_Q", sp.simplify(Q_g0 - (Q + beta - tau + 1)) == 0, {
        "computed": str(Q_g0), "claimed_increment": str(beta-tau+1)
    })

    g2 = {tau: -1/tau, mu: 1+mu/tau, beta: beta-3-6*mu**2/tau}
    tau_plus_beta_g2 = sp.simplify((tau+beta).subs(g2, simultaneous=True))
    mu_g2 = sp.simplify(mu.subs(g2, simultaneous=True))
    assertion(results, "lemma_9_3_g2_transform", sp.simplify(tau_plus_beta_g2 - (-1/tau + beta - 3 - 6*mu**2/tau)) == 0 and sp.simplify(mu_g2-(1+mu/tau))==0, {
        "tau_plus_beta_g2": str(tau_plus_beta_g2), "mu_g2": str(mu_g2)
    })

    a,b,c,d,e = sp.symbols("a b c d e")
    L = a+b*tau+c*mu+d*beta+e*Q
    Lg0_minus_L = sp.expand(L.subs(g0, simultaneous=True)-L)
    assertion(results, "lemma_9_3_first_difference", sp.simplify(Lg0_minus_L - (-b+d+e*(beta-tau+1)))==0, {
        "computed": str(Lg0_minus_L)
    })
    L_reduced = a+b*(tau+beta)+c*mu
    expr_g2 = sp.simplify((L_reduced.subs(g2, simultaneous=True)-L_reduced)*(-tau))
    eq92 = 6*b*mu**2 + c*(tau-1)*mu + b*(tau**2+3*tau+1) - c*tau
    assertion(results, "lemma_9_3_equation_9_2", sp.simplify(expr_g2-eq92)==0, {
        "computed": str(sp.expand(expr_g2)), "claimed": str(eq92)
    })
    eq92_g0_diff = sp.expand(eq92.subs(g0, simultaneous=True)-eq92)
    # Manuscript's displayed result differs by an overall sign depending on subtraction order.
    target_diff = c*mu + 2*b*(tau+1) - c
    assertion(results, "lemma_9_3_second_difference", sp.simplify(eq92_g0_diff-target_diff)==0 or sp.simplify(eq92_g0_diff+target_diff)==0, {
        "computed": str(eq92_g0_diff), "claimed_up_to_subtraction_order": str(target_diff)
    })

    # Lemma 9.4: eta^2 and Gram matrix.
    # eta vector in 2-form basis (gamma u, gamma w, gamma delta, u w, u delta, w delta).
    eta_vec = sp.Matrix([0,0,6,1,0,0])
    eta_square = 0
    for aa, pa in enumerate(basis_pairs):
        for bb, pb in enumerate(basis_pairs):
            if set(pa).isdisjoint(pb):
                seq = list(pa+pb)
                inv = sum(1 for i in range(4) for j in range(i+1,4) if seq[i] > seq[j])
                eta_square += eta_vec[aa]*eta_vec[bb]*((-1)**inv)
    assertion(results, "lemma_9_4_eta_square", int(eta_square)==12, {"computed": int(eta_square), "claimed": 12})

    # Inverse bivector B on V: B(gamma,delta)=-1/6, B(u,w)=-1.
    B = sp.Matrix([
        [0, 0, 0, -sp.Rational(1,6)],
        [0, 0, -1, 0],
        [0, 1, 0, 0],
        [sp.Rational(1,6), 0, 0, 0],
    ])
    tau_b, mu_b, beta_b = sp.symbols("tau_bar mu_bar beta_bar")
    sb1 = sp.Matrix([6*mu_b, tau_b, 1, 0])
    sb2 = sp.Matrix([beta_b, mu_b, 0, 1])
    sigmas = [s1, s2]
    bars = [sb1, sb2]
    Evals = sp.Matrix(2,2, lambda i,j: sp.expand((sigmas[i].T*B*bars[j])[0]))
    # Substitute z-bar differences using Im z = (z-zbar)/(2i); compute i E^.
    I = sp.I
    Gmat = sp.simplify(I*Evals)
    claimed_G = sp.Matrix([
        [I*(tau_b-tau), I*(mu_b-mu)],
        [I*(mu_b-mu), I*(beta_b-beta)/6],
    ])
    # I*(bar-tau)=2 Im(tau); last entry=(1/3)Im(beta).
    assertion(results, "lemma_9_4_gram_matrix", all(sp.simplify(Gmat[i,j]-claimed_G[i,j])==0 for i in range(2) for j in range(2)), {
        "Evee_pairings": [[str(Evals[i,j]) for j in range(2)] for i in range(2)],
        "G_symbolic": [[str(Gmat[i,j]) for j in range(2)] for i in range(2)],
        "interpretation": "[[2 Im tau, 2 Im mu],[2 Im mu,(1/3) Im beta]]",
    })
    Imt, Imm, Imb = sp.symbols("Im_tau Im_mu Im_beta", real=True)
    G_real = sp.Matrix([[2*Imt, 2*Imm],[2*Imm, sp.Rational(1,3)*Imb]])
    detG = sp.factor(G_real.det())
    Ddomain = Imb - 6*Imm**2/Imt
    assertion(results, "lemma_9_4_gram_determinant", sp.simplify(detG-sp.Rational(2,3)*Imt*Ddomain)==0, {
        "determinant": str(detG),
        "factorization": str(sp.Rational(2,3)*Imt*Ddomain),
        "conclusion": "If Im(tau)>0 and D<0, determinant<0 and the real symmetric 2x2 matrix has signature (1,1).",
    })

    # ------------------------------------------------------------------
    # Logical contradiction induced by the claimed global conclusions.
    # ------------------------------------------------------------------
    assertion(results, "cdp20_numerical_contradiction", not (2 <= 0), {
        "manuscript_claim": "c3(X)=2 and X is homeomorphic/diffeomorphic to S6",
        "manuscript_claim_2": "a(X)=1 and f is a holomorphic algebraic reduction",
        "external_theorem": "CDP20 Theorem 2.2 gives c3(X)<=0 under H1=H2=0, a(X)=1, holomorphic algebraic reduction; Corollary 2.3 gives a(X)=0 for X homeomorphic to S6.",
        "formal_incompatibility": "2 <= 0 is false",
        "note": "This check records propositional incompatibility; validation of CDP20 is literature-based rather than computational.",
    })

    # Mark all checks and serialize.
    checks = [v for v in results.values() if isinstance(v, dict) and "passed" in v]
    results["summary"] = {
        "checks_run": len(checks),
        "checks_passed": sum(1 for v in checks if v["passed"]),
        "checks_failed": sum(1 for v in checks if not v["passed"]),
    }
    OUT.write_text(json.dumps(results, indent=2, default=str) + "\n", encoding="utf-8")

    lines = [
        "S6 packet 06 exact-arithmetic verification",
        "==========================================",
        f"Checks run: {results['summary']['checks_run']}",
        f"Passed:     {results['summary']['checks_passed']}",
        f"Failed:     {results['summary']['checks_failed']}",
        "",
    ]
    for key, value in results.items():
        if isinstance(value, dict) and "passed" in value:
            lines.append(f"[{'PASS' if value['passed'] else 'FAIL'}] {key}")
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
