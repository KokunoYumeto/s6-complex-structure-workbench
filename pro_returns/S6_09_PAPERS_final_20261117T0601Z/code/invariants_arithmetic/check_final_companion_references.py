#!/usr/bin/env python3
"""Read-only printed cross-paper number/type validation on the frozen papers.

Uses balanced TeX groups for AUX/tag numbers, inherits paper/type across genuine
plural lists, and keeps nonnumbered paper mentions distinct from references.
"""
from __future__ import annotations
import collections
import hashlib
import json
import re
from pathlib import Path

from build_all_papers_notation import brace_group

D = Path(__file__).resolve().parents[2]
W = D / "work/invariants_arithmetic"
OUT = W / "final_companion_reference_gate.json"
PAPER = re.compile(r"Paper(?:~|\s)+(III|II|I)\b")
TYPES = "Subsubsection|Subsection|Section|Theorem|Proposition|Lemma|Corollary|Equation|Remark|Definition|Problem|Conjecture|Example|Result|Paragraph"
TYPE = re.compile(r"(?P<kind>" + TYPES + r")(?P<plural>s)?(?:~|\s)+")
NUM = re.compile(r"(?:[A-Z]|\d+)(?:\.(?:\d+|[A-Z]))*(?:[a-z])?")
SEP = re.compile(r"(?:~|\s)*(?P<sep>,|;|\band\b|\bor\b|--|–)(?:~|\s)*")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def uncomment_preserve_positions(s):
    result = []
    for line in s.splitlines(keepends=True):
        cut = None
        for i, c in enumerate(line):
            if c != "%": continue
            j = i - 1
            while j >= 0 and line[j] == "\\": j -= 1
            if (i - 1 - j) % 2 == 0:
                cut = i; break
        if cut is None: result.append(line)
        else: result.append(line[:cut] + "".join("\n" if c == "\n" else " " for c in line[cut:]))
    return "".join(result)


def norm_number(s):
    s = s.strip()
    while s.startswith("{"):
        inside, end = brace_group(s, 0)
        if end != len(s): break
        s = inside.strip()
    if s.startswith("(") and s.endswith(")"): s = s[1:-1]
    return re.sub(r"\s+", "", s)


def read_aux(s):
    records, kinds = {}, {}
    for m in re.finditer(r"\\newlabel(?=\s*\{)", s):
        label, j = brace_group(s, m.end())
        outer, _ = brace_group(s, j)
        if label.endswith("@cref"):
            first, _ = brace_group(outer, 0)
            k = re.match(r"\[([^\]]+)\]", first)
            assert k, (label, first)
            kinds[label[:-5]] = k[1]
            continue
        groups, pos = [], 0
        while pos < len(outer):
            if not outer[pos:].strip(): break
            item, pos = brace_group(outer, pos)
            groups.append(item)
        assert label not in records, ("duplicate AUX", label)
        records[label] = {"label": label, "raw_number": groups[0], "number": norm_number(groups[0]),
                          "page": groups[1] if len(groups) > 1 else "",
                          "title": groups[2] if len(groups) > 2 else "",
                          "hyperref_anchor": groups[3] if len(groups) > 3 else ""}
    for label, r in records.items():
        fallback = r["hyperref_anchor"].split(".")[0]
        r["kind"] = kinds.get(label, fallback)
        r["kind_source"] = "cleveref AUX" if label in kinds else "hyperref anchor fallback"
    return records


def number_at(s, pos):
    while pos < len(s) and (s[pos].isspace() or s[pos] == "~"): pos += 1
    start = pos
    if pos < len(s) and s[pos] == "{":
        _, end = brace_group(s, pos)
        return s[start:end], end
    paren = pos < len(s) and s[pos] == "("
    if paren: pos += 1
    m = NUM.match(s, pos)
    if not m: return None
    end = m.end()
    if paren:
        if end >= len(s) or s[end] != ")": return None
        end += 1
    return s[start:end], end


def parse_reference_group(s, paper_match):
    pos = paper_match.end()
    m = re.match(r"(?:~|\s)*,(?:~|\s)*", s[pos:])
    if not m: return [], pos
    pos += m.end()
    tm = TYPE.match(s, pos)
    if not tm: return [], pos
    kind, plural = tm["kind"].lower(), bool(tm["plural"])
    pos = tm.end()
    first = number_at(s, pos)
    if not first: return [], pos
    raw, pos = first
    refs = [{"kind": kind, "raw_number": raw, "number": norm_number(raw), "end_offset": pos, "list_role": "first"}]
    while True:
        sm = SEP.match(s, pos)
        if not sm: break
        candidate = sm.end()
        tm = TYPE.match(s, candidate)
        if tm:
            next_kind, next_plural = tm["kind"].lower(), bool(tm["plural"])
            nm = number_at(s, tm.end())
            role = "continued_typed_reference"
        elif plural or sm["sep"] in ["--", "–"]:
            next_kind, next_plural = kind, plural
            nm = number_at(s, candidate)
            role = "range_endpoint" if sm["sep"] in ["--", "–"] else "inherited_plural_reference"
        else: break
        if not nm: break
        raw, end = nm
        # Do not misread the P of a following 'Paper', or prose after a list.
        if end < len(s) and (s[end].isalpha() or s[end] == "_"): break
        refs.append({"kind": next_kind, "raw_number": raw, "number": norm_number(raw),
                     "end_offset": end, "list_role": role, "separator": sm["sep"]})
        kind, plural, pos = next_kind, next_plural, end
    return refs, pos


def main():
    files = {f"S6_09_PAPERS_{p}.{ext}": (D / f"S6_09_PAPERS_{p}.{ext}").read_bytes()
             for p in ["I", "II", "III"] for ext in ["tex", "aux"]}
    originals = {p: files[f"S6_09_PAPERS_{p}.tex"].decode() for p in ["I", "II", "III"]}
    texts = {p: uncomment_preserve_positions(s) for p, s in originals.items()}
    aux = {p: read_aux(files[f"S6_09_PAPERS_{p}.aux"].decode()) for p in ["I", "II", "III"]}
    bynumber = {}
    for p, records in aux.items():
        for label, r in records.items():
            if "\\label{" + label + "}" not in texts[p]: continue
            bynumber.setdefault((p, r["number"]), []).append(r)
    refs, mentions, observations = [], [], []
    for source_paper, s in texts.items():
        for m in PAPER.finditer(s):
            targets, end = parse_reference_group(s, m)
            line = s[:m.start()].count("\n") + 1
            if not targets:
                context = originals[source_paper][m.start():m.start()+210]
                repeated = bool(PAPER.match(s, end))
                row = {"paper": source_paper, "line": line, "offset": m.start(),
                       "context": context, "disposition": "duplicated_paper_prefix" if repeated else "nonnumbered_paper_mention"}
                mentions.append(row)
                if repeated: observations.append(row)
                continue
            expression = originals[source_paper][m.start():end]
            for item in targets:
                candidates = bynumber.get((m[1], item["number"]), [])
                matching = [r for r in candidates if r["kind"] == item["kind"]]
                if item["kind"] == "result": matching = candidates
                # Several explicit source aliases can point to the very same
                # numbered object; all actual labels are retained as evidence.
                refs.append({"source_paper": source_paper, "source_line": line,
                             "source_offset": m.start(), "printed_expression": expression,
                             "target_paper": m[1], **item,
                             "valid_number_and_kind": bool(matching),
                             "actual_targets": matching,
                             "same_number_other_kinds": [r for r in candidates if r not in matching]})

    overview_path = D / "records/common_numbered_companion_overview.json"
    overview_raw = overview_path.read_bytes()
    overview = json.loads(overview_raw)
    overview_checks = []
    for paper, targets in overview["targets"].items():
        for key, recorded in targets.items():
            actual = aux[paper].get(key)
            appears_now = any(r["source_paper"] == "I" and r["source_line"] < 250 and r["target_paper"] == paper
                              and any(t["label"] == key for t in r["actual_targets"]) for r in refs)
            overview_checks.append({"target_paper": paper, "label": key, "recorded_number": recorded,
                                    "actual": actual,
                                    "recorded_target_still_exact": actual is not None and actual["number"] == norm_number(recorded),
                                    "present_in_current_short_overview": appears_now,
                                    "scope": "Current introductory target" if appears_now else "Historical longer-overview target retained in the overview record; omitted from the current short overview, not a broken current reference."})
    # A range can repeat its Paper/kind prefix at both endpoints.  Check all
    # implied interior numbers as well, not only the explicit endpoint tokens.
    ranges = []
    for left, right in zip(refs, refs[1:]):
        if left["source_paper"] != right["source_paper"] or left["target_paper"] != right["target_paper"]:
            continue
        between = texts[left["source_paper"]][left["end_offset"]:right["source_offset"]]
        adjacent_range = bool(re.fullmatch(r"(?:\s|~)*(?:--|–)(?:\s|~)*", between))
        inherited_range = (right["list_role"] == "range_endpoint" and right["source_offset"] == left["source_offset"])
        if not adjacent_range and not inherited_range:
            continue
        a = re.fullmatch(r"(.*?)(\d+)", left["number"])
        b = re.fullmatch(r"(.*?)(\d+)", right["number"])
        interior = []
        if a and b and a[1] == b[1] and int(a[2]) <= int(b[2]):
            for n in range(int(a[2])+1, int(b[2])):
                number = a[1]+str(n)
                candidates = bynumber.get((left["target_paper"], number), [])
                if left["kind"] == right["kind"]:
                    candidates = [q for q in candidates if q["kind"] == left["kind"]]
                else:
                    candidates = [q for q in candidates if q["kind"] in ["theorem", "proposition", "lemma", "corollary", "remark", "definition", "problem", "example"]]
                interior.append({"number": number, "actual_targets": candidates, "valid": bool(candidates)})
        ranges.append({"source_paper": left["source_paper"], "source_line": left["source_line"],
                       "target_paper": left["target_paper"],
                       "left": {k:left[k] for k in ["kind","number","actual_targets"]},
                       "right": {k:right[k] for k in ["kind","number","actual_targets"]},
                       "interior_checks": interior,
                       "passed": left["valid_number_and_kind"] and right["valid_number_and_kind"] and all(q["valid"] for q in interior)})
    failures = [r for r in refs if not r["valid_number_and_kind"]]
    range_failures = [r for r in ranges if not r["passed"]]
    for n, raw in files.items(): assert (D / n).read_bytes() == raw
    assert overview_path.read_bytes() == overview_raw
    report = {"reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro", "date_utc": "2026-11-17",
              "passed": not failures and not range_failures and all(r["recorded_target_still_exact"] for r in overview_checks),
              "gate_passed": not failures and not range_failures and all(r["recorded_target_still_exact"] for r in overview_checks),
              "input_sha256": {n: sha(raw) for n, raw in files.items()},
              "overview_record_sha256": sha(overview_raw),
              "explicit_numbered_reference_occurrences": len(refs),
              "unique_numbered_destinations": len({(r['target_paper'],r['kind'],r['number']) for r in refs}),
              "reference_counts_by_source_paper": dict(collections.Counter(r["source_paper"] for r in refs)),
              "reference_counts_by_kind": dict(collections.Counter(r["kind"] for r in refs)),
              "broken_number_or_type_count": len(failures), "failures": failures,
              "range_count": len(ranges), "range_interior_destinations_checked": sum(len(r["interior_checks"]) for r in ranges),
              "range_failures": range_failures, "range_checks": ranges,
              "recorded_overview_targets_checked": len(overview_checks),
              "overview_checks": overview_checks,
              "wording_observations": observations,
              "nonnumeric_mentions": mentions,
              "method": "Scan every uncommented Paper I/II/III mention in the frozen TeX; parse explicit kinds, inherited plural and mixed-kind lists and range endpoints. Read every AUX newlabel with balanced nested braces, normalize only whole tag wrappers, and require an actual target TeX label with the matching cleveref kind. Multiple same-object source aliases are retained. The full bibliography has no matching explicit numbered companion reference. This validates destinations/types, not the mathematical applicability of each invocation, which belongs to the existing receiving-proof audits.",
              "proofs_papers_aux_unchanged": True,
              "records": refs}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k: report[k] for k in ["passed","explicit_numbered_reference_occurrences","unique_numbered_destinations","reference_counts_by_source_paper","reference_counts_by_kind","broken_number_or_type_count","recorded_overview_targets_checked"]}))
    for r in failures:
        print(json.dumps({k:r[k] for k in ["source_paper","source_line","printed_expression","target_paper","kind","number","same_number_other_kinds"]},ensure_ascii=False)[:2500])


if __name__ == "__main__":
    main()
