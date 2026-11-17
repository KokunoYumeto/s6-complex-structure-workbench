"""Print every Paper I inventory row with its real in-paper label and audit scope."""
from pathlib import Path
import csv,re,json
OUT=Path(__file__).resolve().parents[2]
with (OUT/'S6_09_PAPERS_inventory.csv').open() as f:rows=[r for r in csv.DictReader(f) if r['paper']=='I']
s=(OUT/'S6_09_PAPERS_I.tex').read_text();labels=set(re.findall(r'\\label\{([^}]+)\}',s))
def esc(x):
 return ''.join({'&':r'\&','%':r'\%','#':r'\#','_':r'\_','$':r'\$','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}'}.get(c,c) for c in str(x))
short={'S6_02_FAMILY':'FAM','S6_02_PUSH':'PUSH','S6_01_INVARIANTS':'INV','S6_05_ARITHMETIC':'ARI','S6_03_CDP':'CDP','S6_04_MAPS_MANIFOLDS':'MAPS',
       'WORKING_EDITION':'WB','working_edition':'WB','WORKING_INV':'WB--INV','WORKING_CDP':'WB--CDP','course_CG-S6':'CG--S6','WORKING_EDITION_COURSE_PROVIDER':'CG prerequisite'}
tex=r'''% BEGIN GENERATED RESULT INDEX
\section{Result, source and verification concordance}
\label{app:I:result-index}
Each row identifies a source result and its actual statement in this paper.
Several source labels may share one statement. Their distinct complete
proofs remain at the adjacent proof or at the explicitly linked appendix;
the concordance is an index, not a substitute for any proof.
FAM, PUSH, INV, ARI, CDP and MAPS identify the six source runs; WB identifies
the working edition, and CG--S6 its course continuation.
All current full readings and source-to-print comparisons in this table
are by GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026.
The historical FAM reading is by Claude Fable 5.2 (Anthropic), effort high,
12 November 2026, 22:30 UTC. Other recorded readings by Claude Fable 5.2
(Anthropic), effort high or effort max, and Claude Opus 5.5 (Anthropic),
effort max, 12--16 November 2026, retain their exact per-result scopes in
the accompanying inventory. The check types are F (complete proof read),
D (steps independently re-derived), S (operative source statement opened
and hypotheses matched), and C (computation rerun). C is restricted to the
programs and outputs in Appendix~\ref{app:I:programs}; it never means that
a numerical computation checked a geometric argument.

\begingroup\small
\begin{longtable}{@{}p{40mm}p{16mm}p{92mm}@{}}
\toprule Source result & Printed number & Verification and source scope\\\midrule
\endfirsthead
\toprule Source result & Printed number & Verification and source scope\\\midrule
\endhead
'''
missing=[]
for r in rows:
 lab=r['printed_label']
 if lab not in labels:
  missing.append((r['source_run'],r['source_id'],lab));num='Pending final placement'
 else:num=r'\ref{'+lab+'}'
 sid=short.get(r['source_run'],r['source_run'])+' '+r['source_id']
 if r['source_id'] in ['C3.8'] or 'gauge-boundary' in r['source_id'] or 'literal-gauge' in r['source_id']:
  desc='F, D: complete partial construction; the literal coefficient evaluation remains open in the separate final part.'
 elif r['source_run']=='WORKING_EDITION_COURSE_PROVIDER':
  desc='F, D: complete classical proof or worked example read and re-derived; receiving source compared with the printed proof. The source attribution carries no novelty claim.'
 elif 'semidirect' in r['source_id']:
  desc='F, D: the commutator quotient and coinvariant abelianization are proved in full.'
 elif r['source_run']=='S6_05_ARITHMETIC' and r['source_id']=='C.7.4':
  desc='F, S: the conditional implication is checked with its named period-conjecture hypothesis; the hypothesis is not asserted.'
 elif r['source_run']=='S6_05_ARITHMETIC' and r['source_id']=='C.7.5':
  desc='C: the specified finite-precision integer-relation experiments were rerun. They are diagnostics and prove no algebraicity or transcendence assertion.'
 else:
  desc='F, S: full proof and operative dependencies checked; original and printed arguments compared. Re-derivations and computations are recorded at their exact individual scope.'
 # Exact source attributions remain explicit in the mathematical statements;
 # the index repeats the positive credit only, not long audit-log prose.
 credit=r['credited_to']
 if credit and not any(x in credit.lower() for x in ['present explicit','no exhaustive','pending']):
  desc+=' Credit: '+credit
 tex+=r'\path{'+sid.replace(' ',r'}\ \path{')+'} & '+num+' & '+esc(desc).replace(r'\_',r'\_\allowbreak ')+r'\\'+'\n'
tex+=r'\bottomrule\end{longtable}\endgroup'+'\n'
tex+=r'''The original-source comparisons and exact proof hashes are retained in
the inventory. A nonoperative unverified bibliography entry is not a source
check. Historical gaps and partial arguments are not erased by a subsequent
proof: the former and the repair are both recorded, and the complete
mathematical arguments are printed at their indicated statements.
% END GENERATED RESULT INDEX
'''
(OUT/'editorial/I_result_index.tex').write_text(tex)
(OUT/'records/I_index_missing.json').write_text(json.dumps(missing,indent=2)+'\n')
print('Rows',len(rows),'unplaced',len(missing))
