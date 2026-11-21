"""Apply the opened-source bibliography corrections and restore estimate citations."""
from pathlib import Path
import csv, json, re, hashlib
from S6_SERIES_PUBLISH_editing import Editor, ROOT

patch_path=ROOT/'agents/provenance/S6_SERIES_PUBLISH_V_bibliography_replacements.json'
patches=json.loads(patch_path.read_text())
bib_path=ROOT/'S6_SERIES_PUBLISH_references.bib'
bib=bib_path.read_text()
for patch in patches:
    assert bib.count(patch['old_text'])==1, patch['key']
    bib=bib.replace(patch['old_text'],patch['new_text'])

ed=Editor('V')
ed.replace("Gronwall's estimate and Cauchy's coefficient formula therefore\nbound the tail after degree $N$, on $|z-z_0|\\le r<R$, by",
           "Gronwall's estimate \\cite[Lemma~2.7, pp.~42--43]{TeschlODE2012}\nand Cauchy's coefficient formula\n\\cite[\\S1.9(iii), (1.9.30)--(1.9.31)]{DLMFCauchy2026}\ntherefore bound the tail after degree $N$, on $|z-z_0|\\le r<R$, by",
           'D18','Restore the primary-source locators in the consolidated common Taylor estimate; both statements and pages were opened and checked.','night:P1.18')
ed.replace('161 computations or formal certificates. It contains another eight',
           '166 computations or formal certificates. It contains another eight',
           'D20','Recompute the current-statement association total from the final merged events.','methodology')
ed.replace('examined. The 252 readings associated with the current statements are',
           'examined. The 301 readings associated with the current statements are',
           'D20','Recompute the current-statement rereading association total from the final merged events.','methodology')
old=r'''\newblock arXiv:2303.15855v5, 2025.

\newblock URL \url{https://arxiv.org/pdf/2303.15855v5}.'''
new=r'''\newblock \emph{Mathematische Zeitschrift}, 311, article 33, 2025.

\newblock \doi{10.1007/s00209-025-03833-4}.

\newblock Statement and page numbers refer to
\href{https://arxiv.org/pdf/2303.15855v5}{arXiv:2303.15855v5}.'''
ed.replace(old,new,'D18','Add verified journal metadata while preserving the explicitly cited preprint pagination.','bibliography:IVVOkaOneV5')

for key in ('ffChen','mapsDeligne1974HodgeIII','Yang2012AC'):
    pattern=r'\\bibitem(?:\[[\s\S]*?\])?\{'+re.escape(key)+r'\}[\s\S]*?(?=\\bibitem|\\end\{thebibliography\})'
    # Search within the bibliography so an optional-label match cannot start at an earlier item.
    start=ed.text.index('\\begin{thebibliography}')
    candidates=list(re.finditer(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',ed.text[start:]))
    match=next(m for m in candidates if m[1]==key)
    a=start+match.start(); b=ed.text.find('\\bibitem',start+match.end())
    if b<0: b=ed.text.index('\\end{thebibliography}',start+match.end())
    old=ed.text[a:b]
    before_bib=ed.text[:start]
    cited={k.strip() for c in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}',before_bib) for k in c.split(',')}
    assert key not in cited
    ed.replace(old,'','D18','Remove an uncited inline bibliography entry after proof consolidation; the source and verification history remain in the shared bibliography and checking records.','bibliography:'+key)

for patch in patches:
    ed.record('D18',patch['old_text'],patch['new_text'],patch['reason'],
              'shared-bibliography:'+patch['key'],old_location='shared bibliography entry',new_location='shared bibliography entry')
ed.save()
bib_path.write_text(bib)
receipt={'patch_count':len(patches),'bib_sha256':hashlib.sha256(bib_path.read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(ed.path.read_bytes()).hexdigest(),
         'primary_receipts':['agents/v_analytic/literature/S6_SERIES_PUBLISH_V_Teschl_locator_receipt.json',
                             'agents/v_analytic/literature/S6_SERIES_PUBLISH_V_DLMF_locator_receipt.json']}
(ROOT/'records/S6_SERIES_PUBLISH_V_bibliography_integration.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
