"""Append completed working-edition proof reads and their precise outcomes."""
from pathlib import Path
import csv
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/maps_audit'
ACTOR=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
working=json.loads((OUT/'working_results_inventory.json').read_text())
events=json.loads((OUT/'check_events.json').read_text())

def add(event_id, ids, scope, outcome, locator, dependencies=()):
    row=dict(event_id=event_id,results=['WORK:'+x for x in ids],scope=scope,
             outcome=outcome,locator=locator,remaining_dependencies=list(dependencies),**ACTOR)
    if not any(x['event_id']==event_id for x in events):events.append(row)
    return row

def file_ids(name):
    return [r['source_id'] for r in working if Path(r['source_file']).name==name]

new_events=[]
new_events.append(add('new-working-globalization-full-20261117',
    file_ids('cusp_globalization_replacement.tex'),
    'Read and rederived every statement and proof in all 738 source lines: the '
    'primitive full-monodromy character, exact quotient metric and asymptotics, '
    'minimal copy count, finite Seifert targets and overlap identities, literal '
    'cusp nonextension, fixed-target H1/H4 obstructions, and smash scope.',
    'All internal arguments checked. Corrected the deck-group description: '
    'the punctured upper-half-plane model is not the universal cover of the '
    'three-punctured base; use the actual triangle deck group, or use the '
    'universal cover when writing pi1 of the base. This changes no quotient '
    'formula or conclusion. The same quotient construction and nonextension '
    'proof are transferred to Paper I and must be cited rather than duplicated.',
    'sources/workbench/cusp_globalization_replacement.tex:1–738; globalization_deck_group_correction.tex; paperI_circle_quotient.tex'))
new_events.append(add('new-working-cone-routes-full-20261117',
    file_ids('cusp_cone_sphere_routes.tex'),
    'Read and rederived all 950 lines: native quotient descent, endpoint '
    'continuity, global S12/S24 smash constructions, exact radial restrictions '
    'and quotient balls, Seifert homology including integral torsion exclusion, '
    'relative target homology, and all three independent almost-complex '
    'obstructions for S12. The distinction between intrinsic quotient metrics '
    'and any fixed ambient metric is preserved.',
    'Full internal proofs checked. Borel–Serre p.430 and p.434, Husemoller '
    'Chapter 20 Corollary 9.8 p.308, and Konstantis–Parton Lemma 4.1, Theorem '
    '4.2 and Section 6 opened and hypotheses matched. These are classical '
    'obstructions and are credited as such. No smooth compact complex '
    'S12 or S24 construction is inferred from the quotient carriers.',
    'sources/workbench/cusp_cone_sphere_routes.tex:1–950; carrier_source_checks.json'))
new_events.append(add('new-working-strengthened-carriers-full-20261117',
    file_ids('cusp_sphere_route_strengthening.tex'),
    'Read and rederived all 1186 lines: rank optimality, reduced-suspension '
    'sphere maps, exact collapsed loci and quotient distance formula, moving '
    'four-spheres and literal R4 open cells, compact cone-on-T4 carriers and '
    'their local-homology nonmanifold test, target wedge homotopy types, and '
    'the exact noncompact decompactification space. Checked its closed '
    'equivalence relation/open quotient, charts, second countability, '
    'Hausdorffness, exact balls, and nonproper/nonquotient comparison map.',
    'Full internal proofs checked. The three-complex wedge step has an '
    'explicit relative-Hurewicz replacement proof, avoiding an unlocated '
    'Whitehead-exact-sequence appeal. Hatcher Corollary 4.24 and the original '
    'Isaksen–Wang–Xu Table 1 establish the exact stable-range input. The '
    'source open question about the one-copy circle carrier is subsequently '
    'closed by the separate extension-homotopy event; the original source '
    'statement and date are retained.',
    'sources/workbench/cusp_sphere_route_strengthening.tex:1–1186; carrier_three_complex_wedge.tex; carrier_source_checks.json'))
new_events.append(add('new-working-S12-carrier-full-20261117',
    file_ids('cusp_s12_carrier_homotopy.tex'),
    'Read and rederived all 609 lines: for arbitrary S6→S3 maps, factor the '
    'smash as E3(x) after E6(y), use the even subgroup of pi12(S9)=Z/24 '
    'and exponent two of pi12(S6), and retain all higher-smash corollaries. '
    'For the actual candidate, checked the exact period chart, holomorphic '
    'unit coordinate change, uniqueness of the complete inverse T3, all '
    'framing signs and determinants, the explicit D2×T2 cap, collar and '
    'normal framing, relative smoothing with no added inverse points, and '
    'the based Pontryagin–Thom conclusion.',
    'Full internal proofs checked. Hatcher p.339 and Chapter 5 Theorem '
    '5.41/pp.577–578, Isaksen–Wang–Xu Table 1, and Milnor Section 7 '
    'Theorem B/Lemma 4 with the boundary-relative formulation were opened '
    'and their exact dimensions and hypotheses matched. The two-copy '
    'order argument, the explicit candidate nullbordism, and the new '
    'extension homotopy are distinct proofs and are all retained.',
    'sources/workbench/cusp_s12_carrier_homotopy.tex:1–609; carrier_source_checks.json'))
new_events.append(add('new-working-G2-homotopy-full-20261117',['G2-8'],
    'Read the source observation and supplied a complete independent proof: '
    'orthogonalization by the J-invariant metric, explicit SU4 realization '
    'of SO6/U3=CP3, the Hopf-fibration computation pi6(CP3)=0, relative '
    'section obstruction theory on the actual possibly twisted bundle over '
    'S6×I, smooth approximation relative to the ends, and the linear ODE '
    'giving an isomorphism of the endpoint complex vector bundles.',
    'The classical fixed-orientation almost-complex homotopy statement is '
    'proved in the supplied block. The orientation-compatible octonionic '
    'structure is the negative of the course-labelled field. No global '
    'trivialization of the twistor bundle and no integrability preservation '
    'are asserted.',
    'sources/notes/G2_notes.md:468–486; almost_complex_homotopy.tex'))
new_events.append(add('new-working-angle-forgotten-one-copy-null-20261117',
    ['cusp-cone-sphere-map-homotopy-status','cusp-null:thm',
     'cusp-s12-one-copy-invariant','cusp_s12_carrier_homotopy:L567'],
    'Independently derived the extension homotopy from the actual local '
    'fundamental-group inclusion (lambda,n)↦lambda mod K. A torus-valued '
    'extension h exists on N0; the difference from the native map lifts '
    'to R2 on the punctured cusp. First homotope the torus coordinate '
    'at fixed radial height, then slide the height to the outer suspension '
    'endpoint using h. Checked joint continuity at both ends and the fixed '
    'basepoint. Applied it to both the T2-cell collapse and its first '
    'circle character.',
    'The previously open one-copy circle carrier is based nullhomotopic. '
    'The rank-two carrier receives a distinct additional proof, while its '
    'full original framed-torus proof is preserved. The literal flat '
    'quotient still fails pointwise extension; retained-angle maps are '
    'outside the lemma because the base meridian is killed by the filling.',
    'carrier_nullhomotopy_by_extension.tex; sources/workbench/integral_leray.tex:878–913'))

(OUT/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
byresult={}
for event in events:
    for result in event['results']:
        byresult.setdefault(result,[]).append(event)

files={'cusp_globalization_replacement.tex','cusp_cone_sphere_routes.tex',
       'cusp_sphere_route_strengthening.tex','cusp_s12_carrier_homotopy.tex'}
for row in working:
    selected=[e for e in byresult.get('WORK:'+row['source_id'],[]) if e['reader'].startswith('GPT')]
    if Path(row['source_file']).name in files or row['source_id']=='G2-8':
        row['your_check']=' | '.join(e['event_id']+': '+e['scope'] for e in selected)
        row['check_event_ids']=[e['event_id'] for e in byresult.get('WORK:'+row['source_id'],[])]
        row['full_proof_read']=True
        row['current_reader']=ACTOR
        row['check_outcome']=' | '.join(e['outcome'] for e in selected)
        row['source_check_manifest']='carrier_source_checks.json' if row['source_id']!='G2-8' else 'almost_complex_homotopy.tex (independent derivation)'
        row['current_unresolved_proof_gaps']=[]
    if row['source_id']=='cusp-spec-globalization-obstruction':
        row['proof_correction']='globalization_deck_group_correction.tex'
        row['overlap_status']='Exact regular quotient and cusp nonextension coincide with MAPS A.1.1–A.1.3 in Paper I; distinct metric/minimal-copy/smash results retained in III.'
    if row['source_id']=='cusp-cone-target-homotopy-types':
        row['proof_supplement']='carrier_three_complex_wedge.tex'
    if row['source_id']=='cusp-cone-sphere-map-homotopy-status':
        row['source_open_question_resolution']='Both one-copy angle-forgotten maps are based nullhomotopic; new full proof in carrier_nullhomotopy_by_extension.tex.'
    if row['source_id']=='G2-8':row['proof_supplement']='almost_complex_homotopy.tex'

(OUT/'working_results_inventory.json').write_text(json.dumps(working,ensure_ascii=False,indent=2)+'\n')
keys=list(dict.fromkeys(k for row in working for k in row))
with (OUT/'working_results_inventory.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
    for row in working:
        writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})

def sha(name):return hashlib.sha256((OUT/name).read_bytes()).hexdigest()
new_results=[
 dict(source_id='MAPS-AUDIT-CARRIER-EXTENSION',kind='lemma',paper='III',
      title='Suspending a torus-valued map that extends up to homotopy',
      printed_label='mapsIII:carrier-extension-lemma',
      proof_file='carrier_nullhomotopy_by_extension.tex',
      proof_sha256=sha('carrier_nullhomotopy_by_extension.tex'),
      relationship='Additional proof lemma; no original source result removed.',**ACTOR),
 dict(source_id='MAPS-AUDIT-CIRCLE-CARRIER-NULL',kind='proposition',paper='III',
      title='Both angle-forgotten one-copy carriers are nullhomotopic',
      printed_label='mapsIII:angle-forgotten-one-copy-null',
      proof_file='carrier_nullhomotopy_by_extension.tex',
      proof_sha256=sha('carrier_nullhomotopy_by_extension.tex'),
      relationship='Closes the working one-copy circle question; supplies an additional proof of the existing qhat3 theorem.',**ACTOR),
 dict(source_id='MAPS-AUDIT-THREE-COMPLEX-WEDGE',kind='lemma',paper='III',
      title='The three-dimensional coned Seifert target',
      printed_label='mapsIII:carrier-three-complex-wedge',
      proof_file='carrier_three_complex_wedge.tex',
      proof_sha256=sha('carrier_three_complex_wedge.tex'),
      relationship='Full classical proof replacing the unexpanded Whitehead-exact-sequence step in the target-homotopy theorem.',**ACTOR)]
(OUT/'working_carrier_additional_results.json').write_text(json.dumps(new_results,ensure_ascii=False,indent=2)+'\n')
(OUT/'working_carrier_full_checks.json').write_text(json.dumps(new_events,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(working_rows=len(working),new_full_source_rows=sum(Path(r['source_file']).name in files or r['source_id']=='G2-8' for r in working),new_events=len(new_events),retained_events=len(events)),indent=2))
