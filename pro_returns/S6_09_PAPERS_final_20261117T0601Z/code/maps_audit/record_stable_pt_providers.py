from pathlib import Path
import hashlib,json,shutil

ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'sources/codex_workspace/courses/CG-S6/src'
OUT=ROOT/'deliverables/work/maps_audit'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
items=[
 dict(name='the-original-integral-stable-group-and-its-completion-maps.md',key='integral-stable-comparison',
      scope='Read and rederived the complete chapter, all nine sections and both full exercises. Checked the integral finite free chain model and the signed contraction of its cone; finite-generation induction for the original coefficient spaces and Whitehead path fibres; the finite-range homology comparison and exact right-appended suspension range; the full Moore short exact sequence with reduction on the cokernel and multiplication by p on the torsion subgroup; both inverse-limit contributions; the original unit map to the p-adic completion, all primary projectors and basis lifts; and the two explicit integer examples, including the negative connecting sign.',
      outcome='The receiving integral comparison is internally consistent. The sixth-stem numerical input is imported from the mod-two and odd-prime actual cooperation calculations and their Adams/arithmetic comparison. Those complete original provider proofs remain to be read: the classical numerical answer alone does not certify this course rederivation. The finite-type construction also imports the exact cocycle/bundle and integer bar/prism comparisons.',
      deps=['the-adams-tower-and-exact-inverse-limits.md','the-actual-mod-two-cooperation-comparison-through-degree-eight.md','the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md','the-original-adams-tower-and-arithmetic-completion.md','integral-handle-chains-and-signed-incidences.md'],
      credit='Strickland 2412.09361v1 original-author TeX intervals 1–160, 241–524, 568–600, 1006–1401 are claimed in the producer source; the current audit has not yet opened them.',
      date='11 October 2026', note='Equation (6.11) has the harmless typesetting string Z_p^{,r}; print Z_p^r in the converted proof.'),
 dict(name='framed-manifolds-and-the-pontryagin-thom-map.md',key='pontryagin-thom',
      scope='Read and rederived all 936 lines, all ten sections and both complete exercises. Checked the explicit finite-chart embedding; tangent-to-normal isomorphism, inverse and permutation sign; nonorthonormal Gram tube, uniform injectivity and smooth flat collapse; framed bordism to based homotopy with endpoint radii and full product collars; relative smooth approximation and fixed-value transversality; the exact recovered inverse-image frame; all three inverse homotopies, including exclusion of extra inverse-image components, curved-to-linear tube and coordinate-ball-to-Gram-ellipsoid comparisons; the full finite-codimension bijection, right-appended suspension and finite-stage stable bounding; the original complex tangent-framing homotopy, with its scope and its separately proved general stable-frame extension retained.',
      outcome='The full printed finite-codimension normal-framed correspondence and specified stable bounding construction are checked. The finite-chart, smooth approximation, tube and regular-value arguments verify their own local hypotheses. Sard is an explicit foundational smooth-analysis input. The complex-specific framing proof is retained separately from the general stable-framing proof in the already read sphere-twist chapter; determinant sign alone is never used to identify their homotopy classes. The use of this normal-framed correspondence as the full abstract tangent-framed bordism equivalence requires retaining the relative embedding and collar conversion, which is tracked separately in the dependency ledger rather than inferred from a set cardinality.',
      deps=['relative-morse-functions-and-original-handles.md'],
      credit='Michel–Weber 1409.0704v1 §3.2 author-source lines 535–539 is the producer’s precise historical context, not a claimed source of the complete printed proof; current primary comparison pending.',
      date='10 October 2026',note='No mathematical correction found in the full printed finite-codimension construction. Stable tangent-bordism conversion is to be checked at its actual receiving use.')
]

dest=OUT/'course_geometric_provider_full_checks.json'
events=json.loads(dest.read_text())
known={e['event_id'] for e in events}
new=[]
for d in items:
 p=SRC/d['name']; ls=p.read_text().splitlines()
 e=dict(event_id='new-course-provider-'+d['key']+'-full-20261117',source=str(p.relative_to(ROOT)),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),locator=f'{p.relative_to(ROOT)}:1–{len(ls)}',line_count=len(ls),raw_producer_header=ls[2],producer='GPT-6 Astra (OpenAI)',producer_effort='Ultra',producer_date=d['date'],full_proof_read=True,scope=d['scope'],outcome=d['outcome'],remaining_imported_proof_dependencies=d['deps'],original_source_comparison=d['credit'],correction_or_scope_note=d['note'],numerical_program_rerun='not yet rerun by this event',**META)
 if e['event_id'] not in known: events.append(e);new.append(e)
dest.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
h=OUT/'check_events.json';hist=json.loads(h.read_text());known={e.get('event_id') for e in hist};hist.extend(e for e in new if e['event_id'] not in known);h.write_text(json.dumps(hist,ensure_ascii=False,indent=2)+'\n')
p=OUT/'course_geometric_dependencies_pending.json';j=json.loads(p.read_text());by={Path(e['source']).name:e for e in events}
for r in j['pending']:
 if r['source'] in by:
  e=by[r['source']];r.update(status='Full receiving-provider proof read; imported dependencies separately tracked',checked_event=e['event_id'],remaining_imported_proof_dependencies=e['remaining_imported_proof_dependencies'])
j['status_note']='All original seven provider chapters have now been read in full. Their deeper operative prerequisites are listed explicitly and are not certified by those receiving reads. Earlier pending events remain preserved.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')

proofdir=OUT/'checked_course_providers';proofdir.mkdir(exist_ok=True)
manifest=[]
for e in events:
 src=ROOT/e['source'];out=proofdir/src.name;shutil.copyfile(src,out)
 manifest.append(dict(source=e['source'],source_sha256=e['source_sha256'],retained_complete_proof=str(out.relative_to(ROOT)),retained_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),checked_event=e['event_id'],full_receiving_proof_read=True,dependency_closure='See remaining_imported_proof_dependencies in full-check event; not blanket certification',producer=e['producer'],producer_effort=e['producer_effort'],producer_date=e['producer_date'],raw_producer_header=e['raw_producer_header'],**META))
(OUT/'course_geometric_retained_proofs_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'original_seven_full_receiving_reads':7,'additional_full_provider_reads':1,'retained_complete_proofs':len(manifest),'new_events':len(new)}))
