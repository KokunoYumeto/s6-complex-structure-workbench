# Independent referee: E.2.17

Reviewer: boundary_d. 15 November 2026. Full source reviewed:
`sections/E_cusp_normal_crossings.tex`.

**Conclusion: PASS at the stated scope.** The argument establishes the
relative local forms q=z1, q=z1*z2 and q=z1*z2*z3, with the original
specialization parameter unchanged, and therefore a proper smooth
simultaneous normalization. It does not yet identify the entire marked
Mumford neighbourhood.

I independently opened the original Lazzeri scan, not just its metadata:
https://www.numdam.org/item/AST_1973__7-8__269_0.pdf
(tool ref turn499view0). Printed pp.274--275 contain Theorem 2, its
corollary and the strict inequality in the corollary's proof. The final
remark explicitly gives the nonsplitting interpretation for a deformed
isolated hypersurface singularity. The proof uses the strict inequality,
not the weaker statement that a submodule is proper.

## Local arguments checked

- The critical scheme of a reduced isolated plane germ in a holomorphic
  one-parameter deformation is finite over a sufficiently small parameter
  disc. Its two gradient equations form a regular sequence in a regular
  three-dimensional local ring; the finite central fibre makes the base
  parameter a nonzerodivisor. Thus its total critical multiplicity is
  conserved. The actual no-extra-critical-value statement places all
  those critical points over q=0, precisely the extra hypothesis needed
  to apply nonsplitting.

- Off the fixed curve, the nonzero relative holomorphic vector field
  gives a flow box with q independent of its flow coordinate. Reducedness
  makes the transverse plane germ reduced. Every nearby singular point
  there is a node. Conservation and nonsplitting force a single node and
  central Milnor number one; the parameter Morse lemma then gives the
  relative double-crossing form.

- Along the fixed curve, compact-circle averaging preserves the
  specialization coordinate and gives weights (0,+1,-1,0). The invariant
  power series is q=T*g(T,z,s), T=xy. Its linear coefficient in T is a
  section of the dual product of the two normal weight lines, namely
  O(2). It cannot vanish identically on the central fixed curve: this
  would make q divisible by x^2*y^2, contradicting reducedness.

- If the two zeros of that section collided, F0(T,z)=T*g0(T,z) would be
  a reduced isolated plane germ. A repeated nonunit factor remains
  repeated after the substitution T=xy, and T does not divide g0; this
  verifies the reducedness used here. Both nearby triple points give
  distinct critical points of Fs with value zero. Every other critical
  point has value zero as well: at T=0 this is automatic; at T nonzero
  the substitution map (x,y,z)->(xy,z) is a submersion and its lifts lie
  in the actual coordinate neighbourhood after shrinking. Conservation
  plus nonsplitting is therefore a genuine contradiction.

- The two zeros are simple. At a zero, replacing z by g(xy,z,s) is an
  invertible holomorphic coordinate change; away from them g is a unit
  and is absorbed into one normal coordinate. These changes keep s
  fixed. They give precisely the triple- and double-crossing equations.

- Compactness of the actual central cusp allows one common shrinking.
  In each displayed chart normalization separates smooth relative
  branches and commutes with the parameter fibre. Finiteness of analytic
  normalization gives the asserted global properness.

No arbitrary quotient smoothness assertion, Kahler assumption,
separatedness theorem, or meromorphic comparison is used.
