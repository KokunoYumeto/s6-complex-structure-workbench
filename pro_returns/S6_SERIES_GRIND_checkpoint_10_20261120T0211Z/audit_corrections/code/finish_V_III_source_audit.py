from pathlib import Path
import csv,hashlib,json,re
here=Path(__file__).resolve().parents[1]
root=here.parents[1]

# Preserve the full displaced proofs before the parent replaces them.
s=(root/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_V.tex').read_text()
archive=[]
for lab in ['night:P1.9','maps:src:F.1.1']:
 p=s.index('\\label{'+lab+'}');a=s.index('\\begin{proof}',p);b=s.index('\\end{proof}',a)+len('\\end{proof}')
 archive.append('% Original attached proof of '+lab+'; displaced only by exact cited specialization.\n'+s[a:b])
(here/'V_displaced_known_proofs_evidence.tex').write_text('\n\n'.join(archive)+'\n')

# Exact primary-source edition, never transfer attached pagination to public v1.
for p in [here/'code/build_V_literature.py',here/'V_known_result_proof_patches.tex',here/'V_root_curve_comparison.tex']:
 t=p.read_text().replace('pp.~56--58','pp.~57--59, attached-source edition').replace('p.~58]{Yang2026}','p.~59, attached-source edition]{Yang2026}')
 t=t.replace('multiplication\nby this rational function gives the line-bundle identification.',
             'multiplication by $t/(t-1)$ gives the explicit map\n$T^5\\to q_3^*L_{3,4}$.')
 p.write_text(t)
for name in ['V_known_result_proof_patches.json','V_literature_front_patches.json']:
 p=here/name;a=json.loads(p.read_text())
 for d in a:
  d['tex']=d['tex'].replace('pp.~56--58','pp.~57--59, attached-source edition').replace('p.~58]{Yang2026}','p.~59, attached-source edition]{Yang2026}')
  if 'source' in d:d['source']+='; citation pages 57–59 are the retained attached-source rendered edition; this run first-pass aux was 56–58 before TOC stabilization. Public arXiv v1 identity is unverified.'
 p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')

patches=[
dict(label='night:P3F.34',operation='replace_statement',tex=r'''For every free affine OS49 cap with $n\ne0$, let
$g=\gcd(3k,n,3d)\in\{1,3\}$. Then
$H_1=H_4=\mathbb Z/|n|$ and
$H_2=H_3=\mathbb Z/|n|\oplus\mathbb Z/g$.
The free cap $(m,n,d)=(9,3,1)$ has
$H_2=H_3=(\mathbb Z/3)^2$.
On the coprime sector $\gcd(n,3k)=1$ one has $g=1$,
recovering \cref{maps:src:D.2.11}; the additional factor
describes the remaining free caps.  The complete $n=0$
groups are also computed below.'''),
dict(label='night:P3F.34',operation='replace_exact_text',old='This is not the general-n value stated in CSV row D.2.11. The complete integral Gysin and exterior-restriction calculation was independently audited before this comparison was marked final.',
new=r'''This example refutes an unrestricted reading of the cyclic
formula in the short CSV summary.  The theorem
\cref{maps:src:D.2.11} and the hypothesis cell of its attached
CSV row explicitly assume $\gcd(n,3k)=1$; there $g=1$ and
the two formulas agree.  The present calculation includes
every free cap classified in \cref{night:P3F.33}.''')]
(here/'P3F34_proposed_patches.json').write_text(json.dumps(patches,indent=2,ensure_ascii=False)+'\n')

report=r'''# P3F.34 source and arithmetic audit

## Result and precise source scope

The displayed homology formula agrees with its integral transfer matrix. The source theorem D.2.11 explicitly assumes gcd(n,3k)=1, both in `sections/manifolds.tex` at lines 2156–2186 and in the hypothesis column of the attached MAPS results CSV. Its short description says “general admissible n”; reading that phrase as every free cap drops a hypothesis that is present elsewhere in the same row. P3F.34 supplies the unrestricted free-cap extension. At gcd(n,3k)=1, g=gcd(3k,n,3d)=1, and the formulas literally coincide. The cap (m,n,d)=(9,3,1) has gcd(n,3k)=3 and g=3. The proposed wording records these exact inclusions and the exceptional term without assigning a false refutation to the scoped theorem.

## Exact arithmetic

The normal circle evaluates as (-n,-3d,3k) on the integral one-classes. Its primitive kernel is the rank-two lattice L. The dual transfer has columns (3d,-n,0) and (3k,0,n). The three two-by-two minors are 3kn,3dn,-n². Therefore its determinantal divisors are g and |n|g, giving Smith factors g,|n|. The kernel L is saturated in Z³: if av lies in the kernel for a nonzero integer a, then the integral normal evaluates to zero on v. Consequently computing torsion in the ambient lattice gives exactly the torsion in this rank-two kernel quotient, with only the extra ambient free direction removed.

In the free sector gcd(k,n,d)=1 and (3 does not divide n or 3 divides k), every prime other than three is excluded from g. A factor 3² in g would divide k,n,d after taking the displayed 3d and 3k entries, so g is 1 or 3. For n=0 the criterion forces 3|k and gcd(k,d)=1, whence g=3. The transfer then has image 3Z in the primitive kernel basis e_psi,(0,k,d); its cokernel is Z⊕Z/3. The additional free kernel in the pair sequence gives H2=Z²⊕Z/3. Duality and χ=2 give the printed remaining groups.

The fresh program `code/independent_V_III_checks.py` imports no earlier computational code. It checks every affine power for 7,650 triples (4,756 free, including 1,304 noncoprime free triples and 52 n=0 free triples), compares the criterion and determinantal divisors, and evaluates 427 direct SymPy Smith forms. It also independently checks the V common-root divisors and realification/Hodge-index substitutions. All 25,759 assertions passed. The program preserves the geometric boundary basis and pair sequence as inputs; its finite enumeration supports the general determinant argument and does not replace those geometric inputs.

## Literature comparison

AC26 original Theorems 7.17 and 7.22, printed pp.57 and 60, have the explicit (3,4) cap presentation with p=12l0−4l1−3l2 and gcd(p,12)=1. The receiving D.2.11 instead gives its exact relation to Xiufan Yang's Type C system: U=M_IV, V=U^-1 M_II U and

S = [[0,0,-1,0],[0,-1,1,1],[0,0,0,1],[-1,0,3,0]], det(S)=−1,

with U^(-t)S=ST1 and V^(-t)S=ST2 (`manifolds.tex` lines 2230–2281). The good-root section coordinate is (tau+1)/3, the point-line Picard coordinate is mu_C, and the translation coordinate is 3mu_C. This is an integral Hurwitz reorder and conjugacy of the actual open systems. The unchanged type-II filling is retained as an additional geometric choice.

Yang's attached `Compact_Complex_Threefolds_REPAIRED_v4_5.tex` Theorem 7.13 (source around lines 4070–4150; first-pass aux p.49) calculates the particular original Type B/C global families. The surrounding proof uses actual cusp sweep maps, unit-coefficient elimination, and two relations rx1=a_kappa x2 and (6−m1)x2=0. His general finite-cap presentation in Theorem 7.2 and prime-subgroup freeness criterion at source lines 4194–4210 are related known inputs. P3F.34 retains the same integral-saturation discipline and supplies the explicit changing normal circle and transfer for the component-supported OS49 exterior. The additional gcd factor has not been located in the opened core papers or the recorded searches.

Wang's attached `order_two_rational_homology_sphere_new.tex`, Theorem 1.1 (`intro:main`, lines 99–113), is a positively identified related construction: the genuine line O(P−O), lifted −6P translation, one cubic logarithmic cap, and three multiplicative completions produce simply connected H2=H3=Z/2. Its introduction explains the integral specialization and transgression coefficients (1,2,2,1). This is credited as related integral-torsion methodology; no equivalence of its marked completion with the present OS49 cap is asserted.

The attached E26 and both DGKX editions were compared at their finite-root and periodic-torus completion constructions. Search engine 1 queries on 2026-11-19 were `"OS49" "homology" "affine"`, `"IV" "II" "I_2" "complex threefold" "homology"`, and `"free affine" "cap" "3k" "homology"`. They returned Wang's related construction and broad unrelated results; no exact target formula was identified. This is a bounded search conclusion. It establishes neither worldwide absence nor absence of other mathematical relationships.

## Check type

The complete printed P3F.34 proof was read for its actual normal-circle map, integral q=eta h/3 boundary class, exterior restriction argument, pair sequence and source scope. The above determinant calculation and fresh executable are independent arithmetic checks performed after that reading, so they are not recorded as a before-reading independent re-proof of the complete theorem. The boundary restriction is fixed using the proved n=1 sphere fillings for every k,d; its projected cross-product W satisfies |kW1−dW2+W3|=1 for all k>0 and d, hence W1=W2=0 and W3=±1. This removes the possible unproved integral splitting in the computation. The remaining geometric inputs are P3F.26, P3F.29 and P3F.33, with their prior checks retained.
'''
(here/'P3F34_source_scope_report.md').write_text(report)

vreport=r'''# Paper V literature comparison

The new substantive attribution is `night:P1.9`: it is the n=3, D=C, B=I specialization of the attached Yang higher-dimensional periodic quotient theorem, using the identical lattice, fan, torus action and root coordinate. The index-d version is its finite-index quotient. `maps:src:F.1.1` uses its n!d Euler formula and short global Euler additivity. Full displaced proofs are preserved in `V_displaced_known_proofs_evidence.tex`; replacements and exact source mappings are in `V_known_result_proof_patches.json`. The global E.1.2 small crepant resolution still needs its explicit A Z3 B^-1 product morphism and fan refinement, and the rank-six global construction still needs its actual boundary maps.

The verified Yang edition is exactly the received `Compact_Complex_Threefolds_REPAIRED_v4_5.tex`, SHA256 `5061ce4e6cda8ed7ba3bb2a7a597d50e018bfd53fb9e49e7b38317f628c332a5`. Its metadata declares it a top-level TeX source but contains no public-v1 content comparison. Exact public PDF and abs/v1 opens returned DisabledError. Citations must identify the attached source edition. The older verified rendered build has Theorem8.7 pp57–59 and Corollary8.8 p59. This run's first-pass unmodified-source aux initially gave pp56–58 before TOC stabilization and then failed during font embedding. No successful fresh PDF opening is claimed for that build. The exact theorem labels and source lines 4674–4848 were read in full.

The diffeomorphism input is a known extended-form classification plus Kramer–Stolz absorption. The actual oriented isometry preserves the form and p1/2, so it preserves the rank-four normal clutching pair (Euler,p1/2). The almost-complex compatibility is also known. The explicit realification map sends (TN,J), pulled back from the constructed integrable fourfold, to TN. Its c2=−Σxi,c4=6u,p2=14u satisfy Mandal's two conditions 14≡2 mod4 and 14−2=12. Huijun Yang's older criteria give the same result: 9σ=18 is even and 4p2−p1²=48=8(b4+2). The rank-six integrable construction itself is retained as the additional result proved by the receiving paper; the bounded searches found no exact earlier statement of that constructed analytic family.

The DGKX root/direct-image method is credited with its actual relationship, not by asserting an undefined separation between constructions. Under t=lambda*/(lambda*−lambda), use the common (15,4) root curve R. The root maps are s3=s15^5 and s5=s15^3. With T=O(4D1−D2), q3*L34=T^5 and q5*L54=T^3; the first identity is multiplication by t/(t−1) in the explicitly stated direction. Thus the first direct images pull back to O⊕T^-5 and O⊕T^-3⊕T^-6. In both cases the exterior-power maps are the cup products. This is the exact shared sheaf method. It does not provide or assert an isomorphism of the full global families.

The Catanese, Esole–Kang, Jia–Meng and Huijun Yang primary PDFs were reopened successfully and matched at their precise locators. The Esole–Kang input is restricted to the displayed universal characteristic polynomials. Applying an algebraic crepant-invariance theorem to an analytic manifold without its stated hypotheses is not needed in the comparison. The Jia–Meng input supplies a Kähler modification; its effect on H1 and H1(O), together with b1=2h01 on the Kähler model, gives the exact obstruction used in E.2.1. Catanese's theorem is used for the smooth compact torus families produced inside the endpoint proof.

P1A.5 and P1A.6 have compatible scopes. The former forbids a proper analytic full-disc extension across the boundary of the parameter domain in the sense defined before that theorem. The latter starts with a punctured-disc family all of whose members are in the classified family; its class map extends to an interior point and its C×Z/2 torsor is removed by at most a double cover. The source comparison preserves these maps and quantifiers.

The original named P1.18 numerical certificates are absent from the attached tree. The independent reconstruction by `paper_i_audit` has now produced a new Arb cover of all four regions, with 1,600 rational closed leaves, four central Hessian boxes and an inner-cusp determinant certificate, plus normalized intertwiner and splitting enclosures. The numerical-validation gate therefore rests on that new preserved certificate, not on the absent historical files. This source-comparison event does not claim to have executed that other agent's code.

All detailed row scopes, exact local source locators, replacement paragraphs, searches and new reference entry are in the companion TSV/JSON/TeX files. No worldwide novelty or mathematical-unrelatedness claim is made. The long E.2.3–E.2.21 supporting assertions were retained as a source-comparison group, with complex-fivefold dimensions kept explicit; this pass is not represented as a new complete proof audit of their full constructions.
'''
(here/'V_literature_comparison_report.md').write_text(vreport)

# A precise current numerical risk field, without claiming another agent's execution.
p=here/'V_literature_comparison.tsv'
with p.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
for r in rows:
 if r['statement_id']=='night:P1.18':
  r['remaining_risk']='The named historical certificates are absent. paper_i_audit reports a new complete independent Arb cover and normalized period certificate; its preserved code/output, not the absent files, now supplies validation. This source-comparison event does not claim its execution.'
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
add=[
('night:P3F.34','targeted proof check','Read the complete proof and compared its integral normal-circle, boundary-basis, exterior-restriction and pair-sequence arguments. The determinant factors are g,|n|. D.2.11 theorem and CSV hypothesis cell already impose gcd(n,3k)=1, where g=1; repair the general-n prose to state the exact specialization rather than refuting that scoped theorem. See P3F34_source_scope_report.md and P3F34_proposed_patches.json.'),
('night:P3F.34','computation or formal certificate','Fresh independent_V_III_checks.py proves symbolic transfer minors (3kn,3dn,-n²), checks all affine powers for7650 triples, including4756 free triples and1304 noncoprime free triples, and compares427 direct Smith forms. All25759 combined assertions pass. Geometry and named pair-sequence inputs are retained; no full before-reading independent re-proof is claimed.'),
('night:P3F.34','targeted proof check','Compared the exact Yang Type C integral conjugacy in D.2.11 (det S=-1, U^-t S=ST1,V^-t S=ST2), the original AC26 scoped homology theorem, Yang attached Thm7.13 and full-twist presentation, Wang attached Thm1.1 integral-torsion construction, and finite-root constructions in E26/DGKXv1/v2. Three further searches identified no exact target formula. Bounded literature conclusion only; positive relationships and queries retained in P3F34_source_scope_report.md.'),
('maps:src:F.4.1','computation or formal certificate','Fresh independent_V_III_checks.py checks the explicit realification characteristic classes against Mandal Thm1.3 and Huijun Yang Theorems1–2: c2²=2,c4=6,p1²=8,p2=14,sigma=2,14≡2 mod4,14−2=12,4p2−p1²=8(b4+2). It checks the first three Hirzebruch holomorphic genera against the displayed P1A.2 Hodge table. This certifies these substitutions only.'),
('night:P1A.1','computation or formal certificate','Fresh independent_V_III_checks.py checks the common-root divisor transports q5*L54=T³ and 5T−q3*L34=div(t/(t−1)). The explicit root coordinate maps and actual cup-product morphisms are recorded in V_root_curve_comparison.tex. This is a convention transport check, not a new complete cohomology proof.'),
('night:P1A.2','computation or formal certificate','Fresh independent_V_III_checks.py computes alternating rows of the Hodge table as chi_p=(0,-1,4,-1,0), agrees exactly with Esole–Kang v1 eq1.2 after c1=c3=0,c2²=2,c4=6, and recovers Euler6. No inference from matching numerical invariants to isomorphism is made.'),
]
p=here/'CHECK_EVENTS.tsv'
with p.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;events=list(r)
for lab,kind,outcome in add:
 eid='s6sg:'+hashlib.sha256((lab+kind+outcome).encode()).hexdigest()[:20]
 if not any(x['event_id']==eid for x in events):events.append(dict(statement_id=lab,date='2026-11-19',who=actor,type=kind,outcome=outcome,event_id=eid,phase='S6_SERIES_GRIND'))
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'events':len(events),'P3_patches':len(patches),'displaced_proofs_archived':len(archive)}))
