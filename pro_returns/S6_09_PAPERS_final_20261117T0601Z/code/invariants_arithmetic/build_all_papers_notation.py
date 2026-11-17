#!/usr/bin/env python3
"""Build the common mathematical dictionary and complete result concordance.

Reads an immutable snapshot of the inventory, all three TeX files and any AUX
files. It does not edit those inputs. Numerical references are optional and are
never inferred from source order. The default is a label-only snapshot; pass
--numbers after the final typesetting pass.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[2]
WORK = PACKAGE / "work/invariants_arithmetic"
BODY = WORK / "notation_all_papers_body.md"
OUTPUT = PACKAGE / "S6_09_PAPERS_notation_sheet.md"
PAPERS = ("I", "II", "III")
MODEL = "GPT-6 Astra (OpenAI, ChatGPT Pro mode)"
EFFORT = "Pro"
REVIEW_DATE = "2026-11-17"
TICK = chr(96)

ALIASES = (
    "work/invariants_arithmetic/statement_aliases.json",
    "work/invariants_arithmetic/working_statement_aliases.json",
    "work/invariants_arithmetic/working_equation_tag_aliases.json",
    "work/maps_audit/paperI_topology_aliases.json",
    "work/maps_audit/course_geometric_PaperI_aliases.json",
    "work/cdp_audit/paperII_statement_aliases.json",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_snapshot(path: Path) -> tuple[str, dict]:
    raw = path.read_bytes()
    return raw.decode("utf-8"), {
        "path": str(path.relative_to(PACKAGE)),
        "sha256": digest(raw),
        "bytes": len(raw),
    }


def uncomment(tex: str) -> str:
    # A percent preceded by an odd number of backslashes is literal.
    out = []
    for line in tex.splitlines(keepends=True):
        cut = len(line)
        for i, c in enumerate(line):
            if c != "%":
                continue
            n = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                n += 1
                j -= 1
            if n % 2 == 0:
                cut = i
                break
        out.append(line[:cut] + ("\n" if cut < len(line) else ""))
    return "".join(out)


def brace_group(s: str, i: int) -> tuple[str, int]:
    """Read a TeX brace group, including nested and escaped braces."""
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s) or s[i] != "{":
        raise ValueError(f"Expected brace at {i}: {s[i:i+60]!r}")
    start = i + 1
    depth = 1
    i += 1
    while i < len(s):
        if s[i] == "\\":
            # Only \{ and \} escape braces; ordinary commands do not.
            if i + 1 < len(s) and s[i + 1] in "{}\\":
                i += 2
                continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[start:i], i + 1
        i += 1
    raise ValueError("Unclosed TeX brace group")


def parse_aux(s: str) -> tuple[dict[str, str], list[dict]]:
    result: dict[str, str] = {}
    repeated = []
    for m in re.finditer(r"\\newlabel(?=\s*\{)", s):
        label, j = brace_group(s, m.end())
        outer, _ = brace_group(s, j)
        if label.endswith("@cref"):
            continue
        number, _ = brace_group(outer, 0)
        if label in result:
            repeated.append({
                "label": label,
                "previous_number": result[label],
                "next_number": number,
                "different": result[label] != number,
            })
        result[label] = number
    return result, repeated


def cell(value: object) -> str:
    return str(value).replace("|", "&#124;").replace("\n", " ").strip()


def code(value: object) -> str:
    return TICK + cell(value).replace(TICK, "&#96;") + TICK


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(text, encoding="utf-8")
    temp.replace(path)


def alias_pairs(obj: object) -> list[tuple[str, str, str]]:
    if isinstance(obj, list):
        result = []
        for row in obj:
            old = row.get("source_label", row.get("source_id"))
            new = row.get("shared_printed_label", row.get("printed_label"))
            if old is None or new is None:
                raise ValueError(f"Unsupported alias record: {row}")
            result.append((str(old), str(new), "statement"))
        return result
    if not isinstance(obj, dict):
        raise TypeError("Alias file must be a dictionary or list")
    result = []
    for old, value in obj.items():
        if isinstance(value, dict):
            if "label" in value:
                result.append((old, value["label"], value.get("kind", "statement")))
            elif "printed_tag" in value:
                result.append((old, value["printed_tag"], "equation_tag"))
            else:
                raise ValueError(f"Unsupported alias object for {old}: {value}")
        else:
            result.append((old, str(value), "statement"))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--numbers", action="store_true",
        help="Include the current AUX numbers (run only after final AUX refresh).",
    )
    args = parser.parse_args()
    inputs = []
    inventory_text, meta = read_snapshot(PACKAGE / "S6_09_PAPERS_inventory.csv")
    inputs.append(meta)
    rows = list(csv.DictReader(io.StringIO(inventory_text)))
    keyed = {(row["source_run"], row["source_id"]): row for row in rows}
    if len(keyed) != len(rows):
        raise ValueError("The inventory has duplicate (source_run, source_id) keys")
    counts = collections.Counter(row["paper"] for row in rows)
    if set(counts) - set(PAPERS):
        raise ValueError(f"Unexpected paper values: {counts}")

    labels = {}
    label_counts = {}
    equation_tags = {}
    numbers = {}
    duplicate_aux = {}
    for paper in PAPERS:
        tex, meta = read_snapshot(PACKAGE / f"S6_09_PAPERS_{paper}.tex")
        inputs.append(meta)
        clean_tex = uncomment(tex)
        labs = re.findall(r"\\label\s*\{([^{}]+)\}", clean_tex)
        label_counts[paper] = collections.Counter(labs)
        labels[paper] = set(labs)
        equation_tags[paper] = collections.Counter(
            brace_group(clean_tex, m.end())[0]
            for m in re.finditer(r"\\tag\*?(?=\s*\{)", clean_tex)
        )
        auxpath = PACKAGE / f"S6_09_PAPERS_{paper}.aux"
        if args.numbers and auxpath.exists():
            aux, meta = read_snapshot(auxpath)
            inputs.append(meta)
            numbers[paper], duplicate_aux[paper] = parse_aux(aux)
        else:
            numbers[paper], duplicate_aux[paper] = {}, []

    unplaced = [
        {"source_run": r["source_run"], "source_id": r["source_id"],
         "paper": r["paper"], "printed_label": r["printed_label"]}
        for r in rows
        if r["printed_label"] not in labels.get(r["paper"], set())
    ]
    if unplaced:
        raise ValueError(f"Inventory destinations absent from actual TeX: {unplaced}")

    canonical = {r["printed_label"] for r in rows}

    def canonical_label(lab: str) -> str:
        # Earlier scoped alias files predate the canonical result namespace.
        # Preserve the old destination as data and make the conversion explicit.
        if lab.startswith("fam:st:"):
            candidate = "fam:src:" + lab.removeprefix("fam:st:")
            if candidate in canonical:
                return candidate
        return lab

    def places(lab: str) -> list[str]:
        return [p for p in PAPERS if lab in labels[p]]

    def loc(lab: str, paper: str | None = None) -> str:
        lab = canonical_label(lab)
        found = [p for p in places(lab) if paper is None or p == paper]
        if not found:
            raise ValueError(f"Notation destination is absent: {lab}")
        parts = []
        for p in found:
            num = numbers[p].get(lab, "") if args.numbers else ""
            parts.append(f"Paper {p}, {code(lab)}" + (f" (number {code(num)})" if num else ""))
        return "; ".join(parts)

    body, meta = read_snapshot(BODY)
    inputs.append(meta)
    body = body.replace(
        "{{inventory_summary}}",
        "; ".join(f"Paper {p}: {counts[p]} rows" for p in PAPERS) + ".",
    ).replace("{{inventory_count}}", str(len(rows)))
    body_refs = []

    def result_ref(m: re.Match) -> str:
        key = (m[1], m[2])
        if key not in keyed:
            raise KeyError(f"Unknown notation result placeholder: {key}")
        row = keyed[key]
        body_refs.append({
            "source_run": key[0], "source_id": key[1],
            "paper": row["paper"], "printed_label": row["printed_label"],
        })
        return loc(row["printed_label"], row["paper"])

    body = re.sub(r"\{\{result\s+(\S+)\s+(\S+)\}\}", result_ref, body)

    def label_ref(m: re.Match) -> str:
        lab = canonical_label(m[1])
        body_refs.append({"printed_label": lab, "papers": places(lab)})
        return loc(lab)

    body = re.sub(r"\{\{label\s+(\S+)\}\}", label_ref, body)
    if "{{" in body or "}}" in body:
        # TeX nested braces legitimately contain "}}"; inspect only placeholders.
        if re.search(r"\{\{(?:result|label|inventory)[^}]*\}\}", body):
            raise ValueError("Unresolved notation template placeholder")
    mode = (
        "Numbers below are the available AUX values in this recorded snapshot."
        if args.numbers else
        "This is a label-only snapshot. Run the generator with --numbers after "
        "the final AUX refresh to add current printed numbers."
    )
    body += "\n\n## Appendix A. Every inventory result and its actual destination\n\n"
    body += mode + "\n\n"
    body += "| Source run | Original result identifier | Paper | Printed label | Current number |\n"
    body += "|---|---|---|---|---|\n"
    result_map = []
    missing_numbers = []
    for row in rows:
        p, lab = row["paper"], row["printed_label"]
        number = numbers[p].get(lab, "")
        if args.numbers and not number:
            missing_numbers.append({"paper": p, "label": lab, "source_id": row["source_id"]})
        shown = code(number) if args.numbers and number else "—"
        body += (
            "| " + code(row["source_run"]) + " | " + code(row["source_id"])
            + " | " + p + " | " + code(lab) + " | " + shown + " |\n"
        )
        result_map.append({
            "source_run": row["source_run"],
            "source_id": row["source_id"],
            "paper": p,
            "printed_label": lab,
            "aux_number": number or None,
            "actual_tex_label_found": True,
        })

    body += "\n## Appendix B. Explicit statement and equation aliases\n\n"
    body += (
        "Each table identifies its source alias file. When an earlier FAMILY "
        "destination used the intermediate namespace, the recorded canonical "
        "destination is shown alongside it. Original alias files are unchanged.\n"
    )
    alias_map = []
    for rel in ALIASES:
        alias_text, meta = read_snapshot(PACKAGE / rel)
        inputs.append(meta)
        obj = json.loads(alias_text)
        body += "\n### " + code(rel) + "\n\n"
        body += "| Source label or tag | Kind | Recorded destination | Current destination |\n"
        body += "|---|---|---|---|\n"
        for old, original_dest, kind in alias_pairs(obj):
            dest = canonical_label(original_dest)
            if kind == "equation_tag":
                found = [p for p in PAPERS if dest in equation_tags[p]]
                if not found:
                    raise ValueError(f"Recorded equation tag absent from TeX: {dest}")
                where = "; ".join(
                    f"Paper {p}, equation tag {code(dest)}" for p in found
                )
            else:
                found = places(dest)
                where = loc(dest)
            body += (
                "| " + code(old) + " | " + cell(kind) + " | "
                + code(original_dest) + " | " + where + " |\n"
            )
            alias_map.append({
                "alias_file": rel, "source_label_or_tag": old, "kind": kind,
                "recorded_destination": original_dest,
                "printed_label": dest if kind != "equation_tag" else None,
                "printed_tag": dest if kind == "equation_tag" else None,
                "papers": found,
                "destination_canonicalized": dest != original_dest,
            })

    body += "\n## Appendix C. Every label present in the assembled papers\n\n"
    body += (
        "This includes equations, sections, statements and retained proof labels. "
        "A label without a number remains addressable by its exact key. "
        "No number is inferred from its position in the source.\n\n"
    )
    body += "| Paper | Actual label | Current number |\n|---|---|---|\n"
    all_label_map = []
    for paper in PAPERS:
        for lab in sorted(labels[paper]):
            num = numbers[paper].get(lab, "")
            body += (
                f"| {paper} | " + code(lab) + " | "
                + (code(num) if args.numbers and num else "—") + " |\n"
            )
            all_label_map.append({
                "paper": paper, "label": lab, "aux_number": num or None,
                "source_occurrences": label_counts[paper][lab],
            })

    changed_inputs = []
    for entry in inputs:
        path = PACKAGE / entry["path"]
        if digest(path.read_bytes()) != entry["sha256"]:
            changed_inputs.append(entry["path"])
    if changed_inputs:
        raise RuntimeError("Inputs changed during snapshot; rerun: " + ", ".join(changed_inputs))

    generated = datetime.now(timezone.utc).isoformat()
    report = {
        "schema": "S6_09_all_papers_notation_concordance_v1",
        "prepared_by": MODEL, "effort": EFFORT, "review_date_utc": REVIEW_DATE,
        "generated_at_utc": generated, "numbers_in_markdown": args.numbers,
        "aux_mode": "read_for_numbered_snapshot" if args.numbers else "not_read_for_label_only_snapshot",
        "inventory_rows": len(rows), "rows_by_paper": dict(counts),
        "paper_labels": {p: len(labels[p]) for p in PAPERS},
        "paper_explicit_equation_tags": {p: len(equation_tags[p]) for p in PAPERS},
        "all_actual_label_count": sum(map(len, labels.values())),
        "explicit_alias_count": len(alias_map),
        "body_resolved_reference_count": len(body_refs),
        "duplicate_inventory_keys": [], "unplaced_results": [],
        "missing_aux_numbers": missing_numbers,
        "duplicate_tex_labels": {
            p: {lab: n for lab, n in label_counts[p].items() if n > 1}
            for p in PAPERS
        },
        "duplicate_aux_labels": duplicate_aux,
        "input_snapshots": inputs,
        "output": str(OUTPUT.relative_to(PACKAGE)),
        "output_sha256": digest(body.encode("utf-8")),
        "regeneration": (
            "python code/invariants_arithmetic/build_all_papers_notation.py --numbers"
        ),
        "scope": (
            "Mechanical coverage and source-label resolution, together with the "
            "separately recorded mathematical notation readings. This does not "
            "replace the receiving proof or original-reference audits."
        ),
    }
    atomic_write(OUTPUT, body)
    for filename, obj in (
        ("notation_concordance.json", report),
        ("notation_label_map.json", {
            "results": result_map, "aliases": alias_map,
            "body_references": body_refs, "all_actual_labels": all_label_map,
        }),
    ):
        atomic_write(WORK / filename, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "output": str(OUTPUT), "inventory_rows": len(rows),
        "rows_by_paper": dict(counts),
        "all_actual_labels": report["all_actual_label_count"],
        "explicit_aliases": len(alias_map), "unplaced_results": 0,
        "missing_aux_numbers": len(missing_numbers),
        "numbers_in_markdown": args.numbers,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
