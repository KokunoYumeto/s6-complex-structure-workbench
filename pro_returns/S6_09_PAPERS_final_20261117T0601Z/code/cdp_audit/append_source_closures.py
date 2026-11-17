"""Append final exact source-reading scopes without overwriting prior records."""
import hashlib,json
from pathlib import Path
ROOT=Path('/workspace/scratch/037cd144174c')
P=ROOT/'deliverables/work/cdp_audit/references_verified.json'
rows=json.loads(P.read_text())
by={r['key']:r for r in rows}
reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run;17November2026UTC'
def extend(key,locators,uses,scope,source=None,aliases=(),title='',url=''):
 r=by.get(key)
 if r is None:
  r={'key':key,'title':title,'url':url,'status':'verified in the specified scope','opened_locators':[], 'uses':[], 'verification_scope':'','own_check':reader,'not_verified':[]};rows.append(r);by[key]=r
 for field,vals in [('opened_locators',locators),('uses',uses),('aliases',aliases)]:
  r.setdefault(field,[])
  for v in vals:
   if v not in r[field]:r[field].append(v)
 if scope not in r['verification_scope']:r['verification_scope']+=' '+scope
 if source:r.update(local_source=source,source_sha256=hashlib.sha256((ROOT/source).read_bytes()).hexdigest())
 r['status']='verified in the specified scope'
extend('Viaclovsky2026Combs',
 ['Theorem2.2 and its complete proof, printed pp4–5; supplied source lines375–490, including the standing proper connected n-manifold-to-disc hypotheses and Lemma2.1','Theorem2.3 and complete proof pp5–6; source lines490–585','Theorem4.1 p11 onward: local period setup and complete case(i), source lines930–1108; only the opened portion of case(ii) is within this additional reading','Theorem6.1 p19 onward: source lines1502–1618, hexagonal setup and displayed independent logarithmic period/action formulas; this is a partial proof reading','Numbered locators verified by compiling unchanged supplied source: t:main=Theorem1.1 p1; degrees=Theorem3.2 p8; smoothingbound=section9.2 p30'],
 ['CDP E4 full known local-freeness result','CDP D1.12 torus/S6 special-case credit','CDP E7 rank-two logarithmic leading matrix in the actual comb cusp'],
 'The exact printed Theorem2.2 is the whole conclusion of E4, whose full proof is a re-derivation; the source acknowledges a Gabber outline through Conrad and its analytic Raynaud counterpart. Theorem2.3 contains the torus/S6 cup-product argument extended by D1.12. Theorem4.1 case(i) and the opened rank-two local formulas give logarithmic coefficient I at the retained hexagonal cusp. This additional event does not claim a complete reading of the whole Theorem6.1 proof.',
 'sources/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex', ['ViaclovskyCombs2026'])
extend('ViaclovskyTwo2026',
 ['Supplied source lines500–563: mum model, actual generators and two independent q-valuation directions','Supplied source lines1490–1560: Proposition6.4 statement and actual simultaneous family construction through the uniform smooth proper construction; the root reader separately read its full proof through line1607'],
 ['CDP E7 rank-two leading period matrix','CDP E13 exact construction hypotheses for the independent tangent/miniversality calculation'],
 'Read the actual period generators, fourth-order roots, line-bundle linearizations, equation y²=x³+tx+mu*t+1 and distinguished section(-mu,sqrt(1-mu³)). The independent q-valuations and uniform gluing match the receiving proof. Root reader separately records sections2–3, Proposition6.1, and the entire Proposition6.4 proof. This source-opening event itself does not assert that every preceding theorem was rederived.',
 'sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex', ['ViaclovskyTwoParameter2026','Viaclovsky2026Two'], 'A two-parameter family of complex structures on the six-sphere','https://arxiv.org/abs/2609.33785')
extend('LiuRollenske2026',
 ['Supplied S6_arxiv.tex lines232–285, surface-facts proposition and displayed Weierstrass, discriminant, j and section formulas','Supplied source lines402–485, compactification proposition and its entire proof'],
 ['CDP E7 local rank-two logarithmic cusp','CDP E14 exact cusp and finite-root construction comparison'],
 'Read the original model y²=x³+(27/4)t³(1-t)x+(27/4)t⁵(1-t), section(-t²,it³), discriminant-3^9*t^9*(1-t)² and III*/II/I1 types. The receiving coordinates t_new=(27/4)(t_old^-1-1),x_new=x_old/t_old²,y_new=y_old/t_old³ give y²=x³+tx+t and section(-1,i). The entire compactification proof has q-valuation directions(c1*q,c2),(c3,c4*q), a dP6 central support and the stated fourth-root good-reduction action with limiting multiplier-i and two A3 plus one A1 quotient singularities. The topology theorem has an independent reader record; commented-out Hodge computations are not imported.',
 'sources/papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex', [],'A complex structure on the six-dimensional sphere','https://arxiv.org/abs/2609.33826')
extend('Viaclovsky2026Log',
 ['Supplied source lines275–606: complete monodromy lemma, logarithmic-transform proposition logprop and boundary-group proposition bound, with their complete proofs','Supplied source lines845–880: Mumford H3 and primitive infinity-image statements','Supplied source lines1055–1105: matrix proposition and its displayed determinant calculation'],
 ['CDP E11 actual free higher-multiplicity logarithmic transformations','CDP E19 comparison of affine marking, normal-circle sign and Mayer–Vietoris determinant'],
 'Read and rederived the degree-mi root, extension of the cyclic symmetry, translation to a varying origin, invariant period section v_i/mi, freeness detected by psi and gcd(ni,mi)=1, and logarithmic conjugacy. The actual punctured gluing retains the full vector ai, not only its torsion class. The positive normal circle is(-vi,mi), giving the exact boundary relation g_i^mi=vi. The stated matrix determinant is m1*n0+m0*n1. AC26 Theorems7.17/7.22 are separately the prior source for the full unrestricted original-twist homology conclusion; a partial reading of later Viaclovsky sections is not recorded as a full proof audit.',
 'sources/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex',['ViaclovskyLog2026'],'Logarithmic transformations and complex structures on the six-sphere','https://arxiv.org/abs/2610.39102')
extend('CDP1998', ['Supplied source lines230–295: Proposition1.1, Corollary1.3, Lemmas1.4/1.5 and their full displayed proofs'], ['CDP C1.2 and E3 known conclusions','CDP E12/E17 exact false unrestricted statements'], 'The complete displayed statements and proofs were read: Corollary1.3 supplies generic endpoint vanishing; Lemma1.4 gives b2>0 for a Moishezon manifold; Proposition1.1 permits nonreduced spaces without excluding embedded components. The receiving embedded-point counterexample and the exact torsion-sensitive base-change calculation distinguish these separate defects.')
extend('CDP2020', ['Supplied source lines493–713: complete section3 resolved-pencil/general-fibre argument','Published p685, Lemma4.6 and conductor canonical formula, with its full displayed proof','Published p686, Proposition4.7 and conductor Euler calculation, with its full displayed proof'], ['CDP E17 exact higher-image claim in the actual pencil setting','CDP A5.3/A5.12 partial conductor-duality credit'], 'The actual section3 pencil proof was read, and the receiving P1 evaluation-sequence argument was matched to its exceptional divisor. Lemma4.6 and Proposition4.7 are known conductor-canonical and Euler inputs; the broader receiving conductor bounds and local exclusions are additional statements, not attributed wholesale to these originals.')
extend('LRS2019', ['Numbered original Theorem3.1 and Corollary3.2, p9, opened by the root reader; the supplied source label main2 new refers to this theorem'], ['CDP E2 whole known nonholomorphic-pencil vanishing theorem'], 'The original numbered locator is Theorem3.1/Corollary3.2 p9 in the2019 version. Every Picard component is obtained by replacing V by V tensor a fixed line bundle. This is a direct extension of notation, not a new vanishing conclusion.')
P.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(rows),'reference groups with final exact scopes; bibliography file untouched.')
