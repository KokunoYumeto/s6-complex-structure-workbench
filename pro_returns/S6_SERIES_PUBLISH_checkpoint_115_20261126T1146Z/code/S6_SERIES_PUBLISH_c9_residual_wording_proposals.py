#!/usr/bin/env python3
"""Context-read P11/P14 passages; writes only this agent's exact proposals.

No canonical source, shared table, inventory, census or manifest is written.
The original cp100 passages are compared directly with the proposed passages.
"""
from __future__ import annotations

from collections import Counter
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from zipfile import ZipFile

from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / "agents/continuation9_global_sweep"
REPAIRS = []


def add(name, sid, finding, old, new, reason):
    REPAIRS.append(dict(name=name, statement_id=sid, finding=finding,
                        old=old, new=new, interpretation=reason))


add("primitive-position-inclusion", "maps:src:D.2.29", "P11",
    "Its restriction to nonstar profiles is an inclusion with inverse\non its image given by the same tuple.",
    "The nonstar positions form a subset with the same marked tuples.",
    "The position is the explicit tuple (profile, section pair, zero, finite site) in the preceding sentence. Inclusion fixes each coordinate, and restriction to its image returns that tuple. The six excluded positions, counts 68 and 62, affine conjugacy and genuine Smith inverses remain unchanged.")
add("general-finite-pattern-inclusion", "maps:src:D.2.30", "P11",
    "this inclusion and its inverse on the image retain\nthose same marked coordinates.",
    "the inclusion retains those marked coordinates.",
    "Selecting g=1 restricts the identical tuple of profile, section pair, zero and chosen sites. The inclusion fixes all tuple entries. Its redundant inverse-on-image phrase is removed; the following nontrivial elimination, affine lift change and Smith quotient inverses are retained.")
add("zero-chern-row-coordinates", "maps:src:D.2.31", "P11",
    "section pair $(a,b)$ and every component coordinate; its inverse\nreads that same tuple. It therefore fixes every marked monodromy",
    "section pair $(a,b)$ and every component coordinate. It therefore\nfixes every marked monodromy",
    "The retained row identification fixes the ordered profile, selected zero, positive pair and every component coordinate. This is an identity on the stated tuple, whose square is the identity. All monodromy, cocycle and cap maps remain.")
add("all-original-pattern-subset", "maps:src:D.2.32", "P11",
    "Theorem~\\ref{maps:src:D.2.31}. The inverse inclusion retains\nevery row and site identity. The complement has 54 patterns, so\nno duplicate or implicit identification of the finite choices\nis used in this comparison.",
    "Theorem~\\ref{maps:src:D.2.31}, with every row and site marking\nretained. The complement consists of the 54 patterns containing\na nonzero-Chern original.",
    "Deleting the patterns containing a nonzero-Chern original restricts the 282 tuple-indexed patterns to the 228-pattern subset. The inclusion is the identity on each surviving marked tuple; the complement is exactly the deleted 54. The rewrite states this set relation and retains all three counts without calling the inclusion an inverse to deletion on the whole set.")
add("multiplicative-cap-input-identity", "maps:src:D.2.33", "P11",
    "Theorem~\\ref{maps:src:D.2.31}, part 6. Identity on these coordinates\nand its inverse carry the full cap diagrams to the ones used here.",
    "Theorem~\\ref{maps:src:D.2.31}, part 6. The identity on these\ncoordinates carries the full cap diagrams to the ones used here.",
    "The marked lattice, power vector, root coordinate and normal orientation are explicitly fixed. The comparison fixes every coordinate of every cap diagram, so its inverse contributes no distinct construction. The boundary root-argument inverse and holomorphic finite-sum conjugacy remain below.")
add("multiplicative-row-identity", "maps:src:D.2.33", "P11",
    "The identification and its inverse fix those coordinates.",
    "The identification fixes those coordinates.",
    "The row coordinates are the ordered profile, selected zero, section pair and all component coordinates. The retained map is the coordinate identity. The following quotient that forgets zero-Chern O/M choices, its canonical section and the full inverse fibre of that quotient remain mathematically substantive and are not changed.")
add("weighted-row-tuple", "maps:src:D.2.37", "P11",
    "every component coordinate in Definition~\\ref{mapsIII:def:elliptic-marked-data};\nthe inverse reads that same tuple. Thus the displayed raw\nmatrices use exactly those marked elliptic matrices and section",
    "every component coordinate in Definition~\\ref{mapsIII:def:elliptic-marked-data}.\nThus the displayed raw matrices use exactly those marked elliptic\nmatrices and section",
    "The tuple identity is retained with every entry named. The subsequent nontrivial Tate-index reflection and its inverse, as well as the integral graph right inverses, remain unchanged.")
add("weighted-pattern-tuple", "maps:src:D.2.37", "P11",
    "row take the Cartesian product\nof the site option sets just stated. Its inverse reads\nthe original row and every site option. This proves\ncompleteness and absence of duplicate marked choices\nby the displayed inverse.",
    "row take the Cartesian product of the site option sets just\nstated. Each marked choice is indexed by that row and its ordered\nsite options, so this product lists every choice exactly once.",
    "A marked choice is the tuple consisting of its row and the ordered choices in those site option sets. The product indexing map sends that tuple to itself. Equality of product coordinates is exactly equality of marked choices, proving completeness and uniqueness without an additional inverse identity sentence. The genuine pattern retraction changing starred F to O and its section remain.")
add("type-c-toric-identity", "os49:rem:type-c-marking", "P11",
    "negative-diagonal fan used here. The identity on every character\nsemigroup and its inverse extend across every toric divisor and\nnode.",
    "negative-diagonal fan used here. The identity on every character\nsemigroup extends across every toric divisor and node.",
    "The retained preceding fan equality identifies each cone and character semigroup. The map sends each character to itself and respects its multiplication, so its induced chart map extends as stated. The inverse lattice marking, reciprocal affine gauges and nontrivial inversion g_Y=g^{-1} remain untouched.")
add("collapsed-subset-quotient-map", "mapsIII:lem:fixed-conical-metrics", "P11",
    "to the same identity quotient $x\\mapsto[x]$ with inverse taking\nthe unique representative off $F$. That proof gives the metric,",
    "to the quotient map $P\\to P/F$, $x\\mapsto[x]$. Its restriction\nfrom $P\\setminus F$ to $(P/F)\\setminus\\{*\\}$ has inverse taking\nthe unique representative. That proof gives the metric,",
    "The quotient relation identifies all points of F and otherwise only a point with itself. Therefore every noncollapsed class has exactly one representative in P\\F, giving both inverse compositions on the stated restrictions. The actual restricted inverse is preserved and its domain made explicit; the quotient metric, length property and topology are unchanged.")

add("primitive-finite-mathematical-method", "mapsIII:rem:primitive-finite-calculations", "P14",
    r"""A finite comparison evaluates \eqref{maps:eq:D.UF1} and the
affine-power fixed-point equations for all $68$ marked matrices,
$1\le k\le6$ and every pair $(n,r)\bmod m$; the $150059$ exact
results agree. For $305$ choices, the full unreduced graph and
normal Smith matrices give the reduced presentation above,
including $99$ torsion-cap instances and $55$ zero-rational-Euler
instances. The all-parameter argument is the proof of
Theorem~\ref{maps:src:D.2.29}.""",
    r"""At each of the $68$ marked finite positions, the proper-power
fixed-point equations give exactly \eqref{maps:eq:D.UF1}.
The normal tori of the affine-group generators give the full Thom
columns \eqref{maps:eq:D.UF9}. For the stated nonstar fillings,
adjoin the integral graph relation \eqref{maps:eq:D.UF4} and the
regular-cap relations. The Smith cokernel, the degree-one
Mayer--Vietoris kernel and the Seifert abelianization give
\eqref{maps:eq:D.UF5}, including torsion central caps and zero
rational Euler number. These are the integral maps constructed
in the proof of Theorem~\ref{maps:src:D.2.29}.""",
    "Read the theorem's local statement, fixed-power obstruction, full Thom columns and complete global gluing argument. The 68 marked positions are a mathematical catalogue count and are retained, while global claims remain restricted to the stated nonstar fillings. The 150059/305/99/55 numbers describe verification batches; they remain verbatim in this defect's old_text and in the Programs section, while the remark now specifies the mathematical method and exact formulas. All arbitrary-order and free-twist scope comes from the same theorem, with no new hypothesis or conclusion.")
add("general-finite-mathematical-method", "mapsIII:rem:general-finite-calculations", "P14",
    r"""The finite calculation includes all $34$ additional lattice bases.
For $1\le k\le6$ and every residue pair, $38675$ exact
affine-power fixed-point tests agree with \eqref{maps:eq:D.AF3}.
The $175$ full unreduced normal and graph Smith matrices agree
with \eqref{maps:eq:D.AF4}, including $35$ torsion-cap instances.
The one-site calculation compares $725$ Smith forms, with five
integer clutch values, with
\eqref{maps:eq:D.AF6}--\eqref{maps:eq:D.AF7}; all agree.
Theorem~\ref{maps:src:D.2.30} proves the formulas for every
positive order and every free integer twist.""",
    r"""At the $34$ additional positions with $g=q>1$, use the integral
fixed and coinvariant bases in \eqref{maps:eq:D.AF2}. The
proper-power obstruction gives \eqref{maps:eq:D.AF3}, and the
normal tori of $\beta,\eta,c$ give the three columns in
\eqref{maps:eq:D.AF4}. For one finite site, eliminate $D=-be\,s$
and put $n'=n-(m/g)e$. The determinantal divisors of
\eqref{maps:eq:D.AF9} give
\eqref{maps:eq:D.AF6}--\eqref{maps:eq:D.AF7}.
Theorem~\ref{maps:src:D.2.30} constructs these integral maps for
every allowed positive order, every free integer twist and every
integer clutch.""",
    "The theorem's fixed/coinvariant bases, proper-power obstruction, normal Thom columns and full one-site reduction were read. Its 34 positions with g=q>1 are retained. The exact substitution n'=n-(m/g)e and the determinantal-divisor method are already in the proof and yield the same referenced groups. The chosen tests 38675/175/35/725 and five clutch values are verification scope, retained in old_text and the Programs section rather than presented as mathematical evidence for arbitrary parameters.")
add("zero-chern-original-mathematical-method", "mapsIII:rem:zero-chern-original-calculations", "P14",
    r"""The finite calculation covers all $396$ unselected zero-Chern
original-cap lattices and folded intersection ranks, the $228$
additive patterns, and $144$ primitive scalar-circle pairs in
the $b=1$ patterns that can be simply connected. The orbit
coordinates in part 4 specialize to the odd-star component
coordinates of Theorems~\ref{maps:src:D.2.16} and
\ref{maps:src:D.2.17}; the inverse reads
the same labelled orbit coefficients. Every permitted narrow-$P$
section pair is included in the option rule above.""",
    r"""The natural factor-pair and site-option enumeration gives $396$
unselected zero-Chern original occurrences and $228$ additive
patterns. The component orbits and their multiplicities determine
the primitive fibre vector $W$; the folded intersection matrix
$I^tQ_KR_0$ in part 4 gives the component rank. At the odd stars,
the comparison sends each labelled orbit coefficient to the same
coefficient in Theorems~\ref{maps:src:D.2.16} and
\ref{maps:src:D.2.17}. The integral reduction in part 8 and the
framed reconstruction give the primitive scalar-circle data for
the simply connected $b=1$ sector. Every permitted narrow-$P$
section pair is included in the option rule above.""",
    "Read the whole component-orbit/primitive-fibre/folded-intersection argument in part 4, the simply connected b=1 integral reduction in part 8, and the framed reconstruction tail. The true enumeration counts 396=316+80 and 228 are preserved. The Programs entry identifies 144 as full-matrix comparisons, so that test count is retained in old_text and its program scope rather than asserted as a geometric count. The odd-star comparison remains the exact identity on labelled orbit coefficients. No scalar-circle construction, cap choice, parameter scope or homology formula is changed.")
add("all-original-additive-mathematical-method", "mapsIII:rem:all-original-additive-calculations", "P14",
    r"""The finite calculation includes all $46$ primitive Chern vectors,
their logarithm vectors, full area kernels and primitive fibre
images, and the complete $282$-pattern table. For the new patterns,
the unreduced graph, normal and fibre-kernel Smith matrices agree
with the reduced presentation in $74$ comparisons, including
$9$ torsion-cap and $54$ zero-rational-Euler instances.""",
    r"""For the $46$ marked nonzero-Chern occurrences, compute the
primitive Chern vectors, their logarithm vectors, the full area
kernels and the primitive fibre images as in the preceding proof.
The products of the site-option sets give the $282$ patterns.
Smith reduction of the full graph, normal and fibre-kernel matrix
gives the degree-two cokernel. The integral degree-one
Mayer--Vietoris kernel supplies its free bridge, giving
\eqref{maps:eq:D.OC3} also at zero rational Euler number.""",
    "The theorem's enumeration, cap-elimination map, full degree-one bridge and zero-Euler example were read. Its 46 marked occurrences and 282 patterns are mathematical counts and are retained. The complete normal/fibre kernels and bridge determine the stated homology. The 74/9/54 numbers in the old remark are comparison-batch counts; they remain recorded here and in the Programs entry. The mathematical 54-pattern complement is separately retained in the theorem.")
add("original-multiplicative-mathematical-method", "mapsIII:rem:original-multiplicative-calculations", "P14",
    r"""The finite calculation covers all $120$ integral normal forms,
primitive fibre and monodromy kernels, values of $\omega$, and
primitive Chern and component-multiplicity vectors. The occurrences
are $I_8$ in $6$ cases, $I_7$ in $14$, $I_2$ in $31$, $I_3$ in
$23$, $I_5$ in $38$ and $I_4$ in $8$. The unreduced graph,
normal and fibre matrices agree with the reduced presentation in
$213$ Smith comparisons for the new patterns, including $18$
torsion-cap and $172$ zero-rational-Euler instances. The proof
above gives the full range of orders and free affine parameters.""",
    r"""At the $120$ marked nonzero-Chern multiplicative positions,
the integral normal forms determine the primitive fibre and
monodromy kernels, their values under $\omega$, and the primitive
Chern and component-multiplicity vectors. The occurrences are
$I_8$ in $6$ cases, $I_7$ in $14$, $I_2$ in $31$, $I_3$ in $23$,
$I_5$ in $38$ and $I_4$ in $8$. Smith reduction of the full graph,
normal and fibre matrix gives the degree-two cokernel. Adjoining
the free degree-one Mayer--Vietoris bridge gives the homology
formulas of Theorem~\ref{maps:src:D.2.33} for the full stated range
of orders and free affine parameters.""",
    "The 120 marked nonzero-Chern positions and the six type counts sum to the same 120 occurrences in the theorem's enumeration. They remain unchanged. The preceding proof constructs the normal forms, fibre images, cap elimination and free bridge, so the rewritten paragraph states that method. The 213/18/172 counts concern finite Smith comparisons and remain in this exact old_text and the Programs scope. All actual integral maps and parameter ranges are retained.")
add("weighted-profile-mathematical-method", "mapsIII:rem:weighted-profile-calculations", "P14",
    r"""The finite computation includes all $172$ constant-specialization
relation matrices and $1626$ full weighted graph presentations on
the $495$ patterns, of which $1131$ have weight greater than one.
The full parameter range follows from the integer right inverses,
complete local kernels and integral relative splitting in the proof.
Definition~\ref{mapsIII:def:weighted-natural-data} specifies the
initial translation iterates and every permitted cap choice.

Theorem~\ref{maps:src:D.2.41} gives the integral algorithm for all
positive weights, including weights sharing factors with $a$.
The inclusion of the present input set fixes the initial marked
row, $d$, every ordered cap choice, all logarithmic $(m,v)$ data
and the clutch; its inverse on that subset reads the same list.""",
    r"""For the $172$ natural rows and $495$ patterns, use the matrices
$A_i(d)$ and the complete local kernels in the proof. Its integer
right inverses determine the exterior quotient. Smith reduction
of the full integral boundary presentation gives the cokernel,
and the integral relative splitting gives the homology for every
stated parameter. Definition~\ref{mapsIII:def:weighted-natural-data}
specifies the initial translation iterates and every permitted
cap choice.

Theorem~\ref{maps:src:D.2.41} gives the integral algorithm for all
positive weights, including weights sharing factors with $a$.
The inclusion of the present input set fixes the initial marked
row, $d$, every ordered cap choice, all logarithmic $(m,v)$ data
and the clutch.""",
    "The theorem's explicit integer right inverse, full local boundary kernels, relative splitting and 495/459 pattern enumeration were read. The 172 rows and 495 patterns remain, with the same restricted parameters in the present definition; the later theorem retains the extension to all positive weights. The 1626/1131 numbers describe chosen weighted matrix comparisons and remain in old_text and program scope. The final inclusion is the identity on the displayed input tuple, so only its redundant inverse sentence is removed.")
add("odd-weighted-mathematical-method", "mapsIII:rem:odd-weighted-calculations", "P14",
    r"""The finite calculations use the permitted odd-common-factor
weights among $1,\allowbreak 2,\allowbreak 3,\allowbreak 5,\allowbreak
7,\allowbreak 9,\allowbreak 15,\allowbreak 21,\allowbreak 25,\allowbreak
35,\allowbreak 45,\allowbreak 105,\allowbreak 315,\allowbreak 1001$.
They include $2334$ exterior presentations, $12249$ saturated
local kernels, $1386$ projected finite lattices and $33264$
finite-action candidates with all their proper powers.
The $6326$ complete global matrices include $4950$ matrices
on the two Euler values and $1376$ matrices with two additional
full-vector regular logarithms. The full written argument
establishes every allowed positive weight and all finite,
regular and clutch parameters in \eqref{maps:eq:D.OW1}.

Theorem~\ref{maps:src:D.2.41} supplies the integral algorithm
for every positive weight. The inclusion of the present input
set fixes the natural row, weight, ordered cap choices, every
logarithmic pair $(m_i,v_i)$ and the clutch; its inverse on
that subset reads the same tuple.""",
    r"""These saturated kernels and full boundary columns give the
integral presentation for every allowed positive weight and all
finite, regular and clutch parameters in \eqref{maps:eq:D.OW1}.

Theorem~\ref{maps:src:D.2.41} supplies the integral algorithm
for every positive weight. The inclusion of the present input
set fixes the natural row, weight, ordered cap choices, every
logarithmic pair $(m_i,v_i)$ and the clutch.""",
    "Read the complete remark, its saturated-preimage requirement, explicit fibre quotient comparison and sign-change maps, plus the preceding theorem's parameter definition. The genuine maps (eta,k)->(omega_d(eta),k), its Bezout inverse modulo return columns, and the sign-change inverse remain byte-identical. The listed weights and counts 2334/12249/1386/33264/6326/4950/1376 are finite verification scope and remain in old_text and the Programs section. Only that narration and the identity-on-input inverse phrase are removed; OW1 and the all-weight extension are unchanged.")
add("all-weight-mathematical-method", "mapsIII:rem:all-weight-integral-calculation", "P14",
    r"""The computation records the full quadratic coefficient vectors
of \eqref{maps:eq:D.BC2}, the ordered suffixes of
\eqref{maps:eq:D.BC3}, every fibre relation and all five normal
columns. Its operations are integer polynomial identities,
saturated integer kernels, the period sum of length $h$, and
Smith or Hermite decompositions of the full matrices. The
result is the complete Seifert abelianization and integral
homology for every positive $d$, every permitted affine power,
every finite regular-logarithm list and every integer clutch.""",
    r"""Form the full quadratic coefficient vectors of
\eqref{maps:eq:D.BC2}, the ordered suffixes of
\eqref{maps:eq:D.BC3}, every fibre relation and all five normal
columns. Integer polynomial identities, saturated integer
kernels, the period sum of length $h$, and Smith or Hermite
decompositions of the full matrices give the complete Seifert
abelianization and integral homology for every positive $d$,
every permitted affine power, every finite regular-logarithm
list and every integer clutch.""",
    "This is the same explicit mathematical algorithm with the same coefficient vectors, suffixes, five normal columns, integer operations and complete input range. The wording now instructs the mathematical operations instead of describing what a computation records. The following (c,k)->(c-h(k)/2,k) comparison and its addition inverse are preserved exactly.")


def main():
    source = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text(encoding="utf-8")
    archive = ROOT.parents[1] / "upload/S6_SERIES_PUBLISH_continue_cp100.zip"
    with ZipFile(archive) as base:
        original = base.read("S6_SERIES_PUBLISH_checkpoint_100/S6_SERIES_PUBLISH_III.tex").decode("utf-8")
    owners, _, _ = parse_statements(source)
    now = datetime.now(timezone.utc).isoformat()
    df = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_defects_III.tsv").open(), delimiter="\t"))
    ef = next(csv.reader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
    candidate = source
    defects, events, groups = [], [], {}
    targets = lambda t: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]+\}', t))
    for i, p in enumerate(REPAIRS, 1):
        old, new = p["old"], p["new"]
        if source.count(old) != 1 or original.count(old) != 1:
            raise ValueError((p["name"], "original/live guard", original.count(old), source.count(old)))
        pos = source.index(old)
        owning = [o for o in owners if o.start <= pos < o.stop]
        if len(owning) != 1 or owning[0].statement_id != p["statement_id"]:
            raise ValueError((p["name"], "formal owner", owning))
        owner = owning[0]
        if targets(old) != targets(new) or candidate.count(old) != 1:
            raise ValueError((p["name"], "overlap or permanent target"))
        candidate = candidate.replace(old, new, 1)
        line = source.count("\n", 0, pos) + 1
        cp_line = original.count("\n", 0, original.index(old)) + 1
        cid = f"CLAUDE-III-{p['finding']}-RESIDUAL-{i:03d}"
        p.update(change_id=cid, tag=owner.tag, current_line=line, cp100_line=cp_line)
        defects.append(dict(change_id=cid, type="D09" if p["finding"] == "P14" else "D08",
            statement_id=p["statement_id"], old_location=f"cp100 source line {cp_line}; tag {owner.tag}",
            old_page="original cp100; current page concordance pending",
            new_location=f"same labelled statement/proof; {p['name']}",
            new_page="pending current rendered-PDF review", old_text=old, new_text=new,
            reason=p["interpretation"], review_status=f"Original and proposed passage and relevant proof context read at {now}; proposed for root admission; no new independent-check or PDF-page credit."))
        groups.setdefault(p["statement_id"], []).append(p)
        print(f"{cid} {owner.statement_id} {owner.tag}: {p['name']}")
    for j, (sid, ps) in enumerate(groups.items(), 1):
        eid = f"publish:c9:III:residual-wording:{j:03d}"
        row = {k: "" for k in ef}
        row.update(statement_id=sid, date=now[:10], who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global wording reviewer",
            type="used and rechecked in this run", outcome="Read the original cp100 passages, current passages and surrounding argument for " + ", ".join(p["name"] for p in ps) + ". Each exact interpretation and retained mathematical scope is documented in its defect reason. Genuine inverse maps and classification counts are retained. Guarded reversal recovers the current pre-edit source exactly; the changed old passages also match original cp100 exactly. This is a scoped wording/method comparison, with no whole-proof, new independent-check or rendered-page credit.",
            event_id=eid, phase="continuation9 Paper III residual publication wording", source_file="code/S6_SERIES_PUBLISH_c9_residual_wording_proposals.py",
            source_event_type="used and rechecked in this run", evidence_group=eid, date_utc=now,
            where="agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_residual_wording_proposals.json")
        events.append(row)
    recovered = candidate
    for p in reversed(REPAIRS):
        if recovered.count(p["new"]) != 1:
            raise ValueError((p["name"], "ambiguous reverse guard"))
        recovered = recovered.replace(p["new"], p["old"], 1)
    assert recovered == source
    assert targets(source) == targets(candidate)
    OWN.mkdir(parents=True, exist_ok=True)
    (OWN / "S6_SERIES_PUBLISH_c9_residual_wording_proposals.json").write_text(json.dumps(REPAIRS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    for name, fields, rows in [("S6_SERIES_PUBLISH_c9_residual_wording_defects.tsv", df, defects), ("S6_SERIES_PUBLISH_c9_residual_wording_events.tsv", ef, events)]:
        with (OWN / name).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader(); writer.writerows(rows)
    print(f"Prepared {len(REPAIRS)} exact proposals and {len(events)} scoped events; original guards, formal owners, targets and exact reverse comparison pass.")


if __name__ == "__main__":
    main()
