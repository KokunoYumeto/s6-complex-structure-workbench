"""Record the two working page images actually read and their bounded edit."""
from S6_SERIES_PUBLISH_c4_edit import *

old = "For this cycle the equation $t=xy$ identifies the\ntwo actual normal lines as dual."
new = "For this cycle the equation $t=xy$ identifies the normal line\nbundles of each double curve in its two component surfaces as dual."
text = SOURCE.read_text()
if text.count(old) != 1:
    # The source's line wrapping is retained in the exact logged replacement.
    import re
    candidates = list(re.finditer(r"For this cycle the equation \$t=xy\$ identifies the\s+two actual normal lines as dual\.", text))
    if len(candidates) != 1:
        raise ValueError("Expected the unique reviewed normal-line sentence")
    old = candidates[0][0]
apply_edit(old, new, "II-C4-SUPPORT-NORMAL-LINES", ["D08"],
    "cdp:st:C.2.UN.54", "Hopf support graphs and diagonal cycles, proof",
    "Name both normal line bundles by their component inclusions. The double chart xy=t gives their unchanged duality map; the adjective carried no additional hypothesis.",
    "Root read the complete current UN54 statement and proof on working page657 and compared this exact replacement. The complete pre-admission proof comparison remains in II-C4-CONDUCTOR18-05.",
    old_page="working PDF page657, 797-page build")
add_event("cdp:st:C.2.UN.54", "II-C4-SUPPORT-NORMAL-LINES", "used and rechecked in this run",
    "Root read the complete current statement and proof on rendered working page657 after the conductor18 admission. Its xy=t sentence now names the normal bundles of the double curve in its two component surfaces, preserving exactly the same duality map. Compared the old and receiving full context; no changed hypothesis or conclusion and no independent derivation credit.",
    "Working page657, Proposition53.2; normal-product sentence", source=__file__)
set_unit_status("subsec:II:hopf-support-tree-remainder", "D08", "done",
    "The complete unit comparison is admitted. The additional adjective found on working page657 was removed through the unchanged xy=t normal-line duality, with the exact text logged; no instance remains in the reviewed unit.",
    "II-C4-CONDUCTOR18-05; II-C4-SUPPORT-NORMAL-LINES")
stamp = now()
with (ROOT / "S6_SERIES_PUBLISH_reading_II.md").open("a", newline="\n") as stream:
    stream.write(f"""

## Fourth-continuation working layout — {stamp}

Root rendered and read the entire working page images 655 and 657 of the
797-page PDF in `build/II_c4_working/`. Page 655 contains the support-incidence
lemma's full statement, its seven numbered displays and the opening proof.
Page 657 contains its proof conclusion, the complete Hopf support-graph
proposition and proof, and the canonical-height subsection opening. Displays,
labels, fonts and page boundaries are legible, with no clipping or overlap
observed. The normal-line sentence on page 657 was made explicit as recorded
in II-C4-SUPPORT-NORMAL-LINES; its rebuild remains due.

All three pdfLaTeX passes succeeded with shell escape disabled. The build has
one overfull box at most 2pt and zero undefined references/citations, missing
fonts/glyphs, duplicate labels/destinations, rerun requests or rendered
UNRESOLVED fallbacks. This is working-layout evidence only; every page of the
final candidate remains open.
""")
print("Read working pages655 and657; bounded normal-line wording logged; no final-page credit.")
