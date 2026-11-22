#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,datetime,sys,re
D=Path(__file__).resolve().parent;ROOT=D.parents[2];sys.path.insert(0,str(ROOT/'code'));from S6_SERIES_PUBLISH_II_packets import parse_source
src=parse_source(ROOT/'S6_SERIES_PUBLISH_II.tex','II');st=src['statement_labels']['cdp:st:D.2.8'];end=max([st['end']]+[x['end'] for x in st['proofs']]);old=src['text'][st['start']:end];new=old;edits=[]
def edit(a,b,t,r):
 global new
 assert new.count(a)==1,(a,new.count(a));pos=new.index(a);new=new.replace(a,b,1);edits.append({'before':a,'after':b,'type':t,'reason':r,'sequential_before_offset':pos})
edit('[Proved coherent and integral comparisons for \\ref{cdp:st:D.2.7}]','[Coherent and integral comparisons for \\ref{cdp:st:D.2.7}]','D08','Remove the workflow-status adjective from the title.')
edit('For the exact threefold and markings of \\ref{cdp:st:D.2.7},','For the threefold and markings of \\ref{cdp:st:D.2.7},','D08','Use the named construction directly.')
edit('The map in \\eqref{cdp:eq:D.34} is restriction to the smooth base, and the\ndisplay gives its exact image.','The map in \\eqref{cdp:eq:D.34} is restriction to the smooth base.','D12','Retain the definition of the map and remove the duplicate description of its displayed image.')
edit(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[leftmargin=*]','D04','Remove the printed proof-iteration prefix; preserve the five mathematical steps.')
edit('Statement \\ref{cdp:st:D.1.12} gives its','Proposition~\\ref{cdp:st:D.1.12} gives its','D04','Give the receiving statement its printed theorem kind.')
edit('Therefore (D.25)\nidentifies','Therefore \\eqref{cdp:eq:D.25}\nidentifies','D04/D06','Replace the source-edition equation number by the current label.')
edit('because (D.24) has constant marked periods.','because \\eqref{cdp:eq:D.24} has constant marked periods.','D04/D06','Bind the product-marking equation by its current label.')
edit('of the trivial rank-two bundle, followed by the proved\nbase-change isomorphism,','of the trivial rank-two bundle, followed by the\nbase-change isomorphism,','D08','Remove the status adjective; retain the base-change map.')
edit('In particular all three\nextra fibre components are necessary in the corrected\ncount: $r=6$, $s=3$, and $t\'=4$ give\n$6=3-1+4$.','The three singular fibres have two components each. Thus\n$r=6$, $s=3$, and $t\'=4$ give $6=3-1+4$.','D01/D08','State the component data and equality positively, preserving all four numerical formulas.')
edit('by the integral vanishing\nalready proved.','by the integral vanishing in \\cref{cdp:st:D.2.7}\nand the universal coefficient theorem.','D06/D08','Give the exact construction input and the cohomology transport instead of a vague backward reference.')
edit('This proves the final\nassertion and the exact meaning of the generic locus\nin this example.','','D08','Remove the closing recap after all stated conclusions have been derived.')
for number in ['D.33','D.34','D.35','D.36']:
 m=next(m for m in re.finditer(r'\\\[(.*?)\\\]',new,re.S) if r'\tag{'+number+'}' in m.group(1));a=m.group(0);body=m.group(1).replace(r'\tag{'+number+'}','');b=r'\begin{equation}'+body+r'\end{equation}';edit(a,b,'D04','Use the paper equation counter while preserving the complete mathematical display, label and hypertarget.')
# Validate every literal subedit and inverse; no canonical mutation.
x=new
for e in reversed(edits):
 at=e['sequential_before_offset'];assert x[at:at+len(e['after'])]==e['after'];x=x[:at]+e['before']+x[at+len(e['after']):]
assert x==old
folder=D/'GF_blocks';folder.mkdir(exist_ok=True)
for suffix,text in [('before',old),('after',new)]:(folder/f'S6_SERIES_PUBLISH_II_01GF_{suffix}.tex').write_text(text)
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes) else x.encode()).hexdigest()
# Text-only numbering is removed from the math comparison, with exact mapping.
clean=lambda s:re.sub(r'\\tag\{D\.\d+\}','',s)
def displays(t):return re.findall(r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}',t,re.S)
a=[clean(x or y) for x,y in displays(old)];b=[clean(x or y) for x,y in displays(new)];assert a==b
inlines=lambda t:re.findall(r'(?<!\\)\$([^$]*?)(?<!\\)\$',t,re.S)
i0=inlines(old);i1=inlines(new);assert i0.count(r'\langle1\rangle')==1;i0.remove(r'\langle1\rangle');assert i0==i1
for cmd in ['label','hypertarget']:
 assert re.findall(r'\\'+cmd+r'\{([^}]+)\}',old)==re.findall(r'\\'+cmd+r'\{([^}]+)\}',new)
g={'id':'II-infra-recovery-01GF-presentation','statement_id':'cdp:st:D.2.8','tag':'01GF','source_sha256':src['sha256'],'before':old,'after':new,'type':'D01/D04/D06/D08/D12','reason':'Preserve all mathematics while replacing historical equation numbering and iteration markup, giving exact source locators, and removing workflow adjectives/recaps.','literal_edits':edits,'original_full_block':str((folder/'S6_SERIES_PUBLISH_II_01GF_before.tex').relative_to(ROOT)),'original_full_block_sha256':sha(old),'proposed_full_block':str((folder/'S6_SERIES_PUBLISH_II_01GF_after.tex').relative_to(ROOT)),'proposed_full_block_sha256':sha(new),'comparison_record':str((D/'S6_SERIES_PUBLISH_II_GF_comparison.json').relative_to(ROOT)),'preservation':{'every_display_math_body_identical_after_removing_only_four_number_tags':True,'inline_math_sequence_identical_after_removing_only_iteration_marker':True,'removed_iteration_marker':r'\langle1\rangle','all_labels_and_hypertargets_identical_in_order':True,'reference_additions':['cdp:eq:D.25','cdp:eq:D.24','cdp:st:D.2.7'],'reference_witnesses':'The exact D25/D24 construction formulas were provided by root before freeze; D2.7 states H1=H2=0 in homology, transported to cohomology by UCT in the independent derivation. No old reference is removed.','subedit_forward_inverse_exact':True},'mathematical_scope_changed':False}
f=D/'S6_SERIES_PUBLISH_II_GF_guards.json';f.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':src['sha256'],'guards':[g],'guard_count':1,'literal_edit_count':len(edits),'status':'Prepared only; complete proposed proof reading to be recorded separately.','events_added':0,'canonical_files_modified':False},indent=2)+'\n');print(json.dumps({'path':str(f.relative_to(ROOT)),'sha256':sha(f.read_bytes()),'literal_edits':len(edits),'after_sha256':sha(new)}));print('\nCOMPLETE FINAL PROPOSED BLOCK\n'+new)
