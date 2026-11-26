#!/usr/bin/env python3
"""Stage L0's exact separate guards and review rows; no canonical writes.

The frozen derivation, programs, certificates and outputs are read-only.
The canonical manuscript, event tables and bibliography are read-only.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import re

ROOT=Path(__file__).resolve().parent.parent
STAGE=ROOT/'agents/continuation7_iii_semistable'
P='S6_SERIES_PUBLISH_III_02L0'
ID='maps:src:D.2.25'
NOW=datetime.now(timezone.utc).isoformat()
FROZEN_TIME='2026-11-24T22:46:48.622325+00:00'
WHO=('GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort '
     'not separately exposed; seventh-continuation semistable check')

def digest(s):
    return sha256(s if isinstance(s,bytes) else s.encode()).hexdigest()

def environment(s,kind):
    a=s.index('\\begin{'+kind+'}')
    b=s.index('\\end{'+kind+'}',a)+len('\\end{'+kind+'}')
    return s[a:b]

def write_tsv(name,fields,rows):
    with (STAGE/name).open('w',encoding='utf8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)

def part(s,start,end):
    a=s.index(start);b=s.index(end,a)+len(end)
    return s[a:b]

canonical_bytes=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert digest(canonical_bytes)=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical=canonical_bytes.decode()
old_statement=environment((STAGE/f'{P}_released_statement.tex').read_text(),'theorem')
old_proof=environment((STAGE/f'{P}_released_proof.tex').read_text(),'proof')
assert digest(old_proof)=='871a24c40cc10efe3bd31259fcc5c176150f0361492042d9f9ebe87622b45471'
receiver_path=STAGE/f'{P}_receiving.tex'
new=receiver_path.read_text()
new_statement=environment(new,'theorem');new_proof=environment(new,'proof')
old=old_statement+'\n\n'+old_proof

guards=[]
shadow=canonical
for kind,before,after in [('statement',old_statement,new_statement),('proof',old_proof,new_proof)]:
    assert canonical.count(before)==1,(kind,'old uniqueness')
    line=canonical[:canonical.index(before)].count('\n')+1
    end=line+before.count('\n')
    if kind=='proof':assert (line,end)==(12564,12737)
    guards.append((kind,before,after,line,end))
    shadow=shadow.replace(before,after,1)
for kind,before,after,_,_ in reversed(guards):
    assert shadow.count(after)==1,(kind,'new uniqueness')
    shadow=shadow.replace(after,before,1)
assert shadow.encode()==canonical_bytes

def identities(s):
    return {key:re.findall(pattern,s) for key,pattern in {
        'labels':r'\\label\{([^}]+)\}',
        'hypertargets':r'\\hypertarget\{([^}]+)\}',
        'equation_tags':r'\\tag\{([^}]+)\}'}.items()}
assert identities(old)==identities(new)
assert identities(new)['labels']==[ID]+[f'maps:eq:D.SC{i}' for i in range(1,9)]
assert identities(new)['hypertargets']==['tag-02L0','tag-023Z']+[f'tag-024{i}' for i in range(7)]
assert identities(new)['equation_tags']==[f'D.SC{i}' for i in range(1,9)]

# Source structure only. These checks are deliberately not a TeX build.
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',new):
    side,env=m.groups()
    if side=='begin':stack.append(env)
    else:assert stack and stack.pop()==env,(side,env)
assert not stack
depth=0
for i,ch in enumerate(new):
    if ch not in '{}':continue
    nslash=0;j=i-1
    while j>=0 and new[j]=='\\':nslash+=1;j-=1
    if nslash%2:continue
    depth+=1 if ch=='{' else -1
    assert depth>=0,i
assert depth==0
math=[]
for token in re.findall(r'\\[()\[\]]',new):
    if token in (r'\(',r'\['):math.append(token)
    else:assert math and math.pop()=={r'\)':r'\(',r'\]':r'\['}[token]
assert not math
refs=re.findall(r'\\(?:eqref|ref|SeriesRef|cref|Cref)\{([^}]+)\}',new)
labels=set(re.findall(r'\\label\{([^}]+)\}',canonical))
assert set(refs)<=labels,set(refs)-labels
bib=(ROOT/'S6_SERIES_PUBLISH_references.bib').read_text()
keys=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib))
cites=re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',new)
assert set(cites)<=keys
for bad in ('\\StatementRecord','manifolds\\_semistable','code/','.json','02KY','02KO','root\'s','saved right','Section 10','Formula the','Equation the','[:,'):
    assert bad not in new,bad
assert 'all other caps and logarithmic data fixed' not in new
assert new.count('\\begin{theorem}')==new.count('\\end{theorem}')==1
assert new.count('\\begin{proof}')==new.count('\\end{proof}')==1

frozen={
STAGE/f'{P}_fresh_derivation.md':'e7e3379be1ee99f5ce0226d2f5e0274a41d0f38f7b846c366ca45e1ee48d45fe',
STAGE/f'{P}_fresh_lattice_certificates.json':'54d5c507ad7969601b5c915afec6719770742c1a95f5516f002dba4ca7878cd6',
ROOT/'code/S6_SERIES_PUBLISH_c7_semistable_initial_and_lattice.py':'bfb44a1734658b7dc3783fbe04629ec2c1c4a1a4f31bd67878a2cdaad07aab92',
ROOT/'code/S6_SERIES_PUBLISH_c7_semistable_initial_and_lattice.out':'a77e978337eef413b9ea7d3a002419df8d5ab5c85d1d0a1f67d43c7da6b8b030',
STAGE/f'{P}_fresh_freeze.json':'7f760ae695b1989045cc4c6d6198ecd69fba12c50a50f3f214b2ed831b1a2f03'}
for path,h in frozen.items():assert digest(path.read_bytes())==h,str(path)

write_tsv(f'{P}_replacements.tsv',['statement_id','old_text','new_text'],[
    dict(statement_id=ID,old_text=before,new_text=after) for _,before,after,_,_ in guards])

defects=[]
def defect(kind,suffix,before,after,reason):
    assert before in old,before[:150]
    assert not after or after in new,after[:150]
    matches=[(block,start,end) for _,block,_,start,end in guards if before in block]
    assert len(matches)==1,(kind,suffix,'ambiguous guarded block')
    block,start,end=matches[0]
    loc=start+block[:block.index(before)].count('\n')
    assert start<=loc<=end
    defects.append(dict(change_id=f'c7-III-02L0-{suffix}',type=kind,statement_id=ID,
        old_location=f'S6_SERIES_PUBLISH_III.tex:{loc}',old_page='',
        new_location=str(receiver_path.relative_to(ROOT)),
        new_page='pending final typeset page concordance',old_text=before,new_text=after,
        reason=reason,review_status='staged; root admission, source application and final page review pending'))

defect('D25','specified-fan-action',
    part(old_proof,'At the zero, index one makes the valuation lattice',
         r'normal bundle $\mathcal O(-1)_{+1}\oplus\mathcal O(-1)_{-1}$.'),
    part(new_proof,r'The construction of \SeriesRef{maps:src:D.2.23} uses the Jordan basis',
         'The fan transport below relates this marking to the physical-circle fan.'),
    'The literal OS47 I2 zero with (a,b)=(7,1) has physical coordinates (-1,2) in the specified short basis. Its two actual fan charts have weights (-1,-1,2) and (1,-2,1), including isolated fixed vertices and order-two stabilizers. Index one does not prove the printed action assertion. The complete receiving proof retains the Jordan fan and supplies a finite actual Farey-flip sequence, exact cone/link maps, the integral Thom induction, nullhomotopy and relative-ball diffeomorphisms. It then constructs and transports the required action. The final oriented theorem, including even M, is proved unchanged.')
defect('D25','original-i2-global-obstruction',
    part(old_statement,'including original-versus-Mumford choices:',r'local defect in \ref{maps:src:D.2.22}.'),
    part(new_statement,'including the original and Mumford choices.',r'rows gives a free direct summand in \(H_2(X;\mathbb Z)\).'),
    'In the natural OS47 row (a,b)=(7,2) with zero at I1, its extra original I2 cap has line degrees (-1,+1), b4(U)=2, b1(boundary)=4 and b1(U)=2, so its local degree-two cokernel defect is zero. The complete fresh proof gives a primitive global mu cycle by explicit Bezout boundary coordinates and the transported cusp-disc right inverse. Its MV boundary coefficient splits H2 onto Z. The original-cap exclusion and sphere table are retained with this proved global assertion.')
defect('D22','unsupported-cancellation-step',
    part(old_proof,'Cancellation by the full Zhubr invariants',
         'including the two-primary refined invariant.'),
    part(new_proof,'Composing the bundle gauges, the normal map,',
         'every simply connected regular-log datum.'),
    'Unproved cited-step gap, repaired: the admitted 02KO proof supplies direct geometric reconstruction and does not establish the invoked full-invariant cancellation for this family. Replace the unsupported invocation by the complete unstabilized oriented identification, with inverse maps and the even-M mod-two spin calculation. The framed surgery and stabilized conclusion are separately retained. This row records a gap repair under the used-and-rechecked event; it is not a refuted mathematical claim, a refutation of a general Zhubr classification theorem, or a claimed new two-primary invariant calculation.')
defect('D09','program-bookkeeping',
    part(old_proof,r'The exact program \texttt{manifolds\_semistable\_catalogue.py}',
         'certificate, not a numerical rank inference.'),
    part(new_proof,'For each row of the displayed complete list, integer elimination gives matrices',
         'These formulas give the displayed integer identities and their inverse coordinates.'),
    'State the exact integer elimination, primitive graph bases and their inverse product identities in the proof. The new independently written source, full output and certificate are recorded outside the paper for the later programs table. The historical program was neither opened nor rerun.')
defect('D01','historical-implementation-credit',
    part(old_proof,'The implementation accepts the general multi-site matrix',
         'and verifies its comparison with all constant graph presentations.'),'',
    'Remove a claim about the earlier implementation. The complete all-site transfer proof and the new pre-exposure computation establish the mathematical comparison; the old program receives no new execution or verification credit.')
defect('D09','action-code-narration',
    part(old_proof,'The code\nchecks these component statements',
         'two unit\nSmith factors at every such site.'),
    part(new_proof,'At a regular logarithmic central torus, simple connectivity gives',
         'including order one and either sign or zero of a permitted\nnumerator.'),
    'Replace code narration by the complete primitive-circle coordinate maps. The rank-one local periods and the regular-root Bezout covector give the actual free action. The false cusp-fan inference is separately corrected.')
defect('D10','machine-header',
    next(line for line in old_statement.splitlines() if line.startswith(r'\StatementRecord')),
    r'\textnormal{\small tag 02L0.}',
    'Retain the permanent label and hypertarget and print the small tag. Mathematical dependencies appear at their precise scope in the receiving proof; graph/check navigation remains in the records.')
defect('D02','defensive-integrality',
    'The argument\nidentifies the full integral kernel, including its index, not only\nits rational span.',
    'These give the complete boundary map and\nits inverse on the fibre quotient.',
    'Give the actual integral maps, sections and inverse coordinates positively. The full normal-transfer argument proves the index without the defensive contrast.')
defect('D02','defensive-group-sentence',
    'The fundamental group is exactly \\eqref{maps:eq:D.FG1}, rather than merely the\nabelian group in degree one.',
    r'The fundamental group is given by \eqref{maps:eq:D.FG1}.',
    'State the group formula directly. The proof invokes and verifies the admitted complete group presentation at its actual parameter scope.')
defect('D11','closing-scope-disclaimer',
    part(old_statement,'For $b>1$,', 'those torsion types is asserted here.'),
    part(new_statement,'For $b>1$,','Every such output is excluded by the sphere criterion.'),
    'State the proved b>1 homology and sphere exclusion positively, explicitly retaining the already present simply-connected hypothesis for SC4. This clarification is not a new D26 scope finding.')
defect('D14','proof-organization',
    r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
    r'\medskip\noindent\emph{Exact construction inputs and conventions.}',
    'Organize the complete proof by construction, integral maps, all-parameter homology, exact fan transport and oriented reconstruction. Preserve all eight auxiliary equation identities and settle each original proof item. Later unit restructuring and final page review remain open.')
defect('D23','poincare-accent',
    'Integral Poincare duality',r"Poincar\'e duality",
    'Supply the accent in the mathematical prose; source check only, with final typeset review pending.')
write_tsv(f'{P}_defects.tsv',[
 'change_id','type','statement_id','old_location','old_page','new_location','new_page',
 'old_text','new_text','reason','review_status'],defects)

event_file=f'{P}_CHECK_EVENTS.tsv'
events=[]
def event(kind,suffix,phase,source,scope,outcome,when=NOW):
    row=len(events)+2
    events.append(dict(statement_id=ID,date=when[:10],who=WHO,type=kind,outcome=outcome,
      event_id=f'publish:c7:III:02L0:{suffix}',phase=phase,source_file=source,source_row='1',
      source_event_type=kind,evidence_group=f'publish:c7:III:02L0:{scope}',
      publish_input_file=str((STAGE/event_file).relative_to(ROOT)),publish_input_row=str(row),
      date_utc=when,where=str((STAGE/f'{P}_comparison.md').relative_to(ROOT))+'; '+str(receiver_path.relative_to(ROOT))))
event('targeted proof check','fresh-complete-derivation','before whole original L0 exposure',
      str((STAGE/f'{P}_fresh_derivation.md').relative_to(ROOT)),'fresh-semistable-derivation',
      'Before original exposure, derived all 62 natural rows, their 17 b=1 cases, actual local period and chart maps with inverses, permitted original-cap comparison and global primitive-mu obstruction for every other original cap. Proved primitive graph/fibre splittings, every regular-root Thom column, arbitrary finite site counts and all integral lifts, zero-Euler free MV extension, complete groups, global CRT inverse maps, sphere criterion and full oriented smooth classification including even M. Kept the specified Jordan fan and constructed actual finite flips, exact link maps, nullcurve Thom induction and relative-ball diffeomorphisms. Root read all 1631 proof lines, all 556 program lines and all 130 output lines before release.',FROZEN_TIME)
event('computation or formal certificate','fresh-integral-maps','before whole original L0 exposure',
      'code/S6_SERIES_PUBLISH_c7_semistable_initial_and_lattice.py','fresh-semistable-derivation',
      'New independently written program, with historical target algorithms and root-held candidate computation closed, derived 62 natural rows and 17 b=1 rows from literal component equations. It verified all integer graph, fibre and cusp inverse identities, 842 specified actual fan flips, 576 presentation cases, 352 CRT inverse comparisons and 576 full-vector lift inverses. Complete source and output read by checker and root. These are exact finite validation of the written universal maps, sharing evidence with the fresh derivation; no bound is used to prove the all-parameter theorem.',FROZEN_TIME)
event('refuted, with the refined statement\'s id','local-assertions-corrected','after whole original L0 exposure',
      str((STAGE/f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)),'post-exposure-local-corrections',
      'Refined identity remains maps:src:D.2.25. Refuted the literal-fan semifree assertion by the allowed OS47 I2 (a,b)=(7,1) ray weights (-1,-1,2) and (1,-2,1), and the blanket positive-local-defect explanation by the OS47 (7,2) extra original I2 cap with local defect zero. Complete actual fan transport and the primitive global mu splitting prove the original smooth and sphere conclusions. This refutation event covers precisely those two counterexamples. No main conclusion is withdrawn; no new D26/D27 finding.')
event('computation or formal certificate','post-exposure-auxiliary-identities','after whole original L0 exposure',
      'code/S6_SERIES_PUBLISH_c7_semistable_auxiliary.py','post-exposure-local-corrections',
      'New independent Leibniz determinant expansion proves all five SC7 cofactors and all SC8 two-by-two minors as symbolic polynomial identities, including n=0; the mathematical Bezout argument identifies the invariant ideals. The two literal toric ray matrices and inverse physical cocharacter map verify the fan counterexample. Source and complete output read. This is post-exposure auxiliary evidence and imports no historical program.')
event('used and rechecked in this run','whole-original-comparison','after whole original L0 exposure',
      str((STAGE/f'{P}_comparison.md').relative_to(ROOT)),'complete-original-comparison',
      'After individual release at 22:53:02.322574 UTC, read the whole original statement and proof, including all eleven items, all eight labelled formulas, historical code assertions, original-cap scope, surgery, projectable spin and final even-M smooth claim. Compared every clause with the frozen derivation and complete receiver. The cited full-invariant cancellation is an unproved step at the claimed 02KO scope; its gap is repaired by the complete unstabilized geometric map, without a refutation of a general cancellation theorem or new refined-invariant calculation. Root identified a stronger relative assertion in the frozen fresh auxiliary: each individual flip map is relative to its own transported outer ball boundary, while the final composition is a global oriented diffeomorphism; pointwise preservation of all other caps or simultaneous preservation of earlier ball boundaries is not established. The receiver and post-exposure note now give exactly this proved scope, with frozen bytes retained and the physical-fan representative separately constructed from the same other fillings. Preserved all nine labels/hypertargets and eight equation tags. Separate unique statement/proof guards reverse to exact canonical bytes; source structure, references and frozen hashes pass. Old algorithms receive no new run credit. No TeX build, page review, canonical mutation or global-table completion is claimed.')
write_tsv(event_file,['statement_id','date','who','type','outcome','event_id','phase',
 'source_file','source_row','source_event_type','evidence_group','publish_input_file',
 'publish_input_row','date_utc','where'],events)

print('L0 exact separate guards and complete local packet: PASS')
print('Staged at',NOW)
for kind,before,after,line,end in guards:
    print(kind,'canonical lines',line,end,'old SHA256',digest(before),'new SHA256',digest(after))
print('Both guards unique; forward/inverse memory substitution recovers canonical bytes: PASS')
print('Identities:',identities(new))
print('Source environments, braces, math delimiters, reference targets and citation keys: PASS')
print('Reference targets:',sorted(set(refs)))
print('Citation keys:',sorted(set(cites)))
print('Frozen files verified unchanged:',len(frozen))
print('Defect rows:',len(defects),'Event rows:',len(events),'Separate replacement rows:',len(guards))
print('Receiver SHA256',digest(receiver_path.read_bytes()))
for suffix in ['comparison.md','post_exposure_auxiliaries.md','replacements.tsv','defects.tsv','CHECK_EVENTS.tsv']:
    p=STAGE/f'{P}_{suffix}'
    print(str(p.relative_to(ROOT)),'SHA256',digest(p.read_bytes()))
print('No TeX compile or rendered-page claim. No separately captured empty stderr claim.')
print('Canonical/global files and all frozen fresh bytes remain unchanged.')
