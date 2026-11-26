"""Remove four residual emphasis clauses after complete proof reading."""
from S6_SERIES_PUBLISH_c3_edit import *
import sys

edits=[
 ('lem:II:proper-conductor-pushout',
  'This calculation uses the actual edge maps without an injectivity assumption. ',
  '', ['D02','D08']),
 ('night:P4.21',
  'identifies the boundary fundamental groups through the actual\nblowdown map.',
  'identifies the boundary fundamental groups through the\nblowdown map.', ['D08']),
 ('night:P4.26',
  'The second identifies the boundary groups through the actual blowdown and preserves connectedness.',
  'The second identifies the boundary groups through the blowdown and preserves connectedness.', ['D08']),
 ('night:P4R.11',
  'This also verifies the actual\nnormalization and conductor morphisms locally.',
  'This also verifies the\nnormalization and conductor morphisms locally.', ['D08']),
]
if '--record' in sys.argv:
    add_event(';'.join(x[0] for x in edits),'II-C3-RESIDUAL-WORDING-COMPLETE-READ',
        'used and rechecked in this run',
        'Root read every complete original statement and proof of P294, P4.21, P4.26 and P4R.11, then every complete receiving proof. '
        'The double-mapping-cylinder proof already displays both induced maps j_a,* and k_a,* and the full van Kampen presentation; '
        'its extra defensive sentence is removed. Three remaining emphasis words are removed from the same blowdown and local '
        'normalization/conductor morphisms. All hypotheses, constructions, formulas and their exact maps are unchanged. '
        'The newly found wording instances are resolved; existing local rows are not counted again as movement. '
        'No independent derivation, required-check or final-page credit.',
        'P294 conductor pushout; P4.21 rational Euler; P4.26 irreducible Euler; P4R.11 tacnodal equality',
        source='code/S6_SERIES_PUBLISH_c3_residual_wording.py')
    print('Four complete receiving-proof comparisons recorded.')
else:
    for n,(label,old,new,kinds) in enumerate(edits,1):
        apply_edit(old,new,f'DII-C3-RESIDUAL-WORDING-{n:02}',kinds,label,
            'Current fully reviewed body unit',
            'Remove editorial emphasis and the repeated defensive scope sentence; '
            'the exact displayed induced homomorphisms, blowdowns and normalization/conductor maps are unchanged.',
            review='Complete original statement/proof read; the complete receiving proof is printed by this program for root rereading and recorded by its --record mode.')
    text=SOURCE.read_text()
    for label,_,_,_ in edits:
        p=text.index(r'\label{'+label+'}')
        a=text.index(r'\begin{proof}',p)
        b=text.index(r'\end{proof}',a)+len(r'\end{proof}')
        print('COMPLETE RECEIVING PROOF',label)
        print(text[a:b])
