#!/usr/bin/env python3
"""Reconcile supplied statement records without inventing proof-check events.

This program inventories and locates source text.  It does not establish any
mathematical assertion.  Present-writing proof outcomes are supplied separately.
"""
from __future__ import annotations

import argparse
import bisect
import collections
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCES = ROOT / "sources"
OUTPUT = Path(__file__).resolve().parents[1]
FIELDS = "paper label s6_09_label source_run source_id kind status main_or_supporting uses check_record credited_to in_compendium_only_because notes".split()
THEOREM_ENVS = {
    "theorem", "proposition", "lemma", "corollary", "claim", "statement",
    "definition", "remark", "example", "problem", "question", "auditrecord",
    "test", "conjecture", "exercise", "computed",
}
RUN_NAMES = {
    "FAM": "S6_02_FAMILY", "INV": "S6_01_INVARIANTS",
    "PUSH": "S6_02_PUSH", "CDP": "S6_03_CDP",
    "MAPS": "S6_04_MAPS_MANIFOLDS", "ARI": "S6_05_ARITHMETIC",
}


def argument(text: str, opening: int) -> tuple[str, int]:
    """Read a TeX brace group, retaining its exact contents."""
    assert text[opening] == "{"
    depth = 1
    j = opening + 1
    while j < len(text):
        char = text[j]
        escaped = j > 0 and text[j - 1] == "\\" and (j < 2 or text[j - 2] != "\\")
        if not escaped:
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return text[opening + 1:j], j + 1
        j += 1
    raise ValueError(f"Unterminated brace group at {opening}")


def commands(text: str, name: str):
    for m in re.finditer(r"\\" + re.escape(name) + r"\*?\s*\{", text):
        try:
            value, end = argument(text, m.end() - 1)
        except ValueError:
            continue
        yield {"start": m.start(), "end": end, "value": value}


def clean_missing_metadata(text: str) -> str:
    # The prompt requests omitted unknown dates/efforts, not these phrases.
    return re.sub(r"(?:,?\s*)(?:effort|date) not recorded", "", text, flags=re.I)


class TexIndex:
    """Exact character ranges, associated proof ranges and section membership."""
    def __init__(self, path: Path, *, source_continuations: bool = True):
        self.path = path
        self.source_continuations = source_continuations
        self.text = path.read_text()
        self.sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
        self.sections = list(commands(self.text, "section"))
        self.section_starts = [x["start"] for x in self.sections]
        self.lines = [0] + [m.end() for m in re.finditer("\n", self.text)]
        self.label_positions = collections.defaultdict(list)
        for label in commands(self.text, "label"):
            self.label_positions[label["value"]].append(label["start"])
        self.blocks = []
        stack = []
        env_re = re.compile(r"\\(begin|end)\{(" + "|".join(sorted(THEOREM_ENVS)) + r")\}")
        for m in env_re.finditer(self.text):
            direction, env = m.group(1), m.group(2)
            if direction == "begin":
                stack.append((env, m.start()))
            else:
                match = next((i for i in range(len(stack)-1, -1, -1) if stack[i][0] == env), None)
                if match is None:
                    continue
                _, start = stack.pop(match)
                self.blocks.append({"start": start, "statement_end": m.end(), "env": env})
        self.blocks.sort(key=lambda b: b["start"])
        proof_stack = []
        proofs = []
        for m in re.finditer(r"\\(begin|end)\{proof\}", self.text):
            if m.group(1) == "begin":
                proof_stack.append(m.start())
            elif proof_stack:
                start = proof_stack.pop()
                if not proof_stack:
                    proofs.append((start, m.end()))
        proofs.sort()
        for i, block in enumerate(self.blocks):
            boundary = self.blocks[i+1]["start"] if i+1 < len(self.blocks) else len(self.text)
            # A new structural section or appendix cannot supply a proof of
            # the preceding statement. This prevents an unindexed appendix
            # proof from being attached to the last theorem before it.
            structural = re.search(r'\\(?:appendix\b|(?:sub)*section\*?\s*\{)', self.text[block['statement_end']:boundary])
            if structural:
                boundary = block['statement_end'] + structural.start()
            after = [p for p in proofs if block["statement_end"] <= p[0] < boundary]
            block["proof_ranges"] = after
            block["end"] = after[-1][1] if after else block["statement_end"]
            uses_tail = self.text[block["statement_end"]:(after[0][0] if after else boundary)]
            block["uses_raw"] = [c["value"] for c in commands(uses_tail, "Uses")]
        self.starts = [b["start"] for b in self.blocks]

    def locate(self, label: str) -> dict:
        positions = self.label_positions.get(label, [])
        if not positions:
            return {"found": False, "file": str(self.path.relative_to(ROOT)), "label": label}
        position = positions[0]
        section_index = bisect.bisect_right(self.section_starts, position) - 1
        sec = self.sections[section_index] if section_index >= 0 else None
        # The smallest enclosing environment is the exact statement container.
        enclosing = [b for b in self.blocks if b["start"] <= position < b["statement_end"]]
        block = min(enclosing, key=lambda b: b["statement_end"] - b["start"]) if enclosing else None
        result = {
            "found": True, "file": str(self.path.relative_to(ROOT)), "sha256": self.sha256,
            "label": label, "label_positions": positions,
            "line": bisect.bisect_right(self.lines, position),
            "section": sec["value"] if sec else "preamble",
            "section_start": sec["start"] if sec else 0,
            "section_end": self.sections[section_index+1]["start"] if section_index+1 < len(self.sections) else len(self.text),
        }
        if block:
            result.update(block)
            result["container_kind"] = "statement_environment"
        else:
            # Some classical/course rows name a subsection or formula rather
            # than a theorem environment; retain exact section membership.
            smaller = [c for name in ("subsection", "subsubsection") for c in commands(self.text, name)]
            smaller.sort(key=lambda c: c["start"])
            before = [c for c in smaller if c["start"] <= position]
            start = before[-1]["start"] if before else result["section_start"]
            after = [c["start"] for c in smaller if c["start"] > position]
            end = min(after[0] if after else len(self.text), result["section_end"])
            result.update({"start": start, "end": end, "container_kind": "labelled_text", "proof_ranges": [], "uses_raw": []})
        # D.2.53 is followed by its explicitly titled complete cubic and
        # finite-coefficient proof outside the first proof environment.  Its
        # continuation ends at the next named moving-zero subsection.
        if self.source_continuations and label == 'maps:src:D.2.53':
            continuation_end = self.text.find(r'\subsection{Moving the zero of the linearization}', result['end'], result['section_end'])
            if continuation_end < 0:
                raise ValueError('D.2.53 explicit continuation boundary was not found')
            result['environment_and_first_proof_end'] = result['end']
            result['continuation_ranges'] = [[result['end'], continuation_end]]
            result['end'] = continuation_end
            result['continuation_note'] = 'Complete primitive cubic, critical-cycle, boundary cochain and full finite-coefficient proof printed as continuing subsections after the first supporting saturation proof.'
        arithmetic_continuations = {
            'ari:C.7.10': ('% END I_ari_cm_enlargement', 'Explicit conductor-361 polynomial witness following the first proof.'),
            'ari:C.7.11': ('% END I_ari_complexified', 'Exact finite-order criterion and triple-independence audit following the first proof.'),
            'ari:C.7.12': ('% END I_ari_division_values', 'Mahler-measure, entropy and period-rank discussion following the first proof; its mathematical scope is separately reviewed in the receiving revision.'),
        }
        if self.source_continuations and label in arithmetic_continuations:
            end_marker, note = arithmetic_continuations[label]
            continuation_end = self.text.find(end_marker, result['end'])
            if continuation_end < 0:
                raise ValueError(f'{label} explicit continuation boundary was not found')
            result['environment_and_first_proof_end'] = result['end']
            result['continuation_ranges'] = [[result['end'], continuation_end]]
            result['end'] = continuation_end
            result['continuation_note'] = note
        exact = self.text[result["start"]:result["end"]]
        refs = []
        for name in ("ref", "cref", "Cref", "eqref", "nameref", "pageref"):
            for c in commands(exact, name):
                refs.extend(x.strip() for x in c["value"].split(",") if x.strip())
        result["all_reference_labels"] = sorted(set(refs))
        result["all_labels_in_block"] = [c["value"] for c in commands(exact, "label")]
        return result


def plan_mains() -> dict[tuple[str, str], str]:
    # The identifiers explicitly named as primary/aggregated results in §2.
    # Endpoints/ranges remain individual identifiers in the provenance record.
    groups = {
        "I": {
            "FAM": "B.2.1 A.2.1 A.3.1 B.2.2 B.2.3 B.3.1 B.4.2 C.1.1 C.2.3 F.1.1 F.2.2 F.3.1 D.1.4 D.1.6 A.5.1 A.5.2 B.4.1",
            "PUSH": "E.1.2 E.4.1 A.3.2 A.1.2 A.2.2 B.4.19 B.4.33 D.1.3 D.2.3 D.3.1 D.4.8 E.2.1",
            "ARI": "C.8.1 C.8.2 C.8.3 C.8.4 C.8.5 C.4.2 C.4.4 C.2.1 C.6.3 C.8.15",
            "INV": "A3.1 A2.2 C1.1 C2.1 C3.3 A4.2 D4.5 D4.1 C3.8",
            "MAPS": "A.3.2",
        },
        "II": {
            "CDP": "A.1.1 B1 A.4.9 D.1.2 C.3.1 C4f C4a C4b C5b D.2.5 D.2.7 E6 E7 E13 E14 E15 E12 E17 E18",
            "PUSH": "E.2.23 E.2.24", "INV": "E2.4 E2.3",
        },
        "III": {"MAPS": "A.2.2 B.1.2 B.2.1 B.3.1 B.5.1 C.1.3 D.1.1 D.1.2 D.1.3 D.1.4 D.1.5 D.1.6 D.1.7 D.1.8 D.1.9 D.1.10 D.1.11 D.2.28 D.2.44 D.2.45 D.2.46 D.2.47 D.2.48 D.3.1 D.3.2 D.3.3 E.2.1 D.2.4"},
        "IV": {"PUSH": "C.3.24 C.3.27", "MAPS": "B.6.24"},
        "V": {"MAPS": "F.2.5 F.2.6 F.3.5 F.3.6 F.3.7 F.4.1 F.2.39 F.3.4 F.3.11"},
        "VI": {"CDP": "C.2.G.1"},
    }
    return {(RUN_NAMES[run], sid): paper for paper, runsets in groups.items() for run, ids in runsets.items() for sid in ids.split()}


def suggested_paper(row: dict, location: dict) -> str:
    old = row["paper"]
    label = row["printed_label"]
    sec = location.get("section", "")
    if old == "II" and (sec in {
        "Unrestricted Euler topology and component covers",
        "Irreducible and reducible torus-fibre Euler criteria",
        "Normal-crossing topology and canonical-flat component comparisons",
        "Compact occurrence of prescribed component classes",
        "Marked Hopf, ruled and elliptic supports with all multiplicities",
        "Actual contractions, canonical reduction and finite generation",
    } or label == "cdp:st:C.2.G.1"):
        return "VI"
    if old == "III":
        if sec == "The rank-three search and a parity obstruction" or (row["source_run"] == "S6_04_MAPS_MANIFOLDS" and row["source_id"].startswith("F.")):
            return "V"
        if sec in {"C. Smooth monodromy and the seven-dimensional invariant", "The parameter-loop reduction in the family marking"}:
            return "IV"
        if row["source_run"] == "S6_04_MAPS_MANIFOLDS" and row["source_id"].startswith("B.6"):
            return "IV"
    return old


def compendium_reason(row: dict, location: dict) -> tuple[str, str]:
    """Conservative, explicit editorial placements; uncertain novelty stays in."""
    run, kind, label = row["source_run"], row["kind"], row["printed_label"]
    sec = location.get("section", "")
    exception = label in {"fam:src:A.5.1", "fam:src:A.5.2", "fam:st:A.5.2", "inv:D1.1", "inv:D1.2", "fam:src:B.4.1"}
    if exception:
        return "", "credited appendix exception; proof review pending"
    if "Classical" in kind or "course" in run.lower() or label.startswith("courseIII:"):
        return "classical: source retains the full derivation; exact external citation still requires current verification", "plan §3 classical/course material"
    if kind == "Cited/re-derived":
        return "known: credited re-derivation retained in the compendium; exact citation pending current verification", "inventory kind and plan condition 2"
    construction_secs = {
        "The analytic threefold constructed in the candidate",
        "Exact integral algebra of the printed monodromy data",
        "Integral topology without the cusp-collapse argument",
        "The alternate collapse and Mayer--Vietoris route",
        "The direct algebraic-reduction proof",
    }
    if row["paper"] == "I" and sec in construction_secs:
        return "known or second proof: construction/topology re-derivation retained in compendium; receiving new lemmas require separate review", "plan §3 identifies construction/topology appendix re-derivations"
    if sec in {"Elementary integral chain constructions", "Actual CW models and the first Hurewicz map", "Path fibres and integral homotopy equivalences", "The orientation generator and the path-fibration proof"}:
        return "classical: chain, CW and path-fibration derivation retained in compendium", "plan Paper I moved-out classical chapters"
    if sec == "A second root-bundle derivation of the Kuranishi statement":
        return "second proof: root-bundle re-derivation retained in compendium; credited appendix contains selected proof", "plan second-proof rule"
    if kind in {"Verification record", "Computational diagnostic"}:
        return "apparatus: verification/diagnostic record retained with source computation", "subject to receiving-proof dependency review"
    return "", "candidate body placement; source-credit and proof reviews pending"


def source_status(row: dict) -> str:
    m = re.search(r"SOURCE STATUS: (.*?)(?: \| |$)", row["notes"])
    status = m.group(1) if m else row["kind"]
    if row["kind"] == "Conditional theorem":
        return "open: period-conjecture premise remains unresolved; source records an implication"
    if "open" in row["kind"].lower() and "settled" not in row["kind"].lower():
        return "open; historical record: " + status
    return "historical record: " + status + "; current-writing proof review pending"


def night_plan_map(plan_text: str) -> dict:
    mapping = {}
    for line in plan_text.splitlines():
        cols = [x.strip() for x in line.split("|")]
        if len(cols) >= 7 and re.fullmatch(r"P\d[A-Z]?\.\d+", cols[1]):
            dest = cols[4].split(":", 1)[0]
            if dest in {"I", "II", "III", "IV", "V", "VI"}:
                mapping[cols[1]] = {"paper": dest, "source_placement": cols[4], "historical_kind": cols[5]}
    return mapping


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--night-dir", type=Path, default=SOURCES / "newer_night" / "checkpoint30")
    p.add_argument("--night-checkpoint", default="30")
    p.add_argument("--night-date", default="2026-11-18")
    args = p.parse_args()
    (OUTPUT / "analysis").mkdir(parents=True, exist_ok=True)
    input_inventory = SOURCES / "s6_09/S6_09_PAPERS_inventory.csv"
    source_rows = list(csv.DictReader(input_inventory.open()))
    ledger_rows = list(csv.DictReader((SOURCES / "checks/S6_CHECK_LEDGER.tsv").open(), delimiter="\t"))
    ledger = {(r["source_run"], r["source_id"]): r for r in ledger_rows}
    indexes = {paper: TexIndex(SOURCES / f"s6_09/S6_09_PAPERS_{paper}.tex") for paper in ("I", "II", "III")}
    mains = plan_mains()
    out_rows, index_records = [], {}
    for r in source_rows:
        key = (r["source_run"], r["source_id"])
        row_key = ":".join(key)
        location = indexes[r["paper"]].locate(r["printed_label"])
        reason, placement_note = compendium_reason(r, location)
        dest = mains.get(key, suggested_paper(r, location))
        record = ledger.get(key)
        check = {
            "current_writing": "proof review pending; this inventory operation is a source-location and metadata reconciliation only",
            "s6_09_recorded_checks": r["recorded_checks"],
            "s6_09_writing_check": r["your_check"],
            "ledger": record["checks"] if record else None,
            "ledger_count_as_recorded": record["earlier_checks"] if record else None,
            "ledger_discussions_are_checks": False,
        }
        notes = {
            "row_key": row_key,
            "source_compendium_paper": r["paper"],
            "source_compendium_label": r["printed_label"],
            "source_file": r["source_file"],
            "source_line": location.get("line"),
            "source_section": location.get("section"),
            "placement_basis": placement_note,
            "placement_state": "provisional editorial mapping; no current mathematical validation inferred",
            "source_kind": r["kind"],
            "source_statement": r["statement_as_printed"],
            "historical_literature_checks": {k: r[k] for k in ("found_in_AC26", "found_in_E26", "found_in_DGKX_v1", "found_elsewhere")},
            "historical_source_notes": r["notes"],
        }
        out_rows.append({
            "paper": dest, "label": r["printed_label"], "s6_09_label": r["printed_label"],
            "source_run": key[0], "source_id": key[1], "kind": r["kind"],
            "status": source_status(r), "main_or_supporting": "main" if key in mains else "supporting",
            "uses": " | ".join(location.get("uses_raw", [])) or "; ".join(location.get("all_reference_labels", [])),
            "check_record": json.dumps(check, ensure_ascii=False),
            "credited_to": r["credited_to"], "in_compendium_only_because": reason,
            "notes": json.dumps(notes, ensure_ascii=False),
        })
        index_records[row_key] = location
    night_file = args.night_dir / "S6_06_BLIND_results.csv"
    night_rows = list(csv.DictReader(night_file.open()))
    nmap = night_plan_map((SOURCES / "plan/KEEP_SKETCH_20261117.md").read_text())
    night_main = {"P3K.31", "P3K.33", "P3F.35", "P3K.23", "P3K.10", "P3F.21", "P3K.22", "P3K.30", "P3F.53", "P3K.36", "P3F.34", "P4.58", "P1A.1", "P1A.2", "P1A.3", "P1A.4", "P1A.5", "P1A.6", "P1.13", "P1.17", "P1.18", "P2.2", "P2.7", "P2.9"}
    for r in night_rows:
        sid = r["id"]
        old = nmap.get(sid, {})
        dest = old.get("paper") or {"P1": "V", "P2": "I", "P3": "IV", "P4": "II", "P5": "I"}[sid[:2]]
        notes = {
            "row_key": "S6_06_BLIND:" + sid, "night_checkpoint": args.night_checkpoint,
            "source_file": str(night_file), "where_proved": r["where_proved"],
            "source_statement": r["statement"], "source_status": r["status"],
            "item_of_the_prompt": r["item_of_the_prompt"],
            "stated_value_compared": r["stated_value_compared (run and id)"],
            "agrees_with_stated_value": r["agrees_with_stated_value"],
            "source_notes": r["notes"],
            "checkpoint12_plan_placement": old or "row added after plan checkpoint 12",
            "placement_state": "provisional; newer corrections govern historical assertions",
        }
        known = r["status"].lower() == "known"
        status = "open; source records open" if r["status"].lower() == "open" else "historical record: " + r["status"] + "; current-writing proof review pending"
        out_rows.append({
            "paper": dest, "label": "night:" + sid, "s6_09_label": "", "source_run": "S6_06_BLIND", "source_id": sid,
            "kind": "Correction or counterexample (source refutation)" if r["status"] == "Refuted" else ("Known result" if known else old.get("historical_kind", "night-run result")),
            "status": status, "main_or_supporting": "main" if sid in night_main else "supporting",
            "uses": r["depends_on"],
            "check_record": f"Historical S6_06_BLIND re-derivation by GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), production run 16-18 November 2026, checkpoint {args.night_checkpoint} snapshot {args.night_date}; source status {r['status']}; individual check date is retained where the source supplies it. Current-writing proof review pending. No claim of blindness is made.",
            "credited_to": "Source credit and literature comparison pending current reading; see source statement and comparison fields",
            "in_compendium_only_because": ("second proof: source-specific diffeomorphism conclusion is shared with maps:src:F.4.1; its Wall comparison and Kramer-Stolz input belong in the selected Paper V proof" if sid == "P1.14" else "known: cited background; source proof retained in night-run record") if known else "",
            "notes": json.dumps(notes, ensure_ascii=False),
        })
    # Night statement names are arguments of the statement environment, not
    # source labels.  Locate their exact receiving proof ranges explicitly.
    for path in sorted((args.night_dir / "notes").glob("*.tex")):
        text = path.read_text()
        matches = list(re.finditer(r"\\begin\{statement\}\{(P[^}]+)\}\{([^}]+)\}", text))
        if not matches:
            continue
        ti = TexIndex(path.resolve())
        by_start = {b["start"]: b for b in ti.blocks}
        for m in matches:
            block = by_start.get(m.start())
            if block is None:
                continue
            sid = m.group(1)
            exact = text[block["start"]:block["end"]]
            index_records["S6_06_BLIND:" + sid] = {
                **block, "found": True, "file": str(path.resolve().relative_to(ROOT)),
                "sha256": ti.sha256, "label": "night:" + sid,
                "source_status": m.group(2), "container_kind": "night_statement_environment",
                "line": text[:m.start()].count("\n") + 1,
                "all_labels_in_block": [c["value"] for c in commands(exact, "label")],
                "all_reference_labels": sorted({x.strip() for name in ("ref", "cref", "Cref", "eqref") for c in commands(exact, name) for x in c["value"].split(",")}),
            }
            # K38's exact all-branch verification is printed after its proof
            # environment.  It is still the mathematical continuation of
            # IM.24 and must travel with this statement in a receiving proof.
            if sid == "P3K.38":
                tail = text[block["end"]:]
                marker = r"\textbf{7. Executed certificate and complete branch coverage}"
                if marker in tail and r"\end{longtable}" in tail:
                    if r"\begin{statement}" in tail:
                        raise ValueError("K38 continuation unexpectedly contains another statement")
                    loc = index_records["S6_06_BLIND:" + sid]
                    loc["original_proof_end"] = block["end"]
                    loc["post_proof_mathematical_continuation"] = {
                        "start": block["end"], "end": len(text),
                        "reason": "The full thirty-branch denominator table and exact certificate establish IM.24; source §7 follows the end-proof marker.",
                    }
                    loc["end"] = len(text)
    # Some checkpoint exports contain complete named statement/proof blocks
    # before their central CSV is updated. Keep these explicit source objects
    # in the inventory, without changing the frozen CSV or awarding a check.
    registered_night_ids = {r['id'] for r in night_rows}
    unregistered_night_exports = []
    for key, loc in list(index_records.items()):
        if not key.startswith('S6_06_BLIND:'):
            continue
        sid = key.split(':', 1)[1]
        if sid in registered_night_ids:
            continue
        exact = (ROOT / loc['file']).read_text()[loc['start']:loc['end']]
        notes = {'row_key': key, 'night_checkpoint': args.night_checkpoint,
                 'source_file': loc['file'], 'source_line': loc['line'],
                 'source_status': loc['source_status'],
                 'source_block_sha256': hashlib.sha256(exact.encode()).hexdigest(),
                 'source_kind': 'explicit named TeX statement/proof export absent from the checkpoint central CSV',
                 'absent_from_central_csv': True, 'receiving_integration_pending': True,
                 'placement_state': 'provisional receiving candidate; not in the checkpoint-04 frozen manuscript',
                 'current_check_state': 'unreviewed in this writing; source Proved status is not a current proof check'}
        out_rows.append({
            'paper': {'P1':'V','P2':'I','P3':'IV','P4':'II','P5':'I'}[sid[:2]],
            'label': 'night:' + sid, 's6_09_label': '', 'source_run': 'S6_06_BLIND',
            'source_id': sid, 'kind': 'Supplemental night TeX export; receiving review pending',
            'status': 'source export: ' + loc['source_status'] + '; current-writing proof review pending; manuscript integration pending',
            'main_or_supporting': 'main', 'uses': '; '.join(loc['all_reference_labels']),
            'check_record': 'Source status and exact statement/proof boundaries extracted only. No current mathematical, computational or human check is assigned by this intake.',
            'credited_to': 'Night-run source export; literature comparison and current proof reading pending',
            'in_compendium_only_because': '', 'notes': json.dumps(notes, ensure_ascii=False),
        })
        unregistered_night_exports.append(sid)
    # These labelled receiving lemmas are printed in S6_09 but lack their own
    # source-inventory rows.  They remain separate from the 1,184 source rows.
    supplementary = [
        ("V", "mapsaudit:order-four-torsion-transgression", "order-four-torsion-transgression"),
        ("III", "mapsIII:carrier-three-complex-wedge", "carrier-three-complex-wedge"),
        ("III", "mapsaudit:finite-degree-three", "finite-degree-three"),
    ]
    for paper, label, sid in supplementary:
        loc = indexes["III"].locate(label)
        if not loc["found"]:
            raise ValueError("Supplementary printed source lemma missing: " + label)
        key = "S6_09_SUPPLEMENT:" + sid
        index_records[key] = loc
        out_rows.append({
            "paper": paper, "label": label, "s6_09_label": label,
            "source_run": "S6_09_SUPPLEMENT", "source_id": sid,
            "kind": "Supporting lemma omitted from source inventory",
            "status": "historical S6_09 source proof; current-writing proof review pending",
            "main_or_supporting": "supporting",
            "uses": " | ".join(loc.get("uses_raw", [])) or "; ".join(loc.get("all_reference_labels", [])),
            "check_record": json.dumps({"historical": "S6_09 manuscript writing and checking record: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 16-17 November 2026", "current_writing": "proof review pending"}),
            "credited_to": "S6_09_PAPERS receiving proof; literature comparison pending current reading",
            "in_compendium_only_because": "",
            "notes": json.dumps({"source_file": loc["file"], "source_line": loc["line"], "source_inventory_gap": "Labelled supporting statement printed in source TeX but absent from its 1,184-row inventory; added without altering any original source row."}),
        })
    additions_path = OUTPUT / "analysis/inventory_additions.json"
    additions = json.loads(additions_path.read_text()) if additions_path.exists() else []
    for addition in additions:
        row = {k: str(addition.get(k, "")) for k in FIELDS}
        key = row["source_run"] + ":" + row["source_id"]
        if any(r["source_run"] + ":" + r["source_id"] == key for r in out_rows):
            raise ValueError("Duplicate additional inventory row: " + key)
        out_rows.append(row)
        if addition.get("_source_file"):
            index_records[key] = TexIndex(ROOT / addition["_source_file"]).locate(row["label"])
    overrides_path = OUTPUT / "analysis/inventory_overrides.json"
    overrides = json.loads(overrides_path.read_text()) if overrides_path.exists() else {}
    for row in out_rows:
        override = overrides.get(row["source_run"] + ":" + row["source_id"], {})
        for field, value in override.items():
            if field == "_notes":
                notes = json.loads(row["notes"])
                notes.update(value)
                row["notes"] = json.dumps(notes, ensure_ascii=False)
            elif field in FIELDS:
                row[field] = value
            else:
                raise ValueError(f"Unknown inventory override field {field}")
    # Rebuilding placements must not discard explicit current proof events.
    from inventory_current_events import merge_rows
    current_events = merge_rows(out_rows)
    path = OUTPUT / "S6_10_PAPERS_inventory.csv"
    temporary = path.with_suffix('.csv.tmp')
    with temporary.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in out_rows:
            w.writerow({k: clean_missing_metadata(str(r[k])) for k in FIELDS})
    temporary.replace(path)
    (OUTPUT / "analysis/inventory_source_index.json").write_text(json.dumps(index_records, indent=2, ensure_ascii=False))
    # Selections are a derived view of these exact reconciled rows.  Regenerate
    # them in the same operation so new checkpoint rows cannot be omitted.
    selection_fields = ['label', 'source_run', 'source_id', 'main_or_supporting',
                        'in_compendium_only_because', 'kind', 'file', 'source_line',
                        'source_section', 'source_bytes', 'uses']
    for paper in ('I', 'II', 'III', 'IV', 'V', 'VI'):
        selection_path = OUTPUT / f'analysis/inventory_paper_{paper}_selection.tsv'
        with selection_path.open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=selection_fields, delimiter='\t')
            writer.writeheader()
            for row in out_rows:
                if row['paper'] != paper:
                    continue
                if json.loads(row['notes']).get('receiving_integration_pending'):
                    continue
                location = index_records.get(row['source_run'] + ':' + row['source_id'], {})
                entry = {k: row.get(k, '') for k in selection_fields}
                entry.update(file=location.get('file', ''), source_line=location.get('line', ''),
                             source_section=location.get('section', ''),
                             source_bytes=location.get('end', 0) - location.get('start', 0))
                writer.writerow(entry)
    counts = {
        "source_s6_09_rows": len(source_rows), "source_unique_s6_09_labels": len({r["printed_label"] for r in source_rows}),
        "source_night_rows": len(night_rows), "night_checkpoint": args.night_checkpoint,
        "source_night_statuses": dict(collections.Counter(r["status"] for r in night_rows)),
        "unregistered_night_export_rows": len(unregistered_night_exports),
        "unregistered_night_export_ids": unregistered_night_exports,
        "supplementary_source_rows": len(supplementary),
        "new_writing_rows": len(additions),
        "output_rows": len(out_rows), "provisional_paper_counts": dict(collections.Counter(r["paper"] for r in out_rows)),
        "compendium_only_rows": sum(bool(r["in_compendium_only_because"]) for r in out_rows),
        "body_candidate_rows": sum(not r["in_compendium_only_because"] for r in out_rows),
        "s6_09_labels_not_found": [k for k, v in index_records.items() if not v["found"]],
        "s6_09_labelled_text_rows": [k for k, v in index_records.items() if v.get("container_kind") == "labelled_text"],
        "current_writing_proofs_claimed_checked": sum(r['status'].startswith('proved; current-writing') for r in out_rows),
        "current_scoped_event_rows": current_events['source_rows_with_current_events'],
    }
    (OUTPUT / "analysis/inventory_counts.json").write_text(json.dumps(counts, indent=2, ensure_ascii=False))
    notes = [
        "# Inventory reconciliation\n",
        "This is a source and placement inventory. A generated row records no new mathematical proof check. Historical checks remain attributed to their recorded checkers.\n",
        f"The S6_09 source supplies {len(source_rows):,} rows and {counts['source_unique_s6_09_labels']:,} distinct printed labels. All source-run/source-id pairs are retained; repeated printed labels are shared statements with distinct source records.\n",
        f"Night checkpoint {args.night_checkpoint} supplies {len(night_rows):,} rows. Its source statuses are {counts['source_night_statuses']}. The 225-row checkpoint-12 plan is older; its assertions must be reconciled against the actual correction rows.\n",
        "The draft mapping places old Paper II sections 7–12 and its unrestricted sign statement in Paper VI; old Paper III's rank-three search in Paper V; its smooth monodromy and parameter-loop material in Paper IV. Exact source-section and character ranges are in inventory_source_index.json.\n",
        "Compendium-only placements are conservative: explicit classical/course rows, labelled known re-derivations outside the stated credited-appendix exceptions, known construction/topology appendices, second Kuranishi derivation and diagnostic apparatus. A receiving new lemma in a construction appendix requires individual review before final exclusion. No unused new result is excluded merely because no main result uses it.\n",
        "All novelty comparisons in notes are historical source records, not claims that this writing has reopened those publications. Current citation verification must be added by the responsible paper author.\n",
        "The source conditional transcendence row is entered as open: its period-conjecture premise remains unresolved. No conditional theorem is newly asserted.\n",
        "## Counts\n",
        "```json\n" + json.dumps(counts, indent=2, ensure_ascii=False) + "\n```\n",
    ]
    (OUTPUT / "analysis/inventory_reconciliation.md").write_text("\n".join(notes))
    print(json.dumps({k: v for k, v in counts.items() if not isinstance(v, list)}, indent=2))


if __name__ == "__main__":
    main()
