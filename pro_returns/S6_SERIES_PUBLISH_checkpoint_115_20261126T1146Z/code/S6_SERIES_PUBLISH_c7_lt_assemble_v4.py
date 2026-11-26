"""Apply the final three explicit reading clarifications to the LT proof."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
P = "S6_SERIES_PUBLISH_III_02LT_"
path = LANE / (P + "receiving.tex")
old = path.read_text()
assert sha256(old.encode()).hexdigest() == "90853429d498d6e257f90fd191e33879422ea7955f8ac5c756bbb7913af92e61"
changes = [
 ("$D\\mid b$. Choose $aD+bg=1$. The section is",
  "$D\\mid b$. For coprime $g,D$, choose $aD+bg=1$. The section is"),
 ("On the punctured neighbourhood the canonical tensor map and its inverse are",
  "From the trivial line with its constant frame, the canonical tensor map\n"
  "on the punctured neighbourhood and its inverse are"),
 ("actual units are included in the clutch maps of section 2.",
  "units are included in the component clutch maps above."),
]
new = old
for a, b in changes:
    assert new.count(a) == 1, a
    new = new.replace(a, b)
print("START", datetime.now(timezone.utc).isoformat())
print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                fromfile="receiver_v3", tofile="receiver_v4")), end="")
cut = new.index(r"\begin{proof}")
for name, value in (("receiving.tex", new), ("receiving_proof.tex", new[cut:])):
    target = LANE / (P + name)
    target.write_text(value, encoding="utf-8", newline="\n")
    raw = target.read_bytes()
    print("FILE", name, len(raw), len(raw.splitlines()), sha256(raw).hexdigest())
print("STATEMENT_UNCHANGED", sha256((LANE / (P + "receiving_statement.tex")).read_bytes()).hexdigest())
print("END", datetime.now(timezone.utc).isoformat())
