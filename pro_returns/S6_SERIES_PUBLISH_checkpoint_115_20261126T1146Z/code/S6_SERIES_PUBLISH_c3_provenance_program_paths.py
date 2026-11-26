#!/usr/bin/env python3
"""Resolve the current program table and prepare the one-records-page edits."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
OUT = ROOT / "agents" / "continuation3_provenance"
TEMP = ROOT.parents[1] / "tmp" / "c3_programs"
OUT.mkdir(parents=True, exist_ok=True)
TEMP.mkdir(parents=True, exist_ok=True)
COMMIT = "bc08b5278bcad2beb70b6862c5722f1b9f636db6"
RECORDS = "https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii"
source = (ROOT / "S6_SERIES_PUBLISH_II.tex").read_text()
start = source.index(r"\section*{Programs}")
end = source.index(r"\begin{thebibliography}", start)
programs = source[start:end]
known_paths = {line for line in (BASE / "REPOSITORY_PROGRAM_PATHS.txt").read_text().splitlines() if line and not line.startswith("#")}
pattern = re.compile(r"\\href\{([^{}]*)\}\{\\nolinkurl\{([^{}]+)\}\}")
items = []
for match in pattern.finditer(programs):
    url, old_printed = match.groups()
    prefix = "https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/"
    assert url.startswith(prefix), url
    tail = url[len(prefix):]
    _, path = tail.split("/", 1)
    assert path in known_paths or (path.startswith("code/") and (ROOT / path).is_file()), path
    items.append(dict(old_exact=match.group(0), old_printed=old_printed, repository_path=path, printed_path=path))

extra_path = "pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/example_mayer_vietoris.py"
assert extra_path in known_paths
items.append(dict(old_exact="", old_printed="example_mayer_vietoris.py", repository_path=extra_path, printed_path=extra_path))
torus_path = "pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/D_trivial_monodromy.py"
assert torus_path in known_paths
items.append(dict(old_exact="", old_printed="D_trivial_monodromy.py", repository_path=torus_path, printed_path=torus_path))
previous_path = OUT / "S6_SERIES_PUBLISH_c3_provenance_program_path_checks.tsv"
previous = {}
if previous_path.exists():
    with previous_path.open() as handle:
        previous = {r["repository_path"]: r for r in csv.DictReader(handle, delimiter="\t")}

def resolve(item):
    row = dict(item)
    path = item["repository_path"]
    if path.startswith("code/") and (ROOT / path).is_file():
        data = (ROOT / path).read_bytes()
        row.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data), checked_at=str(ROOT/path), status="present in checkpoint code/")
        return row
    url = "https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/" + COMMIT + "/" + path
    row["checked_at"] = url
    row["date_utc"] = datetime.now(timezone.utc).isoformat()
    cached = TEMP / item["old_printed"]
    old = previous.get(path)
    if old and old.get("checked_at") == url and cached.is_file():
        data = cached.read_bytes()
        if hashlib.sha256(data).hexdigest() == old.get("sha256"):
            row.update(sha256=old["sha256"], bytes=len(data), date_utc=old["date_utc"], status=old["status"])
            return row
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=35) as reply:
            data = reply.read()
            assert reply.status == 200
        (TEMP / item["old_printed"]).write_bytes(data)
        row.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data), status="path in attached repository list; exact pinned bytes retrieved")
    except Exception as exc:
        row.update(status=type(exc).__name__ + ": " + str(exc), sha256="", bytes="")
    return row

with ThreadPoolExecutor(max_workers=6) as pool:
    resolved = list(pool.map(resolve, items))

def write_tsv(path, fields, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

write_tsv(OUT / "S6_SERIES_PUBLISH_c3_provenance_program_path_checks.tsv",
          ["printed_path", "repository_path", "sha256", "bytes", "checked_at", "date_utc", "status"], resolved)
failed = [r for r in resolved if not r["sha256"]]
if failed:
    for row in failed:
        print("UNRESOLVED", row["repository_path"], row["status"])
    raise SystemExit("Program table is not ready; failed exact retrievals are recorded.")
write_tsv(OUT / "S6_SERIES_PUBLISH_records_II.tsv", ["printed_path", "repository_path", "sha256"], resolved)

fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
edits = []
def add(old, new, where, reason, kind="D18"):
    assert source.count(old) == 1, (where, source.count(old))
    edits.append(dict(change_id=f"II-C3-PROV-{len(edits)+1:03}", type=kind,
        statement_id="", old_location=where, old_page="checkpoint 35; source locator", new_location=where,
        new_page="pending final build", old_text=old, new_text=new, reason=reason,
        review_status="Exact source/link replacement; mathematical statement and proof text untouched."))

old_commit = re.search(r"\\newcommand\{\\SsixRepositoryCommit\}\{[^{}]+\}", source).group()
old_records = re.search(r"\\newcommand\{\\SsixPublishRecords\}\{[^{}]+\}", source).group()
add(old_commit, r"\newcommand{\SsixRepositoryCommit}{" + COMMIT + "}", "preamble: repository commit", "Continuation prompt section 0.3 fixes the single printed commit.")
add(old_records, r"\newcommand{\SsixPublishRecords}{" + RECORDS + "}", "preamble: records-page address", "Continuation prompt section 0.3 fixes the standing records page and Paper II anchor.")
old_method = "The check records and programs are linked from the\n\\href{\\SsixPublishRecords}{project repository}."
new_method = "The check records and programs are available on the\n\\href{\\SsixPublishRecords}{records page} for this paper; the repository\ncommit is \\texttt{\\SsixRepositoryCommit}."
add(old_method, new_method, "section 1.5: records and programs", "The sole repository link is the standing records page, and the prescribed commit is printed once in section 1.5.")
for row in resolved:
    if not row["old_exact"]:
        if row["repository_path"] == extra_path:
            assert row["sha256"] == "435b69ace886218229aaeda3b049a14008e60d110706e762839f6a63028f354b"
        continue
    add(row["old_exact"], r"\nolinkurl{" + row["printed_path"] + "}",
        "Programs: " + row["old_printed"],
        "The file is identified by a plain path; the attached repository path list or checkpoint code/ resolves it, and the records table records its full path and exact SHA-256.", "D09")
old_program_intro = "The following files contain the indicated computations at commit\n\\begin{center}\\small\\ttfamily\\SsixRepositoryCommit\\end{center}\nEach link identifies the complete repository path."
new_program_intro = "The following programs implement the indicated computations.\nThe records page cited in the methodology gives their source files."
add(old_program_intro, new_program_intro, "Programs: introduction", "The commit is printed once in section 1.5; the Programs table gives plain paths and introduces no additional repository link.", "D09")
old_end = "\\end{longtable}}\n\n\\begin{thebibliography}"
extra_row = "Integral lattice quotients, clutch maps, local cellular differentials and Mayer--Vietoris matrices (\\cref{night:P4.3,night:P4.4}) & \\nolinkurl{" + extra_path + "} \\\\[3pt]\n"
torus_row = "Primitive quotient bases, integral clutchings and Smith forms (\\cref{cdp:st:D.2.7}) & \\nolinkurl{" + torus_path + "} \\\\[3pt]\n"
add(old_end, extra_row + torus_row + old_end, "Programs: compact integral examples", "The duplicated matrix listing was removed after comparison with its defining maps. This single program row records its lattice quotients, clutch maps, local differentials, F1/F2 matrices, determinants and Smith forms. Exact pinned bytes agree with the packed historical program. Add the separately required D.2.7 primitive quotient-basis program with its attached repository path.", "D09")
write_tsv(OUT / "S6_SERIES_PUBLISH_c3_provenance_link_edits.tsv", fields, edits)
print("Resolved", len(resolved), "program paths:", sum(r["repository_path"].startswith("code/") for r in resolved), "checkpoint programs and", sum(not r["repository_path"].startswith("code/") for r in resolved), "historical repository programs.")
print("Prepared", len(edits), "exact edit-log rows; no shared file was changed.")
