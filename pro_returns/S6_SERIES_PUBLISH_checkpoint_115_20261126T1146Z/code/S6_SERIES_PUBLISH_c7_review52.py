"""Fourth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 24, 23, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / "PROGRESS_LEDGER.md").read_text()
assert "\n## Review 52 — " not in ledger
baseline = re.search(r"Closed required identities at Review51: ([^\n]+)\.", ledger)
assert baseline
previous = set(baseline[1].split(", "))
assert len(previous) == 99


def table(name):
    with (ROOT / name).open(newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return reader.fieldnames, list(reader)


fields, rows = table("S6_SERIES_PUBLISH_required_progress_III.tsv")
events = {r["event_id"]: r for r in table("CHECK_EVENTS.tsv")[1]}
updates = {
    "02L0": ("root_comparison_review_final_scope_records_pending",
             "/root/iii_graph",
             "Root has read the whole original, receiver, comparison, post-exposure auxiliaries and programs. The global flop map's extra pointwise-other-caps claim is removed at post-exposure scope; frozen fresh bytes remain unchanged. Final packet records and root admission remain open."),
    "02L1": ("whole_comparison_written_root_receiver_review_pending",
             "/root/iii_02kr",
             "Complete fresh proof preceded individual original release. The receiver and comparison record the physical-fan counterexample and the global relative-ball scope clarification. Root has read the new all172 auxiliary program/output; the entire original/receiver root comparison remains open."),
    "02L2": ("fresh_integral_star_cap_maps_in_progress",
             "/root/iii_graph",
             "Original closed. Fresh work has exact primitive I1-star period and component-stabilizer group maps. The remaining gate is the integral normalization/conductor maps, fibre coefficients and boundary surjectivity at the two minimal orders; no target torsion table is yet claimed."),
    "02L7": ("fresh_derivation_written_root_review_in_progress",
             "/root/iii_02ks",
             "Original closed. Root has read fresh Sections1--13, including preservation of component sections and the quotient localization. Complete new program/output reading and final freeze review remain before release."),
    "02L8": ("fresh_derivation_written_root_review_pending",
             "/root/iii_02ks",
             "Original closed. A complete fresh draft and independent all172 catalogue/maps are written. Root's full mathematical and output review remains before release."),
    "02L9": ("fresh_derivation_assigned",
             "/root/iii_02kr",
             "The statement/dependency-only packet was read by root and assigned after L1's final packet freeze. Original and historical target programs remain closed. Required new work covers all120 nonzero-Chern multiplicative sites, the495-pattern quotient, full boundary maps and both Euler ranks."),
}
for row in rows:
    if row["tag"] in updates:
        state, checker, note = updates[row["tag"]]
        assert row["status"] == "open"
        row["packet_status"] = state
        row["assigned_checker"] = checker
        row["notes"] += " Review52: " + note

closed = [r for r in rows if r["status"] == "done"]
tags = {r["tag"] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
for row in closed:
    for eid in row["check_event_id"].split(";"):
        eid = eid.strip()
        if eid:
            assert eid in events and events[eid]["statement_id"] == row["label"]
open_rows = [r for r in rows if r["status"] != "done"]
pending = [r["tag"] for r in open_rows if r["proof_status"] == "released_after_derivation"]
units = Counter(r["paper"] for r in table("S6_SERIES_PUBLISH_unit_progress.tsv")[1]
                if r["status"] == "open")
assert units["III"] == 784 and units["IV"] == 756
source_sha = hashlib.sha256((ROOT / "S6_SERIES_PUBLISH_III.tex").read_bytes()).hexdigest()
assert source_sha == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
old_counts = re.findall(r"Consecutive reviews without qualifying movement: (\d+)\.", ledger)
assert old_counts
no_movement = 0 if new else int(old_counts[-1]) + 1
open_table = "\n".join(
    "| " + r["tag"] + " | " + r["label"] + " | " + r["packet_status"]
    + " | " + r["proof_status"] + " |"
    for r in sorted(open_rows, key=lambda r: r["tag"]))
note = f'''
## Review 52 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review51, {len(new)} required identities have closed:
{', '.join(new) or 'none'}. Paper III has {len(closed)}/128 complete
and {len(open_rows)} open. Every closure resolves to its exact check
events, and no admitted identity has reopened. These required-row
closures are the qualifying movement; the no-movement count is reset.

KX's complete comparison settles the natural initial catalogue,
original-cap Chern alternatives, cusp maps and rank budget. KZ
settles the I3-star exclusion by exact primitive periods, every deck
reflection offset, both original Chern cases, full boundary image,
degree-one refinement map and global quotient injection.
Their original proofs and every auxiliary were read before admission.

L4 and L6 are admitted after complete fresh derivations, individual
release, full original/receiver comparison, all new programs and all
output. Their formulas retain finite core torsion, exact normal
Chern orders, all proper-power freeness, the full Thom image,
every global homology degree and both one-site Euler cases.
L4's D26 scope repair explicitly relates the68 local primitive-gamma
positions to the62 nonstar positions by a marked-tuple inclusion
with six-element complement. The fresh note's auxiliary finite-lift
illustration is corrected post-exposure to N_m lambda in its
general scope; its target kernels and clutch/minor proofs were
derived directly before release. Frozen fresh bytes remain intact.

L0 and L1 are released comparisons still awaiting root admission.
Their concrete physical-fan counterexamples leave the theorem
conclusions proved by actual fan transport and oriented reconstruction.
L0 also replaces a false positive-local-defect explanation at an I2
original by a primitive global meridian two-cycle and free H2 summand.
Root's receiver reading found an unnecessary stronger relative scope
in the fresh auxiliary fan arguments. The individual smooth flop
maps are relative to their transported ball boundaries; their
composition is a global diffeomorphism. The other cap data are
unchanged in constructing the physical-fan representative, while
pointwise preservation by that global map is not claimed.
This correction is recorded post-exposure without changing fresh
bytes or claiming an additional mathematical refutation.

L2's main local gate is its integral I1-star normalization/conductor
comparison at the two minimal orders, including fibre coefficients
and complete boundary image. Its original remains closed.
L7/L8 have complete fresh drafts and a separate independent
all172 computation. Root's L7 reading verifies the extra free
component sections, their preservation through global flop balls,
and fixed-sphere localization in the quotient complement.
Full code/output and L8 review precede their individual release.
L9 is assigned for a fresh complete multiplicative extension.
No draft, release preparation or assignment supplies row credit.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

Released comparisons still open: {', '.join(pending) or 'none'}.
The required-progress table retains each row's individual evidence.
All {units['III']} III unit criteria, all66 IV required checks and
all {units['IV']} IV unit criteria remain open in their existing tables.
Canonical III remains unchanged at SHA256 {source_sha}.
The main gate is completion of III's required checks before the
whole unit pass, guarded source/bibliography integration, provenance,
clean build and final rendered-page reading. IV follows III.
I, II and V retain their closed gates until the five-together step;
the specified II E.5.2/E.5.3 inputs remain unchanged.

Checkpoint75 holds the103/128 state at23:20:02 UTC. This review and
later work are due in checkpoint76 at00:04:24 UTC on25 November.
No packaging, status metadata or side computation is counted as
qualifying movement.

Closed required identities at Review52: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T00:34:24+00:00.
Next checkpoint: 2026-11-25T00:04:24+00:00.
This review refreshes no inventory or census and creates no edit
manifest, seal, receipt, rebinding or derived-file copy.
'''
buf = io.StringIO(newline="")
writer = csv.DictWriter(buf, fields, delimiter="\t", lineterminator="\n")
writer.writeheader()
writer.writerows(rows)
(ROOT / "S6_SERIES_PUBLISH_required_progress_III.tsv").write_text(buf.getvalue(), newline="\n")
for name in ("PROGRESS_LEDGER.md", "S6_SERIES_PUBLISH_report.md"):
    p = ROOT / name
    prior = p.read_text()
    assert "\n## Review 52 — " not in prior
    p.write_text(prior + note, newline="\n")
print(f"Review52: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}")
print("Newly completed: " + ", ".join(new))
print("Released comparisons open: " + ", ".join(pending))
print("Recorded UTC: " + now.isoformat())
