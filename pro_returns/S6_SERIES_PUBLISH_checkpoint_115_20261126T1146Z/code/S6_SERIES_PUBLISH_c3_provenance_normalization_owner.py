#!/usr/bin/env python3
"""Restore the missing normalization criterion in a proposal, without shared writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance/normalization_owner'
OUT.mkdir(parents=True,exist_ok=True)
comp=ROOT.parent/'S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_II.tex'
ct=comp.read_text()
start=ct.index(r'\begin{proposition}[Credited re-derivation: The precise range of the normalization formula]')
old_owner=ct[start:ct.index(r'\end{proof}',start)+len(r'\end{proof}')]
current=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
label='lem:II:persistent-normalization-pullback'
start=current.index(r'\begin{lemma}[Persistent sections and the normalization pullback]')
end=current.index(r'\end{proof}',start)+len(r'\end{proof}')
old_p263=current[start:end]

new_owner=r'''\begin{cited}[The normalization criterion]\hypertarget{tag-01AH}{}\label{cdp:st:A.2.3}
\StatementRecord{cdp:st:A.2.3}{proved}{01AH}{\SeriesRef{cdp:st:A.2.1}, \SeriesRef{cdp:st:A.2.2}; \cite[Theorems~1.1 and~1.3, p.~3; proof of Theorem~1.3, p.~12; Proposition~3.4 and Corollary~3.5, pp.~9--10, arXiv v7]{GS2014}}
For a reduced hypersurface $S$ with the notation of
\cref{cdp:st:A.2.1,cdp:st:A.2.2}, the canonical inclusion
$\eta_*\eta^*N^*\hookrightarrow K$ is an isomorphism exactly when
$S$ has normal crossings outside an analytic subset of codimension
at least two in $S$.
\end{cited}
\begin{proof}[Application of the cited residue criterion]
Apply \cite[Proposition~3.4 and Corollary~3.5, pp.~9--10,
arXiv v7]{GS2014} with their hypersurface $D=S$, local equation
$h=F$, local ring $R=\mathcal O_S$, and normalization ring
$B=\eta_*\mathcal O_{\widetilde S}$. The multiplier map
$q\mapsto(b\mapsto qb)$ identifies their residue module
$\mathcal R_D$ with $J^{-1}=\operatorname{Hom}_R(J,R)$ as
submodules of the same total quotient ring. Their weakly
holomorphic functions form $B$, and their inclusion
$B\subset\mathcal R_D$ is the inclusion of \cref{cdp:st:A.2.2}.
Theorem~1.1, implication $(B)\Rightarrow(C)$, and Theorem~1.3
in \cite[p.~3; proof of Theorem~1.3, p.~12]{GS2014} give
$J^{-1}=B$ exactly for the asserted normal-crossing locus.
Tensor this equality by the invertible sheaf $N^*$.
The finite projection formula and the map
$[F]\otimes q\mapsto q\,dF|_S$ of \cref{cdp:st:A.2.1}
identify its two sides with $\eta_*\eta^*N^*$ and $K$, and
identify their inclusion with the canonical map in the statement.
\end{proof}'''

old='Every codimension-one singularity of $S$ is then an ordinary node, and \\cref{cdp:st:A.2.3} identifies the inverse-Jacobian kernel with the normalization kernel globally, including its codimension-two points.'
new=r'''Every codimension-one singularity of $S$ is then an ordinary
node. Apply \cref{cdp:st:A.2.3} to this reduced hypersurface:
its normalization criterion gives $\mathcal J^{-1}=
\eta_*\mathcal O_T$ on all of $S$. Under the map
$[F]\otimes q\mapsto q\,dF|_S$ of \cref{cdp:st:A.2.1},
the inverse-Jacobian kernel is therefore
$\eta_*\eta^*\mathcal O_Y(-S)$.'''
assert old_p263.count(old)==1
new_p263=old_p263.replace(old,new)
statement=lambda s:s[:s.index(r'\end{lemma}')+len(r'\end{lemma}')]
assert statement(old_p263)==statement(new_p263)
digest=lambda s:hashlib.sha256(s.encode()).hexdigest()
def tsv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

(OUT/'S6_SERIES_PUBLISH_normalization_owner_proposed.tex').write_text(new_owner+'\n',newline='\n')
(OUT/'S6_SERIES_PUBLISH_P263_proposed.tex').write_text(new_p263+'\n',newline='\n')
rows=[dict(change_id='II-C3-NORM-001',type='D04;D06;D17;D18',statement_id='cdp:st:A.2.3',old_location=str(comp)+'; complete original owner near line 53002',old_page='attached compendium source',new_location='After cdp:st:A.2.2 and before cdp:st:A.1.2',new_page='integrated build pending',old_text=old_owner,new_text=new_owner,reason='Restore every mathematical clause at legacy tag 01AH as a cited result. The exact fractional-ideal embedding, tensor factor and projection map transfer the opened residue criterion. The cited source proves both directions; no generic-codimension assertion is inferred from A.1.2 alone.',review_status='Complete old and receiving owner read and compared; used and rechecked in this run.'),
dict(change_id='II-C3-NORM-002',type='D04;D06;D22',statement_id=label,old_location='P263 proof, reduced horizontal conductor case',old_page='cp35 integrated source; final page pending',new_location='Same proof, same case',new_page='integrated build pending',old_text=old,new_text=new,reason='Write the exact restored criterion application and the conormal multiplier map. The coefficient-one branch calculation and whole persistent-normalization statement are retained; no reflexivity or Hartogs conclusion is substituted.',review_status='Complete nine-step old and receiving P263 proof read and compared; used and rechecked in this run.')]
tsv('S6_SERIES_PUBLISH_normalization_owner_defects.tsv',rows)
tsv('S6_SERIES_PUBLISH_normalization_owner_sources.tsv',[dict(source_id='II-C3-NORM-GS-v7',url='https://arxiv.org/pdf/1109.2612v7',secondary_opened_primary_url='https://agag-mschulze.math.rptu.de/download/dlr',version='arXiv:1109.2612v7, 22 May 2014',locus='Theorems 1.1 and 1.3, p.3; complete proof of 1.3, p.12; complete Proposition 3.4 and proof, pp.9–10; complete Corollary 3.5 and proof, p.10',sha256='98bf8328a08614509b1dcc20d2e387d7c5a2cce5b70687cf7ad77a1a21aa70dc',bytes=305372,own_paraphrase='For reduced complex hypersurfaces, logarithmic residues equal the normalization ring exactly when the hypersurface has normal crossings outside a subset of relative codimension at least two. The dual Jacobian module is the same residue fractional ideal. Taking D=S and h=F, then tensoring by the conormal line and using q times dF, gives the precise canonical kernel identity.',reading_limit='Theorem 1.1 is read as the complete Saito theorem as stated by these authors. The complete printed proof of their Theorem 1.3 and Proposition 3.4/Corollary 3.5 were read. No claim to reopening Saito 1980 is made.')])
now=datetime.now(timezone.utc).isoformat()
events=[]
for own,outcome in [('cdp:st:A.2.3','Read the complete attached original owner and the receiving cited owner. Opened exact arXiv v7 theorems and complete proofs at the specified loci. The identity D=S, h=F and multiplier q acting on J identifies the two fractional ideals; tensor by N* and finite projection identify both canonical kernel maps.'),(label,'Recompared all nine original and receiving proof steps, including the ruled conductor cases, exact blowdown formula, coefficient-one and coefficient-two branches, Picard support and descent from the resolution. The restored criterion supplies the precise global equality in step 4. The entire original statement remains byte-identical.')]:
    events.append(dict(statement_id=own,date='2026-11-22',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance',type='used and rechecked in this run',outcome=outcome+' This is an exposed comparison, not an independent derivation or final PDF reading.',event_id='publish:c3:normalization-owner:'+own,phase='publication text and proof comparison',source_file='agents/continuation3_provenance/normalization_owner/S6_SERIES_PUBLISH_normalization_owner_CHECK_EVENTS.tsv',source_row='',source_event_type='used and rechecked in this run',evidence_group='publish:c3:normalization-owner:'+own,publish_input_file='',publish_input_row='',date_utc=now,where='Complete old/receiving owner and P263 application comparison'))
tsv('S6_SERIES_PUBLISH_normalization_owner_CHECK_EVENTS.tsv',events)
tsv('S6_SERIES_PUBLISH_normalization_statement_guard.tsv',[dict(statement_id=label,old_sha256=digest(statement(old_p263)),new_sha256=digest(statement(new_p263)),outcome='Full statement bytes unchanged.')])
oldbib=r'\newblock URL \url{https://arxiv.org/pdf/1109.2612}.'
newbib=r'\newblock arXiv:1109.2612v7, 22 May 2014.'+'\n'+r'\newblock URL \url{https://arxiv.org/pdf/1109.2612v7}.'
assert current.count(oldbib)==1
tsv('S6_SERIES_PUBLISH_bibliography_146_edits.tsv',[dict(change_id='II-C3-PROV-146',type='D18',statement_id='bib:GS2014',old_location='GS2014 bibliography entry',old_page='source; final page pending',new_location='same entry',new_page='integrated build pending',old_text=oldbib,new_text=newbib,reason='Pin the exact freshly opened version used throughout the body while retaining the publisher citation and DOI.',review_status='Version title margin and complete cited loci read; source admission pending.')])
print('Prepared restored tag 01AH, exact P263 application, two exposed events, statement guard and bibliography ID 146; shared source unchanged.')
