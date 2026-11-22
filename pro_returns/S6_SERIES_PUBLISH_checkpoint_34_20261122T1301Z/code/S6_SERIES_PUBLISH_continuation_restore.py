"""Verify the supplied continuation manifests and record the restored state.

No statement receives checking credit from this administrative verification.
Run once after extracting the supplied archive and copying checkpoint 10.
"""
import csv
import datetime as dt
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
BASE = WORKSPACE / "S6_SERIES_PUBLISH_work"
START = "2026-11-21T16:11:17+00:00"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    records = ROOT / "records"
    receipt_path = records / "S6_SERIES_PUBLISH_continuation_restore.json"
    if receipt_path.exists():
        raise SystemExit("Continuation intake already recorded; preserve the receipt.")
    checks = []
    summaries = []
    for name, folder, manifest in [
        ("base", BASE, BASE / "BASE_FILELIST.tsv"),
        ("checkpoint_10", BASE / "S6_SERIES_PUBLISH_checkpoint_10",
         BASE / "S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_checkpoint_10_filelist.tsv"),
    ]:
        rows = list(csv.DictReader(manifest.open(), delimiter="\t"))
        for row in rows:
            path = folder / row["path"]
            actual_size = path.stat().st_size if path.is_file() else None
            actual_sha = digest(path) if path.is_file() else None
            ok = actual_size == int(row["size"]) and actual_sha == row["sha256"]
            checks.append(dict(set=name, path=row["path"], expected_size=row["size"],
                               actual_size=actual_size, expected_sha256=row["sha256"],
                               actual_sha256=actual_sha, passed=ok))
        subset = [r for r in checks if r["set"] == name]
        summaries.append(dict(set=name, files=len(rows), verified=sum(r["passed"] for r in subset),
                              manifest_sha256=digest(manifest)))
    assert all(r["passed"] for r in checks)
    with (records / "S6_SERIES_PUBLISH_continuation_input_verification.tsv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(checks[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(checks)
    shutil.copy2(WORKSPACE / "upload/PROMPT(20261121-154552).md",
                 ROOT / "S6_SERIES_PUBLISH_PROMPT_continuation.md")
    receipt = dict(
        continuation_started_utc=START,
        continuation_started_europe_berlin="2026-11-21T17:11:17+01:00",
        verified_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        supplied_archive_sha256=digest(WORKSPACE / "upload/S6_SERIES_PUBLISH_continue_cp10.zip"),
        supplied_prompt_sha256=digest(ROOT / "S6_SERIES_PUBLISH_PROMPT_continuation.md"),
        manifests=summaries,
        checkpoint_restored="S6_SERIES_PUBLISH_checkpoint_10",
        restored_files=2049,
        source_I_sha256=digest(BASE / "S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex"),
        events_sha256=digest(ROOT / "CHECK_EVENTS.tsv"),
        paper_V_text_of_record=dict(path="S6_series_V_public_v2.tex",
                                    sha256=digest(BASE / "S6_series_V_public_v2.tex")),
        next_checkpoint=dict(number=11, due_utc="2026-11-21T16:56:17+00:00"),
        next_review=dict(number=6, due_utc="2026-11-21T17:11:17+00:00"),
        consecutive_reviews_without_movement=0,
        row_rule="Current-source defect types close separately; each current PDF page is a row; changed page images reopen.",
        mathematical_events_added=0,
    )
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    notice = """

## Continuation from checkpoint 10 — 21 November 2026, 16:11:17 UTC

The continuation began at 17:11:17 Europe/Berlin. The supplied continuation
archive was unpacked once. All 1,987 base-manifest files and all 2,049
checkpoint-manifest files match both their recorded byte sizes and SHA-256
digests. The complete checkpoint worktree was restored; verification is
recorded per file in `records/S6_SERIES_PUBLISH_continuation_input_verification.tsv`.
The continuation prompt is preserved as `S6_SERIES_PUBLISH_PROMPT_continuation.md`.

Paper I resumes from candidate 13. Its 346-page reading coverage is inherited
at the exact recorded image hashes; eleven archived edits, three additional
accent corrections and the continuation's records-link/methodology changes
remain to be integrated and rendered. The final source/PDF/ledger bindings,
defect dispositions and 42 provenance claims remain open at intake. The
required mathematical-check queue for I is empty at the inherited snapshot.
Papers II, III and IV remain queued in that order with 197, 128 and 66 current
required-check candidates, respectively.

Paper V's text of record is the supplied `S6_series_V_public_v2.tex`, with its
published deposit fields. The checkpoint's older completed V files and receipts
are preserved as historical evidence. Series-dependent changes to published
version 2 are reserved for the final five-paper review, as requested.

The continuation applies the finer progress rows of section 0.3: each defect
type closes on its own evidence and each page of the current PDF has its own
reading state. A changed page image reopens that page. The consecutive
no-movement counter starts at zero. Checkpoint 11 is due at 16:56:17 UTC
(17:56:17 Europe/Berlin); review 06 is due at 17:11:17 UTC
(18:11:17 Europe/Berlin). Later checkpoints follow at 45-minute intervals and
reviews at hourly intervals. These intake and restoration operations create
no mathematical check event. The five-paper task remains INCOMPLETE.
"""
    for filename in ["PROGRESS_LEDGER.md", "S6_SERIES_PUBLISH_report.md"]:
        with (ROOT / filename).open("a") as stream:
            stream.write(notice)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
