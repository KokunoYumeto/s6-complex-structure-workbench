"""Shorten the source-status table and state the exposed model-effort scope."""
from S6_SERIES_PUBLISH_c3_edit import *

text = SOURCE.read_text()
start = text.index(r'\subsection{Known and new}')
end = text.index(r'\subsection{Methodology}', start)
old = text[start:end]
new = r'''\subsection{Known and new}
\begingroup\small
\begin{longtable}{@{}p{.10\textwidth}p{.85\textwidth}@{}}
\toprule Theorem & Status and source\\\midrule\endhead
A & New normalization criterion extending \cite[\S10.4, pp.~87--90]{AC26};
corrects \cite[Theorem~2.2, p.~680]{CDP2020} and
\cite[Proposition~1.1, p.~78; Lemma~1.5, pp.~79--80]{CDP98}.\\
B & New integral refinement and fibre classification; the rational component
formula is \cite[\S10.5, p.~91]{AC26}.\\
C & New unrestricted sign and equality theorem; standard-family Euler value:
\cite[Theorem~7.22, p.~60]{AC26} and \cite[Proposition~7.1, p.~17]{Engel2026}.\\
D & New local parity and refinements of each fixed punctured family:
\cref{cdp:st:C.2.UN.1,cdp:st:C.2.UN.4,cdp:st:C.2.UN.14}.\\
E & New twisted formulas and normalization-map ranks; untwisted values:
\cite[Theorem~6.12, pp.~81--82]{DGKXv1}, arXiv version~1.\\
F & New answers to \cite[\S10(1), p.~33]{Viaclovsky2026Combs} and
\cite[\S1.1(1), p.~2]{Viaclovsky2026Log}, with twelve-tooth Hodge values;
corrects \cite[Corollary~1.3, preprint p.~2]{HKP2000}.\\
G & New minimal covering for the fixed scalar and root data of
\cite[equation~(2.3), p.~4; Lemma~2.7 and Corollary~2.8, pp.~6--7;
Proposition~3.6 and Definition~3.7, pp.~9--10]{LiuRollenske2026}, arXiv version~2.\\
\bottomrule\end{longtable}\endgroup
'''
apply_edit(old, new, 'II-C3-FIRSTPART-TABLE', ['D12','D15','D23'],
           'series:II:A;series:II:B;series:II:C;series:II:D;series:II:E;series:II:F;series:II:G',
           'Results and their proofs in outline, Known and new',
           'Replace repeated source-comparison paragraphs by one short status entry per main theorem. Exact detailed source comparisons remain beside the full statements in section 1.2. Widen the Theorem column from .08 to .10 of the text width to remove its 1.7175 pt header overflow.',
           'Root read the full original and receiving table and the full corresponding main-theorem statements and literature paragraphs. No theorem statement or proof changes; literature scope follows the admitted primary-source comparisons.')
old = 'GPT-6 Astra (OpenAI), in ChatGPT Pro mode, carried out the research\nof 12--16 November, the independent re-derivation of 16--18 November,'
new = 'GPT-6 Astra (OpenAI), in ChatGPT Pro mode, with the effort setting\nnot separately exposed, carried out the research of 12--16 November,\nthe independent re-derivation of 16--18 November,'
apply_edit(old, new, 'II-C3-FIRSTPART-EFFORT', ['D15'], 'II',
           'Results and their proofs in outline, Methodology',
           'State the exposed effort-setting information for the ChatGPT Pro work without inventing an unreported setting. Final count recomputation remains at text-final.',
           'Root compared the original and receiving methodology sentences with the prompt and current check-event identity. No count or date recomputation is made here.')
add_event('series:II:A;series:II:B;series:II:C;series:II:D;series:II:E;series:II:F;series:II:G',
          'II-C3-FIRSTPART-TABLE-EFFORT', 'used and rechecked in this run',
          'Root read and compared the complete old/new source-status table, complete main statements with their literature paragraphs, and the bounded methodology effort sentence. Detailed source comparisons remain in section 1.2; one short status row per theorem replaces repeated paragraphs. Every theorem statement and proof is unchanged. The ChatGPT Pro effort is stated as not separately exposed. No independent check, final counts, final layout or whole-unit completion is credited.',
          'Section 1.4 source-status table and section 1.5 model-effort sentence', source=__file__)
print('Short source-status table and explicit exposed-effort scope admitted; first-part final integration remains open.')
