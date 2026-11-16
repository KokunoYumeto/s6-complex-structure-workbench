"""Register the independently audited canonical algorithm and56-class stratum."""
from pathlib import Path
import csv,json,hashlib
root=Path(__file__).resolve().parents[1]
names=('tuple_classification','involution_classes')
for name in names:
    p=root/'code'/f'fourfolds_{name}_proof.tex'
    s=p.read_text()
    if name=='tuple_classification':s=s.replace('F.CA','F.CN')
    p.write_text(s)
    (root/'sections'/f'fourfolds_{name}.tex').write_text(s)
p=root/'sections/fourfolds.tex';s=p.read_text()
anchor=r'\input{sections/fourfolds_integral_conjugacy}'
for name in names:
    marker='\\input{sections/fourfolds_'+name+'}'
    if marker not in s:s=s.replace(anchor,anchor+'\n'+marker)
    anchor=marker
p.write_text(s)
p=root/'records/fourfolds_root_results.csv'
with p.open(newline='') as f:
    rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
rows=[r for r in rows if r['id'] not in ('F.2.37','F.2.38')]
new=[
 ('F.2.37','Every admissible marked F.2 linear tuple has a computable canonical integral representative and checked conjugator. A proved finite input-dependent height bound makes the fallback complete, while an unbounded word trace rules out any fixed global entry box.','sections/fourfolds_tuple_classification.tex','F.2.36;F.2.38;F.2.16','Independent fourfolds proof/code audit PASS. Public normalizer executed on all56 conjugated involution inputs. The general noninvolution height-box fallback is explicitly not claimed exhaustively executed. Returned changes transport all numerators, clutch and cusp marking.'),
 ('F.2.38','The complete ordered linear-involution stratum consists of exactly56 simultaneous integral classes. An explicit Smith, glue and finite-field normalizer returns an exact conjugator for any input; every class admits free actual-order4 affine lifts, and none can give a simply connected filling at any free affine orders.','sections/fourfolds_involution_classes.tex','F.2.31; integral involution glue classification; exact norm quotient; finite-field similarity','Theory independently audited by fourfolds agent, full proof read by root, and complete catalogue independently rerun. All56 classes,112 exact conjugators and112 free affine lifts passed; complete pi1 and H1 computed for the stated order4 choices.')]
for id,claim,where,dep,note in new:
    rows.append(dict(id=id,statement=claim,status='Proved',where_proved=where,depends_on=dep,item_of_the_prompt='F.2',findings_of_the_survey_settled='F30',notes=note))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
files={}
for name in ('fourfolds_involution_classes.py','fourfolds_involution_classes.out',
             'fourfolds_tuple_classification.py','test_fourfolds_tuple_classification.out',
             'fourfolds_unbounded_trace.py','fourfolds_unbounded_trace.out'):
    p=root/'code'/name;files[name]=hashlib.sha256(p.read_bytes()).hexdigest()
(root/'records/tuple_classification_audit.json').write_text(json.dumps({'statements':['F.2.37','F.2.38'],'independent_proof_code_audit':'PASS','complete_finite_stratum':56,'exact_conjugators':112,'free_affine_lifts':112,'public_classifier_checks':56,'general_height_box_exhausted':False,'files':files},indent=2)+'\n')
print('REGISTERED F.2.37--38; complete56-class finite stratum and proved general canonical algorithm.')
