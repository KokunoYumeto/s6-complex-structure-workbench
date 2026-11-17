"""Map the supplied CDP register and working-edition statements without judging proofs."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT.parent / "sources"
OUT = ROOT / "work/cdp_audit"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "extracted").mkdir(exist_ok=True)
CDP = SOURCES / "returns/S6_03_CDP"
rows = list(csv.DictReader((CDP / "S6_03_CDP_results.csv").open()))
blocks = {}
pattern = re.compile(r"\\begin\{(?:statement|idstatement)\}\{([^}]*)\}")
for file in (CDP / "build/ordered").glob("*.tex"):
    content = file.read_text()
    matches = list(pattern.finditer(content))
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[match.start():end]
        blocks[match[1]] = dict(text=block, file=str(file.relative_to(SOURCES)),
            line_start=content.count("\n", 0, match.start()) + 1,
            line_end=content.count("\n", 0, end) + 1)

manifest = []
for row in rows:
    block = blocks[row["id"]]
    target = OUT / "extracted" / ("CDP_" + row["id"].replace(".", "_") + ".tex")
    target.write_text(block["text"])
    manifest.append(dict(source_run="S6_03_CDP", source_id=row["id"],
        source_title=row["statement"], source_status=row["status"],
        source_file=row["where_proved"], canonical_file=block["file"],
        canonical_line_start=block["line_start"], canonical_line_end=block["line_end"],
        extracted_file=str(target.relative_to(ROOT)),
        proof_present="\\begin{proof}" in block["text"],
        proof_sha256=hashlib.sha256(block["text"].encode()).hexdigest(),
        depends_on=row["depends_on"], recorded_checks="", own_check="",
        check_outcome="pending", credit_checks="", remarks=""))

# Do not overwrite the active audit verdicts when rerunning an extraction.
(OUT / "source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
with (OUT / "source_manifest.csv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(manifest[0]))
    writer.writeheader()
    writer.writerows(manifest)

working = []
env_pattern = re.compile(r"\\begin\{(theorem|proposition|lemma|corollary|claim|test)\}(?:\[([^\]]*)\])?")
for relative in ["workbench/cdp_program.tex", "correction_note/N_singular_fibre_vanishing_step.tex",
                 "workbench/analytic_picard_local_obstruction.tex", "workbench/analytic_picard_completion.tex"]:
    file = SOURCES / relative
    content = file.read_text()
    matches = list(env_pattern.finditer(content))
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        env_end = content.index("\\end{" + match[1] + "}", match.end())
        statement = content[match.start():env_end + len(match[1]) + 6]
        label = re.search(r"\\label\{([^}]*)\}", statement)
        identifier = label[1] if label else f"unlabelled-{i + 1}"
        token = ("WB_" if relative.startswith("workbench") else "CN_") + identifier.replace(":", "_")
        output = OUT / "extracted" / (token + ".tex")
        output.write_text(content[match.start():end])
        working.append(dict(source_run="WORKING_CDP" if relative.startswith("workbench") else "CORRECTION_NOTE_20260901",
            source_id=identifier, source_file=relative,
            source_line_start=content.count("\n", 0, match.start()) + 1,
            kind=match[1], title=match[2] or "", paper="II", printed_label="",
            source_statement=statement, extracted_file=str(output.relative_to(ROOT)),
            taken_over_by="", distinct_proof="pending comparison", recorded_checks="",
            own_check="", check_outcome="pending", notes=""))
with (OUT / "working_edition_inventory.csv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(working[0]))
    writer.writeheader()
    writer.writerows(working)
(OUT / "working_edition_inventory.json").write_text(json.dumps(working, indent=2) + "\n")
print(f"Matched {len(manifest)} CDP rows and {len(working)} labelled working-edition/correction-note results.")
