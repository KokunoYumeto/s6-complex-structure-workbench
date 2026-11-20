from pathlib import Path
import csv,json,hashlib,re
A=Path(__file__).resolve().parents[1];W=A.parent
rows=json.loads((A/'row_assessments.json').read_text())
inv={r['label']:r for r in csv.DictReader((W/'S6_SERIES_GRIND_inventory.csv').open()) if r['paper']=='II'}
tags=list(csv.DictReader((W/'S6_SERIES_GRIND_tags.tsv').open(),delimiter='\t'))
tm={r['label']:r for r in tags if r['paper']=='II'}
stat=sorted([r for r in tags if r['paper']=='II' and r['kind']=='statement' and r['page'].isdigit()],key=lambda r:(int(r['page']),r['number']))
body=(W/'parts/II.body.tex').read_text()
record_labels=re.findall(r'\\StatementRecord\{([^}]+)\}',body)
records=[];samples=set();ranges=set()
for label,a in rows.items():
 if label not in inv:continue
 r=inv[label]; t=tm.get(label,{}); start=int(t.get('page') or 0)
 pos=body.find('\\label{'+label+'}')
 following=[(body.find('\\label{'+lab+'}',pos+1),lab) for lab in record_labels if lab in tm]
 following=[(p,lab) for p,lab in following if p>=0 and p>pos]
 next_label=min(following)[1] if following else None
 end=max(start,int(tm[next_label]['page'])) if next_label and tm[next_label]['page'].isdigit() else start+3
 inspected={start,end}
 if end-start>=6:inspected.add((start+end)//2)
 samples|=inspected;ranges.update(range(start,end+1))
 eligibility='Mathematical comparison complete at the recorded scope; eligible for final format/source-disposition and rendered-layout completion'
 remaining=[]
 if label=='ii:LR:covering':remaining=['Apply the exact retained periodic cusp fan/source-attachment hypothesis guard; its current body is still missing this phrase.']
 if label=='night:P3K.36':
  eligibility='Explicit numeric refutation checked; whole geometric counterexample completion also uses the actual receiving IV fan/cap record'
  remaining=['Link the existing actual K74/K105 fan/cap evidence to the T2 value; this branch\'s fresh event only recomputes 0 versus26.']
 if label=='inv:E2.3':
  eligibility='Open mathematical problem, eligible only for completed final-part presentation of its exact remaining splitting gate'
  remaining=['The actual rank-three kernel splitting remains open; E15 proves the positive-comb tangent tuple and smooth Kuranishi germ.']
 records.append(dict(label=label,tag=t.get('tag'),number=t.get('number'),status=r['status'],eligibility=eligibility,current_tag_page=start,upper_enclosing_page=end,next_statement=next_label,required_source_scope=a['confidence_line'],remaining_before_whole_row_completion=remaining,layout_plan={'full_enclosing_page_interval':[start,end],'recommended_pages':sorted(inspected),'basis':'Statement page and next-statement boundary, with one middle page for long blocks. This is a requested inspection plan, not a claim that these pages were viewed.'},source_credit=r.get('credited_to','')))
opening=json.loads((A/'SOURCE_OPENINGS.json').read_text())
plan=dict(date='2026-11-19',reviewer='GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort',scope='95 Paper II rows from this branch:93 proved,1 false-as-stated correction,1 open problem. Current mathematical checks and imported checks keep their exact scopes. No blanket rendered-layout completion is assigned.',tag_map_sha256=hashlib.sha256((W/'S6_SERIES_GRIND_tags.tsv').read_bytes()).hexdigest(),body_sha256=hashlib.sha256((W/'parts/II.body.tex').read_bytes()).hexdigest(),source_openings_count=len(opening['sources']),source_openings_file='SOURCE_OPENINGS.json',records=records,unique_requested_pages=sorted(samples),full_enclosing_pages_count=len(ranges),layout_warning='Page numbers come from the current tag map. Recompute after every integrated text change. Earlier build12/build18 contact-sheet receipts and the root build21 p517 repair retain only their exact image/PDF scope; they do not certify every row.',source_disposition='The retained full proofs establish the displayed receiving forms, constructions, converses, exact maps or computed refinements. Known inputs are cited at the opened source loci. No claim of universal novelty is made; bounded inherited comparisons and new source openings retain their scope.')
(A/'II_completion_eligibility.json').write_text(json.dumps(plan,indent=2)+'\n')

patches=[]
def guard(label,old,new,reason,expected=1):
 count=body.count(old);assert count==expected,(label,count,expected)
 patches.append(dict(label=label,old_text=old,new_text=new,expected_count=count,reason=reason))
guard('ii:LR:covering','the specified\nlogarithmic vector $a=e_4/4$, and its fixed line character.',
      'the specified\nlogarithmic vector $a=e_4/4$, its fixed line character, and\nthe retained periodic cusp fan with its source and line attachment maps.',
      'The complete endpoint construction extends through this retained cusp fan; it is an actual theorem hypothesis, already used in the proof.')
guard('cdp:st:D.2.3',r'\cite[\S2.1, Theorem~2.18, \S2.19, Proposition~2.20 and'+'\n'+r'Theorem~2.21]{Steenbrink1976}',
      r'\cite[\S2.1, p.~234; Theorem~2.18, pp.~237--238; \S2.19 and Proposition~2.20, pp.~238--239; Theorem~2.21, p.~239]{Steenbrink1976}',
      'The opened original analytic comparison supplies these exact page locators; no extra Kahler hypothesis is imported.',2)
guard('cdp:st:D.2.3',r'\cite[Proposition~1.13 and proof of'+'\n'+r'Proposition~2.20]{Steenbrink1976}',
      r'\cite[Proposition~1.13, pp.~233--234, and proof of Proposition~2.20, pp.~238--239]{Steenbrink1976}',
      'Exact opened locations of the monomial/Koszul comparison used in the specialized argument.',2)
guard('cdp:st:E6',r'\cite[\S4, equations (4.3)--(4.5), and \S6]{Horikawa1974}',
      r'\cite[\S4, equations (4.3)--(4.5), p.~649; \S6, Theorem~6.1 and proof, pp.~660--661]{Horikawa1974}',
      'Opened original source confirms the map-deformation Cech framework and its H2-injection hypothesis; the receiving proof explicitly supplies its own torus lifting argument.',2)
(A/'II_guarded_scope_source_patches.json').write_text(json.dumps(patches,indent=2)+'\n')
credits={
 'cdp:st:E5':{'source_credit_verdict':'The locally free R1 direct image is the opened Viaclovsky cohomological-flatness input carried by E4. The displayed rank-two Kodaira-Spencer cup map and its critical-ideal comparison are proved in the receiving proposition.','credit_transport':'The global edge map uses R1g_*O and ordinary cup multiplication on a smooth torus, with the exact map (a,b)->b*u1-a*u2; torsion-freeness extends its zero section across special values.','literature_disposition':'Retain the short two-step receiving proof and the named E4 input.'},
 'cdp:st:E6':{'source_credit_verdict':'DGKX v1 Theorem6.12 and Proposition6.16 give the specified original family\'s Kuranishi line. Horikawa II section4 p649 and section6 Theorem6.1 pp660-661 supply the obstruction framework; Douady sections9-10 pp83-87 supply the graph/embedding/analytic comparison. The present statement addresses every rank-two torus fibration and nonreduced parameter germ by the displayed Artin lifting maps.','credit_transport':'The same torus fibre F is lifted over each small extension; its unobstructed constant Beltrami deformation and the displayed H1 surjection remove the actual map obstruction before relative Douady convergence.','literature_disposition':'Retain all eleven proof steps for this exact receiving form and credit the opened inputs. No generalization is inferred merely from matching dimensions.'},
 'cdp:st:E15':{'credited_to':'Viaclovsky2026Combs constructs the positive combs, admissible period sections and fixed-value smoothing families (Theorem1.1, sections7-9; equations7.1-7.3, Proposition7.3/Remark7.4 and the parameter-space construction). AC26 supplies the periodic hexagonal cusp model. The exact tangent tuple and smooth Kuranishi germ are proved by E15. Only the Kuranishi component of the earlier comb agenda is settled; inv:E2.3 retains its actual rank-three kernel splitting problem.','source_credit_verdict':'Known comb and cusp constructions remain credited. The displayed tuple (2m+1,8m+1,6m+1,0), actual miniversal period family and smooth8m+1 germ retain their complete proof.','credit_transport':'The invariant root-curve Hodge exact sequence, finite-character pushforward, exact cup/Kodaira-Spencer kernel and the actual period deformation map connect the cited comb construction to the receiving tuple. Those data do not determine the unresolved splitting of the rank-three kernel.','literature_disposition':'Retain all nine proof steps; replace the overbroad inventory claim that E15 settles all of inv:E2.3.'},
 'night:P4.58':{'credited_to':'Opened AC26 Theorem7.22 p60 and Corollary8.5 p64, and Engel2026 Proposition7.1 p17, supply the known Euler2 value for their specified families. The universal irreducible-or-normal-crossing classification is assembled from the exact printed P4/P4R lemmas.','source_credit_verdict':'The source-family Euler example is credited to AC26 and Engel. The full receiving classification retains its actual normalization and conductor proof, with bounded source comparisons recorded in SOURCE_OPENINGS.json.','credit_transport':'On each supplied source family, its torus/bielliptic supports have Euler0 and its specified rational-normalized fibre has Euler2. Substitution into the same Euler sum realizes the positive case; it does not replace the universal conductor classification.','literature_disposition':'Retain the five-step assembly and its imported classification dependencies.'},
 'ii:LR:covering':{'source_credit_verdict':'The original fourth-root action, central lattice and logarithmic vector are from Liu-Rollenske Lemma2.7, Corollary2.8, Proposition3.6 and Definition3.7. The degree-two endpoint correction is established by the literal scalar log period, exact quotient and full retained cusp/cap maps in this proof.','credit_transport':'The scalar is alpha=c*u, so one u-turn adds delta=2e3-e1 to e4 and delta/4 to a. The resulting quotient elliptic modulus obstructs one-turn closure. The full two-turn Hom/root/cochain maps and retained cusp fan prove the actual double-cover descent.','literature_disposition':'Retain the full corrective proof and make its actual cusp fan/source attachments explicit in the theorem header.'},
 'night:P3K.36':{'source_credit_verdict':'This is a correction of the historical S6 all-fan clause. The actual IV T2 fan/cap arrows give26, whereas the old polynomial at S=1 gives0.','credit_transport':'The degree-four page (H,chi)=(2,1) and degree-two quotient (J,Hhat,chihat)=(2,1,1/2) enter the explicit displayed expression, giving-2 mod28.','literature_disposition':'Keep the false-as-stated status, counterexample and exact corrected IV receiving target; retain actual geometric input credit.'}
}
(A/'II_source_credit_proposals.json').write_text(json.dumps(credits,indent=2)+'\n')
# Separate old locator repair for root's already integrated K111 block.
(A/'K111_postintegration_locator_guard.json').write_text(json.dumps([dict(label='night:P3K.111',old_text='The entire bounded Cox lift and its inverse are RFB.17.',new_text='The entire bounded Cox lift and its inverse are RFB.16.',expected_count=1,reason='RFB.16 displays the diagonal Cox lift and inverse; RFB.17 is the quaternion exterior map. The original receiving body had not yet applied this earlier proposed locator correction.')],indent=2)+'\n')
print(json.dumps({'rows':len(records),'statuses':{s:sum(r['status']==s for r in records) for s in sorted({r['status'] for r in records})},'unique_requested_pages':len(samples),'full_enclosing_pages':len(ranges),'source_scope_patches':len(patches),'credit_proposals':len(credits)},indent=2))
