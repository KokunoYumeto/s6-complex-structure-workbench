#!/usr/bin/env python3
"""Export audited original-loop simultaneous descent as separate P3K.33."""
from pathlib import Path
from datetime import datetime, timezone
import json, re

ROOT=Path(__file__).resolve().parents[2]
rel='notes/part3_original_cox_descent.md'
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened own '+rel+
              ' and code/part3_fourfold/results_mapping.json. Reason: promote fully audited P3K.33. '
              'Material: exact integral endpoint, both finite-cap arrows, signed original-family dictionary, '
              'simultaneous Cox product and single-loop fan formula. Root and checks audits passed.\n')
source=(ROOT/rel).read_text()
statement=source.split('## Statement and parameter scope',1)[1].split('## 1.',1)[0].strip()
body='## 1.'+source.split('## 1.',1)[1]

def tex(value):
    value=value.replace(r'\tag{OD.',r'\tag{P3K.33.').replace('(OD.','(P3K.33.')
    value=re.sub(r'^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'.}\enspace',value,flags=re.M)
    value=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',value)
    return value.strip()+'\n'

output=(r'\begin{statement}{P3K.33}{Proved}'+'\n'+tex(statement)+
        r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex(body)+r'\end{proof}'+'\n')
assert '#' not in output and '`' not in output
(ROOT/'notes/part3_original_cox_descent.tex').write_text(output)
mapping=json.loads((ROOT/'code/part3_fourfold/results_mapping.json').read_text())
mapping['results']=[x for x in mapping['results'] if x.get('id')!='P3K.33']
mapping['results'].append(dict(
    id='P3K.33',status='Proved',item_of_prompt='3.1, 3.3, 3.4',
    statement='Both signed original/higher sphere data have a literal simultaneous Cox product for their single positive w_h loop; initial pair (-KL,-4KL), and every fan has class KL(S-1)(S-3)/8 modulo 28.',
    proof_file=rel,latex_file='notes/part3_original_cox_descent.tex',
    code='code/part3_fourfold/original_cox_descent_universal.py',
    output='code/part3_fourfold/original_cox_descent_universal.json',
    original_pair=[-1,-4],higher_pair=['-KL','-4KL'],sphere_signs=[-1,1],
    original_fan_classes=[0,1,3,6,7,8,10,13,14,15,17,20,21,22,24,27],
    explicit_nonzero_fan=dict(v=[3,1],w=[-1,0],physical_delta=[0,1],coordinates=[1,3],S=7,oriented_class=3),
    audit='Root full proof and independent checks passed. No homotopy-sphere class is divided.'))
(ROOT/'code/part3_fourfold/results_mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported P3K.33 with complete proof, both sphere signs, exact endpoint and explicit class-3 fan.')


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3_fourfold/results_mapping.json'], ['notes/part3_original_cox_descent.tex'], origin='code/part3_fourfold/export_original_cox_descent.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
