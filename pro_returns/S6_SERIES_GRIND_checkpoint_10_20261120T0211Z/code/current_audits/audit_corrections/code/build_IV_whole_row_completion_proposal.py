from pathlib import Path
import csv,json,hashlib,re,datetime
P=Path(__file__).resolve().parents[1];W=P.parent
s=(W/'parts/IV.body.linked.tex').read_text()
old=json.loads((P/'row_assessments.json').read_text())
events=json.loads((P/'IV_completion_input_events.json').read_text())
for r in csv.DictReader((P/'CHECK_EVENTS.tsv').open(),delimiter='\t'):
 if r['statement_id'] in events and not any(x['event_id']==r['event_id'] for x in events[r['statement_id']]):events[r['statement_id']].append(r)
known={r['label']:r for r in csv.DictReader((P/'IV_known_input_specializations.tsv').open(),delimiter='\t')}
scopes={
1:'Rational elliptic surfaces over C with section; torsion-free rank-one Mordell–Weil group; the eight OS91 rows and their21 realized Kodaira refinements.',
2:'The height formula of the cited Shioda theorem, its positive local-correction rearrangement, and primitive generators in the eight rows of F1.',
3:'Jin’s Torelli isotopy group of S2×S3, with the retained reverse-seam definition of k,ell and the positive p1=4 generator.',
4:'The explicit Hopf lift of a^n, its quaternionic D4×S3 extension and the specified outward-first sphere gluing.',
5:'The actual genus-three degree-twelve compact elliptic page, K=5F, and the normal Euler-class parity obstruction after removing a small ball disjoint from its section; the corrected class is K+2M.',
6:'The normalized curve b^3=a^4+1 and its two maps t=x=b^3 and t=t_*x/(x+t_*−1), with t_* outside{0,1,infinity}; original IV*/III/I1 source and pulled-back point line.',
7:'The AC26 reference sphere, literal e2 delta cocharacter, retained reference cusp triangulation, fixed opposite normal weights and actual conifold smoothing.',
8:'The positive parameter return of that reference sphere family, the equivariant tube trivialization and the oriented cut-and-reglue map to the typed Hopf lift.',
9:'The actual small-resolution charts, second nodal circle, fixed gamma marking and prescribed outer stable framing in the reference cusp model.',
10:'Original twists(0,1,−1), reference cusp fan, regular binding away0,1,infinity, actual physical line M=P−O and the stable boundary marking.',
11:'The equivariant normal framings of F7–8 and the integer Jin coordinates with the retained sixfold parameter and line comparison.',
12:'The actual component cover y^12=t^4/(t−1)^3, its specified I12 extension, identity-component translations, and physical point-P line modulo an integral fibre class.',
13:'The literal P2.2 angular origins, local XY=Qr resolutions and winding−12; the global application uses the separately proved real-trace/symbol/framing maps. No outer-corner descent equality is included.',
14:'B=P(L_+ direct_sum conjugate L_-), meridian-one hyperplane U, roots a,−b and inherited determinant D=pi*(d+a+b); the physical application uses the explicit U=M^-1 map.',
15:'The twelve labelled node charts with rho=Qr, full deck units and source translation−6P, retained unit roots, and central multiplicity12; the outer contraction is outside this local statement.',
16:'The labelled comb-smoothing parameter s of the cited source, on a sufficiently small punctured disc, with fixed real lattice and the actual single-valued radial attachment isotopies.',
17:'Coprime multiplicities(3k,4l), k,l positive, the reference fan and F10 regular-binding boundary marking; the actual degree12kl page and physical line.',
18:'The two named one-logarithmic source constructions in Viaclovsky and Liu–Rollenske, their actual order-four caps and degree-four regular-binding pages.',
19:'Yang’s attached repaired edition Type B/C boundary presentations, all admitted twists; the quotient maps z→0,x→1,y→−1 modulo gcd(m1,m2)=2 or3.',
20:'Wang’s specified primitive I2 filling, the literal monomial coordinate map and physical-circle isotropy2; global pi1/H2/H3 conclusions are cited from Wang, with the separate component-supported OS49 application.',
21:'Literal I7+III+I1+I1 source in the proof, M=O(7G−O), translation−2G, selected nodal zero, stated order-four affine cap and reference fan, lambda=r^4; page pair(−14,−72).',
22:'The outward-first Hopf gluing lambda and Jin’s reverse-seam coordinates; the surgery boundary is −lambda and the positive normalization is mu(lambda b)=+1/28.',
23:'The actual F21 source, point line, root and reference, lambda=r^4 with positive r-loop; full angular difference and fourth-root winding+4.',
24:'An oriented six-sphere return Phi with forward seam(x,1)~(Phi(x),0), the actual disc-supported representative and both spin structures of its mapping torus.'
}
# These are genuine remaining text requirements, not alleged mathematical defects.
scope_gates={
1:'State rational elliptic surfaces over C with zero section explicitly before the eight-row assertion.',
2:'Name F1’s eight configurations and display the exact height/intersection formula in the statement.',
5:'Name the actual degree-twelve genus-three page and the line/normal-Euler convention in the statement.',
6:'Put the two actual degree-twelve base maps and t_* restriction in the statement.',
7:'Name the reference AC26 sphere, fan and literal e2 circle in the statement.',
8:'Name the reference sphere family and positive parameter direction in the statement.',
9:'Name the prescribed reference cusp model, marked circle and outer framing in the statement.',
10:'Name twists(0,1,−1), reference fan, physical M and regular-binding convention in the statement.',
11:'Attach the integer-index statement explicitly to the F7–8 equivariant family and F3 conventions.',
12:'Name the actual component cover, I12 extension and physical point line in the statement.',
14:'Include the opposite-weight projective bundle, U line and inherited determinant in the statement.',
16:'Name the labelled comb parameter s and the small punctured-disc domain in the statement.',
18:'Name both source constructions and the retained order-four caps in the statement.',
21:'Include the literal source/reference fan and chosen affine-cap/linearization data by an exact local cross-reference.',
23:'Attach the positive r-loop to F21’s exact source/line/root/fan choices.',
24:'State the orientation-preserving return and the explicit forward seam in the statement.'
}
text_gates={
7:'Replace absent orbit_mv.py/orbit_mv.out assertions by the actual matrix/conifold method and the fresh61-check output; repair C_n^q caret notation.',
12:'Replace absent compact_torsor.py/torsor_schreier.py assertion by the freshly derived commutator and cover-character method, without a Schreier replay claim; repair q=Q^12,Q^n,A^0 notation.',
14:'Replace literal escaped caret text in spin^c and pi^* by mathematical TeX.',
15:'Repair the remaining literal rho^(-1) caret notation.',
21:'Replace the residual bare os47_topology.json mention by the supplied fresh142-check output at its actual scope.'
}
rows=[]
for label in [f'night:P3F.{n}' for n in range(1,25)]+[f'night:P3K.{n}' for n in (109,110,113,114,115,118)]:
 a=s.index('\\label{'+label+'}');b=s.index('\\end{proof}',a)+len('\\end{proof}');block=s[a:b]
 es=events[label]
 substantive=[r for r in es if r['type']!='used and rechecked in this run' or ('Renewed row-specific credit comparison' in r['outcome'])]
 isF='P3F.' in label
 gates=[]
 if isF:
  n=int(label.rsplit('.',1)[1]);k=known[label]
  if n in scope_gates:gates.append(scope_gates[n])
  if n in text_gates:gates.append(text_gates[n])
  c= {'confidence_state':'proved at the stated construction scope','confidence_line':('The complete retained re-derivation, receiving proof and source/map comparison agree for '+scopes[n]),'independent_routes':[k['opening_and_check_scope'],k['retained_map_or_calculation']],'remaining_risk':'No unresolved mathematical step identified in the stated proof. '+(' '.join(gates) if gates else 'No additional row-specific text defect identified.'),'format_check':None,'layout_check':None,'completion_state':None}
  credit={'credited_to':k['source_locator']+'; '+k['known_input'],'credit_transport':k['retained_map_or_calculation'],'source_credit_verdict':k['condition_4_4_2_disposition'],'literature_disposition':'Cited theorem/input with the stated family-specific map retained. This table makes no claim of worldwide absence.'}
  order='The retained S6_06 producing re-derivation and complete S6_10 receiving re-derivation remain credited. Their imported labels do not establish a new full before-reading derivation in this audit. Fresh computations listed here were written independently after receiving-proof reading.'
  if n in (3,19):order+=' The principal assertion is exactly source-known and is now cited with its short parameter/presentation specialization; no new proof of that source theorem is claimed.'
  if n==22:order+=' The second-model direct spin-c coboundary computation is retained as event ce:3f48670dfc59920169e5, with its exact stated source/orientation limits.'
 else:
  n=int(label.rsplit('.',1)[1]);c=dict(old[label]);c['independent_routes']=list(c['independent_routes']);c['format_check']=None;c['layout_check']=None;c['completion_state']=None
  c['remaining_risk']='No unresolved mathematical proof step identified at the exact hypotheses already recorded. The full proof and computations are present; all source/code workflow replacements were integrated before CP03. Complete recorded independent peer checks remain credited under prompt5.6. The current global build/layout and exact source-credit inventory update are editorial completion gates; this audit makes no new whole-proof blindness claim.'
  credit={'credited_to':'E26’s elliptic quotient and logarithmic-transform construction; the exact source/point-line/fan morphisms are recorded in iv:source_transports and IV_source_morphisms.tex. Shioda supplies the height laws; Jin supplies the characteristic/mapping-torus classification where used. The row’s endpoint/exhaustion statement was not located in the declared bounded source comparisons.','credit_transport':'Retain the literal E_r source, chosen marked node, M_a=O(aG−O), translation−bG, both signed norms, actual root progressions, full constants/characters/annular references and prescribed fan. The source, line and finite-cover maps are the complete EF/SEF/EB/R0E/ES/RJC proof maps named by this row.','source_credit_verdict':'Known construction and characteristic inputs credited; complete endpoint theorem assessed at its literal scope. No priority claim.','literature_disposition':'Retained49-source/1813-term comparison event plus IV_endpoint_completion_searches.json’s two recorded primary-arXiv discovery searches; bounded no-match for the exact full endpoint assertion.'}
  order={109:'Retained complete EF.1–8 root and period-module independent audits; the new full-primary comparison explicitly was not prewritten. Our separate centralizer prereading covers its named algebraic/geometric substeps. Named historical peer files are not supplied separately, so their recorded check is retained without claiming a fresh replay.',110:'Retained complete independent root audit. The received positive-linear/primitive/chronological-phase derivation precedes SEF.1–5; NE.1–4 was compared after reading. The fresh full-unit and annular checks do not claim full-prereading coverage.',113:'Complete retained EBR and EBP geometric proofs are printed. The primitive cyclic cover, quotient, affine inverse, degree-one elliptic map and three-fixed-point argument were independently derived before their comparison, as recorded in ce:2b87dd57340c50f1f78f.',114:'Complete retained root and source/fourfold peer proofs are printed. The quartic source/root map, finite III generator/period argument and degree-one j map were prewritten before the III proof, as recorded in ce:901462090c4726a5519a; the remaining full-reference/cap comparison was after reading.',115:'Complete retained ESP comparison proof is printed. Received prereading derived the endpoint/cover/fan/witness combination but selected a different preliminary page cover; comparison repaired that selection to t=tau+xi^(−m), as recorded in ce:13123ce8a47d0bba328b. The current full ES.1–6 review and new139172 checks agree.',118:'Complete retained JFP.1–12 derivation is printed. Our prewritten four page pairs, phase/divisor necessity and negative-annular target are preserved in IV_K118_additional_prereading.md. Its actual page/root/fan morphisms were then compared in the complete RJC proof; no whole new blind reproof is claimed.'}[n]
  scopes[n if False else 1000+n]=c['confidence_line']
 # No row is promoted by this proposal while the parent has frozen canonical assessment files.
 rows.append({'label':label,'mathematical_status':'proved at its recorded scope','scope':scopes[n] if isF else c['confidence_line'],'statement_proof_sha256':hashlib.sha256(block.encode()).hexdigest(),'numbered_steps':len(re.findall(r'\\item\b',block)),'recorded_evidence':[{'id':r['event_id'],'type':r['type'],'outcome':r['outcome']} for r in substantive],'derivation_order_record':order,'remaining_row_text_gates':gates,'ready_for_completion_after_parent_global_QA':not gates,'global_gate':'Apply exact source-credit fields, use the current assembled tags/uses/backlinks/reference report, and confirm the CP04 changed-page/render checks. No claim of having viewed every PDF page.','assessment_proposal':c,'inventory_credit_proposal':credit})
report={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Proposal only; CHECK_EVENTS and row_assessments are frozen for CP04. Full mathematical closure is distinguished from residual statement/computational provenance/typesetting gates. Retained independent checks count at their actual recorded scopes. No speculative or conditional theorem is added.','rows':rows}
(P/'IV_whole_row_completion_proposal.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
cols=['label','mathematical_status','scope','numbered_steps','ready_for_completion_after_parent_global_QA','remaining_row_text_gates','derivation_order_record','global_gate']
with (P/'IV_whole_row_completion_proposal.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
 for r in rows:w.writerow({k:' | '.join(r[k]) if isinstance(r[k],list) else r[k] for k in cols})
(P/'IV_low_F_inventory_credit_proposal.json').write_text(json.dumps({r['label']:r['inventory_credit_proposal'] for r in rows},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'rows':len(rows),'ready_after_global_QA':[r['label'] for r in rows if r['ready_for_completion_after_parent_global_QA']],'text_gates':[r['label'] for r in rows if r['remaining_row_text_gates']]},ensure_ascii=False))
