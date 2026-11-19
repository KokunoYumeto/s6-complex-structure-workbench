"""Export the complete exact OS49 target-group witnesses to the proof table."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'code/part3_root/os49_all_fans.json').read_text())
w=data['k1_shorter_witnesses']
assert [x['physical_class_mod28'] for x in w]==list(range(28))
lines=[r'\begin{center}\small',r'\begin{tabular}{clr@{\qquad}clr}',
       r'\toprule',r'Class & Basis & \(S\) & Class & Basis & \(S\)\\',r'\midrule']
def cells(item):
    a,b,c,d=item['canonical_basis']
    assert a*d-b*c==1
    residue=item['physical_class_mod28']
    assert item['integer_path_sum']%28==residue
    return str(residue)+r' & \(('+f'{a},{b};{c},{d}'+r')\) & '+str(item['integer_path_sum'])
for i in range(14):lines.append(cells(w[i])+' & '+cells(w[i+14])+r'\\')
lines.extend([r'\bottomrule',r'\end{tabular}',r'\end{center}'])
(root/'notes/part3_os49_all_fan_witness_table.tex').write_text('\n'.join(lines)+'\n')
print('Exported all28 OS49 k1 shorter fan witnesses with exact integer path sums.')
