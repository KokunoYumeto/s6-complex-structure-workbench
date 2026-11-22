#!/usr/bin/env python3
"""Reconstruct reviewed intentions as newly dated, exact unapplied guards."""
from pathlib import Path
import importlib.util,json,hashlib,datetime,re
ROOT=Path(__file__).resolve().parents[3]
AREA=ROOT/'agents/ii_infra/recovery_20261121'
spec=importlib.util.spec_from_file_location('packets',ROOT/'code/S6_SERIES_PUBLISH_II_packets.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
src=p.parse_source(ROOT/'S6_SERIES_PUBLISH_II.tex','II')
blocksdir=AREA/'second_group_blocks';blocksdir.mkdir(exist_ok=False)
marker=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
plain=r'\begin{enumerate}[leftmargin=*]'
def block(owner):
 r=src['statement_labels'][owner];return src['text'][r['start']:max([r['end']]+[x['end'] for x in r['proofs']])]

edits={
'01F4':('cdp:st:C.3.1',[
 ('title',r'\begin{proposition}\hypertarget{tag-01F4}',r'\begin{proposition}[Smooth fibres of an algebraic reduction]\hypertarget{tag-01F4}','D16','Supply the mathematical subject in the title.'),
 ('smoothscope','compact complex threefold with $b_1(Y)=b_2(Y)=0$ and $a(Y)=1$.','smooth compact complex threefold with $b_1(Y)=b_2(Y)=0$ and $a(Y)=1$.','D25','State the intended smooth ambient scope used by tangent bundles, duality and the proof; no singular-total-space claim is asserted.'),
 ('announcement','For completeness we derive the Kodaira-dimension restriction directly.\n','', 'D08','Begin with the actual pluricanonical construction.'),
 ('classification','We now apply the Enriques--Kodaira classification in the form of\n\\cite[Theorem 3.1]{Peters1990}.','The Enriques--Kodaira classification is given in\n\\cite[Theorem 3.1]{Peters1990}.','D08','Remove a proof announcement while retaining the exact classification input.'),
 ('torsiontail','No assertion about torsion in $H_1(F;\\Z)$ was used.\n','', 'D02','Remove the retrospective scope disclaimer; the statement and the complete proof already specify the cohomology coefficients.'),
 ('iteration_marker',marker,plain,'D03','Remove the production iteration marker from the fully reread proof.'),
]),
'01FB':('cdp:st:C.3.5',[
 ('title',r'\begin{proposition}\hypertarget{tag-01FB}',r'\begin{proposition}[Euler numbers of fibre supports]\hypertarget{tag-01FB}','D16','Name the mathematical identity.'),
 ('scopetail','The identity alone assigns no sign to the summands.\n','', 'D11','Remove the repeated limitation after the exact equality has been stated.'),
]),
'01F6':('cdp:st:C.3.11',[
 ('title','[Proved complete cohomological dichotomy]','[Full-fibre cohomology and direct images]','D16','Replace production status with the mathematical objects.'),
 ('grammar','is a two-torus, a primary or secondary Hopf surface of','is a two-torus or a primary or secondary Hopf surface of','D24','Make the stated alternatives grammatical without changing the list.'),
 ('scopetail',' The first line records a cohomological\nalternative rather than a positivity assertion about\nthe splitting of $R^1f_*\\OO_Y$.','','D02/D11','Remove the repeated splitting disclaimer; the exact direct-image relation remains in the table.'),
 ('recaptail',r'$H^1(Y,\OO_Y)=\C\beta$, as asserted.',r'$H^1(Y,\OO_Y)=\C\beta$.','D08','Retain the exact exponential-sequence identification and remove its recap phrase.'),
 ('iteration_marker',marker,plain,'D03','Remove the production iteration marker.'),
]),
'01GB':('cdp:st:D.2.4',[
 ('title','[Proved sign in the full normal-crossings class]','[Euler number in the normal-crossings class]','D16','State the actual equality rather than production status.'),
 ('standing','For the threefolds and maps in D.2 whose reduced fibre supports','For the threefolds and maps in \\ref{cdp:st:D.2.1} whose reduced fibre supports','D06/D25','Bind the standing hypotheses to the exact already repaired smooth-total-space statement.'),
 ('recaptail',' In this class there are no\npositive-Euler-number examples with trivial monodromy.','','D11','Remove the duplicated zero-Euler consequence after the displayed equality.'),
 ('iteration_marker',marker,plain,'D03','Remove the production iteration marker.'),
]),
'01F9':('cdp:st:C.3.3',[
 ('computation_scope','For an entirely finite verification, the attached program enumerates\nthese points in $\\Q(\\sqrt5)^4$, verifies unit norm and all 14,400\nmultiplication-table entries, and computes its commutator subgroup.\nEvery element is a commutator, in particular $G^{\\rm ab}=0$.\nThis is an exact computation over rational pairs representing\n$\\Q(\\sqrt5)$.','Multiplication of the listed coordinates is closed in $\\Q(\\sqrt5)^4$,\nand the commutator map on this finite group is surjective.\nEvery element is therefore a commutator, and $G^{\\rm ab}=0$.','D09','Keep the exact finite algebraic claims, including every-element commutator surjectivity. Move program method, execution count and scalar-field notation to the single end table.'),
 ('iteration_marker',marker,plain,'D03','Remove the production iteration marker from the reread proof; no new independent event.'),
]),
}

# A single paragraph is appropriate for the one-step Euler proof; its entire
# mathematical text is retained and explicitly compared below.
fb=block('cdp:st:C.3.5')
a=fb.index(r'\begin{proof}');proof=fb[a:]
newproof=proof.replace(marker+'\n\\item \n\\noindent\\textbf{Step 1.} ','').replace('\n\\end{enumerate}','')
assert newproof!=proof
edits['01FB'][1].append(('proofparagraph',proof,newproof,'D03/D08','Remove the repeated Step 1 and iteration/list wrapper from the single proof paragraph; all substantive math and references remain.'))

sha=lambda v:hashlib.sha256(v.encode() if isinstance(v,str) else v).hexdigest()
inline=lambda s:re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',s,re.S)
display=lambda s:re.findall(r'\\\[(.*?)\\\]',s,re.S)
refs=lambda s:re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef)\{[^}]*\}|\\CompendiumRef\{[^}]*\}\{[^}]*\}|\\cite(?:\[[^\]]*\])?\{[^}]*\}',s)
guards=[];blocks=[]
for tag,(owner,items) in edits.items():
 before=block(owner);after=before;gg=[]
 for suffix,old,new,typ,reason in items:
  assert after.count(old)==1,(tag,suffix,after.count(old))
  after=after.replace(old,new,1)
  g={'id':f'II-infra-recovery-group2-{tag}-{suffix}','statement_id':owner,'tag':tag,'source_sha256':src['sha256'],'before':old,'after':new,'type':typ,'reason':reason,'comparison_record':str((AREA/'S6_SERIES_PUBLISH_II_second_group_comparison.json').relative_to(ROOT))}
  gg.append(g)
 removed=[r'$\langle1\rangle$'];added_refs=[]
 if tag=='01F4':removed.append(r'$H_1(F;\Z)$')
 if tag=='01F6':removed.append(r'$R^1f_*\OO_Y$')
 if tag=='01F9':removed.append(r'$\Q(\sqrt5)$')
 if tag=='01GB':added_refs=[r'\ref{cdp:st:D.2.1}']
 ia=inline(before)
 for s in removed:ia.remove(s[1:-1])
 assert ia==inline(after),(tag,'inline')
 assert display(before)==display(after),(tag,'display')
 rr=refs(after)
 for s in added_refs:rr.remove(s)
 assert refs(before)==rr,(tag,'refs')
 paths={}
 for side,text in [('before',before),('after',after)]:
  f=blocksdir/f'S6_SERIES_PUBLISH_II_{tag}_{side}.tex';f.write_text(text)
  key='original_full_block' if side=='before' else 'proposed_full_block';paths[key]=str(f.relative_to(ROOT));paths[key+'_sha256']=sha(text)
 for g in gg:g.update(paths);g['named_block_inline_removals']=removed;g['named_block_reference_additions']=added_refs;guards.append(g)
 blocks.append({'tag':tag,'statement_id':owner,**paths,'guard_ids':[g['id'] for g in gg],'named_inline_removals':removed,'named_reference_additions':added_refs,'all_displays_identical':True,'all_previous_references_retained_in_order':True,'new_independent_event_eligible':tag!='01F9'})
 print('COMPLETE PROPOSED '+tag+'\n'+after)

# The full end table is archived to bind the exact transfer from the F9 proof.
s=src['text'];a=re.search(r'\\section\*?\{Programs\}',s).start();b=s.index(r'\begin{thebibliography}',a);before=s[a:b]
old=r'Tangent index; integral monodromy and compact surface calculations (\cref{cdp:st:C.1.1})'
new=r'Tangent index; integral monodromy; Kodaira and Hopf surfaces; 120 unit quaternions, 14,400 products and a surjective commutator map over $\Q(\sqrt5)$ represented by rational pairs (\cref{cdp:st:C.1.1,cdp:st:C.3.2,cdp:st:C.3.3})'
assert before.count(old)==1;after=before.replace(old,new)
paths={}
for side,text in [('before',before),('after',after)]:
 f=blocksdir/f'S6_SERIES_PUBLISH_II_program_table_{side}.tex';f.write_text(text);key='original_full_block' if side=='before' else 'proposed_full_block';paths[key]=str(f.relative_to(ROOT));paths[key+'_sha256']=sha(text)
guards.append({'id':'II-infra-recovery-group2-program-table','statement_id':'tab:II:programs','tag':'program_table','source_sha256':src['sha256'],'before':old,'after':new,'type':'D09','reason':'Place the verified D_exact_checks.py finite-group method and count in the sole program table, with exact C3.2/C3.3 associations. The scalar field notation is transported from the F9 proof.','named_inline_additions':[r'$\Q(\sqrt5)$'],'named_reference_map':{'before':r'\cref{cdp:st:C.1.1}','after':r'\cref{cdp:st:C.1.1,cdp:st:C.3.2,cdp:st:C.3.3}'},**paths})
print('COMPLETE PROPOSED PROGRAM TABLE\n'+after)

receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'recovery_status':'New exact reconstruction after CP14 restoration; not a claim to recovered historical guard bytes.','historical_final_guard_sha256_missing':'a7d7342e79b94a60c68df5a0c2e5e3571cb558512791d13b3e407bdf119ffade','source_sha256':src['sha256'],'status':'UNAPPLIED; complete actual pair review and root approval required','guards':guards,'blocks':blocks,'program_table':paths,'canonical_files_modified':False,'events_added':0}
f=AREA/'S6_SERIES_PUBLISH_II_second_group_guards.json';assert not f.exists();f.write_text(json.dumps(receipt,indent=2)+'\n');print('GUARDS',str(f.relative_to(ROOT)),sha(f.read_bytes()),len(guards))
