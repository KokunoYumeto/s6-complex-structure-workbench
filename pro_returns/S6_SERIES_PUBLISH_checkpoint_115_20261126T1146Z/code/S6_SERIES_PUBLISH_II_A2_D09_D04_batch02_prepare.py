#!/usr/bin/env python3
"""Prepare exact bounded proof edits; never write canonical source or ledgers."""
from collections import Counter
from datetime import datetime, timezone
import csv
import difflib
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_working'
OUT.mkdir(exist_ok=True)
paper=ROOT/'S6_SERIES_PUBLISH_II.tex'
data=paper.read_bytes()
source=data.decode()
source_sha=hashlib.sha256(data).hexdigest()
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
owners=[('cdp:st:C2b','01FH'),('night:P4.38','02XB'),('night:P4.39','02XC')]
blocks={}
for owner,tag in owners:
    anchor=source.index('\\label{'+owner+'}')
    start=source.rfind('\\begin{proposition}',0,anchor)
    proof_end=source.index('\\end{proof}',anchor)+len('\\end{proof}')
    end=proof_end
    if tag in ['02XB','02XC']:
        end=source.index('\\subsection',proof_end)
    blocks[tag]={'owner':owner,'start':start,'end':end,'before':source[start:end],
                 'after':source[start:end], 'guards':[]}
guards=[]


def edit(tag,old,new,types,reason,math='Every mathematical assertion, map and formula in this span is retained.'):
    b=blocks[tag]
    assert b['before'].count(old)==1,(tag,old,b['before'].count(old))
    assert b['after'].count(old)==1,(tag,old,b['after'].count(old))
    pos=b['start']+b['before'].index(old)
    guard={'id':f'A2-ED02-{tag}-{len(b["guards"])+1:02}', 'owner':b['owner'],'tag':tag,
           'old':old,'new':new,'expected_count':1,'defect_ids':types,'reason':reason,
           'mathematical_disposition':math,'source_snapshot_sha256':source_sha,
           'source_character_span':[pos,pos+len(old)],
           'source_byte_span':[len(source[:pos].encode()),len(source[:pos+len(old)].encode())],
           'source_line_span':[source.count('\n',0,pos)+1,source.count('\n',0,pos+len(old))+1]}
    b['guards'].append(guard);guards.append(guard)
    b['after']=b['after'].replace(old,new,1)


for owner,tag in owners:
    header=re.search(r'\\StatementRecord\{[^\n]+',blocks[tag]['before']).group()
    edit(tag,header,f'\\StatementRecord{{{owner}}}{{proved}}{{{tag}}}{{}}',
         ['D10'],'Remove dependency bookkeeping from the statement header; retain the permanent printed tag and every dependency in the proof.')
    edit(tag,r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
         r'\begin{enumerate}[label=\arabic*.,leftmargin=*]', ['D10'],
         'Remove the production-marker prefix from the unchanged numbered proof items.')

edit('01FH',
     r'Their Euler numbers are respectively $-2$ and zero, independently checking the fibre computation. The exact arithmetic is in \texttt{code/C\_euler.py}.',
     r'Their Euler numbers are respectively $-2$ and zero, agreeing with the fibre computation.',
     ['D09','D08'],'Move the program filename to the Programs table and retain the equality of the two Euler calculations.',
     'Both Euler values, all three Betti vectors, the blowup cohomology summands, torsion freeness, and the geometric maps remain in the proof. The historical program also has a triangulated-torus loop which is not attributed to this proposition.')

edit('02XB','An actual irreducible support in Part~4.2 cannot have a singular',
     r'An irreducible fibre support in \cref{def:II:standing-torus-fibration} cannot have a singular',
     ['D05','D08'],'Resolve the standing setting to its exact numbered definition and remove process emphasis.',
     'P204 is the verbatim standing torus-fibration setting previously denoted Part 4.2. No positivity, normality, or genus assumption is added.')
edit('02XB',r'\item We retain the boundary transport of P4.20 throughout.',
     r'\item Throughout, we use the boundary transport of \cref{night:P4.20}.',
     ['D04','D08'],'Resolve the boundary-transport reference and state the operation directly.')
edit('02XB',r'P4.16 gives its compact spherical class of square $-4$.',
     r'\Cref{night:P4.16} gives its compact spherical class of square $-4$.',
     ['D04'],'Replace a raw run label by the existing statement reference.')
xb_tail='''\\end{proof}

The exact quadratic matrix, determinant, and the two nonzero
derivatives in this proof are verified by
\\texttt{code/part4/critical\\_curve\\_node.py}; its saved output
reports PASS.
'''
edit('02XB',xb_tail,'\\end{proof}\n', ['D09','D08'],
     'Move the outside-proof program/output paragraph to the Programs table and reading record.',
     'The quadratic coefficients, determinant, both derivatives, and implicit-root coefficient are already explicit in item 3 and are unchanged. No mathematical assertion is dropped.')

edit('02XC',
     'positive-genus ruled resolution in Part~4.2 cannot lie over\na point where all local critical-curve branches have generic\ntype $D_4$. This assertion does not replace that local\nhypothesis by a mixture of transverse types.',
     'positive-genus ruled resolution of an irreducible fibre support\nin \\cref{def:II:standing-torus-fibration} cannot lie over\na point where all local critical-curve branches have generic\ntype $D_4$.',
     ['D05','D02'],'Resolve the exact standing setting and express the all-branches D4 hypothesis once, positively.',
     'The first local theorem remains unrestricted by the global setting. The particular application retains the explicit hypothesis that every local critical-curve branch has generic type D4; no mixed-type conclusion is asserted.')
edit('02XC','a proposed\npositive-genus exceptional curve $H$',
     'a\npositive-genus exceptional curve $H$', ['D08'],
     'Remove workflow vocabulary from the unchanged curve considered in the contradiction.')
edit('02XC','Actual adjunction gives','Adjunction gives',['D08'],
     'Remove process emphasis from the exact unchanged adjunction formula.')
edit('02XC','argument of P4R.6 applies locally:',
     r'argument of \cref{night:P4R.6} applies locally:', ['D04'],
     'Resolve the negative-intersection-matrix dependency to the existing statement.')
edit('02XC',r'Thus $d\ge5$ is impossible. For $d=4$ we have',
     r'Thus (4.39b) makes $d\ge5$ impossible. For $d=4$ we have',
     ['D09'],'Move the existing literal reference (4.39b) from the program summary to its mathematical inference; retain its raw numbering for D19.',
     'The complete integer-solution argument remains in items 4 and 5. The three solutions are (d,n,a)=(3,1,1),(3,2,0),(4,1,0); the unchanged equation with n>=1 and a>=0 excludes all d>=5.')
edit('02XC','The degree bounds follow from the degree-at-least-three',
     'The degree bounds in (4.39d) follow from the degree-at-least-three',
     ['D09'],'Move the existing literal reference (4.39d) from the program summary to the proof of those bounds; retain its raw numbering for D19.')
old='''Its discriminant has degree at most
two. The resulting quadratic extension of $\\mathbb C(w)$'''
new='''Its discriminant has degree at most
two. Write $B(w)=b_0+b_1w$ and
$C(w)=c_0+c_1w+c_2w^2$. For homogeneous coordinates
$[X:Z]$ on the exceptional line, put
\\[
 B_h=X^2(b_0X+b_1Z),\\qquad
 C_h=X^3(c_0X^2+c_1XZ+c_2Z^2),\\qquad
 Q_h=XU^2+B_hU+C_h.
\\]
Here $Q_h$ has weight five when $X,Z$ have weight one and
$U$ has weight two. On $X\\ne0$ the substitutions $w=Z/X$
and $U=X^2q$ give
\\[
 Q_h(X,Xw,X^2q)=X^5\\bigl(q^2+B(w)q+C(w)\\bigr).
\\]
The homogeneous discriminant is therefore
\\[
 B_h^2-4XC_h
 =X^4\\bigl((b_0X+b_1Z)^2
             -4(c_0X^2+c_1XZ+c_2Z^2)\\bigr).
\\]
It contains the factor $X^4$; the residual homogeneous factor
has degree two. The resulting quadratic extension of $\\mathbb C(w)$'''
edit('02XC',old,new,['D09'],
     'Retain the mathematical fourth-order-factor assertion from the removed program paragraph as an explicit homogeneous formula and exact chart map in item 7.',
     'This expands the existing homogeneous-discriminant assertion, using exactly the historical program inputs. The identity Q_h(X,Xw,X^2q)=X^5(q^2+Bq+C) specifies the coordinate relation. It changes no normalization, branch-count or rationality conclusion.')
xc_tail='''\\end{proof}

The positive-integer solutions of (4.39b), the monomial degree
bounds in (4.39d), and the forced fourth-order factor of the
homogeneous quadratic discriminant are checked in
\\texttt{code/part4/d4\\_pole.py}. Its saved output reports PASS.
'''
edit('02XC',xc_tail,'\\end{proof}\n',['D09','D08'],
     'Move the outside-proof program/output description to Programs and the check record.',
     'Integer solutions and monomial bounds remain proved in items 4, 5 and 7; the discriminant factor is printed with its exact chart relation in item 7. Both raw equation references from this paragraph are retained unchanged in those mathematical sentences.')

preservation=[]
for owner,tag in owners:
    b=blocks[tag];old=b['before'];new=b['after']
    assert source.count(old)==1
    old_displays=re.findall(r'\\\[.*?\\\]',old,re.S)
    new_displays=re.findall(r'\\\[.*?\\\]',new,re.S)
    assert all(new.count(display)==old.count(display) for display in old_displays)
    assert old.count('\\item ')==new.count('\\item ')
    for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{tag-[^}]+\}',r'\\tag\{[^}]+\}',
                    r'\\eqref\{[^}]+\}',r'\((?:P[1-4]R?\.)?\d+\.\d+[a-z]?(?:\.\d+)?\)']:
        assert Counter(re.findall(pattern,old))==Counter(re.findall(pattern,new)),(tag,pattern)
    def inline_math(text):
        text=re.sub(r'\\begin\{enumerate\}\[[^\n]*\]','',text)
        return Counter(re.findall(r'(?<!\\)\$(?!\$).*?(?<!\\)\$',text,re.S))
    missing=inline_math(old)-inline_math(new)
    assert not missing,(tag,missing)
    inverse=[];replayed=new
    for g in reversed(b['guards']):
        assert g['new'] and replayed.count(g['new'])==1,(g['id'],replayed.count(g['new']))
        inverse.append({'id':g['id']+'-inverse','owner':owner,'tag':tag,
                        'old':g['new'],'new':g['old'],'expected_count':1})
        replayed=replayed.replace(g['new'],g['old'],1)
    assert replayed==old
    prefix=f'S6_SERIES_PUBLISH_II_A2_{tag}'
    for suffix,text in [('_before.tex',old),('_after.tex',new),
                        ('_exact.diff',''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=prefix+'_before.tex',tofile=prefix+'_after.tex')))]:
        (OUT/(prefix+suffix)).write_text(text)
    (OUT/(prefix+'_inverse_guards.json')).write_text(json.dumps(inverse,indent=2)+'\n')
    preservation.append({'owner':owner,'tag':tag,'before_sha256':sha(old),'after_sha256':sha(new),
                         'proof_items_preserved':old.count('\\item '),'old_displays_preserved':len(old_displays),
                         'new_displays':len(new_displays),'all_original_inline_math_preserved':True,
                         'labels':re.findall(r'\\label\{([^}]+)\}',old),
                         'equation_tags_preserved':re.findall(r'\\tag\{([^}]+)\}',old),
                         'raw_equation_references_preserved':re.findall(r'\((?:P[1-4]R?\.)?\d+\.\d+[a-z]?(?:\.\d+)?\)',old),
                         'outside_program_paragraph_included':tag in ['02XB','02XC'],
                         'guards':len(b['guards'])})

rows=r'''Betti numbers and Euler numbers of two fibre blowups (\cref{cdp:st:C2b}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/C_euler.py}{\nolinkurl{C_euler.py}} \\[3pt]
Cusp-and-line quadratic matrix and determinant derivatives (\cref{night:P4.38}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/critical_curve_node.py}{\nolinkurl{critical_curve_node.py}} \\[3pt]
Pole-order solutions, normal-degree bounds and homogeneous discriminant (\cref{night:P4.39}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/d4_pole.py}{\nolinkurl{d4_pole.py}} \\[3pt]
'''
anchor='\\end{longtable}}\n\n\\begin{thebibliography}{99}'
assert source.count(anchor)==1
assert all(n not in source[source.index('\\section*{Programs}'):] for n in ['C_euler.py','critical_curve_node.py','d4_pole.py'])
(OUT/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_Programs_rows.tex').write_text(rows)
program_guard={'id':'A2-ED02-Programs-01','owner':'app:II:programs','tag':'',
               'old':anchor,'new':rows+anchor,'expected_count':1,'defect_ids':['D09'],
               'reason':'Add one verified pinned source mapping for each relocated program description.',
               'source_snapshot_sha256':source_sha}
guards.append(program_guard)
(OUT/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_guards.json').write_text(json.dumps(guards,indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_Programs_inverse_guard.json').write_text(json.dumps(
    {'id':program_guard['id']+'-inverse','old':program_guard['new'],'new':program_guard['old'],'expected_count':1},indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_preservation.json').write_text(json.dumps(
    {'source_sha256':source_sha,'owners':preservation,'owner_guard_count':len(guards)-1,'program_guard_count':1,
     'canonical_mutations':0,'created_utc':datetime.now(timezone.utc).isoformat()},indent=2)+'\n')
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_defects.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader()
    for g in guards:
        writer.writerow({'change_id':g['id'],'type':';'.join(g['defect_ids']),'statement_id':g['owner'],
                         'old_location':f"source {source_sha}; lines {g.get('source_line_span','Programs insertion anchor')}",
                         'old_page':'pending current candidate build','new_location':g['owner'],
                         'new_page':'pending final build','old_text':g['old'],'new_text':g['new'],
                         'reason':g['reason']+' '+g.get('mathematical_disposition',''),
                         'review_status':'proposed only; complete original read; final full comparison pending seal'})

# A refreshed lexical census includes outside-proof paragraphs. It does not certify defects.
body_start=source.index('\\begin{document}')
body_end=source.index('\\section*{Programs}')
proofs=list(re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',source,re.S))
headers=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|definition|remark|example)\}[^\n]*',source))
hard=re.compile(r'\.py\b|\.json(?:l)?\b|\.out\b|code/|SHA[- ]?256|\bsaved output\b|\bexecuted independent\b|\b(?:the|attached) program\b',re.I)
raw=re.compile(r'(?<![A-Za-z0-9:{])P[1-4](?:[A-Z]|R)?\.\d+(?:\.\d+)?\b|\bsupplied correction note\b|\b(?:night run|worker|S6_[0-9A-Z_]+)\b')
census=[]
for kind,pattern in [('D09_candidate',hard),('D04_candidate',raw)]:
    for match in pattern.finditer(source,body_start,body_end):
        header=next((h for h in reversed(headers) if h.start()<match.start()),None)
        proof=next((p for p in proofs if p.start()<=match.start()<p.end()),None)
        label=re.search(r'\\label\{([^}]+)\}',header.group()) if header else None
        line_start=source.rfind('\n',0,match.start())+1
        line_end=source.find('\n',match.end())
        census.append({'kind':kind,'owner':label.group(1) if label else None,
                       'inside_proof':bool(proof),'source_line':source.count('\n',0,match.start())+1,
                       'match':match.group(),'line':source[line_start:line_end]})
census_out={'source_sha256':source_sha,'scope':'Lexical candidates in the document body before Programs, including outside-proof paragraphs. Each hit requires contextual review; these are not certified defects.',
            'D09_inside_proof_hits':sum(r['kind']=='D09_candidate' and r['inside_proof'] for r in census),
            'D09_outside_proof_hits':sum(r['kind']=='D09_candidate' and not r['inside_proof'] for r in census),
            'D09_inside_proof_owners':len({r['owner'] for r in census if r['kind']=='D09_candidate' and r['inside_proof']}),
            'D09_outside_proof_owners':len({r['owner'] for r in census if r['kind']=='D09_candidate' and not r['inside_proof']}),
            'D04_candidate_hits':sum(r['kind']=='D04_candidate' for r in census),'rows':census,'canonical_mutations':0}
(OUT/'S6_SERIES_PUBLISH_II_A2_D09_D04_census_02.json').write_text(json.dumps(census_out,indent=2)+'\n')
assert paper.read_bytes()==data,'Canonical source changed during preparation; rebase exact owner guards.'
print(json.dumps({'source_sha256':source_sha,'owners':preservation,'guard_count':len(guards),
                  'census_summary':{k:v for k,v in census_out.items() if k!='rows'}},indent=2))
