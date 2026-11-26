#!/usr/bin/env python3
"""Record the completed exposed QC-to-037M application comparison."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'agents/continuation8_iii_later'
carrier = ROOT / 'agents/continuation8_iii_integration/units/later/further_cusp_carriers.tex'
owner = ROOT / 'agents/continuation8_iii_integration/units/root/carrier_wedge_recognition.tex'
assert hashlib.sha256(carrier.read_bytes()).hexdigest() == '8aeca778ffbbc1e23f0592d51c80ceeb33fef5409253cff7551e4015462468be'
assert hashlib.sha256(owner.read_bytes()).hexdigest() == 'd807087327c2e83eb74f260df4d0aa7ca64039058dcb4c178149d3ef73495ce9'
defects = out / 'S6_SERIES_PUBLISH_III_carrier_wedge_followup_defects.tsv'
with defects.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 1
rows[0]['review_status'] = 'whole earlier QC proof, 199-line comparison, 84-line root rewrite, and complete before/after 037M statement/proof read; exact old/new fields read; exposed use only; actual earlier placement remains root-owned'
with defects.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

events_path = out / 'S6_SERIES_PUBLISH_III_carrier_wedge_followup_CHECK_EVENTS.tsv'
event_fields = ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
stamp = datetime.now(timezone.utc).isoformat()
events = []
for path, tag, sid, detail in [
    (owner, '02QC', 'mapsIII:carrier-three-complex-wedge',
     'Complete earlier proof and 199-line admitted comparison read, followed by the full 84-line root publication proof at hash d807087327c2e83eb74f260df4d0aa7ca64039058dcb4c178149d3ef73495ce9. Exact chosen-generator, mapping-cylinder, retraction, basepoint and inverse-homotopy maps support the 037M application. Root owns this unit and its publication admission.'),
    (carrier, '037M', 'wb:cusp-cone-target-homotopy-types',
     'Complete before/after theorem and proof read. Only the repeated relative-Hurewicz/Whitehead paragraph is replaced: C is the identical based coned target, u is the primitive 12rho0+h boundary kernel and v the oriented boundary torus. Exact G and L maps/inverses retain all signed generators, 49/16 smash summands, ordinary invariants and zero/nonzero surjective representatives. The two raw geometric classes remain unassigned.'),
]:
    text = path.read_text()
    line = text[:text.index(r'\label{' + sid + '}')].count('\n') + 1
    events.append(dict(statement_id=sid, date=stamp[:10],
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
        type='used and rechecked in this run',
        outcome=detail + ' Exposed reading only; no independent derivation, historical-output credit, required-row closure or global placement/render credit.',
        event_id='publish:c8:III:' + tag + ':carrier-wedge-application-recheck',
        phase='continuation8-later-publication', source_file=str(path.relative_to(ROOT)),
        source_row=str(line), source_event_type='used and rechecked in this run',
        evidence_group='publish:c8:III:later-unit-editing',
        publish_input_file=str(events_path.relative_to(ROOT)), publish_input_row=str(len(events) + 2),
        date_utc=stamp, where='agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_carrier_wedge_followup_review.md'))
with events_path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)
for path in (defects, events_path):
    assert b'\r' not in path.read_bytes()
print('Completed readings', len(events), 'exact edit rows', len(rows), 'at', stamp)
text = carrier.read_text()
start = text.index(r'\begin{theorem}[Homotopy types of the conical targets]')
end = text.index(r'\end{proof}', start) + len(r'\end{proof}')
print('Complete revised 037M block', text[:start].count('\n') + 1, 'through', text[:end].count('\n') + 1, 'lines', len(text[start:end].splitlines()))
print('No source change or shared-ledger/criterion mutation; both local tables use LF.')
