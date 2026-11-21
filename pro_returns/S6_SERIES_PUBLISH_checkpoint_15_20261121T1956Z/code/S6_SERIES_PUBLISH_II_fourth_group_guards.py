#!/usr/bin/env python3
"""Prepare exact local guards for four released owners; no canonical edit."""
from pathlib import Path
import importlib.util, hashlib, json, datetime, re
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('packets',ROOT/'code/S6_SERIES_PUBLISH_II_packets.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
source=p.parse_source(ROOT/'S6_SERIES_PUBLISH_II.tex','II')
out=ROOT/'agents/ii_infra/fourth_group_guard_blocks';out.mkdir(exist_ok=False)
marker=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
edits={
'01G9':('cdp:st:D.2.2',[
 ('title','[Proved existence and exact Euler number]','[Existence and Euler number under trivial monodromy]','D16','Replace production status with the actual mathematical scope.'),
 ('smooth_holomorphic_scope','The class of compact complex threefolds with $b_1=b_2=0$,\na proper connected-fibre map with smooth two-torus general fibre,','The class of smooth compact complex threefolds with $b_1=b_2=0$,\na proper connected-fibre holomorphic map to a smooth compact curve\nwith smooth two-torus general fibre,','D25','State the exact smooth holomorphic ambient hypotheses required by C.2.G.1 and the proof. Root has read both receiving loci and confirmed they are a macro and a tag table with no mathematical claim.'),
 ('single_step_prefix',marker+'\n\\item \n\\noindent\\textbf{Step 1.} ','','D03/D08','Remove the production iteration marker and duplicated Step 1 wrapper from this single-paragraph proof.'),
 ('single_step_suffix','\n\\end{enumerate}\n\\end{proof}','\n\\end{proof}','D08','Close the single-paragraph proof after removing its redundant one-item list.'),
 ('explicit_local_reference',r'\ref{cdp:st:D.2.3}--4',r'\ref{cdp:st:D.2.3} and~\ref{cdp:st:D.2.4}','D06','Replace the hand-typed range endpoint by its exact label. D.2.4 is the already fully derived and compared local normal-crossing equality statement.'),
]),
'01GH':('cdp:st:E10',[
 ('title','[Counterexample: A fixed positive-genus target in the unrestricted stability assertion]','[Failure of extension over a fixed positive-genus target]','D16','Name the mathematical obstruction directly.'),
 ('iteration_marker',marker,r'\begin{enumerate}[leftmargin=*]','D03','Remove the inherited proof-iteration marker while preserving the proof steps.'),
 ('cech_accent','Compatibility of the Cech transition equations','Compatibility of the \\v{C}ech transition equations','D23','Restore the mathematical name accent.'),
 ('recap','This proves the counterexample with an actual smooth proper\nfamily and its obstruction class. ','','D08','Remove the conclusion recap after the nonzero first-order obstruction has already been derived; retain the following exact E5 summand identification.'),
]),
'01GJ':('cdp:st:E12',[
 ('title','[Counterexample: The universal local-freeness assertion of CDP98, Lemma 1.5]','[A higher direct image with length-one torsion]','D16','Name the computed mathematical object.'),
 ('iteration_marker',marker,r'\begin{enumerate}[leftmargin=*]','D03','Remove the inherited proof-iteration marker.'),
 ('recap','This proves the direct-image,\nlength, and global-cohomology assertions. ','','D08','Remove the assertion recap after the exact derived image and length computation; the fibre calculation remains.'),
 ('kunneth_accent','Fibre Kunneth gives','Fibre K\\"unneth gives','D23','Restore the mathematical name accent.'),
]),
'01GO':('cdp:st:E17',[
 ('title','[Counterexample: The embedded-component omission in the divisor-twisting lemma]','[Sections surviving arbitrary divisor twists]','D16','Name the mathematical conclusion and counterexample phenomenon.'),
 ('iteration_marker',marker,r'\begin{enumerate}[leftmargin=*]','D03','Remove the inherited proof-iteration marker.'),
 ('recap','This proves the exact stable-space formula. ','','D08','Remove the recap after both inclusions have been proved; preserve the associated-prime deduction that follows.'),
]),
}
guards=[];blocks=[]
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
inline=lambda s:re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',s,re.S)
display=lambda s:re.findall(r'\\\[(.*?)\\\]',s,re.S)
ref=lambda s:re.findall(r'\\(?:ref|eqref|SeriesRef)\{[^}]*\}|\\CompendiumRef\{[^}]*\}\{[^}]*\}|\\cite(?:\[[^\]]*\])?\{[^}]*\}',s)
for tag,(owner,items) in edits.items():
 assert list((ROOT/'agents/ii_infra/released_proofs'/tag).glob('*/S6_SERIES_PUBLISH_release_receipt.json'))
 row=source['statement_labels'][owner];a=row['start'];b=max([row['end']]+[x['end'] for x in row['proofs']]);before=source['text'][a:b];after=before;gg=[]
 for suffix,old,new,kind,reason in items:
  assert after.count(old)==1,(tag,suffix,after.count(old))
  after=after.replace(old,new,1)
  g={'id':f'II-infra-group4-{tag}-{suffix}','statement_id':owner,'tag':tag,'source_sha256':source['sha256'],'before':old,'after':new,'type':kind,'reason':reason,'comparison_record':'agents/ii_infra/S6_SERIES_PUBLISH_II_fourth_group_comparison.json'}
  if suffix in ['iteration_marker','single_step_prefix']:g['inline_math_named_removals']=[r'$\langle1\rangle$']
  if suffix=='explicit_local_reference':g['named_reference_additions']=[r'\ref{cdp:st:D.2.4}']
  gg.append(g)
 ia=inline(before);ia.remove(r'\langle1\rangle');assert ia==inline(after),tag
 assert display(before)==display(after),tag
 rr=ref(after); additions=[]
 if tag=='01G9':rr.remove(r'\ref{cdp:st:D.2.4}');additions=[r'\ref{cdp:st:D.2.4}']
 assert ref(before)==rr,tag
 paths={}
 for name,text in [('before',before),('after',after)]:
  f=out/f'S6_SERIES_PUBLISH_II_{tag}_{name}.tex';f.write_text(text);paths['original_full_block' if name=='before' else 'proposed_full_block']=str(f.relative_to(ROOT));paths[('original_full_block' if name=='before' else 'proposed_full_block')+'_sha256']=sha(text)
 for g in gg:g.update(paths);guards.append(g)
 blocks.append({'tag':tag,'statement_id':owner,**paths,'guard_ids':[g['id'] for g in gg],'all_displays_identical':True,'named_inline_removals':[r'$\langle1\rangle$'],'named_reference_additions':additions,'all_previous_references_in_order':True})
 print('COMPLETE PROPOSED '+tag+'\n'+after)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'UNAPPLIED; actual complete comparison and root review required','source_sha256':source['sha256'],'guards':guards,'blocks':blocks,'canonical_mutations':False,'events_added':0}
f=ROOT/'agents/ii_infra/S6_SERIES_PUBLISH_II_fourth_group_guards.json';assert not f.exists();f.write_text(json.dumps(receipt,indent=2)+'\n');print('GUARDS',str(f.relative_to(ROOT)),sha(f.read_bytes()),len(guards))
