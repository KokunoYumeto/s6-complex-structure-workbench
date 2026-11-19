from pathlib import Path
import re,json,csv,hashlib
A=Path(__file__).resolve().parents[1];root=A.parents[1];src=root/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15'
front=(A/'frontmatter_II.tex').read_text()
body='\n'.join((src/f'S6_10_PAPERS_{p}.tex').read_text() for p in ['II','VI'])
labels=set(re.findall(r'\\label\{([^}]+)\}',body))
main=[]
for letter in 'ABCDEFG':
 m=re.search(r'\\paragraph\{Theorem '+letter+r' \(([^\n]+)\)\.\}',front)
 start=front.index('\\hypertarget{main-II-'+letter+'}')
 end=front.find('\\hypertarget{main-II-',start+1)
 if end<0:end=front.index('\\subsection{The proofs in outline}',start)
 statement=front[start:end]
 os=front.index('\\hypertarget{outline-II-'+letter+'}')
 oe=front.index('\\end{enumerate}',os)
 outline=front[os:oe]
 steps=[]
 for sm in re.finditer(r'\\item\\hypertarget\{step-II-'+letter+r'-(\d+)\}\{\}([\s\S]*?)(?=\\item\\hypertarget|\Z)',outline):
  targets=list(dict.fromkeys(re.findall(r'\\hyperref\[([^]]+)\]',sm[2])))
  assert all(x in labels for x in targets),(letter,targets)
  steps.append({'number':int(sm[1]),'anchor':f'step-II-{letter}-{sm[1]}','body_targets':targets,'claim_tex':sm[2].strip()})
 assert 3<=len(steps)<=7
 main.append({'letter':letter,'title':m[1] if m else '', 'label':f'series:II:{letter}', 'main_anchor':f'main-II-{letter}','outline_anchor':f'outline-II-{letter}','body_labels':list(dict.fromkeys(re.findall(r'\\ref\{([^}]+)\}',statement))),'steps':steps})
(A/'frontmatter_II_map.json').write_text(json.dumps({'paper':'II','main_theorems':main,'rung_grouping':{'old_II_1_2_3_7':'A','old_II_4_5':'B','old_II_6_9_and_VI_sign_equality':'C','old_VI_local_comparison':'D','old_II_8':'E','old_II_10_11_12':'F','old_II_13':{'CDP98_local_freeness_divisor_twist':'A','comb_vector_fields':'F','theta_formula':'E'},'old_II_14':'G','old_II_15':'Results not yet established: inv:E2.3; proved tangent/Kuranishi content is F'},'editorial_scope':'Seven consolidated main statements; no blanket current-run proof certification. Literature statuses require the series-wide source matching before any new-result claim.'},indent=2)+'\n')
patches=[{'paper':'II','label':'ii:LR:covering','old':'the specified\nlogarithmic vector $a=e_4/4$, and its fixed line character.','new':'the specified\nlogarithmic vector $a=e_4/4$, its fixed line character, and\nthe retained periodic cusp fan with its source and line attachment maps.','reason':'The global two-turn endpoint proof uses the retained periodic cusp fan and its exact cap attachments; the theorem header should carry that choice explicitly.'}]
(A/'proposed_patches.json').write_text(json.dumps(patches,indent=2)+'\n')
assert patches[0]['old'] in (src/'S6_10_PAPERS_II.tex').read_text()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'
events=[
('cdp:st:C.2.UN.1','targeted proof check','Re-derived pair-sequence ranks, skew middle-intersection parity, Wang sequence and general orthogonal Cayley-transform parity after deriving an independent reduced-SNC intersection proof before reading the printed proof. Arbitrary-multiplicity tube proof agrees. No fault found; current reading is same model family.'),
('cdp:st:C.2.UN.1','computation or formal certificate','independent_sign_checks.py builds exterior squares by exact 2x2 minors for 120 independently generated SL4(Z) matrices; every fixed-space dimension is even and wedge pairing preserved. Finite auxiliary checks, not a substitute for the general proof.'),
('cdp:st:C.2.UN.2','targeted proof check','Blind exceptional-replacement derivation gives 2(m-k), and the printed horizontal-surface chain supplies the successive genus-two centres. Checked plane leaves and total-space Betti formula. No fault found.'),
('cdp:st:C.2.UN.4','targeted proof check','Blind derivation of Euler change (r-1)e(C), point +2, quartic -4 and total (Delta b2,Delta b3,Delta b4)=(2,6,2); compared every printed blowup chart, multiplicity transport, cohomology map and cofinality step. No fault found.'),
('cdp:st:C.2.UN.14','targeted proof check','Blind derivation of preservation of non-uniruled normalization multiset through strict-transform bimeromorphisms; read and compared five printed steps, explicit exceptional rulings, valuations and compact simultaneous modifications. No fault found.'),
('cdp:st:C.2.UN.36','computation or formal certificate','independent_sign_checks.py computes exact invariant wedge Gram forms for all four displayed oriented unipotent cases: dimensions/signatures (6;3,3,0), (4;1,1,2), (4;1,2,1), (4;2,1,1). This event checks the linear-algebra table only; the geometric integral-transfer homomorphism is outside its scope.'),
('cdp:st:D.2.3','targeted proof check','Opened original Steenbrink journal-text reproduction at Proposition1.13 pp233-234 and section2.1/Theorem2.18/Proposition2.20/Theorem2.21 pp234-239. Matched analytic hypotheses and re-derived relative-log residue comparison, nilpotent-layer spectrum a/gcd(m_i), equivariant zero map, and logarithmic/power positive-volume contradictions. No Kähler premise introduced; original PDF unavailable, reproduced journal text opened.'),
('cdp:st:D.2.3','computation or formal certificate','independent_sign_checks.py enumerates joint monomial kernels for all 216 positive multiplicity triples with entries1..6, agreeing exactly with powers a*(m_i/gcd), 1<=a<gcd. Finite verification complements the all-integer proportional-exponent argument.'),
('cdp:st:D.2.5','targeted proof check','Wrote analytic reduction from extracted dependency statements before reading printed proof, then checked all seven printed steps: fixed all-twists Cartier layer, rational-Betti smooth-support exclusion via actual étale root cover, all-powers Gauduchon degree, nonzero conductor, vertical resolution and D.2.3. No fault found. Its named dependency statements retain their separate proof obligations.'),
('ii:LR:covering','targeted proof check','Derived exact lattice, u-turn tau->tau+1, Albanese modulus shift1/2 and central two-turn conjugacy from attached Liu-Rollenske Lemma2.7, Corollary2.8, Proposition3.6 and Definition3.7 before reading current proof. Then checked intrinsic fibration reconstruction, global square-root divisor, root commutator, endpoint norm and cusp period identity. Proposed explicit retained-fan scope in statement; actual PaperIV cap morphisms retain their separate checks.'),
('ii:LR:covering','computation or formal certificate','independent_sign_checks.py independently verifies root deck order and invariant lattice, cyclic cochain identity, q*j(q) coefficients from divisor sums and limit q*(j(q)-j(-q))=2. Confirms local numerical/algebraic identities only.'),
('night:P3K.36','computation or formal certificate','Exact independent arithmetic: S=1 gives historical polynomial0; (J,Hhat,chihat)=(2,1,1/2) gives receiving expression-2=26 mod28. This verifies the stated numerical discrepancy; geometric input and fan formula require their separate PaperIV proof records.')]
with (A/'CHECK_EVENTS_additions.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome','event_id','phase'])
 for lab,typ,outcome in events:
  uid='ce:grind-sign:'+hashlib.sha256((lab+typ+outcome).encode()).hexdigest()[:20]
  w.writerow([lab,'2026-11-19',who,typ,outcome,uid,'current'])
coverage=[]
for n in range(1,87):
 label=f'cdp:st:C.2.UN.{n}'
 status='Targeted full proof check completed' if n in [1,2,4,14] else 'Displayed exact linear-algebra table checked; geometric transfer remains to check' if n==36 else 'No new full proof check recorded in this audit yet'
 coverage.append({'label':label,'current_audit_scope':status})
(A/'UN_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
print(json.dumps({'main_theorems':len(main),'outline_steps':sum(len(x['steps']) for x in main),'validated_step_targets':sum(len(x['body_targets']) for m in main for x in m['steps']),'events':len(events),'patches':len(patches)},indent=2))
