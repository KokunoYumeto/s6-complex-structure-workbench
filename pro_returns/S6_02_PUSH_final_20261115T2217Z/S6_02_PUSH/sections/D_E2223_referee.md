# Independent referee: E.2.23 arbitrary deformation bases

Reviewer: boundary_d. 15 November 2026.
Full source read: `sections/E_arbitrary_deformation_bases.tex`.
Inputs E.2.22 and its source have been independently checked in
`D_E2222_referee.md`; E.1.2--E.1.3 were reread for the converse.

**PASS.** This is a valid consequence of the proved disc-propagation
statement, including for singular, reducible parameter spaces and
finite deformation chains.

On a connected Riemann surface, a nonempty known-pair locus is open
by local miniversality. A coordinate disc around any closure point
meets that locus in a nonempty open subset. E.2.22 applies directly,
so the locus is closed and hence is the whole Riemann surface.
The pulled-back proper smooth family has sphere topology throughout
by Ehresmann transport from a known fibre.

For a point b in the closure in an arbitrary reduced base, one of the
finitely many irreducible local branches T meets the known locus
arbitrarily near b. The finite local projection may be chosen with
rho^(-1)(0)={b}. For a known point a near b, the inverse image of the
complex line through rho(a) and zero has dimension exactly one:
the d-1 equations give the lower bound and finiteness gives the upper
bound. Any irreducible component C through a is closed and proper
over the connected line disc. Its one-dimensional analytic image is
therefore the whole line disc. It contains the unique point b over
zero. This is the decisive argument: it does not assume that an
arbitrary open known locus contains a punctured analytic curve
approaching b.

The normalization of C is a connected Riemann surface and has points
over both a and b. Smoothness and properness of the original family
survive its base change. Its known locus contains a nonempty open
neighbourhood over a, so the preceding Riemann-surface argument gives
the fibre over b. Thus the original known locus is closed. Connectedness
of the parameter base proves the first assertion. Passing to a
nonreduced base's reduction changes no fibre isomorphism class and
preserves smoothness, as claimed.

Every link of a finite deformation chain now preserves the ordered
pair. Conversely, the explicit E.1.2 congruences and E.1.3 family
comparisons put all sphere data with a fixed pair in the same connected
admissible period family, whose period subgroup is 2kl Z. This supplies
the converse without treating all discrete logarithmic data as equal
before applying the classification.

Source audit: the author's Demailly manuscript was independently
opened at
`https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf`.
Chapter II Theorem 4.19, printed pp. 95--96, supplies finite local
parametrization. Definition 7.9 and Theorem 7.12, pp. 114--115, supply
finite normalization; Corollary 7.7, p. 113, states the normal-curve
regularity used here. Retrieval records include turn515view0,
turn516view2 and turn517view0. The source's cited Theorem 7.6 also
implies that corollary.
