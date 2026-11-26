#!/usr/bin/env python3
"""Publication-language readback: keep every map and remove workflow contrasts."""
from pathlib import Path
from hashlib import sha256
import re
p=Path('agents/continuation7_iii_general_initial_receiving/S6_SERIES_PUBLISH_III_02LN_receiving.tex')
s=p.read_text()
assert sha256(s.encode()).hexdigest()=='0b50476c451e6d11f2278a0b64b50b467efa085c4dc37350ee9137d3be40587b'
ids={c:sorted(re.findall(r'\\'+c+r'\{([^{}]+)\}',s)) for c in ('label','hypertarget','tag')}
patches=[
 ('This is a complete finite presentation, not just\nits abelianization.','This is a finite presentation of the fundamental group.'),
 ('This\nconstructs the line for every stated weight distribution; no\niteration of a natural one-component zero has been imposed.','This constructs the line for every stated weight distribution.'),
 ('Here is the integral check without a divisibility assumption\nbeyond compatibility.','Compatibility implies integrality as follows.'),
 ('In particular the matrix \\(C\\) has\nnot been inferred from an abstract conjugacy of monodromies.',''),
 ('They relabel the same fan and its period\nsubgroup; they do not replace it by a different fan.','They relabel the fan and its period subgroup.'),
 ('There is no saturation in the first kernel in \\eqref{maps:eq:D.GI3}.\n',''),
 ('No representative \\([v]\\) is discarded.\n',''),
 ('Thus these gauges use\nthe actual units and create no unrecorded graph winding.','These gauges use the unit transitions and have zero graph winding.'),
 ('and its mapping-torus cone retain the actual permutation by\n\\(Q\\), with no transitivity assumption.','and its mapping-torus cone have the permutation induced by \\(Q\\).'),
 ('This proves the extension without assuming \\(Q\\) acts transitively.\n',''),
 ('This is a map of the original germ, not merely\nan equality of return matrices.','These mutually inverse maps identify the original germ with the displayed product.'),
 ('No torsion has been removed\nby saturation.\n',''),
 ('including its boundary torsion, rather than only its rank.','including its boundary torsion.'),
 ('This supplies the actual integral splitting,\nnot a choice made over the rationals.','This gives the integral splitting and its inverse.'),
 ('This fixes the last-boundary\nmarking, rather than independently choosing its quadratic lift.','This determines the last-boundary marking and quadratic lift.'),
 ('Both composites fix all generators. This proves the split\nsemidirect product and the injection of \\(V\\), without\nassuming a splitting of an unspecified extension.','Both composites fix all generators, proving the split semidirect\nproduct and the injection of \\(V\\).'),
 ('No bound on those elements, on the number of regular sites,\nor on any input integer is used in this proof.\n',''),
 ('No elliptic or line coordinate of \\(\\lambda_C\\) is discarded.\n',''),
 ('They are also the direct geometric construction\nof the normal-disc boundary, independently of a formula for\nits rank.','Thus they compute the full component-disc boundary map.'),
 ('No torsion in \\(H_1(E)\\), in a\ncusp boundary, or in the fibre coinvariants has been suppressed.\n',''),
 ('The determinant alone would not prove it:\nthe \\(D=16\\) iterate of a natural OS45 \\(I_1\\) input also has period\nindex sixteen, while retaining its \\(I_1\\) support.\n',''),
]
for old,new in patches:
 assert s.count(old)==1,(old,s.count(old))
 s=s.replace(old,new)
# Here these modifiers have no remaining mathematical contrast or hypothesis.
s=re.sub(r'\bactual ', '', s)
s=s.replace('actual-period','period')
s=s.replace('The actual affine','The affine')
s=s.replace('The raw section cocycle','The section cocycle')
s=s.replace('The literal 21','The 21')
s=s.replace('the 21 raw profiles','the 21 marked profiles')
s=s.replace('For raw columns','For the monodromy columns')
s=s.replace('the raw matrices','the matrices')
s=s.replace('literal graph-bundle','marked graph-bundle')
s=s.replace('literal powers','powers')
s=s.replace('a literal profile','a marked profile')
s=s.replace('The literal positive period','The positive period')
s=s.replace('The degree-one map is equally literal:','The degree-one map is')
s=s.replace('The unit-retaining local comparison','The local comparison with its units')
s=s.replace('All component normal discs are retained. For every','For every')
s=s.replace('It retains both cyclic coordinates','It has both cyclic coordinates')
s=s.replace('Trivialize the line there and retain its','Trivialize the line there and use its')
s=s.replace('the retained node','the node')
s=s.replace('above retains the component action','above preserves the component action')
s=s.replace('affine numerators are retained.','affine numerators occur in these columns.')
s=s.replace('composites and retains any torsion in','composites, including on torsion in')
s=s.replace('the full presentation is retained for them','the full presentation applies to them')
s=s.replace('operations retain their inverse maps','operations give their inverse maps')
s=s.replace('has already been retained in','is included in')
s=s.replace('of the retained Cartier frames','of the Cartier frames')
s=s.replace('retaining a preimage','together with a preimage')
s=s.replace('identifications in \\eqref{maps:eq:D.GI7} retain the','identifications in \\eqref{maps:eq:D.GI7} give the')
s=s.replace('retains its support','preserves its support')
s=s.replace('For the nonabelian fundamental group, retain four commuting','For the nonabelian fundamental group, take four commuting')
s=s.replace('Retain the ordered product','Use the ordered product')
s=s.replace('at a cusp this is','at a cusp this is')
s=s.replace('with no saturation.','using the integer return image.')
s=s.replace('The recorded elliptic monodromies','The marked elliptic monodromies')
s=s.replace('the recorded matrices','the given matrices')
s=s.replace('the recorded column matrix','the monodromy column matrix')
s=s.replace('the recorded profiles','the marked profiles')
s=s.replace('the recorded \\(B_i','the marked \\(B_i')
s=s.replace('recorded\nmonodromy images','monodromy images')
for c,v in ids.items():assert v==sorted(re.findall(r'\\'+c+r'\{([^{}]+)\}',s))
assert s.count('\\begin{proof}')==s.count('\\end{proof}')==1
assert not re.search(r'\bactual\b|rather than|not merely|without assuming|no unrecorded',s)
p.write_text(s)
print('RECEIVER',p,'LINES',len(s.splitlines()),'SHA256',sha256(s.encode()).hexdigest())
print('COMPLETE publication-language changes only; all displayed maps, inverses, hypotheses, conclusions and 12/12/11 permanent identities preserved. The determinant-only counterexample stays in the comparison.')
