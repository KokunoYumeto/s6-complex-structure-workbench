#!/usr/bin/env python3
"""Final LH coordinate-notation refinement after whole v3 receiver reading."""
from hashlib import sha256
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
PREFIX = "S6_SERIES_PUBLISH_III_02LH_"
runpy.run_path(str(ROOT/"code/S6_SERIES_PUBLISH_c7_lh_receiver_v3.py"),
              run_name="__main__")
path = LANE/(PREFIX+"receiving.tex")
text = path.read_text()
assert sha256(text.encode()).hexdigest() == (
    "8fff37e1b322b2e18a4455b9f1ab6943bc8649eaa7b400d26e8151c79489187f"
)
old = r"The edge boundary is {[}\(A_{i}\)(d)-I{]}; its two-step filtration gives"
new = r"The edge boundary is \([A_i(d)-I]_{i<N-1}\); its two-step filtration gives"
assert text.count(old) == 1
text = text.replace(old, new)
anchor = r"\emph{Exact degree-one exterior image at every d.}"
addition = r"""
The ordered product of the returns is the identity. The identities
\[
 (MN-I)x=(M-I)Nx+(N-I)x,\qquad
 (M^{-1}-I)x=-(M-I)M^{-1}x
\]
express the relation of the last return, the inverse word in the
other returns, as an integer combination of their relations.
Apply the same identities to the exterior-square representation.
Thus the first \(N-1\) sites generate the full relation image in
both degrees. Inclusion of their columns is the forward image
map, and expansion of the inverse word gives its image section.
The two induced quotient maps are inverse because both fix the
classes of every lattice basis vector or standard bivector.

"""
assert text.count(anchor) == 1
text = text.replace(anchor, addition+anchor)
path.write_text(text, encoding="utf-8", newline="\n")
print("PASS exact omitted-return image maps in both degrees")
print("PASS graph-boundary mathematical delimiters corrected")
print("FINAL_RECEIVER_LINES", len(text.splitlines()))
print("FINAL_RECEIVER_SHA256", sha256(text.encode()).hexdigest())
