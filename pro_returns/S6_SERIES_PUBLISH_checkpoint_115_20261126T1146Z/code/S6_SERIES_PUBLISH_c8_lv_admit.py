"""Record root's completed whole 02LV comparison and support admission."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation8_iii_lv"
PREFIX = "S6_SERIES_PUBLISH_III_02LV_"
ALLOWED = {"targeted proof check", "independent re-proof",
           "computation or formal certificate", "used and rechecked in this run",
           "carried as background without fault found",
           "refuted, with the refined statement's id"}
NOW = datetime.now(timezone.utc).isoformat()


def table(path):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return reader.fieldnames, list(reader)


def write_table(path, fields, rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buffer.getvalue(), encoding="utf-8", newline="\n")


receiver = (LANE / (PREFIX + "receiving.tex")).read_text()
assert sha256(receiver.encode()).hexdigest() == "dd2d7970e3f5d0734dfebd1048976b4ad0a13cfbdc02b1db7ebe509673bebff8"
assert len(receiver.splitlines()) == 1365
assert receiver.count(r"\begin{theorem}") == receiver.count(r"\end{theorem}") == 1
assert receiver.count(r"\begin{proof}") == receiver.count(r"\end{proof}") == 1
assert len(re.findall(r"\\label\{([^}]+)\}", receiver)) == 69
assert len(re.findall(r"\\hypertarget\{([^}]+)\}", receiver)) == 69
comparison = LANE / (PREFIX + "comparison.md")
sources = LANE / (PREFIX + "source_checks.md")
assert comparison.is_file() and sources.is_file()
_, replacements = table(LANE / (PREFIX + "replacements.tsv"))
canonical = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text()
assert sha256(canonical.encode()).hexdigest() == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
for row in replacements:
    assert canonical.count(row["old_text"]) == 1
defect_fields, defects = table(LANE / (PREFIX + "defects.tsv"))
title_row = next(r for r in defects if r["change_id"] == "c8-III-02LV-statement-title")
assert title_row["type"] in {"D02", "D16"}
title_row["type"] = "D16"
fields, events = table(ROOT / "CHECK_EVENTS.tsv")
incoming_fields, incoming = table(LANE / (PREFIX + "CHECK_EVENTS.tsv"))
assert set(incoming_fields) <= set(fields)
assert incoming and all(r["type"] in ALLOWED for r in incoming)
assert all(r["statement_id"] == "maps:src:D.2.53" for r in incoming)
ids = {r["event_id"] for r in events}
assert not any(r["event_id"] in ids for r in incoming)
review_path = "agents/continuation8_iii_lv/" + PREFIX + "root_admission_review.md"
review = f"""# 02LV — whole comparison and root admission

Admitted {NOW}. This supporting theorem is maps:src:D.2.53, outside
the128 required identities. The canonical source remains unchanged.

## Root reading actually completed

Root wholly read the936-line frozen fresh derivation, all61 released
statement lines and875 released proof lines including their headers,
and the380-line following refined-class proof (plus its next heading).
The1304-line staged receiver was read in consecutive windows1–240,
241–520,521–800,801–1060,1061–1304. The complete final v005 diff was
then read, giving the1365-line receiving proof now admitted. Root read
the complete comparison and primary-source scope note, both new
comparison/character sources and all their18 and10 actual stdout lines;
both stderr streams are empty. The local defects/events/guards were
read before this admission. Root's additional signed-support proof
is recorded in the adjacent root_sign_review.md.

The five unchanged historical source/replay readings are attributed
to the receiving checker. Root does not claim a whole manual reading
of the1746-line relation-map JSON or a new primary-page opening. The
comparison records the actual inherited and current scopes, including
failed guard executions and the bounded review corrections. No second
blind LV derivation is claimed for this continuation.

## Mathematical decision

All theorem conclusions stand. The exact period matrix and inverse,
complement peripheral substitutions and relative kernel give the
index-two primitive lattice. The resolved Cremona map and exceptional
permutation identify the two Picard coordinate systems, including
their six ordered boundary curves. The integer relation-image maps
give the same core quotient and the same finite cochain on the full
ambient graph. The component cubic, every mixed coordinate and the
full quadratic/cubic coefficient groups agree through those maps.

The coupled original auxiliary error is repaired by the explicit
support-to-positive-Thom involution h=-Psi, with itself as inverse.
The actual floor differences retain their eighth tensor factors and
mixed-period cancellation. The oriented line clutch gives precisely
the core's affine gradients and constants without changing its area
value+1. The canonical divisor fibre action has weight+m; applied to
h=-Psi it gives the delta-circle character(0,-3r). The delta action
is explicitly inverse to W-line rotation. This supplies a complete
boundary-class comparison, including its coefficient-extension part.
Both finite localization representative sets have the required exact
divisibility. The staged receiver's frame shorthand and global-transfer
inverse shorthand were separately corrected during this review.

The receiver retains the original source-line edge(0,6)–(1,5), theta
frame, full quotient units, Phi embedding, endpoint inverse charts,
and Bott degree-four calculation. No geometric identification with
the fresh generic-edge sphere is assumed. Its full Wang-boundary
character proves that the retained sphere is a primitive odd class.
The complete critical nullchain, actual Borel pair and integral
Thom–Gysin equation give linking number−1 for that sphere. Together
with reference parity1 and the relative linking formula this proves
P_ref=0. Every original mathematical conclusion and permanent identity
is preserved in one theorem and one proof.

## Remaining publication work

The receiver SHA256 is
dd2d7970e3f5d0734dfebd1048976b4ad0a13cfbdc02b1db7ebe509673bebff8.
There are {len(replacements)} guarded replacements, {len(defects)} local
defect records and {len(incoming)} scoped events. These events are
merged without additional independent-check credit from assembly or
root readback. The exact error is D25 in intermediate identifications;
the theorem has no new D26/D27 refutation. The publication-unit edit,
canonical application, provenance review, final build and page reading
remain open. LV is now an admitted supporting input for the fresh LG
synthesis; the LG original stays closed until its own root release.
"""
(ROOT / review_path).write_text(review, encoding="utf-8", newline="\n")
write_table(LANE / (PREFIX + "defects.tsv"), defect_fields, defects)
write_table(ROOT / "CHECK_EVENTS.tsv", fields,
            events + [{k: r.get(k, "") for k in fields} for r in incoming])
with (ROOT / "PROGRESS_LEDGER.md").open("a", encoding="utf-8", newline="\n") as stream:
    stream.write(f"\n### Supporting comparison 02LV admitted — {NOW}\n\n")
    stream.write("Root whole reading and exact sign/geometry comparison are complete. "
                 "All theorem conclusions stand; the coupled D25 support/character "
                 "repair and the complete original source sphere are in the1365-line "
                 "receiver. See " + review_path + ". No required identity or unit "
                 "criterion is closed. LT and LV now supply the final fresh LG synthesis.\n")
print("ADMITTED supporting theorem maps:src:D.2.53 at", NOW)
print("RECEIVER", len(receiver.splitlines()), "lines", sha256(receiver.encode()).hexdigest())
print("REPLACEMENTS", len(replacements), "DEFECTS", len(defects), "EVENTS", len(incoming))
print("Canonical source unchanged; no required or publication-unit rows closed.")
