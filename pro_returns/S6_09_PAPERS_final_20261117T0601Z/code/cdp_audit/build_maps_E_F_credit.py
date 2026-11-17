"""Bounded, per-result credit comparisons; not a worldwide novelty assertion."""
import csv,hashlib,json,re
from pathlib import Path
ROOT=Path('/workspace/scratch/037cd144174c')
OUT=ROOT/'deliverables/work/cdp_audit/maps_credit'
PLAN=json.loads((OUT/'search_plan_55.json').read_text())
SEARCH=json.loads((OUT/'searches_55.json').read_text())
BY={(r['source_id'],r['baseline']):r for r in SEARCH}
EA={r['source_id']:r for r in json.loads((ROOT/'deliverables/work/cdp_audit/maps_E/result_audit.json').read_text())}
META={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
REFS={r['key']:r for r in json.loads((ROOT/'deliverables/work/cdp_audit/maps_E/references_verified.json').read_text())}
CONTEXTS={
 'AC26':{'controlling_source':'sources/original/AC26_original_manuscript.pdf','search_index':'sources/external/root/AC26_pdf_text.txt',
         'previous_actual_contexts':'deliverables/work/cdp_audit/credit_context_readings.json#AC26',
         'locators':['Theorems 7.17 and 7.22, original pp.57 and 60: original rank-four torus-fibred threefold topology','Theorem 9.1 and Propositions 9.11–9.13: original threefold canonical and direct-image data','Section 10 and Appendix A: rank-four monodromy/coinvariants and ambient normal-crossing cusp'],
         'scope':'The controlling original pages and their complete proof scopes were read in the prior CDP audit, retained in that ledger. This event reuses those scoped readings and executes fresh per-result PDF-text searches; it does not claim all new broad-word hits were read.'},
 'E26':{'controlling_source':'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
        'locators':['Original construction/main theorem source lines225–335 (previously read)','Additional remarks source lines1640–1760 (reopened completely in this event), including the Seifert quotient, period comparison and broader six-dimensional construction'],
        'scope':'The original source was searched in full. The listed context readings distinguish the original complex threefold and proposed quotient from the actual repaired map and the new higher-dimensional receiving constructions.'},
 'DGKX_v1':{'controlling_source':'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
            'locators':['Introduction lines310–373 and tangent/Kuranishi theorem loci retained in the CDP context ledger','Root-stack/cusp/direct-image scopes lines8541–9364, independently opened in the invariants_arithmetic source ledger'],
            'scope':'Whole source independently searched. The exact direct-image/cusp antecedents are credited as inputs, not equated with a fourfold or shifted-product theorem. No full receiving E/F conclusion was identified in the queried and reviewed contexts.'},
 'DGKX_v2':{'controlling_source':'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex',
            'locators':['Introduction lines210–360 and section/theorem inventory, previously opened in the CDP audit'],
            'scope':'Whole source independently searched, separately from v1. Period-relative compactification, Oka maps and threefold modifications are related methods. The omitted v1 tangent theorem is not silently assigned to this edition; no rank-six survivor or shifted-manifold result was identified in the bounded comparison.'}}
(OUT/'context_readings.json').write_text(json.dumps({'reader':META,'contexts':CONTEXTS,'limits':'All matches are preserved, including irrelevant uses of general words. A saved hit is not a claim that every surrounding proof was read. The comparison asserts only the exact positive scopes and bounded absence described.'},ensure_ascii=False,indent=2)+'\n')

matches={}
def found(sid,baseline,locator,comparison,relation='partial_known_input'):
    matches.setdefault(sid,[]).append({'baseline':baseline,'relation':relation,'locator':locator,'comparison':comparison})

for sid in EA:
    found(sid,'AC26','Original Theorems7.17 and7.22, pp57 and60; the marked threefold construction in §§4–7',
          'The starting sphere family, rank-four period lattice, finite order-three/four fillings and original cusp are prior construction inputs. The receiving row concerns an additional fourfold, shifted product, complement, return map or framed attachment; the full receiving conclusion is not stated by these original theorems.')
    found(sid,'E26','Original construction/main theorem; additional remarks, source lines1640–1760',
          'The original elliptic-surface construction and its sphere fibres are credited. The Seifert quotient discussion is antecedent motivation; the actual map used by the receiving proof is the separately repaired PaperI map. The broader-construction remark concerns six-manifolds and does not supply the receiving higher-dimensional or marked-complement conclusion.')

for sid in ['E.2.1','E.2.19']:
    found(sid,'DGKX_v1','§6 root-stack, cusp-normalization, structure direct images and vertical geometry, source lines8541–9364; exact scopes in invariants_arithmetic reference ledger',
          'The rank-four sphere-family root descent, coherent direct images and normalized cusp geometry are known antecedents. The receiving fourfold invariants or complete relative smooth six-chart plumbing are additional calculations, whose full statements are not identified here.')
for sid in ['F.2.7','F.2.24','F.2.28','F.2.31','F.2.32']:
    found(sid,'AC26','Original §§6–7, especially Theorem7.17 p57 and Theorem7.22 p60',
          'The rank-four two-root affine van Kampen and integral-topology calculations are known. This row treats the specified rank-six construction, its additional affine data or three-point case; do not present the basic quotient/clutching method as new.')
    found(sid,'E26','Original logarithmic-transform construction and broader-family remark, source lines1738–1760',
          'Logarithmic modification of the torus fibration and broader examples are existing methods. The exact rank-six statement, full kernel computation or eight-manifold homology is not supplied by the original six-dimensional remark.')
for sid in ['F.3.1','F.3.2','F.3.3']:
    found(sid,'E26','Original indefinite period-domain remark, source lines1723–1736',
          'The original rank-four period mapping has a monodromy-invariant form of type(1,6) and indefinite Hodge signature(1,1). This is a lower-dimensional antecedent; it neither supplies the rank-six parity/rank obstruction nor the universal LSAP period existence conclusion.')

e_refs={
 'E.2.1':['ffJiaMeng','ffEsoleKang','ffPetersSterk'],
 'E.2.3':['rootScott83'], 'E.2.8':['rootHirsch76'],
 'E.2.9':['rootScott83','rootDavisKirk01','IsaksenWangXu2023','rootHirsch76'],
 'E.2.10':['mapsWinter08'], 'E.2.13':['rootScott83'],
 'E.2.18':['mapsWhitehead50'], 'E.2.21':['mapsVogel09','mapsMilnor65']}
for sid,keys in e_refs.items():
    for key in keys:
        r=REFS[key]
        found(sid,'elsewhere',f"{key}: {r['locator']}",r['verification'])
for sid in ['F.2.7','F.2.31','F.2.32']:
    found(sid,'elsewhere','Scott1983, Theorems2.3–2.5 pp425–426, orbifold Euler/sign calculation pp427–428; Section3 Euler covering formula Theorem3.6 pp435–436',
          'The spherical/Euclidean/hyperbolic classification and the Seifert covering method are established background. A sphere with three genuine cone points is good; sign of its orbifold Euler characteristic selects the universal model. F31 computes the additional BA-fibration kernel and finite transfer itself; F32 constructs its particular logarithmic family and homology itself.')
found('F.2.36','elsewhere','Bley–Hofmann–Johnston2022, hypothesis(H) p2, Theorems3.4 p6 and4.5(b) p9; Theorem7.9 p20; Algorithm8.3 and correctness p21; Theorem8.4 pp22–23; exact original opened by /root, work/root/references_verified.json key rootBHJ22',
      'The effective principal-ideal/lattice-isomorphism algorithm is a published input and must be credited. The receiving proof supplies the nilpotent-centralizer reduction, split-factor bound in this six-dimensional class, opposite-algebra conversion and integral lift criterion. This event preserves the root reader’s exact source scope and does not claim a second full reading of the BHJ paper.')

standard={
 'E.2.2':'The transversality/preimage argument and the Kunneth calculation are standard formal deductions, written out in full. No literal published receiving statement was identified in the bounded four-baseline comparison. This row should be described as a background derivation, not as a new general theorem.',
 'F.2.3':'The interior blowup changes homology while preserving the boundary. This is the classical blowup mechanism applied to refute an insufficient-data assertion; it is not a new blowup theorem. It does not refute the later fixed-Kuhn-filling classification.',
 'F.2.2':'Cyclotomic factorization and the even real-eigenspace criterion are standard linear algebra; the finite degree-six enumeration is the receiving calculation, not a new theorem on roots of unity.',
 'F.2.22':'The use of an order, trace dual and conductor interval is standard arithmetic methodology. The receiving proof supplies its explicit terminating per-input algorithm and primitive rank-six extension treatment; no new general lattice-finiteness principle is asserted.'}

result=[]
for item in PLAN:
    sid=item['source_id']; ms=matches.get(sid,[]); first=item['source_blocks'][0]
    title=item['statement'].split('\n',1)[0]
    row={'source_run':'S6_04_MAPS_MANIFOLDS','source_id':sid,'source_title':title,
         'source_status':'Refuted' if '(Refuted:' in title else 'Proved',
         'source_file':first['source'],'source_lines':first['lines'],'source_blocks':item['source_blocks'],
         'proof_sha256':first['block_sha256'],'reader':META,
         'comparison_method':'220 actual whole-file scans for55 source results, four baselines independently queried; bounded context readings and exact positive source matching. Negative searches assert no worldwide priority.',
         'matches':ms,'standard_background_note':standard.get(sid,''),
         'own_full_proof_check':EA[sid]['status'] if sid in EA else 'Not claimed by this credit-only event. Full receiving proof belongs to /root; exact detailed record work/root/maps_F_proof_audit.md.',
         'proof_outcome':EA[sid]['status'] if sid in EA else 'Use the parent-owned F proof/program ledger; this row records credit only.'}
    for baseline in ['AC26','E26','DGKX_v1','DGKX_v2']:
        scan=BY[(sid,baseline)]; positive=[x for x in ms if x['baseline']==baseline]
        row['found_in_'+baseline]={'status':'found_antecedent_in_checked_scope' if positive else 'not_found_in_scoped_comparison',
            'full_statement_found':False,'terms_searched':scan['terms_searched'],
            'search_record':f'deliverables/work/cdp_audit/maps_credit/searches_55.json#{sid}|{baseline}',
            'searched_files':[{'path':scan['source'],'sha256':scan['source_sha256'],'hit_count':len(scan['matches'])}],
            'actual_reading_scope_record':f'deliverables/work/cdp_audit/maps_credit/context_readings.json#{baseline}',
            'matches':positive,
            'relation':' '.join(x['comparison'] for x in positive) if positive else 'No full matching receiving statement was identified in the saved result-specific queries and the explicitly reviewed contexts. All hits remain available; this does not claim that every broad-word context or the entire external literature was read.'}
    elsewhere=[x for x in ms if x['baseline']=='elsewhere']
    row['found_elsewhere']={'status':'found_known_inputs' if elsewhere else 'not_found_in_scoped_comparison','full_statement_found':False,'matches':elsewhere,
        'cited_opened_inputs':e_refs.get(sid,[])+(['rootScott83'] if sid in ['F.2.7','F.2.31','F.2.32'] else [])+(['rootBHJ22'] if sid=='F.2.36' else []),
        'actual_scope':'Only the operative original-source groups listed here and the four attached baselines were compared. No additional worldwide search or full-statement novelty claim is asserted.',
        'standard_background_note':standard.get(sid,'')}
    row['novelty_classification']='No priority claim; exact known inputs and bounded full-statement comparison recorded'
    row['route']='Preserve complete receiving proof with precise known-input credit; no full duplicate located in this scoped comparison'
    if sid=='E.2.2':row['route']='Background or known-derivation appendix, retaining its complete short proof; do not style the general transversality/Kunneth argument as new'
    if sid=='F.2.3':row['route']='Keep as an explicit insufficient-data counterexample, with the classical interior-blowup mechanism credited as background'
    row['credited_to']='; '.join(x['locator']+': '+x['comparison'] for x in ms)
    result.append(row)

for prefix,name in [('E.','E_credit_comparison_22'),('F.','F_credit_comparison_33')]:
    rr=[r for r in result if r['source_id'].startswith(prefix)]
    (OUT/(name+'.json')).write_text(json.dumps(rr,ensure_ascii=False,indent=2)+'\n')
    fields=list(dict.fromkeys(k for r in rr for k in r))
    with (OUT/(name+'.csv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()} for r in rr)

for r in EA.values():
    r['credit_status']='Completed bounded four-baseline and operative-original comparison; no global priority assertion'
    r['credit_record']='deliverables/work/cdp_audit/maps_credit/E_credit_comparison_22.json#'+r['source_id']
    if r['source_id']=='E.2.10':
        for e in r['dependency_records']:
            if e['source_id']=='MAPS B5.2':e['scope']='Complete cap/peripheral receiving proof, event new-maps-B-remaining-full-20261117:B.5.2. All11 B certificates were then read/rerun unchanged with exact retained-output agreement, in work/maps_audit/maps_B_remaining_program_manifest.json; maps_cw run scope is in maps_B_remaining_program_runs/maps_cw.run.json.'
ep=ROOT/'deliverables/work/cdp_audit/maps_E/result_audit.json'
ep.write_text(json.dumps(list(EA.values()),ensure_ascii=False,indent=2)+'\n')
fields=list(dict.fromkeys(k for r in EA.values() for k in r))
with ep.with_suffix('.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()} for r in EA.values())

scott={'source_ids':['F.2.31','F.2.32'],'reader':META,'status':'verified in the specified scope',
       'receiving_read_scope':['fourfolds_vankampen.tex lines135–245: orbifold BA-fibration and three-point kernel application','fourfolds_three_point.tex lines84–155: actual logarithmic gluing, Seifert group and hyperbolic fibre injection'],
       'original':REFS['rootScott83'],
       'additional_original_read':'Reopened original pp425–428: Theorems2.3–2.5, full bad-orbifold proof, orbifold Riemann–Hurwitz and curvature/Euler-sign comparison.',
       'match':'A sphere with three genuine cone points of orders at least2 is good by Theorem2.3. Theorem2.4 supplies S2/E2/H2 universal models and pp427–428 select them by Euler sign. Thus pi2 of the classifying space vanishes in the plane cases; the spherical orbifold cover gives the separately computed integral transgression. For F32, 1/5+1/4+1/m<1 for every m>=2, so its circle-fibration pullback is the trivial circle bundle over H2 and the central fibre injects. The receiver computes its exact Euler sign and group relations independently.',
       'limits':'This verifies only the specified F source application. Root owns the full291-line/265-line receiving proofs and their complete algorithms; this event does not duplicate those audits.'}
(OUT/'Scott_F_application_check.json').write_text(json.dumps(scott,ensure_ascii=False,indent=2)+'\n')
rp=ROOT/'deliverables/work/cdp_audit/maps_E/references_verified.json'
refs=json.loads(rp.read_text())
for r in refs:
    if r['key']=='rootScott83':
        r['uses']=list(dict.fromkeys(r['uses']+['MAPS F2.31 good three-cone orbifold universal model','MAPS F2.32 hyperbolic Seifert base and infinite central fibre']))
        r['additional_application_record']='deliverables/work/cdp_audit/maps_credit/Scott_F_application_check.json'
rp.write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
print('Saved22 E and33 F per-result matrices;220 searches and exact Scott F scope retained.')
