#!/usr/bin/env python3
"""Compare every complete checked MAPS D block with the assembled Paper III.

The prior D editorial transform preserves and corrects the source mathematics.
This pass independently checks retention after wrappers, namespace conversion,
cross-paper references and typesetting. It reads production transforms as
explicit permitted editorial rules; it never assembles or edits a paper.
"""
from __future__ import annotations
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

PACKAGE = Path(__file__).resolve().parents[2]
WORK = PACKAGE / "work/invariants_arithmetic"
sys.path.insert(0, str(PACKAGE / "code/editorial"))
from paper_ii_transform import normalize_equations, raw_refs, common_cleanup
from paper_iii_source_aliases import maps as source_aliases


def sha(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def group_end(s: str, a: int) -> int:
    level = 1
    i = a + 1
    while level:
        if i >= len(s):
            raise ValueError("Unclosed command group")
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] in "{}\\":
            i += 2
            continue
        if s[i] == "{":
            level += 1
        elif s[i] == "}":
            level -= 1
        i += 1
    return i


def clean(s: str, keep_destinations: bool = False) -> str:
    # Remove only editorial metadata, equation anchors and theorem closings.
    # Every proof word, mathematical formula, citation and reference remains.
    s = re.sub(r"^%[^\n]*\n", "", s, flags=re.M)
    pieces = []
    pos = 0
    for m in re.finditer(r"\\(Uses|label)\s*\{", s):
        if m.start() < pos:
            continue
        end = group_end(s, m.end() - 1)
        pieces.append(s[pos:m.start()])
        label = s[m.end():end - 1]
        if keep_destinations and m[1] == "label" and re.fullmatch(r"maps:src:D\.\d+\.\d+", label):
            pieces.append("@@DEST_" + label.removeprefix("maps:src:") + "@@")
        pos = end
    pieces.append(s[pos:])
    s = "".join(pieces)
    s = re.sub(r"\\end\{(?:theorem|lemma|proposition|corollary|remark|problem|computed)\}", "", s)
    return "".join(s.split())


def main() -> None:
    inventory_text = (PACKAGE / "S6_09_PAPERS_inventory.csv").read_text()
    inventory = list(csv.DictReader(inventory_text.splitlines()))
    allmaps = [r for r in inventory if r["source_run"] == "S6_04_MAPS_MANIFOLDS"]
    manifest_text = (PACKAGE / "work/root/III_assembly_manifest.json").read_text()
    manifest = json.loads(manifest_text)
    blocks = [r for r in manifest["source_result_blocks"] if r["source_id"].startswith("D.")]
    expected_ids = ([f"D.1.{i}" for i in range(1,13)]
                    + [f"D.2.{i}" for i in range(1,54)]
                    + [f"D.3.{i}" for i in range(1,5)])
    if [r["source_id"] for r in blocks] != expected_ids:
        raise ValueError("Expected all 69 D blocks in their original order")
    for row in blocks:
        if sha(row["complete_expanded_source"]) != row["expanded_original_sha256"]:
            raise ValueError("Expanded source hash mismatch: " + row["source_id"])
    final = (PACKAGE / "S6_09_PAPERS_III.tex").read_text()
    available = set(re.findall(r"\\label\{([^}]+)\}", final))
    s = "\n".join("@@BLOCK_" + r["source_id"] + "@@\n" + r["complete_expanded_source"] for r in blocks)
    s = source_aliases(s)
    prefixes = ("maps:","mapsIII:","mapsD:","courseIII:","mapsaudit:",
                "fam:","push:","inv:","cdp:","mapsI:","wb:")

    def namespace(m):
        vals = [x if x.startswith(prefixes) else "maps:" + x for x in m[2].split(",")]
        return "\\" + m[1] + "{" + ",".join(vals) + "}"

    s = re.sub(r"\\(label|ref|eqref|cref|Cref|autoref)\{([^}]+)\}", namespace, s)
    s, _ = normalize_equations(s, "maps")
    s = raw_refs(s, [r["source_id"] for r in allmaps], "maps:src:")
    s = common_cleanup(s)
    s = re.sub(r"\\(sub)*section\{[A-F]\.\d*\.?\s*",
               lambda m: "\\" + (m[1] or "") + "section{", s)
    s = s.replace("We claim no priority for that general algorithm.",
                  "The general algorithm is credited to its published source.")
    s = re.sub(r"(?:No|no) (?:novelty or )?priority claim\s+is made[^.]*\.", "", s)
    s = re.sub(r"(?:The )?statement makes no priority claim\.", "", s)
    s = re.sub(r";?\s*we claim no priority for integral-conjugacy\s+algorithms\.", ".", s)
    s = s.replace("No claim of priority is made.", "")
    s = s.replace("This states the search outcome and claims no priority.",
                  "This states the search outcome.")
    s = s.replace("{DGKXv1}", "{DuEtAl2026v1}")
    for row in allmaps:
        if row["paper"] != "III" and row["printed_label"]:
            s = s.replace("{maps:src:" + row["source_id"] + "}",
                          "{" + row["printed_label"] + "}")
    aux_inputs = []
    for paper in ("I", "II"):
        aux = (PACKAGE / f"S6_09_PAPERS_{paper}.aux").read_text()
        aux_inputs.append({"paper": paper, "sha256": sha(aux)})
        nums = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]+)\}", aux))
        kinds = dict(re.findall(r"\\newlabel\{([^}]+)@cref\}\{\{\[([^\]]+)\]", aux))

        def external(m):
            out = []
            for key in m[2].split(","):
                if key in nums and key not in available:
                    kind = "Equation" if m[1] == "eqref" else kinds.get(key, "result").capitalize()
                    out.append("Paper~" + paper + ", " + kind + "~" + nums[key])
                else:
                    out.append("\\" + m[1] + "{" + key + "}")
            return " and ".join(out)

        s = re.sub(r"\\(ref|eqref|cref|Cref|autoref)\{([^}]+)\}", external, s)
    # The only algebraically neutral command replacement in the global layout
    # pass that can affect this subject is the standard binomial notation.
    s = s.replace(r"{u_\alpha\choose2}", r"\binom{u_\alpha}{2}")
    # The final standalone-reference pass converts this exact, verified AC26
    # locator into a bibliography citation.  Independently inspected against
    # final_standalone_fixes.py; no statement or proof expression changes.
    citation_before = ("The presentation of the fundamental group in the supplied\n"
                       r"\textup{[AC26, Theorem 7.17]} sends")
    citation_after = ("The presentation of the fundamental group in\n"
                      r"\cite[Theorem~7.17]{AC26} sends")
    if s.count(citation_before) != 1:
        raise ValueError("Expected the one D.1.2 source-citation conversion")
    s = s.replace(citation_before, citation_after)
    cleaned_final = clean(final, keep_destinations=True)
    parts = re.split(r"@@BLOCK_(D\.\d+\.\d+)@@", s)[1:]
    source_by_id = {r["source_id"]: r for r in blocks}
    results = []
    failures_dir = WORK / "maps_D_source_to_print_differences"
    failures_dir.mkdir(exist_ok=True)
    for sid, expected_raw in zip(parts[::2], parts[1::2]):
        expected = clean(expected_raw)
        marker = "@@DEST_" + sid + "@@"
        if cleaned_final.count(marker) != 1:
            raise ValueError("D destination not unique: " + sid)
        after = cleaned_final.split(marker, 1)[1]
        found_at = after.find(expected)
        # The block must begin immediately at its own statement label.
        # A later occurrence is evidence of a misplaced copy, not a pass.
        matched = found_at == 0
        original = source_by_id[sid]
        line = final[:final.index(r"\label{maps:src:" + sid + "}")].count("\n") + 1
        record = {
            "source_run": "S6_04_MAPS_MANIFOLDS", "source_id": sid,
            "paper": "III", "printed_label": "maps:src:" + sid,
            "printed_label_line": line, "routing": original["routing"],
            "expanded_checked_source_sha256": original["expanded_original_sha256"],
            "normalized_full_block_sha256": sha(expected),
            "full_block_matches_at_its_own_label": matched,
            "normalized_match_offset": found_at,
            "complete_proof_count": original["complete_expanded_source"].count(r"\begin{proof}"),
            "scope": "Every statement/proof word, display, citation and resolved reference compared; only whitespace, labels, Uses metadata and outer statement closings ignored.",
        }
        if not matched:
            # Preserve enough exact context to diagnose; no manuscript writes.
            (failures_dir / (sid + ".expected.tex")).write_text(expected_raw)
            (failures_dir / (sid + ".normalized_expected.txt")).write_text(expected)
            (failures_dir / (sid + ".normalized_actual.txt")).write_text(after[:len(expected)+2000])
        results.append(record)
    report = {
        "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro",
        "date_utc": "2026-11-17",
        "source_inventory_sha256": sha(inventory_text),
        "assembly_manifest_sha256": sha(manifest_text),
        "paper_III_sha256": sha(final), "aux_inputs": aux_inputs,
        "rows": len(results), "complete_proofs": sum(r["complete_proof_count"] for r in results),
        "passed": sum(r["full_block_matches_at_its_own_label"] for r in results),
        "failed_ids": [r["source_id"] for r in results if not r["full_block_matches_at_its_own_label"]],
        "prior_mathematical_audit": "work/invariants_arithmetic/maps_D_independent_audit.json",
        "prior_source_correction_retention": "work/invariants_arithmetic/maps_D_editorial_transform_manifest.json",
        "final_citation_normalization": {
            "source_id": "D.1.2", "before": citation_before,
            "after": citation_after,
            "production_rule": "code/editorial/final_standalone_fixes.py, III exact AC26 Theorem 7.17 rule",
            "checked": "The complete post-citation proof is identical; this exact bibliographic formatting and unavailable-prompt wording conversion is the only new permitted difference.",
        },
        "records": results,
    }
    (WORK / "maps_D_source_to_print_check.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    )
    print(json.dumps({k: report[k] for k in ("rows","complete_proofs","passed","failed_ids")}))


if __name__ == "__main__":
    main()
