"""Integrate actual rendered-page findings, preserving mathematical targets."""
from pathlib import Path
import json,re,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor,ROOT,block

ed=Editor('V')
analytic=json.loads((ROOT/'agents/v_analytic/S6_SERIES_PUBLISH_V_final_reading_analytic_guards.json').read_text())
for g in analytic['edits']:
    ed.replace(g['old'],g['new'],g['defect_types'][0],g['proof_scope'],g['finding_id'],g['expected_occurrences'])

patches=[
('matrices give the Hodge table below.','matrices give the Hodge table.','D24','The Hodge table now precedes the outline; remove the incorrect direction.','step-V-E-3'),
('problem to the cited lattice-isomorphism algorithm in its verified\n  hypothesis.',
 'problem to the cited lattice-isomorphism algorithm over the resulting\n  product of matrix algebras over number fields.',
 'D08','State the algebraic scope proved in the body in place of a verification adjective.','step-V-F-2'),
('This enumeration\nrequires exactly the eight cubes with lower vertex in $\\{-1,0\\}^3$;\nno omitted cube can contain zero.',
 'A unit cube contains zero exactly when its lower vertex lies in\n$\\{-1,0\\}^3$, so these eight cubes give the complete enumeration.',
 'D02','The exact positive coordinate criterion proves completeness of the enumeration.','pub:V:branch-resolution'),
('Turned or deform-spun constructions insert\nadditional data and are not excluded by this argument.','',
 'D11','The numbered ordinary-spinning definition and theorem already state the precise scope; delete the repeated adjacent-scope disclaimer.','maps:src:E.2.10'),
('This return is the circle fibration of the shifted\nten-manifold; it is distinct from the six-sphere parameter\nreturns computed in \\SeriesRef{maps:src:B.6.24}.','',
 'D11','The domain and map of the return are explicitly defined in the theorem. Remove the unneeded comparison to another parameter return.','maps:src:E.2.13'),
('\\item The computation of \\eqref{maps:eq:E.S37} needs no further information on $H^*(E_{12})$. Its cyclic deck action is a translation on the',
 '\\item The cyclic deck action on $E_{12}$ is a translation on the',
 'D11','Introduce the exact deck action used to compute the variation map directly; subsequent invariant-subspace proof is unchanged.','maps:src:E.2.14'),
('Betti numbers in \\ref{maps:src:E.2.7} give the numbers of Jordan blocks',
 'Betti numbers in \\cref{maps:src:E.2.3} give the numbers of Jordan blocks',
 'D23','The earlier label points to the stable tangent-bundle proposition; the rational Betti vector is stated in the shifted-product theorem. The Wang calculation is unchanged.','maps:src:E.2.14'),
('\\operatorname{rank}(\\text{E.S53})&11&47&71&47&11',
 '\\operatorname{rank}\\eqref{maps:eq:E.S53}&11&47&71&47&11',
 'D19','Replace the surviving literal equation identifier in the rank table by its dynamic section-numbered reference.','maps:src:E.2.15'),
('\\date{20 November 2026}','\\date{21 November 2026}',
 'D15','The current revision and rendered reading continued into21November2026.','title'),
('this paper were undertaken by GPT-6 Astra on 20 November 2026.',
 'this paper were undertaken by GPT-6 Astra on 20--21 November 2026.',
 'D15','Record both actual UTC dates of the current publication session.','methodology'),
]
for old,new,kind,reason,loc in patches:ed.replace(old,new,kind,reason,loc)

old=r'''\item The quotient $R_1/(h_2-1)$ is nonzero, since the two central
generators are independent, and it is annihilated by the
non-zero-divisor $h_2-1$. A projective $R_1$-module is a
direct summand of a free module and has no such nonzero
annihilated element. Thus \eqref{maps:eq:E.S14} also gives an independent
proof of the nonprojectivity in \ref{maps:src:E.2.11}. '''
assert ed.text.count(old)==1
removed=ROOT/'records/S6_SERIES_PUBLISH_V_removed_independent_proofs.tex'
with removed.open('a') as f:
    f.write('\n% Removed duplicate nonprojectivity argument from maps:src:E.2.12 after the full rendered-page reading.\n'+old+'\n')
ed.replace(old,'','D12','The localized nonprojectivity argument is a second proof of the preceding theorem; preserve it in the checking records. Every assertion of the localization theorem is proved in its remaining nine items.','maps:src:E.2.12')

old=r'''\bibitem[Borcherds et al.(2016)]{pubLieGroups2016}
R.~Borcherds, M.~Haiman, N.~Reshetikhin, V.~Serganova, and T.~Johnson-Freyd.
\emph{Part I: Lie Groups}. Lecture notes, version of 5 October 2016.
\url{https://math.berkeley.edu/~serganov/261/part1.pdf}.'''
new=r'''\bibitem[Borcherds et al.(2016)]{pubLieGroups2016}
R.~Borcherds, M.~Haiman, N.~Reshetikhin, V.~Serganova, and T.~Johnson-Freyd.

\newblock \emph{Part I: Lie Groups}.

\newblock Lecture notes, version of 5 October 2016.

\newblock URL \url{https://math.berkeley.edu/~serganov/261/part1.pdf}.'''
ed.replace(old,new,'D18','Use the same author/title/publication/URL layout as the surrounding bibliography.','bibliography:pubLieGroups2016')
ed.replace('\\newblock URL \\url{https://doi.org/10.1017/fms.2022.74}.\n\n','',
           'D18','Remove the second printing of the identical DOI URL.','bibliography:rootBHJ22')
for arxiv in ('2609.38442','2609.29666'):
    ed.replace('\\url{https://arxiv.org/abs/'+arxiv+'}',
               '\\url{https://arxiv.org/abs/'+arxiv+'v1}',
               'D18','Link the exact preprint version whose statement/page locators are used.','bibliography:arxiv:'+arxiv)

old=r'''\bibitem[Jia and Meng(2022)]{ffJiaMeng}
Jia Jia and Sheng Meng.

\newblock Equivariant K{\"a}hler model for Fujiki's class, 2022.

\newblock URL \url{https://arxiv.org/pdf/2201.06748}.'''
new=r'''\bibitem[Jia and Meng(2024)]{ffJiaMeng}
Jia Jia and Sheng Meng.

\newblock Equivariant K{\"a}hler model for Fujiki's class.

\newblock \emph{The Journal of Geometric Analysis}, 34, article 349, 2024.

\newblock \doi{10.1007/s12220-024-01796-2}.

\newblock Statement and page numbers refer to
\href{https://arxiv.org/pdf/2201.06748v1}{arXiv:2201.06748v1}.'''
ed.replace(old,new,'D18','Official Springer metadata opened:34, article349(2024). Theorem1.1 and Remark1.2 locators remain those of the opened arXivv1, p2.','bibliography:ffJiaMeng')
old=r'''\bibitem[Winter(2008)]{mapsWinter08}
Blake Winter.

\newblock The classification of spun torus knots, 2008.

\newblock URL \url{https://arxiv.org/abs/0711.1638v3}.'''
new=r'''\bibitem[Winter(2009)]{mapsWinter08}
Blake Winter.

\newblock The classification of spun torus knots.

\newblock \emph{Journal of Knot Theory and Its Ramifications},
18(9):1287--1298, 2009.

\newblock \doi{10.1142/S0218216509007476}.

\newblock Statement and page numbers refer to
\href{https://arxiv.org/abs/0711.1638v3}{arXiv:0711.1638v3}.'''
assert (ROOT/'records/S6_SERIES_PUBLISH_V_Winter_journal_receipt.json').exists()
ed.replace(old,new,'D18','World Scientific-deposited Crossref metadata confirms journal18(9),1287–1298(2009),DOI. The opened v3 mathematical locators remain explicit; publisher abstract fetch returned403.','bibliography:mapsWinter08')

bib_path=ROOT/'S6_SERIES_PUBLISH_references.bib';bib=bib_path.read_text()
for p in json.loads((ROOT/'agents/provenance/S6_SERIES_PUBLISH_V_bibliography_supplement.json').read_text()):
    assert bib.count(p['old_text'])==1,p['key'];bib=bib.replace(p['old_text'],p['new_text'])
    ed.record('D18',p['old_text'],p['new_text'],p['reason'],'shared-bibliography:'+p['key'],old_location='shared bibliography entry',new_location='shared bibliography entry')
def entry(key):
    m=re.search(r'(?m)^@\w+\{'+re.escape(key)+r',',bib);assert m,key
    n=re.search(r'(?m)^@\w+\{',bib[m.end():]);return bib[m.start():m.end()+n.start() if n else len(bib)]
for key,year,fields,scope in [
    ('ffJiaMeng','2024',r'''  journal = {The Journal of Geometric Analysis},
  volume = {34},
  eid = {349},
  doi = {10.1007/s12220-024-01796-2},
  note = {Statement and page numbers refer to arXiv:2201.06748v1.},
  metadata_verification = {21 November 2026: official Springer publisher page opened; volume34, article349, publication23September2024. Primary mathematical locators remain Theorem1.1 and Remark1.2, v1 p2.},
''','Add opened journal metadata and preserve exact preprint pagination.'),
    ('mapsWinter08','2009',r'''  journal = {Journal of Knot Theory and Its Ramifications},
  volume = {18},
  number = {9},
  pages = {1287--1298},
  doi = {10.1142/S0218216509007476},
  note = {Statement and page numbers refer to arXiv:0711.1638v3.},
  metadata_verification = {21 November 2026: World Scientific-deposited metadata opened through Crossref works API; journal18(9),1287--1298,2009. Publisher abstract endpoint returned403; mathematical locators remain the separately opened v3.},
''','Add publisher-deposited journal metadata with the primary metadata receipt; preserve v3 locators.')]:
    old=entry(key);new=re.sub(r'^@misc',r'@article',old)
    new=re.sub(r'(\byear\s*=\s*\{)\d{4}(\})',lambda m:m[1]+year+m[2],new,count=1)
    if key=='ffJiaMeng':new=new.replace('https://arxiv.org/pdf/2201.06748}','https://arxiv.org/pdf/2201.06748v1}')
    last=new.rfind('}');prefix=new[:last].rstrip();prefix+=',' if not prefix.endswith(',') else ''
    new=prefix+'\n'+fields+new[last:]
    bib=bib.replace(old,new);ed.record('D18',old,new,scope,'shared-bibliography:'+key,old_location='shared bibliography entry',new_location='shared bibliography entry')

ed.save();bib_path.write_text(bib)
(ROOT/'records/S6_SERIES_PUBLISH_V_page_fixes_01_receipt.json').write_text(json.dumps({'source_sha256':hashlib.sha256(ed.path.read_bytes()).hexdigest(),'bib_sha256':hashlib.sha256(bib_path.read_bytes()).hexdigest(),'changes':len(ed.rows),'source_candidate':'V_candidate_01','final_rerender_required':True},indent=2)+'\n')
