from S6_SERIES_PUBLISH_c3_edit import *

text=SOURCE.read_text()
a=text.index('For a local defining function $ug^m$',text.index('\\label{night:P4.16}'))
b=text.index('\\item We specify the normalization morphism.',a)
old=text[a:b]
new=r"""For the germ-exclusion assertion, apply \cref{cdp:st:A.5.15}
with exponent triple $(a,b,c)=(a,n,1)$. The coordinate map
is the identity on $(x,y,z)$, and its full defining function
$u(x^a-y^bz^c)^m$ is exactly $u(x^a-zy^n)^m$.
The proper holomorphic map, smooth total threefold, torus
nearby fibres and arbitrary positive multiplicity are the
same hypotheses. This gives the asserted exclusion.

"""
apply_edit(old,new,'II-C3-LATTICE-BINOMIAL-APPLICATION',['D12'],
    'night:P4.16; night:P4.17','Spherical intersection lattices, item4',
    'The earlier A.5.15/P4.18 is the complete general binomial obstruction owner. Its identity-coordinate specialization (a,b,c)=(a,n,1) gives precisely this germ and full multiplicity. Retain the stronger complete integral lattice computation, all compact representatives and the weighted scaling; remove only the duplicated unit-removal and torus-obstruction proof. The earlier proof has no input from either receiving lattice label.',
    'Root read A.5.15 statement; conductor agent reread its complete proof and verified its only later reference was a concluding finite-rank scope comparison, removed in the normalization fragment. Both complete lattice originals and receiving proof were read.')
add_event('night:P4.16','II-C3-ROOT-LATTICE-BINOMIAL-APPLICATION',
    'used and rechecked in this run',
    'Compared the exact identity-coordinate specialization of A.5.15, with b=n,c=1, to the full germ and hypotheses of the receiving lattice statement. The complete lattice, compactification, kernel and scaling calculation is unchanged. The duplicate obstruction proof is now one exact source application; no independent check.',
    'S6_SERIES_PUBLISH_II.tex; code/S6_SERIES_PUBLISH_c3_binomial_application.py',
    source='code/S6_SERIES_PUBLISH_c3_binomial_application.py')
print('The general binomial obstruction has one proof; the stronger exact lattice computation remains complete.')
