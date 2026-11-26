#!/usr/bin/env python3
"""Prepare Paper II provenance proposals, without modifying shared paper files.

The old/new rows preserve the source read in this continuation.  The deposit
draft deliberately retains the previously recorded check totals; root must
recompute those totals once, on the text-final CHECK_EVENTS state.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
OUT = ROOT / "agents" / "continuation3_provenance"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = ROOT / "S6_SERIES_PUBLISH_II.tex"
paper = SOURCE.read_text()
deposit_path = ROOT / "S6_SERIES_PUBLISH_deposit_fields_II.json"
deposit = json.loads(deposit_path.read_text())
RECORDS = "https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii"
PROMPT = ROOT.parents[1] / "upload" / "PROMPT(20261122-165446).md"
now = datetime.now(timezone.utc).isoformat()

def write_tsv(name, rows, fields=None):
    fields = fields or list(rows[0])
    with (OUT / name).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

edits = []
def edit(number, typ, label, location, old, new, reason, document="S6_SERIES_PUBLISH_II.tex"):
    if document == "S6_SERIES_PUBLISH_II.tex":
        assert paper.count(old) == 1, (number, paper.count(old), old)
    edits.append(dict(change_id=f"II-C3-PROV-{number:03d}", type=typ,
        statement_id=label, old_location=f"{document}: {location}", old_page="final page binding by root",
        new_location=f"{document}: {location}", new_page="text-final PDF",
        old_text=old, new_text=new, reason=reason,
        review_status="exact proposal; parent integration and rendered-page reading pending"))

old = r"""\textit{Relation to literature.} The comb germ, open twelve-tooth
Hodge values and ordered-pair deformation classes answer the stated
questions in \cite[Section~10(1)--(2), p.~33]{Viaclovsky2026Combs}
and \cite[Section~1.1(1), p.~2]{Viaclovsky2026Log}, and the
vector-field value corrects \cite[Corollary~1.3, preprint p.~2]{HKP2000}."""
new = r"""\textit{Relation to literature.} The comb germ answers
\cite[Section~10(1), p.~33]{Viaclovsky2026Combs}; the Hodge values
address its Section~10(2) for the stated open twelve-tooth family.
The ordered-pair deformation classes answer
\cite[Section~1.1(1), p.~2]{Viaclovsky2026Log}, and the vector-field
value corrects \cite[Corollary~1.3, preprint p.~2]{HKP2000}."""
edit(129, "D18", "series:II:F", "1.2, Theorem F literature status", old, new,
     "The opened Combs question asks for the full Hodge diamond and variation for all constructed m; the theorem proves the stated open m=12 values. Separate that scope from its complete Kuranishi answer.")
old = r"""\cite[Theorem~1.1, p.~2]{Viaclovsky2026Combs}; comb germ and open
twelve-tooth Hodge values answer \cite[Section~10(1)--(2), p.~33]{Viaclovsky2026Combs};
ordered-pair separation refines \cite[Theorem~1.1, p.~1]{Viaclovsky2026Log}"""
new = r"""\cite[Theorem~1.1, p.~2]{Viaclovsky2026Combs}; comb germ answers
\cite[Section~10(1), p.~33]{Viaclovsky2026Combs}; the Hodge values
address its Section~10(2) for the stated open twelve-tooth family;
ordered-pair separation refines \cite[Theorem~1.1, p.~1]{Viaclovsky2026Log}"""
edit(130, "D18", "series:II:F", "1.4, F row", old, new,
     "Apply the same exact open-family Hodge scope to the known-and-new table.")
old = r"""untwisted tuple is \cite[Theorem~6.12, pp.~81--82]{DGKXv1}."""
new = r"""untwisted tuple is \cite[Theorem~6.12, pp.~81--82]{DGKXv1},
arXiv version~1."""
edit(131, "D18", "series:II:E", "1.2, Theorem E literature status", old, new,
     "The exact tuple is present in v1; the current v2 is a substantially shorter Oka paper. The versioned primary citation must remain explicit.")
old = r"""\cite[Theorem~6.12, pp.~81--82]{DGKXv1}.\\"""
new = r"""\cite[Theorem~6.12, pp.~81--82]{DGKXv1}, arXiv version~1.\\"""
edit(132, "D18", "series:II:E", "1.4, E row", old, new,
     "Identify the actual opened edition in the compact status table as well.")
old = r"""\newblock URL \url{https://arxiv.org/abs/2609.38442}."""
new = r"""\newblock URL \url{https://arxiv.org/abs/2609.38442v1}."""
edit(133, "D18", "Engel2026", "bibliography", old, new,
     "The edition stated in the bibliography and opened at Proposition 7.1 is v1; make its URL resolve to that edition.")

old = r"""Claude Fable 5.2 (Anthropic), at effort high and at effort max,
and Claude Opus 5.5 (Anthropic), at effort max, undertook readings,
intakes, checks and recomputations on 12--20 November 2026.
Their objections and calculations were compared with the statements,
proofs and cited sources, and the resulting corrections were
incorporated into the text. The records specify the passages and
calculations examined by each model."""
new = r"""Claude Fable 5.2 (Anthropic), at effort high and at effort max,
and Claude Opus 5.5 (Anthropic), at effort max, undertook readings,
intakes, checks and recomputations on 12--20 November 2026.
Within the series, Claude Opus 5.5 also rewrote Paper~V's abstract
and \S1 on 20 November and read Paper~I in full on 21--22 November.
On 22 November it corrected two accents and one family index in
Paper~I and updated its records links. Their objections and
calculations were compared with the statements, proofs and cited
sources, and the resulting corrections were incorporated into the
text. The records specify the passages and calculations examined
by each model."""
edit(134, "D15", "methodology", "1.5, model contributions", old, new,
     "The controlling third-continuation prompt section 4.1 adds Opus's Paper V front-matter revision and full Paper I reading/deposit corrections. This credits those series contributions without assigning an independent proof derivation to a complete-text reading.")

draft = dict(deposit)
old_comments = deposit["comments"]
tail = "Programs and check records accompany the source bundle. The final records folder and pinned commit will be set at deposit."
assert old_comments.count(tail) == 1
new_comments = old_comments.replace(tail, "The programs and check records are available at " + RECORDS + ".")
draft["comments"] = new_comments
edit(135, "D15", "deposit:II:comments", "comments", old_comments, new_comments,
     "Hexagon receives TeX alone. Replace the source-bundle assertion and future folder placeholder with the one standing records-page address.", deposit_path.name)

old_provenance = deposit["provenance"]
new_provenance = old_provenance.replace(
    "Text: AI-authored; none of it was written by a human.",
    "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.", 1)
production_old = "Claude Fable 5.2 (Anthropic), at effort high and at effort max, and Claude Opus 5.5 (Anthropic), at effort max, undertook readings, intakes, checks and recomputations on 12–20 November 2026."
production_new = production_old + " Within the series, Claude Opus 5.5 also rewrote Paper V's abstract and Section 1 on 20 November and read Paper I in full on 21–22 November. On 22 November it corrected two accents and one family index in Paper I and updated its records links."
assert production_old in new_provenance
new_provenance = new_provenance.replace(production_old, production_new, 1)
records_start = new_provenance.index("Records. ")
new_provenance = new_provenance[:records_start] + (
    "Records. The programs and check records are available at " + RECORDS + ". "
    "The text, programs and check records are dedicated to the public domain under CC0 1.0 Universal "
    "(https://creativecommons.org/publicdomain/zero/1.0/).")
draft["provenance"] = new_provenance
edit(136, "D15", "deposit:II:provenance", "provenance", old_provenance, new_provenance,
     "Insert the required responsibility sentence, add the newly documented model contributions, and replace both historical repository links and the source-bundle assertion. Previously recorded check totals are deliberately unchanged pending the root text-final recomputation.", deposit_path.name)
for number, label, location, old_value, new_value in [
    (137, "deposit:II:comments", "Paper II / Comments", old_comments, new_comments),
    (138, "deposit:II:provenance", "Paper II / Provenance", old_provenance, new_provenance)]:
    md = (ROOT / "S6_SERIES_PUBLISH_deposit_fields.md").read_text()
    assert md.count(old_value) == 1
    edit(number, "D15", label, location, old_value, new_value,
         "Keep the Markdown Paper II deposit block synchronized with the proposed JSON fields; final check counts remain a root text-final operation.", "S6_SERIES_PUBLISH_deposit_fields.md")

write_tsv("S6_SERIES_PUBLISH_c3_provenance_text_edits.tsv", edits)
(OUT / "S6_SERIES_PUBLISH_deposit_fields_II_proposed.json").write_text(json.dumps(draft, ensure_ascii=False, indent=2) + "\n")

downloads = {r["key"]: r for r in csv.DictReader((OUT / "S6_SERIES_PUBLISH_c3_provenance_source_downloads.tsv").open(), delimiter="\t")}
images = {r["key"]: r for r in csv.DictReader((OUT / "S6_SERIES_PUBLISH_c3_provenance_image_downloads.tsv").open(), delimiter="\t")}
readings = []
def reading(claim, main, sources, loci, established, relation, outcome, action="retain exact scoped credit"):
    refs = []
    for key in sources:
        r = downloads.get(key) or images[key]
        refs.append((key, r["url"], r["sha256"]))
    readings.append(dict(claim_id=claim, main_theorem=main, date_utc=now,
        source_keys="; ".join(sources), urls="; ".join(x[1] for x in refs),
        source_sha256="; ".join(x[0]+":"+x[2] for x in refs),
        exact_loci=loci, established_scope=established, mathematical_relation=relation,
        outcome=outcome, proposed_action=action,
        reading_kind="opened primary source; exposed source comparison; no independent derivation credit"))

reading("II-C3-LIT-A1", "A", ["AC26", "CDP2020"],
    "AC26 Lemma 10.3 pp.87–88, Theorem 10.5 pp.88–89, Corollary 10.6 p.89, §10.4 pp.89–90; CDP2020 Theorem 2.2 and Proposition 2.4 p.680, reduction preceding (11) p.692",
    "AC26 constructs a nonzero ambient cotangent section on its normal-crossings cusp fibre from a trivialized pullback to the normalization. Its image in the intrinsic cotangent sheaf is torsion. The same construction gives nonzero top tangent direct image for every twist and nonzero global H2 for general twists. CDP2020 asserts generic tangent vanishing outside degree one, nonpositive index and nonpositive c3 under integral H1=H2=0 and holomorphic algebraic reduction of dimension one.",
    "The two exact sequences for K=ker(V→ΩS/torsion) identify the surviving section space with ker δ once the endpoint sections vanish. On the AC cusp, the dg-induced section maps to the torsion term, so it realizes the same omitted kernel. The theorem's normalization-Picard map specializes to zero because the cusp normalization is rational and ambient line bundles are topologically trivial.",
    "The status correctly credits the prior counterexample and identifies the present criterion as its general normalization-map formulation. The exact erroneous proof locus is CDP2020 p.692; the theorem-level correction is p.680.")
reading("II-C3-LIT-A2", "A", ["CDP98"],
    "CDP98 Proposition 1.1 p.78; Lemma 1.5 pp.79–80",
    "Proposition 1.1 treats eventual disappearance of sections after negative divisor twists on compact complex spaces. Lemma 1.5 asserts local freeness of all higher direct images after lower direct images vanish on a base curve.",
    "For the direct-image counterexample, the normalized Poincaré bundle on E×E and O(-2) on P1 give Rg*=C0[-2], so g*=R1g*=0 but R2g* has length one at 0. For divisor twisting, a component disjoint from the divisor retains its section module; the corrected disappearance assertion uses the associated-component support condition stated in A.",
    "The two concrete source corrections and page references remain accurate; no broader invalidation of the papers is asserted.")
reading("II-C3-LIT-A3", "A", ["CDP2020"],
    "CDP2020 Proposition 7.3 and proof pp.693–695",
    "The result concerns vanishing of sections of the torsion-free intrinsic cotangent quotient on singular irreducible fibres. Its proof uses normalization, conductor and resolution data.",
    "For a unitary local system A_r associated to a transgression twist L_r, differences of continuous local primitives, holomorphic after pullback to the normalization, define the injection H0(S,(ΩS/torsion)⊗L_r)→H1(S,A_r) of A.4.7. The local-coefficient calculations and fibre-neighbourhood maps in A.4.9 make the target zero for irrational r on every reduced support; proper semicontinuity gives the generic conclusion of CDP Proposition 7.3. The ambient cotangent sequence retains the additional K/N*=torsion term displayed in A.",
    "The table's claim that A.4.9 proves the torsion-free conclusion is supported at the cited locus. The ambient-vanishing correction remains specifically attached to the p.692 reduction.")
reading("II-C3-LIT-B1", "B", ["AC26", "CDP98", "CDP2020"],
    "AC26 §10.5 pp.90–91 (Lemma 10.7 and component formula); CDP98 Lemma 3.2 p.84; CDP2020 Lemma 4.2 p.684",
    "AC26 replaces the fibre H1 summand in the abelianization of the split fundamental-group extension by its monodromy coinvariants and obtains r=2g+s−1+t′−b1. The cited CDP component formulas use the full first Betti number of the smooth fibre.",
    "The map K⋊Q→K_ab,Q⊕Q_ab sends (k,q) to ([k],[q]); its kernel is generated by fibre commutators and k−1qkq−1. This identifies t′ with the rational rank in B. The integral refinement applies the pair-duality lattice sequence under H1(Y,Z)=H2(Y,Z)=0, giving a free integral coinvariant quotient.",
    "Retain explicit prior credit for the rational formula and internal references for the integral result. The new arithmetic formula is an integral refinement of the displayed prior quotient map.")
reading("II-C3-LIT-B2", "B", ["CDP2020", "Yang_v1"],
    "CDP2020 §4, Lemmas 4.1–4.3 and proof pp.684–685; Yang v1 Theorem 1.2 and Corollary 1.3 p.4",
    "CDP2020 obtains the fibre Chern-class restrictions using the tangent sequence and surface classification under integral ambient vanishing, then invokes its H1 assertion to restrict surface types. Yang gives compact examples with b2=r−1 and a=1, hence r=1 supplies b1=b2=0 torus-fibred examples.",
    "The sequence 0→TF→TY|F→O_F→0 gives K_F=K_Y|F and c2(F)=c2(Y)|F. Rational ambient H2,H4 vanish in B; H4(F,Z) has no torsion, so c2(F)=0. The very-general terminal list is obtained by the specifically linked exclusions and compact realizations C.3.6–C.3.12 and D.2.7; it is not inferred from a failure of the CDP integral splitting.",
    "The current B wording accurately retains its rational hypothesis and links the complete classification proof; no categorical separation or blanket novelty claim is added.")
reading("II-C3-LIT-C1", "C", ["AC26", "Engel_v1", "Yang_v1"],
    "AC26 Theorem 7.22 p.60; Engel v1 Proposition 7.1 p.17; Yang v1 Theorem 1.2 and Corollary 1.3 p.4",
    "AC26 and Engel compute Euler number two for the standard compact family using the strata of the singular toric fibre. Yang's r=1 compact examples also have b1=b2=0 and Euler number two, with rational central normalization.",
    "For the normal-crossings reduced fibre the inclusion–exclusion formula is the alternating sum of the normalization, double curves and triple points. In the standard hexagonal quotient the surviving contribution is the two triple points. Substitution gives the e=2 case of C. The general sign/equality theorem is proved by the current component, conductor and monodromy arguments under the explicitly stated global Betti assumptions.",
    "Retain the exact standard-family credit. Yang is documented as a further overlapping example with the explicit r=1 specialization, without claiming a separate mathematical category.")
reading("II-C3-LIT-C2", "C", ["Steenbrink1976_p233", "Steenbrink1976_p234", "Steenbrink1976_p237", "Steenbrink1976_p238", "Steenbrink1976_p239"],
    "Steenbrink §2.1 p.234; Theorem 2.18 pp.237–238; §2.19 and Proposition 2.20 pp.238–239; Theorem 2.21 p.239; Proposition 1.13 pp.233–234",
    "Section 2 assumes a proper holomorphic map from a connected complex manifold to a disc, smooth over the punctured disc, whose central divisor has normal crossings. Positive component multiplicities are included. Relative logarithmic hypercohomology is locally free with base change; its Gauss–Manin residue has eigenvalues in [0,1), and monodromy is exp(−2πi Res). The local relative complex is computed by monomial Koszul operators.",
    "The paper's K• is the source relative logarithmic complex with the same dt/t quotient. Its coefficient ideal J/(t) retains monomials y^a for 1≤a<gcd(m_i), giving nonzero residue eigenvalues a/gcd(m_i). Inclusion J/(t)→O/(t) intertwines the residue maps. Identity monodromy makes the ambient residue zero, so the image on hypercohomology vanishes. These are the actual maps used in D.2.3.",
    "The cited analytic source supports the unrestricted multiplicity and non-Kähler setup used here. The full D.2.3 proof was reread after exposure; this supplies source-scope verification, not independent proof credit.")
reading("II-C3-LIT-D1", "D", ["Kamenova"],
    "Kamenova, Degenerations of two-dimensional tori, pp.1–4, especially Theorem 3.1 p.2 and the assumptions in §1 p.1",
    "The paper classifies semistable degenerations of two-dimensional complex tori with Kähler total space and trivial canonical bundle, obtaining smooth tori, elliptic-ruled configurations and rational-component configurations.",
    "Its proper semistable threefold map is an instance of D's local proper holomorphic torus family, by keeping the same map and underlying reduced fibre. D's pair-duality/Wang proof applies to that instance. The present modification formula follows from e(Bl_Z X)−e(X)=(codim Z−1)e(Z): a point in a threefold contributes 2 and a genus-three plane quartic contributes −4.",
    "The opened source gives this concrete overlapping subclass. D's stated local parity and integer-realization assertions are supported by the paper's full proof; the status line makes no universal absence claim about earlier mathematics.")
reading("II-C3-LIT-E1", "E", ["AC26", "DGKX_v1", "DGKX_v2"],
    "AC26 Theorem 10.5 and Corollary 10.6 pp.88–89; DGKX v1 Lemma 6.11 and Theorem 6.12 pp.81–82; current DGKX v2 title/contents and its 30-page scope",
    "AC26 proves the generic H2 nonvanishing and index one for the standard family. DGKX v1 computes the untwisted tangent tuple (1,1,1,0). Its normalization exact sequence compares sections on the normalization and conductor. The current v2 is titled Oka Geometry of Complex Six-Spheres and has a different, shorter scope.",
    "Setting n=0 in E yields exactly (1,1,1,0). The normalization restriction map in E is computed for every integral twist and the nonintegral resonance set, with the same branch-to-conductor restriction operation made explicit by the theta matrices. Thus the n=0 assertion is credited directly to v1, while the all-twist ranks are stated with their explicit formulas.",
    "Retain v1 as the mathematical source and print version 1 in the two status loci. Do not silently redirect its theorem citation to v2.", "admit II-C3-PROV-131 and 132")
reading("II-C3-LIT-F1", "F", ["Two_v1", "LR_v2", "Comb_v1"],
    "Viaclovsky Two v1 Theorem 1.1 p.2; Liu–Rollenske v2 Theorem 5.1 p.21; Viaclovsky Combs v1 Theorem 1.1 p.2 and §10(1) p.33",
    "The two-parameter paper constructs its family and exhibits two deformation directions. Liu–Rollenske identifies its constructed smooth threefold with S6. Combs constructs the m≥12 families, gives h0,1=2m+1, h0,2=2m and a local Kuranishi dimension lower bound 8m−8, and asks for the full germ and fibration persistence.",
    "F's computed tangent tuple gives h1(T)=8m+1. Its local period-section map realizes the entire tangent space and the proof establishes a smooth reduced germ of that dimension. For the two small-scale families the same map realizes h1(T)=2, and the second Liu–Rollenske direction changes the cusp into two nodal fibres. These are the actual deformation maps extending the cited constructed families.",
    "The full comb-germ and fibration-persistence assertion answers the specifically cited deformation question; retain the construction credits.")
reading("II-C3-LIT-F2", "F", ["Comb_v1"],
    "Viaclovsky Combs v1 §10(2) p.33",
    "The question asks for the full Hodge diamond of X_m, which entries depend on m, and which vary within the constructed families.",
    "F restricts to the nonempty open m=12 family with fixed marked period planes and cup kernel O(−8)⊕O(−9)^2. The displayed map κ1 has zero cokernel there, producing h1,1=49 and h1,2=48. The separate problem inv:E2.3 keeps the general-m and special-member splitting questions explicit.",
    "The combined wording that the Hodge values answer the cited questions overstates the proved locus. Replace it at both front-matter locations; the theorem and the stated remaining problem themselves are already scoped.", "admit II-C3-PROV-129 and 130")
reading("II-C3-LIT-F3", "F", ["Log_v1"],
    "Viaclovsky Log v1 Theorem 1.1 p.1; §1.1(1) p.2",
    "The source constructs infinitely many admissible ordered multiplicity pairs and proves biholomorphic inequivalence for different pairs; it asks whether the resulting structures have different deformation classes.",
    "The source multiplicities are the same (3k,4l) appearing in F. F's persistence and propagation arguments preserve these divisors in a proper smooth family over a connected reduced base, hence along finite deformation chains. The converse is supplied by the connected period-and-attachment family at the fixed ordered pair.",
    "The ordered-pair deformation classification directly answers §1.1(1), with the stated family and chain notion. Preserve that precise credit.")
reading("II-C3-LIT-F4", "F", ["HKP_v1", "LRS_v1"],
    "HKP preprint v1 Corollary 1.3 p.2 and its proof; LRS v1 §5, Theorem 5.2 and Corollary 5.3 p.16",
    "HKP's corollary gives h0(T)≤2 for a complex six-sphere, with its proof invoking the then-asserted algebraic-dimension-zero conclusion. LRS presents the corresponding bound with a=0 as an explicit hypothesis.",
    "For a constructed comb with m=12, F gives h0(T)=2m+1=25. Its holomorphic torus fibration is an algebraic reduction of dimension one. This is a concrete counterexample to the unrestricted HKP corollary and is compatible with the a=0 bound as formulated by LRS.",
    "The correction is exactly to HKP Corollary 1.3 at the cited preprint page. The algebraic-dimension-zero theorem is not negated by this a=1 example.")
reading("II-C3-LIT-F5", "F", ["Horikawa1974"],
    "Horikawa §4 equations (4.3)–(4.5) p.649; Theorem 6.1 and proof pp.660–661",
    "The source constructs map-deformation obstruction cocycles from local coordinate lifts and proves stability under degree-one surjectivity and degree-two injectivity of the induced tangent-cohomology maps.",
    "The paper applies the degree-one map to the embedding of a regular torus fibre. Instead of importing Horikawa's degree-two injectivity, its Artin lifting argument uses smoothness of the torus deformation functor and writes the cocycle correction explicitly. The map obstruction restricts to zero on the rank-two regular fibres and then vanishes as a section of the locally free Leray sheaf. The nonreduced analytic extension is separately supplied by the graph construction in the paper.",
    "The Horikawa citation is correctly used for the local obstruction construction with its modified hypothesis fully proved in E6; it is not credited with the paper's entire nonreduced-base theorem.")
reading("II-C3-LIT-G1", "G", ["LR_v2"],
    "Liu–Rollenske v2 equation (2.3) p.4; Lemma 2.7 and Corollary 2.8 pp.6–7; Proposition 3.6 and Definition 3.7 pp.9–10",
    "The source fixes B, scales it by u, forms the logarithmic cusp parameter λ=log α/(2πi), writes the good-reduction torus as a quotient by (c,w)↦(c+1,w+1/2), and uses a translated fourth-root action with w-shift (1+λ)/4.",
    "The source torus lattice is generated by (2,0),(1+i,0),(1,1/2),(0,λ). The chosen translation a=e4/4 is preserved in the fixed marking. The scalar turn gives λ↦λ+1, which changes the quotient Albanese modulus (1+λ)/2 by 1/2; two turns change that modulus by 1 and give the compatible lattice change. The paper's comparison maps glue this lattice change with its fixed cusp and attachment choices, producing u=w² as the minimal descent cover in G's stated fixed-data setting.",
    "Retain the source coordinate and lattice locators, with version 2 explicit. The status attributes the scalar-covering determination to ii:LR:covering, without claiming that the source asserted a contradictory global descent theorem.")

write_tsv("S6_SERIES_PUBLISH_c3_provenance_literature_claims.tsv", readings)

# Fresh search metadata: queries identify the search interval and actual topics;
# the claim table above contains the outcomes, exact readings, and scope maps.
queries = [
    ('A/E', '"Campana" "Demailly" "Peternell" "normalization" "torsion"', ''),
    ('A/E', '"twisted tangent" "cohomology" "six-sphere"', '90'),
    ('B', '"complex threefold" "b_2" "secondary Hopf"', ''),
    ('B', '"compact complex threefolds" "coinvariants"', ''),
    ('B', '"complex threefold" "secondary Hopf" "Betti"', ''),
    ('C/D', '"torus" "Euler" "degeneration" "even" complex threefold', ''),
    ('C/D', '"torus" "Euler characteristic" "degenerations" Kamenova', ''),
    ('C/D', '"torus" "degeneration" "Euler characteristic" parity', ''),
    ('C/D', '"compact complex" "identity monodromy" torus', ''),
    ('C/D', '"degeneration" "abelian surfaces" "Euler" "even"', ''),
    ('C/D', '"degeneration" "two-dimensional tori" "Euler characteristic"', ''),
    ('C/D', '"torus" "Euler" "blowups" "every even"', ''),
    ('C/D', '"holomorphic" "torus fibration" "Euler" "parity"', ''),
    ('F', '"complex" "six-sphere" "torus" "deformations" 2026', '60; arxiv.org'),
    ('F', '"Combs and complex structures on the six-sphere" "Kuranishi"', '60'),
    ('F', '"Logarithmic transformations on the six-sphere" "deformation"', '60'),
    ('F', '"Kuranishi" "combs" "six-sphere"', '60'),
    ('G', '"Liu" "Rollenske" "covering" "parameter"', ''),
    ('G', '"Liu" "Rollenske" "six-sphere" "monodromy"', '60'),
    ('G', '"Liu" "Rollenske" "two-turn" "covering"', '90'),
]
write_tsv("S6_SERIES_PUBLISH_c3_provenance_searches.tsv", [dict(date_utc="2026-11-22", engine="system1_search_query", main_theorems=a, query=b, recency_days_and_domain=c, use="discovery; mathematical outcomes in literature_claims.tsv") for a,b,c in queries])

# New central-schema rows, for parent admission only.  No historical totals or
# central provenance rows are refreshed here.
fields = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_provenance_checks.tsv").open(), delimiter="\t"))
central = []
for row in readings:
    c = {key:"" for key in fields}
    c.update(claim_id=row["claim_id"], paper="II", locations="1.2 and 1.4; cited body statements", claim=row["outcome"],
        against_records="Compared the current main statement, status line and prior continuation preparation; existing proof-gate dispositions retained.",
        by_recomputation="Source bytes retrieved and SHA-256 checked. This row makes no check-count assertion; root recomputes counts at text-final.",
        against_primary_source=row["exact_loci"]+". "+row["established_scope"],
        required_action=row["proposed_action"], evidence="agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_literature_claims.tsv; "+row["urls"],
        current_paper_location="Theorem "+row["main_theorem"]+" status; 1.4", current_deposit_location="Paper II comments and abstract scope",
        resolution_status="primary-source comparison complete; exact proposals prepared", remaining_gate="Root admission; text-final counts and rendered front-matter reading",
        old_HEXAGON_disposition="Current unpublished Paper II deposit draft is compared; I/V manuscripts are untouched.", current_resolution=row["mathematical_relation"])
    central.append(c)

virtual_paper = paper
for proposal in list(csv.DictReader((OUT / "S6_SERIES_PUBLISH_c3_provenance_link_edits.tsv").open(), delimiter="\t")) + edits:
    if proposal["old_location"].startswith("S6_SERIES_PUBLISH_deposit"):
        continue
    assert virtual_paper.count(proposal["old_text"]) == 1, proposal["change_id"]
    virtual_paper = virtual_paper.replace(proposal["old_text"], proposal["new_text"], 1)
repo_urls = re.findall(r"https?://(?:raw\.)?github(?:usercontent)?\.com/[^}\s]+", virtual_paper)
assert repo_urls == [RECORDS], repo_urls
commit_literals = re.findall(r"(?<![A-Za-z0-9])[0-9a-f]{40}(?![A-Za-z0-9])", virtual_paper)
assert commit_literals == ["bc08b5278bcad2beb70b6862c5722f1b9f636db6"]
assert virtual_paper.count(r"\SsixRepositoryCommit") == 2  # definition and §1.5 use
programs_start = virtual_paper.index(r"\section*{Programs}")
programs_end = virtual_paper.index(r"\begin{thebibliography}", programs_start)
virtual_programs = virtual_paper[programs_start:programs_end]
assert r"\href" not in virtual_programs
printed = re.findall(r"\\nolinkurl\{([^{}]+)\}", virtual_programs)
assert len(printed) == 125
assert set(printed) == {r["printed_path"] for r in csv.DictReader((OUT / "S6_SERIES_PUBLISH_records_II.tsv").open(), delimiter="\t")}
for key in ("comments", "provenance"):
    assert re.findall(r"https?://(?:raw\.)?github(?:usercontent)?\.com/[^\s]+", draft[key]) == [RECORDS + "."]
    assert not re.search(r"(?<![A-Za-z0-9])[0-9a-f]{40}(?![A-Za-z0-9])", draft[key])
    assert "accompany the source" not in draft[key]

web_metadata = {r["key"]:r for r in csv.DictReader((OUT / "S6_SERIES_PUBLISH_c3_provenance_web_metadata.tsv").open(), delimiter="\t")}
provenance_facts = [
    ("II-C3-PV-LINK", "The standing Paper II records-page URL and its #paper-ii anchor are the sole repository address in the proposed manuscript and each affected deposit field.",
     "Prompt §0.3 prescribes this exact page and anchor; the prepared edits replace all inherited program/file and checkpoint links.",
     "Applied all proposals to an in-memory paper only: one repository URL; no program hrefs. Both proposed deposit fields contain the same prescribed address and no other repository URL.",
     "Direct opening returned HTTP 200 with the Paper II HTML anchor; retrieved page SHA-256 "+web_metadata["records_II"]["sha256"]+".", "admit the prepared link edits and deposit-field replacements"),
    ("II-C3-PV-PATHS", "All 125 proposed printed program paths resolve to attached repository paths or current checkpoint code and have exact source-byte hashes.",
     "Historical paths were found in REPOSITORY_PROGRAM_PATHS.txt; current-run paths were found in checkpoint code/. The added Mayer–Vietoris program matches the packed recovered source hash.",
     "Verified 125 plain program paths in the in-memory table and equality with the printed-path column of the records TSV. Exact byte hashes are recorded per file; no CHECK_EVENTS count was recomputed.",
     "All 38 historical program sources were retrieved at the prescribed pin; 87 current-run source files were opened locally. The added example_mayer_vietoris.py hash is 435b69ace886218229aaeda3b049a14008e60d110706e762839f6a63028f354b.", "admit S6_SERIES_PUBLISH_records_II.tsv and the Programs edits"),
    ("II-C3-PV-COMMIT", "The proposed source defines the required repository commit once and prints it once in §1.5 through its macro.",
     "Prompt §0.3 gives the exact commit and the single-print location.",
     "In-memory application leaves one 40-hex literal, in the macro definition, and exactly two macro occurrences: definition and §1.5 use. No commit identifier remains in the proposed deposit comments or provenance.",
     "The prescribed pinned historical source URLs returned the exact program bytes documented in the path table.", "admit the commit macro, §1.5 sentence and Programs-introduction edits"),
    ("II-C3-PV-MODELS", "The methodology and proposed deposit preserve the documented Sol/Astra contribution intervals and add the Opus work specified for this continuation.",
     "Prompt §4.1 gives the August–September working edition, November research/re-derivation/writing/publication intervals, Opus's Paper V rewrite and full Paper I reading plus deposit corrections. The active work remains within the printed 20–22 November publication interval.",
     "Compared the proposed method paragraph with its duplicate deposit account. No current effort setting or independent proof count was inferred from a model name or a whole-paper reading.",
     "The prescribed pinned README names Sol through 4 September and Astra at ultra from 5 September; its freshly retrieved SHA-256 is "+web_metadata["authorship"]["sha256"]+". The controlling supplied prompt gives the later specific contributions.", "admit II-C3-PROV-134, 136 and 138"),
    ("II-C3-PV-DEPOSIT", "The proposed Paper II deposit opens with both required responsibility sentences and directs programs and records to the standing page; its numerical check totals remain pending.",
     "Prompt §§0.2(6), 0.3 and delivery format require TeX-only deposit, the standing page and the submitter-responsibility sentence. The provided Paper V deposit metadata has that opening form.",
     "Verified the exact opening and equal comments/provenance text in the proposed JSON and old/new Markdown rows. Existing check-count strings are deliberately retained as draft text and have not been recounted during edits.",
     "Read the controlling prompt and the supplied Paper V deposit JSON as metadata; no I/V manuscript or proof was opened. The human-checking and CC0 declarations remain the supplied production facts.", "admit II-C3-PROV-135–138; root recomputes and replaces every count at text-final"),
]
for claim_id, claim, record_check, recomputation, primary, action in provenance_facts:
    c = {key:"" for key in fields}
    c.update(claim_id=claim_id, paper="II", locations="1.5; Programs; Paper II deposit fields", claim=claim,
        against_records=record_check, by_recomputation=recomputation, against_primary_source=primary,
        required_action=action, evidence="agents/continuation3_provenance/; controlling prompt §§0.3 and 4.1",
        current_paper_location="1.5; Programs; preamble", current_deposit_location="Paper II comments and provenance",
        resolution_status="proposal verified in memory; shared-file admission pending", remaining_gate="Root admission; final numerical counts; rendered-page reading",
        old_HEXAGON_disposition="Paper II remains an unpublished draft. Published I/V metadata was read only for authorized format comparison.", current_resolution=claim)
    central.append(c)
write_tsv("S6_SERIES_PUBLISH_c3_provenance_claim_rows.tsv", central, fields)

report = [
    "# Paper II — third-continuation provenance and literature comparison\n",
    "Date: " + now + ". All statements below concern Paper II. No shared manuscript, central record, or Paper I/V text was modified.\n",
    "## Concrete corrections\n",
    "1. Narrow Theorem F's two literature-status sentences: the full comb germ answers the deformation question; the Hodge calculation treats the stated nonempty open twelve-tooth family. The remaining general and special-member splitting problem stays stated.\n",
    "2. Make DGKX version 1 explicit at both untwisted-tuple credits; its exact Theorem 6.12 is on pp.81–82. The current version 2 is a different shorter edition. Point the Engel bibliography URL to its already-stated version 1.\n",
    "3. Apply the prepared one-records-page edits. There are 125 programs, including the added Mayer–Vietoris and primitive quotient-basis examples. Historical file bytes were opened at the required pin; current-run code was hashed in the checkpoint.\n",
    "4. Add the newly documented Opus series contributions to methodology and deposit provenance; add the required deposit responsibility sentence. Replace the two source-bundle assertions and both historical repository links with the standing Paper II records page.\n",
    "The existing date range 20–22 November 2026 includes the active third continuation. It makes no claim that this continuation has ended. The checkpoint's check totals are retained only as draft text; root must replace them after its final CHECK_EVENTS computation.\n",
    "## Source-scope outcomes\n",
    "The literature claim table records exact loci, source hashes, own paraphrases and the actual mathematical maps. It does not infer priority from unsuccessful searches or assert that no mathematics relates two settings. Fresh online searches were used for all main-theorem topics, and every result used below was checked in its primary text. Source PDFs and journal page images are outside the checkpoint tree.\n",
]
for r in readings:
    report += ["### " + r["claim_id"] + " — Theorem " + r["main_theorem"] + "\n", r["outcome"] + "\n", "**Established scope:** " + r["established_scope"] + "\n", "**Mathematical relation:** " + r["mathematical_relation"] + "\n", "**Opened locus:** " + r["exact_loci"] + "\n"]
report += [
    "## File and source evidence\n",
    "- `S6_SERIES_PUBLISH_c3_provenance_link_edits.tsv`: 128 original/new proposal rows for macros, §1.5 link, Programs introduction and 125 program references.\n",
    "- `S6_SERIES_PUBLISH_records_II.tsv`: one printed path, full repository path and SHA-256 per program.\n",
    "- `S6_SERIES_PUBLISH_c3_provenance_program_path_checks.tsv`: source location, exact hash, byte size and retrieval outcome.\n",
    "- `S6_SERIES_PUBLISH_c3_provenance_text_edits.tsv`: ten additional original/new rows for precise source editions, F's scope, methodology and both deposit representations.\n",
    "- `S6_SERIES_PUBLISH_deposit_fields_II_proposed.json`: full proposed Paper II deposit fields; historical count text awaits the one text-final computation.\n",
    "- `S6_SERIES_PUBLISH_c3_provenance_literature_claims.tsv`: claim-level outcomes and source relationships.\n",
    "- `S6_SERIES_PUBLISH_c3_provenance_claim_rows.tsv`: the same outcomes in the central provenance schema, ready for parent admission.\n",
    "- Source-download, image-download and web-metadata TSVs retain retrieval metadata only.\n",
    "The records-page URL was opened directly with HTTP 200 and its Paper II anchor verified. The prescribed pinned authorship README was reopened to compare the August/September contributions. The current prompt supplies the additional Opus work and this continuation's authority; its SHA-256 is `"+hashlib.sha256(PROMPT.read_bytes()).hexdigest()+"`.\n",
    "No CHECK_EVENTS count was recomputed. No independent re-derivation is claimed. The full D.2.3 proof and E6 lifting argument were read after exposure to compare their exact uses of Steenbrink and Horikawa. No unobserved manuscript proof check is inferred from a source download.\n",
]
(OUT / "S6_SERIES_PUBLISH_c3_provenance_report.md").write_text("\n".join(report))
summary = {"date_utc": now, "shared_files_modified": False, "additional_edit_rows": len(edits), "primary_scope_claims":len(readings), "program_rows":len(list(csv.DictReader((OUT/"S6_SERIES_PUBLISH_records_II.tsv").open(), delimiter="\t"))), "check_event_counts_recomputed":False, "deposit_counts":"retained as draft; root text-final recomputation required"}
(ROOT / "code" / "S6_SERIES_PUBLISH_c3_provenance_proposals.out").write_text(json.dumps(summary, indent=2)+"\n")
print(json.dumps(summary, indent=2))
