"""Merge the separately audited working-edition inventories, preserving print fields."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
target = ROOT / 'S6_09_PAPERS_inventory.csv'
with target.open() as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
index = {(r['source_run'], r['source_id']): r for r in rows}
def re_stability(sid):
    return sid.startswith('E.2.') and sid[4:].isdigit() and 4 <= int(sid[4:]) <= 24
inputs = [ROOT/'work/root/working_edition_inventory.csv',
          ROOT/'work/cdp_audit/working_edition_inventory.csv',
          ROOT/'work/maps_audit/working_results_inventory.csv',
          ROOT/'work/invariants_arithmetic/working_edition_inventory.csv']
for path in inputs:
    with path.open() as f:
        incoming = list(csv.DictReader(f))
    for x in incoming:
        key = (x['source_run'], x['source_id'])
        r = index.get(key)
        if r is None:
            r = {k:'' for k in fields}
            r['source_run'], r['source_id'] = key
            rows.append(r); index[key] = r
        for field in ['source_file','paper','kind','recorded_checks','check_outcome']:
            if x.get(field): r[field] = x[field]
        r['your_check'] = x.get('your_check',x.get('own_check','')) or r['your_check']
        r['statement_as_printed'] = r['statement_as_printed'] or x.get('source_statement',x.get('statement',x.get('statement_as_source','')))
        r['printed_label'] = r['printed_label'] or x.get('printed_label','')
        r['wording_vs_source'] = r['wording_vs_source'] or 'Source statement recorded; final wording comparison pending.'
        details = [x.get('notes','')]
        for k in ['taken_over_by','distinct_proof','overlap_status','source_line_start','start_line','source_sha256']:
            if x.get(k): details.append(k+'='+x[k])
        r['notes'] = '; '.join(z for z in details if z)
        for k in ['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere']:
            r[k] = r[k] or 'Credit comparison pending; no novelty claim made.'
for r in rows:
    run, sid = r['source_run'],r['source_id']
    if run=='S6_03_CDP' and sid=='D.1.14':
        r['paper']='I';r['notes']+='; Subject transfer: integral monodromy group, merged with FAM F.1.1.'
    if run=='S6_02_PUSH' and sid.startswith('C.'):
        r['paper']='III';r['notes']+='; Subject transfer: smooth parameter monodromy and homotopy spheres.'
    if run=='S6_02_PUSH' and sid.startswith('E.5.'):
        r['paper']='II';r['notes']+='; Subject transfer: two-parameter relatives.'
    if run=='S6_02_PUSH' and re_stability(sid):
        r['paper']='II';r['notes']+='; Subject transfer: global fibration stability and deformation chains.'
    if run=='S6_02_FAMILY' and sid in ['E.2.2','E.2.3']:
        r['paper']='III';r['notes']+='; Subject transfer: smooth parameter monodromy.'
    if run=='S6_04_MAPS_MANIFOLDS' and sid.startswith('A.3.'):
        r['paper']='I';r['notes']+='; Subject transfer: real forms of the family.'
    if run=='S6_04_MAPS_MANIFOLDS' and sid in ['A.1.1','A.1.2','A.1.3','A.2.1']:
        r['paper']='I';r['notes']+='; Subject transfer: complete circle quotient construction needed for real forms; homotopy calculations remain III.'
with target.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('Inventory rows:',len(rows))
print('Working-edition rows:',len(rows)-745)
