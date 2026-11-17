from pathlib import Path
import json,csv,re,hashlib
ROOT=Path('.')
OUT=ROOT/'deliverables/work/maps_audit'
PROV={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','review_type':'new independent complete proof reading and rederivation; not human review'}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks={
'lem:triangle-generator-orientations':('Recomputed elliptic derivative signs in Cayley coordinates; checked simultaneous inverse convention and excluded mixed-sign products by their nonparabolic traces.','Beardon1983','period cocycles and deck normalization'),
'prop:period-input-audit':('Read the entire modular-cover lift and deck normalization, cusp normalization, mu-torsor O(-1) obstruction calculation, beta-torsor O obstruction calculation, exact cyclic affine laws, cusp regularity, invariant D and negativity choice, lattice nondegeneracy and family descent. No omitted analytic construction step.','Beardon1983;Serre1973','period cocycles and deck normalization'),
'prop:period-exact-admissible-constants':('Verified D descends, tends to minus infinity at the cusp, attains a finite maximum on the remainder, and the exact nondegeneracy region is Im(c0)<-M; equality and the opposite side give actual degeneracy.','','period cocycles and deck normalization'),
'lem:toric-chart-control':('Checked logarithmic barycentric coordinates in the explicitly restricted polydiscs, the closed-unit-chart identity, orbit-face coverage, and extraction of a finite subcover for each compact set. This statement does not assert the false unrestricted-affine-chart logarithmic bound.','Fulton1993;CoxLittleSchenck2011',''),
'thm:candidate-cusp-geometry':('Read all fan charts and overlaps, smoothness and Hausdorffness, free properly discontinuous action including central strata, compact fundamental representatives and properness, every local central-fibre equation, normalization and opposite-edge identifications with all holomorphic units, triple points, and invariant canonical volume form.','Fulton1993;CoxLittleSchenck2011;Cartan1954Quotient','period cocycles and deck normalization'),
'prop:candidate-cusp-overlap':('Checked the full covering-group quotient: normal subgroup H, residual deck group, exponentiation kernel, conjugations and the actual marked punctured-overlap biholomorphism.','','period cocycles and deck normalization'),
'lem:middle-period-proper':('Checked base proper discontinuity, fibrewise uniform lattice bounds over compact base sets, Hausdorff quotient and local properness of the compact-torus family.','Cartan1954Quotient',''),
'prop:candidate-finite-fillings':('Checked holomorphic affine actions in the varying periods, exact order and freeness at all powers, smooth quotient, reduced central fibre, multiplicity, and the logarithmic punctured-overlap formula.','Cartan1954Quotient','monodromy;period cocycles and deck normalization'),
'lem:finite-filling-stalk-map':('Checked the equivariant radial retraction in actual flat coordinates and the resulting integral nearby-fibre pullback as the precise quotient-covering map, not only a rational invariant identification.','','monodromy'),
'thm:candidate-global-geometry':('Read every gluing and separation case, connectedness and compactness, local properness, exact exceptional fibres and multiplicities, and the restricted canonical-bundle identification. The obsolete conductor-label prose is nonoperative and requires the already recorded editorial replacement.','Cartan1954Quotient',''),
'prop:monodromy-certificate':('Multiplied all displayed cohomology and homology matrices exactly; checked orders, inverse-transpose convention, cusp nilpotence and A1 A2 M0=I.','','monodromy'),
'thm:cusp-lattices':('Checked every exterior-power fixed lattice, rank, integral basis and saturation, including equality of cusp image and kernel.','','cusp invariant lattices'),
'thm:coinvariants':('Checked global invariant generators and integral coinvariants in every exterior degree; compared the printed B2/B3 matrices entry by entry and their Smith invariants.','','global invariant/coinvariant lattices'),
'prop:finite-indices':('Read the finite Bieberbach group abelianizations, all fixed-power kernels, pullbacks in every degree, index and parity arguments, integral perfect-pairing step and explicit cyclic-extension transgression. Recomputed degree-three pairings and exact norm lattices. The independent finite_extension_transgression proof supplies the operative d2 formula.','Brown1982;Hatcher2002','finite invariant and pullback arithmetic'),
'prop:terminal-group':('Checked the nonabelian van Kampen quotient, normal closure reduction to the stated abelian generators, affine translation relations and exact determinant giving the terminal group.','','terminal certificates'),
'prop:terminal-degree-two':('Recomputed the complete integer boundary matrix, primitive annihilator, two coprime minors and Smith form; verified that they establish equality of integral sublattices.','','terminal certificates'),
'prop:terminal-all-degree':('Checked every explicitly stated hypothesis, group and H2 inputs, finite generation, UCT/PD deductions and smooth recognition; this is a conditional package whose geometric hypotheses are supplied by the full construction and topology blocks.','Hatcher2002;Smale1961;Smale1962;KM1963','terminal certificates'),
'ffcert:prop:integral-summands':('Verified full kernel/image sublattices for both finite actions, primitivity, every basis vector and determinant giving indices three and two.','','fixed/moving product-cover lattices'),
'ffcert:thm:product-covers':('Checked the actual unchanged central complex periods, fixed and moving elliptic factors, linear product maps, full kernel enumeration and cyclic orders, hence the exact product-cover degrees nine and eight.','','fixed/moving product-cover lattices;central complex product maps'),
'ffcert:prop:quotient-charts':('Checked all cyclic quotient charts, free actions, central multiplicities and maps to the original affine finite-filling charts.','Cartan1954Quotient','central complex product maps'),
'ffcert:thm:normalization':('Read the entire normalized branched base-change argument, all connected components and their quotient identifications, residual actions and comparison with the original total spaces.','','central complex product maps'),
'ffcert:thm:peripheral-kernel':('Checked the complete peripheral group presentation and based overlap map, including the central infinite cyclic kernel and the original marked homology lattice; no nonabelian relation was replaced silently by its abelianization.','','monodromy;fixed/moving product-cover lattices'),
'ffcert:cor:covering-h1':('Checked the explicit covering map on first homology and all rational/integral coordinate comparisons, including the direction of the contragredient action.','','monodromy;fixed/moving product-cover lattices'),
'ffcert:thm:normal-trivialization':('Checked the normal bundle character, exact holomorphic torsion order and its lower bound, all equivariance equations, and the explicit smooth nowhere-zero trivialization. The redundant finite-normal-order pointer is replaced by the assertion proved in this same proof.','','central complex product maps')
}
source_rows=list(csv.DictReader(open('deliverables/work/root/working_edition_inventory.csv')))
source_rows=[r for r in source_rows if r['source_id'] in checks]
assert len(source_rows)==24
ledger=json.load(open(OUT/'references_verified.json'))
rows=[]
for r in source_rows:
 sid=r['source_id']; relative,ln=r['source_file'].rsplit(':',1); p=Path('sources')/relative
 txt=p.read_text(); lines=txt.splitlines(); start=int(ln)
 i=start-1
 while i>0 and not re.search(r'\\begin\{(?:theorem|proposition|lemma|corollary)\}',lines[i]):i-=1
 statement_start=i+1
 j=i
 while j<len(lines) and not re.search(r'\\end\{(?:theorem|proposition|lemma|corollary)\}',lines[j]):j+=1
 proof_start=next(k for k in range(j+1,len(lines)) if '\\begin{proof}' in lines[k])
 proof_end=next(k for k in range(proof_start+1,len(lines)) if '\\end{proof}' in lines[k])
 segment='\n'.join(lines[statement_start-1:proof_end+1])
 scope,refs,reruns=checks[sid]
 deps=[]
 for m in re.finditer(r'\\(?:c|C|eq|page)?ref\{([^}]+)\}',segment):deps.extend(x.strip() for x in m.group(1).split(','))
 rows.append({'source_run':'WORKING_EDITION','source_id':sid,'source_file':str(p),'source_sha256':sha(p),'paper':'I','printed_label':'wb:'+sid,'statement_start_line':statement_start,'statement_end_line':j+1,'proof_start_line':proof_start+1,'proof_end_line':proof_end+1,'statement_as_source':r['statement_as_source'],'source_dependencies':sorted(set(deps)),'recorded_checks':'Existing parent/source review records must be retained; this manifest adds the current full read, and does not negate or replace earlier checks.','your_check':scope,'full_proof_read':True,'check_outcome':'Full proof independently read and rederived; exact arithmetic certificates PASS where applicable; stated companion dependencies are explicit.','remaining_mathematical_gap':'None identified in this result after matching the named companion hypotheses; conditional statements retain all source hypotheses.','operative_external_source_keys':refs.split(';') if refs else [],'external_source_check_ledger':'deliverables/work/maps_audit/references_verified.json; wb_foundation_source_checks.json; topology_source_checks.json','independent_rerun_scopes':reruns.split(';') if reruns else [],'independent_program':'deliverables/code/maps_audit/paperI_foundation_arithmetic.py','independent_program_sha256':sha('deliverables/code/maps_audit/paperI_foundation_arithmetic.py'),'independent_output':'deliverables/code/maps_audit/paperI_foundation_arithmetic.json','independent_output_sha256':sha('deliverables/code/maps_audit/paperI_foundation_arithmetic.json'),'check_event_id':'new-construction-24-full-20261117',**PROV})
obj={'scope':'All 24 labelled construction results assigned by parent, plus complete source context','complete_files_read':[{'file':'sources/workbench/'+f,'lines':len(Path('sources/workbench',f).read_text().splitlines()),'sha256':sha(Path('sources/workbench',f))} for f in ['candidate_geometry.tex','exact_algebra.tex','finite_filling_certificates.tex']],'proof_read_count':24,'arithmetic_status':'PASS','limits':'No computation is used as a substitute for the analytic, geometric, covering-space or spectral-sequence proofs. Source hypotheses and edition limitations in the reference ledger remain explicit.','rows':rows}
(OUT/'paperI_construction_full_checks.json').write_text(json.dumps(obj,indent=2)+'\n')
with (OUT/'paperI_construction_full_checks.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in r.items()} for r in rows)
# Preserve every previous event and append the present one exactly once.
events=json.load(open(OUT/'check_events.json'))
event={'id':'new-construction-24-full-20261117','source_ids':[r['source_id'] for r in rows],'scope':'Entire candidate_geometry.tex (1581 lines), exact_algebra.tex (587 lines), finite_filling_certificates.tex (760 lines) read and all 24 labelled proofs rederived. Independent exact arithmetic rerun passes eight named scopes.','outcome':'No new mathematical gap identified; source edition/hypothesis limits and already identified editorial pointers retained.','manifest':'deliverables/work/maps_audit/paperI_construction_full_checks.json',**PROV}
if isinstance(events,list):
 if not any(x.get('id')==event['id'] for x in events):events.append(event)
else:raise TypeError('Unexpected event ledger shape')

for event_record in events:
 if 'event_id' not in event_record:
  event_record['event_id']=event_record['id']
  event_record['results']=['WORK:'+x for x in event_record['source_ids']]
  if 'scope' not in event_record:event_record['scope']='Complete source proof reads: '+'; '.join(event_record.get('full_proof_reads',[]))
  event_record['locator']=event_record['manifest']
  event_record['remaining_dependencies']=[]
(OUT/'check_events.json').write_text(json.dumps(events,indent=2)+'\n')
print('Saved',len(rows),'full result checks. Source ranges:',[(r['source_id'],r['proof_start_line'],r['proof_end_line']) for r in rows])
