#!/usr/bin/env python3
"""Archive literal candidate15 prose proposals; do not edit the paper or log."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/i_cont_edits"
SOURCE_SHA = "45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8"
PDF_SHA = "b72c6da6acddfd797c82837fbd086e222eeef8e4526ed736328affde474df780"
sha = lambda b: hashlib.sha256(b).hexdigest()

# All complete rendered statements/proofs containing these clauses were read
# on candidate15 pages271--307. Only the quoted prose is proposed for change.
PROPOSALS = [
    (276, "D11", " They do not by themselves\nidentify those numbers with the orders of the Tate--Shafarevich groups.", "", "The statement gives exact analytic BSD quotients and its complete denominator/height proof establishes those values. Delete the appended negative identification disclaimer; the actual quotient claims and the final-part Tate--Shafarevich question remain."),
    (277, "D02", "up to sign, with no additional\nminimal-model scaling.", "up to sign.", "The exact twist pullback equality and the stated invariant scalings already give the normalization used in the cancellation. Retain those maps and delete the repeated negative scaling qualifier."),
    (277, "D02", " The map\nneed not be optimal; optimality is not used below.", "", "The proof's input is the explicitly stated parametrization and its differential. Its full construction, conductor hypotheses, differential factor and degree cancellation remain; delete the subsequent negative optimality reminder."),
    (286, "D02", "For completeness, the passage from individual orbits to\nthe full division divisor does not require uniformity of\nthe equidistribution theorem in $n$. ", "", "The complete following degree, multiplicity and test-function argument proves the passage to full division divisors. Delete the introductory negative requirement claim; retain all positive bounds, limits and equations."),
    (288, "D02", ", not a\npoint of the elliptic curve.", ".", "The proof retains the explicit coordinate z=v^2=k chi^2 and the positive declaration that z is a modular-disc coordinate. Delete only its negative comparison with an elliptic point."),
    (289, "D02", ", not the Fourier nome.", ".", "The exact local formula q=2r/(1-r^2) and the sentence limiting this abbreviation to the display and estimates remain. Delete the negative notation aside."),
    (290, "D02", "They follow without special-function evaluation from", "They follow from", "The full positive arctangent/exponential-series construction, cutoffs and remainders follow immediately. Remove only the negative method qualification."),
    (295, "D02", " This also avoids treating an integral with an endpoint\nat a residue pole as an unregularized ordinary integral.", "", "The relative-homology period, third-kind differential, exponential map, signs and exact cited correspondence are stated positively and remain. Delete the aside arguing against an unregularized interpretation."),
    (296, "D11", " but makes no\nalgebraicity assertion about its theta value.", ".", "The exact real-axis identity and its modular substitution remain. Delete the appended disclaimer about an algebraicity assertion absent from the statement."),
    (296, "D02", "; no extra quotient torus\nis necessary.", ".", "The statement retains its positive use of the single motive M_R in the real case. The full bracket and centre calculation remains; remove the negative extra-torus reminder."),
    (296, "D02", ";\nthere is no deficient or Ribet exception, including for CM.", ".", "The explicit bracket 2 psi, its nonzero span Q(1), and Z'=Z=G_m remain, followed by the precise CM/non-CM pure groups and dimensions. Delete only the repeated exception disclaimer."),
    (297, "D11", "; specifying only the span of $P,Q$ would\nnot determine that last factor.", ".", "The statement and full proof specify the algebraic lift, the quotient-torus criterion for e, and its Kummer contribution. Retain that positive dependence and delete the repeated negative input-scope sentence."),
    (302, "D11", " The proof establishes this slope statement from a period\nof $G_Q$ without deciding the algebraicity of $R_N$.", "", "The statement already asserts the transcendental slope and the exact algebraicity equivalence for the compact point. The full proof retains the period vector and its separate compactness calculation. Delete only the appended account of what the proof does not decide."),
    (302, "D02", ", not $\\alpha$\nacting on an arbitrarily identified copy of $E$.", ".", "Keep the positive identification of alpha-star as the dual endomorphism and the complete subsequent principal-polarization and Rosati transport maps. Delete the negative comparison with an arbitrary identification."),
    (302, "D02", "Thus there is no additional ambiguity\nfrom $\\operatorname{Hom}(E,\\mathbb G_m)$, and the\nendomorphism is exactly $[n]$.", "Thus the endomorphism is exactly $[n]$.", "The preceding proof explicitly factors the difference through E to G_m and proves that homomorphism zero. Preserve the exact endomorphism conclusion and delete the repeated ambiguity language."),
    (302, "D02", " without any component assumption.", ".", "Retain the positive identity-component conclusion, exact doubling, negative discriminant, real-root calculation and selected real logarithm. Delete only the negative assumption aside."),
    (303, "D02", "This argument uses the period vector alone;\nit does not assume algebraicity of $N(P)$.", "This argument uses the period vector.", "The complete period-vector contradiction and transcendental-slope conclusion remain. Delete the subsequent repeated negative algebraicity-assumption disclaimer."),
    (303, "D02", ", with no imaginary logarithm\nambiguity.", ".", "The chosen logarithm is already specified as real by the displayed positive function and v=log(r/f_u(u)). Preserve these equations and the exact compactness substitution; delete the repeated ambiguity aside."),
    (303, "D02", " It cannot be discarded while retaining the\ncompactness equation.", "", "The exact CM decomposition and positive identification of the Gaussian derivative remain. Delete the instruction about an imagined discarded term."),
    (304, "D11", "; the proof does not decide the\nalgebraicity of its first coordinate alone.", ".", "The exact statement that at least one of the two coordinates is transcendental remains. The full eigenprojection, nonapproximation and slope arguments remain; remove only the appended unasserted first-coordinate scope disclaimer."),
    (306, "D02", ", without producing an algebraic\ngroup map that evaluates it.", ".", "Retain the complete Hom=0 argument, toric-slope obstruction and the positive conclusion that the construction isolates the Gaussian in a Lie eigencoordinate. Delete the repeated production disclaimer."),
    (306, "D02", " This comparison\ndoes not turn a limiting operation on complex Lie spaces\ninto an algebraic-group endomorphism or transfer a\n$p$-adic height conclusion to the real Gaussian.", "", "The exact archimedean eigenvalue gap, ordinary-prime valuations, polynomial reduction and positive comparison remain. Delete the final negative claim about unperformed transfers or limiting operations."),
]


def source_block(s, position):
    heads = list(re.finditer(r"\\begin\{(theorem|proposition|lemma|corollary|remark|definition)\}", s[:position]))
    head = heads[-1]
    statement_end = s.index(r"\end{" + head[1] + "}", head.end()) + len(r"\end{" + head[1] + "}")
    end = statement_end
    if re.match(r"\s*\\begin\{proof\}", s[end:]):
        end = s.index(r"\end{proof}", end) + len(r"\end{proof}")
    block = s[head.start():end]
    label = re.search(r"\\label\{([^}]+)\}", block)[1]
    assert head.start() <= position < end
    return label, block, statement_end - head.start()


def displays(s):
    return [re.findall(p, s) for p in [
        r"\\\[[\s\S]*?\\\]", r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$",
        r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}[\s\S]*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}"]]


def main():
    source_path = ROOT / "S6_SERIES_PUBLISH_I.tex"
    source_bytes = source_path.read_bytes()
    assert sha(source_bytes) == SOURCE_SHA
    s = source_bytes.decode()
    guards, blocks = [], {}
    for i, (page, typ, old, new, reason) in enumerate(PROPOSALS, 1):
        assert s.count(old) == 1, (i, s.count(old), old)
        pos = s.index(old)
        label, block, statement_end = source_block(s, pos)
        blocks.setdefault(label, {"original": block, "replacement": block, "statement_end": statement_end, "guards": []})
        assert blocks[label]["replacement"].count(old) == 1
        blocks[label]["replacement"] = blocks[label]["replacement"].replace(old, new, 1)
        gid = f"I15-edits-{i:02d}"
        blocks[label]["guards"].append(gid)
        inline = lambda text: re.findall(r"(?<!\\)\$(?:\\.|[^$\\])*(?<!\\)\$", text)
        old_inline, new_inline = inline(old), inline(new)
        removed = list(old_inline)
        for token in new_inline:
            if token in removed:
                removed.remove(token)
        guards.append({"id": gid, "page": page, "type": typ, "statement_id": label,
                       "source_line": s[:pos].count("\n") + 1, "old": old, "new": new, "reason": reason,
                       "source_sha256": SOURCE_SHA, "pdf_sha256": PDF_SHA,
                       "inline_math_mentions_removed_with_disclaimer": removed,
                       "inline_math_new": [token for token in new_inline if token not in old_inline],
                       "status": "proposed for consolidated root review; not applied", "mathematical_events_added": 0})
    archives = []
    for i, (label, block) in enumerate(blocks.items(), 1):
        a, b = block["original"], block["replacement"]
        assert displays(a) == displays(b)
        for p in [r"\\label\{([^}]+)\}", r"\\hypertarget\{([^}]+)\}", r"\\(?:eqref|ref|cref|Cref|cite|citet|citep)(?:\[[^\]]*\])?\{([^}]+)\}"]:
            assert re.findall(p, a) == re.findall(p, b)
        stem = OUT / f"S6_SERIES_PUBLISH_I_candidate15_edits_block_{i:02d}"
        pa, pb = Path(str(stem) + "_original.tex"), Path(str(stem) + "_proposed.tex")
        pa.write_text(a); pb.write_text(b)
        delta = Path(str(stem) + ".diff")
        delta.write_text("".join(difflib.unified_diff(a.splitlines(True), b.splitlines(True), fromfile=label + "/candidate15", tofile=label + "/proposed")))
        archive = {"statement_id": label, "original": str(pa.relative_to(ROOT)), "original_sha256": sha(pa.read_bytes()),
                   "proposed": str(pb.relative_to(ROOT)), "proposed_sha256": sha(pb.read_bytes()),
                   "diff": str(delta.relative_to(ROOT)), "diff_sha256": sha(delta.read_bytes()),
                   "guards": block["guards"], "display_math_identical": True,
                   "all_labels_targets_and_citation_reference_sequences_identical": True,
                   "complete_rendered_statement_and_proof_read": True,
                   "all_other_block_bytes_unchanged": True}
        archives.append(archive)
        for guard in guards:
            if guard["statement_id"] == label:
                guard["full_block_archive"] = archive
    assert len(blocks) == 8
    after = s
    maps = []
    for guard in guards:
        pos = after.index(guard["old"])
        maps.append((pos, guard["old"], guard["new"]))
        after = after[:pos] + guard["new"] + after[pos + len(guard["old"]):]
    reverse = after
    for pos, old, new in reversed(maps):
        assert reverse[pos:pos + len(new)] == new
        reverse = reverse[:pos] + old + reverse[pos + len(new):]
    assert reverse == s
    assert source_path.read_bytes() == source_bytes
    output = OUT / "S6_SERIES_PUBLISH_I_candidate15_edits_guards.json"
    data = {"paper": "I", "candidate": 15, "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "source_sha256": SOURCE_SHA, "pdf_sha256": PDF_SHA,
            "guards": guards, "full_blocks": archives, "source_modified": False, "mathematical_events_added": 0,
            "exact_reverse_reconstruction_of_proposal_verified": True,
            "scope": "All assigned37 whole pages271--307 actually read. Complete rendered statements/proofs for all eight affected blocks read, exact source clauses inspected and proposed differences compared. Every display, label, target, citation/reference sequence and every other block byte is preserved. Listed inline symbol mentions are removed only as part of the quoted negative/metaproof disclaimers; no operative formula, value, hypothesis, construction map or mathematical conclusion is changed.",
            "ordinary_math_retained": ["p275: exact ordinary-prime and discriminant hypotheses/exceptions", "p293: ramification/coarse saddle comparison with explicit derivatives and root expansions", "p298: unsquared rationality qualification with an explicit square-lattice divisor example", "p300: cited criteria with exact normalization maps and tangent/field/inverse-image obstructions", "p304--306: proved Hom=0, eigenprojection nonexistence/nonapproximation and algebraic-subtorus slope conclusions", "p303: genuine remaining point-algebraicity question directed to final part D"]}
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    record_path = OUT / "S6_SERIES_PUBLISH_I_final_candidate15_reading_edits.json"
    record = json.loads(record_path.read_text())
    assert [row["page"] for row in record["pages"]] == list(range(271, 308))
    assert (record["source_sha256"], record["pdf_sha256"]) == (SOURCE_SHA, PDF_SHA)
    for row in record["pages"]:
        ids = [guard["id"] for guard in guards if guard["page"] == row["page"]]
        if ids:
            row["finding"] += " Full-block review completed: exact proposals " + ", ".join(ids) + "; source remains unchanged."
    record.update({"candidate": "I_candidate15", "assigned_pages": list(range(271, 308)), "actual_full_image_reading_count": 37,
                   "source_edits": 0, "mathematical_events_added": 0,
                   "proposed_guards": [{key: guard[key] for key in ["id", "page", "type", "statement_id", "status"]} for guard in guards],
                   "guard_file": str(output.relative_to(ROOT)), "guard_file_sha256": sha(output.read_bytes()),
                   "finalized_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()})
    record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    md = ["# Paper I candidate15 — actual page reading, pages271–307", "", f"Source SHA-256: `{SOURCE_SHA}`", "", f"PDF SHA-256: `{PDF_SHA}`", "", "All37 assigned complete PNG images were individually viewed and read. The source and defect log were not changed. The22 precise prose proposals are preserved with eight complete original/proposed source blocks; root's consolidated disposition is pending. No mathematical event is claimed.", "", "| Page | Image SHA-256 | Actual finding |", "|---:|---|---|"]
    for row in record["pages"]:
        md.append(f"| {row['page']} | `{row['image_sha256']}` | {row['finding'].replace('|', '/')} |")
    md += ["", "## Guard summary", "", "| Guard | Page | Type | Statement |", "|---|---:|---|---|"]
    for guard in guards:
        md.append(f"| {guard['id']} | {guard['page']} | {guard['type']} | `{guard['statement_id']}` |")
    md += ["", "Every display and all labels, targets, citations and references are identical between the complete original and proposed blocks. The guard JSON explicitly lists inline symbol mentions contained in deleted disclaimers; those deletions leave the operative hypotheses, formulas, maps and conclusions in place. Ordinary mathematical negative statements with their exact comparison/obstruction arguments were retained.", ""]
    record_path.with_suffix(".md").write_text("\n".join(md))
    print(json.dumps({"record": str(record_path.relative_to(ROOT)), "record_sha256": sha(record_path.read_bytes()), "pages_actually_read": 37,
                      "guard_file": str(output.relative_to(ROOT)), "guard_file_sha256": sha(output.read_bytes()),
                      "guards": len(guards), "blocks": len(blocks), "types": {typ: sum(g['type']==typ for g in guards) for typ in ["D02", "D11"]},
                      "source_modified": False, "mathematical_events_added": 0}, indent=2))


if __name__ == "__main__":
    main()
