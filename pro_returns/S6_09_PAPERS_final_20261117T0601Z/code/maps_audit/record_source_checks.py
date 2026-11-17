from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[3]
O=P/'deliverables/work/maps_audit'
def sha(p):return hashlib.sha256((P/p).read_bytes()).hexdigest()
actor={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17'}
records=[]
def add(key,file,url,locators,match,scope='Exact original statement opened and hypotheses matched.'):
 records.append(dict(key=key,file=file,url=url,sha256=sha(file) if file else None,locators=locators,
                     application_match=match,scope=scope,**actor))
add('Dimca2004','sources/external/maps_audit/dimca_book_mirror.html',
    'https://www.scribd.com/document/768903674/Dimca-Sheaves-in-Topology',
    ['Def. 4.2.1 pp.102–103','Prop.4.2.2','Prop.4.2.11 p.109 entire proof',
     'Th.2.3.26 pp.41–42','Cor.2.3.4 p.33','Chapter 4 coefficient hypotheses p.81',
     'Example 3.1.2(ii); §3.1 dimensional hypotheses'],
    'Proper analytic f0:N0→disc; target function identity; constant integral constructible complex. Z is noetherian of global dimension one. Spaces locally compact, countable at infinity, finite real dimension. Original book reproduction matched to official Springer edition DOI 10.1007/978-3-642-18868-8.')
add('Hatcher2002','sources/external/maps_audit/hatcher.pdf',
    'https://pi.math.cornell.edu/~hatcher/AT/AT.pdf',
    ['Prop.0.19 and Cor.0.20 pp.16–17 complete proofs','Th.4.5','Th.4.32','Cor.4.33','§3.H pp.335–336'],
    'Collared manifold inclusion is cofibration; weak equivalence between CW types is homotopy equivalence; cofibration homotopy equivalence yields strong deformation retraction. Simply connected homology sphere gives homotopy sphere. Arbitrary local-system H_c² identification proved directly in candidate to avoid overreading the ring-bundle wording.')
add('Brown1962','sources/external/maps_audit/brown_collars.pdf',
    'https://www.maths.gla.ac.uk/~mpowell/Brown%20collars.pdf',
    ['Theorem 2 p.339','Theorem 1 and Lemma 5 used in its proof'],
    'Boundary of topological manifold has a collar; applied to actual boundary quotient. Correct DOI is 10.2307/1970177.')
add('Smale1961','sources/external/maps_audit/smale1961.pdf',
    'https://www.math.uchicago.edu/~shmuel/tom-readings/Smale%2C%20PC.pdf',
    ['Theorem A p.391'],
    'Closed smooth homotopy n-sphere, n≥5; conclude homeomorphism to standard sphere.')
add('Smale1962','sources/external/maps_audit/smale1962.pdf',
    'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/structur.pdf',
    ['Theorem 1.1 p.387','Corollary 1.2 p.388'],
    'Simply connected oriented smooth h-cobordant n-manifolds, n≥5, are oriented diffeomorphic; Cor.1.2 explicitly states every homotopy six-sphere is diffeomorphic to S6.')
add('KervaireMilnor1963','sources/external/maps_audit/kervaire_milnor.pdf',
    'https://doi.org/10.2307/1970128',['Opening table pp.504–505; following remark'],
    'Theta6 has order one; h-cobordism classes coincide with oriented diffeomorphism classes for dimension six. Scanned original visually inspected.')
add('Knudson2004','sources/external/maps_audit/knudson.pdf',
    'https://arxiv.org/pdf/math/0409133',['Theorem 4.1(1)'],
    'Finite-dimensional Z/p-CW mod-p homology sphere; fixed set empty or mod-p homology sphere. Involution on closed smooth real six-sphere meets CW hypothesis by Illman1972 Th.3.1.')
add('Illman1972','sources/external/maps_audit/illman1972.pdf',
    'https://ncatlab.org/nlab/files/Illman_EquivariantAlgebraicTopology1972.pdf',
    ['Chapter 3 hypothesis compact Lie group p.44','Theorem 3.1 p.48; PDF page 53'],
    'Smooth antiholomorphic involution is a differentiable Z/2 action on compact smooth manifold; equivariant triangulation gives finite-dimensional G-CW structure. Original scanned theorem visually read; theorem proof not independently reproved.')
for tag,loc,match in [
 ('08J5','Remark 13.12.4','Canonical truncation triangles for any complex in an abelian category.'),
 ('0FLJ','Example 20.29.3','Hypercohomology spectral sequence and bounded-below convergence; cohomological d2 indexing.'),
 ('0F16','Lemma 21.26.1','Conditional MV triangle: comparison map must be an isomorphism. Candidate proves it for the two-open cover by degreewise exact flabby Cech sequence.'),
 ('012K','Section 12.24, equations and Lemma 12.24.2','Exact filtered-complex dr representative formula.'),
 ('0FKU','Section 20.31, Lemmas 20.31.1–3 and Remark 20.31.2','Derived cup product, its naive-complex comparison and functoriality.')]:
 add('Stacks-'+tag,None,'https://stacks.math.columbia.edu/tag/'+tag,[loc],match)
(O/'topology_source_checks.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
credits=[
 {'result_scope':'working integral_leray.tex (all seven labelled results)',
  'baseline':'AC26 original §§7.7,8 and Appendix B; Engel §7',
  'opened_locators':'AC26 Lemma7.25, Props7.26–7.27, Cor7.29, Th8.1, Lemma8.2, AppB ThB1 and RemarksB2/B4; Engel source S6.tex lines1331–1355, Lemma7.4',
  'comparison':'Same sphere homology conclusion and integral specialization. Workbench supplies explicit truncation/Čech identification and degree-three sign detail. Credit as rederivation/expanded proof, not a new sphere theorem.',**actor},
 {'result_scope':'working topology_reduction.tex spine, collapse and specialization',
  'baseline':'AC26 original §7.2, Props7.11–7.12 and Appendix B',
  'opened_locators':'AC26 Lemmas7.5–7.10; Props7.11–7.12; AppB RemarksB2/B4',
  'comparison':'Same topological spine/collapse structure; workbench adds displayed integral cell matrices and explicit comparison. Full proof retained with credit.',**actor},
 {'result_scope':'working topology_reduction.tex finite bands and MV–Leray comparison',
  'baseline':'AC26 original §7.6 and Prop7.27',
  'opened_locators':'AC26 Lemmas7.18–7.19, Th7.22, Remark7.23, Prop7.27',
  'comparison':'Known H1/H2 and sphere-homology route, with explicit matrices and commuting squares added. False alpha3=alpha1 occurs only in workbench, not the AC26 argument; corrected integral H3 map supplied.',**actor},
 {'result_scope':'MAPS A.1.1–A.1.3 and A.2.1',
  'baseline':'AC26 original page2; Engel Lemma3.8 and Remark8.3',
  'opened_locators':'Engel S6.tex lines842–863 and1685–1723',
  'comparison':'Invariant covector and regular circle quotient credited to Engel. Literal cusp extension in Remark8.3 fails by two explicit radial sequences; repaired quotient construction and distinct extendible/fixed curves checked. Do not attribute corrected map to the literal formula.',**actor},
 {'result_scope':'MAPS A.3.1–A.3.4',
  'baseline':'FAMILY real structures and even shifts; targeted AC26/E26/DGKX review',
  'opened_locators':'FAMILY B.4.1/B.4.2/A.3.1; actual periods; DGKX v1 closing lines10630–10678 and11863ff',
  'comparison':'Candidate-specific real-involution classification uses actual period and cusp actions. Targeted absence searches do not constitute a universal novelty claim.',**actor}
]
(O/'source_credit_checks.json').write_text(json.dumps(credits,ensure_ascii=False,indent=2)+'\n')
for fn in ['smale_retrieval.json','topology_source_retrieval.json']:
 p=O/fn;rr=json.loads(p.read_text())
 for r in rr:
  k=r['key'];matches=[x for x in records if x['key'].lower().replace('2002','').replace('1962','').replace('1961','').replace('1963','').replace('2004','')==k or x['key'].lower()==k]
  if matches:r['reading_status']='Exact locators opened; see topology_source_checks.json';r['check_record']=matches[0]['key'];r.update(actor)
 p.write_text(json.dumps(rr,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(records),'exact source checks and',len(credits),'scoped credit comparisons.')
