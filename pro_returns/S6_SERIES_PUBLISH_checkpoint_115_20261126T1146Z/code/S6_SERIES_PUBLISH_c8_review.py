"""Record an hourly publication-gate review from live progress, without a census."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re

csv.field_size_limit(16 * 1024 * 1024)

ROOT = Path(__file__).resolve().parents[1]
START = datetime(2026, 11, 25, 15, 23, 14, tzinfo=timezone.utc)


def table(name):
    with (ROOT / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def supplementary_completions():
    """Count actual provenance, clean-build and current-page status rows."""
    result = {f"{paper}_{kind}": 0 for paper in ("III", "IV")
              for kind in ("provenance", "build", "pages")}
    provenance = ROOT / "S6_SERIES_PUBLISH_provenance_checks.tsv"
    if provenance.exists():
        for row in table(provenance.name):
            if (row["paper"] in {"III", "IV"}
                    and row["resolution_status"] == "complete: three-way source/deposit provenance"):
                result[f"{row['paper']}_provenance"] += 1
    builds = ROOT / "S6_SERIES_PUBLISH_build_progress.tsv"
    if builds.exists():
        rows = table(builds.name)
        for paper in ("III", "IV"):
            selected = [row for row in rows if row["paper"] == paper]
            assert len(selected) <= 1, (paper, "Multiple current build rows")
            result[f"{paper}_build"] = sum(row["status"] == "done" for row in selected)
    for paper in ("III", "IV"):
        pages = ROOT / f"S6_SERIES_PUBLISH_page_progress_{paper}.tsv"
        if pages.exists():
            rows = table(pages.name)
            assert len({row["page"] for row in rows}) == len(rows), "Repeated current-PDF page"
            assert len({row["pdf_sha256"] for row in rows}) <= 1, "Mixed current-PDF page states"
            result[f"{paper}_pages"] = sum(row["status"] == "done" for row in rows)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", type=int)
    args = parser.parse_args()
    number = args.number
    assert number >= 64
    due = START + timedelta(hours=number - 63)
    now = datetime.now(timezone.utc)
    assert now >= due, f"Review not due until {due.isoformat()}"
    ledger_path = ROOT / "PROGRESS_LEDGER.md"
    ledger = ledger_path.read_text(encoding="utf-8")
    marker = f"\n## Review {number} — "
    assert marker not in ledger, "This review is already recorded"
    required = table("S6_SERIES_PUBLISH_required_progress_III.tsv")
    events = {r["event_id"]: r for r in table("CHECK_EVENTS.tsv")}
    closed = {r["tag"] for r in required if r["status"] == "done"}
    assert len(required) == 128
    if number == 64:
        previous = {r["tag"] for r in required if r["tag"] != "02LG"}
        previous_time = START
        previous_stagnation = 0
    else:
        previous_note = ledger.split(f"\n## Review {number - 1} — ", 1)[1]
        previous_time = datetime.fromisoformat(previous_note.splitlines()[0])
        match = re.search(rf"Closed required identities at Review{number - 1}: ([^\n]+)\.", previous_note)
        assert match
        previous = set(match[1].split(", "))
        previous_stagnation = int(re.search(r"Consecutive reviews without qualifying movement: (\d+)\.", previous_note)[1])
    assert not previous - closed, "A required row reopened; review its exact movement manually"
    newly_closed = sorted(closed - previous)
    for row in required:
        if row["status"] == "done":
            for event_id in row["check_event_id"].split(";"):
                if event_id.strip():
                    assert event_id.strip() in events
                    assert events[event_id.strip()]["statement_id"] == row["label"]
    units = table("S6_SERIES_PUBLISH_unit_progress.tsv")
    open_units = Counter(r["paper"] for r in units if r["status"] == "open")
    done_units = Counter(r["paper"] for r in units if r["status"] == "done")
    # Evidence-only timestamp updates supply no status movement. Actual build
    # findings can reopen a source criterion, so report the signed net change.
    previous_done = {"III": 0, "IV": 0}
    if number > 64:
        for paper in previous_done:
            match = re.search(rf"Paper {paper}:\s*\d+/\d+ required checks complete;\s*\d+ unit\s*criteria open and (\d+) done", previous_note)
            assert match, (paper, "Missing prior done count")
            previous_done[paper] = int(match[1])
    unit_completion_delta = sum(done_units[p] - previous_done[p] for p in previous_done)
    supplementary = supplementary_completions()
    previous_supplementary = dict.fromkeys(supplementary, 0)
    if number > 70:
        match = re.search(rf"Supplementary completions at Review{number - 1}: ([^\n]+)\.", previous_note)
        assert match, "Missing preceding actual supplementary status counts"
        previous_supplementary = dict((key, int(value)) for key, value in
                                      (item.split("=") for item in match[1].split("; ")))
        assert set(previous_supplementary) == set(supplementary)
    # Review69/checkpoint99 preceded the first III provenance admission,
    # complete build and any rendered-page reading; IV had not begun.
    # All six supplementary completion counts at that boundary were zero.
    supplementary_delta = {key: value - previous_supplementary[key]
                           for key, value in supplementary.items()}
    movement = bool(newly_closed or unit_completion_delta > 0
                    or any(value > 0 for value in supplementary_delta.values()))
    stagnation = 0 if movement else previous_stagnation + 1
    open_required = [r for r in required if r["status"] != "done"]
    required_table = "\n".join(
        "| " + " | ".join((r["tag"], r["label"], r["packet_status"], r["proof_status"])) + " |"
        for r in open_required
    ) or "| None | All 128 required checks admitted | Complete | Released and compared |"
    iv_progress = ROOT / "S6_SERIES_PUBLISH_required_progress_IV.tsv"
    if iv_progress.exists():
        iv = table(iv_progress.name)
        iv_done = sum(r["status"] == "done" for r in iv)
        iv_total = len(iv)
    else:
        with (ROOT / "records/S6_SERIES_PUBLISH_required_check_candidates.csv").open(encoding="utf-8", newline="") as stream:
            iv = [r for r in csv.DictReader(stream) if r["paper"] == "IV"]
        iv_done, iv_total = 0, len(iv)
        assert iv_total == 66
    previous_iv_done = 0
    if number > 64:
        match = re.search(r"Paper IV:\s*(\d+)/\d+ required checks complete", previous_note)
        assert match, "Missing preceding Paper IV required-check count"
        previous_iv_done = int(match[1])
    iv_required_delta = iv_done - previous_iv_done
    movement = movement or iv_required_delta > 0
    stagnation = 0 if movement else previous_stagnation + 1
    gate = ("Complete the final 02LG original/history comparison and root admission before applying the admitted manuscript repairs."
            if open_required else
            "Complete Paper III's final unit restructuring and register pass, provenance, clean pdfLaTeX build and every-page visual reading.")
    elapsed = (now - START).total_seconds()
    next_checkpoint_offset = (int(elapsed // 2700) + 1) * 2700
    next_checkpoint = START + timedelta(seconds=next_checkpoint_offset)
    note = f"""
## Review {number} — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {due.isoformat()}.
Since the preceding review boundary, {len(newly_closed)} Paper III required
identities closed: {', '.join(newly_closed) or 'none'}.
The final-unit tables record a signed change of {unit_completion_delta} in
completed III/IV criterion rows. Each required completion resolves to its
exact check events. Reopened layout/source criteria are included in this
signed change. A positive change establishes qualifying completions;
evidence-only timestamp updates receive no movement credit.
Support comparisons, fresh derivation, historical retrieval, prepared edits,
source application and checkpoint packaging receive no separate movement credit.
Paper IV's signed change in completed required checks is {iv_required_delta}.

### Open required checks and publication rows

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{required_table}

Paper III: {len(closed)}/128 required checks complete; {open_units['III']} unit
criteria open and {done_units['III']} done in the live unit table.
Paper IV: {iv_done}/{iv_total} required checks complete; {open_units['IV']} unit
criteria open and {done_units['IV']} done. The current source and full unit
status, evidence and criterion details remain in
`S6_SERIES_PUBLISH_unit_progress.tsv`; the required identities and their
individual states remain in the corresponding required-progress tables
(IV uses its attached 66-row candidate list until its phase begins).

The admitted LT and LV support comparisons retain their exact mathematical
scope and do not create required identities. LG's frozen derivation, original
release, historical comparison and admission state are recorded in its live
required row. The unchanged 495-presentation scope and the residual smooth
invariant corrections are assessed through their explicit marked maps.

Current main gate: {gate}
Paper IV follows completion of III. Papers I, II and V retain their individual
closed gates until the joint phase. The provenance table, final-build gate,
and current-PDF page-reading gate remain open wherever their actual required
work has not been completed; this review awards no inferred closure.

Closed required identities at Review{number}: {', '.join(sorted(closed))}.

Supplementary completions at Review{number}: {'; '.join(key + '=' + str(value) for key, value in supplementary.items())}.
Signed changes since the preceding boundary: {'; '.join(key + '=' + str(value) for key, value in supplementary_delta.items())}.
These counts use only complete three-way source/deposit provenance rows,
done clean-build rows, and done pages of one identified current PDF.
Open joint-source claims and submission actions receive no inferred closure;
provenance completion itself supplies no PDF-page or clean-build credit.

Consecutive reviews without qualifying movement: {stagnation}.
Next hourly review: {(due + timedelta(hours=1)).isoformat()}.
Next checkpoint boundary: {next_checkpoint.isoformat()}.
The two-consecutive-no-movement stop rule {'is reached; prepare the final incomplete package' if stagnation >= 2 else 'has not been reached'}.
"""
    for name in ["PROGRESS_LEDGER.md", "S6_SERIES_PUBLISH_report.md"]:
        path = ROOT / name
        prior = path.read_text(encoding="utf-8")
        assert marker not in prior
        path.write_text(prior + note, encoding="utf-8", newline="\n")
    print(f"Review{number}: III {len(closed)}/128; newly required {','.join(newly_closed) or 'none'}; signed completed-unit change {unit_completion_delta}")
    print("Supplementary actual completions:", supplementary)
    print("Supplementary signed changes:", supplementary_delta)
    print("Paper IV signed required-check change:", iv_required_delta)
    print(f"Open unit criteria: III={open_units['III']}, IV={open_units['IV']}; consecutive no-movement reviews={stagnation}")
    print("Recorded UTC:", now.isoformat())


if __name__ == "__main__":
    main()
