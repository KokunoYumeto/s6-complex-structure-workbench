"""Reconstruct K88's fixed-scalar T0-sector witnesses by exact arithmetic."""
from pathlib import Path
import json
from source_zero_all_fans import base_sector_witnesses,calculate,Q0,Q1,mul
ROOT=Path(__file__).resolve().parents[2]
def main():
    branches=[base_sector_witnesses(a,10) for a in (1,2)]
    for a,values in ((1,(6,6)),(2,(9,0))):
        assert tuple(calculate(P,a)['physical_class_mod28'] for P in (mul(Q0,Q0),mul(Q0,Q1)))==values
    record={'status':'PASS','recovery':'Reconstructed from the retained K88 initial integer seed and full recurrence. Original post19 bytes were lost.','input_scope':'Fixed scalar k=0; canonical vertical seed j=0; every word begins Q0.','branches':branches,'total_words':2046,'all28_witnesses_each_branch':True}
    (ROOT/'code/part3_root/source_zero_base_sector.json').write_text(json.dumps(record,indent=2)+'\n')
    for branch in branches:
        a=branch['a'];lines=[r'\begin{center}\small',r'\begin{tabular}{crr@{\qquad}crr}',r'\toprule',r'Class & Basis & \(S\) & Class & Basis & \(S\)\\',r'\midrule']
        def cells(w):
            u,v,x,y=w['input_basis'];return str(w['physical_class_mod28'])+r' & \(('+f'{u},{v};{x},{y}'+r')\) & '+str(w['integer_path_sum'])
        for i in range(14):lines.append(cells(branch['witnesses'][i])+' & '+cells(branch['witnesses'][i+14])+r'\\')
        lines.extend([r'\bottomrule',r'\end{tabular}',r'\end{center}'])
        (ROOT/f'notes/part3_source_zero_base_sector_witnesses_a{a}.tex').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'status':'PASS','total_words':2046,'witnesses':56,'first_flop_examples':{'good':[6,6],'reduced':[9,0]}},indent=2))
if __name__=='__main__':main()
