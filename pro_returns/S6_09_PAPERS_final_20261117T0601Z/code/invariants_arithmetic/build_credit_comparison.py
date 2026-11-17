"""Reproducible, scope-limited source-credit matrix for all 121 INV/ARI/WB rows.

Literal searches are an index, not a substitute for the recorded original-source
readings.  In particular a negative record never asserts worldwide novelty.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/invariants_arithmetic'
META = dict(checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17 UTC')
rows = json.loads((OUT/'result_audit.json').read_text()) + json.loads((OUT/'working_edition_inventory.json').read_text())
refs = {r['citation_key']: r for r in json.loads((OUT/'references_verified.json').read_text())}
credits = json.loads((OUT/'source_credit_map.json').read_text())
credit_by_key = {r['citation_key']: r for r in credits}

extra_scopes = {
 'AC2026': 'Also original PDF Theorem 5.4(iii) p.32 and its flat-character proof p.35; Theorem 9.1(vi) p.65; Proposition 9.20 p.80; Corollary 9.22 p.81; Remark9.27 p.83. The original PDF, not the transcription, governs the comparison.',
 'DuEtAl2026v1': 'Also §6: weighted-root-base lemma and proof lines8541–8614; root-stack-lift and proper-flat-root-fibration lines8628–8727; cusp-normalization-resolution and cusp-structure-cup lines8768–8877; vertical-log-bundle lines8897–9000; log-tangent-sequence lines9017–9048; structure-direct-images statement and relevant proof lines9154–9235,9275–9306; vertical/horizontal/log tangent calculation lines9312–9364. §7 intrinsic-fibration theorem and proof lines10018–10120. Theorem1.4 exact-period statement lines335–344.',
}
for key, extra in extra_scopes.items():
 old=credit_by_key[key]['opened_locator']
 if key=='AC2026': old=old.split(' Also original PDF Theorem 5.4')[0]
 if key=='DuEtAl2026v1': old=old.split(' Also §6:')[0]
 credit_by_key[key]['opened_locator'] = old+' '+extra
 if key in refs:
  refs[key]['opened_locator'] = credit_by_key[key]['opened_locator']
if 'DuGuoKusakabeXie2026v1' in refs:
 refs['DuGuoKusakabeXie2026v1']['opened_locator'] = refs['DuEtAl2026v1']['opened_locator']
credit_by_key['AC2026']['actual_use'] = credit_by_key['AC2026']['actual_use'].split(' The parameterized Hodge diamond')[0] + ' The parameterized Hodge diamond is already Theorem9.1(vi)/Remark9.21; holomorphic-form vanishing is Proposition9.20; only the value h12=1 and the resulting numerical table require the later computation.'
credit_by_key['DuEtAl2026v1']['actual_use'] = credit_by_key['DuEtAl2026v1']['actual_use'].split(' Also the root-base')[0] + ' Also the root-base Picard/cohomology lemma, root lift, logarithmic vertical splitting, cusp cup pairing, structure direct images and intrinsic bi-anticanonical pencil. INV D1.1 adds the explicit coarse floor-descent formula.'

SOURCES = {
 'AC26': dict(citation_key='AC2026', index_source='sources/audit_cache/inv_ari/AC26_text.txt'),
 'E26': dict(citation_key='Engel2026'),
 'DGKX_v1': dict(citation_key='DuEtAl2026v1'),
}
OTHER_KEYS = ['DuEtAl2026v2','Yang2026','Wang2026','ViaclovskyLog2026','ViaclovskyTwoParameter2026','ViaclovskyCombs2026','LiuRollenske2026','McHugh2018','Angella2018']
for baseline, spec in SOURCES.items():
 spec.update({k:credit_by_key[spec['citation_key']][k] for k in ['local_source','source_sha256','opened_locator']})
 spec.setdefault('index_source',spec['local_source'])

# Per-result search vocabulary.  Every vocabulary is actually searched in all
# three baseline texts and the nine named further sources below.
VOCAB = {
 'A1':['direct image','structure','cup','gamma','logarithmic','cotangent'],
 'A2':['Kodaira','determinant','Eichler','Zagier','Imamo','mu','E_6','E6'],
 'A3':['Hodge','holomorphic form','Dolbeault','Leray','h^{1,2}','eta'],
 'A4':['torsion','relative differential','cotangent','9.21','xy','xyz'],
 'B1':['line bundle','theta','linearization','logarithmic transform','multiplicit','Dolbeault'],
 'B2':['canonical','anticanonical','Veronese','3k','4l','Hodge'],
 'B3':['universal cover','cyclic','cusp','Betti','normalization','Frolicher'],
 'C1':['Frolicher','spectral sequence','d_1','d1','degenerat','Hodge'],
 'C2':['Bott','Aeppli','double complex','McHugh','Angella'],
 'C3':['Bott','Aeppli','Picard','Green','balanced','Gauduchon','SKT','astheno','twelve'],
 'D1':['root','weighted','Picard','tangent','direct image','cohomology'],
 'D2':['Kodaira','Spencer','generator','gamma','deformation'],
 'D3':['Kuranishi','bracket','miniversal','semiuniversal','obstruction'],
 'D4':['twist','Picard','torsion','Fourier','Koszul','10.5','jump'],
 'C.1':['Green','isogen','norm','theta','48','216','special value'],
 'C.2':['Albanese','nome','real locus','antiholomorphic','reflection','exact-period','216'],
 'C.3':['expansion','equianharmonic','lemniscatic','maximum','minimum'],
 'C.4':['Siegel','division','torsion','multiplication','local height','norm'],
 'C.5':['complex multiplication','CM','torsion','class number','j-invariant'],
 'C.6':['height','rank','Gross','Zagier','Sha','Tate','Rubin','canonical'],
 'C.7':['transcenden','sigma','semi-abelian','motivic','Schanuel','compact subgroup','CM'],
 'C.8':['maximum','critical','Mahler','Gaussian','equidistribution','duplication','ray','216'],
}
WB_LINK = {
 'prop:workbench-holomorphic-form-vanishing':'A3.1','thm:parametric-hodge-diamond':'A3.1',
 'thm:frolicher-e2-candidate':'C1.1','prop:period-derivative-determinant':'A2.1',
 'prop:log-relative-direct-images':'A1.2','prop:log-ks-divisor':'A2.1',
 'prop:absolute-cotangent-direct-images':'A1.3','hodge_frolicher:remark:8':'A4.2',
 'thm:h12-scalar':'A2.4','cor:exact-hodge-diamond':'A3.1',
 'thm:exact-bott-chern-aeppli':'C2.2','record:h12-direct-images':'A1.3',
 'lem:bcpr-degree-one-input':'C3.1','lem:bcpr-eta-extension':'A3.2',
 'rem:bcpr-literal-gauge':'C3.8','prop:bcpr-generators-are-bases':'C3.1',
 'thm:bcpr-square-zero-algebra':'C3.3','rem:bcpr-global-gauge-boundary':'C3.8',
 'formula:bcpr-fibre-representatives':'A3.2','formula:bcpr-factor-twelve-chern':'C3.2',
 'lem:hodge-line-audit':'A1.0','lem:finite-normal-order-audit':'B1.0',
 'lem:cusp-structure-sheaf-audit':'A1.0','thm:structure-direct-images-audit':'A1.0',
 'cor:picard-line-audit':'C3.1','thm:uniform-nontorsion-audit':'D4.3',
 'analytic_picard:remark:7':'A1.0',
}

def terms_for(r):
 sid=r['source_id']
 if r['source_run']=='WORKING_INV': sid=WB_LINK[sid]
 group = '.'.join(sid.split('.')[:2]) if sid.startswith('C.') else sid.split('.')[0]
 return VOCAB[group]

def fold(s):
 s=unicodedata.normalize('NFKD',s).casefold()
 s=''.join(c for c in s if not unicodedata.combining(c))
 return re.sub(r'[\\{}"\'`~-]','',s)

SEARCH_SPECS={**SOURCES,**{k:dict(citation_key=k,local_source=credit_by_key[k]['local_source'],index_source=credit_by_key[k]['local_source'],source_sha256=credit_by_key[k]['source_sha256'],opened_locator=credit_by_key[k]['opened_locator']) for k in OTHER_KEYS}}
indexed={k:(ROOT/v['index_source']).read_text(errors='replace').splitlines() for k,v in SEARCH_SPECS.items()}
folded={k:list(map(fold,v)) for k,v in indexed.items()}
search_records=[]

def search(r,key,terms):
 hits=[]
 for term in terms:
  needle=fold(term)
  found=[i+1 for i,line in enumerate(folded[key]) if needle in line]
  hits.append(dict(term=term,count=len(found),line_numbers=found))
 rec=dict(row_key=r['source_run']+':'+r['source_id'],source=key,index_source=SEARCH_SPECS[key]['index_source'],terms=hits)
 search_records.append(rec)
 return dict(record_file='work/invariants_arithmetic/credit_search_log.json',record_key=rec['row_key']+'|'+key,terms_searched=terms,hit_counts={x['term']:x['count'] for x in hits})

MATCHES={}
def match(ids,baseline,locator,relation,full=False,kind='partial_antecedent'):
 for sid in ids.split('|'):
  MATCHES[(sid,baseline)]=dict(locator=locator,relation=relation,full_statement_found=full,kind=kind)

match('A1.0','AC26','Lemma9.12 pp.71–74; Proposition9.13 pp.74–76; Theorem9.1(ii) p.64','The complete structure-sheaf direct-image, fixed gamma-subline, cusp cup pairing and full scheme-fibre assertions are known. The discriminant/root derivation is retained as an expanded proof.',True,'known_result')
match('A1.1','AC26','Remark9.21 p.81; local charts in §§4–5','The logarithmic quotient is named and its required computation is explicitly left open. Local charts are construction input; the claimed exact sequence is not supplied here.',False,'construction_input_only')
match('A1.2|A1.3|A2.1|A2.2|A2.4','AC26','Remark1.3 p.5 and Remark9.21 p.81','The cotangent/direct-image calculation and h12=1 are explicitly uncomputed/expected in AC26. This is an earlier open target, not an earlier proof.',False,'earlier_open_problem')
match('A2.3','AC26','§§2–3 period data; Remark9.21 p.81','The underlying period functions and finite specializations are construction data. The exact inverse-Weierstrass branch identification, normalized zero formula and contact-order proof are not stated in the checked scope.',False,'construction_input_only')
match('A3.1','AC26','Theorem9.1(ii),(iv),(vi) pp.64–65; Proposition9.20 p.80; Remark9.21 p.81','All vanishing statements and the one-integer Hodge diamond are known; h12=1 is only expected, so the exact numerical table is an addition.',False,'partial_antecedent')
match('A3.2','AC26','Proposition9.13 pp.74–76; Lemma9.2 p.65 and §9.1','The invariant gamma and eta classes and the cusp structure frame are known inputs. The full Leray generators, trace-dual list and global Dolbeault lift Q are not given there.',False,'partial_antecedent')
match('A4.1|A4.2','AC26','Remark1.3 p.5; Remark9.21 p.81, original PDF','The source contains the claim being corrected: the degree-one cusp-torsion assertion in Remark9.21 is false. The degreewise local-module proof is a correction of the original itself, not a correction of its transcription.',False,'corrects_source_claim')
match('B1.0','AC26','§§2–5 period/finite-gluing construction; §9.1','Marked period and finite-gluing data are the AC construction. The exact comparison to Engel, reference-scale ambiguity and matrix dictionary are additional comparison work.',False,'construction_input_only')
match('B1.1|B1.2|B2.1','AC26','Propositions9.11,9.13 pp.70–76; Proposition9.20 p.80; Theorem5.4 and Remark5.8 pp.32–35','These supply the original (3,4) case and admissible finite translation twists. They do not state the full (3k,4l) cotangent/Hodge computation.',False,'original_case_only')
match('B2.2|B3.3','AC26','Proposition9.11 pp.70–71','The original canonical line is known. The generalized Veronese ring / degree-n-cover Betti and Frolicher claims are not the proposition stated there.',False,'original_case_only')
match('B3.1|B3.2','AC26','§7 monodromy and homology; Proposition9.13 pp.74–76','Original-family topology and structure direct images are inputs. The n-component universal-cover cotangent correction and exact general-n Hodge table are not found in the checked statements.',False,'construction_input_only')
match('C1.1|C1.2','AC26','Corollary9.22 p.81','Nondegeneration at E1 and injectivity of d1:H01→H11 are already proved. Full E2 degeneration and every differential rank/basis are additional.',False,'partial_antecedent')
match('C3.1','AC26','Proposition9.13 pp.74–76; Theorem10.5(b) pp.88–89','The Picard line, its nowhere-zero gamma section and injective restrictions are known. The global Green representative and Bott–Chern Chern map are additional.',False,'partial_antecedent')
match('C3.2','AC26','Proposition7.27 pp.62–63','The integral factor12/transgression is already present up to the common orientation choice. The explicit exponential comparison and FAMILY sign normalization are expanded here.',False,'partial_antecedent')
match('C3.5','AC26','Remark1.2 p.5; Remark9.27 p.83','The no-Kähler/no-Kähler-current clause follows in the source from b2=0. The additional balanced, strongly Gauduchon, LCK and Hermitian-symplectic exclusions are not all stated there.',False,'partial_antecedent')
match('D1.2|D1.3|D2.1|D3.1','AC26','Theorem9.1(iv),(v) pp.64–65; Proposition9.13 pp.74–76','The structure direct images, one-dimensional holomorphic vector field and Euler characteristic of TX are known. Exact higher tangent cohomology and Kuranishi smoothness are not proved by these assertions.',False,'partial_antecedent')
match('D4.1|D4.2|D4.3|D4.4|D4.5','AC26','Theorem10.5 pp.88–89; §10.5; Proposition10.8 pp.92–94','Nonzero cusp R2 for every twist, generic nonzero H2, Picard restriction and uniform nontorsion are earlier results. The complete stalk lengths, annihilators and all-twist dimensions are additional.',False,'partial_antecedent')

match('B1.0','E26','§1 lines235–280; §2 lines288–390; linearization discussion lines1647–1681','The section-translation lift on a line bundle and contracting-scale construction are Engel’s. INV supplies the precise marked comparison and normalization.',False,'partial_antecedent')
match('B1.1|B1.2|B2.1|B2.2|B3.1|B3.2|B3.3','E26','Main theorem lines882–910; integral homology lines1617–1643; §1 lines235–280','The original order-(3,4) twisted construction and sphere criterion are antecedents. E26 explicitly omits Dolbeault computations and does not give these generalized direct-image/Hodge/cover formulas.',False,'construction_input_only')
match('A3.2|C3.1','E26','Invariant-form discussion and final remark lines1717–1725','The invariant Hodge class of type(1,6), signature(1,1), and invariant covector are known construction data. The stated global representatives/Chern map are not supplied.',False,'construction_input_only')
match('C.6.1|C.6.3|C.6.4','E26','§2 lines288–390','The height1/6 of the elliptic-surface section is prior input. It is a function-field height, not the specialized CM-fibre Néron–Tate heights, local-norm identity or maximum inequality.',False,'construction_input_only')

match('A1.0','DGKX_v1','§6 p2:prop:cusp-structure-cup lines8814–8877; p2:prop:structure-direct-images lines9154–9306','Root-base structure direct images, gamma subline and cusp cup pairing are proved. Coarse direct images follow by the explicit descent used in INV; the precise coarse presentation is retained.',False,'partial_antecedent')
match('A1.1','DGKX_v1','p2:prop:vertical-log-bundle lines8897–9000; p2:lem:log-tangent-sequence lines9017–9048','The vertical logarithmic splitting, logarithmic exact sequence and relative canonical determinant are present on the root base; dualizing and descending gives the cotangent ingredients.',False,'equivalent_root_base_input')
match('A1.2','DGKX_v1','p2:prop:vertical-log-bundle; p2:prop:structure-direct-images; p2:eq:vertical-direct-images lines9312–9323','The root vertical and structure bundles needed by projection formula are known. The six coarse logarithmic-cotangent summands of this row are not separately stated there.',False,'partial_antecedent')
match('B1.0','DGKX_v1','§§2–3 marked core, finite affine action and cusp gluing; §6 vertical-bundle proof','The marked period/affine-gluing family is prior data. The Engel scale and reversed-meridian dictionary is an explicit comparison added here.',False,'construction_input_only')
match('B2.2|B3.3','DGKX_v1','p2:thm:intrinsic-fibration and proof lines10018–10120; p2:eq:canonical-root-pullback','The original-family canonical formula and intrinsic bi-anticanonical pencil are known. The generalized ring and degree-n-cover conclusions are not this theorem.',False,'original_case_only')
match('D1.1','DGKX_v1','p2:lem:weighted-root-base, equations p2:eq:root-picard, root-canonical, weighted-cohomology, lines8541–8614','Picard Z, the root line, canonical O(-7), weighted Čech cohomology and acyclicity are already proved. INV adds the explicit coarse rho_*O(n)=O(d(n)) floor formula.',False,'partial_antecedent')
match('D1.2','DGKX_v1','p2:lem:root-stack-lift lines8628–8678; p2:prop:vertical-log-bundle lines8897–9000; p2:lem:log-tangent-sequence lines9017–9048; p2:prop:structure-direct-images lines9154–9306','All stated root-lift, vertical splitting, structure direct-image and horizontal O(-5) assertions are already present.',True,'known_result')
match('D1.3','DGKX_v1','Theorem6.12 p2:thm:tangent-cohomology lines9445–9487; preceding log/ordinary tangent sequences','The tangent-cohomology vector(1,1,1,0) is exactly known. INV’s full coarse direct-image splitting is additional to the printed theorem statement.',False,'partial_antecedent')
match('D2.1','DGKX_v1','Corollary6.13 p2:cor:tangent-generator lines9490–9510; §6 Kodaira–Spencer calculation; Theorem1.3 lines310–317','The generator xi⊗gamma and isomorphism of the parameter Kodaira–Spencer map are known-source results.',True,'known_result')
match('D3.1','DGKX_v1','Proposition6.16 p2:prop:kuranishi-line lines9876–9917; Theorem1.3 lines310–317','Smooth reduced one-dimensional Kuranishi germ and local miniversality are known. The vanishing primary obstruction is an immediate consequence; INV retains its explicit bracket/gluing proof.',True,'known_result')
match('D4.1','DGKX_v1','Theorem6.12 p2:thm:tangent-cohomology lines9445–9487','Only the untwisted n=0 cohomology vector is supplied. The complete integral Picard-twist formula is not found.',False,'special_case_only')
match('C.2.1|C.2.2','DGKX_v1','Theorem1.4 p2:thm:exact-period lines335–344; connected automorphisms lines9967–10010','Exact 2Z parameter identification and Aut(X)=C* are known inputs. Exact nomes/natural boundary and the antiholomorphic reflection classification are additional statements.',False,'partial_antecedent')

# Working-edition full matches override the partial modern INV statement to
# which a duplicate is attached.  Every distinct proof remains in its appendix.
for sid in ['prop:workbench-holomorphic-form-vanishing']:
 match(sid,'AC26','Proposition9.20 p.80, with full direct period proof; Theorem9.1(vi) p.65','Exactly the vanishing theorem already proved in AC26; this is an expanded rederivation, not a new statement.',True,'known_result')
match('thm:parametric-hodge-diamond','AC26','Theorem9.1(ii),(iv),(vi) pp.64–65; Remark9.21 p.81','Exactly the one-integer Hodge diamond already printed in AC26. The later determination m=1 is a separate result.',True,'known_result')
match('lem:hodge-line-audit','AC26','Lemma9.10 p.70; Proposition9.11 pp.70–71','The finite determinant characters, modular frame, Hodge O(1) line and canonical formula are known. Maps’ full expanded proof is the shared printed destination.',True,'known_result')
match('lem:finite-normal-order-audit','AC26','Theorem5.4(iii) p.32; flat-character proof p.35','Exact normal-line orders3 and4 are already proved by the primitive characters.',True,'known_result')
match('lem:cusp-structure-sheaf-audit','AC26','Lemma9.12 pp.71–74','Cusp dimensions, normalization comparison, gamma/u frame and cup product are already present.',True,'known_result')
match('thm:structure-direct-images-audit','AC26','Proposition9.13 pp.74–76; Theorem9.1(ii) p.64','The structure direct images and full-fibre base-change/gamma conclusions are known; the appendix retains the expanded proof.',True,'known_result')
match('cor:picard-line-audit','AC26','Proposition9.13 pp.74–76; Theorem10.5(b) pp.88–89','Pic(X)=C, the gamma restriction line and injective restriction to every full fibre are known.',True,'known_result')
match('lem:bcpr-degree-one-input','AC26','Proposition9.13 pp.74–76','The distinguished gamma class and nowhere-zero gamma subline are known. The explicit period-coordinate representative is an expanded expression of that class.',False,'partial_antecedent')
match('thm:uniform-nontorsion-audit','AC26','Proposition10.8 and full proof pp.92–94','Exactly the uniform fibrewise nontorsion result, including reduced finite fibres, is already proved. This block belongs to PaperII.',True,'known_result')
match('analytic_picard:remark:7','AC26','Propositions9.13 and10.8; Theorem5.4(iii)','This is provenance commentary comparing proof methods. The normal order and nontorsion conclusions are known; it is not a new independent theorem.',False,'provenance_record')
match('lem:cusp-structure-sheaf-audit','DGKX_v1','p2:lem:cusp-normalization-resolution and p2:prop:cusp-structure-cup lines8768–8877','The normalization-resolution dimensions and nonzero cup pairing are explicitly rederived, with AC26 credit.',True,'known_result')
match('lem:hodge-line-audit','DGKX_v1','p2:prop:vertical-log-bundle lines8897–9000; p2:eq:relative-canonical-bundle; p2:thm:intrinsic-fibration','Root determinant and canonical formulas provide another derivation of the same Hodge/canonical data; the exact WB modular frame is separately expanded.',False,'partial_antecedent')

OTHER_EXTRA={
 'A1.0':['ViaclovskyCombs2026'], 'A1.1':['Deligne1970'],
 'A1.2':['ViaclovskyCombs2026'], 'A2.1':['Serre1973'],
 'A3.1':['AtiyahSinger1963','Serre1955Duality','Ugarte2000'],
 'B1.0':['Schnell19'], 'B1.1':['ViaclovskyLog2026','ViaclovskyCombs2026'],
 'B1.2':['ViaclovskyLog2026'], 'B2.1':['ViaclovskyLog2026'],
 'B2.2':['ViaclovskyLog2026'], 'B3.1':['Yang2026'],
 'C1.1':['Ugarte2000','Angella2018'], 'C1.2':['Angella2018'],
 'C2.1':['Stelzig2021','McHugh2018','Angella2018'],
 'C2.2':['McHugh2018','Angella2018'],
 'C3.1':['Schweitzer2007'], 'C3.2':['Schweitzer2007'],
 'C3.3':['Schweitzer2007'], 'C3.4':['AngellaTomassini2013'],
 'C3.6':['Gauduchon1985','STW2017'],
}
OTHER_DETAIL={
 'Ugarte2000':'General complex-S6 Frolicher/Hodge constraints; E3 degeneration, not the stronger candidate-specific E2 result.',
 'ViaclovskyLog2026':'Theorem1.1 supplies coprime(3k,4l) sphere constructions and invariance of multiplicities; it does not compute the full Hodge table or generalized anticanonical ring.',
 'ViaclovskyCombs2026':'General flat torus direct-image/cup-product results and original-family h0q are antecedents; the source is not a proof of this row’s exact cotangent table.',
 'Yang2026':'Different B(4,6)/C(3,6) construction with r cusp components and rational-homology statements; related comparison, not this degree-n cover theorem.',
 'Schnell19':'Appell–Humbert/Riemann input for complex tori, not the entire family normalization dictionary.',
 'McHugh2018':'General compact complex threefold Bott–Chern dimension formulas specialize after the separately proved Hodge/Frolicher input; exact numerical specialization is recorded as a consequence.',
 'Angella2018':'Complex-six-sphere Bott–Chern/Hodge constraints; exact candidate Hodge inputs must be supplied independently.',
 'Schweitzer2007':'Definitions, harmonic duality and first-Chern normalization are standard input; the candidate-specific products/representatives are not asserted by this general source.',
 'Deligne1970':'Local logarithmic freeness, residues and relative normal-crossing setup, with positive monomial exponents; candidate global direct images are additional.',
 'AtiyahSinger1963':'Hirzebruch–Riemann–Roch for compact complex manifolds and holomorphic bundles; the row is a specialization using the separately verified Chern data.',
 'Serre1955Duality':'Compact complex Serre duality; candidate numerical input is supplied separately.',
 'Serre1973':'Modular valence and simple zero of G3 at i, giving the exact double zero of j−1728; the candidate scalar/determinant calculation is additional.',
}

def external_matches(r):
 sid=WB_LINK.get(r['source_id'],r['source_id']) if r['source_run']=='WORKING_INV' else r['source_id']
 keys=list(dict.fromkeys(r.get('reference_dependencies',[])+OTHER_EXTRA.get(sid,[])))
 aliases={'BanicaStanasila1976':'BS76','McHugh2019':'McHugh2018','RamisRuget1970':'RR70','RamisRugetVerdier1971':'RRV71'}
 matches=[]; excluded=[]
 for k in keys:
  k=aliases.get(k,k)
  if k in ['AC2026','Engel2026','DuEtAl2026v1','DuGuoKusakabeXie2026v1']: continue
  if any(x['citation_key']==k for x in matches): continue
  rec=refs.get(k)
  if not rec or not rec.get('status','').startswith('verified'):
   excluded.append(dict(citation_key=k,status=rec.get('status','not_in_local_verified_ledger') if rec else 'not_in_local_verified_ledger',reason='Not treated as an opened theorem or mathematical support.'))
   continue
  matches.append(dict(citation_key=k,locator=rec.get('opened_locator',''),relation=OTHER_DETAIL.get(k,rec.get('actual_use',rec.get('hypotheses_and_normalization_check','Verified operative theorem/formula input for the proof; no assertion that this source contains the entire specialized row.'))),kind='known_input_or_partial_antecedent',full_statement_found=False,verification_record='work/invariants_arithmetic/references_verified.json'))
 return matches,excluded

result=[]
for r in rows:
 rid=r['source_id']; sid=WB_LINK.get(rid,rid) if r['source_run']=='WORKING_INV' else rid
 terms=terms_for(r)
 item=dict(source_run=r['source_run'],source_id=rid,printed_label=r['printed_label'],statement=r.get('statement',r.get('title','')),paper=r.get('paper','I'),reviewer=dict(META))
 for baseline,spec in SOURCES.items():
  search_evidence=search(r,baseline,terms)
  m=MATCHES.get((rid,baseline),MATCHES.get((sid,baseline)))
  # A WB duplicate does not automatically inherit an unrelated extra clause
  # of the later theorem under which its full proof is placed.
  if r['source_run']=='WORKING_INV' and rid=='lem:finite-normal-order-audit' and baseline in ['E26','DGKX_v1']:
   m=None
  field=dict(status='found' if m else 'not_found_in_checked_scope',citation_key=spec['citation_key'],original_source=spec['local_source'],source_sha256=spec['source_sha256'],actual_reading_scope=spec['opened_locator'],search=search_evidence)
  if m: field.update(m)
  else:
   field.update(full_statement_found=False,kind='bounded_negative',locator='',relation='The precise result was not found in the explicitly listed original-source sections and statement searches. This is not a claim of absence from unread sections or from the literature as a whole.')
  item['found_in_'+baseline]=field
 further,excluded=external_matches(r)
 othersearch={k:search(r,k,terms) for k in OTHER_KEYS}
 item['found_elsewhere']=dict(status='found' if further else 'not_found_in_checked_scope',full_statement_found=False,matches=further,unverified_sources_excluded=excluded,actual_reading_scope=[dict(citation_key=k,locator=credit_by_key[k]['opened_locator']) for k in OTHER_KEYS],additional_opened_theorem_scopes=[dict(citation_key=x['citation_key'],locator=x['locator']) for x in further],search=othersearch,relation='Found entries distinguish general operative inputs or related constructions from the full specialized result. A negative is limited to the nine listed source scopes and recorded searches; it is not a worldwide novelty claim.')
 item['internal_duplicate_or_shared_destination']=dict(taken_over_by=r.get('taken_over_by',''),printed_label=r['printed_label'],proof_file=r.get('printed_proof_file',r.get('candidate_file','')),proof_preservation='All distinct complete proofs are retained; see statement_aliases.json and working_appendix_manifest.json.')
 result.append(item)

assert len(result)==121 and len({(r['source_run'],r['source_id']) for r in result})==121
fields=['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere']
assert all(all(r.get(k,{}).get('status') in ['found','not_found_in_checked_scope'] for k in fields) for r in result)
(OUT/'credit_comparison.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
(OUT/'credit_search_log.json').write_text(json.dumps(dict(metadata=META,method='Case/accent/TeX-punctuation-folded literal terms in original supplied source text. Hits are an index only; all semantic claims are bounded by actual_reading_scope. AC26 PDF controls extracted text. Comments in TeX may appear in search hits; unpublished commented blocks are never credited as theorem statements.',sources=SEARCH_SPECS,records=search_records),indent=2,ensure_ascii=False)+'\n')
with (OUT/'credit_comparison.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['source_run','source_id','printed_label','statement']+fields)
 w.writeheader()
 for r in result:
  flat={k:r[k] for k in ['source_run','source_id','printed_label','statement']}
  for key in fields:
   v=r[key]
   flat[key]=v['status']+' | '+(' ; '.join(x['citation_key']+': '+x['locator'] for x in v.get('matches',[])) if key=='found_elsewhere' else v.get('locator',''))+' | '+v['relation']
  w.writerow(flat)

# Update only owned source ledgers, not the root inventory.
(OUT/'source_credit_map.json').write_text(json.dumps(credits,indent=2,ensure_ascii=False)+'\n')
(OUT/'references_verified.json').write_text(json.dumps(list(refs.values()),indent=2,ensure_ascii=False)+'\n')
for name in ['result_audit.json','working_edition_inventory.json']:
 rr=json.loads((OUT/name).read_text())
 for r in rr:
  r['credit_comparison_record']='work/invariants_arithmetic/credit_comparison.json#'+r['source_run']+':'+r['source_id']
  candidate=r.get('candidate_file')
  if candidate and (ROOT/'deliverables'/candidate).exists():
   r['own_check']['candidate_sha256']=hashlib.sha256((ROOT/'deliverables'/candidate).read_bytes()).hexdigest()
 (OUT/name).write_text(json.dumps(rr,indent=2,ensure_ascii=False)+'\n')
 csvpath=OUT/name.replace('.json','.csv')
 if csvpath.exists():
  with csvpath.open(newline='') as f: old_fields=csv.DictReader(f).fieldnames
  write_fields=list(old_fields or [])
  if 'credit_comparison_record' not in write_fields: write_fields.append('credit_comparison_record')
  with csvpath.open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=write_fields,extrasaction='ignore'); w.writeheader()
   for row in rr: w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})
print(json.dumps(dict(rows=len(result),baseline_counts={k:{s:sum(r[k]['status']==s for r in result) for s in ['found','not_found_in_checked_scope']} for k in fields},search_records=len(search_records)),indent=2))
