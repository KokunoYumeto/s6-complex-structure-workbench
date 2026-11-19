#!/usr/bin/env python3
"""Preserve prototype labels, then record the proved actual OS45 family."""
from pathlib import Path
from datetime import datetime, timezone
import json
import shutil

directory=Path(__file__).resolve().parent
root=directory.parents[1]
history=directory/'history';history.mkdir(exist_ok=True)
for suffix in ('.py','.json','.out'):
    source=directory/('os45_tuple'+suffix)
    target=history/('os45_tuple_initial_candidate'+suffix)
    if not target.exists():shutil.copy2(source,target)
script=directory/'os45_tuple.py'
text=script.read_text()
text=text.replace('Exact I8+4I1 source and weighted candidate tuple; geometric scope in notes.',
                  'Exact actual I8+4I1 source and weighted sphere tuple, proved in P3K.10.')
text=text.replace('Exact candidate lattice and source arithmetic; source marking and geometric local-comparison proof are separate obligations.',
                  'Proved actual source marking, holomorphic sphere family and signed return in notes/part3_os45.md P3K.10.')
text=text.replace("'computed_candidate_homology'","'integral_homology'")
text=text.replace("'page_candidate'","'actual_page'")
text=text.replace("'predicted_index_before_actual_trace_check'","'actual_positive_return_index'")
text=text.replace("print('Candidate homology'","print('Integral homology'")
text=text.replace('Geometric marking remains to be independently identified; no sphere conclusion is inferred by this script alone.',
                  'Geometric marking, every local comparison, actual positive return -3 and class25 are proved in P3K.10.')
script.write_text(text)
path=directory/'results_mapping.json';data=json.loads(path.read_text())
data['results']=[row for row in data['results'] if row['id']!='P3K.10']
data['results'].append({
 'id':'P3K.10','status':'Proved','item_of_prompt':'3.4',
 'statement':'The explicit I8+4I1 source with M=8G-O, Q=G and one ordinary multiplicity-one gamma log cap gives a holomorphic S6 family with positive return A=-3 and oriented class25; its positive finite parameter covers realize all of Theta7.',
 'proof_file':'notes/part3_os45.md','latex_file':'notes/part3_fourfold.tex',
 'source_entry':'torsion-free OS45, I8+4I1',
 'smooth_log_site':'t=0, multiplicity1, integral gamma clutch1',
 'parameter':'lambda, no parameter cover for one gamma turn',
 'positive_return_index':-3,'Eells_Kuiper':'-3/28','Theta7_class':25,
 'all_parameter_cover_classes':[(-3*n)%28 for n in range(1,29)],
 'homology':['Z',0,0,0,0,0,'Z'],'fundamental_group':1,
 'own_value':'All 28 oriented homotopy-sphere monodromy classes occur among holomorphic families of complex structures on S6.',
 'codes':['code/part3_fourfold/os45_tuple.py','code/part3_fourfold/os45_origins.py','code/part3_fourfold/rank_two_cusp.py'],
 'historical_prototype':'code/part3_fourfold/history/os45_tuple_initial_candidate.*; the candidate label predates the source-marking and geometric comparison proofs and is superseded by P3K.10.',
 'classification_scope':'This constructs an additional literal Remark8.5 family. It does not by itself exhaust arbitrary vertical line modifications or all logarithmic sites.'
})
path.write_text(json.dumps(data,indent=2)+'\n')
log=root/'records/literature_fourfold.md'
with log.open('a') as handle:
    handle.write('\n## '+datetime.now(timezone.utc).isoformat()+' — OS45 proof and local cusp certificate\n\n')
    handle.write('Read the final cusp paragraph of Engel Lemma7.4 in the supplied S6.tex. It states integral specialization onto all invariants; the owned rank_two_cusp.py now independently reproduces the full local chain and collapse calculation using the actual topological model of P1.11. Read current-team P3F.22–24 sign and mapping-torus comparisons to apply the proved actual one-gamma positive loop. The new source marking is proved from its explicit I9 degeneration and the unique modular covering graph; the full twelve-coset table is generated exactly. Initial candidate code and output labels are retained under code/part3_fourfold/history and are explicitly superseded by P3K.10.\n')
print('Recorded the proved OS45 generator family and all 28 parameter-cover classes.')
