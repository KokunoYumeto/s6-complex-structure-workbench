from pathlib import Path
import datetime, hashlib, json
from S6_SERIES_PUBLISH_editing import Editor

r = Path(__file__).resolve().parents[1]
ed = Editor('I')
before = hashlib.sha256(ed.text.encode()).hexdigest()
p = r / 'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_Shioda1990_guarded.json'
guards = json.loads(p.read_text())['patches']
for g in guards:
    ed.replace(g['old'], g['new'], 'D18', g['reason'], ', '.join(g['statement_ids']))
for old, new, label in [
    ('The actual monodromy group is', 'The monodromy group is', 'series:I:C'),
    ('with the actual modular\nlifts', 'with the modular\nlifts', 'series:I:C'),
    ('comparing the actual cusp\ncollar', 'comparing the cusp\ncollar', 'series:I:B'),
    ('Actual modular lifts first reduce', 'The modular lifts first reduce', 'series:I:C'),
]:
    ed.replace(old, new, 'D08', 'Remove a process epithet; the same displayed group, lifts and collar maps are retained.', label)
old = 'finite etale descent gives the global'
if old in ed.text:
    ed.replace(old, "finite \\'etale descent gives the global", 'D23',
               'Restore the accent in the standard mathematical term.', 'series:I:D')
bibp = r / 'S6_SERIES_PUBLISH_references.bib'
bib = bibp.read_text()
bp = r / 'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_09.json'
for g in json.loads(bp.read_text())['changes']:
    assert bib.count(g['old']) == 1
    bib = bib.replace(g['old'], g['new'])
ed.save()
bibp.write_text(bib)
(r / 'records/S6_SERIES_PUBLISH_I_primary9_front_integration.json').write_text(json.dumps({
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'before_sha256': before,
    'after_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
    'primary_guards_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    'shared_bib_guards_sha256': hashlib.sha256(bp.read_bytes()).hexdigest(),
    'scope': 'Root read all five guards, the complete source/application receipt with its exact maps and hypotheses, and both versions of the full shared bibliography entry. Four first-part epithet removals leave the defined objects identical. No new mathematical check event.'
}, indent=2) + '\n')
