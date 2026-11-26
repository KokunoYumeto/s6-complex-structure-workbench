"""Final bounded reading-scope/coordinate clarification, preserving prior bytes."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib

root = Path(__file__).resolve().parents[1]
lane = root / "agents/continuation7_iii_vertical_correction"
path = lane / "S6_SERIES_PUBLISH_III_02LS_fresh_derivation.md"
saved = lane / "S6_SERIES_PUBLISH_III_02LS_fresh_derivation_draft_v001.md"
blob = path.read_bytes()
assert sha256(blob).hexdigest() == "af9c1e81032492cc676f24ec18e7357278fb4f0a868b889020032f417ce34846"
assert not saved.exists()
saved.write_bytes(blob)
before = blob.decode()
after = before
changes = [
("""  at08:51:05.219879 UTC, with Sections4--6 reread here: the general
  primitive rank-one/cusp chart and specialization maps.""",
"""  at08:51:05.219879 UTC, with the exact bounded passages253--307
  and453--596 reread here: the general primitive rank-one/cusp
  chart and specialization maps."""),
("""The invariant vector eta=-e4 satisfies m_can^t eta=1.
""",
"""In the new order c_new=P m_can and eta_new=-e4 satisfy
c_new^t eta_new=1; the old-order vector is P^t eta_new.
"""),
("""The toric cover and its contractible cell
charts give pi1=Z<h,w0>; the two long translations are its
generators, with their coordinate reading as inverse.
The primitive conductor calculation gives H2=Z4,H3=Z2,H4=Z.
Its H4 generator is the one oriented central component.
""",
"""The normalized toric surfaces and their double curves are
simply connected, and their lifted dual cell complex is the
triangulated plane. Van Kampen on that cover therefore gives
trivial fundamental group. Its two period deck translations
give pi1=Z<h,w0>, with their coordinate reading as inverse.
The primitive conductor calculation gives H2=Z4 and H4=Z.
Its degree-three group is a kernel between free conductor
chain groups and is free; the two triangle strata give
Euler number2, so its rank is2. Thus H3=Z2. The H4
generator is the one oriented central component.
"""),
("""All preceding partial LS notes and actual execution
streams are preserved.""",
"""The completed-proof assembler and its first narrow edit
are code/S6_SERIES_PUBLISH_c7_ls_finish_v001.py and
code/S6_SERIES_PUBLISH_c7_ls_finish_edit_v001.py, with their
actual successful .out and empty .err streams. The exact
first-written assembler is preserved as
code/S6_SERIES_PUBLISH_c7_ls_finish_v001_preexecute.py;
it was not executed. Before the first assembly, the edit
made the ordinary boundary map's domain/direction and
the six-disc sign conversion explicit, and clarified
the zero-based array notation and H^3 symbol. No failed
mathematical run is attributed to that unexecuted source.

The final bounded edit is
code/S6_SERIES_PUBLISH_c7_ls_finish_edit_v002.py, with its
actual .out/.err and complete retained .diff. It preserves
the first assembled proof as
S6_SERIES_PUBLISH_III_02LS_fresh_derivation_draft_v001.md.
It makes the recent LJ rereading scope literal, labels
eta's coordinate order explicitly, and spells out the
cusp cover/conductor inference and this execution record.
The mathematical program and all of its outputs are unchanged.
A read-only rg lookup initially used the wrong directory
for the admitted KQ receiver and returned a missing-file
diagnostic; the filename was then resolved in the authorized
carrier folder. No target original was opened by that lookup.

All preceding partial LS notes and actual execution
streams are preserved."""),
]
for old, new in changes:
    assert after.count(old) == 1, old
    after = after.replace(old, new)
path.write_text(after)
diff = root / "code/S6_SERIES_PUBLISH_c7_ls_finish_edit_v002.diff"
assert not diff.exists()
diff.write_text("".join(difflib.unified_diff(
    before.splitlines(True), after.splitlines(True),
    fromfile="fresh_derivation_draft_v001", tofile="fresh_derivation_final")))
print("EDITED", datetime.now(timezone.utc).isoformat())
print("PRESERVED_DRAFT", saved.relative_to(root), sha256(blob).hexdigest())
print("FINAL_PROOF", path.relative_to(root), sha256(path.read_bytes()).hexdigest())
print("LINES", len(after.splitlines()), "BYTES", len(after.encode()))
print("EXACT_REPLACEMENTS", len(changes), "DIFF", diff.relative_to(root))
print("SCOPE: bounded final exposition/provenance clarification; all mathematical computation bytes unchanged.")
