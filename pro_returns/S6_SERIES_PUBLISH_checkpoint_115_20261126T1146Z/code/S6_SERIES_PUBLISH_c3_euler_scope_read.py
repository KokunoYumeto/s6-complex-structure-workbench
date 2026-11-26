"""Record the complete receiving read after the irreducible-scope clarification."""
from S6_SERIES_PUBLISH_c3_edit import *

text = SOURCE.read_text()
start = text.index(r'\begin{theorem}[The Euler sign for every degeneration and its equality criterion]')
end = text.index(r'\end{proof}', start) + len(r'\end{proof}')
fragment = text[start:end]
assert 'For a singular irreducible support $S$, write $Z\\to T\\to S$' in fragment
assert fragment.count(r'\item \textbf{') == 7
assert r'\cref{cdp:st:C.2.INT.3}' in fragment
add_event(
    'cdp:st:C.2.G.1', 'II-C3-EULER-IRREDUCIBLE-SCOPE-RECEIVING-READ',
    'used and rechecked in this run',
    'Root read the complete current theorem and all seven proof steps after the bounded scope edit. '
    'The holomorphic torsion statement K_Z+D applies to the normalization resolution of a singular irreducible support in mS. '
    'The reducible-support step instead uses the adjacent-component effective divisor with rationally trivial first Chern class '
    'and the exact normalization complement isomorphism into the INT.1--INT.3 arguments. '
    'Root had read all three complete proposed INT receiving proofs; their main-source admission is still pending, '
    'so the G.1 D25 receiver row stays open. This records a receiving-proof comparison, not an independent derivation or a final-page reading.',
    'S6_SERIES_PUBLISH_II.tex: cdp:st:C.2.G.1, complete statement and proof; '
    'agents/continuation3_provenance/sec07_tail/S6_SERIES_PUBLISH_INT_1_proposed.tex; '
    'agents/continuation3_provenance/sec07_tail/S6_SERIES_PUBLISH_INT_2_proposed.tex; '
    'agents/continuation3_provenance/sec07_tail/S6_SERIES_PUBLISH_INT_3_proposed.tex',
    source='code/S6_SERIES_PUBLISH_c3_euler_scope_read.py')
print('Complete receiving G.1 proof read recorded; D25 receiver remains open until the INT package is admitted.')
