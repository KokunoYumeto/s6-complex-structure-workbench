#!/usr/bin/env python3
"""Prepare LH local proposals only; read canonical text solely at released spans."""
import csv
from datetime import datetime, timezone
from hashlib import sha256
from itertools import islice
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
PREFIX = "S6_SERIES_PUBLISH_III_02LH_"
ID = "maps:src:D.2.40"
CANON = ROOT/"S6_SERIES_PUBLISH_III.tex"
SOURCE_SHA = "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
SPANS = {"statement": (16765, 16822), "proof": (16825, 17043)}


def digest_file(path):
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


assert digest_file(CANON) == SOURCE_SHA
frozen = {
    "fresh_derivation.md": "23e7026ce52f00005d7d4248f33b4975900e3c64b9905a06b614ecde06cbf0d8",
    "fresh_local_maps.md": "71eb34b0e8735b77d34e3bfe7a48240b2acde421a0a2fdc8ea7b96bc4cc79ee0",
    "fresh_calculation_readout.md": "ba51666ac3a29c19dc7460e392c1896514ea63d6a7351c4c25692cf5d7409ae1",
    "post_exposure_derivation.md": "8732d435c1afe288761d1f60d7feac37981f9ad842634bd376f67d63d6717a20",
    "receiving.tex": "ece531cc11837af5ef7933a486976d9c70c2dab77ab619c3d29c30658042510b",
    "post_exposure_data.json": "f76fd831512be981ca38bbca123886f82c6f446bd9e35c113b049f110694e168",
}
for suffix, expected in frozen.items():
    assert digest_file(LANE/(PREFIX+suffix)) == expected, suffix


def environment(text, name):
    start = text.index("\\begin{"+name+"}")
    end = text.index("\\end{"+name+"}", start)+len("\\end{"+name+"}")
    return text[start:end]


old = {}
for kind, env in (("statement", "theorem"), ("proof", "proof")):
    released = (LANE/(PREFIX+"released_"+kind+".tex")).read_text()
    old[kind] = environment(released, env)
    lo, hi = SPANS[kind]
    with CANON.open() as f:
        bounded = "".join(islice(f, lo-1, hi)).rstrip("\n")
    assert bounded == old[kind], kind
    assert len(bounded.splitlines()) == hi-lo+1
    print("PASS exact", kind, "guard", lo, hi,
          sha256(bounded.encode()).hexdigest())
receiver = (LANE/(PREFIX+"receiving.tex")).read_text()
new = {"statement": environment(receiver, "theorem"),
       "proof": environment(receiver, "proof")}
assert old["proof"].count(r"\item ") == 14
for kind in old:
    for pattern in (r"\\label\{([^}]+)\}", r"\\hypertarget\{([^}]+)\}",
                    r"\\tag\{([^}]+)\}"):
        assert re.findall(pattern, old[kind]) == re.findall(pattern, new[kind])
print("PASS complete 14-item original and exact eight-label/eight-target/seven-tag partitions")


def write_tsv(suffix, fields, records):
    path = LANE/(PREFIX+suffix+".tsv")
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t",
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)
    raw = path.read_bytes()
    assert b"\r" not in raw and raw.endswith(b"\n")
    with path.open(newline="") as f:
        assert list(csv.DictReader(f, delimiter="\t")) == [
            {k:str(row[k]) for k in fields} for row in records
        ]
    return path


replacements = [
    dict(statement_id=ID, old_text=old[kind], new_text=new[kind],
         reason=(
             "Whole LH "+kind+" replacement after complete fresh derivation and "
             "whole-original comparison; preserve all permanent identities. "
             "Clarify 459/495 scope, give full odd-torsion maps and inverses, "
             "and remove historical file apparatus. All mathematical formulas stand. "
             "Separate local proposal; no canonical application."
         ))
    for kind in ("statement", "proof")
]
write_tsv("replacements", ["statement_id", "old_text", "new_text", "reason"], replacements)


def between(text, first, last=None):
    start = text.index(first)
    return text[start:] if last is None else text[start:text.index(last, start)]


def item(number):
    pieces = old["proof"].split(r"\item ")[1:]
    assert len(pieces) == 14
    value = pieces[number-1]
    if number == 14:
        value = value[:value.index(r"\end{enumerate}")]
    return value.strip()


heads = list(re.finditer(r"\\emph\{([^}]+)\}", new["proof"]))
sections = {}
for i, m in enumerate(heads):
    end = heads[i+1].start() if i+1 < len(heads) else new["proof"].index(r"\end{proof}")
    sections[m[1]] = new["proof"][m.start():end].strip()


def sec(title):
    return sections[title]


def new_between(first, last=None):
    return between(receiver, first, last).strip()


def location(text, value, base, name):
    assert text.count(value) == 1, (name, value[:100], text.count(value))
    start = text.index(value)
    first = base+text[:start].count("\n")
    last = first+value.count("\n")
    return f"{name}:lines {first}--{last}"


defects = []


def defect(slug, kind, old_kind, before, after, reason):
    assert old_kind in SPANS
    assert before and after
    old_location = location(old[old_kind], before, SPANS[old_kind][0],
                            "S6_SERIES_PUBLISH_III.tex ("+old_kind+" guard)")
    new_location = location(receiver, after, 1,
                            str((LANE/(PREFIX+"receiving.tex")).relative_to(ROOT)))
    defects.append(dict(
        change_id=f"III-c7-02LH-{len(defects)+1:02d}-{slug}",
        type=kind, statement_id=ID,
        old_location=old_location,
        old_page="not asserted; exact released source interval",
        new_location=new_location,
        new_page="pending final III PDF build and page review",
        old_text=before, new_text=after, reason=reason,
        review_status="local whole comparison complete; root record admission and final page review pending",
    ))


s = old["statement"]
p = old["proof"]
defect("machine-header", "D10", "statement",
       next(line for line in s.splitlines() if line.startswith(r"\StatementRecord")),
       r"\textup{\small(tag 02LH)}",
       "Replace machine uses/status apparatus by the printed small tag; retain the theorem label and hypertarget.")
defect("short-title", "D16", "statement",
       r"\begin{theorem}[shared odd factors in every weighted profile]",
       r"\begin{theorem}[Shared odd factors in weighted profiles]",
       "Give the statement a short mathematical title.")
defect("starred-cap-scopes", "D26", "statement",
       between(s, "In particular it covers", "The free ranks"),
       new_between("The all-star-original scope consists", "Use the period lattice"),
       "Make the literal all-star-original 459 families and the broader 495 families explicit, with inclusion and retraction; retain odd I_n* originals in both. No false-reading refutation is claimed.")
defect("graph-target-marking", "D20", "statement",
       between(s, "Use the target", "and include all columns"),
       new_between("Use the period lattice", "Include every return column"),
       "Define the weighted period lattice, primitive graph kernel and peripheral insertion before using the full target.")
defect("finite-criterion-at-weight", "D22", "statement",
       "freeness tests and full Seifert groups remain valid.",
       new_between("At a finite-good site let", "Include all five columns"),
       "State the projected-lattice coordinates and every-power criterion at the current weight, with the separate rank-four regular-site criterion.")
defect("kernel-reference-scope", "D08", "statement",
       between(s, "Here $\\mathcal K_i(1)$", "Formula \\eqref{maps:eq:D.OW4}"),
       new_between("For a nonzero-Chern original, \\(\\mathcal K_i(1)\\)",
                   "The kernel in \\eqref{maps:eq:D.OW4}"),
       "Replace recorded-data wording by the principal-bundle fibre kernel and its resolved series references.")
defect("positive-integral-kernel-scope", "D02", "statement",
       between(s, "Formula \\eqref{maps:eq:D.OW4}", "Let $T$"),
       new_between("The kernel in \\eqref{maps:eq:D.OW4}", "Let \\(T\\)"),
       "State saturation and retention of nonunit factors positively.")
defect("group-and-rank-parameters", "D22", "statement",
       between(s, "Let $T$", "The executable"),
       new_between("Let \\(T\\)", "In particular \\(\\chi(X)"),
       "Give the full Seifert group, A1, r, beta, L and all homology groups at the place the extended torsion rule is stated.")
defect("historical-executable-apparatus", "D09", "statement",
       between(s, "The executable", "\n\n\\end{theorem}"),
       new_between("In particular \\(\\chi(X)", "\\end{theorem}"),
       "Remove the unavailable historical executable assertion from the mathematical theorem. The comparison records exact availability and the new algorithms; no historical execution is claimed.")
defect("machine-proof-enumeration", "D10", "proof",
       r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
       r"\emph{Exact degree-one exterior image at every d.}",
       "Use mathematical proof paragraphs in place of the machine-labelled enumeration; compare all fourteen original items.")
defect("full-exterior-quotient", "D22", "proof",
       between(item(1), "Put $g=", "The regular graph"),
       sec("The full fibre quotient and its explicit coordinates."),
       "Give the exact five-generator relation image, Z plus Z/g quotient and its Bezout inverse, establishing the original torsion-prime assertion integrally.")
defect("actual-involution-map", "D22", "proof",
       between(item(1), "Fibre inversion"),
       new_between("Use the period exponential and its inverse above.",
                   "Write \\(\\mathfrak a\\)"),
       "Construct inversion on the actual semidirect exterior, identify its two actions and give the exact cellular graph sequence.")
defect("evaluation-matrix-notation", "D20", "proof",
       item(2),
       new_between("Write \\(\\mathfrak a\\)", "For \\(k\\in K_d\\)"),
       "Distinguish the two evaluation homomorphisms from return/presentation matrices; give invariance, restriction and integral division by odd g.")
defect("defensive-involution-introduction", "D02", "proof",
       "We spell out the resulting splitting to avoid a\nformality or invariant-descent assumption.",
       r"\emph{The marked graph and its integral involution section.}",
       "Replace the defensive introduction by the construction itself.")
defect("odd-half-and-inverse", "D22", "proof",
       between(item(3), "Given\n$k\\in K$", "Thus\n$H_2(V)=C\\oplus K$"),
       new_between("For \\(k\\in K_d\\)", "Give \\(C_{d}\\) the trivial"),
       "Write the inverse of doubling, lift independence, uniqueness, additivity and both inverse splitting maps.")
defect("fixed-and-norm-sweeps", "D22", "proof",
       item(4),
       new_between("A literal fixed normal is", r"\emph{The raw normal images"),
       "Give the actual fixed normal and m-fold covering pushforward with inverse strip coordinates and zero full fibre coordinate.")
defect("shear-meridian-marking", "D20", "proof",
       item(5),
       new_between("For a free logarithm", "For the core root generator"),
       "Express the original meridian m theta-v as the exact commuting pair and calculate its whole cocycle and graph coordinates.")
defect("root-thom-source", "D22", "proof",
       between(item(6), "For the affine meridian", "The proof of the general"),
       new_between("For the core root generator", r"\emph{Every finite affine action"),
       "Give the determinant-one root generator change, its inverse and the root column; the full core presentation later verifies all source relations including torsion.")
defect("finite-every-power-proof", "D22", "proof",
       "The proof of the general\nfreeness test \\eqref{maps:eq:D.WP5} is unchanged.",
       sec("Every finite affine action and its complete Thom source."),
       "Derive the full weighted projected lattice, fixed-point inverse, affine and holomorphic conjugacies, source relations and regular specialization for every allowed parameter.")
defect("free-cap-target-bases", "D22", "proof",
       item(7),
       new_between("The central fibre is an integral homology retract",
                   "For a multiplicative fibre, its central cycle"),
       "Give the actual flat gauges, cone maps, powered orbits and free integral bases; the cusp and nonzero-Chern targets are given in their own receiving paragraphs.")
defect("cusp-integral-kernel", "D22", "proof",
       item(8),
       sec("The cusp: its free basis and each normal disc."),
       "Supply the literal period basis, primitive wedge image and inverse, full boundary H1/H2, entire normal kernel, each ray-character disc and its integral inverse, retaining Z/d.")
defect("rank-one-specialization", "D22", "proof",
       between(item(9), "For the rank-one cap", "For an\noriginal zero-degree additive cap"),
       new_between("At a narrow unselected", r"\emph{Nonzero-Chern originals.}"),
       "Give both primitive period cases, flat node maps, four specialization images, integral inverse coordinates and saturation of the torsion boundary kernel.")
defect("additive-fibre-coordinates", "D22", "proof",
       between(item(9), "For an\noriginal zero-degree additive cap"),
       new_between("The nearby elliptic area specializes", "For a multiplicative fibre"),
       "Give the positive component-orbit and angular-return coefficients, their image coordinates and rational injectivity, including original odd stars.")
defect("cover-transfer-saturation", "D22", "proof",
       item(10),
       sec("The period cover and its transfer."),
       "Prove the covering square and its simplex transfer, the identity on the fibre image, saturated pullback and all quotient/section inverse equations.")
defect("rim-history", "D01", "proof",
       "There is one previously isolated correction:",
       r"\emph{The elliptic image and the exact angular rim.}",
       "State the geometric rim relation without narration of an earlier correction.")
defect("fixed-normal-geometric-scope", "D20", "proof",
       between(item(11), "The full fixed-normal projections",
                   "Indeed, for all $172$ rows"),
       sec("All unchanged fixed-normal images, including section corrections."),
       "Use the full primitive fixed lattice and actual geometric normal; include its rim inverse and distinguish explicitly changed Wang sections by their complete shears.")
defect("elliptic-unit-map", "D22", "proof",
       between(item(11), "Indeed, for all $172$ rows",
                   "These $172$ matrices"),
       new_between("For each defining profile form", "Every return fixes"),
       "Prove D.OW7 with Euclidean-minor right inverses and the exact OS46/II inverse and index-three word inclusion. D.OW7 is retained as true; no D25 credit.")
defect("historical-json-apparatus", "D09", "proof",
       between(item(11), "These $172$ matrices", "Since every"),
       "The displayed minor sections give every integral preimage.",
       "Remove the absent historical JSON retention claim from the proof; retain its availability record in the comparison and provide complete new matrix data.")
defect("complete-boundary-wang-map", "D22", "proof",
       item(12),
       new_between("Finally, the Wang sequence", r"\emph{Relative normal discs"),
       "Subtract the full marked normal part and use the exact saturated fibre kernel in the integral Wang sequence, including boundary torsion.")
defect("finite-first-and-bridge-inverse", "D22", "proof",
       between(item(13), "The relative pair argument",
                   "The top component counts"),
       sec("Finite-first attachment retaining the angular torsion."),
       "Retain g delta, all power columns, the distinct cusp meridians and the complete component matrix; construct the Mz=Pz' kernel, geometric splitting and inverse.")
defect("weighted-count-rule", "D20", "proof",
       between(item(13), "The top component counts"),
       sec("Free ranks and every integral homology group."),
       "Write the powered component-count rule rho_i(d), rank-one gcd, bridge rank and duality coordinates explicitly. Unchanged formulas are evaluated at the actual d; no constant weight-one component count is inferred.")
defect("full-seifert-generator-maps", "D22", "proof",
       between(item(14), "The vertical normal closures",
                   "The argument has not used"),
       sec("The full fundamental group for all weights and orders."),
       "Give the complete vertical normal closure, the two original-star exceptional maps, both generator maps and the unbounded Seifert abelianization.")
defect("positive-unbounded-scope", "D02", "proof",
       "The argument has not used a bound on weights\nor logarithmic parameters.",
       new_between("The formulas for the graph, finite actions",
                   r"\emph{The role of oddness.}"),
       "State the full parameter range positively, with both catalogue domains and their exact maps.")
defect("even-marking-witness", "D22", "proof",
       between(item(14), "It uses oddness"),
       sec("The role of oddness."),
       "Supply the actual OS43/default even-g example, exact order-two fibre class and two distinct anti-invariant lifts, with the addition inverse. This is post-exposure auxiliary evidence only.")

fields = ["change_id", "type", "statement_id", "old_location", "old_page",
          "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
write_tsv("defects", fields, defects)
assert len(defects) == 34
assert sum(r["type"] == "D26" for r in defects) == 1
assert not any(r["type"] in ("D25", "D27") for r in defects)
print("PASS 34 narrowly typed correction rows; one D26, no D25 or D27")
for row in defects:
    print("DEFECT", row["type"], row["change_id"], row["old_location"],
          "->", row["new_location"])

fresh_files = [
    PREFIX+x for x in (
        "fresh_derivation.md", "fresh_local_maps.md", "fresh_source_scope.md",
        "fresh_calculation_readout.md", "attempt_record.md", "fresh_local_data.json",
        "fresh_finite_data.json", "fresh_global_data.json", "fresh_patterns.json",
        "saved_data_audit_v2.md",
    )
]
fresh_where = [str((LANE/x).relative_to(ROOT)) for x in fresh_files]
fresh_where += [
    "agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_02LH_packet.tex",
    "agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LH_fresh_review.md",
]
fresh_programs = (
    "integral", "exterior_local_v1", "exterior_local_v2", "exterior_local_v3",
    "component_denominators_v1", "catalogue_v1", "runtime_probe_v1",
    "readout_v1", "format_v1", "format_v2", "format_v3",
    "saved_audit_v1", "saved_audit_v2",
)
for stem in fresh_programs:
    for extension in (".py", ".out", ".err"):
        path = ROOT/"code"/("S6_SERIES_PUBLISH_c7_lh_"+stem+extension)
        if path.exists():
            fresh_where.append(str(path.relative_to(ROOT)))
post_where = [str((LANE/(PREFIX+x)).relative_to(ROOT)) for x in (
    "released_statement.tex", "released_proof.tex", "post_exposure_derivation.md",
    "post_exposure_data.json", "receiving.tex", "comparison.md",
    "replacements.tsv", "defects.tsv",
)]
for stem in ("post_exposure_v1", "receiver_v1", "receiver_v2", "receiver_v3",
             "receiver_v4", "receiver_check_v1", "receiver_check_v2",
             "prepare_packets_v1"):
    for extension in (".py", ".out", ".err"):
        post_where.append("code/S6_SERIES_PUBLISH_c7_lh_"+stem+extension)
assert all((ROOT/p).exists() for p in fresh_where+post_where)
now = datetime.now(timezone.utc).isoformat()
common = dict(
    statement_id=ID, date="2026-11-25",
    who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed",
    source_file="S6_SERIES_PUBLISH_III.tex", source_row=16765,
    evidence_group="publish:c7:III:02LH:check-sequence",
    publish_input_file=str((LANE/(PREFIX+"comparison.md")).relative_to(ROOT)),
    publish_input_row=1, date_utc=now,
)
events = [
    dict(common, type="targeted proof check",
         event_id="publish:c7:III:02LH:fresh-complete-derivation",
         phase="before whole original LH exposure",
         source_event_type="targeted proof check",
         where="; ".join(fresh_where),
         outcome=(
             "Complete statement-only LH derivation frozen 2026-11-25T04:21:45Z, "
             "with exhaustive saved-data audit completed and frozen 04:43:14 UTC, "
             "before individual original release 04:45:22.657861 UTC. Proved all-d "
             "coefficient images, full Z plus Z/g fibre quotient, actual period "
             "and graph maps, odd doubled-cocycle splitting, every finite projected "
             "lattice and proper-power criterion, complete Thom columns, every "
             "unchanged-cap free target and saturated transfer kernel, distinct "
             "cusp meridians, finite-first inverse splitting, full Seifert group "
             "and all integral homology. Independently computed 172 rows, 495/459 "
             "patterns with inclusion/retraction, 2334 exteriors, 12249 local kernels, "
             "1386 finite lattices, 33264 actions and 6326 complete global matrices. "
             "All proof/source/output read. Large JSON entries were exhaustively "
             "verified computationally, not all manually read. Interrupted local "
             "attempts and unobserved audit-v1 completion are preserved without "
             "success credit. Same-library audit gives no extra independent-blind "
             "credit. Target original and historical program remained closed; "
             "post-exposure auxiliaries are excluded from this event."
         )),
    dict(common, type="used and rechecked in this run",
         event_id="publish:c7:III:02LH:whole-original-comparison",
         phase="after whole original LH exposure",
         source_event_type="used and rechecked in this run",
         where="; ".join(fresh_where+post_where),
         outcome=(
             "Read and compared the entire released 58-line statement, all 219 proof "
             "lines and fourteen original items, seven displays and every auxiliary. "
             "Proved the exact involution/cocycle marking equivalence, full root "
             "generator inverse, all 172 elliptic unit right inverses and all-d mixed "
             "preimages, OS46/II index-three word inclusion, and the bounded even-g "
             "marking ambiguity. D.OW7 is true; no refutation credit. Supplied smooth "
             "collar representatives and additive specialization coordinates, plus "
             "exact omitted-return image maps. Complete 1680-line receiver read; "
             "all new sources and complete mathematical outputs read. D26 clarifies "
             "459 all-star-original versus broad 495 by exact inclusion/retraction. "
             "All group formulas and the weighted component-count rule stand. "
             "Historical program/JSON bytes absent: no historical execution, replay "
             "or bytewise comparison claimed. Two separate guards, 34 correction "
             "rows, eight labels/targets and seven equation tags preserved. Syntax "
             "checks confer no canonical/PDF/build/unit/page credit. No D25/D27 "
             "and no extra independent-blind credit. Root record admission and "
             "canonical application remain separate."
         )),
]
event_fields = ["statement_id", "date", "who", "type", "outcome", "event_id", "phase",
                "source_file", "source_row", "source_event_type", "evidence_group",
                "publish_input_file", "publish_input_row", "date_utc", "where"]
write_tsv("CHECK_EVENTS", event_fields, events)
assert len({r["evidence_group"] for r in events}) == 1
assert digest_file(CANON) == SOURCE_SHA
for suffix, expected in frozen.items():
    assert digest_file(LANE/(PREFIX+suffix)) == expected, suffix
print("PASS two narrowly scoped events in one evidence group; no extra blind credit")
print("PASS all writes confined to the LH proposal lane; canonical/global files unchanged")
for suffix in ("receiving.tex", "post_exposure_derivation.md", "comparison.md",
               "replacements.tsv", "defects.tsv", "CHECK_EVENTS.tsv"):
    print("FINAL_SHA256", PREFIX+suffix, digest_file(LANE/(PREFIX+suffix)))
print("PACKET_COMPLETE_UTC", now)
