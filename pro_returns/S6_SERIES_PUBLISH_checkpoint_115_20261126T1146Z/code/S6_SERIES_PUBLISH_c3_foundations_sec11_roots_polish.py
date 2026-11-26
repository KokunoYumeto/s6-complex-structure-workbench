# Final map-preserving prose adjustments, after TeX normalization.
polish = {
'p342': [
 ('with specified height-one subdivisions and inverse coarsening maps.','with height-one subdivisions and their coarsening morphisms.'),
 ('tangent-dependent transition units;\nthe maps use those same holomorphic transition units.','tangent-dependent holomorphic transition units.'),
 ('For the embedded assertion\nretain every old component and stratum\nlabel as well as each subdivision ray.','The atlas includes every original component and stratum\nlabel together with each subdivision ray.'),
 ('star charts glue without a global\nself-incidence.','star charts glue as embedded global components.'),
 ('trivialization supplied by $f$.','trivialization defined by $f$.'),
 ('A compact cyclic base cover with the specified local root.','A compact cyclic cover with the given local root.'),
 ('and the retained local root model;','and the local root model $t=\\sigma^N$;')
],
'new76': [
 ('retained coarse-cone quotient','coarse-cone quotient'),
 ('the retained periodic coarse triangles','the periodic coarse triangles of the marking'),
 ('with their specified smooth','with their smooth'),
 ('The old-cone contractions and finite invariant-ring maps are retained\nat both ends,','The old-cone contractions and finite invariant-ring maps are\npart of the marking at both ends,'),
 ('a specified integral','the corresponding integral'),
 ('for a retained }','for }'),
 ('with the\nnonzero units retained.','with the same nonzero unit factors.'),
 ('The period equations retaining the finite action.','The period equations and finite action.'),
 ('We retain the names\n\\(\\Lambda\\subset\\Lambda_0\\), \\(B,D,d,a_0\\) for these\nimages.','Denote these images by\n\\(\\Lambda\\subset\\Lambda_0\\), \\(B,D,d,a_0\\).'),
 ('of a retained coarse central chart','of an original coarse central chart'),
 ('This property is retained by the exact central log\ncomparison.','The central log isomorphism identifies these same inertia maps.'),
 ('monoid chart, retained in','monoid chart in'),
 ('Compactness and the precise retained scope.','Compact gluing.')
],
'new78': [
 ('Retain the full record','Use the full record'),
 ('with these retained regularization,','with these regularization,'),
 ('with a specified inverse','with an inverse'),
 ('the retained $\\phi$-record.','the $\\phi$-record.'),
 ('its specified analytic\nneighbourhood. This retains all transverse terms in that input.','its analytic neighbourhood, including every transverse term\nin the input.')
],
'p341': [
 ('including their transverse terms, are retained.','including their transverse terms, belong to the datum.'),
 ('by the specified\ninverse record','by the given\ninverse record'),
 ('and finite action are retained.','and finite action belong to the datum.'),
 ('can equivalently be supplied by its','can equivalently be given by its'),
 ('central charts are supplied globally;','central charts are given globally;')
],
'new86': [
 ('recovers the supplied\nfamily exactly.','recovers the given\nfamily exactly.'),
 ('of the retained sigma record.','of the sigma record.'),
 ('Reversing a retained record recovers every\nspecified normal extension and every transverse jet.','Reversing the record recovers its normal extensions and\nall transverse jets.'),
 ('maps retain the original units','maps use the original units'),
 ('\\(Z\\), and retain its comparison','\\(Z\\), with comparison'),
 ('Applying the retained\nequivariant coarsening','Applying the\nequivariant coarsening'),
 ('The converse from the specified finite input.','The converse construction.'),
 ('specified smooth proper \\(Z\\)','smooth proper \\(Z\\) of the datum'),
 ('proper core and retained proper maps;','proper core and its proper maps;'),
 ('the supplied maps and their checks.','the maps and coordinate identities in the definition.'),
 ('The Euler changes of the specified maps.','The Euler changes of the construction maps.'),
 ('using their specified identity maps','using their identity maps'),
 ('globally supplied compact admissible','global compact admissible')
]
}
for name, changes in polish.items():
    owner={'p342':'prop:II:cyclic-root-normalization','new76':'cdp:st:C.2.UN.76','new78':'cdp:st:C.2.UN.78','p341':'def:II:finite-rooted-reconstruction','new86':'cdp:st:C.2.UN.86'}[name]
    val=locals()[name]
    for old,new in changes:
        val=pkg.edit(val,old,new,'D08',owner,'Use the named analytic maps and data directly; all component labels, multiplicities, arrows, units and gluing information remain.')
    locals()[name]=val

