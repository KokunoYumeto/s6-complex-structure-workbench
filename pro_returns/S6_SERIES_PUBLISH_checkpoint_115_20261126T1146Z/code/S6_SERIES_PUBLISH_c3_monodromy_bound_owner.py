"""Use the earlier monodromy bound through its exact root and duality maps."""
from S6_SERIES_PUBLISH_c3_edit import *

text=SOURCE.read_text()
start=text.index(r'\subsection{Integral component lattices and monodromy}')
end=text.index(r'\subsection{Rank-four monodromy stratum signatures}',start)
old=text[start:end]
new=old
new=new.replace(
    r'\cref{lem:II:compact-component-transport,cdp:st:C.2.UN.33,cdp:st:C.2.UN.11}',
    r'\cref{lem:II:compact-component-transport,cdp:st:C.2.UN.33,night:P4.13}')
old_statement=r'''\Cref{cdp:st:C.2.UN.11} gives
$(U_1-I)^2=0$. In an oriented real basis of'''
new_statement=r'''The monodromy bound \eqref{cdp:eq:C.MS.10} of
\cref{night:P4.13}, transported through the chosen base change
and the natural cohomology--homology pairing, gives
$(U_1-I)^2=0$. In an oriented real basis of'''
assert new.count(old_statement)==1
new=new.replace(old_statement,new_statement,1)
old_proof=r'''\item It remains to compute the exact
monodromy bound. \ref{cdp:st:C.2.UN.11} proves
that $N_0=U_1-I$ has square zero
and rank at most two. In rank one,'''
new_proof=r'''\item Apply \cref{night:P4.13} to this same degeneration.
Let $T$ be its monodromy on $H^1(F,\Q)$ and $M$ its
semisimple order. The chosen root has $M\mid N$.
Writing $D=T^M-I$, equation \eqref{cdp:eq:C.MS.10} gives
$D^2=0$, so the cohomology monodromy after the root is
$T^N=I+(N/M)D$. The flat perfect pairing with
$H_1(F,\Q)$ identifies $(T^N)^{-1}$ with the dual of
$U_1$. Since $(T^N)^{-1}=I-(N/M)D$, it follows that
$N_0=U_1-I$ has square zero. Its image lies in its kernel
on a four-dimensional space, so its rank is at most two.
In rank one,'''
assert new.count(old_proof)==1
new=new.replace(old_proof,new_proof,1)
assert 'cdp:st:C.2.UN.11' not in new
assert identifiers(old)==identifiers(new)
apply_edit(old,new,'DII-C3-MONODROMY-SQUARE-ZERO-OWNER',['D04','D14','D22'],
    'cdp:st:C.2.UN.36','Integral component lattices and monodromy',
    'The square-zero monodromy assertion is already proved at P4.13/C.MS.10. UN11 contains the later signature table, '
    'so its inherited citation is replaced by the exact earlier owner. The root map gives T^N=I+(N/M)(T^M-I); '
    'the flat perfect cohomology--homology pairing identifies the inverse with U1 dual. '
    'Thus the original U1 square-zero and rank conclusions have their explicit map, and the complete invariant-lattice '
    'and oriented-form proof is unchanged elsewhere. No mathematical conclusion changes.',
    review='Root read the complete current original UN36 statement and proof, the exact P4.13 statement and full bound derivation, '
           'and the full receiving UN36 proof. This is an exposed owner/application repair, not an independent proof.')
add_event('cdp:st:C.2.UN.36','II-C3-MONODROMY-SQUARE-ZERO-OWNER',
    'used and rechecked in this run',
    'The full UN36 original and receiving proofs were read. The cited square-zero bound stands in the earlier P4.13/C.MS.10, '
    'not in the later UN11 signature-table proof. The corrected application gives the exact root power and inverse-dual '
    'cohomology/homology identification; image-contained-in-kernel gives the unchanged rank bound. '
    'The compact transfer, multiplicity-weighted pairing, signatures and all equations retain their original proofs. '
    'This resolves the apparent later-owner dependency without moving or altering UN11. No theorem is refuted, '
    'no new result is asserted and no independent-check, required-check or final-page credit is claimed.',
    'UN36 complete statement/proof; P4.13/C.MS.10 and its nearby-cycle filtration derivation',
    source='code/S6_SERIES_PUBLISH_c3_monodromy_bound_owner.py')
print('UN36 uses the earlier bound with the exact base power and perfect pairing.')
