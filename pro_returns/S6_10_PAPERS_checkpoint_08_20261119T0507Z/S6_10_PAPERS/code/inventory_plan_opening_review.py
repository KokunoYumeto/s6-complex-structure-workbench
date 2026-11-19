#!/usr/bin/env python3
"""Preserve the focused plan-to-opening scope comparison, without new proofs."""
import csv
import datetime
import hashlib
import json
from pathlib import Path

W = Path(__file__).resolve().parents[1]
located = json.loads((W/'analysis/inventory_opening_ladders.json').read_text())
ladders = {x['id']:x for x in located['ladders']}
groups = []


def add(paper, item, ladder_ids, labels, reason='The opening states the grouped result and gives its coarse proof through the named complete receiving arguments.', disposition='covered'):
    ids = [f'{paper}.L{i:02}' for i in ladder_ids]
    groups.append(dict(plan_item=f'{paper}.{item}', paper=paper, ladders=ids,
                       original_main_labels=labels.split(), disposition=disposition,
                       scope_comparison=reason,
                       opening_locations=[dict(id=i,file=ladders[i]['file'],line=ladders[i]['line'],
                                               steps=ladders[i]['steps'],text_sha256=ladders[i]['text_sha256']) for i in ids]))

add('I',1,[4],'fam:src:B.2.1 fam:src:A.2.1 fam:src:A.3.1')
add('I',2,[5],'fam:src:B.2.2 fam:src:B.2.3')
add('I',3,[6],'push:src:E.1.2 fam:src:B.3.1')
add('I',4,[9],'fam:src:B.4.2 mapsI:src:A.3.2','The two real classes and their S3 fixed manifolds are proved through the actual reflection, quotient and meridian maps. The plan\'s arc-only phrase is corrected: one negative-imaginary form maps onto all RP1; the other nonempty images are the stated arcs.')
add('I',5,[2],'fam:src:C.1.1')
add('I',6,[3],'fam:src:C.2.3 ari:C.8.1 ari:C.8.2 ari:C.8.3 ari:C.8.4 push:src:E.4.1','The same exact radius is proved by the displayed division/annulus/local-Rouche ladder. The ARI C8.5 source row shares the fam:C2.3 conclusion; E4.1 is the separately checked Arb/analytic proof of that conclusion, not another main claim.')
assert 'ari:C.4.4' in ladders['I.L07']['references']
assert 'F_8&=49t^4' in ladders['I.L07']['text']
add('I',7,[7],'ari:C.4.2 ari:C.4.4','The revised seven-step ladder includes the exact five-value table, all five F4--F8 polynomials, the proper-order/gcd argument and every positive norm equation. The model map and distribution identity supply the coarse proof of each displayed specialization.')
add('I',8,[8],'ari:C.2.1')
add('I',9,[23,24],'ari:C.6.3 ari:C.8.15')
add('I',10,[10],'fam:src:F.1.1')
add('I',11,[11],'fam:src:F.2.2 fam:src:F.3.1')
add('I',12,[12],'fam:src:D.1.4 fam:src:D.1.6')
add('I',13,[13],'inv:A3.1 inv:A2.2')
add('I',14,[14],'inv:C1.1 inv:C2.1 inv:C3.3')
add('I',15,[15],'inv:A4.2')
add('I',16,[16],'inv:D4.5 inv:D4.1')
add('I',17,[18],'push:src:A.3.2 push:src:A.1.2 push:src:A.2.2')
add('I',18,[19],'push:src:B.4.19')
add('I',19,[20],'push:src:B.4.33 night:P2.2 night:P2.7 night:P2.9')
add('I',20,[21],'push:src:D.1.3')
add('I',21,[22,24],'push:src:D.2.3 push:src:D.3.1 push:src:D.4.8')
add('I',22,[4,5,17],'fam:src:A.5.1 fam:src:A.5.2 fam:src:B.4.1 push:src:E.2.1','The general classification and its standard-data two-class specialization appear in L04/L05. L17 gives tangent cohomology, Kuranishi and automorphisms with the actual root/period mechanism and explicit DGKX credit. fam:st:A.5.2 is the exact co-located source alias of fam:src:A.5.2.')
add('I',23,[25],'inv:C3.8 ari:C.7.4','The final ladder states the two precise open questions and their proved reductions; it asserts no conditional theorem or resolution of the remaining norm/atlas questions.','formal open scope, not an unfinished ladder')

ii_labels = {
1:'cdp:st:A.1.1',2:'cdp:st:B1',3:'cdp:st:A.4.9',4:'cdp:st:D.1.2',5:'cdp:st:C.3.1',
6:'night:P4.58',7:'cdp:st:C4f cdp:st:C4a cdp:st:C4b',8:'cdp:st:C5b',9:'cdp:st:D.2.5 cdp:st:D.2.7',
10:'cdp:st:E6 cdp:st:E7',11:'cdp:st:E13 cdp:st:E14 cdp:st:E15',12:'push:src:E.2.23 push:src:E.2.24',
13:'cdp:st:E12 cdp:st:E17 cdp:st:E18 inv:E2.4',14:'night:P3K.36',15:'inv:E2.3'}
for n, labels in ii_labels.items():
    reason='The opening states the grouped result and gives its coarse proof through the named complete receiving arguments.'
    disposition='covered'
    if n==5: reason='The current claim correctly says very general fibre; its five steps retain the integral CDP hypotheses and the exact component/monodromy exclusions.'
    if n==6: reason='Paper II states the irreducible/normal-crossings theorem and its complete local/global ladder; the unrestricted C2.G.1 main statement is assigned to Paper VI.'
    if n==7: reason='The plan\'s all-twist surjection was refuted at n=-1. The current ladder proves the exact full-fibre generic criterion and all-twist nonvanishing through its conductor injection; it makes no universal-surjectivity claim. C4a/C4b are grouped exact-sequence inputs.'
    if n==12:
        assert 'push:src:E.2.24' in ladders['II.L12']['references']
        assert 'finite local projection' in ladders['II.L12']['text']
        assert 'saturated diffeomorphism quotients' in ladders['II.L12']['text']
        reason='The revised seven-step ladder includes disc propagation, finite-projection/curve-normalization closure, the connected-family converse and the actual Kuranishi retraction and saturated clopen quotient passage. It now states the full two named main conclusions and cites their exact receiving labels.'
    if n==13:
        assert 'cdp:st:E18' in ladders['II.L13']['references']
        assert 'degree-six isogeny' in ladders['II.L13']['text']
        assert 'cdp:eq:E-theta-general' in ladders['II.L13']['references']
        reason='The revised six-step ladder states all four corrections. E18 is explicit through the half-period compact-torus family, its actual index-six identity-induced isogeny and the nonzero wp term in the full determinant formula. The original wp=0 branch and an additional linearization derivative retain their exact scopes.'
    if n==14: reason='The historical whole P3K36 fan compound remains Refuted. The actual fixed-data parameter conclusion is now the fully proved ii:LR:covering, and this ladder gives its Albanese comparison, odd/even return and full even attachment maps.'
    if n==15:
        reason='The remaining comb-kernel splitting data are explicitly Open, with the exact known tuple and unsolved morphism retained.'
        disposition='formal open scope, not an unfinished ladder'
    add('II',n,[n],labels,reason,disposition)

for n, labels in {
1:'maps:src:A.2.2',2:'maps:src:B.1.2',3:'maps:src:B.2.1',4:'maps:src:B.3.1',5:'maps:src:B.5.1',6:'maps:src:C.1.3',
7:' '.join(f'maps:src:D.1.{i}' for i in range(1,12)),
8:'maps:src:D.2.28 maps:src:D.2.44 maps:src:D.2.45 maps:src:D.2.46 maps:src:D.2.47 maps:src:D.2.48 night:P3F.34',
9:'maps:src:D.3.1 maps:src:D.3.2 maps:src:D.3.3',10:'maps:src:E.2.1 maps:src:D.2.4'}.items():
    reason='The opening states the grouped result and gives its coarse proof through the named complete receiving arguments.'
    if n==7: reason='The one cyclic-cover ladder explicitly retains d prime to six, the integral torsion, divisor ring, finite-coefficient cubic evaluations, integral p1 and complete Zhubr invariant. Intermediate D1.2/.3/.5/.7/.8/.10 are the cusp, character, ring, family-dependence and detection steps of that single conclusion; the complex member moduli are also in Paper I.'
    if n==8: reason='The seven-step ladder retains the initial marking, all 21 profiles, 59 patterns on 50 initial rows, exact integral cokernels and finite cubic/Pontryagin invariants. The OS49 noncoprime correction is explicit: the Gysin factors g and |n| remain, including (9,3,1) giving (Z/3)^2.'
    if n==10: reason='The five-step transverse-product proof gives the canonical class, algebraic dimension, class-C obstruction by the actual Hodge/Betti comparison and middle form. D2.4 is explicitly identified as the remaining classification question in the following scope paragraph.'
    add('III',n,[n],labels,reason)

add('IV',1,[1],'push:src:C.3.24','The reference class zero is obtained through the actual physical inverse-clutch transfer and the reference page/cap characteristic values, with the original fan/marking retained.')
add('IV',2,[1],'push:src:C.3.27 maps:src:B.6.24','The same reference value and the coprime extensions are grouped with the reference physical transfer. Independent historical proof routes are preserved in the complete body and their separate check records; they do not create multiple main statements.')
add('IV',3,[8,9],'night:P3K.31 night:P3K.33 night:P3F.35','The old norm-only polynomial is explicitly refuted by the actual original shorter loop at T2, where the answer is26 rather than0. The full source/line/native-prism algorithm replaces it, with all28 witnesses. Positive covers of the physical OS45 generator realize the separate all-class conclusion.','covered by proved correction of the plan')
add('IV',4,[9],'night:P3K.23','The actual two-ruling native map and physical-line dictionary give the corrected multiplier7A_M. The rejected -5 physical interpretation is expressly refuted.','covered by proved correction of the plan')
add('IV',5,[9,10],'night:P3K.10 night:P3F.21 night:P3K.22','The physical classes are OS45=3 and OS47=4. The former is a unit modulo28, and the actual positive parameter cover composes the return. The plan\'s former values25 and24 are not printed as current physical values.','covered by proved correction of the plan')
add('IV',6,[8,10],'night:P3K.30 night:P3F.53','The original natural-page scalar baseline is the physical H/2-chi, transported through the exact dual-line/inverse-clutch map. The current grouped table retains distinct original/shorter parameter loops, fans, cap progressions, norms, characters and endpoints. The full thirty-branch table and corrected local K30 proof remain in the body; the broader source and OS49 constructions use their complete replacement algorithms.','covered by corrected family/scalar table and exact algorithms')

add('V',1,[1],'maps:src:F.2.5 maps:src:F.2.6','The complete integral lattice, primitive cusp and order-four boundary map give the three-connected eight-manifold; the coefficient-one torsion transgression is explicitly shown before the middle-form calculation.')
add('V',2,[2],'maps:src:F.3.5 maps:src:F.3.6','The precise index-two primitive-to-quotient map, rank-three wedge period, root-curve splitting and real-intersection function are displayed; no integral identification is assumed without that morphism.')
add('V',3,[3],'maps:src:F.3.7 maps:src:F.4.1','The finite/cusp period extension, exact characteristic-vector descent and separately credited Wall/Kramer-Stolz application give the actual oriented diffeomorphism.')
add('V',4,[1,4],'night:P1A.1 night:P1A.2 night:P1A.3 night:P1A.4 night:P1A.5 night:P1A.6 night:P1.13 night:P1.17 night:P1.18','The exact half-plane, canonical/Hodge/tangent data, automorphisms and no-real-structure obstruction are stated with their mechanisms. The two different end statements retain their actual parameter domains: full-disc boundary obstruction and punctured-disc classification/filling. The explicit splitting translation is retained.')
add('V',5,[5],'maps:src:F.2.39 maps:src:F.3.4 maps:src:F.3.11','The effective input-dependent lattice classification, explicit unimodular conjugator/cusp maps and cell calculation are separate from the jet-preserving period construction; the polarized source exclusion retains its actual filtration and parity calculation.')

add('VI','prompt-10',[1],'cdp:st:C.2.G.1','The separate Paper VI ladder keeps arbitrary positive full-fibre multiplicities and arbitrary support singularities under the stated smooth compact torus-fibration and Betti hypotheses. It proves the normalization/conductor nonnegativity and global Euler sign.')
add('VI','equality',[2],'cdp:st:C.2.INT.3','The exact equality conditions follow from vanishing of each nonnegative conductor/normalization contribution, the minimal-resolution argument and unramified elliptic conductor maps.')
add('VI','local-parity',[3],'cdp:st:C.2.UN.1 cdp:st:C.2.UN.2','The local tube/mapping-torus parity calculation explicitly omits global Betti assumptions. The actual curve and point blowups realize every even integer, without expanding the global sign theorem scope.')

for labels, nums in [
    ('night:P3K.99 night:P3K.100 night:P3K.103',[2]),
    ('night:P3K.101 night:P3K.102',[3]),
    ('night:P3K.104 night:P3K.105',[4]),
    ('night:P3K.106',[5]),
    ('night:P3K.108 iv:i3_all_reduced_caps',[6]),
    ('night:P3K.107',[7])]:
    add('IV','new-'+labels.split()[0].split('.')[-1],nums,labels,
        'The current dedicated ladder gives the actual original source/line/cap and parameter maps, both integral characteristic numbers, full native fan transport and its exact finite image. Every cap/norm/character/reference and common strict scalar range is retained. K108 and ICAP are the same receiving theorem with both labels and one full proof.')

timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = dict(recorded_at=timestamp, checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)',
              scope='Focused exact main-result opening coverage and scope comparison. No new theorem proof or independent review credit is assigned.',
              plan_source='sources/plan/KEEP_SKETCH_20261117.md',
              groups=groups,
              rung_count=len(ladders), proof_ladders=sum(x['steps'] is not None for x in ladders.values()),
              invalid_step_counts=[dict(id=x['id'],steps=x['steps']) for x in ladders.values() if x['steps'] is not None and not 3<=x['steps']<=7],
              pending_groups=[x['plan_item'] for x in groups if 'pending' in x['disposition']],
              resolved_coverage_gaps=[
                  dict(plan_item='I.7',repair='Five-value table and complete orders4--8 specialization added; seven proof steps.',receipt='analysis/I_final_arithmetic_presentation.json'),
                  dict(plan_item='II.12',repair='Connected analytic families and C-infinity clopen separation added; seven proof steps.'),
                  dict(plan_item='II.13',repair='Arbitrary-section theta counterexample and full determinant correction added; six proof steps.')],
              scope_findings='All identified main-result opening coverage gaps are repaired in the exact current texts. No further opening overstatement found in this focused comparison. This conclusion does not assign new theorem proof credit or replace final rendering QA.')
(W/'analysis/inventory_opening_coverage_review.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
with (W/'analysis/inventory_opening_coverage_review.tsv').open('w',newline='') as f:
    fields=['plan_item','paper','ladders','original_main_labels','disposition','scope_comparison']
    out=csv.DictWriter(f,fields,delimiter='\t');out.writeheader()
    for x in groups:out.writerow({k:'; '.join(x[k]) if isinstance(x[k],list) else x[k] for k in fields})
lines=['# Main-result opening coverage', '', f'Recorded {timestamp}. This is a bounded opening-to-body scope comparison; it creates no new proof review.', '',
       'The 59 numbered plan items, the separate general-sign instruction and its two supporting opening results, and six groups covering the ten newly exported IV main results are mapped below. There are 68 actual proof ladders plus Paper I’s series rung zero. Every current proof ladder has three to seven steps.', '',
       'No main-result opening coverage gap remains in this focused comparison. The three identified omissions (I.7 special values, II.12 connected-family/clopen conclusions and II.13 theta correction) are now present with complete coarse proofs. The JSON retains their exact source hashes and resolved-gap history.', '',
       '| Plan item | Opening ladder | Exact main labels | Disposition |', '|---|---|---|---|']
for x in groups:lines.append('| '+x['plan_item']+' | '+', '.join(x['ladders'])+' | '+', '.join('`'+l+'`' for l in x['original_main_labels'])+' | '+x['disposition']+' |')
lines += ['', 'The JSON/TSV retains the per-group scope comparison and exact opening locations/hashes, including every corrected plan claim and all alias/grouping explanations.', '']
(W/'analysis/inventory_opening_coverage_review.md').write_text('\n'.join(lines))
print(json.dumps(dict(groups=len(groups),proof_ladders=result['proof_ladders'],pending=result['pending_groups'],invalid_step_counts=result['invalid_step_counts']),indent=2))
