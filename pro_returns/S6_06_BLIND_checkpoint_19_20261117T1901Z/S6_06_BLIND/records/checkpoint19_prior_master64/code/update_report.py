"""Rebuild the live audit register from this run's proofs and comparison records."""
from pathlib import Path
import csv, json, re
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT.parent/'background/data/stated_values.csv'
ITEMS={
'1.1':('P1.1–P1.3','Proved: exact matrices, invariant groups, affine freeness and the integral exterior-square comparison.'),
'1.2':('P1.9, P1.11','Proved: charts, properness, strata, collapse and all indices.'),
'1.3':('P1.3, P1.10–P1.13, P1.19','Proved: van Kampen, integral complement/Mayer–Vietoris computation and independent complete cellular computation, including the forced nonzero cusp Ext term, every differential and every Smith certificate.'),
'1.4':('P1.2, P1.4–P1.5, P1.7–P1.9, P1.15–P1.16','Literal rank-three Hodge formula and integral primitive identification corrected. Global periods proved; two independent numerical methods agree beyond 30 digits, with certified transversality bound.'),
'1.5':('P1.10, P1.13, P1A.1–P1A.4','Proved: construction, canonical bundle, full Hodge table, algebraic dimension, full automorphisms, all tangent cohomology and Chern numbers.'),
'1.6':('P1.6, P1.14','Proved: oriented diffeomorphism, including the homotopy-sphere issue, by opened classification theorems.'),
'1.7':('P1.8, P1.15–P1.18, P1A.3–P1A.6','Proved: exact Frobenius definition and globally certified minimum, admissible half-plane, parameter injectivity, smooth miniversal germ, absence of real structures for the fixed marking and Kuhn fan, and no analytic extension across either parameter end.'),
'2.1':('P2.1','Proved for every marked admissible twist, with the collar retained.'),
'2.2':('P2.3','Proved: explicit proper smooth partial filling and component rotations.'),
'2.3':('P2.2','Refuted sign: the radial coefficient is −pn, with the conventions fixed in the prompt.'),
'2.4':('P2.4–P2.7, P2.9','Proved: unrestricted proper Hausdorff analytic nonexistence, all admissible twists and coprime higher families.'),
'2.5':('P2.8','Proved: explicit p=−5 formulas and nonexistence.'),
'2.6':('P2.10–P2.11','Proved proper flat untwisted filling; the proposed central space in Conjecture 8.2 is refuted.'),
'3.1':('P3F.3–P3F.15, P3F.22–P3F.24, P3K.5–P3K.9, P3K.67–P3K.74', 'Proved original reference-fan class0, with both independent methods and the physical/dual morphism. K73 computes every actual fan for the specified original positive loop; its28 explicit fan witnesses realize all of Theta7, including class3 on basis((1,-2),(0,1)). The broader all-fan zero assertion is false.'),
'3.2':('P3F.5–P3F.6, P3F.9–P3F.14, P3K.5–P3K.7, P3K.68–P3K.69', 'Proved actual page and line-square inputs. K68 corrects K6: the meridian-one class restricts to the Hermitian dual of the source line. Its square and the zero reference index are retained.'),
'3.3':('P3F.2–P3F.3, P3K.7–P3K.9, P3K.68–P3K.69', 'Proved heights, reducible-fibre correction and rotating normal clutch. The displayed descended pair(-1,-4) is the meridian-one U pair; the physical M pair is(1,4). K68 proves the exact circle, orientation and gluing dictionary. The index is zero in both conventions.'),
'3.4':('P3F.1–P3F.56, P3K.5–P3K.79; exact corrected scopes below', 'INCOMPLETE. K71 now computes the actual selected-cusp source return on every GL2Z lattice-basis fan, with the full source, period, Cox, cap and closing maps. K72 proves the complete scalar vertical-seed integer pair, and K73 gives a terminating exact algorithm for every fan of the specified whole-zero I1 canonical scalar families and their constructed shorter endpoints. For the original K=L=1 family with its literal positive AC parameter loop, explicit verified fan witnesses realize all28 elements of Theta7; the basis((1,-2),(0,1)) has class3. An independent program solved86 full target systems for the28 witnesses. K70 independently gives primitive OS45 class11 on basis((2,-1),(-1,1)); the selected-cusp source loop there has class1. K74 refutes eight formerly open compound numerical assertions by actual counterexamples and replaces their whole-zero scalar formulas with K73. F52 is reproved through its actual invariant-divisor family isomorphism and return conjugacy. The fixed-source cap/site comparisons give the appropriate integer iterate of this actual scalar return. K68--69 retain the exact physical/dual line and orientation correction, with physical class A_M=-A_U. The source-zero paired constraints remain (k*A_scalar+14e,a+k*A_scalar+14e), e=0 or1, with A_scalar=0 or3p-1. The smallest good pair is(0,1) or(14,15); reduced p=k=1 gives(2,4) or(16,18). The active finite real cut construction has the explicit source resolution, Cartier line, associated UV=q chart, cap endpoint and charged ruling-end data, but the complete oriented attachment has not been proved. K65 supplies OS49 negative-diagonal classes-3k on r and-k on the shorter w-loop, with positive-diagonal class0. K76 completes every OS49 vertical-edge fan as an integer: A_r=-m*(n-1)^2 and A_w=-k*(n-1)^2, with physical pairs (2j-6j*(n-1)^2,8j), j=m or k. Its full bottom-row collar, exact positive-fan reference and actual degree-three endpoint are retained. K77 computes every OS49 lattice-basis fan, with its actual shorter endpoint and marked cap-data iterates. Its image on either loop is exactly gcd(k,28)Z/28; all28 k=1 witnesses have166 independent full target solves. The basis((2,-1),(-1,1)) gives shorter class7. K78 completes every fixed marked smooth order-one OS49 translation clutch by the full integral root-groupoid H2=Z plus Z/k and actual holomorphic source/line/cap maps. The signed norm is D=n+m*sum(psi(ell_i)); sphere sectors D=+/-1 have the K77 return on every fan and the specified transported shorter endpoint. K79 proves the full holomorphic automorphism group C* for all these fixed OS49 sphere data, using actual base recovery, the integral centralizer, local inversions and the full affine torsor obstruction. Every specified holomorphic scalar endpoint has winding L=Nk and return N S_k(P). K75 retains the source-zero global attachment, further ordinary/singular-site scopes, marked source-moduli loops and endpoint sectors outside this completed fixed-source OS49 scope. Source-zero now has the exact two-node/Tate/Cartier map, both full finite faces with their oriented product-ball boundary, a positive-width charged-shape comparison and the actual spin lift. The global fixed-cap and period-strip equation remains under audit; its exceptional class and each end must be counted once. No unknown central class is assigned.'),
'4.1':('P4.1–P4.5','Proved by explicit charts and all integral Mayer–Vietoris matrices.'),
'4.2':('P4.6–P4.58, P4R.1–P4R.20','Proved in the requested irreducible or normal-crossing scope: B=P1, c3 in{0,2}, b3=2−c3, and nonnegative Euler number for every reduced fibre support. The complete normalization classification and equality criterion are P4.58. Every rationally resolved irreducible support has Euler number2; every other irreducible support has Euler number0 and is either a smooth support with a finite unramified torus cover, a singular support with smooth minimal elliptic ruled normalization, or a singular support with smooth minimal Hopf normalization. Positive-b2 class-VII resolutions are excluded. For normal-crossing supports, the Euler number equals the number of triple points; the zero case has smooth Hopf or non-Kahler elliptic normalization components and smooth elliptic conductor with finite unramified branch maps. P4.54 closes every contracted-horizontal ruled case. P4.55–57 and P4R.19–20 close the remaining D4 image without restricting the other transverse type, by the actual cubic spectral map, graph budget, local ribbon normalization and simple-zero identities. P4.10–11 supply the requested hypothesis examples. Broader supplied assertions about arbitrary reducible non-NC supports remain separately undecided.'),
'5.1':('P5.1–P5.4','Blind proof: tangent dimensions (1,1,1,0), smooth one-dimensional miniversal germ.'),
'5.2':('P5.5–P5.6','Blind proof: full automorphism group C*, and parameter period 2Z.'),
'5.3':('P5.7','Proved comparison after checkpoint01: version1 agrees on all four controls; version2 omits the former deformation and automorphism sections.')}
MAP={1:{1:'1.1',2:'1.1;1.4',3:'1.1;1.3',4:'1.4',5:'1.4',6:'1.6',7:'1.4',8:'1.4;1.7',9:'1.2;1.4',10:'1.3;1.5',11:'1.2;1.3',12:'1.3',13:'1.3;1.5',14:'1.6'},2:{1:'2.1',2:'2.3',3:'2.2',4:'2.4',5:'2.4',6:'2.4',7:'2.4',8:'2.5',9:'2.4',10:'2.6',11:'2.6'},4:{1:'4.1',2:'4.1',3:'4.1',4:'4.1',5:'4.1'},5:{1:'5.1',2:'5.1',3:'5.1',4:'5.1',5:'5.2',6:'5.2'}}
comparisons={}
prompt_comparisons=[]
for path in ROOT.glob('code/**/results_mapping.json'):
    if any(part in ('attempts','archive','archived') for part in path.relative_to(ROOT).parts):
        continue
    obj=json.loads(path.read_text())
    if isinstance(obj,dict) and any(isinstance(obj.get(k),list) for k in ('comparisons','fully_compared_rows','compound_rows_not_marked_agree_prematurely')):
        for c in obj.get('comparisons',[])+obj.get('fully_compared_rows',[]):
            c=dict(c);c['proof']='; '.join(c.get('proof_ids',[])) or c.get('proof','')
            comparisons[c['run']+' '+c['id']]=c
        for c in obj.get('compound_rows_not_marked_agree_prematurely',[]):
            c=dict(c);c['proof']='; '.join(c.get('proof_ids',[])) or c.get('proof','')
            c['value']=c.get('state','');c['verdict']='undetermined'
            comparisons.setdefault(c['run']+' '+c['id'],c)
        prompt_comparisons.extend(obj.get('prompt_statements_not_separate_csv_rows',[]))
    elif isinstance(obj,dict):
        comparisons.update({k:v for k,v in obj.items() if isinstance(v,dict)})
def put(run,id,value,proof,verdict='agrees'):
    comparisons[f'{run} {id}']={'value':value,'proof':proof,'verdict':verdict}
for id in ('B.4.30','B.4.33'):
    put('S6_02_PUSH',id,'No proper Hausdorff analytic filling after any finite cover.','P2.4–P2.7')
put('S6_02_PUSH','A.3.1','Virtual top Chern number is constant in the stated proper flat lci smoothing.','P2.11')
put('S6_02_PUSH','A.3.2','The specified self-glued central space has virtual Euler number 0; the smooth fibres have Euler number 2.','P2.11')
put('S6_02_PUSH','B.1.1','The actual semiabelian bundle has the explicit twelve-cycle filling.','P2.3')
put('S6_02_PUSH','B.1.2','The finite actions extend freely, with shifts 4 and −3 in the default datum.','P2.3')
put('S6_02_PUSH','B.4.18','The two logarithmic origins and their explicit overlaps give the punctured-bidisc filling.','P2.1–P2.3')
put('S6_02_PUSH','B.4.19','Proper smooth-total flat partial filling, missing only the corner.','P2.3')
put('S6_02_PUSH','B.4.31','Every horizontal parameter-central meridian is a multiple of delta.','P2.4–P2.6')
put('S6_02_PUSH','B.4.32','The ordinary radial class modulo delta is zero.','P2.6')
put('S6_04','F.1.1','The index-d Kuhn cusp has Euler number 6d.','P1.9')
put('S6_04','F.2.5','The specified fourfold has the stated integral, hence rational, topology and signature.','P1.10–P1.13')
put('S6_04','F.2.6','Three-connected, with H4=Z^4 and no homology torsion.','P1.12')
put('S6_04','F.3.6','Global transverse periods with bounded cusp correction exist.','P1.8')
put('S6_04','F.3.7','The specified free quotient and Kuhn fillings are holomorphic and compact.','P1.9–P1.10')
put('S6_04','F.4.1','The complex fourfold is oriented diffeomorphic to 3HP2#(−HP2).','P1.14')
put('S6_03','D.2.7','All the stated values hold, with integral matrices supplied.','P4.1–P4.5')

# Exact corrected-line I1star comparisons; supplied narrow qualifiers remain undefined.
put('S6_04','D.2.27','The actual corrected-line weighted I1star constructions in P3F.36/38 give spheres. The supplied natural-profile qualifier is not defined, so its narrower scope remains undecided.','P3F.36; P3F.38','undetermined')
put('S6_04','D.2.49','The actual primitive boundary torsion cancels in the corrected-line weighted sphere construction. The supplied canonical qualifier does not identify its exact tuple.','P3F.36','undetermined')
put('S6_04','D.2.50','The exact line O(aG-O-L0) produces the proved sphere tuples; the supplied sixteen corrected-line tuples are not identified in the row.','P3F.36; P3F.38','undetermined')

def expanded_ids(text):
    found=set()
    for m in re.finditer(r'\b(P\d+[A-Z]*\.)(\d+)(?:[–-](?:P\d+[A-Z]*\.)?(\d+))?',text):
        prefix,start,end=m.groups();start=int(start)
        for n in range(start,int(end)+1 if end else start+1):found.add(prefix+str(n))
    return found
statements=[]
proof_files=[(p,ROOT/f'notes/part{p}.tex') for p in (1,2,3,4,5)]
proof_files += [(1,ROOT/'notes/part1_analytic.tex'),(1,ROOT/'notes/part1_endpoints.tex'),(1,ROOT/'notes/part1_arithmetic.tex'),(3,ROOT/'notes/part3_characteristics.tex'),(4,ROOT/'notes/part4_unibranch.tex'),(5,ROOT/'notes/part5_comparison.tex')]
seen={path.resolve() for _,path in proof_files}
for p,path in proof_files:
    if not path.exists():continue
    for name in re.findall(r'\\input\{(notes/[^}]+)\}',path.read_text()):
        child=(ROOT/name).resolve()
        if child.suffix!='.tex':child=child.with_suffix('.tex')
        if child not in seen:
            proof_files.append((p,child));seen.add(child)
for p,path in proof_files:
    if not path.exists():continue
    source_text=path.read_text()
    for m in re.finditer(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{statement\}',source_text,re.S):
        id,status,body=m.groups(); body=re.sub(r'\s+',' ',body).strip()
        short=status.split(';')[0]
        status='Open' if 'Unresolved' in short else ('Refuted' if short.startswith('Refuted') else ('Known' if short=='Known' else 'Proved'))
        n=int(id.split('.')[-1])
        items=MAP.get(p,{}).get(n,f'{p}.2' if p==4 else f'{p}.1')
        if id.startswith('P1A.'):items='1.7' if n in (5,6) else ('1.5;1.7' if n in (3,4) else '1.5')
        if id.startswith('P1.') and n in (15,16,18):items='1.4;1.7'
        if id=='P1.17':items='1.7'
        if id=='P1.19':items='1.3'
        if id.startswith('P3F.'):
            items={1:'3.4',2:'3.3;3.4',3:'3.1;3.3',4:'3.1',5:'3.1;3.2',6:'3.2',7:'3.1',8:'3.1',9:'3.1;3.2',10:'3.2',11:'3.1',12:'3.1;3.2',13:'3.1;3.2',14:'3.1;3.2',15:'3.1',16:'3.4',17:'3.4',18:'3.4',19:'3.4',20:'3.4',21:'3.4',22:'3.1;3.4',23:'3.4',24:'3.4'}.get(n,'3.4')
        if id.startswith('P3K.'):items='3.4' if n>=10 else ('3.3' if n==9 else '3.1;3.2')
        if id.startswith('P4R.'):items='4.2'
        if id=='P5.7':items='5.3'
        controls=[k for k,v in comparisons.items() if id in expanded_ids(str(v.get('proof','')))]
        proof_end=source_text.find('\\end{proof}',m.end())
        proof_text=source_text[m.end():proof_end] if proof_end>=0 else ''
        dependencies=sorted(expanded_ids(proof_text)-{id})
        if (id.startswith('P3F.') and n>=50) or (id.startswith('P3K.') and n>=31):
            local_dependencies=set(dependencies)
            for dm in re.finditer(r'(?<![A-Za-z0-9_.])([FK])(\d+)(?:[–-]{1,2}(?:[FK])?(\d+))?',proof_text):
                letter,lo,hi=dm.groups();lo=int(lo)
                for j in range(lo,int(hi)+1 if hi else lo+1):
                    local_dependencies.add('P3'+letter+'.'+str(j))
            dependencies=sorted(local_dependencies-{id})
        verdicts={str(comparisons[k].get('verdict',comparisons[k].get('comparison','undetermined'))) for k in controls}
        compared=next(iter(verdicts)) if len(verdicts)==1 else '; '.join(k+': '+str(comparisons[k].get('verdict',comparisons[k].get('comparison','undetermined'))) for k in controls)
        statements.append([id,body,status,str(path.relative_to(ROOT)), '; '.join(dependencies),items,'; '.join(controls),compared,m[2]])
if not (ROOT/'notes/part3.tex').exists():
    path=ROOT/'notes/part3_family.md'
    text=path.read_text()
    for m in re.finditer(r'^## (P3F\.\d+)\. (.+)$',text,re.M):
        id,title=m.groups()
        statements.append([id,title,'Proved',str(path.relative_to(ROOT)),'','3.1;3.2;3.3;3.4','','','See exact scope and unresolved application in the proof.'])
with (ROOT/'S6_06_BLIND_results.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','item_of_the_prompt','stated_value_compared (run and id)','agrees_with_stated_value','notes']);w.writerows(statements)
def esc(s):return str(s).replace('|','\\|').replace('\n',' ')
lines=['INCOMPLETE','','| Prompt item | Statements | Current state |','|---|---|---|']
lines += [f'| {i} | {a} | {b} |' for i,(a,b) in ITEMS.items()]
lines+=['','| Stated value | Supplied assertion | Independent value and proof | Comparison |','|---|---|---|---|']
rows=list(csv.DictReader(DATA.open()))
for row in rows:
    key=row['run']+' '+row['id']; c=comparisons.get(key)
    value=(str(c.get('value',c.get('own_value','')))+' '+str(c.get('proof',''))) if c else 'No complete derivation of this full assertion yet; see the relevant part notes for proved portions and failed approaches.'
    verdict=c.get('verdict',c.get('comparison','undetermined')) if c else 'undetermined'
    lines.append(f'| {esc(key)} | {esc(row["statement"])} | {esc(value)} | {esc(verdict)} |')
if prompt_comparisons:
    lines+=['','## Additional explicit prompt comparisons','','| Prompt item | Assertion | Independent value and proof | Comparison |','|---|---|---|---|']
    for c in prompt_comparisons:
        lines.append('| '+ ' | '.join(esc(v) for v in (c['item_of_the_prompt'],c['statement'],c.get('own_value','')+' '+', '.join(c.get('proof_ids',[])),c['comparison']))+' |')
lines+=['','## State and provenance','','This is a live hourly record of an unfinished audit, AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. An undetermined comparison does not assert agreement or disagreement. Each source used is recorded in the chronological literature log and the three agent source logs. The earlier-run proof repository has not been opened. During a bounded read of the supplied Liu–Rollenske construction source, a reviewer unexpectedly encountered an explicitly unchecked commented AI-generated invariants summary. The reviewer stopped, disregarded it and did not reopen it; no explicit earlier-run identifier was visible, and none of that material is used. The exact supplied path, output range, observed time interval and exclusion are recorded in records/checks_comment_encounter.json and the chronological literature log.','','The explicit prompt lead in 2.3 disagrees: the radial origin-difference class is −pn gamma, not pn gamma, in the prescribed positive-loop convention (P2.2). The primitive exterior-square lattice maps to its dual quotient with index two (P1.2). The formula using the rank-two Hodge bundle produces rank one; the rank-four de Rham bundle gives the required rank-three bundle (P1.5). The height correction for reducible fibres has a plus sign when solving for P.O (P3F.2).','','## Remaining mathematical obligations','','INCOMPLETE. K71 now computes the actual selected-cusp source return on every GL2Z lattice-basis fan, with the full source, period, Cox, cap and closing maps. K72 proves the complete scalar vertical-seed integer pair, and K73 gives a terminating exact algorithm for every fan of the specified whole-zero I1 canonical scalar families and their constructed shorter endpoints. For the original K=L=1 family with its literal positive AC parameter loop, explicit verified fan witnesses realize all28 elements of Theta7; the basis((1,-2),(0,1)) has class3. An independent program solved86 full target systems for the28 witnesses. K70 independently gives primitive OS45 class11 on basis((2,-1),(-1,1)); the selected-cusp source loop there has class1. K74 refutes eight formerly open compound numerical assertions by actual counterexamples and replaces their whole-zero scalar formulas with K73. F52 is reproved through its actual invariant-divisor family isomorphism and return conjugacy. The fixed-source cap/site comparisons give the appropriate integer iterate of this actual scalar return. K68--69 retain the exact physical/dual line and orientation correction, with physical class A_M=-A_U. The source-zero paired constraints remain (k*A_scalar+14e,a+k*A_scalar+14e), e=0 or1, with A_scalar=0 or3p-1. The smallest good pair is(0,1) or(14,15); reduced p=k=1 gives(2,4) or(16,18). The active finite real cut construction has the explicit source resolution, Cartier line, associated UV=q chart, cap endpoint and charged ruling-end data, but the complete oriented attachment has not been proved. K65 supplies OS49 negative-diagonal classes-3k on r and-k on the shorter w-loop, with positive-diagonal class0. K76 completes every OS49 vertical-edge fan as an integer: A_r=-m*(n-1)^2 and A_w=-k*(n-1)^2, with physical pairs (2j-6j*(n-1)^2,8j), j=m or k. Its full bottom-row collar, exact positive-fan reference and actual degree-three endpoint are retained. K77 computes every OS49 lattice-basis fan, with its actual shorter endpoint and marked cap-data iterates. Its image on either loop is exactly gcd(k,28)Z/28; all28 k=1 witnesses have166 independent full target solves. The basis((2,-1),(-1,1)) gives shorter class7. K78 completes every fixed marked smooth order-one OS49 translation clutch by the full integral root-groupoid H2=Z plus Z/k and actual holomorphic source/line/cap maps. The signed norm is D=n+m*sum(psi(ell_i)); sphere sectors D=+/-1 have the K77 return on every fan and the specified transported shorter endpoint. K79 proves the full holomorphic automorphism group C* for all these fixed OS49 sphere data, using actual base recovery, the integral centralizer, local inversions and the full affine torsor obstruction. Every specified holomorphic scalar endpoint has winding L=Nk and return N S_k(P). K75 retains the source-zero global attachment, further ordinary/singular-site scopes, marked source-moduli loops and endpoint sectors outside this completed fixed-source OS49 scope. Source-zero now has the exact two-node/Tate/Cartier map, both full finite faces with their oriented product-ball boundary, a positive-width charged-shape comparison and the actual spin lift. The global fixed-cap and period-strip equation remains under audit; its exceptional class and each end must be counted once. No unknown central class is assigned. Parts1,2 and the original blind Part5 retain their independently recorded proofs and immutable original hashes. Part4.2 is proved in the requested irreducible or normal-crossing scope; the separately supplied broader arbitrary non-normal-crossing assertion remains undecided. All earlier false formulas and attempted proofs remain in their identified archives and correction ledgers.','','## Reproduction and typesetting','','Every executed program and its recorded output lies under code/. The manuscript inputs the numbered proof files under notes/. Initial LuaLaTeX builds exposed missing system Lua/font packages; the exact build logs are retained. The current checkpoint build is checked in the typesetting review below; every subsequent mathematical addition receives a fresh build and rendering audit before delivery. The manuscript remains a working document.','','No supplied attachment is duplicated in the current checkpoint. All generated proofs, notes, scripts, outputs and current deliverables are included. Full externally retrieved article/book payloads, their OCR/page-image copies, and the extracted copy of supplied AC26 are omitted from checkpoint03 onward; records/source_payload_exclusions.json lists every path and hash. These source copies are replaced in the deliverable by the complete bibliography, chronological read log, URLs and retrieval records. Earlier checkpoints remain unchanged. Superseded mathematical attempts remain included and explicitly identified in their notes.','','Updated '+datetime.now(timezone.utc).isoformat()+'.']
audits=sorted((ROOT/'records').glob('typesetting_checkpoint*.json'), key=lambda p:int(re.search(r'checkpoint(\d+)',p.name).group(1)))
if audits:
    qa=json.loads(audits[-1].read_text())
    lines+=['','## Most recent checkpoint typesetting review','',
        f"Checkpoint {qa['checkpoint']} contained {qa['pages']} manuscript pages. "
        f"The correction set contained {qa.get('before_over_2pt',qa.get('before_sixth_hour_over_2pt',qa.get('before_fifth_hour_over_2pt',qa.get('before_fourth_hour_over_2pt',qa.get('before_third_hour_over_2pt',qa.get('before_second_hour_over_2pt','unrecorded'))))))} overfull boxes above 2pt; "
        f"the checked build has {qa['overfull_over_2pt']} above 2pt, with a maximum overflow of {qa['max_overfull_pt']}pt. "
        'Rendered pages: '+', '.join(map(str,qa['rendered_pages']))+'. '+qa['visual_inspection'],
        '', 'This review applies to the recorded checkpoint build. Later mathematical additions receive a fresh build and rendering check before delivery.',
        '', 'To reproduce the data-dependent calculations, extract the supplied background ZIP into the sibling background directory. Its attachments are not duplicated in these checkpoints.']
progress=sorted((ROOT/'records').glob('progress_check_*_hours.json'), key=lambda p:int(re.search(r'progress_check_(\d+)_hours',p.name).group(1)))
if progress:
    check=json.loads(progress[-1].read_text())
    lines+=['','## Required progress check','',
        check['checked_utc']+': '+check['decision']+'. '+check['reason'],
        '', ' '.join(check['main_question_progress']),
        '', ' '.join(check['other_open_item_progress']),
        '', 'Next check: '+check['next_progress_check_due_utc']+'.']
(ROOT/'S6_06_BLIND_report.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'statements':len(statements),'prompt_items':len(ITEMS),'stated_values':len(rows),'comparisons_entered':len(comparisons)}))
