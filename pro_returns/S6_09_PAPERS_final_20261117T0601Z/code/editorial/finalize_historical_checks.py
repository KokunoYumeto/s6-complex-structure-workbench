"""Preserve historical checks at their expressly recorded scope.

A status intake, a proof comparison, and a full mathematical reading are
different events. Neither title matching nor the producing run's badge is
used to infer a proof check. Run after merging the current agent inventories.
"""
from pathlib import Path
import csv,json,re

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables'; SRC=ROOT/'sources'
path=OUT/'S6_09_PAPERS_inventory.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)

events=[]
def event(eid,run,ids,reader,effort,date,kind,scope,locator):
    events.append(dict(event_id=eid,source_run=run,source_ids=ids,reader=reader,
                       effort=effort,date=date,type=kind,scope=scope,locator=locator))
fable='Claude Fable 5.2 (Anthropic)'
opus='Claude Opus 5.5 (Anthropic)'
event('push-intake-full','S6_02_PUSH',
      ['A.3.1','A.3.2','B.4.4','B.4.27','B.4.30','B.4.31','B.4.32','B.4.33',
       'C.3.21','C.3.22','C.3.23','C.3.24','C.3.27','D.1.1','D.1.2','E.2.21','E.2.22','E.2.24'],
      fable,'high','16 November 2026, 12:57 UTC','F',
      'Entire named proof read. The reviewer did not open external PDFs or rerun these programs; the reading does not certify an unread dependency.',
      'reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md, opening scope lines 7–25 and section 1')
event('push-intake-partial','S6_02_PUSH',['D.1.3','E.2.7'],fable,'high',
      '16 November 2026, 12:57 UTC','partial F',
      'Only the opening of D.1.3 and first half of E.2.7 are expressly listed as read in the opening scope. The later summary is not used to enlarge that scope.',
      'reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md, opening scope and section 1')
event('push-intake-statements','S6_02_PUSH',['B.1.1','B.1.2','B.4.19'],fable,'high',
      '16 November 2026, 12:57 UTC','R',
      'Statements read; no whole-proof check inferred.',
      'reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md, opening scope')
event('push-expert-full','S6_02_PUSH',['B.4.24','B.4.26','B.4.30','B.4.33'],fable,'max',
      '16 November 2026, 13:15 UTC','F, scoped D',
      'Full proofs read. Deck differences, ghost argument, norm/finiteness argument and saturation argument rederived by hand. The actual origins and their affine comparison were taken from the producing run; that remaining issue is repaired in the current writing.',
      'reviews/S6_FINAL_INTAKE_20261116/EXPERT_POSITION.md, opening scope and section (a)')
event('push-expert-orbit','S6_02_PUSH',['B.4.31'],fable,'max',
      '16 November 2026, 13:15 UTC','D (specified argument)',
      'The SL2(Z) finite-orbit argument rederived; not a claim of a separate full reading of every surrounding dependency.',
      'reviews/S6_ROUTES_FABLE_MAX/NOTES.md, third step; EXPERT_POSITION.md section (a)')
event('push-expert-log-torsor','S6_02_PUSH',['B.4.27'],fable,'max',
      '16 November 2026, 13:15 UTC','partial D',
      'H1(S,A_S)=0 rederived in outline, as explicitly qualified by the reviewer.',
      'reviews/S6_ROUTES_FABLE_MAX/NOTES.md, third step')
event('push-cycle-reading','S6_02_PUSH',['B.1.1','B.1.2','B.4.18'],opus,'max',
      '16 November 2026, approximately 12:10 UTC','F; scoped algebraic check',
      'Named source intervals read, corrected cusp-overlap file read in full; component rotations and Albanese identifications checked. Section 38 preserves corrections to earlier interpretations. The auxiliary twelve-cycle program is recorded by the reviewer; it is not represented as a new rerun in this writing.',
      'notes/CLAUDE_NOTES_S6_20261115-16.md, sections 34 and 38')

# The previous paper comparison is retained as a comparison, not promoted to F.
diff=json.loads((SRC/'reviews/S6_PAPER_DRAFT_CHECK_20261116/out/diff_rows.json').read_text())
proofs={x['label']:x for x in json.loads((SRC/'reviews/S6_PAPER_DRAFT_CHECK_20261116/out/proofs.json').read_text())}
run_map={'FAM':'S6_02_FAMILY','PUSH':'S6_02_PUSH','INV':'S6_01_INVARIANTS',
         'CDP':'S6_03_CDP','MAPS':'S6_04_MAPS_MANIFOLDS','ARI':'S6_05_ARITHMETIC'}
for d in diff:
    if d.get('run') not in run_map: continue
    proof=proofs.get(d['label'])
    scope='The previous printed statement was compared with its source.'
    if proof:
        scope+=' Its retained proof was also compared with the source (token comparison ratio '+str(proof.get('ratio'))+').'
    scope+=' This is a source-to-print comparison, not an additional independent mathematical proof verification.'
    event('previous-draft-'+d['label'],run_map[d['run']],[d['sid']],fable,'high',
          '16 November 2026','comparison',scope,
          'reviews/S6_PAPER_DRAFT_CHECK_20261116/DRAFT_CHECK.md sections 2–4; out/diff_rows.json label '+d['label']+
          ('; out/proofs.json same label' if proof else ''))

# Expand the fully specified historical events supplied by the topology reader.
maps_events=json.loads((OUT/'work/maps_audit/check_events.json').read_text())
for e in maps_events:
    if not e.get('event_id','').startswith('prior-'):continue
    for r in rows:
        rec=r.get('recorded_checks','')
        if e['event_id'] in rec:
            full=(e['reader']+', effort '+e['effort']+', '+e['date']+
                  ': '+e['scope']+' ['+e['locator']+']')
            if full not in rec:r['recorded_checks']=rec+' | '+full

for r in rows:
    k=(r['source_run'],r['source_id']); old=r['recorded_checks']
    matched=[e for e in events if e['source_run']==k[0] and k[1] in e['source_ids']]
    parts=[]
    if 'Review mapping in progress' in old or (not old and k[0] in run_map.values()):
        parts.append('Recorded result-register intake: '+fable+', effort high, 16 November 2026, 12:57 UTC; reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md, opening scope. Every status was examined; text was read for non-proved and main-question rows. This register intake alone is not a whole-proof check. The expressly identified proof readings and comparisons follow where applicable.')
    elif old:parts.append(old)
    if not old and k[0]=='WORKING_CDP':
        parts.append('Working-edition self-checks are provenance. The current independent complete proof reading is recorded in your_check; no historical whole-proof reading is inferred from the working-edition status badge.')
    for e in matched:
        value=e['reader']+', effort '+e['effort']+', '+e['date']+'; '+e['type']+': '+e['scope']+' ['+e['locator']+']'
        if value not in old:parts.append(value)
    if parts:r['recorded_checks']=' | '.join(parts)

with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(OUT/'records/historical_check_concordance.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print('Recorded historical events:',len(events),'inventory rows:',len(rows))
