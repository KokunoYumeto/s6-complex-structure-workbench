#!/usr/bin/env python3
"""Prepare only the reviewed KV/KW comparison packets; no global writes."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "agents/continuation7_iii_original_caps"
PREFIX = "S6_SERIES_PUBLISH_III_"
CANONICAL = ROOT / "S6_SERIES_PUBLISH_III.tex"
SOURCE_BYTES = CANONICAL.read_bytes()
assert sha256(SOURCE_BYTES).hexdigest() == (
    "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0")
SOURCE = SOURCE_BYTES.decode()
META = {
    "02KV": {
        "id": "maps:src:D.2.20", "statement_span": (11499, 11560),
        "proof_span": (11563, 11816),
        "fresh": "6821df4abe8adfdde85c775ee9c34595290c4709423f56170dede39dcc810eb1",
        "proof": "98e97bea7215bf6e8e65cebfc345df2853b9e7c2b86f04bc454fc840b4331904",
        "release": "2026-11-24T21:08:35.927622+00:00", "items": 13,
    },
    "02KW": {
        "id": "maps:src:D.2.21", "statement_span": (11818, 11849),
        "proof_span": (11850, 11927),
        "fresh": "13d902518b944b1f27afd68db150eac82da379c8faa9be649c3ca1501f7e9487",
        "proof": "0a10b337b94d95a8b66a6ca82f2cb21ac1b8ab006d053411f2d2f44b5621432a",
        "release": "2026-11-24T21:08:36.488593+00:00", "items": 5,
    },
}


def write_tsv(path, fields, rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buffer.getvalue(), newline="\n")


def release(tag, kind):
    lines = (FOLDER / f"{PREFIX}{tag}_released_{kind}.tex").read_text().splitlines()
    assert len(lines) > 5 and all(x.startswith("%") for x in lines[:5])
    return "\n".join(lines[5:]).rstrip("\n")


def span(text):
    assert SOURCE.count(text) == 1
    first = SOURCE.index(text)
    start = SOURCE[:first].count("\n") + 1
    return start, start + text.count("\n")


def extract(text, start, end):
    i = text.index(start)
    j = text.index(end, i + len(start))
    return text[i:j].rstrip("\n")


def structure(old, new, tag):
    for pattern in (r"\\label\{([^}]+)\}", r"\\hypertarget\{([^}]+)\}",
                    r"\\tag\{([^}]+)\}"):
        assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, new))
    assert new.count(r"\begin{theorem}") == new.count(r"\end{theorem}") == 1
    assert new.count(r"\begin{proof}") == new.count(r"\end{proof}") == 1
    assert r"\StatementRecord" not in new
    assert "manifolds" not in new and ".py" not in new and ".json" not in new
    assert r"\small(tag " + tag + ")" in new
    assert new.count(r"\[") == new.count(r"\]")
    assert len(re.findall(r"(?<!\\)\$", new)) % 2 == 0
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", new):
        direction, env = m.groups()
        if direction == "begin":
            stack.append(env)
        else:
            assert stack and stack.pop() == env, (tag, env)
    assert not stack
    depth = 0
    for m in re.finditer(r"(?<!\\)[{}]", new):
        depth += 1 if m.group() == "{" else -1
        assert depth >= 0
    assert depth == 0


DEFECT_FIELDS = [
    "change_id", "type", "statement_id", "old_location", "old_page",
    "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
with (ROOT / "CHECK_EVENTS.tsv").open(newline="") as f:
    EVENT_FIELDS = csv.DictReader(f, delimiter="\t").fieldnames
now = datetime.now(timezone.utc)

for tag, meta in META.items():
    base = PREFIX + tag + "_"
    old_statement, old_proof = release(tag, "statement"), release(tag, "proof")
    assert span(old_statement) == meta["statement_span"]
    assert span(old_proof) == meta["proof_span"]
    assert sha256(old_proof.encode()).hexdigest() == meta["proof"]
    assert sha256((FOLDER / (base + "fresh_derivation.md")).read_bytes()).hexdigest() == meta["fresh"]
    receiver_path = FOLDER / (base + "receiving.tex")
    new = receiver_path.read_text().rstrip("\n")
    new_statement = new[:new.index(r"\begin{proof}")].rstrip("\n")
    new_proof = new[new.index(r"\begin{proof}"):]
    structure(old_statement + "\n\n" + old_proof, new, tag)
    for old_part, new_part in [(old_statement, new_statement), (old_proof, new_proof)]:
        for pattern in (r"\\label\{([^}]+)\}", r"\\hypertarget\{([^}]+)\}",
                        r"\\tag\{([^}]+)\}"):
            assert sorted(re.findall(pattern, old_part)) == sorted(re.findall(pattern, new_part))
    replacements = []
    for part, before, after in [
        ("statement", old_statement, new_statement), ("proof", old_proof, new_proof)
    ]:
        replacements.append({
            "statement_id": meta["id"], "old_text": before, "new_text": after,
            "reason": (
                f"Separate exact {part} guard, individually released at {meta['release']}; "
                f"canonical lines {meta[part+'_span'][0]}--{meta[part+'_span'][1]}. "
                "Whole-original and every auxiliary assertion comparison complete. "
                "All statement conclusions and integer parameter scopes stand. "
                "Retain exact theorem/equation labels, hypertargets and equation tags. "
                "The receiving proof supplies actual germ, lattice, boundary and inverse maps; "
                "all-parameter integer eliminations; canonical/divisor calculation; and direct "
                "oriented framed reconstruction with integral ring verification. "
                "Historical program execution claims are unverified and omitted. "
                "Root admission, source application and unit/page gates remain separate."
            ),
        })
    write_tsv(FOLDER / (base + "replacements.tsv"),
              ["statement_id", "old_text", "new_text", "reason"], replacements)

    defects = []
    old = old_statement + "\n\n" + old_proof
    def defect(suffix, kind, before, after, reason):
        assert before and before in old
        assert not after or after in new
        source_part = old_statement if before in old_statement else old_proof
        assert source_part.count(before) == 1, (tag, suffix)
        part_start = meta["statement_span"][0] if source_part is old_statement else meta["proof_span"][0]
        old_line = part_start + source_part[:source_part.index(before)].count("\n")
        defects.append({
            "change_id": f"c7-III-{tag}-{suffix}", "type": kind,
            "statement_id": meta["id"],
            "old_location": f"S6_SERIES_PUBLISH_III.tex:{old_line}", "old_page": "",
            "new_location": str(receiver_path.relative_to(ROOT)), "new_page": "",
            "old_text": before, "new_text": after, "reason": reason,
            "review_status": (
                "complete checker and root mathematical comparison; proposed for root admission; "
                "canonical application, unit criteria and final page review pending"),
        })

    header = next(x for x in old_statement.splitlines() if x.startswith(r"\StatementRecord"))
    defect("header", "D10", header, r"\textup{\small(tag " + tag + ")}",
           "Replace the machine record by the small printed permanent tag; place mathematical citations at their applications.")
    old_title = old_statement.splitlines()[0]
    new_title = new_statement.splitlines()[0]
    defect("title", "D23", old_title, new_title,
           "Give the result a short capitalized mathematical title with identical hypotheses and conclusions.")
    defect("hierarchy", "D10",
           r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]", "",
           "Replace the generated numbered hierarchy by one connected proof; every original item is compared.")
    items = old_proof.split(r"\item ")[1:]
    assert len(items) == meta["items"]
    items[-1] = items[-1].split(r"\end{enumerate}")[0]
    items = [x.rstrip("\n") for x in items]

    if tag == "02KV":
        headings = [
            r"\emph{The marked construction.}", r"\emph{The original additive caps.}",
            r"\emph{Nodes, cusp and the global exterior.}",
            r"\emph{The regular logarithm and all integral groups.}",
            r"\emph{The canonical line and the fixed normal model.}",
            r"\emph{Direct oriented reconstruction.}",
            r"\emph{The untwisted Engel member.}", r"\end{proof}"]
        sections = [extract(new, a, b) for a, b in zip(headings, headings[1:])]
        defect("group-introduction", "D08", r"For $n\ne0$, the answer is",
               r"For $n\ne0$, the integral groups are",
               "Introduce the displayed integral groups directly; their formulas and full scope are unchanged.")
        defect("zero-introduction", "D23", r"For $n=0$, it is", r"For $n=0$, they are",
               "Make the second introduction agree grammatically with the preceding integral-group description.")
        descriptions = [
            ("marked-inputs", 0, "Give the six actual defining tuples, line criterion, positive contracting convention, lattice maps and inverse period changes."),
            ("own-germ-caps", 1, "Construct the retraction, Lie logarithm, connection gauge and positive-roof maps on the original analytic germ; explicitly separate the type-II zero Euler row."),
            ("integral-cap-groups", 1, "Prove the same cap groups by the primitive circle Gysin sequence and Kunneth, with component-kernel lifts and inverse coordinates."),
            ("complete-fibre-map", 1, "Give the exact elliptic projection and invariant-covector uniqueness proving the complete integral specialization, including its component coordinates."),
            ("complete-boundary-kernel", 1, "Give the actual normal-disc sweeps and distinguish the rank-five fibre kernel before Wang from its rank-one boundary image; retain D.O6 at its stated nonzero-line scope."),
            ("global-fibre-quotient", 2, "Give the primitive global detector, explicit local fibre-kernel basis, every h value and the integer gcd-one elimination; all original constants agree."),
            ("primitive-rims", 2, "Supply the based graph injections, full primitive kernel and inverse projection together with the actual rim chains and the swept null-meridian disc."),
            ("unrestricted-log", 3, "Derive D.O8 from the actual exterior-power lattice and prove the invariant factors for every integer input, including the zero vector and the n=0 extension."),
            ("fundamental-group-map", 3, "Specify that U already includes the unchanged original caps and give the meridian-to-s map, quotient and inverse cyclic generator."),
            ("global-groups-and-model", 3, "Retain all rank counts, identify the full-cap and two-piece sequences by subdivision, and supply the duality/Bockstein/linking maps; the named Engel model is separately identified below."),
            ("canonical-and-divisor", 4, "Replace the broad canonical citation by the actual meromorphic form, free quotient, and cohomological Thom map; prove exact finite order and primitive infinite class, including all bridge coordinates."),
            ("direct-oriented-type", 5, "Replace the unspecific cancellation invocation by the direct quotient and framed-suspension maps with inverses, full zero Euler class, integral ring check and all auxiliary surgery/orbit assertions."),
        ]
        for i, (suffix, section, reason) in enumerate(descriptions):
            defect(suffix, "D22", items[i], sections[section], reason)
        # Use the exact concluding two-sentence passage from the released item.
        engel = items[9][items[9].index("In particular"):]
        defect("engel-model", "D22", engel, sections[6],
               "Identify the actual named untwisted member by inverse base, Weierstrass, section, divisor-line, contraction and unit-period fan maps; equality of group lists alone is not used.")
        defect("historical-program", "D09", items[12], "",
               "Remove historical program path and 4386/582 execution claims from the proof. Those historical runs were not verified; the new exact calculations and unrestricted integer proof are separately recorded.")
    else:
        headings = [
            r"\emph{The finite cap in its integral marking.}",
            r"\emph{The complement and its cyclic class.}",
            r"\emph{The complete gluing for unbounded parameters.}",
            r"\emph{Canonical class and oriented smooth type.}", r"\end{proof}"]
        sections = [extract(new, a, b) for a, b in zip(headings, headings[1:])]
        defect("historical-adjective", "D01", "Use the uncorrected degree-one data",
               "Use the degree-one data",
               "State the section data directly without referring to a correction history.")
        reasons = [
            "Construct the literal integral basis, original-germ maps, finite affine action, mapping-torus coordinates and inverse maps; verify the complete primitive graph basis.",
            "Retain the original component circle bundle and its complete fibre map, the primitive cusp map, and the intermediate exterior Z/h with its actual sweep and inverse splitting.",
            "Give every cap boundary map and the full all-parameter elimination retaining Z/h; construct the exact normal-kernel tori and transfer coordinate maps that recover the original small presentation.",
            "Give the exact gamma=mz generator relation with its Bezout inverse, identify the two Mayer--Vietoris subdivisions, and compute all integral groups with explicit duality coordinates.",
            "Prove the exact reduced-divisor order and canonical multiple, angular freeness, null fixed class and projectable-spin surgery; prove the same unstabilized smooth type by direct framed reconstruction and integral ring verification.",
        ]
        for i, (sec, suffix) in enumerate([(0, "actual-caps"), (1, "exterior-class"),
                                          (2, "full-finite-transfer"), (2, "groups-and-generator"),
                                          (3, "canonical-and-smooth-type")]):
            defect(suffix, "D22", items[i], sections[sec], reasons[i])
        old_code = items[0][items[0].index("The exact integer inverses"):]
        defect("historical-program", "D09", old_code, "",
               "Remove the historical program and JSON path from the proof; use the explicit construction, constants and inverse maps. No historical execution was verified.")
        old_count = items[2][items[2].index("The companion code"):]
        defect("historical-count", "D09", old_count, "",
               "Remove the unverified claim of 1068 historical full Smith checks. The actual new computations and all-parameter proof have separate records.")
        defect("duplicate-square", "D23", r"\hfill$\square$", "",
               "Remove the manual square inside the proof; the proof environment supplies its unique end marker.")

    write_tsv(FOLDER / (base + "defects.tsv"), DEFECT_FIELDS, defects)
    event_id = f"publish:c7:III:{tag}:targeted"
    result = (
        "All six original-filled configurations, every free regular logarithm, n=0 and n!=0, "
        "all integral groups, exact simple connectivity, both oriented signs, even m, m=1 and "
        "the actual untwisted Engel model agree. Complete cap, boundary, primitive rim, graph, "
        "rank, canonical and divisor-order assertions checked. The direct framed reconstruction "
        "proves the original unstabilized type and every integral degree-two product, replacing "
        "the unspecific cancellation invocation. Historical 4386-per-degree and 582-zero-n "
        "execution claims remain unverified and are removed."
        if tag == "02KV" else
        "All five configurations and every permitted k>0, signed n and integer r agree. "
        "Actual affine cap and boundary maps, primitive graph/norm columns, intermediate Z/h, "
        "universal Bezout cancellation, gamma=mz inverse generator map, complete integral groups, "
        "canonical/divisor order, both oriented simply connected signs and sphere exclusion checked. "
        "Direct framed reconstruction and the full integral degree-two product replace the "
        "unspecific cancellation invocation. Historical 1068 execution claim remains unverified "
        "and is removed."
    )
    where = [
        FOLDER / (base + "fresh_derivation.md"),
        ROOT / "agents/continuation7_iii_root" / (base + "fresh_root_review.md"),
        FOLDER / (base + "released_statement.tex"), FOLDER / (base + "released_proof.tex"),
        FOLDER / (base + "comparison.md"), receiver_path,
        FOLDER / (base + "replacements.tsv"), FOLDER / (base + "defects.tsv"),
        FOLDER / "S6_SERIES_PUBLISH_III_02KV_KW_fresh_scope.md",
        FOLDER / "S6_SERIES_PUBLISH_III_02KV_KW_primary_reading.md",
        FOLDER / "S6_SERIES_PUBLISH_III_02KV_KW_post_exposure_derivation.md",
        FOLDER / "S6_SERIES_PUBLISH_III_02KV_KW_post_exposure_constants.json",
        ROOT / "code/S6_SERIES_PUBLISH_c7_original_caps.py",
        ROOT / "code/S6_SERIES_PUBLISH_c7_original_caps.out",
        ROOT / "code/S6_SERIES_PUBLISH_c7_original_log_arithmetic.py",
        ROOT / "code/S6_SERIES_PUBLISH_c7_original_log_arithmetic.out",
        ROOT / "code/S6_SERIES_PUBLISH_c7_original_post_exposure.py",
        ROOT / "code/S6_SERIES_PUBLISH_c7_original_post_exposure.out",
    ]
    assert all(x.exists() for x in where)
    event = {field: "" for field in EVENT_FIELDS}
    event.update({
        "statement_id": meta["id"], "date": now.date().isoformat(),
        "who": (
            "GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; "
            "seventh-continuation original-cap checker with root full fresh/original/receiver review"),
        "type": "targeted proof check",
        "outcome": (
            "Completes the full frozen fresh derivation completed at 2026-11-24T21:05:18+00:00 "
            f"and fully reviewed before individual original release at {meta['release']}, "
            "followed by whole-original and every auxiliary assertion comparison. " + result +
            " Fresh arithmetic comprises six exterior calculations, 96 regular-log and 468 "
            "finite-log presentations at their relevant scopes. New post-exposure arithmetic "
            "checks eleven constant cases, with twelve PASS lines including summary. "
            "No new statement refutation, D25, D26 or D27 is confirmed. This is one targeted "
            "sequence; the exposed comparison and structural preparation receive no new blind "
            "proof credit. Proposed for root admission; canonical/unit/build/page gates remain pending."
        ),
        "event_id": event_id,
        "phase": "frozen fresh derivation followed by individually authorized full original and receiving comparison",
        "source_file": "S6_SERIES_PUBLISH_III.tex",
        "source_row": str(meta["statement_span"][0]),
        "source_event_type": "targeted proof check", "evidence_group": event_id,
        "publish_input_file": str((FOLDER / (base + "CHECK_EVENTS.tsv")).relative_to(ROOT)),
        "publish_input_row": "2", "date_utc": now.isoformat(),
        "where": "; ".join(str(x.relative_to(ROOT)) for x in where),
    })
    write_tsv(FOLDER / (base + "CHECK_EVENTS.tsv"), EVENT_FIELDS, [event])

    for name in ["replacements.tsv", "defects.tsv", "CHECK_EVENTS.tsv"]:
        with (FOLDER / (base + name)).open(newline="") as f:
            restored = list(csv.DictReader(f, delimiter="\t"))
        expected = replacements if name == "replacements.tsv" else defects if name == "defects.tsv" else [event]
        assert restored == expected
    print(f"PASS {tag}: separate exact statement {meta['statement_span']} and proof {meta['proof_span']} guards.")
    print(f"PASS {tag}: permanent labels/targets/tags, TeX structure, {len(defects)} exact defect rows, one proposed targeted event.")

for path in FOLDER.iterdir():
    if path.is_file() and path.suffix in (".md", ".tex", ".tsv", ".json"):
        data = path.read_bytes()
        assert not [b for b in data if b < 32 and b not in (9, 10)], str(path)
        assert data.endswith(b"\n"), str(path)
assert CANONICAL.read_bytes() == SOURCE_BYTES
print("PASS LF/control bytes; frozen fresh hashes unchanged; no canonical or global records written.")
print("Packet preparation completed", now.isoformat())
