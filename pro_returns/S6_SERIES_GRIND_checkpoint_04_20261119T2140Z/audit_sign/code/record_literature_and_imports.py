from pathlib import Path
import csv, hashlib, json

p = Path(__file__).resolve().parents[1]
root = p.parents[1]
who = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'

sources_path = p / 'SOURCE_OPENINGS.json'
sources = json.loads(sources_path.read_text())
def source(key, **kw):
    record = dict(key=key, **kw)
    fp = record.get('path')
    if fp:
        f = root / fp
        if f.exists():
            record['sha256'] = hashlib.sha256(f.read_bytes()).hexdigest()
    for i, old in enumerate(sources['sources']):
        if old['key'] == key:
            sources['sources'][i] = record
            break
    else:
        sources['sources'].append(record)

source('Douady1966',
       path='S6_SERIES_GRIND_work/audit_sign/literature/Douady1966_original.pdf',
       url='https://www.numdam.org/article/AIF_1966__16_1_1_0.pdf',
       reading='Original journal PDF opened and relevant passages read; original PDF downloaded locally.',
       locators='Introduction p1 footnote on nilpotents; section9 Theorem1 pp83-84 and Theorem2 pp84-85; section10.1 Proposition1 p86 with proof; section10.2 Theorem1 p87.',
       statement_scope='E6 absolute Douady space, graph open subspace and isomorphism openness for proper flat analytic families over possibly nonreduced bases.',
       refs=['turn796266472view0', 'turn572004794view0'],
       limitation='Only the passages used in E6 were compared; no independent re-proof of all Douady representability is claimed.')
source('Horikawa1974II',
       path='S6_SERIES_GRIND_work/audit_sign/literature/Horikawa1974_II_original.pdf',
       url='https://www.jstage.jst.go.jp/article/jmath1948/26/4/26_4_647/_pdf/-char/en',
       reading='Original publisher PDF downloaded, converted to text and directly read. Web retrieval of the full PDF failed; the actual local original supplies the opening.',
       locators='Section4 p649, equations4.3-4.5 and Theorems4.3-4.4; section6 Theorem6.1 and proof pp660-661.',
       statement_scope='E6 map-deformation obstruction framework and comparison with the H1-surjection/H2-injection hypotheses. E6 expressly supplies its own torus Artin-lifting argument in place of invoking the H2-injection hypothesis.',
       refs=['turn290826507search2', 'turn456200687search3'],
       limitation='The web refs identify the journal item only; full-text comparison was with the downloaded original PDF.')
source('AC26_sign_credit',
       path='S6_SERIES_GRIND_source/S6_GRIND_6_literature/original/AC26_original_manuscript.pdf',
       reading='Attached original manuscript PDF converted to text and the listed pages read, without relying on its transcription.',
       locators='Main Theorem items1-8 p4; Corollary1.1 and Remarks1.2-1.3 pp4-5; section1.2 p5; Theorem7.22 and proof p60; Corollary8.5 and proof p64.',
       statement_scope='Exact source-family Euler number2, torus and bielliptic zero-Euler fibres, two triple points of the dP6 normalization quotient, integral sphere case and stated CDP conflict.',
       limitation='This opens the exact known-example credit. It does not certify every input of AC26, nor establish the unrestricted P4.58 classification by attribution.')
source('Engel2026_sign_credit',
       path='S6_SERIES_GRIND_source/S6_GRIND_6_literature/papers/arXiv_2609.38442_Engel_src/S6.tex',
       url='https://arxiv.org/pdf/2609.38442',
       reading='Attached original TeX and public original PDF both opened; the exact proposition and complete proof read.',
       locators='Proposition7.1, printed p17 (PDF page17, zero-based P16), TeX1270-1286.',
       statement_scope='Euler number2 for Engel\'s given family, obtained from its two zero-dimensional toric strata and the zero-Euler torus/bielliptic fibres.',
       refs=['turn543675182view0', 'turn764606902view0'],
       limitation='This passage treats the specified source family. No claim that it proves the unrestricted sign/equality theorem is made.')
source('CDP2020_sign_comparison',
       url='https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/algebraic_dimension_of_compact_complex_threefolds_with_vanishing_second_betti_number.pdf',
       reading='Actual primary publisher PDF opened and exact statements read.',
       locators='Theorem2.1 p679; Theorem2.2, Corollary2.3 and Proposition2.4 p680.',
       statement_scope='Theorem2.2 uses integral H1=H2=0, algebraic dimension1 and holomorphic algebraic reduction, and concludes generic tangent vanishing, nonpositive Euler characteristic and c3<=0. Proposition2.4 explicitly requires the second direct-image vanishing.',
       refs=['turn674092371search8', 'turn543675182view3'],
       limitation='This source opening verifies the claims and hypotheses used for comparison, not their validity for the example.')
source('DGKXv1_sign_scope',
       path='S6_SERIES_GRIND_source/S6_GRIND_6_literature/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
       reading='Attached original TeX intro163-365 and exact fixed-marking passage10720-10775 read; full-text targeted search for Euler/sign/all-fan return language.',
       locators='Introduction and main theorem statements; remark preceding proof of p2:thm:exact-period, lines10720-10739; subsection p2:sec:orbit-groupoid lines10747-10775.',
       statement_scope='Oka/modification results, ordinary tangent tuple and Kuranishi/automorphism/exact-period claims for the specified family. The exact-period map retains the finite uniformizers, cusp splitting and fan marking.',
       limitation='Public PDF open was disabled. No general Euler-sign classification or all-fan Theta7 formula was located in this scoped search; this is not a universal absence proof.')
source('DGKXv2_sign_scope',
       path='S6_SERIES_GRIND_source/S6_GRIND_6_literature/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex',
       reading='Attached original TeX abstract and introduction135-290 read; full-text targeted search for Euler/sign/all-fan return language.',
       locators='Abstract and introduction, lines135-290; fixed A2 fan construction located at1146-1170.',
       statement_scope='Oka, cyclic-cover and finite-point modification results for the specified source family; credits AC/LR/Viaclovsky.',
       limitation='Public PDF open was disabled. Search scope supplies no assertion that the whole manuscript was independently checked.')
source('ViaclovskyCombs_II_scope',
       path='S6_SERIES_GRIND_source/S6_GRIND_6_literature/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex',
       reading='Attached original TeX exact source passages read, including the whole proof of theorem raynaud.',
       locators='Theorem raynaud and proof418-494; section7 equations7.1-7.3, Proposition7.3 and Remark7.4, lines2008-2121; paramspace/effective2182-2267.',
       statement_scope='E4/E5 torsion-freeness by reduced root and invariant pushforward; E15 fixed-value period-family dimension; smooth topology comparison along a short smoothing path, with stated invariance of integral source-fibration monodromy.',
       limitation='The section7 passage constructs Phi_s along a short path. It does not explicitly supply the full globally single-valued radial parameter-loop trivialization used in F16; F16\'s own maps remain needed.')
sources_path.write_text(json.dumps(sources, indent=2, ensure_ascii=False)+'\n')

search_path = p / 'SEARCH_LOG_continued.json'
search = json.loads(search_path.read_text())
queries = [
 ('system1','"compact complex threefold" "b_1" "b_2" "Euler" torus'),
 ('system1','"torus" "degeneration" "Euler characteristic" "nonnegative" complex surfaces'),
 ('system1','"Horikawa" "Deformations of holomorphic maps. II" pdf'),
 ('system1','"Douady" "1966" "83" "compact" sous-espaces'),
 ('system1','"torus degeneration" "nonnegative Euler"'),
 ('system1','"complex two-tori" "Euler" "sign"'),
 ('system1','"Liu" "Rollenske" "monodromy" "sphere" 2026'),
 ('system1','"threefolds" "torus" "b_2" "c_3" 2026'),
 ('system2','"Horikawa" "6.1" "660" holomorphic maps'),
 ('system2','"02640647" pdf'),
]
existing = {r['query'] for key in ['queries','additional_queries'] for r in search.get(key,[])}
for engine,q in queries:
    if q not in existing:
        search.setdefault('additional_queries',[]).append(dict(engine=engine,query=q,date='2026-11-19',purpose='Exact E6 original passages and scoped global sign/monodromy literature comparison. Irrelevant or secondary hits were not relied upon.'))
search_path.write_text(json.dumps(search,indent=2,ensure_ascii=False)+'\n')

f=p/'CHECK_EVENTS_additions.tsv'
with f.open() as h: ev=list(csv.DictReader(h,delimiter='\t'))
fields=list(ev[0]); ids={x['event_id'] for x in ev}
for x in ev:
    if x['event_id']=='S6_SERIES_GRIND_sign_K111_moving_star_180':
        x['outcome']=x['outcome'].replace('All180','All202').replace('both horizontal Cartier orders,','all source-band whole-chart tests, all relative common-lift whole-chart tests, both horizontal Cartier orders,')
def event(label,key,text,kind='targeted proof check'):
    eid='S6_SERIES_GRIND_sign_'+key
    if eid not in ids:
        ev.append(dict(statement_id=label,date='2026-11-19',who=who,type=kind,outcome=text,event_id=eid,phase='continued mathematical review'));ids.add(eid)
event('cdp:st:E6','E6_Douady_Horikawa_originals','Opened and compared actual Douady1966 section9 Theorems1-2 pp83-85 and section10.1 Proposition1/section10.2 Theorem1 pp86-87, including nilpotent-base convention; opened Horikawa1974II section4 p649 and Theorem6.1/proof pp660-661 from the original publisher PDF. E6 supplies its own torus Artin-lift argument in place of Horikawa\'s H2-injection hypothesis. The exact external source-opening gate is closed; imported theorems are used at those precise scopes.')
event('night:P4.58','P458_primary_literature_comparison','Read AC26 original Main Theorem p4, section1.2 p5, Theorem7.22/proof p60 and Corollary8.5/proof p64; Engel2026 Proposition7.1 and full proof printed p17; CDP2020 Theorems2.1-2.2, Corollary2.3 and Proposition2.4 pp679-680. The known example Euler number2 is correctly credited. Also read DGKXv1/v2 original introductions and exact v1 fixed-fan scope. Scoped web and source searches did not locate an earlier theorem matching the unrestricted local classification/equality conclusion; no universal novelty claim or whole-literature absence claim is made.')
event('night:P3K.111','K111_E81_actual_Tate','Reopened entire E81 subsection cp15 IV46226-46403. Checked the actual inverse-j Q and analytic fourth-root scale, coordinate map x=a^2(xT+1/12)-r/3,y=a^3(yT+xT/2), Tate node Jacobian−1, the exact P/t and W/t limits, source (P,R) Jacobian2, P^3=Q on s=0, R-P=s*u_s with u_s(0)=1, residue-normalized eta, and all point/O Cartier and period factors. This closes the E81 original-coordinate import at K111\'s used scope; K111 SI2 still supplies its actual selected-height adaptation.')
event('night:P3K.111','K111_topology_import_scope','Reopened full F35 proof IV9943-9996: actual periodic integral-basis flops, primitive blowup summands and van Kampen maps, plus prime fixed sets. Read F41 SC.5 IV11878-11999: E6 good-root H2 free block is unimodular for every retained kappa, torsion coefficient−2 is a unit modulo3, and D1=D3=[[0,1],[n,-m]]. Reopened K96 EX.1-3 and EX.5-6 at the M2/cubic-good-root usage: strict-section Cartier min(v_w,2*l*v_z), translated graph, exact chord normalization, norm and full annular squares, identity parameter closing. Read K111 ASI2.7 actual source path and transport. K94 simultaneous-source input and original source chain arrays retain inherited scope; this event does not claim all of F41/F46/K96 re-proved.')
with f.open('w') as h:
    w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(ev)

a=json.loads((p/'row_assessments.json').read_text())
a['cdp:st:E6']['confidence_line']+=' Exact Douady and Horikawa original passage comparisons completed.'
a['cdp:st:E6']['remaining_risk']='No specific fault found in the eleven-step comparison. The external Douady/Horikawa passages have now been opened and matched at their exact hypotheses; their general theorems and all other standard inputs are not independently re-proved here.'
a['night:P4.58']['remaining_risk']='Fresh review checks all five assembly steps and exact primary literature credit. Every imported irreducible/conductor classification lemma has not been independently re-proved in this subtask. Scoped source/web searches do not establish universal novelty.'
a['night:P3K.111']['confidence_line']=a['night:P3K.111']['confidence_line'].replace('by180','by202')+' E81 actual Tate/source import and the exact F35/F41/K96 topology usages were freshly reopened.'
a['night:P3K.111']['remaining_risk']='The full common/endpoint fixed-stratum atlas supplying CFL(2723,19124) and the IL321-contraction histogram have no attached machine arrays and are not freshly reconstructed here. Historical computation records retain their inherited scope. F41 original chain arrays, K94 simultaneous-source construction and parts of the larger F41/F46/K96 proof chains retain inherited scope. No absolute seed closure is asserted.'
(p/'row_assessments.json').write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')
c=json.loads((p/'K111_coverage.json').read_text())
c['fresh_exact_checks']=244
c['closed_fresh_gate']=c['closed_fresh_gate'].replace('180 exact checks','202 exact checks, including source-band and relative common-lift whole-chart preservation')
c['remaining_gates'][-1]='F35 full proof and E81 complete used subsection reopened. F41 source-chain arrays, K94 simultaneous-source construction and parts of the larger F41/F46/K96 chains retain inherited scope; exact K111-used topology passages were compared.'
c['proof_supplement']='K111_native_star_supplement.tex'
(p/'K111_coverage.json').write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n')
print('Recorded',len(ev),'events;',len(sources['sources']),'source openings;',c['fresh_exact_checks'],'K111 moving/map checks.')
