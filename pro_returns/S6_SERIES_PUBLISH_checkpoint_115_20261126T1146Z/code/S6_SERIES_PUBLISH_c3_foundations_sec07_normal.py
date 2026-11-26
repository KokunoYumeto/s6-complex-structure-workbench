from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations/sec07'
source = (OUT / 'S6_SERIES_PUBLISH_II_sec07_input.tex').read_text()
begin = source.index(r'\begin{proposition}[Every normal irreducible support')
end = source.index(r'\end{proof}', begin) + len(r'\end{proof}')
original = source[begin:end]
text = original
rows = []

def replace(old, new, kinds, reason):
    global text
    assert old in text, old[:120]
    occurrences = text.count(old)
    for i in range(occurrences):
        for kind in kinds.split(','):
            rows.append(dict(change_id=f'II-C3-S07-N-{len(rows)+1:03}', type=kind,
                statement_id='cdp:st:C.2.UN.5', old_location='sec:II:07 / normal irreducible support',
                old_page='cp35; page concordance pending', new_location='subsec:II:normal-irreducible-supports',
                new_page='integrated build pending', old_text=old, new_text=new,
                reason=reason+f' [Occurrence {i+1} of {occurrences}.]', review_status='complete original read; receiving comparison pending'))
    text = text.replace(old, new)

step3start = text.index(r'\item We verify that $A$ is a torus')
step3end = text.index(r'\item Write a generator', step3start)
old = text[step3start:step3end]
new = r'''\item Apply \cite[Theorem~4.6 and its proof, pp.~13--14]{Catanese2002}
to the proper submersion $h:U'\to\Delta_s$. Its central fibre is
the compact complex manifold $A$, and every fibre with $s\ne0$ is
a two-torus. A local classifying map to the Kuranishi base of $A$
therefore sends a sequence $s_\nu\to0$ to torus points converging to
the central parameter, exactly the hypothesis of that theorem.
It follows that $A$ is a two-torus. The period-integral map in
the source's proof is the Albanese map of this family; on $A$,
after choosing an origin $a_0$, it is the isomorphism
$a\mapsto[\omega\mapsto\int_{a_0}^a\omega]$.

'''
replace(old,new,'D17,D18','The existing Albanese re-proof is replaced only after opening arXiv:math/0111245v2, Theorem 4.6 and its full proof on pp.13–14. The proper family, central fibre, classifying map and limit of torus parameters are identified explicitly; the same period-integral Albanese map is retained.')
replace(r'\SeriesRef{cdp:st:A.5.17} supplies',r'\cref{cdp:st:A.5.17} supplies','D04','Use the current in-paper statement number.')
replace('This argument uses no Betti-number or\nK\\"ahler hypothesis on the ambient threefold.','', 'D02,D11','The statement already gives the smooth local ambient domain without these restrictions.')
replace(r'\cite[Definition~3.1 and Theorems~3.2--3.3]{Catanese2002}',r'\cite[Definition~3.1 and Theorems~3.2--3.3, p.~9]{Catanese2002}','D18','The exact cited version and p.9 were opened and read; its product quotient definition and seven group cases match the displayed deck-character construction.')
replace('the\nactual map as','the\nmap as','D08','Remove the production modifier; keep the local equation and its unit.')
replace('the actual nearby\ntorus fibre','the nearby\ntorus fibre','D08','Keep the inclusion of the Milnor fibre into the nearby torus.')
replace('the\nnormalization of the actual fibre product','the\nnormalization of the fibre product','D08','The finite normalization map and its chart equations remain explicit.')
replace('Thus these are actual compact realizations\nof the displayed support and multiplicity.','Thus the quotient realizes the displayed support and multiplicity.','D08','The action, quotient and full fibres prove the realization directly.')

# Remove the obsolete hidden Buchdahl dependency after replacing the only use.
record_start = text.index(r'\StatementRecord')
record_end = text.index('\n',record_start)
old_record = text[record_start:record_end]
new_record = r'\StatementRecord{cdp:st:C.2.UN.5}{proved}{01DU}{\cref{cdp:st:A.5.17}; \cite[Theorem~4.6, pp.~13--14; Definition~3.1 and Theorems~3.2--3.3, p.~9]{Catanese2002}}'
replace(old_record,new_record,'D18','The hidden dependency record now follows the exact cited application and preserves the existing statement tag.')

equations=[]
def equation(match):
    body=match.group(1)
    tag=re.search(r'\\tag\{([^{}]+)\}',body)
    if not tag:
        return match.group(0)
    label=re.search(r'\\label\{([^{}]+)\}',body).group(1)
    equations.append({'old_tag':tag.group(1),'label':label,'owner':'cdp:st:C.2.UN.5'})
    updated=re.sub(r'\\tag\{[^{}]+\}','',body)
    old=match.group(0)
    new='\\begin{equation}'+updated+'\\end{equation}'
    rows.append(dict(change_id=f'II-C3-S07-N-{len(rows)+1:03}',type='D19',statement_id='cdp:st:C.2.UN.5',old_location='sec:II:07 / '+tag.group(1),old_page='cp35; page concordance pending',new_location=label,new_page='integrated build pending',old_text=old,new_text=new,reason='Convert the tagged bracket display to equation, retaining its existing label and permanent target; root has enabled section equation numbering.',review_status='complete original read; receiving comparison pending'))
    return new
text=re.sub(r'\\\[([\s\S]*?)\\\]',equation,text)
text=re.sub(r'\n{3,}','\n\n',text).strip()+'\n'
heading=r'\subsection{Normal irreducible supports}\label{subsec:II:normal-irreducible-supports}'+'\n\n'
text=heading+text
rows.append(dict(change_id=f'II-C3-S07-N-{len(rows)+1:03}',type='D14',statement_id='sec:II:07',old_location='sec:II:07 opening block',old_page='cp35; page concordance pending',new_location='subsec:II:normal-irreducible-supports',new_page='integrated build pending',old_text='An unpartitioned 6896-line section starts with the normal-support classification and quotient realization.',new_text=heading,reason='A substantive normal-support subsection keeps its classification, root-cover construction and multiplicity realization together before nonnormal supports.',review_status='complete original read; receiving comparison pending'))

for name, pattern in [('labels',r'\\label\{([^{}]+)\}'),('targets',r'\\hypertarget\{([^{}]+)\}')]:
    old_ids=re.findall(pattern,original)
    for identity in old_ids:
        assert re.findall(pattern,text).count(identity)==1,(name,identity)
assert '\r' not in text
fragment=OUT/'S6_SERIES_PUBLISH_II_sec07_normal.tex'
fragment.write_text(text,newline='\n')
guards=[dict(key='sec07_normal_support',old=original,new=text.rstrip(),reason='Normal-support subsection and exact Catanese deformation application; all hypotheses, conclusions, quotient maps and identifiers retained.')]
(OUT/'S6_SERIES_PUBLISH_sec07_normal_guards.json').write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n',newline='\n')
with (OUT/'S6_SERIES_PUBLISH_sec07_normal_defects.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
with (OUT/'S6_SERIES_PUBLISH_sec07_normal_equation_map.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['old_tag','label','owner'],delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(equations)
print(f'Wrote {len(text.splitlines())} lines, {len(rows)} defect rows and {len(equations)} equation conversions. Receiving proof comparison is pending.')
