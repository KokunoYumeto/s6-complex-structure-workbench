"""Render the actual complete target-group witness list as a compact TeX table."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'code/part3_root/scalar_all_fans.json').read_text())
w=data['original_shorter_all_28_witnesses']
assert [x['residue'] for x in w]==list(range(28))
lines=[r'\begin{center}\small',r'\begin{tabular}{clr@{\qquad}clr}',
       r'\toprule',r'Class & Basis & \(S\) & Class & Basis & \(S\)\\',r'\midrule']
def cells(item):
    a,b,c,d=item['basis']
    assert a*d-b*c==1
    assert item['integer_path_sum']%28==item['residue']
    return str(item['residue'])+r' & \(('+f'{a},{b};{c},{d}'+r')\) & '+str(item['integer_path_sum'])
for i in range(14): lines.append(cells(w[i])+' & '+cells(w[i+14])+r'\\')
lines.extend([r'\bottomrule',r'\end{tabular}',r'\end{center}'])
(root/'notes/part3_scalar_all_fan_witness_table.tex').write_text('\n'.join(lines)+'\n')
print('Wrote all28 verified basis witnesses.')
