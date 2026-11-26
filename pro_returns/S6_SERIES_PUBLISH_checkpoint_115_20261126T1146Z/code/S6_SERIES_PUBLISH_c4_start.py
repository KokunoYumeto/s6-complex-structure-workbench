"""Record continuation four without refreshing derived publication records."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "2026-11-23T10:47:46+00:00"
HEADING = f"## Fourth continuation started — {START}"

addition = f"""

{HEADING}

The continuation resumes the merged checkpoint-44 working directory. Running
`python restore_cp44.py` verified all 12,789 base files with zero mismatches.
The first recorded session time is {START}. The attached continuation prompt
dated 23 November controls restoration, links, checkpoints and the work order.

Paper II's 198 required checks remain resolved. Its complete horizontal/interface
tail, conductor package 18 and original sections 07, 10 and 11 remainders are
being compared with the current manuscript. Three parallel readers prepare these
disjoint packages; root owns manuscript and central table integration, overall
placement and provenance. D10 and D16 remain done. The per-unit table starts with
4,738 done and 982 open rows for II; III has 728 open rows and IV has 702.
These counts describe the inherited state and receive no movement credit.

Main theorem C still awaits the interface admission. Global structure, provenance,
text-final derived records, final build and every final Paper II PDF page remain
open. Papers III and IV follow II, with 128 and 66 required checks respectively.
The five-paper step follows those gates. Papers I and V retain their closed gates
and their attached public/submitted texts of record. The two protected Paper II
statements push:src:E.5.2 and push:src:E.5.3 are unchanged at continuation start.

No result, proof comparison or final-page reading is credited by initialization.
No manifest, seal, census, inventory or derived-record refresh is made for it.
Checkpoint 45 is due 2026-11-23T11:32:46+00:00; review 30 is due
2026-11-23T11:47:46+00:00. Consecutive reviews without movement: 0.
"""

for name in ("PROGRESS_LEDGER.md", "S6_SERIES_PUBLISH_report.md"):
    path = ROOT / name
    text = path.read_text()
    if HEADING in text:
        raise SystemExit(f"Continuation already recorded in {name}")
    if name == "PROGRESS_LEDGER.md":
        for number, title in ((10, "Machine statement headers and navigation text"),
                              (16, "Statements without titles, titles with process words")):
            text = text.replace(
                f"| II | D{number}: {title} | open |",
                f"| II | D{number}: {title} | done; inherited gate preserved under continuation prompt §0.4 |",
            )
    path.write_text(text + addition, newline="\n")

print("Continuation four recorded; inherited gates retained; checkpoint 45 due 11:32:46 UTC.")
