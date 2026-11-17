"""Rebuild the live audit register from this run's proofs and comparison records."""
from pathlib import Path
import csv, json, re
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT.parent/'background/data/stated_values.csv'
ITEMS={
'1.1':('P1.1–P1.3','Proved: exact matrices, invariant groups, affine freeness and the integral exterior-square comparison.'),
'1.2':('P1.9, P1.11','Proved: charts, properness, strata, collapse and all indices.'),
'1.3':('P1.3, P1.10–P1.13','Integral topology proved by explicit complement/Mayer–Vietoris matrices. Independent complete cell calculation still being completed.'),
'1.4':('P1.2, P1.4–P1.5, P1.7–P1.9','Literal rank-three Hodge formula and integral primitive identification corrected. Global periods proved. Two independent numerical period calculations and real normalization in progress.'),
'1.5':('P1.10, P1.13','Construction and Chern numbers proved. Full Hodge table and analytic invariants under calculation.'),
'1.6':('P1.6, P1.14','Proved: oriented diffeomorphism, including the homotopy-sphere issue, by opened classification theorems.'),
'1.7':('P1.8','Admissible set expressed by the attained minimum of an explicitly defined real function. Evaluation, real structures and both ends remain under investigation.'),
'2.1':('P2.1','Proved for every marked admissible twist, with the collar retained.'),
'2.2':('P2.3','Proved: explicit proper smooth partial filling and component rotations.'),
'2.3':('P2.2','Refuted sign: the radial coefficient is −pn, with the conventions fixed in the prompt.'),
'2.4':('P2.4–P2.7, P2.9','Proved: unrestricted proper Hausdorff analytic nonexistence, all admissible twists and coprime higher families.'),
'2.5':('P2.8','Proved: explicit p=−5 formulas and nonexistence.'),
'2.6':('P2.10–P2.11','Proved proper flat untwisted filling; the proposed central space in Conjecture 8.2 is refuted.'),
'3.1':('P3F.3–P3F.5, P3F.7–P3F.8','Actual orbit surgery and Hopf-gluing comparison proved. The return map characteristic integers and the two independent determinations of the sphere class remain unresolved.'),
'3.2':('P3F.5–P3F.6','The two degree-twelve covers and their fibre configurations are computed. The geometric page, relative framing, and section identification remain unresolved.'),
'3.3':('P3F.2–P3F.3','Height calculations proved; the sign of reducible-fibre corrections is refuted. Actual return integers remain unresolved.'),
'3.4':('P3F.1–P3F.2','Eight Mordell–Weil entries and 21 configurations enumerated exactly. Full family topology, pages and monodromy remain unresolved; the stated bounded slice supplies no search bounds.'),
'4.1':('P4.1–P4.5','Proved by explicit charts and all integral Mayer–Vietoris matrices.'),
'4.2':('P4.6–P4.14','Normal-crossings assertion and equality classification proved; normal irreducible supports proved smooth. Nonnormal irreducible supports beyond normal crossings remain unresolved. Two omitted conductor singularities located.'),
'5.1':('P5.1–P5.4','Blind proof: tangent dimensions (1,1,1,0), smooth one-dimensional miniversal germ.'),
'5.2':('P5.5–P5.6','Blind proof: full automorphism group C*, and parameter period 2Z.'),
'5.3':('P5.1–P5.6','Independent proof written; comparison source remains unopened until the first hourly checkpoint has been saved.')}
MAP={1:{1:'1.1',2:'1.1;1.4',3:'1.1;1.3',4:'1.4',5:'1.4',6:'1.6',7:'1.4',8:'1.4;1.7',9:'1.2;1.4',10:'1.3;1.5',11:'1.2;1.3',12:'1.3',13:'1.3;1.5',14:'1.6'},2:{1:'2.1',2:'2.3',3:'2.2',4:'2.4',5:'2.4',6:'2.4',7:'2.4',8:'2.5',9:'2.4',10:'2.6',11:'2.6'},4:{1:'4.1',2:'4.1',3:'4.1',4:'4.1',5:'4.1'},5:{1:'5.1',2:'5.1',3:'5.1',4:'5.1',5:'5.2',6:'5.2'}}
comparisons={}
for path in ROOT.glob('code/**/results_mapping.json'):
    obj=json.loads(path.read_text())
    if isinstance(obj,dict) and isinstance(obj.get('comparisons'),list):
        for c in obj['comparisons']:
            c=dict(c);c['proof']='; '.join(c.get('proof_ids',[])) or c.get('proof','')
            comparisons[c['run']+' '+c['id']]=c
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

statements=[]
for p in (1,2,3,4,5):
    path=ROOT/f'notes/part{p}.tex'
    if not path.exists():continue
    for m in re.finditer(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{statement\}',path.read_text(),re.S):
        id,status,body=m.groups(); body=re.sub(r'\s+',' ',body).strip()
        short=status.split(';')[0]
        status='Open' if 'Unresolved' in short else ('Refuted' if short.startswith('Refuted') else ('Known' if short=='Known' else 'Proved'))
        n=int(id.split('.')[-1])
        items=MAP.get(p,{}).get(n,f'{p}.2' if p==4 else f'{p}.1')
        controls=[k for k,v in comparisons.items() if id in str(v.get('proof',''))]
        statements.append([id,body,status,str(path.relative_to(ROOT)), '',items,'; '.join(controls),'See comparison table',m[2]])
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
lines+=['','## State and provenance','','This is a live hourly record of an unfinished audit, AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. An undetermined comparison does not assert agreement or disagreement. Each source used is recorded in the chronological literature log and the three agent source logs. The earlier-run proof repository has not been opened.','','The explicit prompt lead in 2.3 disagrees: the radial origin-difference class is −pn gamma, not pn gamma, in the prescribed positive-loop convention (P2.2). The primitive exterior-square lattice maps to its dual quotient with index two (P1.2). The formula using the rank-two Hodge bundle produces rank one; the rank-four de Rham bundle gives the required rank-three bundle (P1.5). The height correction for reducible fibres has a plus sign when solving for P.O (P3F.2).','','## Remaining mathematical obligations','','The exact outstanding instances and every investigated approach are retained in notes/part1.md, notes/part3_family.md, notes/part4.md and the root Part 2 audit notes. The main unresolved sphere case is the original (3,4) positive-loop return map. Its actual orbit/conifold comparison has been constructed; its characteristic pair has not yet been computed. For the irreducible-fibre sign assertion the remaining case is a nonnormal support whose conductor has more general planar singularities; the regular-locus Euler number has been proved nonnegative. For the fourfold, the full Hodge table, real structures and the ends of the parameter domain remain under calculation.','','## Reproduction and typesetting','','Every executed program and its recorded output lies under code/. The manuscript inputs the numbered proof files under notes/. Initial LuaLaTeX builds exposed missing system Lua/font packages; the exact build logs are retained. The PDF has not yet passed the required final rendering and overflow audit. No PDF is being presented as final.','','No supplied attachment is duplicated in the checkpoint. All generated notes, records, scripts and current deliverables are included. Superseded attempts are retained and explicitly identified in their notes.','','Updated '+datetime.now(timezone.utc).isoformat()+'.']
(ROOT/'S6_06_BLIND_report.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'statements':len(statements),'prompt_items':len(ITEMS),'stated_values':len(rows),'comparisons_entered':len(comparisons)}))
