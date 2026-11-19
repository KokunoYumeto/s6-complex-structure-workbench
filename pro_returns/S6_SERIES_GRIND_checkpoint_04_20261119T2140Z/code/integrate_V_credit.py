"""Integrate exact opened-source specializations and their convention maps."""
from pathlib import Path
import json,csv,re
ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(10**9)
bodypath=ROOT/'parts/V.body.linked.tex';body=bodypath.read_text();changes=[]
for patch in json.loads((ROOT/'audit_corrections/V_known_result_proof_patches.json').read_text()):
 lab=patch['label'];pos=body.index('\\label{'+lab+'}');a=body.index(r'\begin{proof}',pos);b=body.index(r'\end{proof}',a)+len(r'\end{proof}')
 new=patch['tex'].replace('pp.~56--58','attached-source edition, pp.~57--59').replace('p.~58]{Yang2026}','attached-source edition, p.~59]{Yang2026}')
 old=body[a:b]
 if old==new:continue
 changes.append(dict(paper='V',label=lab,operation='replace_complete_known_specialization_proof',old=old,new=new,reason=patch['source']+'; page references explicitly use the stable attached-source build.'))
 body=body[:a]+new+body[b:]
bodypath.write_text(body)
frontpath=ROOT/'frontmatter/frontmatter_V.tex';front=frontpath.read_text()
for patch in json.loads((ROOT/'audit_corrections/V_literature_front_patches.json').read_text()):
 pos=front.index('\\label{'+patch['label']+'}');a=front.index(r'\textit{Relation to literature.}',pos);b=front.index(r'\hyperlink{outline-',a)
 new=patch['tex'].replace('pp.~56--58','attached-source edition, pp.~57--59')+'\n'
 old=front[a:b]
 if old==new:continue
 changes.append(dict(paper='V',label=patch['label'],operation='replace_source_relationship',old=old,new=new,reason='Exact source and bundle transports from the independently opened-source comparison.'))
 front=front[:a]+new+front[b:]
frontpath.write_text(front)
comparison=(ROOT/'audit_corrections/V_root_curve_comparison.tex').read_text()
comparison=comparison.replace('There are root maps',r'Write $L_{3,4}=\mathcal O(\tfrac13[0]-\tfrac14[1])$ and $L_{5,4}=\mathcal O(\tfrac45[0]-\tfrac34[1])$ on their respective root curves. There are root maps')
comparison=comparison.replace('multiplication\nby this rational function gives the line-bundle identification.',r'multiplication by $(t-1)/t$ sends $q_3^*L_{3,4}$ to $T^5$ in the meromorphic-section convention for $\mathcal O(D)$, and multiplication by $t/(t-1)$ is its inverse.')
(ROOT/'frontmatter/V_literature_comparison.tex').write_text(comparison)
# Fresh opened primary entry, with locators explicitly in the preprint.
raw=(ROOT/'audit_corrections/V_reference_addition.bib').read_text()
(ROOT/'analysis/additional_references.bib').write_text(raw)
bbl=r'''\bibitem[Yang(2012)]{Yang2012AC}
Huijun Yang.
\newblock Almost complex structures on $(n-1)$-connected $2n$-manifolds.
\newblock \emph{Topology and its Applications}, 159:1361--1368, 2012.
\newblock \doi{10.1016/j.topol.2011.12.013}.
\newblock Original preprint: \url{https://arxiv.org/pdf/1110.1798}.
\newblock Verified in this writing: original arXiv v1 PDF, realification map on p.~1 and Theorems~1--2 on pp.~2--3.
'''
sourcepath=ROOT/'analysis/source_bibliography_entries.json';sources=json.loads(sourcepath.read_text());sources['Yang2012AC']=[{'paper':'V','text':bbl}];sourcepath.write_text(json.dumps(sources,indent=2))
with (ROOT/'S6_SERIES_GRIND_inventory.csv').open() as f:rows=list(csv.DictReader(f))
credit={r['label']:r for r in json.loads((ROOT/'audit_corrections/V_known_result_proof_patches.json').read_text())}
for row in rows:
 if row['label'] in credit:
  row['credited_to']='Yang2026, attached REPAIRED_v4_5 source, Theorem8.7 and Corollary8.8; exact n=3, D=C, marked Kuhn-fan specialization.'
  row['notes']+=' The long re-derivation is replaced by the cited specialization and exact identity map; earlier proof preserved in analysis/V_credit_changes.json.'
with (ROOT/'S6_SERIES_GRIND_inventory.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
path=ROOT/'analysis/V_credit_changes.json';prior=json.loads(path.read_text()) if path.exists() else [];path.write_text(json.dumps(prior+changes,indent=2))
print(json.dumps({'changed_spans':len(changes),'added_reference':'Yang2012AC','scope':'attached Yang source pagination only'}))
