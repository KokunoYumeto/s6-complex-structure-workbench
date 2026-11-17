"""Register the independently checked universal order-six obstruction."""
from pathlib import Path
import csv,json,datetime
root=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','findings_of_the_survey_settled','notes']
row={'id':'F.2.27','statement':'Every remaining order-(5,6) datum at every rational relative position and stable integral lattice has nonzero three-primary H3 if its degree-two suspension cokernels vanish; hence the only possible three-connected order pair in F.2 is minimal(5,4).',
     'status':'Proved','where_proved':'sections/fourfolds_universal_56_obstruction.tex',
     'depends_on':'F.2.25;F.2.9;F.2.14;E.1.3;integral Poincare duality;Leray filtration',
     'item_of_the_prompt':'F.2','findings_of_the_survey_settled':'F30',
     'notes':'Root proof independently audited by fourfolds agent. h=6 forces local Z3 representation1+Perm3+(-I2); invariant middle pairing has determinant valuation2, so the finite degree-three covering cokernel isZ/3. It injects in E_inf(1,3); the finite E_inf(2,2) kernel cannot absorb its torsion. Exact local code passed, with an independent pairing computation.'}
with (root/'records/fourfolds_root_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fields);w.writeheader();w.writerow(row)
a=root/'records/root_audit_checkpoint06_progress.json'
d=json.loads(a.read_text())
d['updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
d['statements']['F.2.25']='Passed: root independently checked full integral finite splitting, exact m/h suspension cokernel, its surviving Leray injection, the rank-one integral operator divisibilities h|n and h|f(1), and all eight cyclotomic values. Exact program independently rerun.'
d['statements']['F.2.27']='Root proof passed independent fourfolds-agent audit. Norm3 nonzero modulo3 forces the regular permutation3 summand. The full invariant degree-three lattice and pairing are primitive, with determinant valuation2. Degree6 pullback forces index valuation1. The local order3 group survives the Leray middle column, and a finite lower filtration kernel cannot absorb it into a free group. Thus three-primary homology H3 is nonzero for every possible global lattice and rational parameter in this spectral locus.'
for n in ['root_suspension_filter_audit.out','fourfolds_universal_56_obstruction.out']:
 if n not in d['exact_reruns']:d['exact_reruns'].append(n)
a.write_text(json.dumps(d,indent=2)+'\n')
p=root/'S6_04_MAPS_MANIFOLDS_report.md'
s=p.read_text();lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('| F.2 |'):
  lines[i]='| F.2 | F.2.1–F.2.27 | Undecided: every possible three-connected datum now has exactly two genuine finite fillings with actual multiplicities(5,4) and the stated unique finite spectra; all other spectral loci are excluded for every rational pair, lattice and twist. The full rational(5,4) normal form and a terminating complete lattice algorithm are proved. The entire explicit unbounded family has exactly two survivor classes; the other rational parameters and their full affine homology remain unclassified |'
s='\n'.join(lines)+'\n'
heading='## Universal reduction of F.2 to the minimal (5,4) locus'
if heading not in s:
 s+='''\n\n## Universal reduction of F.2 to the minimal (5,4) locus

F.2.25 replaces the former eight-spectral-case filter by an all-lattice local obstruction. At a finite point with linear order n and actual affine multiplicity m, split off an invariant vector on which the primitive global covector has value one. If λ and φ are primitive fixed vertical vector and covector, put h=φ(λ)>0. The exact degree-two covering cokernel is Z/(m/h). Integral averaging and the complementary characteristic polynomial f imply h divides n and h divides f(1). Vanishing of H2 and H3 forces this cokernel to vanish, hence m=h=n and n divides f(1). The eight-case table leaves only minimal(5,4) and the repeated-negative minimal(5,6) spectrum; every order-eight and order-twelve relative position is excluded.

F.2.27 then excludes the entire remaining(5,6) locus. Over Z3, h=6 forces the rank-three order-three summand to be the regular permutation representation: its norm is nonzero modulo3, so it has one length-three Jordan block and a primitive orbit basis. The full local representation is1 plus the permutation3 plus two negative lines. The four invariant middle-degree exterior forms have skew-pairing determinant9. Pullback from the actual free degree-six quotient multiplies a unimodular rank-four pairing by six, forcing an order-three covering cokernel. There are no global invariant degree-three forms to remove it. It survives in the Leray middle column. The adjacent lower filtration term is finite, so the preimage of this order-three subgroup is itself finite and cannot turn into a free group through an extension. Consequently Tor3 H3 is nonzero for every rational position and every stable lattice in that locus.

The only possible three-connected data in F.2 now have the minimal actual multiplicities(5,4). The complete rational normal form of F.2.20 and the terminating lattice/extension algorithm of F.2.22 therefore apply to every possible survivor. The remaining difficulty is the arithmetic and affine-homology classification across that whole rational parameter space, not a multiplicity cutoff or an unexamined finite spectrum. The independent audit and exact middle-pairing certificate are saved in records/root_audit_checkpoint06_progress.json and code/fourfolds_universal_56_obstruction.py/.out.
'''
p.write_text(s)
print('Registered F.2.27; updated universal F.2 scope and independent audit.')
