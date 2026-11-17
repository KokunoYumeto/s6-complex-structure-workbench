"""Refresh scoped audit records without changing source status or deleting checks.

This is bookkeeping, not a proof verifier.  Every event describes work actually
performed; arithmetic reruns are deliberately separated from geometric checks.
"""
from pathlib import Path
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/maps_audit'
CODE = ROOT / 'deliverables/code/maps_audit'
READER = {'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
          'effort':'Pro', 'date':'2026-11-17'}
FABLE = {'reader':'Claude Fable 5.2 (Anthropic)',
         'effort':'high', 'date':'2026-11-16'}
SURVEY = {'reader':'Claude Fable 5.2 (Anthropic)',
          'effort':'high', 'date':'2026-11-12'}

def dump(name, obj):
    (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
def export_csv(name, rows):
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f, fieldnames=keys);w.writeheader()
        for r in rows:
            w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ids(prefix, lo, hi): return [f'{prefix}.{n}' for n in range(lo,hi+1)]

events_path=OUT/'check_events.json'
events=json.loads(events_path.read_text()) if events_path.exists() else []
def event(key, results, scope, outcome, actor=READER, locator=None, dependencies=None):
    if any(e['event_id']==key for e in events): return
    events.append(dict(event_id=key, results=results, **actor, scope=scope,
        outcome=outcome, locator=locator or '', remaining_dependencies=dependencies or []))

def mids(v): return ['MAPS:'+x for x in v]
def pids(v): return ['PUSH:'+x for x in v]
review='sources/reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md'
event('prior-fable-full-maps-20261116',mids(['A.3.1','F.2.5','F.3.4','F.3.5','F.3.6','F.4.1']),
      'Full proofs read, as expressly listed by the reviewer. Source theorem openings were not part of this reading.',
      'Recorded outside reading/check retained with its stated limits.',FABLE,review+': introduction lines 7–24 and §3',
      ['The reviewer explicitly did not verify F.2.6 torsion differentials, Kuhn cusp filling, or Nagy source.'])
event('prior-fable-partial-maps-20261116',mids(['A.3.2','F.2.6']),
      'A.3.2 statement and setup; first half of F.2.6, not its torsion differential proof.',
      'Partial recorded outside check; no full-proof certification inferred.',FABLE,review+': introduction and §3')
event('prior-fable-statements-b6-20261116',mids(ids('B.6',16,22)),
      'Statements only of B.6.16–B.6.22; Jin paper not opened by that reader.',
      'Recorded statement review; not a proof check.',FABLE,review+': introduction and §3')
event('prior-fable-tuple-rerun-20261116',mids(['F.2.5']),
      'Independent exact verification of tuple, Smith factors, affine freeness, Seifert determinant and exterior-square identity (F.11).',
      'Passed in the recorded output.',FABLE,
      'sources/reviews/S6_FINAL_INTAKE_20261116/checks/f25_check.py; f25_check.out; INTAKE_FINAL.md §3')
event('prior-fable-full-pushc-20261116',pids(ids('C.3',21,24)+['C.3.27']),
      'Full proof readings of these five statements. C.3.10, C.3.14 and C.3.18 were expressly not read.',
      'Recorded outside check retained; dependencies not thereby certified.',FABLE,review+': introduction and §1')

transferred=['A.1.1','A.1.2','A.1.3','A.2.1']+ids('A.3',1,4)
event('new-circle-real-full-20261117',mids(transferred),
      'Full statements and proofs read and rederived; all exact matrix/fixed-point verifiers rerun. Quotient smoothing, local nonextension, cusp origin and real-locus arguments checked. Full proofs transferred once to Paper I.',
      'Candidate proofs supplied. Lattice d versus complex period e type error repaired; no change in theorem conclusion.',
      locator='paperI_circle_quotient.tex; paperI_real_forms.tex; associated manifests; selected_reruns.json',
      dependencies=['FAMILY geometric existence and marked period conventions are companion inputs.',
                    'Smith theorem is opened in Knudson Theorem 4.1; equivariant triangulation realization remains a standard background input.'])
event('new-maps-homotopy-read-20261117',mids(['A.2.2']+ids('B.1',1,2)+['B.2.1']+ids('B.3',1,3)+['B.4.1']),
      'Full arguments read and rederived: stable framing, degree-twelve weighted Hopf factor, retained-angle Arf class, angle-forgotten cone nullhomotopy and conical wedge.',
      'Internal arguments checked; source matches not yet complete.',
      dependencies=['Toda/APS exact low-stem normalizations','Named-family geometric identifications in B.4.1'])
event('new-maps-cw-read-20261117',mids(['B.5.1']),
      'Full CW/mapping-cylinder construction read; exact cell count and cusp comparison examined.',
      'Candidate-specific argument read; Waldhausen exact theorem remains to be opened.',
      dependencies=['Waldhausen Theorem 6.1'])
event('new-maps-fixed-conifold-read-20261117',mids(['B.6.16','B.6.18','B.6.19','B.6.20']),
      'Full four proofs read and rederived, including free-circle conifold model, Jin invariant identification, spin trace, and actual cubic collar computation. Associated arithmetic reruns pass.',
      'Jin Proposition 3.1, Lemmas 2.1/4.4/4.8 and Theorem 4.9 opened and hypotheses compared. Final global conclusion still depends on remaining B.6 chain.',
      dependencies=['B.6.17 actual Pontryagin computation','B.6.21–25 final/general twist comparisons'])
event('new-fourfold-read-20261117',mids(['E.1.1','E.1.2','E.1.3','E.1.5']+ids('F.1',1,4)+['F.2.1','F.2.5','F.2.6']+ids('F.3',4,11)+['F.4.1']),
      'Full proofs of listed statements read except the still unresolved geometric d2 identification in F.2.6. Exact matrix, discriminant, period and LSAP-tube programs pass. The actual LSAP bundle-section theorem, Nagy inertia theorem and Jin statements have been opened.',
      'Scoped progress, not a complete-chain certification. F.3.11 gives bounded correction at one retained cusp; it does not establish simultaneous good reduction at every finite puncture.',
      dependencies=['F.2.6 geometric torsion transgressions','Chen rank-three cusp comparison','Mandal almost-complex criterion','Forstneric–Prezelj relative section theorem','Wall/Nikulin classification normalization'])
event('new-fourfold-partial-read-20261117',mids(['E.1.4','F.2.2']),
      'Partial proof readings only.', 'In progress; no full proof check inferred.')
event('new-manifold-small-read-20261117',mids(['D.2.2','D.2.3']),
      'Bounded-computation scope and Euler/clutching sensitivity argument read in full. D.2.2 depends on supplied local-model database and is explicitly not an independent validation of all geometric attaching maps.',
      'Euler argument rederived. Full engine job rerun and database geometric audit remain separate.',
      dependencies=['D.2.2 exact fifty-input computation and attached model database'])

readpush=['C.3.5','C.3.10','C.3.14','C.3.15','C.3.18','C.3.20','C.3.21','C.3.22']
event('new-pushc-read-20261117',pids(readpush),
      'Full proofs read and rederived: actual cusp closing, annular reduction, characteristic cap, affine stable-frame defect, actual cubic and delta-line square, and common signed cap. Exact symbolic programs rerun.',
      'Actual-origin identification gap closed; remaining external topological comparison sources explicitly listed.',
      locator='closing_origin_check.tex; selected_reruns.json; code/maps_audit/PUSH/code/*.audit_rerun.txt',
      dependencies=['C.3.14 Wall/Davis/Fintushel–Pao/Haefliger exact theorem hypotheses','C.3.18 relative Pontryagin normalization','C.3.23–27 full final comparison chain'])
event('new-actual-cusp-origin-20261117',pids(['C.3.5']),
      'Inserted actual FAMILY periods into the explicit closing: Pi_c g=(6mu,-s+C_c,21), ell=-s/12+kappa0, D=C_0,21-12kappa0. Derived bbar=(-hmu/2,-h(c+D)/12-h²/24)=sigma(c+h)-sigma(c), sigma=(-cmu/2,-c²/24-cD/12), c=-12v, in the actual fixed exponential chart. Toric unit extension and deck equivariance checked.',
      'Passed exact symbolic rederivation and independent parent check. Distinguished explicit representative from isotopic cohomological representative.',
      locator='closing_origin_check.tex; PUSH/code/d_push_closing.audit_rerun.txt')

working=json.loads((OUT/'working_results_inventory.json').read_text())
foundation=[x for x in working if Path(x['source_file']).name in ('integral_leray.tex','topology_reduction.tex')]
event('prior-A1-foundation-20261112',['WORK:'+x['source_id'] for x in foundation],
      'Survey reading, explicitly not a blanket verification. A1-10 direct-limit argument assessed correct pending Dimca; A1-11 collapse matrix annihilation and Smith forms checked; A1-12 same spine proof as AC26; A1-13 Smith/Phi/Delta1 determinant checked; A1-14 nearby-cycle rank bookkeeping redone, with degree-three Gysin and integral Dimca hypotheses left for full check.',
      'All these existing scoped checks retained.',SURVEY,
      'sources/notes/A1_notes__v3.md §§1.3–1.4 and A1-10–A1-14 (lines 370–432); effort from sources/reviews/WHO_WROTE_WHAT.md')
event('new-foundation-full-20261117',['WORK:'+x['source_id'] for x in foundation],
      'Both full source sections read step by step; nearby-cycle integral hypotheses opened and matched; stalk/Gysin/rank arguments, finite lattices as supplied, transgression signs, cellular collapse and HEP comparison rederived. Direct toric pi1 and compact-support local-coefficient proofs supplied. Every proof preserved in namespaced candidate blocks.',
      'Checked relative to the explicit parent-owned geometry and exact-lattice dependencies. False H3 transfer argument repaired separately. No new geometry certification implied.',
      locator='paperI_integral_leray.tex; paperI_topology_reduction.tex; paperI_topology_manifest.json; paperI_topology_labels.csv',
      dependencies=['Proper smooth analytic cusp and finite-filling construction','Parent exact invariant/coinvariant lattices and finite pullbacks'])
event('new-H3-correction-20261117',['WORK:prop:actual-finite-band-maps'],
      'Refuted the source alpha3=alpha1 assertion. Replaced its invalid H1/H3 pairing by same-degree Kronecker pairings and the integral degree-three pullback lattices. Explicit corrected alpha3, Smith factors and kernel rerun.',
      'Corrected alpha3 has rows (1,0,0,0),(0,-4,-2,1),(-2,0,0,0),(0,3,3,-1); Smith 1,1,1,0; kernel (0,1,1,6). H1/H2 sphere proof unaffected. This error is in the working edition, not AC26 Lemma 7.19.',
      locator='finite_degree_three_correction.tex; code/maps_audit/finite_degree_three_correction.py; source topology_reduction.tex lines 733–737,774–779')

# Later checks are appended rather than rewriting earlier records of open gaps.
event('new-illman-source-closed-20261117',mids(['A.3.4']),
      'Illman 1972 Theorem 3.1 was opened in the original scanned thesis and its compact-Lie-group and differentiable-action hypotheses matched to the smooth involution. Knudson Theorem 4.1(1) then applies to its finite-dimensional equivariant CW realization.',
      'The previously recorded equivariant-triangulation citation prerequisite is closed. The earlier event remains as a dated record of the audit state at that point.',
      locator='references_verified.json: Illman1972 and Knudson2004; paperI_real_forms.tex')
event('new-maps-B617-full-20261117',mids(['B.6.17']),
      'Full proof read and rederived: logarithmic cotangent sequence and Koszul critical-cycle formula, vanishing c1(L) and c2(V), p1=-2[Crit], and signed Euler contributions of the two actual critical components. The first contributes +2 and the second zero.',
      'The candidate-specific calculation gives p1(Q)=-4y. This closes the B.6.17 internal proof prerequisite recorded earlier; the final B.6 comparison chain remains separate.',
      locator='sources/returns/S6_04_MAPS_MANIFOLDS/sections/maps_fixed_quotient_tangent.tex lines 1–207',
      dependencies=['Actual conifold geometry and its identified critical components','Exact cited background sources for the logarithmic/Koszul formula remain tracked separately.'])
event('new-fourfold-actual-torsion-d2-20261117',mids(['F.2.6']),
      'Supplied a full independent cellular-prism proof of the three actual finite-boundary torsion differentials. The affine generator has an invariant normal coordinate; theta=a+4k gives primitive generators e_theta=(1,0), e_h=(-4,1). A torsion coinvariant w has norm zero, so its boundary cocycle has theta component w and fibre component zero. The Cech boundary is the global coinvariant [w], without a factor four. Independent integral order and global-residue tests rerun in degrees 2,3,4.',
      'The previously unexamined geometric torsion-transgression step is closed by a full proof and exact arithmetic checks. This is not certification of the independent rank-three cusp-existence and remaining Leray inputs.',
      locator='fourfold_torsion_transgression.tex; code/maps_audit/fourfold_torsion_transgression.py; .json; .rerun.txt',
      dependencies=['Rank-three Kuhn cusp construction and properness','Other F.2.6 stalk and global Leray groups; maximal cusp specialization'])
event('new-pushc-all-proofs-read-20261117',pids(['C.1.1','C.1.2','C.2.1','C.2.2','C.2.3']+ids('C.3',1,27)+['C.4.1','C.4.2','C.5.1']),
      'All 35 final Part C statements and their full source proofs have now been read. Internal arguments rederived, including equivariant division and gauge extension, cusp quotient and gradient deformation, normal Euler classes, weighted Hopf linking, marked product extension, relative frame and cubic calculations. The distinct C.3.24 orbit-knot and C.3.27 spin-c index proofs are retained separately. A full source read does not certify every imported theorem.',
      'Full internal proof readings complete for Part C. Exact arithmetic reruns and source checks retain their separate scopes; outstanding imported theorem checks are not relabelled as proved.',
      locator='sources/returns/S6_02_PUSH/sections/C_push.tex and its included C_*.tex files; selected_reruns.json',
      dependencies=['Remaining exact external statements for smoothing/isotopy, orbit-knot classification, and characteristic-index normalizations','Companion FAMILY/Paper I geometric construction and closing map'])
event('new-pushc-two-integer-proofs-20261117',pids(ids('C.3',23,27)),
      'Both final integer-level methods read and rederived in full. C.3.23 uses disjoint-support additivity before reduction modulo 28; C.3.25 constructs the eight-dimensional cap, accounts for its extra CP2 contribution and computes Q=((k,1),(1,0)), p1=(p+k,3), c^2=(k,1), and mu=(p-4k)/672. C.3.26 proves additivity of this characteristic index. Both use the same actual values p=-24 epsilon and k=-6 epsilon, but different conversion/additivity arguments.',
      'Both proofs avoid the invalid inference 6[Phi]=0 implies [Phi]=0 in Z/28: the divisible quantity is an integer which vanishes before reduction. Both full proofs must be printed or explicitly retained as separate proofs.',
      locator='C_equivariant_integer.tex; C_monodromy_value.tex; C_actual_eight_coboundary.tex; C_index_additivity.tex; C_independent_monodromy_value.tex; PUSH/code/e_push_C_{cap,cubic,attempts}.audit_rerun.txt',
      dependencies=['External index/smoothing source hypotheses remain separately scoped in reference ledger.'])
event('new-closing-transfer-I-20261117',pids(['C.3.5']),
      'Transferred the entire checked holomorphic closing construction and its full proof to Paper I, where PUSH B.4.18/B.4.24 use it. Actual even-shift origin reconstructed in FAMILY coordinates; exact ordinary, finite and cusp defects and the quadratic coherence term rederived and rerun.',
      'Print once in Paper I as push:src:C.3.5; Paper III cites it for smooth monodromy. DGKX v1 already proves the even-shift chart gluing and quadratic strictification and receives explicit credit.',
      locator='paperI_closing_cocycle.tex; paperI_closing_cocycle_manifest.json; closing_origin_check.tex')
event('new-working-kummer-full-20261117',['WORK:cusp-cover-extension-theorem','WORK:cusp-cover-naive-action-failure','WORK:cusp-cover-global-scope'],
      'Read all 442 source lines and rederived the scaled periods, toric power map, G=mu_N^2 invariant ring, normalization, nonflat fibre lengths, ramification, central component maps, and integral monodromy conjugacy. Repaired the improper assertion that whole affine charts have bounded logarithmic position by a uniform compact-subset estimate, then supplied the proper-discontinuity and properness argument.',
      'Full local construction checked with the attached compact-chart repair. The original global-scope remark is an earlier limitation; later MAPS C.1 results must be compared before it is stated as a present open problem.',
      locator='sources/workbench/cusp_toric_cover_completion.tex lines 1–442; kummer_compact_chart_repair.tex',
      dependencies=['Actual underlying toric cusp and fixed period conventions from Paper I','Later MAPS C.1.2–C.1.5 global comparison remains to be audited.'])

g2=[x for x in working if x['source_run'].startswith('course_') or x['source_id']=='G2-8']
event('prior-G2-survey-20261112',['WORK:'+x['source_id'] for x in g2],
      'Exact reader scope retained: lesson 11 and the sphere-twist chapter were read; the survey explicitly marks other prerequisite chapters and bordism invariance unread or partial. G2-8 adds a short almost-complex homotopy observation. This is not a blanket check of the course or every prerequisite.',
      'Prior reading preserved at its stated scope. Effort high is supplied by the survey row of WHO_WROTE_WHAT, not guessed from the note header.',SURVEY,
      'sources/notes/G2_notes.md §§1.2–1.4, G2-3–G2-8 and unread-work list lines 518–534; sources/reviews/WHO_WROTE_WHAT.md line 20')

dump('check_events.json', events)
byresult={}
for e in events:
    for r in e['results']: byresult.setdefault(r,[]).append(e)

maps=json.loads((OUT/'results_audit.json').read_text())
blocks=json.loads((OUT/'source_blocks.json').read_text())
for r in maps:
    es=byresult.get('MAPS:'+r['id'],[])
    r['check_event_ids']=[e['event_id'] for e in es]
    r['source_blocks']=[{k:v for k,v in b.items() if k!='text'} for b in blocks.get(r['id'],[])]
    prior=[e for e in es if e['reader'].startswith('Claude')]
    new=[e for e in es if e['reader'].startswith('GPT')]
    if prior:r['recorded_checks']=' | '.join(e['event_id']+': '+e['scope']+' ['+e['locator']+']' for e in prior)
    if new:
        r['your_check']=' | '.join(e['event_id']+': '+e['scope'] for e in new)
        r['audit_state']='scoped reading/rederivation recorded; see unresolved dependencies'
        r['audit_notes']=' | '.join(e['outcome'] for e in new)
    elif prior:r['audit_state']='prior scoped check retained; new full check pending'
    if r['id'] in transferred:
        r['printed_paper']='I';r['printed_label']='mapsI:src:'+r['id']
        r['audit_state']='full candidate proof supplied to Paper I; companion dependencies explicit'
        if not r.get('credit_checks'):
            r['credit_checks']='Scope-specific source comparison is recorded in source_credit_checks.json.'
export_csv('results_audit.csv',maps);dump('results_audit.json',maps)

pushfile=ROOT/'sources/returns/S6_02_PUSH/S6_02_PUSH_results.csv'
oldpush={x['id']:x for x in json.loads((OUT/'push_C_audit.json').read_text())} if (OUT/'push_C_audit.json').exists() else {}
push=[dict(x,**{k:v for k,v in oldpush.get(x['id'],{}).items() if k not in x}) for x in csv.DictReader(pushfile.open()) if x['id'].startswith('C.')]
for r in push:
    es=byresult.get('PUSH:'+r['id'],[])
    r['printed_paper']='III';r['printed_label']=''
    r['check_event_ids']=[e['event_id'] for e in es]
    r['recorded_checks']=' | '.join(e['event_id']+': '+e['scope'] for e in es if e['reader'].startswith('Claude'))
    r['your_check']=' | '.join(e['event_id']+': '+e['scope'] for e in es if e['reader'].startswith('GPT'))
    r['audit_state']='scoped checks recorded; see remaining dependencies' if es else 'full proof check pending; original source status retained'
    r['source_status']=r['status']
    if r['id']=='C.3.5':
        r['printed_paper']='I';r['printed_label']='push:src:C.3.5'
        r['audit_state']='full checked construction transferred to Paper I; companion inputs explicit'
        r['transfer_manifest']='paperI_closing_cocycle_manifest.json'
export_csv('push_C_audit.csv',push);dump('push_C_audit.json',push)

for r in working:
    es=byresult.get('WORK:'+r['source_id'],[])
    r['check_event_ids']=[e['event_id'] for e in es]
    if es:
        r['recorded_checks']=' | '.join(e['event_id']+': '+e['scope']+' ['+e['locator']+']' for e in es if e['reader'].startswith('Claude'))
        r['your_check']=' | '.join(e['event_id']+': '+e['scope'] for e in es if e['reader'].startswith('GPT'))
        if r in foundation:
            construction_closed=(OUT/'paperI_construction_full_checks.json').exists()
            r['check_outcome']=('Full checked proof supplied; every construction companion dependency now has a complete independent proof-read record.' if construction_closed else 'Full candidate proof supplied, with explicit geometry/exact-lattice companion dependencies.')
            if r['source_id']=='prop:actual-finite-band-maps':r['check_outcome']='Working-only H3 error corrected by the full checked integral transfer proof; AC26 already has the correct degree-three indices.'
            r['printed_label']='mapsI:top:'+r['source_id'] if not ':L' in r['source_id'] else 'mapsI:top:remark:'+r['source_id'].split(':')[-1]
            r['overlap_status']='AC26 known-result overlap checked; explicit maps and alternate proof retained with credit.'
        if r['source_id'].startswith('cusp-cover-'):
            r['check_outcome']='Full local proof checked with compact-chart properness repair; global final-run comparison pending.'
            r['proof_correction']='kummer_compact_chart_repair.tex'
dump('working_results_inventory.json',working);export_csv('working_results_inventory.csv',working)

for name in ['paperI_topology_manifest.json','paperI_circle_quotient_manifest.json','paperI_real_forms_manifest.json']:
    path=OUT/name;raw=path.read_text();raw=raw.replace('not independently exposed; not inferred','Pro');path.write_text(raw)

retry=CODE/'MAPS/code/manifolds_mapping_quotient.audit_rerun_2.txt'
rr=json.loads((CODE/'selected_reruns.json').read_text())
if retry.exists() and not any(x.get('attempt')==2 for x in rr):
    rr.append({'program':'MAPS/code/manifolds_mapping_quotient.py','attempt':2,'exit_code':0,
               'output':'MAPS/code/manifolds_mapping_quotient.audit_rerun_2.txt',
               'prerequisite':'Original attached records/explorer/api/engine copied unchanged; first failure retained.',
               **READER})
(CODE/'selected_reruns.json').write_text(json.dumps(rr,indent=2)+'\n')
print(json.dumps({'MAPS_rows':len(maps),'PUSH_C_rows':len(push),'working_rows':len(working),
                  'check_events':len(events),'foundation_rows':len(foundation)},indent=2))
