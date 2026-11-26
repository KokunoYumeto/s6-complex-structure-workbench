#!/usr/bin/env python3
"""Resolve the four normalization programs without changing shared records."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import csv
import hashlib
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents" / "continuation3_provenance"
TEMP = ROOT.parents[1] / "tmp" / "c3_programs"
COMMIT = "bc08b5278bcad2beb70b6862c5722f1b9f636db6"
prefix = "pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/"
names = ["E_triple_images.py", "A_low_delta_cusp.py", "E_binary_products.py", "E_cubic_double.py"]
known = set((ROOT.parent / "REPOSITORY_PROGRAM_PATHS.txt").read_text().splitlines())
with (OUT / "S6_SERIES_PUBLISH_records_II.tsv").open() as handle:
    existing = list(csv.DictReader(handle, delimiter="\t"))
assert not any(any(r["repository_path"].endswith("/"+name) for name in names) for r in existing)

def retrieve(name):
    path = prefix + name
    assert path in known
    url = "https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/"+COMMIT+"/"+path
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=35) as response:
        assert response.status == 200
        data = response.read()
    (TEMP / name).write_bytes(data)
    return dict(printed_path=path, repository_path=path, sha256=hashlib.sha256(data).hexdigest(),
        bytes=len(data), date_utc=datetime.now(timezone.utc).isoformat(), checked_at=url,
        status="Exact attached-list path; prescribed pinned bytes opened; absent from existing 125 program rows")

with ThreadPoolExecutor(max_workers=4) as pool:
    rows = list(pool.map(retrieve, names))

def write(name, fields, values):
    with (OUT / name).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        writer.writeheader(); writer.writerows(values)

write("S6_SERIES_PUBLISH_c3_provenance_extra_program_checks.tsv", list(rows[0]), rows)
write("S6_SERIES_PUBLISH_records_II_additions.tsv", ["printed_path", "repository_path", "sha256"], rows)
scopes = [
    r"Symbolic cubes, cubic discriminant poles and the nodal-image product map (\cref{cdp:st:A.5.19,ex:II:nodal-triple-affine-fibre})",
    r"Symbolic-square and symbolic-cube saturations, conormal frames, Hessian and cubic pole orders (\cref{cdp:st:A.5.19})",
    r"Weighted scaling, simple zeros and the endpoint intersection number for binary products (\cref{cdp:st:A.5.21})",
    r"Cubic coefficient degrees, intersection ranks, blowup charts and the scalar-zero coordinate and covering maps (\cref{cdp:st:C.2.D4.2,ex:II:vanishing-cubic-sphere,ex:II:vanishing-cubic-aspherical})",
]
new_rows = "".join(scope+" & \\nolinkurl{"+row["repository_path"]+"} \\\\[3pt]\n" for scope,row in zip(scopes,rows))
(OUT / "S6_SERIES_PUBLISH_c3_provenance_extra_program_rows.tex").write_text(new_rows)
anchor = "\\end{longtable}}\n\n\\begin{thebibliography}"
source = (ROOT / "S6_SERIES_PUBLISH_II.tex").read_text()
assert source.count(anchor) == 1
change = dict(change_id="II-C3-PROV-139", type="D09", statement_id="cdp:st:A.5.19;cdp:st:A.5.21;cdp:st:C.2.D4.2",
    old_location="Programs: end of table", old_page="current source; final page concordance pending",
    new_location="Programs: four normalization programs", new_page="integrated build pending",
    old_text=anchor, new_text=new_rows+anchor,
    reason="Resolve the four inherited body program names against their exact attached-list repository paths. Each is absent from the existing125 rows; pinned bytes were retrieved and their source read to match the listed computation scopes. The A_low_delta program checks the symbolic and jet computations in A.5.19; the exact nodal product map is in E_triple_images. Outputs remain associated with their generating program.",
    review_status="Four full program source files opened and their scopes compared; path and SHA256 metadata recorded; no mathematical-computation rerun claimed.")
write("S6_SERIES_PUBLISH_c3_provenance_extra_program_edits.tsv", list(change), [change])
for row in rows:
    print(row["repository_path"], row["sha256"], row["bytes"])
