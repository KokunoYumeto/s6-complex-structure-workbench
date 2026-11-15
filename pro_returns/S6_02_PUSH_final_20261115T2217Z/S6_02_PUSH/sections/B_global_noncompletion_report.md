# B.4.33: the unrestricted proper-filling contradiction

## Review and integration state

The complete proof in `B_global_noncompletion.tex` has passed root, boundary_d, and limits_ab full-source review. Root requested an explicit uniform local-root paragraph and a precise treatment of sigma under modifications; both were inserted before registration. The result is Proved, with its own CSV, and is input immediately after B.4.32. The author's adversarial audit is retained separately from the independent referee notes.

## Exact conclusion

No proper Hausdorff complex-analytic filling of the actual punctured six-sphere family exists after any finite parameter cover. This includes arbitrary singular central spaces and vertical three-dimensional fibres of the marked two-parameter map. Consequently no positive exponent N can provide the smooth, reduced normal-crossings filling requested in Part B. The assertion is stronger than B.4.30, which only excludes completing the particular B.4.19 axial models.

## Proof structure and the previously missing affine comparison

The revised B.4.4 extends the marked fibration after resolving the main component of any putative proper filling. Its proof needs smoothness of the dominating fourfold, not a reduced central divisor. B.4.31 is also valid with central multiplicities. The only semistable constructions are local one-parameter surface reductions near generic boundary divisors, retaining a transverse parameter.

After shrinking the cusp bidisc, excess fibre dimension can occur only at its origin: a three-dimensional fibre must contain a central divisor component mapped to a constant marked base value, and there are finitely many such components. B.4.30's direct coefficient-ideal construction then makes the marked map equidimensional after point blowups of that origin. A finite cover of K=the inverse image of the origin supplies finite local multisections. This covers the whole modified small bidisc after shrinking, including the case of no blowup, when K is a point.

Multiply the local traces to one common degree D. Their differences extend to the exact associated-log-torus sheaf on every boundary divisor: full-rank monodromy treats exceptional divisors and the actual q axis, while B.4.31 forces every angular residue on the unknown strict r axis to lie in the delta line. Thus the first character remains a unit and the second is a boundary monomial times a unit, exactly as required by the bounded character sheaf. Norms give a common multiplier; Hartogs for logarithmic sections fills isolated crossings. These differences glue a torsor Q on all of the modified base S. They do not assert that the cap itself is a log-group model.

B.4.27 gives H1(S,A)=0, so Q has a global origin h whose ordinary restriction is a section of the actual D-fold torsor. B.4.32 says h relative to the B.4.19 ordinary origin has zero radial class in Lambda_Q/Q delta. The actual ordinary-to-rotating comparison is G(s)+6v delta; its radial class is also zero in that quotient. Therefore h relative to the rotating origin has zero gamma-loop coefficient. This is only a loop statement: a common essential translation is still allowed.

On the actual q-axis model, sigma is a genuine extending origin, so h−D sigma is a section of the specified log torus on the whole q-axis region. The injective q-ghost period map diag(12m,12m) makes its gamma-loop coefficient zero as well. However, sigma minus the rotating origin is exactly the audited clutching section F, whose positive r-root loop has gamma coefficient n. Subtracting the two expressions for h therefore gives 0=D n, impossible for positive D and n.

## What this argument does not assume

It does not identify an unknown r-axis completion with the B.4.19 rotating model. It does not infer boundedness of a single translated origin from relative forms or Gauss–Manin data. It does not infer Hartogs extension for torsors; only sections are extended, after the actual trace differences have been obtained. It does not invoke a projective or Kähler semistable-reduction theorem for threefolds. The earlier essential-translation counterexample B.4.29 remains valid and is explicitly accommodated.

## Source and verification provenance

The final proof combines the already opened primary inputs recorded in B.4.24, B.4.27, and B.4.30, including analytic logarithmic Riemann–Hilbert comparison, the coefficient-ideal equidimensionalization argument, analytic resolution, and compatible toroidal subdivisions. No new general completion theorem is claimed. Exact period differences and the complete gauge cancellation are audited in `code/e_push_completion_diagnostics.py`; root-transfer and global fixed spaces are audited independently in `code/d_push_global_loop_defect.py` and `code/ab_push_global_meridians.py`. These computations verify identities, not the geometric nonexistence argument.

The finite trace normalization, strict-r residue comparison, global loop invariant, and final affine comparison have each received an independent agent referee. Those reviews are independent checks of one proof, not separate proofs or new published literature. Full downloaded articles remain outside the deliverable tree.

## Uniformity and comparison checks

A finite cover of the compact inverse image of the origin supplies finitely many local finite covers and trace degrees. Embedded resolution over a relatively compact neighbourhood supplies finitely many boundary multiplicities. One product of the multiplicity common multiple with lcm(1,...,d_max) therefore bounds the local transverse roots and norms at every generic boundary point. No global root along an entire boundary curve is claimed or needed; local norm extensions glue by uniqueness. Nonboundary branch curves and section-lift indeterminacy add only isolated points near that compact set, where Hartogs applies. Sigma can be compared directly through projection to its prescribed fan model and the explicit finite-character norm, without a global holomorphic lift through an arbitrary modification.

The untwisted Engel family is not contradicted. Its identity closing has both extending fan origins equal to zero and therefore has zero clutching section F. The actual twisted closing has the nonzero gamma loop calculated in B.4.24. The linear monodromy and zero fixed-space calculation alone do not distinguish these cases; the exact affine closing does.

## Literature status

No matching theorem excluding arbitrary proper analytic fillings was found in the sources checked for this task. The cited analytic logarithmic comparison, toroidal modification, and equidimensionalization results supply specific inputs; they are not cited as an existing general noncompletion theorem. This is a derivation for the actual family from its audited periods and affine transitions. No priority or novelty claim is made.
