"""Authorize only 02LG after the complete frozen fresh synthesis was read."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT / "agents/continuation8_iii_lg_fresh/S6_SERIES_PUBLISH_III_02LG_fresh_synthesis.md"
LANE = ROOT / "agents/continuation8_iii_lg_receiving"
LANE.mkdir(parents=True, exist_ok=True)
HASH = "2ec88ef8479dc870b20515290225c1e45eb26ac31ddecb7eda6aa68cb7912059"
FROZEN = "2026-11-25T16:06:08+00:00"
assert sha256(FRESH.read_bytes()).hexdigest() == HASH
assert len(FRESH.read_text().splitlines()) == 784
assert (ROOT / "agents/continuation8_iii_lv/S6_SERIES_PUBLISH_III_02LV_root_admission_review.md").is_file()
NOW = datetime.now(timezone.utc).isoformat()
REVIEW = LANE / "S6_SERIES_PUBLISH_III_02LG_root_fresh_review.md"
REVIEW.write_text(f"""# 02LG — complete fresh synthesis read before original release

Root review completed {NOW}. Fresh freeze {FROZEN}; SHA256 {HASH}.

Root read the entire staged synthesis Sections1–8, then all new
Section9 and final open scope, then every final admission/reference
edit. These readings cover all784 frozen lines. Root also wholly
read the274-line catalogue source and all922 actual output lines,
the new105-line coefficient source and all195 actual output lines,
its derivation and full input/readback note. The enumerations and
unit/CRT maps are computationally checked; the underlying geometric
invariant formulas retain their admitted predecessor scopes. No
new whole proof or primary-page reading of every predecessor is
claimed. Root completed and admitted both LT and LV support comparisons.

The finite row definitions, inclusion of459 original-star presentations
in495 presentations with the permitted finite choices,162 minimal
patterns,24 complete coefficient orbits and59 sphere patterns on50
rows were checked with the explicit row/site maps. The cyclic unit
maps and coprime H2/H6 maps include their inverses and mixed-term
vanishing proofs. The corrected residual orders4,8,20 are explicit.
The actual arbitrary-cusp, weighted, primitive-long-star, corrected-
vertical and invariant-Chern cap maps retain their proved scope.

The weighted OS45 input is the fully admitted1365-line LV receiver,
with the signed positive-Thom/support map, whole boundary class,
original selected source sphere, primitive detector, reference parity1
and complete critical linking number−1. Its full invariant package
is included. The remaining open families are stated precisely.

The fresh target synthesis is complete at these admitted-input scopes.
Only now is the original02LG unit and its historical target evidence
released for comparison. This authorization grants no required-check
completion or publication-unit credit. The canonical manuscript is
unchanged. The final comparison must settle every discrepancy with
the original text and retain all permanent identities.
""", encoding="utf-8", newline="\n")

# Original target access occurs only after the fresh review above is written.
source = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text()
source_hash = sha256(source.encode()).hexdigest()
assert source_hash == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
anchor = source.index(r"\hypertarget{tag-02LG}")
matches = list(re.finditer(r"\\begin\{(problem|question|theorem|proposition|lemma|remark)\}", source[:anchor]))
assert matches
start = matches[-1].start()
environment = matches[-1][1]
statement_end = source.index(r"\end{" + environment + "}", anchor) + len(r"\end{" + environment + "}")
stops = [source.find(token, statement_end) for token in
         ("\n\\section", r"\begin{thebibliography}", r"\end{document}")]
end = min(i for i in stops if i >= 0)
original = source[start:end].rstrip() + "\n"
assert r"\label{maps:src:D.2.4}" in original
released = LANE / "S6_SERIES_PUBLISH_III_02LG_released_original.tex"
released.write_text(original, encoding="utf-8", newline="\n")
progress = ROOT / "S6_SERIES_PUBLISH_required_progress_III.tsv"
with progress.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields, rows = reader.fieldnames, list(reader)
row = next(r for r in rows if r["tag"] == "02LG")
assert row["status"] == "open" and row["proof_status"] == "embargoed"
row.update(assigned_checker="/root/lg_fresh", packet_status="released_full_comparison_in_progress",
           source_ownership_status="verified", proof_status="released_after_derivation",
           derivation_path=str(FRESH.relative_to(ROOT)), derivation_sha256=HASH,
           derivation_completed_utc=FROZEN, root_release_authorization=str(REVIEW.relative_to(ROOT)),
           proof_released_utc=NOW, released_source_sha256=source_hash,
           released_proof_sha256=sha256(original.encode()).hexdigest(), unresolved_inputs="",
           checker_exposure_note="Whole frozen fresh synthesis and its actual computational scopes read before individual original release; support LT/LV fully admitted. Historical target comparison begins only after this timestamp.")
row["notes"] += " Continuation8: complete784-line synthesis frozen and root-read; original/history individually released for comparison. No completion credit yet."
buffer = io.StringIO(newline="")
writer = csv.DictWriter(buffer, fields, delimiter="\t", lineterminator="\n")
writer.writeheader(); writer.writerows(rows)
progress.write_text(buffer.getvalue(), encoding="utf-8", newline="\n")
with (ROOT / "PROGRESS_LEDGER.md").open("a", encoding="utf-8", newline="\n") as stream:
    stream.write(f"\n### 02LG original released after complete fresh review — {NOW}\n\n")
    stream.write(f"The784-line synthesis froze {FROZEN}, SHA256 {HASH}, after LT/LV admission. "
                 "Root whole reading is complete; the original unit and its historical target evidence "
                 "are individually released for comparison. The required row remains open and the "
                 "canonical source remains unchanged. See " + str(REVIEW.relative_to(ROOT)) + ".\n")
print("RELEASED 02LG at", NOW)
print("FRESH", len(FRESH.read_text().splitlines()), HASH)
print("ORIGINAL", environment, "source lines", source.count("\n", 0, start)+1,
      source.count("\n", 0, end)+1, "released lines", len(original.splitlines()))
print("ORIGINAL SHA256", sha256(original.encode()).hexdigest())
print("Required check remains open; canonical source unchanged.")
