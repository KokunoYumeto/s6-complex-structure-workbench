from pathlib import Path
import re,json,hashlib,datetime

ROOT=Path('/workspace/scratch/653608133b22')
OUT=ROOT/'work/agents/i_provenance'
P=ROOT/'work/S6_SERIES_PUBLISH_I.tex'
original=P.read_text(); s=original; changes=[]
def add(old,new,reason):
    global s
    assert old!=new
    count=s.count(old); assert count,repr(old)
    # Context makes every receiving guard unique, including repeated hidden citations.
    for _ in range(count):
        at=s.find(old); a=at; b=at+len(old)
        if s.count(old)>1:
            a=s.rfind('\n',0,at)+1; b=s.find('\n',at+len(old))
            if b<0:b=len(s)
            while s.count(s[a:b])>1:
                a=max(0,a-80);b=min(len(s),b+80)
        guard=s[a:b]; replacement=guard[:at-a]+new+guard[at-a+len(old):]
        assert s.count(guard)==1
        changes.append(dict(id=f'IP-C11-L{len(changes)+1:02}',old=guard,new=replacement,reason=reason))
        s=s.replace(guard,replacement,1)

locs=[
(r'\citet[Theorem 3.1.2]{bost2009}',r'\citet[Theorem~3.1.2, p.~386]{bost2009}'),
(r'\cite[Theorem~3.1.2]{bost2009}',r'\cite[Theorem~3.1.2, p.~386]{bost2009}'),
(r'\citet[Theorem 1.4 and Corollary 1.6]{nguyen2023}',r'\citet[Theorem~1.4 and Corollary~1.6, arXiv v1, p.~3]{nguyen2023}'),
(r'\citet[Theorems 1.3 and 2.3]{xie2024algebraicity}',r'\citet[Theorem~1.3, p.~3, and Theorem~2.3, p.~12, arXiv v1]{xie2024algebraicity}'),
('in Definition 1.2 of\n\\citet{noguchi2024}. Their Theorem 1.3 gives',r'in the subgroup condition (1.2) of \citet[author preprint, p.~2]{noguchi2024}. Their Theorem~1.3 on the same page gives'),
(r'\citet[Theorems 3.6 and 3.7]{waldschmidt2009auxiliary}',r'\citet[Theorems~3.6--3.7, author proof, pp.~21--22]{waldschmidt2009auxiliary}'),
(r'\citep[Theorem6.1]{herblot2012meromorphic}',r'\citep[Theorem~6.1, pp.~31--32]{herblot2012meromorphic}'),
(r'\citep[Theorem4.16]{gasbarri2010analytic}',r'\citep[Theorem~4.16, author preprint, p.~25]{gasbarri2010analytic}'),
(r'\citep[Theorem1.1 and system(1.2)]{adamczewski2017mahler}',r'\citep[Theorem~1.1 and system~(1.2), p.~56]{adamczewski2017mahler}'),
(r'\citep[Theorem5.1]{einsiedler2001entropy}',r'\citep[Theorem~5.1, author preprint, p.~9]{einsiedler2001entropy}'),
(r'\citep[Theorem4.1 and Corollary4.3]{waldschmidt1988periodrank}',r'\citep[Theorem~4.1, pp.~385--386, and Corollary~4.3, p.~386]{waldschmidt1988periodrank}'),
(r'\citet[slides 5--8]{bertrand2017}',r'\citet[PDF slides~5--8]{bertrand2017}'),
(r'\cite[final slide, comment~(c)]{bertrand2017}',r'\cite[PDF slide~15, comment~(c)]{bertrand2017}'),
(r'Theorem~2.1 of \cite{bertrand1995}',r'\citet[Theorem~2.1, p.~147]{bertrand1995}'),
(r'\cite[Theorem~3.1]{bertrand1995}',r'\cite[Theorem~3.1, p.~150]{bertrand1995}'),
(r'Theorem 1.1 of \citet{demarco2017}',r'Theorem~1.1 of \citet[arXiv v2, p.~2]{demarco2017}'),
(r'\citet[Theorem 1.1 and Corollary 1.2]{demarco2017}',r'\citet[Theorem~1.1 and Corollary~1.2, arXiv v2, p.~2]{demarco2017}'),
('Silverman reproduced as Theorems 2.2 and 2.3 in that paper:',r'Silverman reproduced in \citet[Theorems~2.2--2.3, arXiv v2, pp.~7--8]{demarco2017}:'),
('\\citet[Construction~3.4, p.~12, Lemma~3.5, p.~13, and\nProposition~4.12, pp.~19--20]{bertolin2022} compute the motivic', '\\citet[Construction~3.4, p.~12, and Lemma~3.5, p.~13, arXiv v2]{bertolin2022} compute the motivic'),
(r'\cite[Conjecture~4.7, p.~18]{bertolin2022}',r'\cite[Conjecture~4.7, arXiv v2, p.~18]{bertolin2022}'),
(r'\cite[Proposition~4.12, pp.~19--20]{bertolin2022}',r'\cite[Proposition~4.12, arXiv v2, pp.~19--20]{bertolin2022}'),
('The bracket is described in their Section~6.1, pp.~26--27, and\ntheir corrected Table~2, pp.~28--29, gives unipotent dimension', 'The bracket is described in their Section~6.1, pp.~26--27, and\ntheir corrected Table~2, p.~29, with the correction on p.~28, gives unipotent dimension'),
]
for a,b in locs:add(a,b,'Exact primary locator and edition verified on actual rendered source pages; no mathematical event. Proposition4.12 remains cited for its conjecture relation in the open-question paragraph, not as the unconditional motivic-dimension input.')

# Same-work publication/preprint correspondence has been checked at the used loci.
bmmap=[
(r'\cite[Theorem 1.6 and the following analytic-neighborhood paragraph, preprint p.~5]{BM97}',r'\cite[Theorem~1.6 and the following noncompact extension, p.~215]{BM97}'),
(r'\cite[Theorem 1.10, preprint p.~7, with the analytic category in (0.2), p.~3]{BM97}',r'\cite[Theorem~1.10, p.~216, with the analytic category in (0.1)(2), p.~208]{BM97}'),
]
for a,b in bmmap:add(a,b,'Actual preprint/publication comparison; cite the opened published counterpart.')
rx=re.compile(r'\\cite(?:t|p)?(?:\[[^\]]*\])?\{BM95AB\}')
for match in list(rx.finditer(s)):
    old=match.group(); cmd=old[:old.find('[')] if '[' in old else old[:old.find('{')]
    if '0.2' in old:loc=r'Analytic category (0.1)(2), p.~208; Theorem~1.6 and its noncompact extension, p.~215; Remark~1.16, p.~221'
    elif 'Remark' in old:loc=r'Theorem~1.6, p.~215; Remark~1.16, p.~221'
    elif '1.10' in old:loc=r'Theorems~1.6 and 1.10, pp.~215--216, including the noncompact extension after Theorem~1.6'
    else:loc=r'Theorem~1.6 and the following noncompact extension, p.~215'
    if old in s:add(old,cmd+'['+loc+']{BM97}','Duplicate-work citation mapped to the authenticated published result; old preprint locator archived.')

def bibspan(key):
    m=re.search(r'\\bibitem[^\n]*\{'+re.escape(key)+r'\}',s);assert m
    n=s.find('\\bibitem',m.end());return s[m.start():n if n>=0 else s.find('\\end{thebibliography}',m.end())]
old95=bibspan('BM95AB'); (OUT/'S6_SERIES_PUBLISH_I_BM95AB_archived_inline.tex').write_text(old95)
add(old95,'','Duplicate preprint entry consolidated into the published entry; exact edition comparison receipt retained.')
old97=bibspan('BM97');new97=old97.replace(r'\newblock URL \url{https://arxiv.org/pdf/alg-geom/9508005}.',r'\newblock Earlier Chapter~I preprint: arXiv:alg-geom/9508005v2 (1995), with separate pagination. \newblock \url{https://arxiv.org/abs/alg-geom/9508005v2}.')
add(old97,new97,'Keep one published work entry and explicitly identify the separately paginated earlier Chapter I preprint.')

receipt=OUT/'literature/S6_SERIES_PUBLISH_I_final_primary_locator_receipt.json'
payload=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source=str(P),source_sha256=hashlib.sha256(original.encode()).hexdigest(),source_writes=False,receipt=str(receipt),mathematical_check_events=0,changes=changes)
(OUT/'S6_SERIES_PUBLISH_I_candidate11_locator_guards.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')

# Shared bibliography retains the historical alias because other papers may still cite it.
B=ROOT/'work/S6_SERIES_PUBLISH_references.bib';b=B.read_text();bc=[]
for key,note in [('BM95AB','Historical preprint alias; Paper I uses canonical key BM97 after actual comparison of arXiv v2 pp.3,5,7,11 with publication pp.208,215,216,221. Analytic category (0.2)(2) becomes (0.1)(2). No whole-work identity or whole-book reading is asserted.'),('BM97','Actual published pages 207-209,215-217,221-222 viewed on 21 November 2026; analytic category (0.1)(2)p208, Theorem1.6/noncompact extension p215, Theorem1.10p216, Remark1.16 and canonical local-isomorphism passage p221. Earlier arXiv v2 has separate pagination pp.3,5,7,11. Published PDF retrieved from an academic mirror, publisher metadata independently opened; zero mathematical events.')]:
    m=re.search(r'@\w+\{'+key+r',',b);n=re.search(r'\n@',b[m.end():]);end=m.end()+n.start() if n else len(b);old=b[m.start():end];close=old.rfind('}');head=old[:close].rstrip();head=head if head.endswith(',') else head+',';new=head+'\n  current_run_locator = {'+note+'}\n'+old[close:];bc.append(dict(id='IP-C11-BIB-'+key,old=old,new=new,reason='Preserve historical fields and append actual current-run edition/locator scope.'))
(OUT/'S6_SERIES_PUBLISH_I_candidate11_shared_bib_guards.json').write_text(json.dumps(dict(source=str(B),source_sha256=hashlib.sha256(b.encode()).hexdigest(),changes=bc,source_writes=False),indent=2)+'\n')
print(len(changes),'source locator guards;',len(bc),'shared bibliography guards; source SHA',payload['source_sha256'])
