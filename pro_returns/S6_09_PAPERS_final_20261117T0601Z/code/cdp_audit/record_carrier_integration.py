"""Persist exact receiving scopes and the two required prerequisite rows."""
import csv, hashlib, importlib.util, json, re, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'deliverables/work/cdp_audit'
META = {'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort':'Pro',
        'date':'2026-11-17', 'timezone':'UTC', 'reader':'/root/cdp_audit'}
MOD = ROOT/'deliverables/code/editorial/paper_iii_carrier_corrections.py'
spec=importlib.util.spec_from_file_location('carrier_corrections',MOD)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

current=ROOT/'deliverables/S6_09_PAPERS_III.tex'; s=current.read_text()
t=mod.transform(s)
assert mod.transform(t)==t
old=set(re.findall(r'\\label\{([^}]+)\}',s)); new=set(re.findall(r'\\label\{([^}]+)\}',t))
assert old<=new
assert all(x not in t for x in [mod.DECK_OLD,mod.KUMMER_OLD,mod.WEDGE_OLD,mod.NULL_OLD])
missing=['wb:cusp-spec-full-inverse-transpose','wb:cusp-spec-holomorphic-errors',
         'wb:cusp-spec-native-quotient','wb:cusp-spec-radial-notation']
assert all(x in new for x in missing)
review=WORK/'carrier_transformed_review.tex';review.write_text(t)
write(WORK/'carrier_transform_validation.json',{
    'reader':META,'input':str(current.relative_to(ROOT)),'input_sha256':sha(current),
    'output':str(review.relative_to(ROOT)),'output_sha256':sha(review),
    'transformer':str(MOD.relative_to(ROOT)),'transformer_sha256':sha(MOD),
    'idempotent':True,'all_existing_labels_preserved':True,
    'original_label_count':len(old),'new_label_count':len(new),
    'added_labels':sorted(new-old),'stale_blocks_removed':True,
    'four_missing_prerequisites_defined':True})

program=ROOT/'deliverables/code/cdp_audit/check_carrier_period_matrix.py'
before=sha(program); start=time.monotonic()
run=subprocess.run([sys.executable,str(program)],capture_output=True,text=True,cwd=ROOT)
out=program.with_suffix('.out');out.write_text(run.stdout)
err=program.with_suffix('.err');err.write_text(run.stderr)
assert run.returncode==0 and sha(program)==before
execution={'command':[sys.executable,str(program)],'cwd':str(ROOT),'exit_code':run.returncode,
           'elapsed_seconds':round(time.monotonic()-start,3),'program':str(program.relative_to(ROOT)),
           'program_sha256':before,'stdout':str(out.relative_to(ROOT)),'stdout_sha256':sha(out),
           'stderr':str(err.relative_to(ROOT)), 'reader':META,
           'scope':'All printed real-period and inverse-transpose entries and exact projected columns, symbolically. No geometric claim is inferred from a finite or symbolic check.'}
write(WORK/'carrier_period_program_record.json',execution)

readings=[
 {'source':'sources/workbench/cusp_toric_cover_completion.tex','ranges':[[1,285],[350,405]],
  'scope':'Original statement, full source-action/freeness/properness context and power-map descent; final regular-period and conductor argument. The intervening local nonflatness argument is covered by the prior full reader, not reread in this event.'},
 {'source':'sources/workbench/cusp_globalization_replacement.tex','ranges':[[1,220],[315,408]],
  'scope':'Actual deck quotient, radial metric definitions, native-quotient dependency, invariant character, full inverse-transpose and expansion uses, minimality context.'},
 {'source':'sources/workbench/cusp_cone_sphere_routes.tex','ranges':[[1,170]],
  'scope':'Complete native-descent lemma and its proof, target definitions and first S12 carrier statement, to match the missing compact-quotient prerequisite.'},
 {'source':'sources/workbench/cusp_sphere_route_strengthening.tex','ranges':[[630,698],[785,885]],
  'scope':'Exact moving-sphere and one-copy status contexts; complete target-homotopy statement and receiving wedge argument through its unstable-scope conclusion.'},
 {'source':'sources/workbench/cusp_s12_carrier_homotopy.tex','ranges':[[1,185],[538,609]],
  'scope':'Original universal smash vanishing and all-higher-smash proof, one-copy invariant, scope, final based-nullbordism conclusion and corollary. The middle explicit torus/cap construction remains the prior full reader’s scope, not a new full reading here.'},
 {'source':'sources/workbench/cusp_spectral_geometry.tex','ranges':[[4,153],[190,241],[722,770],[866,944]],
  'scope':'Only the necessary nonspectral period/realification, dual lattice, long-plane bound and complete native compact-quotient proof. No spectral theorem is certified or imported.'},
 {'source':'sources/workbench/topology_reduction.tex','ranges':[[640,790]],
  'scope':'Original actual finite-band theorem/proof and exact erroneous degree-one/degree-three identification; checked against already corrected PaperI proposition and full repair.'},
]
for r in readings:r['sha256']=sha(ROOT/r['source'])
repairs=[]
for name in ['globalization_deck_group_correction','carrier_three_complex_wedge','kummer_compact_chart_repair','finite_degree_three_correction','carrier_nullhomotopy_by_extension']:
 p=ROOT/'deliverables/work/maps_audit'/f'{name}.tex'
 repairs.append({'source':str(p.relative_to(ROOT)),'sha256':sha(p),'reading':'Full text read; mathematical argument independently rederived at its stated scope.'})

audit={'event_id':'carrier-actual-use-receiving-check-20261117','reader':META,
       'scope':'Independent check of the exact five repair texts, their actual original and assembled use, and every line of the new nonspectral prerequisite proof. This is not a second full reading of all five complete carrier source files.',
       'prior_full_reading':'deliverables/work/maps_audit/working_carrier_full_checks.json',
       'original_context_readings':readings,'complete_repair_readings':repairs,'changes':mod.CHANGES,
       'independent_reasoning':[
           'The punctured upper-half-plane model uses the triangle deck image; only the universal-cover model may take the full base fundamental group as its deck group.',
           'A maximal height-one chart gives log-position barycentric coefficients summing to one. Upper bounds on compact chart pieces bound each coefficient below and therefore above. Finite compact chart pieces and the uniform translation lower bound give proper discontinuity. Unit polydiscs must be cut by a closed subdisc lying inside the action domain before taking their compact images.',
           'The wedge map is an isomorphism on H2. Its mapping-cylinder pair is 2-connected; relative Hurewicz, the homology exact sequence and the surjective homotopy exact sequence yield a spherical H3 generator. Homological Whitehead then proves the full wedge equivalence.',
           'The extension homotopy has two stages: lift the torus-valued difference on the punctured neighbourhood, then move the suspension height after reaching a map defined on the full neighbourhood. Compactness of the target gives uniform endpoint continuity; the explicit frontier hypothesis permits closed pasting; h(x0)=0 fixes the basepoint.',
           'The finite-band degree-three correction uses the actual H3/H^3 Kronecker pairing and the integral pulled-back H3 lattices. Its indices1 and2 differ from the degree-one indices3 and4. The actual I statement/proof already prints this correction; the false original sentence is not present in III.',
           'The new radial helper is a complete direct derivation: holomorphic Taylor bounds, literal realification, an exact 2x2 inverse system, integral kernel lattice, orthogonal quotient, singular-value lower bound, and onto-ball isometry. No Laplace or spectral theorem enters.'
       ],
       'outcome':'No unaddressed mathematical objection in the specified repaired scopes. Current-use stale assertions removed, full repaired proofs retained, and four substantive missing dependencies supplied.',
       'parent_review':{'reader':'/root','model':META['model'],'effort':'Pro','date':META['date'],
           'scope':'Complete new radial prerequisite proof, inverse transpose and exact quotient/ball argument.',
           'outcome':'Passed independent receiving review.',
           'evidence':'Parent collaboration message: integrated carrier transform and independently read/rederived complete radial prerequisite proof.'},
       'program_record':'deliverables/work/cdp_audit/carrier_period_program_record.json',
       'transform_validation':'deliverables/work/cdp_audit/carrier_transform_validation.json'}
write(WORK/'carrier_integration_audit.json',audit)

mapping=[]
for label,scope,lines in [
 ('wb:cusp-spec-radial-notation','Definition of every radial symbol used in the actual carrier circumference and quotient calculations',[42,67]),
 ('wb:cusp-spec-holomorphic-errors','Taylor estimates needed for the exact circle asymptotics',[68,74]),
 ('wb:cusp-spec-full-inverse-transpose','Complete inverse transpose, rederived from the literal real period matrix',[88,153,190,241]),
 ('wb:cusp-spec-native-quotient','Complete native real compact quotient and geometric systolic/onto-ball proof',[722,770,866,944])]:
 mapping.append({'missing_label':label,'resolution':'Exact same label supplied in a complete nonspectral prerequisite block',
                 'destination':'deliverables/work/cdp_audit/carrier_radial_prerequisites.tex',
                 'source':'sources/workbench/cusp_spectral_geometry.tex','source_ranges':lines,
                 'necessary_math':scope,'excluded_lane':'Laplacian, eigenfunctions, spectrum, heat/counting laws, volume-normalized spectral limits and the later exceptional elliptic quotient are not imported.'})
write(WORK/'carrier_missing_reference_map.json',mapping)

inventory=list(csv.DictReader((ROOT/'deliverables/S6_09_PAPERS_inventory.csv').open()))
fields=list(inventory[0]); assert len(fields)==17
helper=WORK/'carrier_radial_prerequisites.tex'; h=helper.read_text()
extra=[]
for sid,label,source_scope,wording in [
 ('carrier-real-periods','mapsIII:carrier-real-periods','cusp_spectral_geometry.tex:4–153,190–241',
  'Necessary real-period and dual-coordinate portion, with full independent proof; excludes the distinct Laplacian/spectrum clauses of the original broader proposition.'),
 ('carrier-native-quotient','wb:cusp-spec-native-quotient','cusp_spectral_geometry.tex:722–770,866–944',
  'Complete native compact quotient, integral kernel and systolic proof retained; includes the complete immediate onto-ball argument required by the subsequent carrier limits.')]:
 pos=h.index('\\label{'+label+'}'); start=h.rfind('\\begin{proposition}',0,pos);end=h.index('\\end{proposition}',pos)+len('\\end{proposition}')
 row={k:'' for k in fields}
 row.update(source_run='WRITING_REPAIR',source_id=sid,
   source_file='deliverables/work/cdp_audit/carrier_radial_prerequisites.tex; original sources/workbench/'+source_scope,
   paper='III',printed_label=label,kind='Proposition',statement_as_printed=h[start:end],
   wording_vs_source=wording,
   recorded_checks='Original working source retained; current independent rederivation and separate parent receiving review are recorded in work/cdp_audit/carrier_integration_audit.json. No historical full proof check is invented.',
   your_check='GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC, /root/cdp_audit: every statement and proof line read and rederived. Separate /root receiving review: complete proof, inverse transpose and exact quotient/ball argument passed. Exact symbolic transcription check recorded in carrier_period_program_record.json.',
   check_outcome='Passed in the stated nonspectral scope; printed through the idempotent carrier transformer. Root independently reviewed the complete new proof.',
   found_in_AC26='Known original complex cusp construction is an input; exact full-statement attribution recorded separately in the bounded carrier comparison.',
   found_in_E26='Known original torus-period construction is an input; exact full-statement attribution recorded separately in the bounded carrier comparison.',
   found_in_DGKX_v1='Known cusp/period model is an input; no novelty assertion. The two DGKX editions remain separate in the detailed comparison.',
   found_elsewhere='Direct real linear algebra and flat quotient geometry are classical background. This row supplies the explicit necessary marked calculation with its complete proof.',
   credited_to='Underlying complex sphere/torus construction: AC26 and Engel; original explicit radial formulas: attached working edition. Linear duality and flat quotient arguments are background rederivations.',
   notes='Necessary nonspectral prerequisite. Definitions and Taylor estimates are common data, not separate inventory results. Complete helper SHA256 '+sha(helper)+'. Root review provenance: collaboration message received this turn.')
 extra.append(row)
write(WORK/'carrier_prerequisite_inventory_2.json',extra)
with (WORK/'carrier_prerequisite_inventory_2.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(extra)
print('Saved carrier audit, reference map, updated validation, exact symbolic command record, and two17-column inventory rows.')
