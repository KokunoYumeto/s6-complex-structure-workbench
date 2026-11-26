"""Scheduled lean continuation-nine checkpoints, relative to attached cp100."""
from pathlib import Path
from datetime import datetime, timedelta, timezone
import argparse
import csv
import hashlib
import io
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
START = datetime(2026, 11, 26, 0, 30, 22, tzinfo=timezone.utc)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rows(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def changed():
    prefix = ROOT.name + "/"
    old = {r["path"][len(prefix):]: r["sha256"]
           for r in rows(BASE / "BASE_FILELIST.tsv")
           if r["path"].startswith(prefix)}
    # Restored duplicate paths keep the original identity and are not changes.
    for r in rows(BASE / "CP100_INDEX.tsv"):
        path = r.get("path", "")
        if path.startswith(prefix):
            path = path[len(prefix):]
        if r.get("sha256"):
            old.setdefault(path, r["sha256"])
    excluded_parts = {"__pycache__", ".git", "build", "renders", "rendered",
                      "tmp", "downloads", "external_tmp", "temporary_literature",
                      "source_cache"}
    excluded_extensions = {".pyc", ".aux", ".fls", ".fdb_latexmk", ".toc",
                           ".synctex", ".zip", ".png", ".jpg", ".jpeg"}
    payload = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if "continuation9_current_tex" in rel.parts or "continuation9_build_III" in rel.parts:
            continue
        if "continuation9_tex_runtime" in rel.parts:
            if rel.as_posix() != "agents/continuation9_tex_runtime/aliases/S6_SERIES_PUBLISH_c9_display_aliases.tex":
                continue
        if any(p in {"software", "third_party", "backend_source", "sage_runtime"} for p in rel.parts):
            continue
        if path.name.startswith("S6_SERIES_PUBLISH_checkpoint_") and path.suffix in {".md", ".tsv"}:
            # The current README and list are constructed once below; earlier
            # checkpoint wrappers are already in the base and are not payload.
            continue
        if "continuation8_iii_later" in rel.parts and path.name.endswith("_publication_packet.json"):
            # Redundant per-batch manifests are forbidden by prompt section 0.5.
            # Exact edits/events, substantive reviews and actual logs are retained.
            continue
        if "continuation8_iii_later" in rel.parts and path.name.endswith("_equation_aliases.tsv"):
            continue
        if "continuation8_iii_weighted_units" in rel.parts and path.name == "S6_SERIES_PUBLISH_MINIMAL_new_equation_identities.tsv":
            continue
        if any(p in excluded_parts or p.startswith("texmf") for p in rel.parts):
            continue
        if path.suffix.lower() in excluded_extensions:
            continue
        if "continuation8_tex_runtime" in rel.parts and path.suffix.lower() in {".pdf", ".log"}:
            continue
        data = path.read_bytes()
        if old.get(rel.as_posix()) == digest(data):
            continue
        if path.suffix.lower() in {".md", ".tex", ".tsv", ".csv", ".py", ".json", ".out", ".err", ".txt", ".bib"}:
            assert b"\r\n" not in data, ("Non-LF text", rel.as_posix())
        payload[rel.as_posix()] = data
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["inspect", "pack"])
    parser.add_argument("--number", type=int, default=101)
    parser.add_argument("--progress", default="")
    args = parser.parse_args()
    if args.mode == "inspect":
        payload = changed()
        print(json.dumps({"changed_files": len(payload),
                          "uncompressed_bytes": sum(map(len, payload.values())),
                          "largest": sorted(((len(v), k) for k, v in payload.items()), reverse=True)[:15]}, indent=2))
        return
    assert args.number >= 101
    due = START + timedelta(minutes=45 * (args.number - 100))
    now = datetime.now(timezone.utc)
    assert now >= due, ("Checkpoint not due", due.isoformat())
    assert args.progress.strip(), "Describe actual mathematical and unit progress."
    outdir = BASE.parent / "output"
    outdir.mkdir(exist_ok=True)
    destination = outdir / f"S6_SERIES_PUBLISH_checkpoint_{args.number}.zip"
    assert not destination.exists(), "Never replace a delivered checkpoint."
    required = {"III": rows(ROOT / "S6_SERIES_PUBLISH_required_progress_III.tsv")}
    iv_progress = ROOT / "S6_SERIES_PUBLISH_required_progress_IV.tsv"
    if iv_progress.exists():
        required["IV"] = rows(iv_progress)
    else:
        # IV has not begun and has no per-check progress table at cp100.
        # Its 66 required identities are the supplied candidate rows; the
        # prompt and current ledger leave every required check open.
        with (ROOT / "records/S6_SERIES_PUBLISH_required_check_candidates.csv").open(newline="") as stream:
            iv_candidates = [r for r in csv.DictReader(stream) if r["paper"] == "IV"]
        assert len(iv_candidates) == 66
        required["IV"] = [{"tag": r["tag"], "status": "open"} for r in iv_candidates]
    units = rows(ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv")
    done = {p: [r["tag"] for r in rr if r["status"] == "done"] for p, rr in required.items()}
    unit_open = {p: sum(r["paper"] == p and r["status"] != "done" for r in units) for p in required}
    next_review = START + timedelta(hours=int((now - START).total_seconds() // 3600) + 1)
    assert (ROOT / "S6_SERIES_PUBLISH_report.md").read_text().splitlines()[0].startswith("INCOMPLETE")
    section = (f"\n\n## Checkpoint {args.number} — {now.isoformat()}\n\n"
               f"{args.progress.strip()}\n\n"
               f"Paper III: {len(done['III'])}/{len(required['III'])} required checks complete; "
               f"{unit_open['III']} unit criteria open. Paper IV: {len(done['IV'])}/{len(required['IV'])} "
               f"required checks complete; {unit_open['IV']} unit criteria open. "
               "I, II and V retain their individual gates until the five-paper step. "
               "Packaging earns no movement credit. The report remains INCOMPLETE.\n\n"
               f"Next checkpoint: {(due + timedelta(minutes=45)).isoformat()}. "
               f"Next hourly review: {next_review.isoformat()}.\n")
    for name in ("S6_SERIES_PUBLISH_report.md", "PROGRESS_LEDGER.md"):
        with (ROOT / name).open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(section)
    summary = {"checkpoint": args.number, "scheduled_utc": due.isoformat(),
               "snapshot_utc": now.isoformat(), "required_done_tags": done,
               "open_unit_criteria": unit_open, "progress": args.progress.strip(),
               "path": str(destination)}
    log = json.dumps(summary, indent=2) + "\n"
    (ROOT / "code" / f"S6_SERIES_PUBLISH_c9_checkpoint_{args.number}.out").write_text(log, newline="\n")
    payload = changed()
    assert "CHECK_EVENTS.tsv" in payload
    assert "S6_SERIES_PUBLISH_findings_III.tsv" in payload
    readme = (f"# S6_SERIES_PUBLISH checkpoint {args.number}\n\n"
              f"Snapshot: {now.isoformat()}.\n\n"
              "Unpack the supplied S6_SERIES_PUBLISH_continue_cp100.zip once and run "
              "python restore_cp100.py at its root. Extract this checkpoint into "
              "S6_SERIES_PUBLISH_checkpoint_100, replacing the same relative paths. "
              "The attached base and this newest checkpoint alone restore the working state.\n\n"
              "Read the latest report and ledger sections and the cited admission and unit records. "
              "File existence alone confers no completed check or unit criterion. "
              "Continue Paper III, then Paper IV, then the five-paper step.\n\n"
              f"{args.progress.strip()}\n\n"
              "The file list gives size and SHA-256 of every payload except itself. "
              "Unchanged base files, other-author publications or extracts, downloaded page images, "
              "reproducible TeX runtime caches, and old archives are excluded. "
              "All newly needed authored programs, records and actual streams are retained. "
              "The seven-display authored diagnostic source is retained; downloaded runtime and backend software are excluded.\n\n"
              f"Next checkpoint: {(due + timedelta(minutes=45)).isoformat()}. "
              f"Next hourly review: {next_review.isoformat()}.\n")
    payload[f"S6_SERIES_PUBLISH_checkpoint_{args.number}_README.md"] = readme.encode()
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    writer.writerow(["path", "size", "sha256"])
    for name, data in sorted(payload.items()):
        writer.writerow([name, len(data), digest(data)])
    payload[f"S6_SERIES_PUBLISH_checkpoint_{args.number}_filelist.tsv"] = buffer.getvalue().encode()
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            archive.writestr(name, data)
    assert destination.stat().st_size < 500_000_000, "Split before delivery."
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        for name, data in payload.items():
            assert archive.read(name) == data
    print(log, end="")
    print("Payload files:", len(payload), "ZIP bytes:", destination.stat().st_size,
          "SHA-256:", digest(destination.read_bytes()))


if __name__ == "__main__":
    main()
