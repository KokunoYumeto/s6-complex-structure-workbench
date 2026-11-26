"""Retain the first unexecuted assembler, then make exact orientation edits."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
path = root / "code/S6_SERIES_PUBLISH_c7_ls_finish_v001.py"
saved = root / "code/S6_SERIES_PUBLISH_c7_ls_finish_v001_preexecute.py"
blob = path.read_bytes()
assert not saved.exists()
saved.write_bytes(blob)
text = blob.decode()
changes = [
("""The core is
the ordinary four-torus; the exact covering formula

    (x,tau) -> (x+tau v, exp(2pi i tau))

and its inverse, obtained by choosing the sheet and
subtracting tau v, give the marked normal solid torus.
This is also the m=1 case of the admitted LI Thom map.
""",
"""The core is
the ordinary four-torus. Take the cap T4_y times D2_z.
Its exact boundary attaching map into the exterior is

    F_o(y,tau)=(x=y-tau v, exp(2pi i tau)),
    F_o^(-1)(x,tau)=(y=x+tau v, exp(2pi i tau)).

These maps are well-defined for tau modulo1 because v
is an integral period. The core-point normal meridian
is sent to mu_o-v. This specifies the solid-torus
attachment and its boundary inverse; it does not
assert that this boundary clutch extends over the
exterior puncture. It is the m=1 admitted LI Thom map.
"""),
("""Using the positive boundary orientation,
mu_o=-(mu0+...+mu4). Reversing that one normal-disc
generator if necessary expresses the six boundary
columns as
""",
"""Using the positive boundary orientation,
mu_o=-(mu0+...+mu4). In the positive exterior basis
(gamma,mu0,...,mu4), the columns of the ordinary
normal disc and the five positive singular discs
are [(e,-1,-1,-1,-1,-1)^t | e1 | ... | e5].
Change the exterior coordinates by diag(1,-I5)
and the relative disc generators by the same
matrix diag(1,-I5). Both matrices are their own
inverses. Thus the exact convention used in the
recorded component-disc calculation is
"""),
("""This reversal is a change of the relative generator,
not a deletion of a boundary sign; the program uses
this exact convention and records its inverse.
""",
"""The two displayed diagonal maps give the full
conversion from the positive boundary convention
and back. The program retains this literal matrix
and its inverse.
"""),
("""If U_R R V_R=D_R is the saved Smith factorization, its
literal quotient map is
""",
"""The integer-array indices for U_R,U_D and B_full
below start at zero; the geometric wedge labels
12,13,14,23,24,34 keep their usual one-based meaning.
If U_R R V_R=D_R is the saved Smith factorization, its
literal quotient map is
"""),
("""H3(X;Z); oriented cap product sends it to H3(X;Z)
homology.""",
"""H^3(X;Z); oriented cap product sends it to H3(X;Z)
homology."""),
]
for before, after in changes:
    assert text.count(before) == 1, before
    text = text.replace(before, after)
path.write_text(text)
print("EDITED", datetime.now(timezone.utc).isoformat())
print("PRESERVED_UNEXECUTED", saved.relative_to(root), sha256(blob).hexdigest())
print("FINAL_SOURCE", path.relative_to(root), sha256(path.read_bytes()).hexdigest())
print("EXACT_REPLACEMENTS", len(changes))
print("SCOPE: orientation/domain and index notation clarified before the first assembler execution.")
