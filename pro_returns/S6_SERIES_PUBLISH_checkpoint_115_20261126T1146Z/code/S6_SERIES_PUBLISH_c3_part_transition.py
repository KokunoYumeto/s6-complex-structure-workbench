"""Keep the arbitrary-degeneration transition with its part and conventions."""
from S6_SERIES_PUBLISH_c3_edit import *

apply_edit('Hirzebruch surfaces are simply connected and a\neach point-blowup map',
 'Hirzebruch surfaces are simply connected and\neach point-blowup map',
 'II-C3-EXAMPLE-RECEIVING-GRAMMAR',['D23'],'night:P4.10',
 'Complete receiving proof, point-blowup sentence',
 'The full receiving reading found an extra article left at the exact proof-reference substitution. Remove it; the map and assertion are unchanged.',
 'Caught and repaired during complete receiving reading, after the clean working build.')
s=SOURCE.read_text()
a=s.index(r'\section{The degeneration and its normalization maps}')
b=s.index(r'\section{Unrestricted Euler topology and component covers}',a)
old=s[a:b]
new=r'''This part studies the Euler topology and component geometry of torus
degenerations with arbitrary central supports. The global sign statements
use the setting of \cref{def:II:standing-torus-fibration}; the local
degenerations and comparison constructions have the hypotheses in their
statements. We begin with Euler parity and vertical modifications, then
study component covers, compact realizations and contractions.

'''
apply_edit(old,new,'II-C3-DEGENERATION-PART-TRANSITION',['D12','D13','D14','D20','D24'],
 'the-degeneration-and-its-normalization-maps',
 'Introductory one-paragraph section at the arbitrary-degeneration part',
 'Merge the introductory paragraph with its part and refer to the standing numbered definition. The Cartier-fibre and Euler conventions are added there. The earlier notation nu:N->S, sigma:T->N denotes exactly the same normalization and resolution that the removed paragraph called nu:T->S, pi:Z->T; the identity renaming sends (old T,old Z,old pi) to (N,T,sigma). Every following component statement already defines its own exact maps. No hypothesis or theorem changes, and the empty section is removed.')
old=r'''two-torus. For an irreducible support $S$, its full fibre is $mS$;
we use the normalization $\nu:N\to S$ and a resolution'''
new=r'''two-torus. A full fibre is the effective Cartier divisor $f^*(b)$;
its reduced support is denoted by $S$. Euler characteristic means
topological Euler characteristic, while $\chi(\mathcal O)$ denotes the
coherent Euler characteristic. For an irreducible support $S$, the
full fibre is $mS$; we use the normalization $\nu:N\to S$ and a resolution'''
apply_edit(old,new,'II-C3-FIBRE-CONVENTIONS-OWNER',['D12','D13','D20'],
 'def:II:standing-torus-fibration','Standing numbered definition',
 'Place the full-fibre and Euler conventions in the single standing definition. The effective Cartier divisor is the pullback of the base point by the same f; the reduced support and its normalization/resolution maps retain their exact meaning.')
add_event('the-degeneration-and-its-normalization-maps;def:II:standing-torus-fibration',
 'II-C3-ROOT-DEGENERATION-PART-TRANSITION','used and rechecked in this run',
 'Root read the complete short old section, the standing definition and the receiving transition/conventions. The global hypotheses point to P204; the Cartier fibre f^*(b), reduced S and Euler convention are transferred verbatim in meaning. Normalization/resolution symbols correspond by the explicit identity renaming (old T,old Z,old pi)=(N,T,sigma); local statements still name their maps. The empty section is removed and its unit rows are migrated, with no progress credit for migration.',
 'Arbitrary-degeneration part introduction and P204',source=__file__)
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
oldrows=[r for r in rows if r['paper']=='II' and r['unit_id']=='the-degeneration-and-its-normalization-maps']
assert len(oldrows)==26,len(oldrows)
rows=[r for r in rows if r not in oldrows]
write_tsv(path,fields,rows)
print('Part transition and numbered conventions integrated; no proof or final-page credit for removed unit.')
