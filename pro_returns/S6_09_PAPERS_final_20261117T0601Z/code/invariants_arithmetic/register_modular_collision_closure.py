"""Register the newly supplied geometric realization and exact source scopes."""
from pathlib import Path
from copy import deepcopy
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'deliverables/work/invariants_arithmetic'
CODE=ROOT/'deliverables/code/invariants_arithmetic'
META=dict(checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17 UTC')
p=WORK/'maps_D_references_verified.json'
refs=json.loads(p.read_text())
by={x['citation_key']:x for x in refs}
by['manFukae02']['opened_locator'] += (' Additional opening for the marked collision repair: '
 '§2.1 p3 and footnote1 (inverse circuit convention); §3.1 pp6–10, full definitions (4),(8),(9); '
 '§3.2 Lemmas3.1–3.2 with proof and equation(11), pp11–13; Lemma4.1 and proof, Theorem4.2 '
 'and Corollaries4.2–4.3, pp21–22; §4.2 basis algorithm pp24–25.')
by['manFukae02']['actual_use'] += (' The naturally marked integral cocycle quotient, including torsion, '
 'is identified with actual Mordell–Weil sections on the two constructed rational surfaces; '
 'their heights are calculated from the opposite rational junction pairing.')
by['manFukae02']['hypotheses_and_normalization_check'] += (' The surfaces are independently constructed and proved rational. '
 'The ordinary ordered matrices A_i are converted to Fukae by reversed circuits '
 'K_i=P_i A_i^(-1) P_i^(-1), charges y_i=P_i q_i. Integral coboundaries become his U1 '
 'exactly, and saturation becomes U2. The marked cut-and-jump argument is printed. '
 'The pairing sign and cross-term reversal are derived explicitly and checked by exact code; '
 'no geometric realization is inferred from a numerical tuple alone.')
by['manSS10']['opened_locator'] += (' Additional opening: §4.5 Table1 p14 (types II, I_n, I_n* from '
 'minimal Weierstrass valuations); §8.2–8.4 pp38–39 (degree bounds, fundamental degree=chi, '
 'canonical formula and rationality criterion for a minimal degree-(4,6) model with singular fibre).')
by['manSS10']['actual_use'] += (' Rationality and exact fibre types of the independent 50/II and 56/II constructions.')
milne=ROOT/'sources/audit_cache/inv_ari/maps_literature/Milne2017.pdf'
record=dict(citation_key='mapsMilne2017',author='James S. Milne',
 title='Modular Functions and Modular Forms (Elliptic Modular Curves), version 1.31',year=2017,
 url='https://www.jmilne.org/math/CourseNotes/MF.pdf',
 retrieved_url='https://www.jmilne.org/math/CourseNotes/MF.pdf?writing=20261117',
 local_source=str(milne.relative_to(ROOT)),source_sha256=hashlib.sha256(milne.read_bytes()).hexdigest(),
 status='verified_for_stated_use',
 opened_locator='Original version1.31 dated22March2017: Proposition2.16 and proof pp34–35; Examples2.19–2.20 and explicit quotient coordinates pp35–36; Proposition2.21 and proof p36; general finite-index compactification p37; Theorem2.22 and complete ramification calculation pp37–38; Proposition4.3 and Remark4.4 p49. Original PDF text read at all these locators; web screenshots returned placeholders and are not claimed as visual inspection.',
 actual_use='Construction and genus of the two finite-index modular covers and normalized modular j-function.',
 hypotheses_and_normalization_check='Theorems apply to arbitrary finite-index subgroups, not only congruence groups. Indices are in PSL2Z; both lifted subgroups contain -I. Ramification at fixed order-three cosets is one, and cusp widths are the sr cycle lengths. Milne uses J normalized to1 at i; the proof uses j=1728J. Coset and actual punctured-surface peripheral calculations are supplied independently, not cited to an omitted drawing.',**META)
if record['citation_key'] in by:by[record['citation_key']].update(record)
else:refs.append(record);by[record['citation_key']]=record
for old,new in [('manBHS19','BHS19'),('mapsZhubr13','ffZhubr13')]:
 rec=deepcopy(by[old]);rec['citation_key']=new;rec['alias_of']=old
 if new in by:by[new].update(rec)
 else:refs.append(rec);by[new]=rec
p.write_text(json.dumps(refs,indent=2,ensure_ascii=False)+'\n')

# Preserve the previously verified entries, adding exact source metadata from
# the archived bibliography, but replace the producing run's notes by our own
# scoped source-opening record.  No old source-verification badge is copied.
src=(ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/S6_04_MAPS_MANIFOLDS_references.bib').read_text()
def entry(key):
 m=re.search(r'@\w+\{'+re.escape(key)+r',',src);assert m,key
 start=m.start();level=0
 for j in range(src.index('{',start),len(src)):
  if src[j]=='{':level+=1
  elif src[j]=='}':
   level-=1
   if level==0:break
 text=src[start:j+1]
 m=re.search(r'\bnote\s*=\s*\{',text)
 if m:
  k=m.end();level=1
  while level:
   level += (text[k]=='{')-(text[k]=='}');k+=1
  text=text[:m.start()]+text[k:]
 text=re.sub(r',\s*,',',',text)
 text=text.rstrip().rstrip('}').rstrip().rstrip(',')
 return text+',\n note={Verified for the exact uses in maps\_D\_references\_verified.json; original source opened by GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC.}\n}\n'
bibpath=WORK/'maps_D_checked_references.bib';bib=bibpath.read_text()
for key in ['BHS19','manKM63','manCDP98','manEngel26','ffThomas56','ffBrown72','mapsKaplan79','ffZhubr13','mapsWhitehead50']:
 if not re.search(r'@\w+\{'+re.escape(key)+',',bib):bib+='\n'+entry(key)
if '@misc{mapsMilne2017,' not in bib:
 bib+='\n@misc{mapsMilne2017,\n author={James S. Milne},\n title={Modular Functions and Modular Forms (Elliptic Modular Curves)},\n year={2017},\n url={https://www.jmilne.org/math/CourseNotes/MF.pdf},\n note={Version 1.31, 22 March 2017; verified for the compactification, ramification, genus and normalized j-function at the exact locators in maps\_D\_references\_verified.json.}\n}\n'
bibpath.write_text(bib)

proof=WORK/'maps_modular_collision_realizations.tex'
run=json.loads((CODE/'maps_D_review/modular_collision_realizations_run.json').read_text())
closure=dict(source_run='WRITING_REPAIR',source_id='MODULAR_COLLISION_50_56',
 printed_label='mapsD:repair:collision-realization',paper='III',kind='Gap filled',
 source_file=str(proof.relative_to(ROOT)),source_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
 source_lines=[1,len(proof.read_text().splitlines())],
 closes='Absent geometric-monodromy-proof.md and j-map-cover realization certificate for archived 50/II and56/II profiles.',
 statement='Actual rational elliptic surfaces, exact positive peripheral matrices, primitive actual section cocycles and heights1/12 and1/30 for both archived marked profiles.',
 proof_scope='Complete modular-cover construction, actual punctured-surface free-group calculation, Weierstrass model or divisor construction, exact lift signs/conjugation, natural integral section-junction identification and primitive generators.',
 computation=run,
 external_dependencies=['mapsMilne2017','manFukae02','manSS10','manMiranda90'],
 credit='Known fibre configurations and MW lattices: Miranda1990 §4 and Fukae2002 Table3 rows50,56. This provider supplies a missing exact geometric marking; no new configuration claim.',
 current_check='Authored full proof and exact independent numerical certificate; supplied to parent for its independent reading.',
 caveats='No claim that arbitrary matrix factorizations or arbitrary local models are geometrically realizable.',**META)
(WORK/'maps_modular_collision_closure.json').write_text(json.dumps(closure,indent=2,ensure_ascii=False)+'\n')
print('Saved modular closure, scoped source additions and bibliography metadata.')
