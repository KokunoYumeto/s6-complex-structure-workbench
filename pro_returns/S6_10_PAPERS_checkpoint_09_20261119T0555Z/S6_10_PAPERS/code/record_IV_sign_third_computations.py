"""Consolidate bounded execution receipts; never import source audit claims."""
from pathlib import Path
import csv,json,hashlib,datetime
P=Path(__file__).resolve().parents[1];TREE=P/'analysis/IV_sign_third_replays'
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)'
scopes={
'source_cusp_circle_trace':('night:P3K.52','21 exact quaternion-axis, factorization, integral-volume and variation-matrix checks. This dependency execution supplies no new full-proof review of K51.'),
'source_cusp_ordinary_relative':('night:P3K.50','13 exact actual-chart, inverse-cylinder direction and retained free-coordinate identities. The program hard-codes historical central+1; that constant and its emitted proof/audit status are not accepted as current physical conclusions.'),
'source_cusp_stable_trace':('night:P3K.52','19 exact covering-group, quaternion trace, Spin endpoint and stable-derivative/free-coordinate identities, using this batch\'s fresh circle-trace JSON. No inference of geometric prism or frame extensions from the program.'),
'source_cusp_first_flops':('night:P3K.54','6 exact native-chart, directed conjugation and inverse-flop checks. Its old central+1 input yields withdrawn23,23,1; current21,21,27 is checked in the separate corrected arithmetic program.'),
'source_cusp_vertical_fans':('night:P3K.56','16 exact shear, trace, triangle, recurrence, period and reflection identities; bounded rows n=-56 through56. The historical+1 polynomial is retained only as input to the unchanged replay, not restored as the physical return.'),
'source_cusp_mutation_diagnostic':('night:P3K.59','Exact symbolic staircase matrix/derivative steps plus depth-seven search of210 basis states and128 fan states, with zero conflicts/integrality failures. Four separate fixed-target transitions are explicitly skipped. The historical central baseline is not promoted, and the finite search does not prove the unbounded fan theorem.'),
'source_zero_double_loop_product':('night:P3K.60','59 exact full-unit seam/chart/Cox/trace identities,64 signed cap tuples and the retained single-free-coordinate square. Its32 historical paired rows use the refuted scalar sign; separate corrected arithmetic supplies the current pairs. No division in Theta7 or geometric order-two selection is made by this code.'),
'source_global_groupoid':('night:P3K.58','215 exact source, discriminant, height, Cartier/root endpoint, named-chart and quadratic-cochain identities. The final historical+1 cut relation and derived pairs are refuted physical inputs; their current corrections are separately replayed. The program does not prove analytic gluing or the cut-surface isotopy.'),
'source_infinity_exact':('night:P3K.57','307 exact polynomial, Tate-unit, theta/Cartier involution, root endpoint and separator/norm inequalities, with108 marked cap rows. Full source/line units are retained; code does not establish analytic properness or a global return.'),
'source_infinity_regular_fan':('night:P3K.57','Fresh execution of the unchanged primitive-ray and period-face algorithm for the stated case: exact determinant-one final cones, simultaneous stellar drops, protected boundary preservation and every exported literal face/period map. No analytic filling or physical return is inferred by the program.'),
'source_infinity_fixed_charts':('night:P3K.57','Fresh execution on both newly recomputed regular fans, forming every exact inverse cone matrix, physical weight and minimal-face component/period identification. This is a finite chart computation, not the analytic attachment proof.'),
'source_infinity_interior_residues':('night:P3K.57','Fresh exact rational localization on every compact interior component of both new fixed-chart exports; cocharacters(1,4,16,64) and(1,5,25,125) agree component by component. Reproduces9333/16 and739. Boundary/gluing/orientation maps remain the separate mathematical argument.'),
'source_infinity_h_residues':('night:P3K.57','Fresh full three-point H-unit degrees including(1-w)^N, higher ray heights and recorded periods; two auxiliary fibre circles agree on every component. Reproduces-9301/16 and-734,125/111 H components and194/152 auxiliary fixed curves. No uncomputed boundary sign is inferred.'),
'source_infinity_e_cycles':('night:P3K.57','Fresh actual E central-cycle, primitive multiplicity and determinant-order computation in both new fixed-chart exports:8/6 I2 components, intersection[[-2,2],[2,-2]], multiplicities[1,1], determinant orders[0,0]. Its annular E residue is not substituted for the separately proved closed E-double contribution.')}
receipts=[]
for file in sorted((TREE/'receipts').glob('*.json')):
 r=json.loads(file.read_text());assert r['returncode']==0
 stem=Path(r['source']).stem;label,scope=scopes[stem]
 src=Path(r['unchanged_copy']);assert hashlib.sha256(src.read_bytes()).hexdigest()==r['source_sha256']
 if stem in ['source_infinity_regular_fan','source_infinity_fixed_charts','source_infinity_interior_residues','source_infinity_h_residues']:
  args=r['arguments'];case=args[args.index('--case')+1];cases=['1_2_8','2_1_6'] if case=='all' else [case.replace(',','_')]
  outputs=[src.parent/(stem+'_'+case+'.json') for case in cases]
 elif stem=='source_infinity_e_cycles':outputs=[src.parent/(stem+'_'+case+'.json') for case in ['1_2_8','2_1_6']]
 else:outputs=[src.with_suffix('.json')]
 rows=[]
 for output in outputs:
  data=json.loads(output.read_text());small=data.get('summary',data)
  observed={k:small[k] for k in ['status','checks','checks_count','check_count','star_steps','maximal_cone_counts','chart_count','component_count','interior_component_count','H_component_count','H_full_fibre_torus_fixed_curves','basis_states','fan_states','depth','skipped_separate_fixed_targets','total_normal_link_residue','H_normal_link_residue'] if k in small}
  if 'checks' in observed and isinstance(observed['checks'],list):observed['checks']=len(observed['checks'])
  rows.append({'file':str(output.relative_to(P)),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'bytes':output.stat().st_size,'observed':observed})
 r.update({'labels':label,'bounded_scope':scope,'outputs':rows,'record_note':'Source-emitted historical reviewer/audit and theorem-status prose is preserved only as raw output, never imported as a current check.'})
 receipts.append(r)
# Preserve one current event per actual run; a two-case command remains one event.
f=P/'records/IV_sign_computation_events.tsv'
with f.open() as h:r=csv.DictReader(h,delimiter='\t');fields=r.fieldnames;old=list(r)
assert len(old)==25,len(old)
new=[]
for i,r in enumerate(receipts,26):
 event=f'IV-SIGN-C-{i:03d}'
 output_receipt=TREE/'receipts'/(Path(r['source']).stem+'_scoped_'+str(i)+'.json')
 output_receipt.write_text(json.dumps(r,indent=2)+'\n')
 new.append({'event_id':event,'labels':r['labels'],'who':who,'date':r['finished'],'type':'current unchanged exact code replay','verdict':'PASS within explicitly retained arithmetic scope','scope':r['bounded_scope'],'source_sha256':r['source_sha256'],'output_sha256':hashlib.sha256(output_receipt.read_bytes()).hexdigest(),'script':str(Path(r['unchanged_copy']).relative_to(P)),'output':str(output_receipt.relative_to(P)),'result_observed':r['finished']})
file=P/'analysis/IV_sign_corrected_retained_arithmetic.json';d=json.loads(file.read_text());script=P/'code/IV_sign_corrected_retained_arithmetic.py'
new.append({'event_id':f'IV-SIGN-C-{26+len(receipts):03d}','labels':'night:P3K.50;night:P3K.54;night:P3K.56;night:P3K.57;night:P3K.58;night:P3K.59;night:P3K.60','who':who,'date':d['date'],'type':'current new independent arithmetic certificate','verdict':'PASS','scope':'17 symbolic/bounded checks of the corrected central baseline, both unbounded polynomial recurrences, complete28/7 residue images, both freshly recomputed infinity sums and all32 corrected paired congruences. The physical-line, clutch and E-double maps are separate mathematical inputs; no good-branch order-two choice is selected by code.','source_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'script':str(script.relative_to(P)),'output':str(file.relative_to(P)),'result_observed':d['date']})
with f.open('w') as h:
 w=csv.DictWriter(h,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(old+new)
(P/'analysis/IV_sign_third_replay_manifest.json').write_text(json.dumps({'updated':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unchanged_runs':receipts,'new_corrected_arithmetic':new[-1],'events':new,'not_executed':'The copied source_infinity_excision_certificate.py was read but not run: it requests four extra historical fan cases. The two required fresh cases, their exact local source/Jacobian inputs and the actual closed-double lattice were rederived and checked directly; no new execution credit is assigned to the four optional cases.'},indent=2)+'\n')
print('Recorded',len(receipts),'unchanged runs and one corrected certificate; computation events now',len(old+new))
