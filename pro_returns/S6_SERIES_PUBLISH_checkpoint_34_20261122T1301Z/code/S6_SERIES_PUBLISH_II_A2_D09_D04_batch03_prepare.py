#!/usr/bin/env python3
"""Prepare bounded D09/D04 edits, preserving all numbering-marker formats."""
from collections import Counter
from datetime import datetime,timezone
import csv,difflib,hashlib,json,re
from pathlib import Path

R=Path(__file__).resolve().parents[1]
W=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_working'
W.mkdir(exist_ok=True)
p=R/'S6_SERIES_PUBLISH_II.tex';raw=p.read_bytes();s=raw.decode();source_sha=hashlib.sha256(raw).hexdigest()
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
headers=list(re.finditer(r'\\begin\{(?:proposition|theorem|lemma|corollary|definition|example|remark)\}[^\n]*',s))
owners=[('cdp:st:A.2.5','01AJ'),('cdp:st:B1','01BK'),('cdp:st:A.3.2','01AM')]
blocks={};guards=[]
for owner,tag in owners:
    at=s.index('\\label{'+owner+'}');start=next(h.start() for h in reversed(headers) if h.start()<at)
    proof_end=s.index('\\end{proof}',at)+len('\\end{proof}')
    end=next(h.start() for h in headers if h.start()>proof_end)
    blocks[tag]={'owner':owner,'start':start,'before':s[start:end],'after':s[start:end],'guards':[]}


def edit(tag,old,new,types,reason,disposition):
    b=blocks[tag];assert b['before'].count(old)==1,(tag,old)
    assert b['after'].count(old)==1,(tag,old)
    at=b['start']+b['before'].index(old)
    g={'id':f'A2-ED03-{tag}-{len(b["guards"])+1:02}','owner':b['owner'],'tag':tag,
       'old':old,'new':new,'expected_count':1,'defect_ids':types,'reason':reason,
       'mathematical_disposition':disposition,'source_snapshot_sha256':source_sha,
       'source_character_span':[at,at+len(old)],
       'source_byte_span':[len(s[:at].encode()),len(s[:at+len(old)].encode())],
       'source_line_span':[s.count('\n',0,at)+1,s.count('\n',0,at+len(old))+1]}
    guards.append(g);b['guards'].append(g);b['after']=b['after'].replace(old,new,1)


edit('01AJ',
     r'The general criterion (A.4)--(A.5) retains the full conductor and applies without a singularity-type restriction. The exact polynomial identities and exponent computations are recorded in \path{code/A_local_algebra.py} and its output.',
     r'The general criterion (A.4)--(A.5) retains the full conductor and applies without a singularity-type restriction.',
     ['D09'],'Relocate the program description to Programs and map it to the statements actually computed.',
     'The entire AJ statement/proof and all mathematical content of the surrounding general-criterion paragraph remain byte-identical. The historical source computes normal crossings (A.1.2) and pinch/cusp modules (A.2.4), not AJ; the Programs row names the exact former owners.')

edit('01BK',r'In particular the two proposed vanishings hold exactly for $\lambda\ne1$,',
     r'In particular, $H^0(S,N^*_{S/X}\otimes A)$ and $H^0(S,\widetilde\Omega^1_S\otimes A)$ both vanish exactly for $\lambda\ne1$,',
     ['D08'],'Replace the workflow phrase by the two cohomology groups already computed in the statement table.',
     'The two vanishings are a joint condition: the conormal group has dimension d_lambda and the torsion-free cotangent group has dimension zero for every lambda. Thus their simultaneous vanishing is exactly lambda != 1, as before.')
edit('01BK','the normal-crossing conormal identification of Part A with the globally fixed conormal $dt$.',
     r'the normal-crossing conormal identification of \cref{cdp:st:A.1.2} with the globally fixed conormal $dt$.',
     ['D05'],'Resolve Part A to the exact canonical normal-crossings proposition.',
     'The whole supporting proof was read. With x_1=v,x_2=w and conormal dt=d(vw), its map (a,b) -> a*w*dv+b*v*dw is exactly the map used here, in dimension one as allowed by the all-dimensional proof.')
edit('01BK','The coherent Kunneth isomorphism',r'The coherent K\"unneth isomorphism',
     ['D23'],'Restore the accent in Kunneth.','No mathematical text or formula changes.')
old_last='This proves the claim also for all roots of unity, including the identity.'
new_last=old_last+' With the gluing convention of \\eqref{cdp:eq:B.2}, the only exceptional scalar for the conormal vanishing is $1$.'
edit('01BK',old_last,new_last,['D09'],
     'Retain the mathematical gluing convention and exceptional-scalar conclusion from the program paragraph at the end of the proof.',
     'Every root of unity, including the identity, remains covered by the line-bundle extension. The exact descent morphism h -> h(1)-lambda*h(-1) remains in B.2; its scalar 1-lambda proves the exceptional value. The existing eqref token and inline value $1$ are relocated unchanged.')
post='''\\end{proof}



The calculation recovers the local example in the supplied correction note, Lemma 4.3 and Theorem 4.4, with the gluing convention fixed by \\eqref{cdp:eq:B.2}. The computation applies to roots of unity as well: the only exceptional scalar for the conormal vanishing is $1$. The symbolic computation and the exact gluing matrices are recorded in \\texttt{code/B\\_examples.py} and its output.
'''
edit('01BK',post,'\\end{proof}\n',['D01','D04','D09'],
     'Move the historical supplied-note attribution and program/output description to the records; keep the mathematical conclusion in the proof and the verified source link in Programs.',
     'The complete old attribution is preserved verbatim in the before block and guard. The attached CDP report identifies an existing supplied workbench/correction-note/course antecedent; no primary publication is manufactured. The exact original correction note remains unidentified. Its gluing convention and scalar conclusion are printed at the end of item 4.')

am=blocks['01AM']['before']
begin_tail=am.index('\n\\end{enumerate}\n\\end{proof}')
tail=am[begin_tail:]
start_math=tail.index('For this example')
end_math=tail.index('The finite counts')
math_text=tail[start_math:end_math]
finite='The finite counts for $3\\le m\\le12$ and all characters are checked in \\path{code/A_multiple_fibres.py}.'
assert finite in tail
new_tail='\n\n'+math_text+'\n\\end{enumerate}\n\\end{proof}\n\n\n\n\n\n'
edit('01AM',tail,new_tail,['D09','D13'],
     'Move the complete thickening/character calculation into the final proof item, preserving A.13 exactly, and move the finite program range to Programs/records.',
     'All words, inequalities, the character-cardinality formula, its A.13 tag, hypertarget and label are retained in the proof. The only omitted inline expression is the finite execution range $3<=m<=12$, reproduced in the Programs row; it is not a restriction on the uniform theorem. No item or numbering-marker format changes.')

program_rows=r'''Normal-crossing branch generators and pinch/cusp module identities (\cref{cdp:st:A.1.2,cdp:st:A.2.4}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/A_local_algebra.py}{\nolinkurl{A_local_algebra.py}} \\[3pt]
Nodal cubic normalization, descent scalar and cohomology table (\cref{cdp:st:B1}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/B_examples.py}{\nolinkurl{B_examples.py}} \\[3pt]
Finite character counts for $3\le m\le12$ and all characters (\cref{cdp:st:A.3.2}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/A_multiple_fibres.py}{\nolinkurl{A_multiple_fibres.py}} \\[3pt]
'''
anchor='\\end{longtable}}\n\n\\begin{thebibliography}{99}'
assert s.count(anchor)==1
assert all(name not in s[s.index('\\section*{Programs}'):] for name in ['A_local_algebra.py','B_examples.py','A_multiple_fibres.py'])
guards.append({'id':'A2-ED03-Programs-01','owner':'app:II:programs','tag':'','old':anchor,'new':program_rows+anchor,
               'expected_count':1,'defect_ids':['D09'],'source_snapshot_sha256':source_sha,
               'reason':'Add only the three successfully opened historical source paths, with exact proved-owner scopes.'})

summary=[]
for owner,tag in owners:
    b=blocks[tag];before,after=b['before'],b['after'];assert s.count(before)==1
    displays=re.findall(r'\\\[.*?\\\]',before,re.S)
    assert all(after.count(v)==before.count(v) for v in displays)
    assert before.count('\\item ')==after.count('\\item ')
    for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{tag-[^}]+\}',r'\\tag\{[^}]+\}',r'\\eqref\{[^}]+\}',
                    r'\((?:A|B)\.\d+[a-z]?\)',r'\\begin\{enumerate\}\[[^\n]*\]']:
        assert Counter(re.findall(pattern,before))==Counter(re.findall(pattern,after)),(tag,pattern)
    def inline(t):return Counter(re.findall(r'(?<!\\)\$(?!\$).*?(?<!\\)\$',t,re.S))
    missing=inline(before)-inline(after)
    assert not missing or (tag=='01AM' and missing==Counter({'$3\\le m\\le12$':1})),(tag,missing)
    assert not (missing-inline(program_rows))
    recovered=after;inverse=[]
    for g in reversed(b['guards']):
        assert g['new'] and recovered.count(g['new'])==1,(g['id'],recovered.count(g['new']))
        inverse.append({'id':g['id']+'-inverse','owner':owner,'tag':tag,'old':g['new'],'new':g['old'],'expected_count':1})
        recovered=recovered.replace(g['new'],g['old'],1)
    assert recovered==before
    prefix='S6_SERIES_PUBLISH_II_A2_'+tag
    for suffix,txt in [('_before.tex',before),('_after.tex',after),('_exact.diff',''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=prefix+'_before.tex',tofile=prefix+'_after.tex')))]:
        (W/(prefix+suffix)).write_text(txt)
    (W/(prefix+'_inverse_guards.json')).write_text(json.dumps(inverse,indent=2)+'\n')
    summary.append({'owner':owner,'tag':tag,'before_sha256':sha(before),'after_sha256':sha(after),
                    'proof_items_preserved':before.count('\\item '),'all_original_displays_preserved':len(displays),
                    'new_displays':len(re.findall(r'\\\[.*?\\\]',after,re.S)),
                    'numbering_marker_formats_unchanged':True,'all_labels_tags_and_eqrefs_preserved':True,
                    'inline_expressions_transferred_to_Programs':list(missing.elements()),'guard_count':len(b['guards'])})
(W/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_guards.json').write_text(json.dumps(guards,indent=2)+'\n')
(W/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_Programs_rows.tex').write_text(program_rows)
(W/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_Programs_inverse_guard.json').write_text(json.dumps({'id':'A2-ED03-Programs-01-inverse','old':guards[-1]['new'],'new':anchor,'expected_count':1},indent=2)+'\n')
(W/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_preservation.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':source_sha,'owners':summary,'canonical_mutations':0},indent=2)+'\n')
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (W/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_defects.tsv').open('w',newline='') as f:
    out=csv.DictWriter(f,fieldnames=fields,delimiter='\t');out.writeheader()
    for g in guards:
        out.writerow({'change_id':g['id'],'type':';'.join(g['defect_ids']),'statement_id':g['owner'],
                      'old_location':f"source {source_sha}; lines {g.get('source_line_span','Programs anchor')}",
                      'old_page':'pending current candidate','new_location':g['owner'],'new_page':'pending final build',
                      'old_text':g['old'],'new_text':g['new'],'reason':g['reason']+' '+g.get('mathematical_disposition',''),
                      'review_status':'proposed only; full original read; final comparison pending seal'})
assert p.read_bytes()==raw
print(json.dumps({'source_sha256':source_sha,'owners':summary,'guards':len(guards),'program_rows':3,'canonical_mutations':0},indent=2))
