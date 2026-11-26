"""Apply the complete readback corrections to the three LT receiving bodies."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
import re
ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
P = "S6_SERIES_PUBLISH_III_02LT_"
path = LANE / (P + "receiving.tex")
old_raw = path.read_bytes()
assert sha256(old_raw).hexdigest() == "3da39e584754c0682545f169c594019d57f09d8aba1c9047f075498700187156"
old = old_raw.decode()
new = old
changes = [
 (r"\begin{proof}" + "\n", r"\begin{proof}" + "\n" +
  "Set $A_0=\\sigma-I$. Every orbit is ordered by the return in the\n"
  "positive roof direction; the scalar circle has its complex orientation.\n"),
 (r"\rho(p)", r"\varrho(p)"),
 (r"\begin{split}", r"\begin{aligned}"),
 (r"\end{split}", r"\end{aligned}"),
 ("The component degrees remain the literal $c_i$. The component clutch degree is $c_i$ at each component.",
  "The component clutch degree is the given integer $c_i$ at each component."),
 (r"\paragraph{The two extension maps.}" + "\nThe orbit relations themselves are",
  r"\paragraph{The two extension maps.}" + "\nFor $c\\ne0$, the orbit relations are"),
 ("For $c=0$, this sequence is split by the infinite class $t$.",
  "For $c=0$, the Wang sequence is\n"
  "$0\\to\\mathbb Z^\\rho\\to\\mathbb Z^\\rho\\oplus\\mathbb Zt\n"
  "\\to\\mathbb Z\\to0$, with section given by the infinite class $t$."),
 ("This proves freeness and supplies both quotient maps with the displayed inverse.",
  "These maps give the quotient and its inverse over the integers."),
 ("No cancellation has been made in the $\\mathbb Z/h$ coordinate.",
  "The scalar-long coordinate is read separately by \\eqref{maps:eq:IC_local_15}."),
 ("This includes the star degrees of the line bundles in Theorem~\\ref{maps:src:D.2.50}\n",
  "This includes the following star degrees from Theorem~\\ref{maps:src:D.2.50}:\n"),
]
for a, b in changes:
    assert a in new, a
    new = new.replace(a, b)
labels = re.findall(r"\\label\{([^}]+)\}", new)
assert len(labels) == len(set(labels))
for ref in re.findall(r"\\eqref\{(maps:eq:IC_local_[^}]+)\}", new):
    assert ref in labels, ref
assert not any(ord(ch) < 32 and ch not in "\n\t" for ch in new)
assert new.count(r"\begin{equation}") == new.count(r"\end{equation}")
cut = new.index(r"\begin{proof}")
parts = {"receiving.tex": new,
         "receiving_statement.tex": new[:cut].rstrip() + "\n",
         "receiving_proof.tex": new[cut:]}
print("START", datetime.now(timezone.utc).isoformat())
print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                fromfile="receiver_v2", tofile="receiver_v3")), end="")
for name, value in parts.items():
    target = LANE / (P + name)
    target.write_text(value, encoding="utf-8", newline="\n")
    raw = target.read_bytes()
    print("FILE", name, len(raw), len(raw.splitlines()), sha256(raw).hexdigest())
print("ALL_LOCAL_EQUATION_REFERENCES_RESOLVE", True)
print("END", datetime.now(timezone.utc).isoformat())
