"""Persist root's post-checkpoint-10 mathematical audits and one new exact check.

The proof reviews described here are human-readable records of the root
agent's checks, not claims that the Python assertions prove the geometry.
"""
from pathlib import Path
import datetime
import hashlib
import json
import manifolds_general_initial as G

ROOT = Path(__file__).resolve().parents[1]


def file_hash(relative):
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


info = G.PROFILES[(49, "II")]
result = G.compute(49, "II", 3, 2,
                   [0] * len(info["kodaira_types"]) + [1], e=1)
assert result["fundamental_group"]["vertical_quotient"] == {
    "free": 0, "torsion": [2, 2]}
assert result["homology"][1] == {"free": 0, "torsion": [3, 27]}
assert result["homology"][2] == {"free": 0, "torsion": [54]}
assert result["homology"][3] == {"free": 2, "torsion": [54]}
(ROOT / "records/root_general_initial_exception_3_2.json").write_text(
    json.dumps(result, indent=2, default=int) + "\n")

proofs = [
    "sections/fourfolds_D2_critical_frame.tex",
    "sections/fourfolds_D2_remaining_even.tex",
    "code/manifolds_general_initial_proof.tex",
    "code/root_critical_link_refined_P_proof.tex",
    "code/maps_D2_frame_proof.tex",
    "code/maps_D2_finite_generator_frame.tex",
]
audit = {
    "updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "source_hashes_at_review": {p: file_hash(p) for p in proofs},
    "D.2.44": {
        "decision": "PASS: approved for registration",
        "scope": "Seven default semistable minimal patterns, ordinary clutch e=+1 or -1, primitive Mumford caps, no extra regular logarithms.",
        "primary_checks": [
            "Brown72 printed369-372: root visually read Lemma1.2, F(u,v), Theorem1.7, Cor1.11, Cor1.13 and Hopf-invariant remark.",
            "Kaplan79 correct27-page original scan: root opened theorem and full proof pp243-246, Def1.7/Remark1.8 p239, relative w2 p240, intro0/2-handle statement p237.",
            "Zhubr13 Theorem1 p6 permits any specified embedded basis of Tor2 H3; root reread exact statement and p1=4o4.",
            "Zhubr75 primary opened again: Theorem3 pp795, natural P definition and Theorem5 p796; complete invariant recognition retained.",
        ],
        "geometry": "Unit Bott obstruction, abstract df kernel and nonzero delta section, flat-reference H3 comparison, Brown PT naturality and sphere parity, rank3 secondary-obstruction vanishing, exact marked critical-cycle lifts, unique-framed surgery models all independently reviewed.",
        "exact_replays": "Root reran all14 critical-cycle rows and the independent local/AH degree certificate: all passed.",
        "peer_review": "records/maps_D44_peer_audit.md",
    },
    "D.2.45": {
        "decision": "PASS: approved for registration",
        "scope": "All11 remaining minimal residual4/8/20 patterns, including every free II-log order6k, integer ordinary clutch e, and affine r,n with n-me=+/-1.",
        "geometry": "Full proof independently checked: originalII Jacobian multiplicity2, corrected-good-log empty critical scheme, actual relative spin characteristic identity, preferred full-generator core character including its nonzero root-loop value, literal all-parameter delta Thom relation, complete fundamental-class invariant and coprime spin-bordism splitting.",
        "exact_replays": {
            "full_Smith_and_symbolic": "records/root_extended_critical_cycles_audit.out",
            "auxiliary_line": "records/root_remaining_AH_audit.out",
            "local_II": "records/root_II_frame_checks_audit.out",
        },
        "counts": {"full_Smith_cases": 158, "unbounded_integral_chain_certificates": 11,
                   "all_remaining_minimal_patterns": 18, "initial_rows": 14,
                   "semicharacter_checks": 1056, "adapted_matrices": 62,
                   "symbolic_finite_rows": 4, "original_II_rows": 4},
        "consequence": "All162 specified minimal simply connected patterns are classified; broader D2 remains open.",
    },
    "D.2.46": {
        "decision": "PASS: approved after replacing the artificial20-step closure cap by HNF stabilization",
        "scope": "Compatible positive initial pairs, arbitrary effective whole-fibre weights on multiplicative/regular sites, original stars; general vertical modifications and star logs excluded.",
        "geometry": "Direct Poincare lift integrality/product, primitive Chern-vector comparison without component-generator assumption, nonsaturated general-cusp boundary torsion, exact relative H2 extension and duality checked.",
        "exact_replay_output": "records/root_general_initial_audit.out",
        "counts": {"exhaustive_residues": 284, "local_projected_lines": 912,
                   "elliptic_unit_certificates": 21, "D41_overlaps": 90,
                   "broader_full_Smith_examples": 148},
        "independent_exception": "OS49/II P3G,Q2G (b not divisible by6), all zeros regular, both finite caps: residual vertical Klein four; H1=Z/3 plus Z/27,H2=Z/54,H3=Z^2 plus Z/54.",
    },
    "relative_critical_link_lemma": {
        "decision": "Proof independently passed maps and fourfolds; available as input to D.2.45, no separate numbered claim yet.",
        "main_identity": "-B.C=2q+ord(N)k with k even, using actual relative spin classes and a sphere-first Kaplan construction.",
        "scope": "N need only generate the two-primary projection; its actual order is used. The actual rational link is divided before reduction, never an even cyclic residue.",
    },
}
(ROOT / "records/root_completion_audit11.json").write_text(
    json.dumps(audit, indent=2) + "\n")
print("PASS: OS49/II P3G,Q2G exception, including exact H1,H2,H3.")
print("PASS: D44, D45 and D46 root proof/source/replay audits saved.")
print("PASS: relative critical-link lemma has two independent geometric reviews.")
