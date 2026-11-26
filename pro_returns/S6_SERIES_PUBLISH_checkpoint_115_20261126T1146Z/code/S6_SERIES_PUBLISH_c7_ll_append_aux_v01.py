#!/usr/bin/env python3
"""Append the fully checked generic framing auxiliaries to LL's receiver.

This retains their permanent anchors and adds the exact normalization
and kernel-generation arguments proved in the post-exposure note.
No canonical source or frozen fresh file is modified.
"""
from pathlib import Path
from hashlib import sha256

lane=Path('agents/continuation7_iii_residual_two_primary')
old=(lane/'S6_SERIES_PUBLISH_III_02LL_released_proof.tex').read_text()
start=old.index(r'\item \emph{A framing parity')
end=old.index(r'\item \emph{The integral linking calculation.}')
part=old[start:end]
part=part.replace('$a$','$\\mathfrak a$')
part=part.replace(r'\langle a,[T]\rangle',r'\langle\mathfrak a,[T]\rangle')
part=part.replace(
    'The homomorphism\n$\\pi_3SO(3)\\to\\pi_3SO(6)$ has image $2\\mathbb Z$.',
    r'''The homomorphism
$\pi_3SO(3)\to\pi_3SO(6)$ has image $2\mathbb Z$.
Indeed, under the double cover $SU(2)\to SO(3)$ the adjoint
bundle of a rank-two complex bundle $E$ has $p_1=-4c_2(E)$,
whereas its underlying real rank-four bundle has $p_1=-2c_2(E)$
and represents the stable generator. This proves the factor two;
the quotient map to $\pi_3V_{6,3}$ is reduction modulo two.''')
part=part.replace(
    'chart $f=xyz$ it has basis\n$x\\partial_x-y\\partial_y,y\\partial_y-z\\partial_z$.',
    r'''chart $f=xyz$ it has basis
$x\partial_x-y\partial_y,y\partial_y-z\partial_z$.
For the first assertion, a relation among $(y,x,0)$ forces the
first two coefficients to be divisible by $x,y$, with opposite
quotients. For the second, a relation among $(yz,xz,xy)$ forces
the coefficients to be divisible by $x,y,z$, and their quotients
sum to zero. These arguments prove generation of the kernels,
including at the critical strata.''')
receiver=lane/'S6_SERIES_PUBLISH_III_02LL_receiving.tex'
current=receiver.read_text()
assert r'\label{maps:eq:D44.2}' not in current
receiver.write_text(current+part)
print('APPENDED_FULL_CHECKED_AUXILIARIES',len(part.splitlines()),'lines')
print('RECEIVER_INTERMEDIATE_SHA256',sha256(receiver.read_bytes()).hexdigest())
