"""Assemble the complete arbitrary-fan calculations and exact remaining state."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,shutil
root=Path(__file__).resolve().parents[1]
archive=root/'records/checkpoint17_prior_master54';archive.mkdir(exist_ok=True)
for name in ['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log','S6_06_BLIND_paper.aux',
             'S6_06_BLIND_paper.tex','S6_06_BLIND_report.md','S6_06_BLIND_results.csv',
             'code/update_report.py','notes/part3.tex']:
    p=root/name;q=archive/name;q.parent.mkdir(parents=True,exist_ok=True)
    if p.exists() and not q.exists():shutil.copy2(p,q)
parts=['scalar_nonvertical','source_all_fans','scalar_vertical_integer_seed',
       'scalar_all_fans','scalar_formula_corrigendum','remaining_return_obligations']
p=root/'notes/part3.tex';s=p.read_text()
for name in parts:
    child='notes/part3_'+name+'.tex';assert (root/child).is_file()
    line='\\input{'+child+'}'
    if line not in s:s+='\n'+line+'\n'
p.write_text(s)
state=('INCOMPLETE. K71 now computes the actual selected-cusp source return on every GL2Z lattice-basis fan, with the full source, period, Cox, cap and closing maps. K72 proves the complete scalar vertical-seed integer pair, and K73 gives a terminating exact algorithm for every fan of the specified whole-zero I1 canonical scalar families and their constructed shorter endpoints. For the original K=L=1 family with its literal positive AC parameter loop, explicit verified fan witnesses realize all28 elements of Theta7; the basis((1,-2),(0,1)) has class3. An independent program solved86 full target systems for the28 witnesses. K70 independently gives primitive OS45 class11 on basis((2,-1),(-1,1)); the selected-cusp source loop there has class1. K74 refutes eight formerly open compound numerical assertions by actual counterexamples and replaces their whole-zero scalar formulas with K73. F52 is reproved through its actual invariant-divisor family isomorphism and return conjugacy. The fixed-source cap/site comparisons give the appropriate integer iterate of this actual scalar return. K68--69 retain the exact physical/dual line and orientation correction, with physical class A_M=-A_U. The source-zero paired constraints remain (k*A_scalar+14e,a+k*A_scalar+14e), e=0 or1, with A_scalar=0 or3p-1. The smallest good pair is(0,1) or(14,15); reduced p=k=1 gives(2,4) or(16,18). The active finite real cut construction has the explicit source resolution, Cartier line, associated UV=q chart, cap endpoint and charged ruling-end data, but the complete oriented attachment has not been proved. K65 supplies OS49 negative-diagonal classes-3k on r and-k on the shorter w-loop, with positive-diagonal class0. K75 records the exact remaining source-zero attachment, other OS49 fans and added ordinary clutches, remaining marked source-moduli loops and unmarked endpoint sectors. No unknown central class is assigned.')
p=root/'code/update_report.py';s=p.read_text();lines=s.splitlines()
for i,line in enumerate(lines):
    if line.startswith("'3.1':"):
        lines[i]="'3.1':"+repr(('P3F.3–P3F.15, P3F.22–P3F.24, P3K.5–P3K.9, P3K.67–P3K.74','Proved original reference-fan class0, with both independent methods and the physical/dual morphism. K73 computes every actual fan for the specified original positive loop; its28 explicit fan witnesses realize all of Theta7, including class3 on basis((1,-2),(0,1)). The broader all-fan zero assertion is false.'))+','
    if line.startswith("'3.4':"):
        lines[i]="'3.4':"+repr(('P3F.1–P3F.56, P3K.5–P3K.75; exact corrected scopes below',state))+','
s='\n'.join(lines)+'\n'
start=s.index("'## Remaining mathematical obligations'")
a=s.index("'INCOMPLETE.",start);b=s.index("','','## Reproduction and typesetting'",a)
remaining=state+' Parts1,2 and the original blind Part5 retain their independently recorded proofs and immutable original hashes. Part4.2 is proved in the requested irreducible or normal-crossing scope; the separately supplied broader arbitrary non-normal-crossing assertion remains undecided. All earlier false formulas and attempted proofs remain in their identified archives and correction ledgers.'
s=s[:a]+repr(remaining)+s[b+1:]
ast.parse(s);p.write_text(s)
now=datetime.now(timezone.utc).isoformat()
p=root/'code/part3_root/results_mapping.json';d=json.loads(p.read_text())
new=d.setdefault('additional_scalar_fan_results',{})
for ident,name,proof,cert in [
    ('P3K.73','Complete arbitrary-fan physical scalar return, actual shorter endpoints and28 original-family witnesses.','notes/part3_scalar_all_fans.tex','code/part3_root/scalar_all_fans.json'),
    ('P3K.74','Eight exact compound-formula counterexamples and corrected actual family-comparison values.','notes/part3_scalar_formula_corrigendum.tex','code/part3_root/refute_remaining_scalar_polynomials.json'),
    ('P3K.75','Exact remaining source-zero central attachment and other uncomputed return sectors.','notes/part3_remaining_return_obligations.tex','records/remaining_scalar_formula_correction_scope.json')]:
    new[ident]={'utc':now,'id':ident,'status':'Open' if ident=='P3K.75' else 'Proved','item_of_prompt':'3.4','statement':name,'proof':proof,'certificate':cert}
p.write_text(json.dumps(d,indent=2)+'\n')
record={'checked_utc':now,'decision':'CONTINUE',
 'reason':'The main monodromy question advanced to complete arbitrary-fan algorithms for two actual loop classes and explicit witnesses for every element of Theta7; the remaining source-zero and OS49 integer attachments have new actual maps under construction.',
 'main_question_progress':['K71 proves the selected-cusp source return on every GL2Z fan, with6504 input checks and439 independent traversal states.','K72 proves the scalar vertical integer seed with63 exact checks and two complete audits.','K73 proves every scalar fan and actual shorter endpoint;39024 bounded executions,210 full free-invariant cover checks and28 separately verified original-family witnesses accompany the proof.','K74 supplies eight actual counterexamples and preserves the valid family-comparison maps; F52 covariance is reproved.'],
 'other_open_item_progress':['The source-zero compact-cut construction now retains its Cartier line, associated UV=q chart, actual cap arrow and intermediate finite characters; the oriented global end remains unassigned.','The OS49 bottom-row winding calculation retains its extra linear collar term and is being matched to the actual positive-fan integer reference.'],
 'next_main_steps':['Complete the source-zero fixed-boundary surgery and its oriented global attachment.','Apply the exact bottom-row relative tensor calculation to OS49 and extend it over every fan.','Complete the remaining marked source-moduli, ordinary-clutch and unmarked endpoint sectors.'],
 'next_progress_check_due_utc':'2026-11-17T17:49:44+00:00'}
(root/'records/progress_check_17_hours.json').write_text(json.dumps(record,indent=2)+'\n')
print('Assembled K70--75, preserved master54 and recorded main-question progress.')
