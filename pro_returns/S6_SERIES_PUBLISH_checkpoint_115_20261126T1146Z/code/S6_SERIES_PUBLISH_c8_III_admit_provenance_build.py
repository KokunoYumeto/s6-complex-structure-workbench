#!/usr/bin/env python3
"""Record actual documentary reviews and the converged III build, without page credit."""
import csv
from collections import Counter
from datetime import datetime, timezone
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(16 * 1024 * 1024)
PDF_SHA = "798f814252fc3fd72809a96d7fa946b0e09e2daadfd153f8f6cc83f8ab92c43e"
WHO = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed"


def require(value, reason):
    if not value:
        raise RuntimeError(reason)


def table(name):
    raw = (ROOT / name).read_bytes()
    reader = csv.DictReader(io.StringIO(raw.decode()), delimiter="\t")
    return raw, reader.fieldnames, list(reader)


def main():
    now = datetime.now(timezone.utc).isoformat()
    raw, fields, events = table("CHECK_EVENTS.tsv")
    require(raw.endswith(b"\n") and b"\r" not in raw, "Event table line endings")
    _, _, provenance = table("S6_SERIES_PUBLISH_provenance_checks.tsv")
    ours = [row for row in provenance if row["paper"] == "III"]
    expected = {"complete: three-way source/deposit provenance": 56,
                "open: joint-source provenance verification": 4,
                "open: final-PDF program-table visibility": 1}
    require(dict(Counter(row["resolution_status"] for row in ours)) == expected,
            "The admitted provenance dispositions changed")
    require(len({row["claim_id"] for row in ours}) == 61, "Claim identities")
    for stem in ("provenance_inspect", "provenance_apply", "program_records_final"):
        require((ROOT / f"code/S6_SERIES_PUBLISH_c8_III_{stem}.err").read_bytes() == b"",
                f"Nonempty stderr: {stem}")
    applied = (ROOT / "code/S6_SERIES_PUBLISH_c8_III_provenance_apply.out").read_text()
    require("APPENDED 61 III provenance rows" in applied, "No actual provenance application")
    _, _, programs = table("S6_SERIES_PUBLISH_records_III.tsv")
    require(len(programs) == 181 and len({r["printed_path"] for r in programs}) == 181,
            "Final program record domain")
    metadata_path = ROOT / "agents/continuation8_tex_runtime/III_final/S6_SERIES_PUBLISH_III_final_metadata.json"
    metadata = json.loads(metadata_path.read_text())
    require(metadata["pdf"]["physical_pages"] == 694, "Converged page count")
    require(not [r for r in metadata["issues"] if r["severity"] == "error"], "Extractor errors")
    require(len(metadata["issues"]) == 20, "Reviewed extractor warning scope changed")
    require((ROOT / "code/S6_SERIES_PUBLISH_c8_tex_III_final_pass08.err").read_bytes() == b"",
            "Nonempty final engine stderr")
    require((ROOT / "code/S6_SERIES_PUBLISH_c8_tex_extract_final_III.err").read_bytes() == b"",
            "Nonempty extractor stderr")
    build_path = ROOT / "S6_SERIES_PUBLISH_build_progress.tsv"
    require(not build_path.exists(), "Build gate already registered")
    records = [
        ("III:final-program-source-identities", "publish:c8:III:final-program-source-identities",
         "code/S6_SERIES_PUBLISH_c8_III_program_records.py",
         "S6_SERIES_PUBLISH_records_III.tsv; code/S6_SERIES_PUBLISH_c8_III_program_records_final.out; agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_III_programs_table_review.md",
         "Root wholly read the final program-record generator and its actual final stdout/empty stderr: 181 distinct printed paths, 131 local files and 50 exact pinned historical HTTP200 byte identities. Root read every retained 42-digest comparison: 36 CP12/CP15 and six cone/OS45 agree, zero disagreements. Eight historical paths retain the bounded absence of a located prior digest. The previously admitted exact 31-file transport maps and inverses remain in the program review. This documentary review runs no mathematical program and supplies no old-execution, proof, independent or PDF-page credit."),
        ("III:final-source-deposit-provenance", "publish:c8:III:final-source-deposit-provenance",
         "code/S6_SERIES_PUBLISH_c8_III_provenance_apply.py",
         "agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_final_provenance_deposit_review.md; code/S6_SERIES_PUBLISH_c8_III_provenance_inspect.out; code/S6_SERIES_PUBLISH_c8_III_provenance_apply.out; S6_SERIES_PUBLISH_provenance_checks.tsv",
         "lg_fresh read the full proposal and substantive 580-line review; root wholly read the 1413-line application, initial 486 review lines and every changed/appended range, and all 181 actual inspection-output lines plus empty stderr and all application output/empty stderr. The exact eleven fields and 61 claims were applied with old shared bytes preserved as prefixes: 56 source/deposit comparisons complete, S02/S03/S06/S07 joint checks and P16 printed program-table visibility open. The official MSC/taxonomy/CC0 and standing-records access source/output readings retain their exact documented scope, including the ligature correction. The sole source commit remains outside deposit fields. No external publication, new mathematical derivation, count regeneration or PDF reading is claimed."),
        ("III:converged-build-and-reference-extraction", "publish:c8:III:converged-build-and-reference-extraction",
         "code/S6_SERIES_PUBLISH_c8_tex_pdflatex.py",
         "code/S6_SERIES_PUBLISH_c8_tex_final_build_notes.md; code/S6_SERIES_PUBLISH_c8_tex_III_final_pass08.log; code/S6_SERIES_PUBLISH_c8_tex_extract_final_III.out",
         "tex_runtime wholly read each actual pass01–08 log and all actual stdout/empty stderr at the exact scopes recorded in the build notes. Root wholly read the notes for these eight final-build passes, exact repair proposals and corresponding source contexts. Pass08 exits0 with 694 pages, 4478489 bytes, stable aux/toc/out, no fatal error, missing font, undefined reference/citation, rerun request or overfull box beyond2pt. The approved III extractor exits0: 1222 labels,1216 hypertargets,249 formal owners, zero errors and20 target-page warnings reserved for actual page inspection. The coordinated PDF SHA256 is " + PDF_SHA + ". This closes the clean-build row only; every final page retains its separate actual-reading gate. No mathematical or independent credit is created.")
    ]
    existing = {row["event_id"] for row in events}
    additions = []
    for subject, event_id, source, where, outcome in records:
        require(event_id not in existing, "Duplicate administrative event")
        require(subject not in {r["key"] for r in metadata["source"]["labels"]},
                "An administrative subject is a current literal statement target")
        row = dict.fromkeys(fields, "")
        row.update(statement_id=subject, date=now[:10], who=WHO,
                   type="used and rechecked in this run", outcome=outcome,
                   event_id=event_id, phase="continuation8 final documentary admission",
                   source_file=source, source_event_type="used and rechecked in this run",
                   evidence_group=event_id, date_utc=now, where=where)
        additions.append(row)
    stream = io.StringIO(newline="")
    csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n").writerows(additions)
    new_events = raw + stream.getvalue().encode()
    build_fields = ["paper", "status", "date_utc", "source_file", "pdf_file", "pdf_sha256", "log_files", "evidence", "detail"]
    build = dict(paper="III", status="done", date_utc=now,
                 source_file="S6_SERIES_PUBLISH_III.tex",
                 pdf_file="agents/continuation8_tex_runtime/III_final/S6_SERIES_PUBLISH_III.pdf",
                 pdf_sha256=PDF_SHA,
                 log_files="code/S6_SERIES_PUBLISH_c8_tex_III_final_pass08.log",
                 evidence="code/S6_SERIES_PUBLISH_c8_tex_final_build_notes.md; publish:c8:III:converged-build-and-reference-extraction",
                 detail="Converged pdfLaTeX/no-shell-escape build,694pages,4478489bytes; zero overfull>2pt, missing fonts, undefined references/citations or rerun requests. Page reading and20 extractor target-page warnings remain separately open.")
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, build_fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerow(build)
    build_bytes = stream.getvalue().encode()
    require((ROOT / "CHECK_EVENTS.tsv").read_bytes() == raw, "Event table changed during admission")
    (ROOT / "CHECK_EVENTS.tsv").write_bytes(new_events)
    build_path.write_bytes(build_bytes)
    require((ROOT / "CHECK_EVENTS.tsv").read_bytes() == new_events, "Event write mismatch")
    require(build_path.read_bytes() == build_bytes, "Build-row write mismatch")
    print(json.dumps({"date_utc": now, "administrative_events_appended": len(additions),
                      "provenance": expected, "clean_build_rows_closed": 1,
                      "unit_rows_closed": 0, "pdf_pages_read": 0,
                      "mathematical_event_counts_changed": False}, indent=2))


if __name__ == "__main__":
    main()
