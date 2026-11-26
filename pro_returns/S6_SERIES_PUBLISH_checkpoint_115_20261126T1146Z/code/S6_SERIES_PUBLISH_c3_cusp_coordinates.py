from S6_SERIES_PUBLISH_c3_edit import *

apply_edit('Let $p$ lie on a reduced fibre support in the standing torus-fibration setting of \\cref{sec:II:night-sign}.',
    'Let $p$ lie on a reduced fibre support in the setting of \\cref{def:II:standing-torus-fibration}.',
    'II-C3-CUSP-SETTING',['D06'],'night:P4.28','Local rigidity of a transverse cusp, statement',
    'Resolve the existing standing hypotheses at their numbered definition, with exactly the same fibration and normalization maps.')
apply_edit(r"""Proposition~\ref{night:P4.16}, with $n=3$, gives a
compact spherical class of square $-6$ in its
affine nearby fibre.""",
    r"""The coordinates $(x,y,z)=(X,y,-Z)$ identify this
function with $x^2-zy^3$. Proposition~\ref{night:P4.16},
with $a=2$ and $n=3$, gives a compact spherical class
of square $-6$ in its affine nearby fibre.""",
    'II-C3-CUSP-LATTICE-MAP',['D22'],'night:P4.28',
    'Local rigidity of a transverse cusp, item4',
    'Write the exact invertible sign map and both parameters of the common lattice calculation. Positive weights (2,1,1), degree4, are unchanged and scale the same polynomial; the boundary transport remains complete.')
apply_edit(r"""After a sign change and permutation,
\cref{night:P4.18}, with exponents $(3,2,1)$, gives
the compact spherical class of nonzero square.""",
    r"""The coordinates
$(x',y',z')=(\widehat Y,\widehat x,-\widehat Z)$
write this function as $(x')^3-(y')^2z'$.
Thus \cref{night:P4.18}, with exponents $(3,2,1)$, gives
the compact spherical class of nonzero square.""",
    'II-C3-CUSP-BINOMIAL-MAP',['D22'],'night:P4.28',
    'Local rigidity of a transverse cusp, item6',
    'Spell out the existing sign change and permutation as the exact linear coordinate isomorphism. The exponents, unit-removal equality and nonzero intersection are unchanged.')
apply_edit('\\item For clarity, the two transports use nested balls.',
    '\\item The two transports use nested balls.',
    'II-C3-CUSP-TRANSPORT-PROSE',['D08'],'night:P4.28',
    'Local rigidity of a transverse cusp, item7',
    'Retain the entire two-ball transport argument, including each inclusion and orientation-preserving parameter map.')
apply_edit(r"""All these maps preserve the
compact intersection calculation. No extension of
the second perturbation outside $B_2$ is needed.
The unit has been retained in that perturbation
and removed at its binomial point by the explicit
degree-three coordinate map in item~6.""",
    r"""All these maps preserve the compact intersection calculation.""",
    'II-C3-CUSP-TRANSPORT-RECAP',['D02','D08','D11'],'night:P4.28',
    'Local rigidity of a transverse cusp, item7',
    'The preceding full nested-ball construction already gives the exact domains and maps. The unit and its removal are explicitly present in item6. Remove only the defensive domain sentence and duplicated closing recap.')
print('The full original cusp proof was read; exact coordinate applications and process removals recorded.')
