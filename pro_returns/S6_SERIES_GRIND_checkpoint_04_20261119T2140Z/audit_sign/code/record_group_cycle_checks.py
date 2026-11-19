from pathlib import Path
import csv,json,hashlib
D=Path(__file__).resolve().parents[1]
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'
items=[
('cdp:st:C.2.UN.44','targeted proof check','Checked all fifteen steps after independent meridian/root-cover derivation. Verified gradient-flow retraction and uniform tail bound, exact meridian normal subgroup, all lifted meridians and relation module, actual etale gcd root, blowup fundamental-group maps, homotopy-colimit dual-complex quotient, exterior-algebra injection and finite-cover rank-two bound. Opened Kurdyka1998 Theorem(LI) p775 and Lojasiewicz1964 section3 Theorem2 p464. Final Euler identity uses UN39 and the checked UN11 trace formula at their stated scopes.'),
('cdp:st:C.2.UN.47','targeted proof check','Independently derived the finite-cover/genus-budget mechanism before comparing all eight steps. Checked the actual holomorphic finite tube cover, Stein disc, component fibre-product degrees and distinctness, elementary subgroup separation in the virtually abelian group, actual dual-complex quotient and the chi1/chi2 inequalities. UN44 and UN28 have separate current checks. No fault found.'),
('cdp:st:C.2.UN.46','targeted proof check','Checked all twelve steps after independent complement-lattice derivation: entire axis line charts, affine logarithmic edge maps, basis/logarithm changes, finite normal-product plumbing and its compact covering pieces, actual arbitrary-smoothing tubular comparison, injected semidirect product, closed-coframe torus action and precise fourth period. Checked two-component matrix multiplication and deck-group coordinate exchange. Compact two-component occurrence uses UN41/43 at their stated scopes; those constructions were not fully checked by this event.'),
('cdp:st:C.2.UN.57','targeted proof check','Checked all thirteen steps after the independent cycle criterion derivation: secondary angular primitivity, affine edge maps, lattice-injected necessity, coframe sufficiency, positive transverse sum, exact normal-constant adjustment, all-C-star positive period determinant, moving Hopf/ruled charts and their conjugate-end identifications. Proper closed-base gluing and ruled collar details use UN51/55 at their stated scope; no independent verification of every such dependency is claimed.'),
('cdp:st:C.2.UN.62','targeted proof check','Checked all nineteen printed composition steps after independent height/pruning derivation. Verified exact root/normal order, ordinary R1 frame and restriction maps, normalization incidence matrix, cycle-only canonical minimum, full-multiplicity base-differential orders and path heights, common-period leading coefficients, actual inverse-record restoration requirements, and the explicit four-triple-fibre plurigenus formula. UN60 root-stack pruning, inverse charts, boundary pushouts and properness bounds remain separately identified unchecked inputs; this is a full composition check, not a standalone certification of those constructions.')]
p=D/'CHECK_EVENTS_additions.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'));seen={r['event_id'] for r in rows}
for label,typ,outcome in items:
 eid='ce:grind-sign:'+hashlib.sha256((label+typ+outcome).encode()).hexdigest()[:16]
 if eid not in seen:rows.append(dict(statement_id=label,date='2026-11-19',who=who,type=typ,outcome=outcome,event_id=eid,phase='current'))
with p.open('w') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome','event_id','phase'],delimiter='\t');w.writeheader();w.writerows(rows)
c=json.load(open(D/'UN_coverage.json'))
for r in c:
 n=int(r['label'].split('.')[-1])
 if n in [44,47,46,57,62]:r['current_audit_scope']='All printed proof steps checked with exact scope and remaining inputs recorded in event and BLIND_DERIVATIONS'
 if n in [65,75]:r['current_audit_scope']='Full printed argument checked; UN46/57 cycle construction now individually checked on explicit UN41/43/51/55 dependencies; no blanket independent-chain certification'
(D/'UN_coverage.json').write_text(json.dumps(c,indent=2)+'\n')
s=json.load(open(D/'SOURCE_OPENINGS.json'));keys={r['key'] for r in s['sources']}
for r in [dict(key='Kurdyka1998',url='https://www.numdam.org/article/AIF_1998__48_3_769_0.pdf',reading='Published original opened',locators='Theorem(LI) p775; adjacent comparison with analytic case',statement_scope='UN44 local analytic gradient inequality with exponent below one; manuscript supplies compact patching and smooth-metric norm comparison.',refs=['turn802967809view0','turn369482347view0']),dict(key='Lojasiewicz1964',url='https://www.numdam.org/article/ASNSP_1964_3_18_4_449_0.pdf',reading='Published original opened',locators='section3 Theorem2 p464 with properties(a)-(c) of Theorem1',statement_scope='UN44 simultaneous compatible triangulation of finite analytic components and intersections in the real analytic total manifold.',refs=['turn802967809view1','turn369482347view1'])]:
 if r['key'] not in keys:s['sources'].append(r)
(D/'SOURCE_OPENINGS.json').write_text(json.dumps(s,indent=2)+'\n')
print(len(rows),'events')
