"""Preserve full current-reader course-provider checks without erasing older events."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/maps_audit'
SRC = ROOT / 'sources/codex_workspace/courses/CG-S6/src'
META = dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17')

RECORDS = [
 ('framing-invariant', 'the-original-six-dimensional-framing-invariant.md',
  'Read and rederived all 1386 lines, including both solved exercises. Checked the quaternion covers and the unstable-to-stable factor two; complete tangent-normal matrices; local and product framing parities; finite quadratic and Gauss identities; the rank-drop derivative defect and real-blowup compactification of unordered double points; the explicit one-double-point model; the tube comparison and middle-homology quadratic law; embedded representatives by adding a null Whitney sphere and removing pairs; both exact middle-homology sequences for index-three surgery, primitive belt lattice and the full L-perpendicular/L comparison; framed surgery preparation and index reduction; the specified product invariant and conditional Pontryagin–Thom conclusion.',
  'No internal contradiction found. The final framed-nullbordism conclusion additionally depends on the separately audited Pontryagin–Thom and integral stable-stem providers, and the handle reductions depend on the explicitly listed geometric providers. Reading this receiving proof does not certify those imported proofs.',
  ['the-original-integral-stable-group-and-its-completion-maps.md', 'framed-manifolds-and-the-pontryagin-thom-map.md', 'framed-handle-slides-and-index-one-removal.md', 'removing-the-original-zero-and-top-handles.md', 'integral-handle-chains-and-signed-incidences.md', 'rearranging-the-original-framed-handles.md', 'relative-morse-functions-and-original-handles.md'],
  'Michel–Weber 1409.0704v1 lines 620–779 and Snaith 1001.4751v1 lines 1218–1281, 1440–1488: original archives retrieved; operative source comparison not yet read at this event.'),
 ('receiving-whitney', 'whitney-moves-in-the-receiving-dimensions.md',
  'Read and rederived all 607 lines and both examples. Checked the complement dimension inequalities for (5,2,3), (6,2,4), (6,3,3); complete corner strips and rounded disk collar; metric-dependent mixed normal projections; endpoint orientation signs; the Spin(4) lift and full-rotation correction; full adapted normal-frame filling; transverse dilation and tangential shear for the complete sheet-coordinate germs; the supported ambient flow, its exact critical time and intersection signs; the normal quotient, every cutoff derivative, and thick attaching-tube transport.',
  'The printed six-dimensional receiving calculations are internally consistent. The earlier complete belt-complement construction, relative embedded-disk perturbation, corner-disk parametrization and boundary-collar extension remain explicit imported proof dependencies. The ambient isotopy moves the attaching sheet; the second sheet is retained as a comparison and is not falsely assumed pointwise fixed by the ambient flow.',
  ['belt-sphere-complements-and-the-whitney-disk.md', 'whitney-move-with-controlled-support.md', 'rearranging-the-original-framed-handles.md'],
  'Benedetti 1907.10297v1 original-author TeX lines 15077–15409: retrieved, comparison not yet read at this event.'),
 ('higher-slides', 'higher-index-framed-slides-and-chain-maps.md',
  'Read and rederived all 411 lines, including both worked integral examples. Checked the full framed corridor and crossing field; the sign h=(-1)^(k-1) sigma; the actual comparison diffeomorphism; the prism correction T=F_*−boundary(Pbar)−Pbar(boundary) which fixes the old lower sublevel; the filtered chain map with T_k=U^(-1), U=I+hE_ji; both adjacent differential formulas D_k_new=D_k U and D_(k+1)_new=U^(-1)D_(k+1); ordered products, inverses and all mixed elementary-matrix terms.',
  'The actual comparison and both adjacent integral chain formulas are consistent. Signed algebraic basis comparisons are distinguished from an orientation-reversing geometric move. Exact ambient patch transport, belt complements and the integral handle-chain comparison remain imported proofs requiring their own reads.',
  ['rearranging-the-original-framed-handles.md', 'belt-sphere-complements-and-the-whitney-disk.md', 'integral-handle-chains-and-signed-incidences.md', 'framed-handle-slides-and-index-one-removal.md'],
  'Durst–Geiges–Kegel 1811.09055v1 original handle-homology.tex: retrieved; whole 987-line primary source comparison not yet read at this event.'),
 ('middle-realization', 'realizing-framed-handles-and-middle-cancellation.md',
  'Read and rederived all 693 lines and both examples. Checked exact collar comparison retaining tangential shear and positive normal factor; the variable-height roof and original radii; the full Morse function f=c−A+B, coordinate change and df(X)>0; seam and corner smoothing; exact outgoing variable-flow collar and normal quotient; the actual same-level bijection between reduced intersections and trajectories; escape of every other unstable trajectory to the retained lower level; compact disjoint support neighbourhoods; supported cancellation; and the finite simply connected cobordism reductions in dimensions six and seven with the explicit final product flow and inverse.',
  'No internal contradiction found. Its cancellation theorem has now been independently read in full in the additional Morse provider. The zero/top/index-one reductions, arrangement and handle-chain foundations remain separately listed imported proof dependencies. This result does not assert that an arbitrary sphere clutch extends over a disk.',
  ['removing-the-original-zero-and-top-handles.md', 'framed-handle-slides-and-index-one-removal.md', 'integral-handle-chains-and-signed-incidences.md', 'rearranging-the-original-framed-handles.md', 'relative-morse-functions-and-original-handles.md'],
  'Laudenbach 1307.2545v1 §§1–3, Benedetti 1907.10297v1 lines 15077–15409, and Durst–Geiges–Kegel 1811.09055v1: exact primary comparisons pending at this event.'),
 ('supported-morse', 'morse-cancellation-with-controlled-support.md',
  'Read and rederived all 369 lines, both solved exercises and the local counterexample. Checked the relative Morse coordinate lemma including Schur-complement mixed terms; relative rectification tangent to the prescribed submanifold; the precise unique-orbit, escape and support hypotheses; construction of the complete descending disk and its nonlevel cap; global relative disk coordinates; the increasing minorant h1 and cutoff bound rho*K<1; every off-axis derivative including the varying radius; exclusion of extra critical points throughout the supported deformation; end-index cases with empty blocks; and the final relative product diffeomorphism.',
  'The full printed supported cancellation argument is checked at its stated hypotheses, permitting other critical points outside the specified support. It does not claim a unique birth–death time along the entire deformation. The finite polynomial counterexample correctly demonstrates the failed cutoff bound; finite arithmetic is not a substitute for the written support argument.',
  [],
  'Laudenbach 1307.2545v1 original theorem and full proof comparison still pending; this receiving proof has been read independently.'),
 ('spin-six', 'spin-six-and-the-framing-comparison.md',
  'Read and rederived all 444 lines and both examples. Checked the Toeplitz compact-defect and Fredholm-family construction, finite-dimensional stabilization and kernel bundle, index of a projection loop and the inverse Bott map; clutching and unitary stability in the needed dimensions; the explicit exterior-square SU(4)→SO(6) double cover; the real fixed-space basis and exact positive Euler formula e=(x1+x2)(x1+x3)(x1+x4)=c3 when c1=0; tangent clutch as the SO(7) connecting generator; pi5 SO(7)=0; and the actual stable and rank-six bundle comparison maps for a given homotopy six-sphere.',
  'The full printed bundle arguments are consistent in the required compact Hausdorff sphere setting. The earlier polynomial Bott-generation and integral characteristic-class providers have already been read. The signed diagonal proof of e(TΣ)[Σ]=chi(Σ) used for the rank-six comparison and nontriviality must still be read separately; the rank-seven framing conclusion itself does not require that particular Euler calculation.',
  ['tangent-index-with-torsion-line-bundles.md'],
  'Classical Spin/Bott/Euler source credit and exact original-source scope remain separate from these complete printed calculations.')
]

events = []
for key, name, scope, outcome, deps, credit in RECORDS:
    p = SRC / name
    lines = p.read_text().splitlines()
    events.append(dict(event_id=f'new-course-provider-{key}-full-20261117',
                       source=str(p.relative_to(ROOT)), source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                       locator=f'{p.relative_to(ROOT)}:1–{len(lines)}', line_count=len(lines),
                       raw_producer_header=lines[2], producer='GPT-6 Astra (OpenAI)', producer_effort='Ultra',
                       producer_date=('11 October 2026' if key=='framing-invariant' else '10 October 2026' if key in {'receiving-whitney','higher-slides','middle-realization'} else 'October 2026'),
                       full_proof_read=True, scope=scope, outcome=outcome,
                       remaining_imported_proof_dependencies=deps, original_source_comparison=credit,
                       numerical_program_rerun='not yet rerun by this event', **META))

dest = OUT / 'course_geometric_provider_full_checks.json'
old = json.loads(dest.read_text()) if dest.exists() else []
known = {r['event_id'] for r in old}
old.extend(r for r in events if r['event_id'] not in known)
dest.write_text(json.dumps(old, ensure_ascii=False, indent=2)+'\n')

hist = OUT / 'check_events.json'
history = json.loads(hist.read_text())
known = {r.get('event_id') for r in history}
history.extend(r for r in events if r['event_id'] not in known)
hist.write_text(json.dumps(history, ensure_ascii=False, indent=2)+'\n')

pending_path = OUT / 'course_geometric_dependencies_pending.json'
pending = json.loads(pending_path.read_text())
pending.setdefault('original_pending_snapshot', pending['pending'])
by_name = {Path(r['source']).name:r for r in events}
current=[]
for original in pending['original_pending_snapshot']:
    r=dict(original)
    if r['source'] in by_name:
        e=by_name[r['source']]
        r.update(status='Full receiving-provider proof read; imported dependencies separately tracked',
                 checked_event=e['event_id'], remaining_imported_proof_dependencies=e['remaining_imported_proof_dependencies'])
    current.append(r)
pending['pending']=current
pending['additional_provider_events']=[e['event_id'] for e in events if e['source'].endswith('morse-cancellation-with-controlled-support.md')]
pending['status_note']='This current list updates the original seven-file snapshot without erasing earlier recorded pending states. Complete closure of the Theta6 derivation has not yet been claimed.'
pending_path.write_text(json.dumps(pending, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'saved_events':len(events),'fully_read_original_seven':sum(x['source'] in by_name for x in current),'additional_full_read_providers':1},indent=2))
