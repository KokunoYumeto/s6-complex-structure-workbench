from pathlib import Path
import datetime as dt, hashlib, json, re

R=Path(__file__).resolve().parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def bind(p): return dict(path=p,sha256=sha((R/p).read_bytes()))
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert sha(source.encode())=='c7423fc0de48299a4c6d2a7c2064cf985d5e49af7d79096f55848120f2939363'
out=R/'agents/continuation2_root/S6_SERIES_PUBLISH_II_RAT6_restore_plan.json'
assert not out.exists()
blockpath='agents/continuation2_root/S6_SERIES_PUBLISH_II_RAT6_proposed.tex'
block=(R/blockpath).read_text()
assert source.count(r'\hypertarget{tag-01CI}')==0
anchor=r'\begin{proposition}[Every primitive rational double ordinary-triple cover has nonnegative Euler number]'
edits=[dict(type='D13',owner='cdp:st:C.2.RAT.6',old=anchor,new=block+'\n\n'+anchor,
 reason='Restore the inherited01CI known-result anchor and the exact delta-five form used by the paper. The sources give classification and invariant formulas; the short application supplies the needed bound under the known-result exception. Original extended derivation stays bound in the attached research source; no new required-check row.')]
start=source.index('Here are its equations and derivation. A reduced plane germ')
end=source.index('\\paragraph{Homology and the compact intersection pairing.}',start)
old=source[start:end]
assert old.count('\\item')==1
new=r'''Cited result~\ref{cdp:st:C.2.RAT.6} gives the geometric-genus
bound and the sum of the link first Betti numbers, since
the total delta here is at most four. The negative-definite
exceptional intersection matrix identifies the rational
first homology of each link with $H_1(Q_p;\Q)$: in the
homology sequence of its plumbed neighbourhood the map on
second homology is that invertible matrix. Thus it gives
exactly the two bounds in \eqref{cdp:eq:C.D4.7}.

\item '''
edits.append(dict(type='D14',owner='cdp:st:C.2.D4.1',old=old,new=new,
 reason='Consolidate the repeated local normal-form and invariant calculation into the single restored cited result01CI. The exact map is the identity on each local equation w^3=r and the restriction of its delta-five table to total delta at most four. The original local link-to-exceptional-divisor plumbing map remains here; all subsequent global cyclic-cover and homology steps remain byte-identical. The former two enumeration items become the local comparison and the already existing global cohomology paragraph.'))
oldrow='Cubic-suspension Jacobian spectra by the Koszul Hilbert series (\\cref{cdp:st:C.2.D4.1})'
edits.append(dict(type='D13',owner='Programs',old=oldrow,new='Cubic-suspension Jacobian spectra by the Koszul Hilbert series (\\cref{cdp:st:C.2.RAT.6})',reason='Associate the existing computation citation with the single owner of the consolidated local table; the program and link are unchanged.'))
arnold=r'''\bibitem[Arnold(1976)]{Arnold1976NormalForms}
Vladimir I. Arnold.

\newblock Local normal forms of functions.

\newblock \emph{Inventiones Mathematicae}, 35:\penalty0 87--109, 1976.

\newblock URL \url{https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf}.
\newblock \emph{Verified}.

'''
anchor2=r'\bibitem[Atkin and Garvan(2002)]{AtkinGarvan2002}'
edits.append(dict(type='D13',owner='Bibliography',old=anchor2,new=arnold+anchor2,reason='Restore the exact opened published Arnold source for the analytic normal-form list. Printed pp92,95,101 read as images and p100 read in extraction; published scan hash and scope recorded.'))
mtstart=source.index('\\bibitem[Merle and Teissier(1976--1977)]')
mtend=source.index('\\bibitem[Milnor(1968)]',mtstart)
mtold=source[mtstart:mtend]
mtnew=mtold.replace('Merle and Teissier','Teissier and Merle').replace('Michel Merle and Bernard Teissier.','Bernard Teissier and Michel Merle.')
edits.append(dict(type='D13',owner='Bibliography',old=mtold,new='',reason='Move the entry to its correct first-author position, retaining the citation key and all verified publication data. The primary scan lists Teissier before Merle.'))
anchor3=r'\bibitem[Teleman(2006)]{Teleman2006}'
edits.append(dict(type='D13',owner='Bibliography',old=anchor3,new=mtnew+anchor3,reason='Restore the author order Teissier, Merle and place the rendered entry before Teleman. Citation key MerleTeissier1977 is retained so every existing citation resolves.'))
candidate=source
for e in edits:
 assert candidate.count(e['old'])==1,e['owner']
 candidate=candidate.replace(e['old'],e['new'],1)
assert candidate.count(r'\hypertarget{tag-01CI}')==1
# Every existing permanent tag and label is retained; the restored owner adds one.
for pattern in [r'\\hypertarget\{([^}]+)\}',r'\\label\{([^}]+)\}']:
 before=re.findall(pattern,source);after=re.findall(pattern,candidate)
 for token in set(before): assert before.count(token)==after.count(token),token
bwstart=candidate.index(r'\begin{proposition}[A connected triple tangent-root cover') if r'\begin{proposition}[A connected triple tangent-root cover' in candidate else candidate.rfind('\\begin{proposition}',0,candidate.index('\\hypertarget{tag-01BW}'))
bwend=candidate.index('\\end{proof}',bwstart)+len('\\end{proof}')
bw=candidate[bwstart:bwend]
bwpath='agents/continuation2_root/S6_SERIES_PUBLISH_II_BW_RAT6_consolidated_proposed.tex'
assert not (R/bwpath).exists();(R/bwpath).write_text(bw)
assert bw.count('\\item')==12
bibpath='S6_SERIES_PUBLISH_references.bib';bib=(R/bibpath).read_text()
assert 'Arnold1976NormalForms' not in bib
bibanchor='  author = {Merle, Michel and Teissier, Bernard},'
assert bib.count(bibanchor)==1
bibnew=bib.replace(bibanchor,'  author = {Teissier, Bernard and Merle, Michel},',1)
newentry=r'''
@article{Arnold1976NormalForms,
  author = {Arnold, Vladimir I.},
  title = {Local Normal Forms of Functions},
  journal = {Inventiones Mathematicae},
  volume = {35},
  pages = {87--109},
  year = {1976},
  url = {https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf},
  verification = {verified at listed scope},
  source_note = {Published university-hosted scan, SHA256 1d75961a44caa5dba08a5729fcf612b1c94a479df02e64bcb1bbf8f3e32ebee8. Actually read printed pp92,95,101 as images and p100 in extraction on22November2026. Section1 I.0 gives ADE equations; II1 gives the complete nonzero-cubic-jet list and Milnor numbers, including J2,0 with its discriminant and absent c term; Section2 items1-12 give the determinator and analytic-germ notation. Scope is these loci, not the whole paper.}
}
'''
bibnew+=newentry
bibproposed='agents/continuation2_root/S6_SERIES_PUBLISH_references_RAT6_proposed.bib'
# This is a short exact edit plan, not a full per-batch bibliography copy.
bibedits=[dict(old=bibanchor,new='  author = {Teissier, Bernard and Merle, Michel},',reason='Primary source author order'),dict(append=newentry,reason='Opened exact normal-form source')]
plan=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),source_before_sha256=sha(source.encode()),source_after_sha256=sha(candidate.encode()),source_edits=edits,bib_before_sha256=sha(bib.encode()),bib_after_sha256=sha(bibnew.encode()),bib_edits=bibedits,restored_block=bind(blockpath),BW_proposed=bind(bwpath),freeze=bind('agents/continuation2_root/S6_SERIES_PUBLISH_II_root_RAT6_freeze.json'),required_rows_changed=0,required_count=197,proof_items_BW=12,scope='Known-result support and duplicate consolidation only. Does not modify any open target owning block, including01BX and the B checker targets; does not assign independent or final-page reading credit.')
out.write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps(dict(plan=bind(str(out.relative_to(R))),BW_proposed=plan['BW_proposed'],source_after_sha256=plan['source_after_sha256'],source_edit_count=len(edits)),indent=2))
