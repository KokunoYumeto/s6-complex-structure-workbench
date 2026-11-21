#!/usr/bin/env python3
"""Verify historical Paper V program paths at the stated immutable commit.

This is a metadata/source-identity operation, not a mathematical check.  The
cp15 tree is needed because forty cited historical programs are absent from
the supplied cp10 manifest.  No downloaded program is executed by this script.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[2]
REPO = "KokunoYumeto/s6-complex-structure-workbench"
COMMIT = "83d76022bcd442278b760db9ff438afceed6c6ea"
CP10 = "pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z"
CP15 = "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS"


def digest(body):
    return hashlib.sha256(body).hexdigest()


def get(url):
    request = Request(url, headers={"User-Agent": "S6-publication-provenance-check"})
    with urlopen(request, timeout=45) as response:
        return response.status, response.read()


def main():
    mentions = []
    for part in ("core", "classification", "shifted"):
        with (ROOT / f"S6_SERIES_PUBLISH_V_{part}_programs.tsv").open() as handle:
            mentions.extend(dict(row, editorial_part=part)
                            for row in csv.DictReader(handle, delimiter="\t"))
    mentions.extend([
        {"filename": "reconstruct_V_global_06.py", "location": "night:P1.12",
         "editorial_part": "consolidated core", "retained_url": ""},
        {"filename": "verify_V_global_saved_07.py", "location": "night:P1.12",
         "editorial_part": "consolidated core", "retained_url": ""},
        {"filename": "fourfolds_checks.py", "location": "maps:src:E.1.4",
         "editorial_part": "resolved product", "retained_url": ""},
        {"filename": "fourfolds_integral_audit.py", "location": "maps:src:E.1.5",
         "editorial_part": "resolved product", "retained_url": ""},
    ])
    manifest = list(csv.DictReader((BASE / "source/S6_SERIES_GRIND_filelist.tsv").open(),
                                  delimiter="\t"))
    tree_by_path = {}
    for part in ("III", "V"):
        tree = json.loads((ROOT / f"S6_SERIES_PUBLISH_program_tree_{part}.json").read_text())
        assert not tree["tree"].get("truncated")
        for entry in tree["tree"]["tree"]:
            tree_by_path[f"{part}/{entry['path']}"] = entry

    work = []
    for filename in sorted({row["filename"] for row in mentions}):
        refs = [row for row in mentions if row["filename"] == filename]
        manifest_rows = [row for row in manifest
                         if row["path"].endswith("/" + filename)]
        explicit = {row["retained_url"] for row in refs if row["retained_url"]}
        if manifest_rows:
            selected = next(row for row in manifest_rows if row["path"].startswith("code/"))
            path = f"{CP10}/{selected['path']}"
            git_blob = ""
            basis = "attached cp10 manifest; primary raw source"
        else:
            selected = None
            if explicit:
                assert len(explicit) == 1
                path = next(iter(explicit)).split(f"/blob/{COMMIT}/", 1)[1]
            else:
                relative = f"V/replay_chains/code/{filename}"
                assert relative in tree_by_path, filename
                path = f"{CP15}/code/{relative}"
            relative = path.split(f"{CP15}/code/", 1)[1]
            git_blob = tree_by_path[relative]["sha"]
            basis = "primary immutable cp15 tree; absent from attached cp10 manifest"
        work.append({"filename": filename, "path": path,
                     "statement_ids": sorted({row["location"] for row in refs}),
                     "source_mentions": refs, "manifest": selected,
                     "tree_blob_sha1": git_blob, "verification_basis": basis})

    def read_program(row):
        raw_url = f"https://raw.githubusercontent.com/{REPO}/{COMMIT}/{row['path']}"
        status, body = get(raw_url)
        blob = hashlib.sha1(b"blob " + str(len(body)).encode() + b"\0" + body).hexdigest()
        record = dict(row, commit=COMMIT, url=f"https://github.com/{REPO}/blob/{COMMIT}/{row['path']}",
                      raw_url=raw_url, http_status=status, bytes=len(body),
                      sha256=digest(body), computed_git_blob_sha1=blob)
        if row["tree_blob_sha1"]:
            assert blob == row["tree_blob_sha1"], row["filename"]
            record["matches_immutable_tree_blob"] = True
        if row["manifest"]:
            expected = row["manifest"]
            record["matches_attached_manifest"] = (
                digest(body) == expected["sha256"] and len(body) == int(expected["size"]))
            assert record["matches_attached_manifest"], row["filename"]
            attached = BASE / "source/S6_PUBLISH_programs" / expected["path"]
            if attached.exists():
                record["attached_source"] = str(attached.relative_to(BASE))
                record["matches_attached_source_bytes"] = attached.read_bytes() == body
                assert record["matches_attached_source_bytes"]
        text = body.decode("utf-8")
        return record, text

    fetched = list(ThreadPoolExecutor(max_workers=6).map(read_program, work))
    records = [record for record, _ in fetched]
    sources = {record["filename"]: text for record, text in fetched}
    (ROOT / "S6_SERIES_PUBLISH_V_program_path_receipt.json").write_text(
        json.dumps(records, indent=2) + "\n")
    (ROOT / "S6_SERIES_PUBLISH_V_verified_program_sources.json").write_text(
        json.dumps(sources, indent=2) + "\n")
    fields = ("filename", "statement_ids", "commit", "path", "bytes", "sha256",
              "verification_basis", "url")
    with (ROOT / "S6_SERIES_PUBLISH_V_program_path_manifest.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in records:
            out = {key: row[key] for key in fields}
            out["statement_ids"] = "; ".join(row["statement_ids"])
            writer.writerow(out)
    print(json.dumps({"verified_files": len(records),
                      "cp10_manifest_files": sum(bool(row["manifest"]) for row in records),
                      "cp15_tree_files": sum(bool(row["tree_blob_sha1"]) for row in records),
                      "http_failures": sum(row["http_status"] != 200 for row in records),
                      "mathematical_check_events_added": 0}, indent=2))


if __name__ == "__main__":
    main()
