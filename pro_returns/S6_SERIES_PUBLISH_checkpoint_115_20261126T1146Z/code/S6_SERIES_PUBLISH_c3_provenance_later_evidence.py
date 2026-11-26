#!/usr/bin/env python3
"""Write primary-source scope outcomes and the bounded integration report."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "agents/continuation3_provenance"
OUT = BASE / "later_part"
metadata = {}
for path in [
    BASE / "S6_SERIES_PUBLISH_c3_provenance_source_downloads.tsv",
    BASE / "S6_SERIES_PUBLISH_c3_provenance_image_downloads.tsv",
    BASE / "section12/S6_SERIES_PUBLISH_c3_provenance_section12_sources.tsv",
    OUT / "S6_SERIES_PUBLISH_later_source_downloads.tsv",
]:
    for row in csv.DictReader(path.open(), delimiter="\t"):
        metadata[row["key"]] = row

claims = [
 ("BierstoneMilman_v2", "arXiv:alg-geom/9508005v2",
  "§0.2(2), pp.3–4; Theorem1.6 and Remarks1.7, pp.5–6",
  "D.2.5 and D.2.6",
  "The source includes the complex analytic category and a locally finite smooth-centre embedded resolution with normal-crossing total transform. Compactness of the central divisor makes finitely many of those local blowups suffice after the base disc is shrunk. Over the punctured disc the resolution is the identity, so the same smooth fibres, markings and monodromy enter the logarithmic comparison."),
 ("CDP98", "Compositio Mathematica112 (1998),77–91",
  "Proposition1.1, p.78; Lemma1.5, pp.79–80",
  "E12, E17 and P267",
  "The embedded square-zero summand at p survives twisting by a Cartier point q away from p, with the displayed split module and cohomology. The Poincaré bundle example gives the exact derived image C0[−2], whose degree-two skyscraper has length one despite generic fibrewise vanishing. These concrete objects address the hypotheses and conclusions printed at the cited loci; E12 retains the parameter base-change exact sequence and E17 the no-embedded-component form."),
 ("LRS_v1", "arXiv:1912.09719v1,20December2019",
  "Theorem3.1 and footnote6, p.9; complete proof pp.10–14; Example3.4(2) and Lemma3.5, p.10; line following eq.(3.5), p.14",
  "Restored E2 at01GR; E17; P266 and P272",
  "Theorem3.1 establishes all-degree generic vanishing for an arbitrary vector bundle on Pic0, the index zero there, and c3=0. Tensor translation Q↦L*⊗Q with inverse L↦L*^{-1}⊗L carries the theorem for V⊗L* to every component. Example3.4(2), specialized to a smooth plane cubic, factors the exceptional contraction through that cubic and gives the length-one R1. Lemma3.5 gives the vanishing specialization without embedded components. Cartier Ext duality gives K_Y(F)|F for the sign correction."),
 ("Horikawa1974", "Journal of the Mathematical Society of Japan26(4)(1974),647–667",
  "§4, equations(4.3)–(4.5), p.649; §6, Theorem6.1 and proof, pp.660–661",
  "E6",
  "The source gives the Čech holomorphic-map obstruction and a stability criterion with H1 surjectivity and a degree-two condition. E6 uses that same cocycle map di but proves lifting of the torus source by its constant Beltrami tensors; the subsequent divisor-equation calculation identifies the restricted map obstruction with a coboundary. The receiving proof states every replacement hypothesis and map."),
 ("Douady1966_publisher", "Annales de l'Institut Fourier16(1)(1966),1–95; publisher PDF",
  "§9, Theorems1–2, pp.83–85; §10.1, Proposition1, p.86; §10.2, Theorem1, p.87",
  "E6",
  "The full analytic parameter category allows nilpotents. The source constructs the universal proper flat compact-subspace parameter and proves finite dimension, the isomorphism open locus for proper flat families, and the graph construction for holomorphic maps. E6 explicitly factors the absolute universal graph through the varying base by its unit-map calculation, then applies these results to the relative graph germ."),
 ("Buchdahl1999", "Annales de l'Institut Fourier49(1)(1999),287–302",
  "Theorem11, p.297",
  "E6",
  "The theorem gives Kählerness for a compact complex surface with even first Betti number. E6 then supplies its own Albanese degree-one and even-intersection-form argument for a surface diffeomorphic to T4; that latter conclusion is not attributed to Theorem11 alone."),
 ("ArtebaniDolgachev2009", "L'Enseignement Mathématique55(3/4)(2009),235–273",
  "§2, pp.238–241",
  "E10",
  "The source gives the Hesse pencil, nine base points, its rational elliptic-surface blowup and four triangular singular members. The receiving construction uses the explicit Möbius pullback t↦1/(t−4) to make the two critical sets disjoint, and its moving sixth branch value supplies the genus-two target deformation and obstruction."),
 ("Comb_v1", "arXiv:2610.10451v1,7October2026",
  "Theorem1.1, p.2; Theorem2.2 and proof, pp.4–5; Proposition4.1(i), pp.11–12; eq.(5.5), p.16; Proposition5.3, pp.17–18; Proposition6.1, pp.19–21; Proposition6.2, pp.22–23; Lemmas8.1–8.2 and Proposition8.3, pp.27–28; §10(1), p.33",
  "E5–E7, E15–E16 and P264",
  "The source proves degree-one cohomological flatness, the finite-cover/logarithmic period frames, the local fillings, the m≥12 construction and the dimension lower bound for the germ with all three period values fixed. Its normal-sheaf formula is 4+4c_m−2h−4r. The explicit identification c_m=2m−1,h=−2,r=3 gives8m−8. The identity on marked sections embeds that germ into the root-period germ; its differential has quotient lengths4,3,2. E15's proof constructs and checks the additional nine directions and the full8m+1 Kuranishi germ."),
 ("Two_v1", "arXiv:2609.33785v1",
  "Theorem1.1, p.2; eq.(3.1) and Proposition3.1, pp.6–7; Proposition6.4 and proof, pp.19–20",
  "E7, E13 and E16",
  "The source gives the compact bidisc construction near μ=0 and small nonzero λ, its three nodal fillings and order-four cover, and two independent invariant derivatives. E13 uses the same elliptic equation, section and labelled nodes; its full connection/residue maps compute h(T) and show that the already-constructed bidisc has invertible tangent map to the Kuranishi germ."),
 ("LR_v2", "arXiv:2609.33826v2",
  "Proposition2.1 and proof, pp.3–4; Proposition2.5, p.5; Lemma3.10, pp.11–12; Theorem5.1, p.21",
  "E7 and E14",
  "The source gives the stated Weierstrass model, section, line Hom identity, hexagonal compactification, local topological comparison and six-sphere theorem. E14's maps t_new=(27/4)(t_old^{-1}−1), x_new=x_old/t_old², y_new=y_old/t_old³ identify that exact source model with y²=x³+tx+t and transport its line and linearization. The ε-family, cusp jet map and Kuranishi calculation are then proved in the receiving text."),
 ("Log_v1", "arXiv:2610.39102v1",
  "Theorem1.1, p.1",
  "E11",
  "The construction theorem identifies the admissible coprime multiplicity data and the members with six-sphere topology. E11 retains that range. Its root morphism[x:y]↦[x^l:y^k], equivariant bundle pullbacks, scale derivative and one-dimensional Kuranishi calculation are the additional explicit computations here."),
 ("AC26", "Author PDF retrieved22November2026; SHA256 identifies version",
  "Setup/Main Theorem, p.2; Remark3.12, p.19",
  "P261, E8 and C5b",
  "The marked periods and j(τ)=1728t identify the same original family. Adjoining(μ,β/6) to its raw lattice gives the index-six inclusion; identity on C² induces the isogeny whose Lie differential and H1 pullback identify the Kodaira–Spencer tensors. The equation for j then gives the root-coordinate orders used by E8 and C5b."),
 ("AtkinGarvan2002", "arXiv:math/0208050v1,6August2002",
  "equations(3.2) and(3.5), p.8",
  "E8 and the resonance coefficient",
  "The normalized Eisenstein-series definitions and q-derivative identities give E2′=(πi/6)(E2²−E4) after d/dτ=2πi q d/dq. With g2=(4π^4/3)E4 and g3=(8π^6/27)E6 they also give the derivative at the order-three elliptic point used in the resonance proof."),
]
dlmf_loci = {
 "20_2": "eqs.20.2.1–2,20.2.6,20.2.12",
 "20_4": "eqs.20.4.3–5",
 "20_5": "eq.20.5.1",
 "20_7": "eq.20.7.5",
 "20_13": "eq.20.13.1",
 "23_3": "eq.23.3.9",
 "23_6": "eq.23.6.2",
 "23_17": "eq.23.17.8",
}
for key, locus in dlmf_loci.items():
    claims.append(("DLMF_"+key, "NIST DLMF online edition retrieved22November2026", locus,
        "E8 and E18",
        "Read the cited equation on the live primary DLMF page and its MathML expression. The conversion is ϑ_j(z,τ)=θ_j(πz|τ), q=e^{πiτ}, periods2ω1=1 and2ω3=τ. The heat equation, logarithmic product derivatives, half-period identity and positive theta constants are used with these exact scale factors."))
for page in (231,233,234,235,236,237,238,239):
    claims.append((f"Steenbrink1976_p{page}", "Inventiones Mathematicae31(1976),229–257; journal page image",
        f"p.{page}; combined loci Proposition1.13, §2.1, Theorem2.18, §2.19, Proposition2.20 and Theorem2.21",
        "D.2.3 and D.2.6",
        "Read the primary journal-page images at the used loci. The analytic proper-disc setting and full normal-crossing multiplicities give the logarithmic Gauss–Manin extension and monomial residue calculation. The receiving proof applies the same relative logarithmic quotient, identifies each branch map by subtracting its normal residue times(dt/t)/m_i, and supplies the coefficient-ideal and positive-volume arguments."))

rows=[]
for key, version, locus, owners, outcome in claims:
    m=metadata[key]
    rows.append(dict(key=key, url=m["url"], version=version, locus=locus,
        sha256=m["sha256"], bytes=m.get("bytes",""), date_utc=m.get("date_utc",""),
        owners=owners, outcome=outcome, source_content_in_checkpoint=False,
        reading="Opened exact primary locus; outcome is own mathematical paraphrase."))
with (OUT/"S6_SERIES_PUBLISH_later_sources.tsv").open("w",newline="") as f:
    w=csv.DictWriter(f,list(rows[0]),delimiter="\t");w.writeheader();w.writerows(rows)

status=json.loads((OUT/"S6_SERIES_PUBLISH_later_status.json").read_text())
report = """# Paper II: later-period and deformation part

## Receiving text and admission

The complete receiving fragment is S6_SERIES_PUBLISH_later_part_proposed.tex.
It replaces the old sections sec:II:12, sec:II:13 and sec:II:14 as a unit,
then belongs after the Euler-sign development. It includes the previously
prepared section12 edits and the further edits in S6_SERIES_PUBLISH_later_defects.tsv.
Do not also insert the earlier section12 proposal or a second E8 block.
All main/shared files remain untouched by this agent.

The section12 instance rows and thirteen exposed comparisons remain in
../section12/. The later instance rows and exposed comparisons are separate;
their events are editorial/proof comparisons, not independent checks.
All original labels and permanent targets in the three bounded sections
are preserved exactly once. E2 is restored at the existing tag01GR.
The two outside statement guards identify E.5.2 and E.5.3 exactly.
Neither statement is part of a replacement fragment. No direct P4R.13 or
P4.40 use occurs in the original or receiving bounded text.

## Complete internal order

1. Tangent cohomology: global finite-fibre tests; the full persistent
   normalization-pullback lemma; normalization criteria; hexagonal models;
   the branch-normal quotient; marked Picard coordinate; the complete E8
   theta determinant; integral and nonintegral resonance; jump loci.
2. Trivial monodromy: component count and logarithmic period obstruction;
   Euler upper bound; general Euler equality; its normal-crossing corollary;
   extension of periods; extended groups/Albanese-map comparison; coherent
   and integral cohomology of the compact example.
3. Fibration stability: the Leray boundary; the complete Artin and analytic
   graph lifting proof; applications to the constructed families; the
   concrete fixed-genus-two-target obstruction.
4. Explicit deformations: coprime logarithmic transforms; the two-parameter
   germ; the Liu–Rollenske transverse family; the positive-comb germ; the
   exact inclusion of the published fixed-period-value germ.
5. Rank divisors and theta comparisons: family rank divisors, followed by
   the elliptic-half-period example.
6. Direct images and divisor vanishing: the cited non-holomorphic theorem;
   the Poincaré torsion direct image; divisor stabilization and graph fibres;
   the embedded-point example; pencil exceptional thickenings; elliptic
   exceptional higher image; full-Cartier adjunction.

E8 precedes C5b/C5c because its explicit degree-six isogeny identifies the
Kodaira–Spencer tensors. Evaluating the weighted matrix at the cusp and
the order-three point proves ab≠0 and c0≠0 where those constants are used.
E13 precedes E14 and E15, whose maps and bundles precede E16. The complete
E8 proof travels with its original tag and equation target.

For global integration, the outside sec:II:combs owners inv:E2.2 and
inv:E2.5 use E15 and its bundle formulas and should follow explicit
deformations in this later part. The final splitting problem follows them.
The current irreducible-cluster reference from C.2.IRR.1 to C4e was reported
to root, who owns that cluster and the global sign-theorem placement.
These outside regions have not been edited here.

## Mathematical comparisons and corrections

E2 has the full compendium statement, now with its primary theorem owner.
LRS Theorem3.1 proves the Pic0 result for an arbitrary vector bundle. For
each component, Q↦L*⊗Q has inverse L↦L*^{-1}⊗L; applying the source theorem
to V⊗L* identifies every cohomology group and Euler index with the desired
one. This retains the full scope without repeating its known graph proof.

The normal-crossing equality is the identity-map specialization of D.2.2
on the same Y, base and full fibres. Its old two-step proof is represented
in the exact defect row, while the narrower corollary and realization
remain in the receiving text.

The comb comparison is an explicit inclusion of parameter germs, identity
on marked sections. Coarse descent is its inverse on the image. The
normal-sheaf quotient has lengths4,3,2. The opened source dimension formula
4+4c_m−2h−4r, with c_m=2m−1,h=−2,r=3, gives8m−8. Its H1 vanishing gives the
exact nine-dimensional tangent quotient and total dimension8m+1.

The pencil-divisor lemma retains the full evaluation-sequence proof:
pullback and the projection formula give R2 O(−tE)=0; the divisor sequence
gives R1/R2 O_tE=0; its image has dimension at most one, so H2(tE,σ*W)=0.
The exceptional elliptic example uses the exact composition S=P(N_C)→C→p.
The embedded-point example retains the local ring and all cohomology
groups. Cartier Ext duality proves the plus sign in K_Y(F)|F, including
nonreduced full fibres, and locates the published sign error precisely.

Every other proof in sections13–14 is carried in full. The comparison
events name the actual maps, filtrations and cohomology steps read.
The source-scope TSV identifies URLs, versions, exact loci, hashes and
own paraphrases; no published source bytes are included.

## Remaining integration gates

Root admits the fragments and rows, updates §1.6 and global placement,
regenerates the series references, renders and reads the final pages, and
computes the final event/text counts. This work makes no claim that those
global or rendered gates have already been completed.

The separate pending source proposals139–141 are the four canonical
normalization-program appendix rows and the Reid/Teleman edition
identifications. The earlier source edits001–134 were acknowledged as
admitted; the deposit-only edits135–138 remain deferred to the final state.
"""
report += "\n## Local proposal status\n\n" + "\n".join([
    "- Exact later edit rows: "+str(status["edit_rows"])+".",
    "- Complete receiving comparison: "+str(status["comparison_completed"])+".",
    "- Exposed later comparison events: "+str(status["exposed_comparison_events"])+".",
    "- Whole receiving fragment SHA256: "+status["receiving_part_sha256"]+".",
    "- New tags: P264–P272; earlier P261–P263 remain in section12; restored tag01GR.",
    "- Unused reserved tags: P273–P280.",
]) + "\n"
(OUT/"S6_SERIES_PUBLISH_later_report.md").write_text(report)
print("Wrote "+str(len(rows))+" primary-scope rows and bounded integration report.")
