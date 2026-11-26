"""Finish and apply the two opening body units, preserving all identities."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import csv

import S6_SERIES_PUBLISH_c8_integrate_units as units
import S6_SERIES_PUBLISH_c8_root_units as records

ROOT = units.ROOT
radial_path = units.WORK / "root/radial_coordinates.tex"
before = radial_path.read_text(encoding="utf-8")
old = r"""In the cusp coordinate of the marked period family, write
\[
 \Pi=[Z\mid I_2],\qquad
 Z=s\begin{pmatrix}0&1\\-1&0\end{pmatrix}
       +\begin{pmatrix}6\mu(t)&h(t)\\b(t)-h(t)&\mu(t)\end{pmatrix},
 \qquad t=e^{2\pi i s}.
\]
The functions $\mu,b,h$ are holomorphic on a disc containing zero.
On the positive radial ray we put $t=e^{-2\pi T}$ and $s=iT$, and set
"""
new = r"""Use the cusp coordinate $t_c=1/t$ on the marked base and the
logarithmic coordinate $t_c=e^{2\pi i s}$. Put
$\beta=\beta^{\rm part}+c$, $h=\tau-s$, and $b=\beta+\tau$.
The inverse substitutions are $\tau=s+h$ and $\beta=b-s-h$.
The cusp expansion of \cite[Proposition~3.21, p.~22]{AC26} gives
\[
 \Pi=[Z\mid I_2],\qquad
 Z=s\begin{pmatrix}0&1\\-1&0\end{pmatrix}
       +\begin{pmatrix}6\mu(t_c)&h(t_c)\\
                       b(t_c)-h(t_c)&\mu(t_c)\end{pmatrix}.
\]
The functions $\mu,b,h$ are holomorphic on a disc containing zero.
On the positive radial ray put $t_c=e^{-2\pi T}$ and $s=iT$, and set
"""
if before.count(old) != 1:
    raise ValueError("Stale radial primary-source guard")
after = before.replace(old, new, 1)
old_substitution = "Substitution of $t=e^{-2\\pi T}$ gives"
new_substitution = "Substitution of $t_c=e^{-2\\pi T}$ gives"
if after.count(old_substitution) != 1:
    raise ValueError("Stale Taylor parameter guard")
after = after.replace(old_substitution, new_substitution, 1)
units.check_permanent_identifiers(before, after)
fields, defects = records.table(records.DEFECTS)
ident = "III-C8-RADIAL-PRIMARY-CUSP-FORM"
if any(r["change_id"] == ident for r in defects):
    raise ValueError("Radial source completion already recorded")
defects.append(dict(change_id=ident, type="D06", statement_id="mapsIII:def:radial-cusp-data",
    old_location="radial cusp input and its obsolete compendium pointer", old_page="pending page concordance",
    new_location="Definition mapsIII:def:radial-cusp-data", new_page="pending final PDF",
    old_text=old, new_text=new,
    reason="Opened AC26 Proposition3.21 and its complete proof on printedp22. Its cusp holomorphic functions give the exact displayed form. State both substitutions between tau,beta and s,h,b and distinguish the cusp coordinate t_c=1/t from the base coordinate. The later Taylor substitution uses that same t_c.",
    review_status="source change applied; final page review open"))

# Only the completed opening body units and the preamble changes enter the
# canonical source. Other agents' in-progress fragments are not read here.
canonical_path = units.repairs.SOURCE
canonical = canonical_path.read_text(encoding="utf-8")
pieces = units.parse_pieces(canonical)
original = units.fragments(canonical, pieces)
old_radial = original["radial_coordinates"] + original["regular_quotients"]
if canonical.count(old_radial) != 1:
    raise ValueError("The original radial/global units are not one guarded contiguous block")
candidate = canonical.replace(old_radial, "", 1)
common = (units.WORK / "root/common_conventions.tex").read_text(encoding="utf-8")
preamble = (units.WORK / "root/preamble.tex").read_text(encoding="utf-8")
regular = (units.WORK / "root/regular_quotients.tex").read_text(encoding="utf-8")
for old_text, new_text, name in (
    (original["common_conventions"], common + after, "opening body units"),
    (original["preamble"], preamble, "preamble"),
    (original["further_cusp_carriers"], regular + original["further_cusp_carriers"], "global quotient placement"),
):
    if candidate.count(old_text) != 1:
        raise ValueError("Stale canonical application guard: " + name)
    candidate = candidate.replace(old_text, new_text, 1)
allowed_labels = ["mapsIII:def:marked-family", "mapsIII:rem:dual-transport",
    "mapsIII:def:period-parameters", "mapsIII:def:engel-marking",
    "mapsIII:sec:marked-conventions", "mapsIII:def:radial-cusp-data"]
allowed_targets = ["tag-Q00" + str(n) for n in range(6)]
units.check_permanent_identifiers(canonical, candidate, allowed_labels, allowed_targets)
radial_path.write_text(after, encoding="utf-8", newline="\n")
canonical_path.write_text(candidate, encoding="utf-8", newline="\n")
records.write_table(records.DEFECTS, fields, defects)
now = datetime.now(timezone.utc).isoformat()
print("CANONICAL_OPENING_UNITS_APPLIED", now)
print("PREAMBLE", "pdfLaTeX fonts, section equations, small tag and proof-hook changes")
print("BODY", "common conventions and radial quotient prerequisites in their final opening order")
print("RELOCATED", "complete global quotient theorem before further cusp carriers")
print("NEW_IDENTITIES", len(allowed_labels), "labels and", len(allowed_targets), "targets")
print("PRESERVED", "every existing label and hypertarget multiplicity")
print("OTHER_AGENT_FRAGMENTS", "not read or applied")
print("NO_CREDIT", "review/progress/check tables await complete readback")

