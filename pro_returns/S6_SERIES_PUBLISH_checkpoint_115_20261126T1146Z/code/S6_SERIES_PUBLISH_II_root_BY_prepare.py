from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
P=R/'agents/continuation2_root/01BY'
old_path='agents/ii_infra/released_proofs/01BY/f0df7a4f2d18c00b/S6_SERIES_PUBLISH_full_owning_block.tex'
old=(R/old_path).read_text();work=old;guards=[]
def change(a,b,kind,reason):
 global work
 assert work.count(a)==1,(a,work.count(a))
 guards.append(dict(old=a,new=b,type=kind,reason=reason));work=work.replace(a,b,1)
marker=next(x for x in old.splitlines(True) if x.startswith('\\StatementRecord'))
change(marker,'','D10','Move machine metadata to the check file; retain the permanent tag target and every label.')
change(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D10','Remove the production marker from proof-item numbering.')
change('We first recall exactly how a finite attachment bound gives\nthe Euler inequality.','A finite attachment bound gives the Euler inequality as follows.','D08','State the mathematical use of the attachment bound directly.')
change('the exact graph count (C.RA.24)',r'the graph count \eqref{cdp:eq:C.RA.24}','D04','Replace the inherited equation identifier by its hyperlinked number.')
change(r'The complete computation \CompendiumRef{II}{cdp:st:C.2.RAT.6}',r'The cubic-suspension bound of \cref{cdp:st:C.2.RAT.6}','D04','Resolve the compendium reference to the restored, verified statement in this paper.')
change('(C.D4.8)--(C.D4.12)',r'\eqref{cdp:eq:C.D4.8}--\eqref{cdp:eq:C.D4.12}','D04','Use the printed hyperlinked equation numbers for the cyclic-cover calculation.')
change('Thus (C.D4.10) gives',r'Thus \eqref{cdp:eq:C.D4.10} gives','D04','Replace the bare equation identifier by its number.')
change('This contradicts (C.D4.2)',r'This contradicts \eqref{cdp:eq:C.D4.2}','D04','Link the torus-pairing obstruction by its printed equation number.')
change('These summands describe the normalization in\ncodimension one and hence everywhere by normality.',
       'Locally, with $F=\\{s=0\\}$ and the reduced horizontal equation $r$,\n'
       'the basis $1,w,v=w^2/s$ has multiplication\n'
       '$w^2=sv$, $wv=sr$ and $v^2=wr$. It is a finite free algebra\n'
       'over the smooth base, so it satisfies Serre\'s $S_2$ condition.\n'
       'Its generic branch parametrizations make it regular in codimension\n'
       'one. Serre\'s criterion therefore identifies it with the normalization.',
       'D22','Supply the finite-free algebra and the exact S2/R1 normality argument underlying the original eigensheaf step.')
assert old.count('\\item')==work.count('\\item')==6
assert re.findall(r'\\\[(.*?)\\\]',old,re.S)==re.findall(r'\\\[(.*?)\\\]',work,re.S)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
 assert re.findall(pat,old)==re.findall(pat,work)
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert source.count(old)==1
for label in ['cdp:eq:C.RA.24','cdp:st:C.2.RAT.6','cdp:eq:C.D4.8','cdp:eq:C.D4.10','cdp:eq:C.D4.12','cdp:eq:C.D4.2']:
 assert source.count('\\label{'+label+'}')==1,label
program='S6_SERIES_PUBLISH_II_root_BY_prerelease.py'
row='Rational triple-cover contact partitions, character cohomology and attachment bounds (\\cref{cdp:st:C.2.D4.3}) & \\href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\\SsixRepositoryCommit/code/'+program+'}{\\nolinkurl{'+program+'}} \\\\[3pt]\n'
anchor='\\end{longtable}}\n\n\\begin{thebibliography}'
assert source.count(anchor)==1
extra=dict(old=anchor,new=row+anchor,type='D09',owner='Programs',location='Programs',reason='Cite the new exact contact-partition computation once in the Programs table through the common commit macro.')
for name,data in [('proposed_v1.tex',work),('guards.json',json.dumps(guards,indent=2)+'\n'),('programs_guard.json',json.dumps(extra,indent=2)+'\n')]:
 p=P/('S6_SERIES_PUBLISH_II_root_BY_'+name);assert not p.exists();p.write_text(data)
 print(json.dumps(dict(path=str(p.relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size)))
