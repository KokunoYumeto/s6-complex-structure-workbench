from pathlib import Path
import csv,json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
counts=list(csv.DictReader((r/'records/S6_SERIES_PUBLISH_check_counts.tsv').open(),delimiter='\t'))
c=next(x for x in counts if x['paper']=='I' and x['scope']=='current_printed_statements_and_definitions')
method=r'''\subsection{Methodology}
This text is AI-produced; no part of it was written by a human.
GPT-5.6 Sol (OpenAI), in Codex at reasoning effort ultra, contributed
to the working edition of 24 August--9 September 2026. The pinned
repository's authorship record also credits GPT-6 Astra (OpenAI),
at reasoning effort ultra, from 5 September.
GPT-6 Astra (OpenAI), in ChatGPT Pro mode, carried out the research
of 12--16 November, the independent re-derivation of 16--18 November,
and the writing of 16--20 November 2026. The publication revision
and further checks of this paper were undertaken by GPT-6 Astra
on 20--21 November 2026. The reasoning-effort setting of this
publication session was inherited; the interface exposed no separate
numerical setting.

Claude Fable 5.2 (Anthropic), at effort high and at effort max,
and Claude Opus 5.5 (Anthropic), at effort max, undertook readings,
intakes, checks and recomputations on 12--20 November 2026.
Their objections and calculations were compared with the statements,
proofs and cited sources, and the resulting corrections were
incorporated into the text. The records specify the passages and
calculations examined by each model.

For the statements printed in this paper, the record contains
@TARGETED@ examinations of proof steps, @REPROOF@ independent
re-derivations, and @COMPUTATION@ computations or formal certificates.
It also records @USED@ readings of the proofs and applications,
@BACKGROUND@ uses of background results without a fault found,
and @REFUTED@ refutation associated with its corrected statement.
Each total counts recorded links from a check to a statement;
one calculation used for several statements can contribute several
links. Every outcome specifies its scope. Re-reading an edited proof
is recorded separately from deriving its steps before comparison.
Exact algebra, numerical enclosures and analytic arguments retain
their respective scopes, and the records identify the implementations
used for independent computational comparisons.
No human has checked the mathematics.

The historical sources, programs and check records are available in the
\href{https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/\SsixRepositoryCommit/pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/}{project repository}.
The additional records and programs of this publication revision
accompany its source distribution.
The text and accompanying work are dedicated to the public domain under
\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0 1.0 Universal}.

'''
keys={'TARGETED':'targeted proof check','REPROOF':'independent re-proof','COMPUTATION':'computation or formal certificate','USED':'used and rechecked in this run','BACKGROUND':'carried as background without fault found','REFUTED':"refuted, with the refined statement's id"}
for token,key in keys.items():method=method.replace('@'+token+'@',c[key])
a=ed.text.index(r'\subsection{Methodology}');b=ed.text.index(r'\subsection{How the paper is organized}',a)
old=ed.text[a:b]
if old!=method:ed.replace(old,method,'D01','State verified model/effort/date facts and recomputed scoped totals in plain language; remove internal run names and file links.','sec:results')
macro=r'\newcommand{\SsixRepositoryCommit}{83d76022bcd442278b760db9ff438afceed6c6ea}'
if r'\newcommand{\SsixRepositoryCommit}' not in ed.text:
 ed.replace(r'\allowdisplaybreaks[2]',r'\allowdisplaybreaks[2]'+'\n'+macro,'D09','Define the immutable repository commit once for the methodology link and every program source.','tab:I:programs')
oldpara=r'''This paper is the first of a series on the holomorphic families built
from the $(3,4,\infty)$ family of torus-fibred complex structures on
$S^6$ \citep{AC2026,Engel2026}.  The table gives the main result of each paper
of the series and the papers it uses.'''
newpara=r'''This series studies the $(3,4,\infty)$ family of torus-fibred complex
structures on $S^6$ \citep{AC2026,Engel2026}, its periods, maps and smooth
monodromy, and the higher-dimensional complex manifolds built from it.
The table gives the main result of each paper and the papers it uses.'''
if oldpara in ed.text:ed.replace(oldpara,newpara,'D07','Use the common series paragraph without a paper-specific ordinal.','sec:results')
ed.save()
(r/'records/S6_SERIES_PUBLISH_series_overview_paragraph.tex').write_text(newpara+'\n')
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'counts':c,'events_sha256':hashlib.sha256((r/'CHECK_EVENTS.tsv').read_bytes()).hexdigest(),'counts_sha256':hashlib.sha256((r/'records/S6_SERIES_PUBLISH_check_counts.tsv').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'scope':'Counts computed from the current merged ledger for current printed statement identities, including retained aliases. Final source/distribution/deposit synchronization is still required after remaining checks.'}
(r/'records/S6_SERIES_PUBLISH_I_methodology_counts.json').write_text(json.dumps(receipt,indent=2)+'\n')
