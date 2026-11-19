"""Assemble the corrected scalar claims, narrow repair and shear theorem."""
from datetime import datetime,timezone
from pathlib import Path
import ast,json
root=Path(__file__).resolve().parents[1]
parts=['scalar_outer_clutch_obstruction','scalar_native_comparison','source_cusp_shear_pontryagin']
for name in parts:
    assert (root/('notes/part3_'+name+'.tex')).is_file(),name
for file in ['records/root_audit_scalar_consistency.json',
             'records/root_audit_source_cusp_shear_pontryagin.json',
             'records/blind_audit_source_cusp_shear_pontryagin.json']:
    d=json.loads((root/file).read_text());assert d['status']=='PASS',file
p=root/'notes/part3.tex';text=p.read_text()
for name in parts:
    include='\\input{notes/part3_'+name+'.tex}'
    assert include not in text,include
    text+='\n'+include+'\n'
p.write_text(text)
p=root/'code/update_report.py';text=p.read_text()
text=text.replace('P3K.40–P3K.62; reopened','P3K.40–P3K.63; reopened')
old='The source-zero global central attachment, full sheared fixed-star characteristics, corrected scalar-fan returns,'
new='P3K.63 completes the actual sheared quotient, Euler-line and relative Pontryagin comparison and proves ell(T_n)=0 for every signed n. With the actual integer index A_n it gives native fixed pair(0,-6A_n), V00=6A_n-6 and delta0=-6A_n-6; the existing central residue fixes V00=-18n(n-1) and delta0=-12+18n(n-1) modulo168, without selecting an integer lift. The source-zero global central attachment, the remaining integer fixed-star index, corrected scalar-fan returns,'
assert text.count(old)==2,text.count(old)
text=text.replace(old,new)
ast.parse(text);p.write_text(text)
p=root/'records/progress_check_15_hours.json';d=json.loads(p.read_text())
d['main_question_progress'][-1]='K63 completes the actual source-cusp shear quotient, oriented endpoint dictionary, typed Cartier map, retained Euler-line crossing and nilpotent boundary derivative. It proves ell(T_n)=0 and the exact fixed-star consequences modulo168, with no unproved integer lift.'
d['next_main_steps'][2]='Compute the remaining integer fixed-star index and carry the corrected scalar native products through further fan changes.'
d['audit_updated_utc']=datetime.now(timezone.utc).isoformat()
p.write_text(json.dumps(d,indent=2)+'\n')
print('Included K61--63 with explicit scalar correction and completed ell comparison; build51 ready.')
