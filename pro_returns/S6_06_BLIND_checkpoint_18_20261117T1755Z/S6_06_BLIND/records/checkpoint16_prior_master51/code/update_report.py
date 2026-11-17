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
'3.1':('P3F.3–P3F.15, P3F.22–P3F.24, P3K.5–P3K.8','Proved by two independent calculations of the actual return index: the real-trace characteristic formula and the analytic Picard-line index with an explicit marked cap switch. The original reference-fan class is zero with every orientation convention fixed. The all-fan extension previously asserted in P3K.33 is reopened by the scalar-product audit P3K.61; the reference-fan proof is retained.'),
'3.2':('P3F.5–P3F.6, P3F.9–P3F.14, P3K.5–P3K.7','Proved: actual page, twelve I1 fibres, chi(O)=1, signature −8, relative p1=−24, actual line section P and line square −2; the real trace transfers these inputs to the actual return index.'),
'3.3':('P3F.2–P3F.3, P3K.7–P3K.9','Proved: heights and the corrected plus sign for reducible-fibre corrections; the actual normal clutch has zero normal Pontryagin number and yields k=−1, ell=−4 in the explicitly descended rotating-framing convention.'),
'3.4':('P3F.1–P3F.56, P3K.5–P3K.38, P3K.40–P3K.63; reopened compound assertions identified below','INCOMPLETE, with a newly located proof error. The exact fixed-source construction, source/root/cap topology, initial page and line calculations, actual shorter-parameter morphisms, minimal scalar covers, and marked cap-data comparisons remain in their stated independently proved scopes. The reference OS45 family has class25 and its positive covers realize every class in Theta7; the stated universal vanishing is therefore refuted independently of the withdrawn fan recurrence. The fixed-source catalogue retains sixteen profiles, twenty-six source pairs, thirty-one root branches with thirty nonempty branches, and its exact reference values. However P3K.61 proves that the simultaneous marked delta-equivariant three-curve product used in P3K.29 cannot exist for nonzero scalar winding M. The actual outer C1 determinant winds-2M at one branch and0 at the other. P3K.25, P3K.29 and P3K.31 therefore require correction, and the all-fan portions of P3F.52–53 and P3K.33–37,41,43–44 are explicitly reopened. The analogous OS49 outer-marking assertion in P3K.17 is under its own audit. Every earlier proof and audit is preserved, and the affected compound statement labels are Unresolved. P3K.62 supplies the literal scalar C1/C2 native maps, their actual relative squares and the narrow C2 characteristic comparison; it repairs the initial/reflected scalar equality used in P3K.57–58 without the withdrawn universal assertion. The selected-cusp source-loop results P3F.55–56 and P3K.40,42,45–60 use their separately constructed products and the retained local topology/frame arrows. They include the initial class1, fixed-edge class23, ordinary variation and derivative, unselected collision class0, the full vertical-edge source return1-3n(n-1), and the two exact infinite families in P3K.59. For P_j=[[1,-j],[0,1]], j>=0, the class is1-3j(j+1), with its full matrix and derivative; for R_j=[[j+1,-j],[-1,1]], the class is-5-24j(j+1), with least period7 and range{3,15,19,23}. P3K.57 gives the actual source-infinity classes0 and1 on the initial/reflected fans, with the corrected N-5/N-6 analytic bounds and safe geometric orders8 and6. P3K.58 gives the full global groupoid and paired source-zero sums. P3K.60 gives the actual single native pair(1-a,a) and difference Z_JT-Z_T=a. The remaining ordered pair is(-a+k*A_scalar+14e,k*A_scalar+14e), e in{0,1}, with A_scalar=0 or1-3p; no e is selected. The smallest good case is(27,0) or(13,14), and reduced p=k=1 gives(24,26) or(10,12). P3K.63 completes the actual sheared quotient, Euler-line and relative Pontryagin comparison and proves ell(T_n)=0 for every signed n. With the actual integer index A_n it gives native fixed pair(0,-6A_n), V00=6A_n-6 and delta0=-6A_n-6; the existing central residue fixes V00=-18n(n-1) and delta0=-12+18n(n-1) modulo168, without selecting an integer lift. The source-zero global central attachment, the remaining integer fixed-star index, corrected scalar-fan returns, remaining source-moduli loops, added ordinary OS49 clutches and unmarked endpoint sectors remain under proof.'),
'4.1':('P4.1–P4.5','Proved by explicit charts and all integral Mayer–Vietoris matrices.'),
'4.2':('P4.6–P4.58, P4R.1–P4R.20','Proved in the requested irreducible or normal-crossing scope: B=P1, c3 in{0,2}, b3=2−c3, and nonnegative Euler number for every reduced fibre support. The complete normalization classification and equality criterion are P4.58. Every rationally resolved irreducible support has Euler number2; every other irreducible support has Euler number0 and is either a smooth support with a finite unramified torus cover, a singular support with smooth minimal elliptic ruled normalization, or a singular support with smooth minimal Hopf normalization. Positive-b2 class-VII resolutions are excluded. For normal-crossing supports, the Euler number equals the number of triple points; the zero case has smooth Hopf or non-Kahler elliptic normalization components and smooth elliptic conductor with finite unramified branch maps. P4.54 closes every contracted-horizontal ruled case. P4.55–57 and P4R.19–20 close the remaining D4 image without restricting the other transverse type, by the actual cubic spectral map, graph budget, local ribbon normalization and simple-zero identities. P4.10–11 supply the requested hypothesis examples. Broader supplied assertions about arbitrary reducible non-NC supports remain separately undecided.'),
'5.1':('P5.1–P5.4','Blind proof: tangent dimensions (1,1,1,0), smooth one-dimensional miniversal germ.'),
'5.2':('P5.5–P5.6','Blind proof: full automorphism group C*, and parameter period 2Z.'),
'5.3':('P5.7','Proved comparison after checkpoint01: version1 agrees on all four controls; version2 omits the former deformation and automorphism sections.')}
MAP={1:{1:'1.1',2:'1.1;1.4',3:'1.1;1.3',4:'1.4',5:'1.4',6:'1.6',7:'1.4',8:'1.4;1.7',9:'1.2;1.4',10:'1.3;1.5',11:'1.2;1.3',12:'1.3',13:'1.3;1.5',14:'1.6'},2:{1:'2.1',2:'2.3',3:'2.2',4:'2.4',5:'2.4',6:'2.4',7:'2.4',8:'2.5',9:'2.4',10:'2.6',11:'2.6'},4:{1:'4.1',2:'4.1',3:'4.1',4:'4.1',5:'4.1'},5:{1:'5.1',2:'5.1',3:'5.1',4:'5.1',5:'5.2',6:'5.2'}}
comparisons={}
prompt_comparisons=[]
for path in ROOT.glob('code/**/results_mapping.json'):
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
lines+=['','## State and provenance','','This is a live hourly record of an unfinished audit, AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. An undetermined comparison does not assert agreement or disagreement. Each source used is recorded in the chronological literature log and the three agent source logs. The earlier-run proof repository has not been opened. During a bounded read of the supplied Liu–Rollenske construction source, a reviewer unexpectedly encountered an explicitly unchecked commented AI-generated invariants summary. The reviewer stopped, disregarded it and did not reopen it; no explicit earlier-run identifier was visible, and none of that material is used. The exact supplied path, output range, observed time interval and exclusion are recorded in records/checks_comment_encounter.json and the chronological literature log.','','The explicit prompt lead in 2.3 disagrees: the radial origin-difference class is −pn gamma, not pn gamma, in the prescribed positive-loop convention (P2.2). The primitive exterior-square lattice maps to its dual quotient with index two (P1.2). The formula using the rank-two Hodge bundle produces rank one; the rank-four de Rham bundle gives the required rank-three bundle (P1.5). The height correction for reducible fibres has a plus sign when solving for P.O (P3F.2).','','## Remaining mathematical obligations','','The exact outstanding instances, attempted constructions and failures remain in the part notes, working proofs and code outputs. This checkpoint includes an explicit post-checkpoint14 scalar-fan correction. INCOMPLETE, with a newly located proof error. The exact fixed-source construction, source/root/cap topology, initial page and line calculations, actual shorter-parameter morphisms, minimal scalar covers, and marked cap-data comparisons remain in their stated independently proved scopes. The reference OS45 family has class25 and its positive covers realize every class in Theta7; the stated universal vanishing is therefore refuted independently of the withdrawn fan recurrence. The fixed-source catalogue retains sixteen profiles, twenty-six source pairs, thirty-one root branches with thirty nonempty branches, and its exact reference values. However P3K.61 proves that the simultaneous marked delta-equivariant three-curve product used in P3K.29 cannot exist for nonzero scalar winding M. The actual outer C1 determinant winds-2M at one branch and0 at the other. P3K.25, P3K.29 and P3K.31 therefore require correction, and the all-fan portions of P3F.52–53 and P3K.33–37,41,43–44 are explicitly reopened. The analogous OS49 outer-marking assertion in P3K.17 is under its own audit. Every earlier proof and audit is preserved, and the affected compound statement labels are Unresolved. P3K.62 supplies the literal scalar C1/C2 native maps, their actual relative squares and the narrow C2 characteristic comparison; it repairs the initial/reflected scalar equality used in P3K.57–58 without the withdrawn universal assertion. The selected-cusp source-loop results P3F.55–56 and P3K.40,42,45–60 use their separately constructed products and the retained local topology/frame arrows. They include the initial class1, fixed-edge class23, ordinary variation and derivative, unselected collision class0, the full vertical-edge source return1-3n(n-1), and the two exact infinite families in P3K.59. For P_j=[[1,-j],[0,1]], j>=0, the class is1-3j(j+1), with its full matrix and derivative; for R_j=[[j+1,-j],[-1,1]], the class is-5-24j(j+1), with least period7 and range{3,15,19,23}. P3K.57 gives the actual source-infinity classes0 and1 on the initial/reflected fans, with the corrected N-5/N-6 analytic bounds and safe geometric orders8 and6. P3K.58 gives the full global groupoid and paired source-zero sums. P3K.60 gives the actual single native pair(1-a,a) and difference Z_JT-Z_T=a. The remaining ordered pair is(-a+k*A_scalar+14e,k*A_scalar+14e), e in{0,1}, with A_scalar=0 or1-3p; no e is selected. The smallest good case is(27,0) or(13,14), and reduced p=k=1 gives(24,26) or(10,12). P3K.63 completes the actual sheared quotient, Euler-line and relative Pontryagin comparison and proves ell(T_n)=0 for every signed n. With the actual integer index A_n it gives native fixed pair(0,-6A_n), V00=6A_n-6 and delta0=-6A_n-6; the existing central residue fixes V00=-18n(n-1) and delta0=-12+18n(n-1) modulo168, without selecting an integer lift. The source-zero global central attachment, the remaining integer fixed-star index, corrected scalar-fan returns, remaining source-moduli loops, added ordinary OS49 clutches and unmarked endpoint sectors remain under proof. The correction ledger is records/scalar_fan_correction_scope.json, with complete prior files under records/attempts/scalar_fan_premise_correction/. The local common-exterior integral topology and single-star frame arrows remain separately audited and are the only portions of K29/K31 used by the new source-loop proofs. The exploratory second mutation seed is also preserved; the active certificate starts only from the proved initial seed and checks210 bases and128 fans. The unrestricted non-normal-crossing extensions of the supplied Part4 assertions, unidentified extra numerical rows, and any broader claims outside the explicit theorem scopes remain undecided. Part4.2 is proved in its requested irreducible or normal-crossing scope. Parts1,2 and the original blind Part5 retain their recorded proofs and immutable blind hashes. No uncomputed class, missing global filling, or unsupported integer lift is assigned.','','## Reproduction and typesetting','','Every executed program and its recorded output lies under code/. The manuscript inputs the numbered proof files under notes/. Initial LuaLaTeX builds exposed missing system Lua/font packages; the exact build logs are retained. The current checkpoint build is checked in the typesetting review below; every subsequent mathematical addition receives a fresh build and rendering audit before delivery. The manuscript remains a working document.','','No supplied attachment is duplicated in the current checkpoint. All generated proofs, notes, scripts, outputs and current deliverables are included. Full externally retrieved article/book payloads, their OCR/page-image copies, and the extracted copy of supplied AC26 are omitted from checkpoint03 onward; records/source_payload_exclusions.json lists every path and hash. These source copies are replaced in the deliverable by the complete bibliography, chronological read log, URLs and retrieval records. Earlier checkpoints remain unchanged. Superseded mathematical attempts remain included and explicitly identified in their notes.','','Updated '+datetime.now(timezone.utc).isoformat()+'.']
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
