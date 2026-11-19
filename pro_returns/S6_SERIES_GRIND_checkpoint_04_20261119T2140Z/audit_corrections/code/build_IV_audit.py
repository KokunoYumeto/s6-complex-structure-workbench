from pathlib import Path
import csv,datetime,hashlib,json,re

OUT=Path(__file__).resolve().parents[1]
SRC=OUT.parents[1]/'S6_SERIES_GRIND_source'/'S6_GRIND_1_papers_cp15'
s=(SRC/'S6_10_PAPERS_IV.tex').read_text()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
with (OUT/'CHECK_EVENTS.tsv').open() as f:events=list(csv.DictReader(f,delimiter='\t'))
def event(label,kind,outcome):
    d=dict(statement_id=label,date='2026-11-19',who=who,type=kind,outcome=outcome,phase='S6_SERIES_GRIND')
    d['event_id']='s6sg:'+hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest()[:20]
    if not any(e['event_id']==d['event_id'] for e in events):events.append(d)
labels=re.findall(r'\\label\{(iv:correction:[^}]+)\}',s)
assert len(labels)==33
rows=[]
for lab in labels:
    a=s.index('\\label{'+lab+'}');pa=s.index('\\begin{proof}',a);pb=s.index('\\end{proof}',pa)
    suffix=lab.split(':')[-1]
    verdict='holds at the stated retained-input scope'
    remaining='The original source, cap, page and native-product constructions remain the named proved inputs; this event does not re-prove their entire dependency chain.'
    outcome=('Before opening this receiving proof, derived its explicit correction implication from the stated physical duality and named retained construction results in IV_corrections_prereading.md. Then read the complete receiving proof and compared every step, including the actual fan/parameter/endpoint map where used. The printed implication agrees with that derivation. '+remaining)
    if suffix=='P3K.22':
        verdict='wording repair required: degree-two homology'
        outcome=('Opening the retained source night:P3K.22 equation (P3K.22.1) revealed that its injected cap term is direct_sum_i(Z/m_i)^2 -> H_2(Y;Z), while the receiving statement calls it a first homology contribution. The exact rim-cycle Mayer--Vietoris map supplies the sphere obstruction in degree two. proposed_patches.json replaces the phrase with the explicit H_2 injection. The reference index arithmetic and m_i=1 conclusion are unchanged. The frozen prereading note initially inherited the receiving H_1 wording; this source audit repairs that error rather than crediting it as a successful check. '+remaining)
    event(lab,'targeted proof check',outcome)
    rows.append(dict(label=lab,proof_lines=f'{s.count(chr(10),0,pa)+1}-{s.count(chr(10),0,pb)+1}',
                     verdict=verdict,new_derivation='IV_corrections_prereading.md',
                     explicit_source_proof='IV_correction_proofs.txt',
                     independent_computation='code/independent_IV_checks.py and .json',
                     credit_limit=remaining))

event('iv:rank_two_specialization','targeted proof check',
 'Read all nine steps after the statement; then independently checked the integral source normalization complex, the full-unit proper deformation and q-preserving stratum flow, the monomial map to the nodal product, and the global Cartier cross line. The proof supplies actual source-to-target family maps and unit-preserving line cocycles. The later computation is independently implemented after source reading and is not labeled a before-reading re-proof.')
event('iv:rank_two_specialization','computation or formal certificate',
 'Fresh independent_IV_checks.py derives the toric restriction matrix from its six ray divisors, computes Smith forms, constructs every exterior-power monodromy matrix, and obtains integral invariant ranks (1,2,4,2,1) with primitive constraints. It also verifies the exact cross-line quadratic cocycle. No older S6 code is read or imported; geometric existence of the family flow and descended Cartier bundle is checked in the separate proof event.')
for lab in ['iv:i3_all_reduced_caps','night:P3K.108']:
    event(lab,'targeted proof check',
     'Read every step of the complete nine-step proof, then its K103 OC.1-3 source/root, Cartier and norm-lift inputs. Verified the analytic height ratio and fixed branch, signed norm mR=G, graph-line comparison through coincidence, exact sector words, weighted contraction, cap product relative to the prescribed common boundary, and source reference arc. The separate equality of k and ell follows from connections pulled back from each five-dimensional cap quotient body, matched by the full collar line/tangent maps; neither equality is inferred only from the index. The initial K106 characteristic pair is a retained input, not independently recomputed here.')
    event(lab,'computation or formal certificate',
     'Fresh independent_IV_checks.py recomputes the original discriminant roots and rational selected-height map, actual root substitutions for nine cap orders, all signed meridian matrices, three A2 chart identities, the sixfold point by fresh chord/tangent addition, the full formal unit at its coincidence, and the middle-chart translation x arrow by polynomial remainder. It checks the exact fan reflection adapter -J*T_j*R0^2*swap=T_(1-j), the signed vertical index, and all 28 K106 fan witness values from a new linear-system solver. The sampled root substitutions supplement the displayed universal exponent identities; they are not presented as proof for arbitrary l by enumeration.')
for lab,scope in [
    ('night:P3K.71','selected-cusp integral prism algorithm, the two-step class 1 and the witnessed odd residues'),
    ('night:P3K.73','whole-zero scalar integral prism algorithm, the OS45 two-step class 11, original repeated-Q0 class 3, and explicit all-28 witnesses'),
    ('night:P3K.77','OS49 component-line integral prism algorithm, two-step class 7, and explicit all-28 witnesses at k=1'),
    ('night:P3K.106','selected-I3 integral prism algorithm, increments 48 and 300 and integer 356, with explicit all-28 witnesses by depth seven'),
    ('night:P3K.100','exact sixteen-element closed-form image for every primitive pair, reduced modulo 112'),
    ('night:P3K.107','exact sixteen-element closed-form image for every primitive pair, reduced modulo 112')]:
    event(lab,'computation or formal certificate',
        'Fresh independent_IV_checks.py checks the '+scope+'. The program derives target matrices and derivatives by rational Gaussian elimination of the prism equations, then compares the printed reconstruction formulas. It imports no earlier code. For the closed-form images it checks every primitive residue vector modulo112 and records the complete polynomial period; the audit explains primitive lifting. This verifies the stated algebraic consequences and explicit finite witnesses, not the full geometric derivation of these large receiving theorems.')
for lab in ['iv:correction:P3K.56','iv:correction:P3K.59','iv:correction:P3K.60']:
    event(lab,'computation or formal certificate',
        'Fresh independent_IV_checks.py verifies the exact polynomial image and period, or solves both source-zero congruences exhaustively for all residues and both branches. The receiving proof supplies the universal period or multiplication-by-two kernel argument, so the finite computation has an explicit exhaustive domain.')
event('night:P5.7','used and rechecked in this run',
 'Opened both attached DGKX version-specific sources. The v1 assertions and their theorem locators match P5.3-P5.6 in the fixed standard-data scope; the v2 mathematical sections omit those four assertions. P5_7_insertion.tex supplies the exact affine map a=c+delta, delta=beta_part-beta0, its inverse, identical marked period matrix, and transported admissible half-plane. The beta difference descends to P1 and is constant. This event verifies the source comparison, not a new deformation-theory proof.')
for lab in ['night:P1.6','night:P1.14']:
    event('maps:src:F.4.1','used and rechecked in this run',
     'Missing night source row '+lab+' is accounted for in missing_night_rows.json as the reported independent Wall/Kramer-Stolz classification route to this conclusion. Its register and report are attached, but the registered notes/part1.tex proof file is not. The independently written implication in fourfold_classification_prereading.md and its separate event supply a fresh scoped derivation; importing this historical record is not credited as another new mathematical proof.')
event('series:IV:frontmatter','used and rechecked in this run',
 'Grouped all nineteen inherited IV rung blocks into seven full main statements A-G and 5/6/7/6/6/7/7 precise outline steps, with source, physical line, fan, cap, character, scalar and endpoint scopes. Preserved the exact mapping-torus covering morphism and family/construction/class/positive-cover table. This is an editorial and linkage audit, not a new proof of every main theorem.')

with (OUT/'IV_high_risk_audit.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome','event_id','phase'],delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'receiving_corrections':len(rows),'all_new_events':len(events),'repairs':['iv:correction:P3K.22: H2 injection'],
                  'generated':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2))
