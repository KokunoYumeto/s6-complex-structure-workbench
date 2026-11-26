"""Read-only provenance and equation-locator inventory for the minimal unit."""
from datetime import datetime, timezone
import difflib
import hashlib
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
fragment = root / "agents/continuation8_iii_integration/units/weighted/minimal_primary_types.tex"
source = fragment.read_text()
print("UTC", datetime.now(timezone.utc).isoformat())
print("INPUT", len(source.splitlines()), hashlib.sha256(fragment.read_bytes()).hexdigest())
for unit, number, lane in [("LB", 35, "conic"), ("LC", 36, "odd_cubic"), ("LE", 38, "mixed_torsion")]:
    label = "maps:src:D.2." + str(number)
    anchor = source.index("\\label{" + label + "}")
    begin = source.rfind(r"\begin{theorem}", 0, anchor)
    end = source.index(r"\end{proof}", anchor) + len(r"\end{proof}")
    received = root / ("agents/continuation7_iii_" + lane) / ("S6_SERIES_PUBLISH_III_02" + unit + "_receiving.tex")
    old = received.read_text().strip()
    current = source[begin:end].strip()
    print("RECEIVER", unit, len(received.read_text().splitlines()), hashlib.sha256(received.read_bytes()).hexdigest())
    difference = list(difflib.unified_diff(old.splitlines(), current.splitlines(), fromfile="admitted_" + unit, tofile="repaired_extract_" + unit, lineterm=""))
    print("DIFF_LINES", len(difference))
    print("\n".join(difference))
manual = re.findall(r"\\qquad\\textup\{\((\d+)\)\}", source)
print("MANUAL_DISPLAY_NUMBERS", len(manual), ",".join(manual))
le_start = source.index(r"\begin{theorem}[the mixed ten-")
le = source[le_start:]
print("LE_LITERAL_PARENTHESIZED_NUMBERS", ",".join(sorted(set(re.findall(r"\((\d+)\)", le)), key=int)))
for name in ["S6_SERIES_PUBLISH_c7_lb_conic.py", "S6_SERIES_PUBLISH_c7_lb_post_exposure.py", "S6_SERIES_PUBLISH_c7_lc_odd_cubic.py", "S6_SERIES_PUBLISH_c7_lc_post_exposure.py", "S6_SERIES_PUBLISH_c7_le_mixed_v001.py", "S6_SERIES_PUBLISH_c7_le_post_exposure_v001.py"]:
    path = root / "code" / name
    if path.exists():
        print("RETAINED_PROGRAM", path.relative_to(root), hashlib.sha256(path.read_bytes()).hexdigest())
    else:
        print("PROGRAM_NAME_NOT_FOUND", name)
print("WRITES0; MATHEMATICAL_CREDIT0; SOURCE_CONTENT_READING_NOT_INFERRED")
