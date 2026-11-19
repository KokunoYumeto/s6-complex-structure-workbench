#!/usr/bin/env python3
"""Register the specifically reviewed A.2.1/A.1.2 receipts and UN13 steps.

Backups and exact before/after hashes make the operation reversible;
--revert refuses to overwrite any file changed since this operation.
No paper mathematical/authoring source is modified.
"""
import argparse,csv,hashlib,io,json
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
AN=ROOT/'analysis/continuation_II_ledger'
BACK=AN/'post_checkpoint12_registration_before'
RECEIPT=AN/'post_checkpoint12_registration_receipt.json'
FILES=['records/continuation_II_ledger_events.tsv',
       'records/continuation_VI_ledger_events.tsv',
       'analysis/continuation_II_ledger/completed_row_gates.json',
       'analysis/continuation_II_ledger/printed_scope_overrides.json',
       'S6_10_PAPERS_inventory.csv']
sha=lambda b:hashlib.sha256(b).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--revert',action='store_true');args=ap.parse_args()
if args.revert:
    rec=json.loads(RECEIPT.read_text())
    for name,d in rec['files'].items():
        if sha((ROOT/name).read_bytes())!=d['after_sha256']:
            raise SystemExit('Refusing to overwrite later change: '+name)
    for name,d in rec['files'].items():(ROOT/name).write_bytes((ROOT/d['backup']).read_bytes())
    print('Reverted exact registered files; registration receipt retained.')
    raise SystemExit
if RECEIPT.exists():
    print('Already registered; no mutation.');raise SystemExit
pending=json.loads((AN/'pending_post_checkpoint12_A2_A1_updates.json').read_text())
before={name:(ROOT/name).read_bytes() for name in FILES}
BACK.mkdir(parents=True,exist_ok=True)
for name,data in before.items():
    p=BACK/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation'

def append_tsv(name,newrows):
    p=ROOT/name
    with p.open() as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
    for row in newrows:
        if row not in rows:rows.append(row)
    with p.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)

iirows=[{'statement_id':e['statement_id'],'date':e['date'][:10],
         'who':e['checker'],'type':e['type'],'outcome':e['outcome']}
        for e in pending['events']]
append_tsv(FILES[0],iirows)
un_scope=('UN13 isolated complete prereading residuals frozen08:14:42 UTC: actual two-/three-dimensional blowup-quotient charts and O(-2) normal maps; nowhere-zero two-form including factor1/2; coherent/rational averaging trace and Euler24; ambient pair/Gysin splitting with sections -j_*(1)/2 and -j_*(h)/2; full support pair/Gysin splitting with -1 normal, all four quartic boundary intersections; exact multiplicity-one fibre equations; ruled-domination contradiction through resolved pullback. Target Steps2/4/5/7/9/10/13 compared only in the explicitly delineated residual scope; mixed-step extra routes are exposure only. No whole-row re-proof claim. ')
append_tsv(FILES[1],[
 {'statement_id':'cdp:st:C.2.UN.13','date':'2026-11-19','who':who,'type':'targeted proof check','outcome':un_scope+'Evidence analysis/continuation_VI_ledger/UN13_residual_before_read_receipt.json, UN13_residual_comparison.md and comparison_receipt.json. No mathematical source replacement needed.'},
 {'statement_id':'cdp:st:C.2.UN.13','date':'2026-11-19','who':who,'type':'computation or formal certificate','outcome':'New independent UN13_residual_fresh.py passed67 exact checks before target exposure: form Jacobians/overlap sign, Veronese minors and quotient-chart cocycles, trace/exterior dimensions, Euler arithmetic, -2/-1 Gysin sections, support additions and full fibre equations at all four quartic boundary points. The universal relative-pair proof is separately written, not inferred from finite matrices. Evidence code/continuation_VI_ledger/UN13_residual_fresh.py and analysis/continuation_VI_ledger/UN13_residual_fresh.output.json; freeze08:14:42 receipt.'}
])
p=ROOT/FILES[2];g=json.loads(p.read_text())
for label,fields in pending['gates'].items():
    if label in g and g[label]!=fields:raise RuntimeError('Conflicting owner gate '+label)
    g[label]=fields
p.write_text(json.dumps(g,indent=2)+'\n')
p=ROOT/FILES[3];sc=json.loads(p.read_text())
for label,scope in pending['printed_scope_overrides'].items():
    sc[label]={'scope_tex':scope,'basis':'analysis/continuation_II_ledger/A2_1_A1_2_before_read_receipt.json; A2_1_A1_2_comparison.md; exact source_scans receipts'}
p.write_text(json.dumps(sc,indent=2)+'\n')
p=ROOT/FILES[4]
with p.open() as f:reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['label'] in pending['gates']:
        notes=json.loads(row['notes'])
        notes.setdefault('continuation_renewed_source_comparisons',[]).append({
            'date':'2026-11-19','reviewer':who,
            'scope':pending['gates'][row['label']]['renewed_main_result_credit_check'],
            'receipt':'analysis/continuation_II_ledger/A2_1_A1_2_comparison.md',
            'prior_credited_to_preserved_verbatim':row['credited_to']})
        row['notes']=json.dumps(notes,ensure_ascii=False)
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
receipt={'registered_utc':datetime.now(timezone.utc).isoformat(),
         'authorization':'Root observed checkpoint12 save08:15:53 UTC and released freeze; explicitly requested staged II merge and UN13 comparison.',
         'registered_II_rows':list(pending['gates']),'new_II_events':6,
         'new_UN13_targeted_events':2,'paper_sources_modified':False,
         'rich_credited_to_modified':False,
         'files':{name:{'before_sha256':sha(data),'after_sha256':sha((ROOT/name).read_bytes()),
                        'backup':str((BACK/name).relative_to(ROOT))} for name,data in before.items()}}
RECEIPT.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'registered_utc':receipt['registered_utc'],'II_rows':receipt['registered_II_rows'],
                  'new_events':8,'receipt':str(RECEIPT)},indent=2))
