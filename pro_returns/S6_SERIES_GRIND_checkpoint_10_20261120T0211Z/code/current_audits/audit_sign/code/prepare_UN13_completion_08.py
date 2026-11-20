"""Prepare UN13's current certificate guard and precise retained-scope proposal."""
from pathlib import Path
import csv,datetime as dt,hashlib,json
WORK=Path(__file__).resolve().parents[2];OUT=WORK/'audit_sign'
NOW=dt.datetime.now(dt.timezone.utc).isoformat()
WHO='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name,data):
    p=OUT/name;p.write_text(json.dumps(data,indent=2)+'\n')
    return {'path':str(p.relative_to(WORK)),'sha256':sha(p)}
label='cdp:st:C.2.UN.13'
evidence=json.loads((OUT/'II_95_exact_evidence_map_07.json').read_text())['records'][label]
events={e['event_id']:e for e in evidence['events']}
bodypath=WORK/'parts/II.body.linked.tex';body=bodypath.read_text()
old=r'''The construction is based on the classical Kummer
quotient. Its chart,
trace, Euler and cohomology calculations are retained
in \path{code/E_kummer_filling.py} and its output.'''
new=r'''The construction is based on the classical Kummer quotient.
The explicit invariant-character charts and transitions, descended
two-form coefficients, invariant and Gysin matrices, ambient and support
Betti vectors, quartic-block Euler changes and quadratic-normalization
inverse are computed in
\path{code/current_audits/audit_sign/code/UN13_current_exact_certificate_08.py}.
The complete output is
\path{code/current_audits/audit_sign/UN13_current_exact_certificate_08.json}.
These calculations use the finite-sheaf, relative-pair and
derived-pushforward maps proved above.'''
assert body.count(old)==1
guard_meta=save('UN13_current_certificate_guard_08.json',{'date_utc':NOW,'target':'parts/II.body.linked.tex','target_sha256':sha(bodypath),'guards':[{'label':label,'old_text':old,'new_text':new,'expected_count':1,'reason':'Replace the unavailable historical producer claim with the exact current executed321-check certificate, preserving the preceding full geometric proof and classical Kummer credit.'}],'certificate':{'code':'audit_sign/code/UN13_current_exact_certificate_08.py','code_sha256':sha(OUT/'code/UN13_current_exact_certificate_08.py'),'output':'audit_sign/UN13_current_exact_certificate_08.json','output_sha256':sha(OUT/'UN13_current_exact_certificate_08.json'),'stdout':'audit_sign/UN13_current_exact_certificate_08.stdout.txt','checks':321,'reading_order':'Authored after receiving proof access; no producer imported and no new whole-before-reading credit.'},'proof_transport':'audit_sign/UN13_original_to_current_proof_transport_08.json','remaining_gates':'Root integration of this one code-only guard and actual rebuilt full-row layout inspection.'})

source={
 'date_utc':NOW,'label':label,'reviewer':WHO,
 'fresh_primary_reading':{'key':'HuybrechtsK3Draft','url':'https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf','file':'audit_sign/primary_sources/Huybrechts_K3Global_author_08.pdf','sha256':sha(OUT/'primary_sources/Huybrechts_K3Global_author_08.pdf'),'locator':'Author prepublication draft Chapter1 Example1.3(iii), pp8–9. Entire passage and its continuation/commutative quotient square/canonical and H1 arguments were read.','exact_application':'Take the supplied abelian surface A over C. The source blows up its sixteen two-torsion points and takes the lifted involution quotient. The receiving strict surface P has exactly that quotient map: in the covering blowup chart(a,b)=(r,ru), the quotient coordinates are(R,u)=(r²,u). These charts commute with the identity on the open A/{plus-or-minus1} and glue the actual proper resolution. The source finite double-cover/averaging construction applies to this same surface. The receiving form da wedge db=(1/2)dR wedge du makes the canonical-line trivialization explicit. The original source diagram and this literal chart map supply the classical Kummer credit; the compact threefold quotient and its forty later blowups are retained in the receiving proof.'},
 'retained_source_event':events['ce:1b5252bbe70e694c9da9'],
 'retained_current_primary_event':events['S6_SERIES_GRIND_sign_source_HuybrechtsK3Draft_UN13'],
 'imported_geometry':{'UN3':'Actual inverse-map/common smooth-center modification supplies the uniruled exceptional-divisor argument; its separately opened AKMW source and its exact proper maps retain their own scope.','UN4':'Actual point/quartic vertical charts supply the20 blocks over each end, full support inverse images and smooth projective blowup maps. Their individual proof/source scopes are not promoted by the new arithmetic certificate.'},
 'credit_verdict':'The classical Kummer quotient is explicitly credited. The complete receiving compact family, multiplicities, cohomology maps, prescribed Euler-balancing and original-base persistence remain printed. Retained bounded AC26/Engel/DGKX source comparisons keep their exact recorded scopes; no unavailable historical comparison file is claimed reopened and no worldwide novelty or absence conclusion is added.',
}
source_meta=save('UN13_source_application_08.json',source)
with (WORK/'S6_SERIES_GRIND_inventory.csv').open() as f:row=next(r for r in csv.DictReader(f) if r['label']==label)
values={
 'credited_to':'The surface quotient is the classical Kummer construction, explicitly described in Huybrechts author draft Chapter1 Example1.3(iii)pp8–9. The receiving actual chart quotient of Bl_(A[2])A is that same surface. UN3 supplies the actual bimeromorphic noncontraction comparison and UN4 the vertical point/quartic operations. The complete threefold construction, full divisor multiplicities, ambient/support cohomology maps and prescribed forty-block refinement remain proved in the receiving statement.',
 'literature_searches':'Current Huybrechts primary opening/reopening is the author prepublication draft Chapter1 Example1.3(iii)pp8–9, full passage and quotient/canonical/H1 arguments; URL/hash and exact chart application in audit_sign/UN13_source_application_08.json. Retained ce:1b5252bbe70e694c9da9 records the broader037_UN13_primary_credit comparison of Huybrechts, AKMW, Peters, original AC26, Engel and both DGKX relative-cusp statements. The named historical report is absent from the supplied archive; its exact event/gate is retained without claiming it was reopened. No worldwide priority search is inferred.',
 'source_credit_verdict':'The actual Kummer quotient, lifted blowup involution, branched double cover and trace input receive precise classical credit. Retain the complete receiving compact-filling and modification proof. The current finite certificate is an exact calculation within that proof; its execution does not certify the full literature or add a new before-reading route.',
 'credit_transport':'The source quotient Bl_(A[2])A -> Km(A) is identified with the receiving strict surface P by the literal covering charts(a,b)=(r,ru) and quotient chart(R,u)=(r²,u), which commute with the identity away from the sixteen nodes. The descended two-form is(1/2)dR wedge du and the coherent H1 image lies in the minus-one invariants. In the threefold chart(a,b,s)=(r,ru,rv), the full base function is t=Rv², giving2P plus the exceptional plane; its normal transition is the square of the tautological one, O(-2). Twenty actual point/quartic blocks per end are disjoint from P. At their boundary crossings, pullback of xy through the two(x,z)-blowup charts is Ry and Ruy, so all relevant full reduced-divisor factors are retained. The quotient-pair/Gysin and derived Cartier maps are printed in Steps7,10,11. Finally adjoining s to the even-monomial ring gives the actual finite normalization C[a,b,s], with punctured inverse a=(as)/s,b=(bs)/s; these charts glue the stated quadratic-base-change map.',
 'literature_disposition':'Retain with complete proof and explicit classical Kummer credit. Every mathematical statement and all thirteen proof steps are byte-identical to the retained cp15 target before the proposed code-only replacement. Preserve the exact owner/ledger before-reading union and its historical file-availability limits; no single-owner fully blind claim is manufactured.',
}
retained_ids=['ce:0df83610e1758f9fd423','ce:c034590a661263ece2ca','ce:cd97efe1b8af5bf95d1f']
proposal={
 'date_utc':NOW,'label':label,'reviewer':WHO,
 'guarded_source_updates':[{'field':k,'old_value':row.get(k,''),'new_value':v} for k,v in values.items()],
 'retained_whole_step_union':[events[k] for k in retained_ids],
 'retained_three_check_gates':evidence['retained_explicit_three_check_gates'],
 'scope_reading':'The explicit aggregate event ce:0df83610e1758f9fd423 says all13 current steps have before-reading coverage from the frozen owner035 assertion route plus the independently frozen ledger residuals. The ledger event ce:c034590a661263ece2ca names only its exact Step2/4/5/7/9/10/13 residual scopes and discloses mixed-step exposure; it is not enlarged to a ledger whole-proof route. Other step-by-step owner paragraph assignments are not invented from missing historical files. The complete before-reading union is retained because the aggregate event and completed-row gate expressly record it, not because of an event-type label.',
 'current_full_receiving_event':events['ce:grind-sign:18fa5f9ef6e71af2'],
 'exact_current_to_retained_target':{'receipt':'audit_sign/UN13_original_to_current_proof_transport_08.json','sha256':sha(OUT/'UN13_original_to_current_proof_transport_08.json'),'mathematical_statement_byte_identical':True,'complete_thirteen_step_proof_byte_identical':True,'proof_sha256':'58f914d5469638c01f16f5bb941af20b578234f725014b5305eaf83828b53583','scope':'Before the pending current-code-only guard; StatementRecord/checks metadata is outside this comparison.'},
 'current_certificate':{'guard_receipt':guard_meta,'derivation_plan':'audit_sign/UN13_current_certificate_plan_08.md','output':'audit_sign/UN13_current_exact_certificate_08.json','checks':321,'scope':'All3 invariant quotient charts and9 ordered overlaps, every inverse/cocycle, all Veronese minors, full base-character multiplicities, the exact descended two-form coefficient/transition, invariant exterior/coherent dimensions,32 exceptional Gysin sections, support incidence/kernel matrices, all displayed ambient/support vectors, point/quartic reduced-divisor maps and Euler changes, and the actual quadratic-normalization generator/inverse maps. Geometric sheaf, formal-functions, relative-pair, derived-pushforward and noncontraction inputs remain the full receiving proof.','reading_order':'Written after receiving proof access and the current certificate plan. No old producer imported. This does not replace or enlarge the retained before-reading union.'},
 'source_application':source_meta,
 'layout_before_guard':{'receipt':'audit_sign/II_95_visual_QA_06.json','actual_old_sample_pages':[580,584],'current_build30_row_pages':[581,582,583,584,585],'scope':'Old build23 actual sample only; no current whole-row inspection yet.'},
 'remaining_gates':['Root acceptance/integration of the one truthful current-code guard.','Actual rebuilt full UN13 row inspection with current PDF/image hashes.'],
 'completion_recommendation':'After the exact integration and full-row QA tasks, recommend this row alone done at the expressly retained thirteen-step union and current receiving/source/computation scopes. No shared body, inventory or canonical assessment is edited here.',
}
proposal_meta=save('UN13_completion_proposal_08.json',proposal)
md=['# UN13: current certificate and exact completion proposal','',
 'The entire current mathematical statement and its thirteen-step proof are byte-identical to the cp15 source before the proposed code-only replacement. The retained target proof SHA is `58f914d5469638c01f16f5bb941af20b578234f725014b5305eaf83828b53583`. The current321-check standard-library certificate replaces the unavailable `E_kummer_filling.py` claim at exactly the stated finite chart/trace/Euler/cohomology scope.','',
 '## Retained before-reading scope','',proposal['scope_reading'],'',
 'The complete owner/ledger target union is explicitly recorded in `ce:0df83610e1758f9fd423`; the residual event is `ce:c034590a661263ece2ca`. Their exact unchanged outcomes and completed-row gates appear in the JSON proposal. The historical owner1065, separate post-target8 and ledger67 calculations remain the distinct retained event `ce:cd97efe1b8af5bf95d1f`. Their named files are absent from the supplied bundle, and no new opening/replay is claimed. The current full thirteen-step receiving comparison is `ce:grind-sign:18fa5f9ef6e71af2`.','',
 '## Current executable scope','',proposal['current_certificate']['scope'],'',
 'The universal chart derivation identifies the invariant character lattice explicitly, supplies every reciprocal chart map and its cocycles, and proves the quotient chart rings through their actual quadratic generators. The two-form comparison retains its one-half coefficient and the sign of the other chart. The degree-two support kernel uses the actual sixteen exceptional curves and their rational orthogonal complement, with the explicit projection x+(1/2)sum(x.Ci)Ci. No substitute numerical intersection lattice is introduced.','',
 'At the four quartic boundary intersections the two full-divisor charts are Ry and Ruy, with all coefficients one. The stratum Euler change, proper-map Euler change and alternating cohomology increment all equal−2. The current base-change certificate retains the literal inverse on s nonzero and the monic integral equations for a and b. The preceding geometric proof supplies finite trace, formal functions, quotient pairs, derived Cartier pushforward and noncontraction.','',
 '## Source credit','',source['fresh_primary_reading']['exact_application'],'',source['credit_verdict'],'',
 '## Remaining publication tasks','',
 'Root applies the one current-code guard. The current build30 row spans pages581–585; after the new paragraph is integrated, the exact rebuilt full row will be inspected. The old visual evidence is only the recorded build23 sample pages580/584. No current whole-row layout claim or canonical completion is made yet.']
(OUT/'UN13_completion_report_08.md').write_text('\n'.join(md)+'\n')

ep=OUT/'CHECK_EVENTS_additions.tsv'
with ep.open() as f:rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
new_events=[
 {'statement_id':label,'date':NOW,'who':WHO,'type':'computation or formal certificate','outcome':'New after-reading standard-library UN13_current_exact_certificate_08.py PASS321 checks: all3 quotient charts/9 ordered overlap maps and every cocycle; exact invariant characters, Veronese minors, base multiplicities and two-form factor; invariant cohomology, ambient/support Gysin/kernel maps and all Betti vectors; full point/quartic boundary maps, three matching Euler calculations and quadratic-normalization inverse/integrality maps. Universal map derivation in UN13_current_certificate_plan_08.md. No old producer import; no new before-reading credit. Sheaf averaging, formal functions, relative-pair topology, derived pushforward and global noncontraction remain the separately recorded full proof.','event_id':'S6_SERIES_GRIND_sign_UN13_exact_certificate_08','phase':'current'},
 {'statement_id':label,'date':NOW,'who':WHO,'type':'used and rechecked in this run','outcome':'Read the entire Huybrechts author-draft Chapter1 Example1.3(iii)pp8–9 passage/continuation, its blowup-involution quotient square and canonical/H1 arguments. Matched the same abelian surface and literal covering(r,u)->(R=r²,u) chart to the receiving P, retaining the one-half two-form and averaging map. URL/hash/application in UN13_source_application_08.json. Complete current mathematical statement and13-step proof are byte-identical to cp15, exact proofSHA58f914d5469638c01f16f5bb941af20b578234f725014b5305eaf83828b53583; transport receipt saved. This source/target comparison awards no new before-reading proof or broader literature claim.','event_id':'S6_SERIES_GRIND_sign_UN13_source_transport_08','phase':'current'},
]
ids={r['event_id'] for r in rows};rows.extend(r for r in new_events if r['event_id'] not in ids)
with ep.open('w') as f:wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');wr.writeheader();wr.writerows(rows)
print(json.dumps({'guard':guard_meta,'source':source_meta,'proposal':proposal_meta,'events':len(rows)},indent=2))
