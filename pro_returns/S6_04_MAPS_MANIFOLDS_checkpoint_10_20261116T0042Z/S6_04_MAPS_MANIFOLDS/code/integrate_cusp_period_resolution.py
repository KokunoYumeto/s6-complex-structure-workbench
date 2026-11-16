"""Integrate the audited bounded-cusp theorem and original additive fillings."""
from pathlib import Path
import datetime
import json

root = Path(__file__).resolve().parents[1]
report_path = root / "S6_04_MAPS_MANIFOLDS_report.md"
report = report_path.read_text()
report = report.replace("| D.2 | D.2.1–D.2.15 |", "| D.2 | D.2.1–D.2.17 |")
report = report.replace(
    "| F.3 | F.3.1–F.3.9 | Undecided only in compactification scope: explicit nonselfdual tuple compactified; an explicit LSAP/Oka-1 proof now realizes every oriented rank-six monodromy by nondegenerate holomorphic periods on the open base; finite-fibre extension and bounded cusp correction remain to be decided for all data |",
    "| F.3 | F.3.1–F.3.11 | (a): every surviving datum has nondegenerate holomorphic periods on the punctured sphere with a bounded holomorphic cusp correction and any prescribed finite cusp jet; the explicit tuple also has all finite extensions. No universal simultaneous finite-good-reduction assertion is made |"
)
report = report.replace(
    "Full simultaneous conjugacy under the cusp centralizer, all twist choices and the remaining period data are still unbounded; these necessary conditions do not substitute for that classification.",
    "Full simultaneous conjugacy under the cusp centralizer and all twist choices remain unclassified; these necessary conditions do not substitute for that classification. The universal bounded-cusp period question has now been resolved by F.3.8–F.3.11 below."
)
report += """

## Resolution of the stated F.3 period question

F.3.10 supplies the needed extension argument, with its proof written out. The period bundle is placed inside the Grassmannian of the logarithmic extension of the flat vector bundle. At the cusp, the affine chart of all bounded correction matrices C is adjoined. This is an open complex manifold over the base: in the original flat frame the imaginary part is yI+Im(C), where y=−log|t|/(2π), and it has positive determinant uniformly for bounded C near t=0. The cusp is therefore an interior point of a holomorphic submersion.

Keep that point and remove the finite-monodromy points, so the base remains an open Riemann surface. Begin with any desired polynomial jet of C on a small Runge cusp disc. The period domain is simply connected, which supplies a continuous extension. The exhaustion attaches new discs and arcs away from the cusp. Cartan-A generators of End(V) vanishing to the prescribed jet order give explicit vertical exponential sprays on the old compact set; they need dominate only on the attaching intersections. The Alarcón–Forstnerič LSAP gluing applies there, and the critical arc step is their Mergelyan theorem in a trivialized Grassmannian bundle. Summable approximation errors preserve the open period condition and holomorphicity at the retained cusp. Hence the limit has Z=(log t)/(2πi)I+C(t), with C holomorphic at zero.

This proves F.3.11 for every oriented rank-six local system with a maximal square-zero cusp, and therefore for every topological survivor of F.2, independently of the unresolved integral classification. Nondegeneracy means real transversality, equivalently a nondegenerate imaginary part in each normalized period chart. Root and the maps agent independently audited the whole argument against the primary approximation theorem, including the changing cusp fibre and jet-preserving spray gluing; both passed.

F.3 asks for periods over the punctured sphere and a bounded cusp correction. These specified conditions are now settled. Simultaneous good reduction at every other puncture is a stronger condition that this open-base proof does not assert. The compact example in F.4 already has those finite extensions by its separate explicit construction. We do not impose that additional universal condition as a new requirement for the stated F.3 period decision.

## Further original additive fillings

D.2.16 and D.2.17 retain the original odd-star fibres in four marked profiles and allow every free logarithmic transform at a regular fibre. Additive section logarithms reduce the local translation to a genuine order-four torsion section, so the fill is S1 times the mapping torus of its component action. This computes its free local defect and, through the actual two circle sweeps of the section disc, its full integral boundary kernel. The additional original II and IV fills have no defect. The same unrestricted normal-matrix formula as D.2.13 then applies.

For n=±1 the oriented smooth type is #^b(S2×S4)#^b(S3×S3)#tildeSigma0(N_m), with b=2 for the OS46 profiles and b=1 for the OS50 profiles treated there. The proof retains the twisted suspension framing and uses repeated Galaz-García–Reiser Theorem A, followed by cancellation using the complete Zhubr invariants. Root checked the local exponential and torsion-section statements directly in Ulmer–Urzúa and the translation extension in Schütt–Shioda, and independently reran1,462 full Smith matrices for each theorem, including194 n=0 cases in each. This is still a specified-family result; it does not exhaust every divisor pair of sections, every zero location, or every filling choice requested by D.2.
"""
report_path.write_text(report)

audit_path = root / "records/root_audit_checkpoint04_progress.json"
audit = json.loads(audit_path.read_text())
audit["reviewed_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
audit["statements"].update({
    "D.2.16": "Passed: primary UU21 Section2.4 equation2.2 and Proposition3.5(1),(3) opened, including additive period stalkzero and orderfour invariant Betti leaf; SS10 Sections7.6-7.7 opened for translation extension. Local logarithm and rigidified line deformation preserve meridian and fixed periods. Component permutation, full primitive circle-sweep kernel, PL free defect and all-order residual matrix checked. Root independently reran1462 full14x15 Smiths including194 n=0. Repeated GR TheoremA/B(2) and full Zhubr cancellation verify the exact framed smooth types.",
    "D.2.17": "Passed: original II fill EII timesT2 and original IV fill S1 times orderthree translation mapping torus each have one component orbit and zero free defect. Actual primitive fixed loops, both boundary Wang groups, PL surjectivity, primitive ranknine global kernel and all-order normal map checked. Root independently reran1462 full10x11 Smiths including194 n=0. The same spin free-circle surgery and full smooth classification apply.",
    "F.3.10": "Passed independently by root and maps: the open Grassmannian projection is a holomorphic submersion at the added point; Cartan-A ideal endomorphisms give explicit exponential vertical sprays, with domination only on the attaching intersections. Primary AF Lemma5.1 equations5.6-5.8 and Theorem2.13 finite-jet Mergelyan statement opened directly. All bumps avoid the retained point, critical arcs preserve the base after holomorphic vector-bundle trivialization, and controlled summable errors preserve the open target and jets. No Serre-fibration claim at the changing fibre is used.",
    "F.3.11": "Passed independently by root and maps: logarithmic frame sign, primitive integral marking, choice of period component, openness of the adjoined affine cusp chart, continuous relative extension using pi1(D3)=0 and Runge cusp disc checked. F.3.10 yields C holomorphic at the retained cusp and hence bounded, with arbitrary finite jet. This resolves the exact F.3 period clause; universal finite good reduction is expressly not asserted."
})
audit_path.write_text(json.dumps(audit, indent=2) + "\n")
print("F.3 resolved as stated; D.2.16–17 audited. Four prompt-item scopes remain open.")
