# Current standalone B status reconciliation

**Date:** 15 November 2026. **Authorization:** root, after full acceptance of B.4.33.

Only current standalone B TeX/CSV files were updated. Master AB files, the new B.4.33 files, all historical reports and all referee records were left untouched. No numbered status value or local theorem scope changed. Complete originals are retained in `evidence/ab_push_final_status_before`; the structured before/after ledger is `evidence/ab_push_final_status_audit.json`.

The corrections replace stale global-open wording with precise B.4.30/B.4.33 forward references. Independent auxiliary deformation/classification questions remain explicitly outside the proved local lemmas. The B.4.4 registry now states its proved scope for a resolved main component of any proper analytic filling, with no central reducedness assumption.

**Changed files:** 33. **Recorded changed passages/cells:** 46.

## sections/B_hodge_obstruction.tex

**Previous passage**

```text
The existence and least base-change exponent in B.4.1 therefore
remain open in the unrestricted analytic category.
```

**Current passage**

```text
These Hodge arguments alone give conditional restrictions, not
unrestricted nonexistence. The latter is proved in B.4.33 for
every finite parameter cover, using the actual affine clutching.
```

## sections/B_analytic_comparison_audit.tex

**Previous passage**

```text
\paragraph{The remaining analytic comparison.}
```

**Current passage**

```text
\paragraph{Why automatic analytic comparison is not used.}
```

## sections/B_analytic_comparison_audit.tex

**Previous passage**

```text
that every proper analytic filling is one of these models. We have
not constructed that global log input with the required finite-place
and cusp markings for the six-sphere family.
```

**Current passage**

```text
that every proper analytic filling is one of these models.
B.4.24 constructs the actual local Jacobian log input and isolates
its affine torsor obstruction. B.4.33 derives an associated torsor
from traces in a hypothetical cap; it does not identify that cap
with a proper fan model.
```

## sections/B_analytic_comparison_audit.tex

**Previous passage**

```text
unrestricted proof still needs a specific extension or boundedness
argument for the comparison, or an actual non-toroidal cusp
construction with the prescribed punctured restriction.
```

**Current passage**

```text
unrestricted proof needs additional information beyond a
punctured isomorphism. B.4.30--B.4.33 supply exactly such information:
bounded differences of extending sections and a global radial-loop
invariant. Their contradiction proves nonexistence without extending
an individual punctured isomorphism meromorphically.
```

## sections/B_comparison_literature.tex

**Previous passage**

```text
failure directly. None of these comparisons closes B.4.
```

**Current passage**

```text
failure directly. None of these automatic-comparison results
proves the conclusion of B.4.33, whose argument instead uses
extending-section differences and the global affine loop invariant.
```

## sections/ab_push_parabolic_insertion.tex

**Previous passage**

```text
\begin{remark}[The third component and the actual cusp remain open]
```

**Current passage**

```text
\begin{remark}[Auxiliary normal matching and the actual filling obstruction]
```

## sections/ab_push_parabolic_insertion.tex

**Previous passage**

```text
If such a smoothing exists, its topological Euler number is
$4+8-2\chi(E)=12$ and its holomorphic Euler number is one.
These necessary data do not supply a compact third threefold or
prove the existence of that smoothing.
```

**Current passage**

```text
The surface smoothing is constructed in B.4.11--B.4.12.
Its topological Euler number is $4+8-2\chi(E)=12$ and its
holomorphic Euler number is one. Its total space over an open
disc is not a compact third threefold, so that construction
does not supply a compact threefold assembly.
```

## sections/ab_push_parabolic_insertion.tex

**Previous passage**

```text
Thus B.4.1 and B.5.1 remain open after this auxiliary construction.
```

**Current passage**

```text
These auxiliary matching statements do not produce a filling
of the actual family. B.4.33 proves that no such proper analytic
filling exists after any finite parameter cover.
```

## sections/ab_push_hopf_cap.tex

**Previous passage**

```text
\begin{remark}[Relation to the primary literature and to the remaining cusp]
```

**Current passage**

```text
\begin{remark}[Primary literature and the scope of the auxiliary cap]
```

## sections/ab_push_hopf_cap.tex

**Previous passage**

```text
component rotations.  These comparisons remain open.
```

**Current passage**

```text
component rotations. The construction here establishes none of
those additional comparisons. B.4.33 separately rules out a proper
analytic filling of the actual global family, without denying the
auxiliary Hopf degeneration constructed above.
```

## sections/ab_push_corrected_cusp_overlap.tex

**Previous passage**

```text
The next local construction must complete this
proper family over the single missing base point.
```

**Current passage**

```text
This construction fills the punctured bidisc, not its
origin. B.4.30 proves that its prescribed partial family
has no proper analytic completion at that point.
```

## sections/ab_push_corrected_cusp_overlap.tex

**Previous passage**

```text
comparison over $q$ between them. A successful
origin cap must retain the actual two-open
comparison just constructed and prove its own
analytic extension and properness.
```

**Current passage**

```text
comparison over $q$ between them. B.4.33 further
excludes every proper filling of the actual global family,
even if its other central axial model is changed. Thus
the missing origin is not left as a construction claim.
```

## sections/ab_push_global_partial.tex

**Previous passage**

```text
is $(\infty,0)$; no proper completion over it, and no
proper filling over the whole $r$ disc, is asserted.
```

**Current passage**

```text
is $(\infty,0)$. This proposition constructs only the
partial family: B.4.30 proves its noncompletion, and
B.4.33 excludes every proper filling of the actual
family over the whole $r$ disc.
```

## sections/ab_push_global_partial.tex

**Previous passage**

```text
saved output. They do not supply an origin cap.
```

**Current passage**

```text
saved output. They do not supply an origin cap; the
nonexistence statements are proved in B.4.30 and B.4.33.
```

## sections/ab_push_tate_interface.tex

**Previous passage**

```text
Mumford cusp. Global plumbing data and that
period comparison are still missing.
```

**Current passage**

```text
Mumford cusp. This auxiliary proposition supplies neither
global plumbing data nor that period comparison. B.4.33
subsequently excludes any proper filling of the actual family.
```

## sections/B_degree_one_tate_repair.tex

**Previous passage**

```text
with the prescribed torus family.
\end{proposition}
```

**Current passage**

```text
with the prescribed torus family. Such a proper filling of
the actual family is excluded by B.4.33; the present
statement retains its auxiliary embedded-collar scope.
\end{proposition}
```

## sections/ab_push_corner_resolution.tex

**Previous passage**

```text
fixed-base obstruction in B.4.20 is not removed
by recognizing a local Mumford triple chart.
```

**Current passage**

```text
fixed-base obstruction in B.4.20 is not removed
by recognizing a local Mumford triple chart. B.4.30 and
B.4.33 exclude the respective actual origin completion
and global proper filling; the local model above remains
a proved auxiliary construction.
```

## sections/B_log_base_modification.tex

**Previous passage**

```text
therefore removes a specific logarithmic
repair by base blowups without removing the
remaining unrestricted analytic possibility.
```

**Current passage**

```text
therefore removes a specific logarithmic
repair by base blowups. B.4.30--B.4.33 supply the
additional extending-section and global-loop arguments
that exclude an arbitrary proper filling; no such
comparison is assumed in this proposition.
```

## sections/B_log_torsor_obstruction.tex

**Previous passage**

```text
the obstruction has exactly the
scope stated. The period differences and complete
```

**Current passage**

```text
the obstruction has exactly the
scope stated. The additional bridge from hypothetical
arbitrary caps is proved later in B.4.30--B.4.33,
using traces and a global radial-loop invariant.
The period differences and complete
```

## sections/B_fixed_partial_noncompletion.tex

**Previous passage**

```text
It does not exclude every possible filling over
the $r$ disc: a different completion along
$r=0$, $q\ne0$ need not have the axial model of
B.4.19. In particular, resolving the graph of the
marked map in B.4.4 does not by itself supply
that additional identification.
```

**Current passage**

```text
This proposition alone does not exclude every filling
over the $r$ disc: a different completion along
$r=0$, $q\ne0$ need not have the axial model of
B.4.19. Resolving the graph in B.4.4 does not by
itself supply that identification. B.4.31--B.4.33
remove the need for it by controlling meridians and
the global affine loop class, and prove unrestricted
nonexistence for the actual family.
```

## sections/B_fixed_partial_noncompletion.tex

**Previous passage**

```text
Along the strict $r$ axis
alone the monodromy has rank one, so an
arbitrary other cap can have additional
invariant elliptic residues. The proof
does not silently identify such a cap
with B.4.19.
```

**Current passage**

```text
Along the strict $r$ axis the linear monodromy
condition alone leaves invariant elliptic directions.
The proof here does not control their geometric
residues or identify an unknown cap with B.4.19.
That control is supplied by the global argument in
B.4.31 and used, together with B.4.32, in B.4.33.
```

## sections/ab_push_global_meridians.tex

**Previous passage**

```text
Comparing the resulting unknown axial torsor with the
particular origin of B.4.19 is an additional question.
The invariant-form counterexample B.4.29 is consistent with
this limitation. No unrestricted nonexistence theorem for
Part B is inferred here.
```

**Current passage**

```text
Controlling its affine loop relative to the particular
origin of B.4.19 is an additional step, proved in B.4.32.
The invariant-form counterexample B.4.29 is consistent with
this limitation. B.4.33 uses the loop class, rather than
an extending comparison of individual origins, to prove
unrestricted nonexistence for Part B.
```

## sections/B_forms_translation_counterexample.tex

**Previous passage**

```text
such a difference. That stronger possible
bridge remains separate. Exact chart,
```

**Current passage**

```text
such a difference. The difference-extension bridge
is proved in B.4.30; B.4.31--B.4.33 add the global
meridian and loop control needed for the actual family.
They do not contradict this counterexample. Exact chart,
```

## sections/ab_push_log_canonical_torus.tex

**Previous passage**

```text
\begin{remark}[The missing reduction for an arbitrary completion]
The proposition cannot alone complete B.4.19 at its
missing origin.
```

**Current passage**

```text
\begin{remark}[The separate canonical-model reduction]
This conditional proposition is not the noncompletion
argument for B.4.19.
```

## sections/ab_push_log_canonical_torus.tex

**Previous passage**

```text
that missing reduction.
\end{remark}
```

**Current passage**

```text
that missing reduction. The unrestricted nonexistence
of the actual sphere filling in B.4.33 does not require
such a canonical model; it uses extending-section traces
and the global affine loop invariant instead.
\end{remark}
```

## sections/ab_push_kato_period_lift.tex

**Previous passage**

```text
These observations leave open connected unfoldings of noncompact
pieces with a new boundary geometry. Their analytic transition
maps, proper discontinuity, correct punctured quotient and compact
central quotient would all have to be proved; none follows from
the auxiliary compact family in B.4.10.
```

**Current passage**

```text
These observations alone do not classify connected unfoldings
of noncompact pieces with a new boundary geometry. Analytic
transition maps, proper discontinuity and the retained punctured
quotient are not supplied by the auxiliary compact family in
B.4.10. Independently of that restricted classification question,
B.4.33 rules out any such construction giving a proper filling
of the actual global family.
```

## sections/B_origin_fibre_dimension.tex

**Previous passage**

```text
has an
proper analytic completion
```

**Current passage**

```text
has a
proper analytic completion
```

## sections/B_origin_fibre_dimension.tex

**Previous passage**

```text
geometry retained.
\end{proposition}
```

**Current passage**

```text
geometry retained. B.4.30 subsequently excludes even
the permitted vertical-component completions of the
fixed partial family, and B.4.33 excludes every proper
filling of the actual global family.
\end{proposition}
```

## sections/B_hodge_results.csv / B.4.3 / notes

**Previous passage**

```text
Existing Hodge results are applied with complete derivation. Excludes all-Kahler and all-Moishezon component models in the simple-NC category for every finite base change; unrestricted analytic fillings remain open. Independently refereed in E_B_hodge_referee.md.
```

**Current passage**

```text
Existing Hodge results are applied with complete derivation. Excludes all-Kahler and all-Moishezon component models in the simple-NC category for every finite base change; unrestricted nonexistence for the actual family is proved separately in B.4.33. Independently refereed in E_B_hodge_referee.md.
```

## sections/B_hodge_results.csv / B.4.4 / statement

**Previous passage**

```text
In every such filling the intrinsically marked map to P1 extends meromorphically and becomes holomorphic on a proper projective graph modification that is unchanged over the punctured disc.
```

**Current passage**

```text
After resolving the reduced main component of any proper analytic filling of a finite cover of the actual family, the intrinsic marked map to P1 extends meromorphically on the smooth dominating fourfold and becomes holomorphic on a proper projective graph modification unchanged over the punctured disc.
```

## sections/B_hodge_results.csv / B.4.4 / notes

**Previous passage**

```text
Coherent bi-anticanonical frame and the three labelled critical-value branches remove essential PGL2 gauges. No smoothness of the graph or Moishezon property of unknown vertical components is inferred. Independent referee: E_B44_referee.md.
```

**Current passage**

```text
Coherent bi-anticanonical frame and three labelled critical-value branches remove essential PGL2 gauges. No hypothesis on the central divisor or its multiplicities is used. No Moishezon assertion for unknown vertical components is inferred. Independent original referee E_B44_referee.md; arbitrary-filling scope checked by root and limits_ab in B.4.31.
```

## sections/B_hodge_results.csv / B.4.5 / notes

**Previous passage**

```text
No ddbar assumption on intersections and no algebraicity or simple-crossing assumption are required. All-Kahler and all-Moishezon normalization constructions are excluded for every finite base change. The arbitrary analytic filling remains open.
```

**Current passage**

```text
No ddbar assumption on intersections and no algebraicity or simple-crossing assumption are required. All-Kahler and all-Moishezon normalization constructions are excluded for every finite base change. The arbitrary proper analytic filling is excluded by the separate global argument in B.4.33.
```

## sections/ab_push_corrected_cusp_overlap_results.csv / B.4.18 / notes

**Previous passage**

```text
Root and boundary_d independently passed the construction. Orientation corrected at 19:39 UTC: the positive fractional deck has positive-q shift +1 and clockwise g0 shift -1; this is the common B.3 marking. The retained affine family and prescribed rotations occur on their respective axes. The origin completion and global finite-place overlaps remain open. Exact code/output ab_push_corrected_cusp_overlap.py/.out/.json; referee D_corrected_cusp_overlap_referee.md; earlier wording retained in the working note.
```

**Current passage**

```text
Root and boundary_d independently passed the construction. Orientation corrected at 19:39 UTC: the positive fractional deck has positive-q shift +1 and clockwise g0 shift -1; this is the common B.3 marking. The retained affine family and prescribed rotations occur on their respective axes. The global finite-place overlaps are constructed in B.4.19. The prescribed origin completion is excluded in B.4.30, and arbitrary proper fillings of the actual global family are excluded in B.4.33. Exact code/output ab_push_corrected_cusp_overlap.py/.out/.json; referee D_corrected_cusp_overlap_referee.md; earlier wording retained in the working note.
```

## sections/ab_push_global_partial_results.csv / B.4.19 / notes

**Previous passage**

```text
Root and boundary_d independently passed the full proof. Scalar logarithms k=log(K)/(2pi i) give integral r shifts; finite collars cancel exactly; corrected cusp comparison is G(s)+6v delta. Exact code/output ab_push_global_partial.py/.out/.json PASS; referee D_B4419_referee.md. Properness is over the punctured two-dimensional base Omega, not over the full r disc. Origin completion, global B filling, central topology, and analytic C.5.1 remain Open.
```

**Current passage**

```text
Root and boundary_d independently passed the full proof. Scalar logarithms k=log(K)/(2pi i) give integral r shifts; finite collars cancel exactly; corrected cusp comparison is G(s)+6v delta. Exact code/output ab_push_global_partial.py/.out/.json PASS; referee D_B4419_referee.md. Properness is over the punctured two-dimensional base Omega, not over the full r disc. B.4.30 excludes this partial family's origin completion; B.4.33 excludes every proper filling of the actual global family after finite covers. Thus no actual global central topology or analytic filling of C.5.1 arises from such a degeneration.
```

## sections/ab_push_tate_interface_results.csv / B.4.20 / notes

**Previous passage**

```text
Root and boundary_d independently passed. In W=exp(-2pi i zeta2), normal factor a=exp(-2pi i mu) corresponds to M^-1 for M=O(P-O); closing translation is a^-6=6P. At nodes s=uv-h differs from normal-line s=uv. Fixed-base localized plumbing of entire Kato retains exceptional rational curves and cannot give ordinary two-tori. Full second-period extension and actual origin cap remain Open. Exact code/output ab_push_tate_interface.py/.out/.json PASS.
```

**Current passage**

```text
Root and boundary_d independently passed. In W=exp(-2pi i zeta2), normal factor a=exp(-2pi i mu) corresponds to M^-1 for M=O(P-O); closing translation is a^-6=6P. At nodes s=uv-h differs from normal-line s=uv. Fixed-base localized plumbing of entire Kato retains exceptional rational curves and cannot give ordinary two-tori. No full second-period extension is constructed here. The actual fixed origin cap is excluded by B.4.30 and every proper global sphere filling by B.4.33; the embedded Tate-interface theorem remains auxiliary. Exact code/output ab_push_tate_interface.py/.out/.json PASS.
```

## sections/B_degree_one_tate_repair_results.csv / B.4.21 / notes

**Previous passage**

```text
Root and limits_ab independently passed the full source. Exact code/output code/d_push_degree_one_repair.py/.out/.json PASS. Original punctured Kato family is unchanged; the original-to-new normal gauge is q^-1. This is an actual collar construction, not an extension of the whole second-period action or an identification with the actual torus family. The B.4.19 origin cap remains Open.
```

**Current passage**

```text
Root and limits_ab independently passed the full source. Exact code/output code/d_push_degree_one_repair.py/.out/.json PASS. Original punctured Kato family is unchanged; the original-to-new normal gauge is q^-1. This is an actual collar construction, not an extension of the whole second-period action or an identification with the actual torus family. The B.4.19 origin cap is excluded by B.4.30, and arbitrary proper global fillings are excluded by B.4.33. The proved collar remains an auxiliary construction.
```

## sections/ab_push_corner_resolution_results.csv / B.4.22 / notes

**Previous passage**

```text
Root and boundary_d independently passed the full source. Actual collar F=(1+H)^-1; additional F=0 charts are only a local completion candidate. After q=s^n the reduced divisor is s=0 and div(q) has multiplicity n; no q-deck descent asserted. n12 gives144 cones over one triple point, agreeing with the earlier local count. Global complement, whole second-period action, surviving rational-curve families and origin cap remain Open. Exact code/output/json ab_push_corner_resolution all PASS.
```

**Current passage**

```text
Root and boundary_d independently passed the full source. Actual collar F=(1+H)^-1; additional F=0 charts are only a local completion candidate. After q=s^n the reduced divisor is s=0 and div(q) has multiplicity n; no q-deck descent asserted. n12 gives144 cones over one triple point, agreeing with the earlier local count. A global complementary Kato model and whole second-period action are not constructed. B.4.30 excludes the fixed actual origin cap, and B.4.33 excludes every proper filling of the actual global family. The local resolution and retained collar comparison remain proved. Exact code/output/json ab_push_corner_resolution all PASS.
```

## sections/ab_push_kato_period_lift_results.csv / B.4.13 / notes

**Previous passage**

```text
Root and boundary_d independently checked the finite-modification proof; D supplied the normal-line strengthening. The marked axis and holomorphic action must extend. Infinite disjoint-copy shifting has the wrong punctured core; connected noncompact unfoldings and central-only caps remain open. No meromorphic-to-holomorphic comparison is assumed.
```

**Current passage**

```text
Root and boundary_d independently checked the finite-modification proof; D supplied the normal-line strengthening. The marked axis and holomorphic action must extend. Infinite disjoint-copy shifting has the wrong punctured core; the restricted lemma does not classify connected noncompact unfoldings or central-only modifications. B.4.33 independently excludes any construction producing a proper filling of the actual family. No meromorphic-to-holomorphic comparison is assumed.
```

## sections/ab_push_hopf_cap_results.csv / B.4.7 / notes

**Previous passage**

```text
Root independently refereed. Exact Chern restrictions1,i and generic1+i; integral H1 matrix unimodular, coherent H1 map rank1. This is not an S6 filling: nearby pi1=Z and Euler0. Triple-divisor corrections may repair the naive interface degree mismatch; the actual cusp comparison remains open.
```

**Current passage**

```text
Root independently refereed. Exact Chern restrictions1,i and generic1+i; integral H1 matrix unimodular, coherent H1 map rank1. This is not an S6 filling: nearby pi1=Z and Euler0. Triple-divisor corrections may repair the naive interface degree mismatch; this auxiliary family is not an actual cusp comparison. B.4.33 independently excludes proper fillings of the actual global family.
```

## sections/ab_push_log_canonical_results.csv / B.4.28 / notes

**Previous passage**

```text
Root and boundary_d independently passed the revised full proof. Parabolic components are excluded by elliptic normal-degree balance; hyperbolic components by a zero homology/nonzero relative-form-period contradiction in the nearby torus. The original false central free-product argument is explicitly rejected and retained in evidence/ab_push_log_canonical_rejected_free_product.tex. The omega_D-trivial hypothesis is not inferred from nearby tori; obtaining such a modification of an arbitrary analytic completion remains Open. Exact determinant/residue code ab_push_log_canonical_period PASS.
```

**Current passage**

```text
Root and boundary_d independently passed the revised full proof. Parabolic components are excluded by elliptic normal-degree balance; hyperbolic components by a zero homology/nonzero relative-form-period contradiction in the nearby torus. The original false central free-product argument is explicitly rejected and retained in evidence/ab_push_log_canonical_rejected_free_product.tex. The omega_D-trivial hypothesis is not inferred from nearby tori; a general canonical-model reduction for arbitrary analytic torus degenerations is not proved. B.4.33 excludes the actual sphere filling without that reduction. Exact determinant/residue code ab_push_log_canonical_period PASS.
```

## sections/B_elliptic_weights_results.csv / B.4.14 / notes

**Previous passage**

```text
Root full-source and AB independent referee PASS. Exact code ab_push_kato_weights.py passes. Nonisolated local deformation compatibility and analytic globalization remain open; no compact third component or S6 filling is inferred.
```

**Current passage**

```text
Root full-source and AB independent referee PASS. Exact code ab_push_kato_weights.py passes. Nonisolated local deformation compatibility and analytic globalization for this auxiliary associated bundle are not proved; no compact third component is inferred. The actual proper S6 filling is excluded by B.4.33.
```

## sections/B_hopf_resonance_obstruction_results.csv / B.4.25 / notes

**Previous passage**

```text
Root and limits_ab independently passed the full proof. Accumulating anticanonical resonances contradict the coherent direct-image exact sequence. Oda1978 Section13 instead has both contraction eigenvalues tending to zero. This excludes the specified unblown Hopf replacement of the Kato collar and does not exclude arbitrary completions of the actual two-torus family.
```

**Current passage**

```text
Root and limits_ab independently passed the full proof. Accumulating anticanonical resonances contradict the coherent direct-image exact sequence. Oda1978 Section13 instead has both contraction eigenvalues tending to zero. This excludes the specified unblown Hopf replacement of the Kato collar and alone does not exclude arbitrary completions of the actual two-torus family; the actual global noncompletion is proved in B.4.33.
```

## sections/B_fixed_partial_noncompletion_results.csv / B.4.30 / notes

**Previous passage**

```text
Root and boundary_d full-source PASS. Direct coefficient-ideal equidimensionalization, coherent saturation, integral primitives, simultaneous product root and compatible star subdivisions, norms and Hartogs prove the fixed-partial noncompletion. This result alone does not exclude arbitrary r-only fillings with different r-axis caps.
```

**Current passage**

```text
Root and boundary_d full-source PASS. Direct coefficient-ideal equidimensionalization, coherent saturation, integral primitives, simultaneous product root and compatible star subdivisions, norms and Hartogs prove the fixed-partial noncompletion. This result alone does not exclude arbitrary r-only fillings with different r-axis caps. B.4.31--B.4.33 supply the global meridian and affine-loop bridge and exclude them without identifying their models.
```

## sections/B_log_torsor_results.csv / B.4.24 / notes

**Previous passage**

```text
Root and boundary_d independently opened the original KKN source and passed the complete proof. The two actual extending origins give clutching F; the r-loop Y class gamma cannot split because the q-ghost map is injective. Fixed fan models are not called group objects. No implication from an arbitrary analytic cap with vertical threefolds to this torsor category is assumed.
```

**Current passage**

```text
Root and boundary_d independently opened the original KKN source and passed the complete proof. The two actual extending origins give clutching F; the r-loop Y class gamma cannot split because the q-ghost map is injective. Fixed fan models are not called group objects. No implication from an arbitrary analytic cap with vertical threefolds to this torsor category is assumed here. B.4.30--B.4.33 later construct the required associated torsor from extending trace differences.
```

## sections/ab_push_global_meridians_results.csv / B.4.31 / notes

**Previous passage**

```text
Root and boundary_d full-source PASS; root also passed the explicit reduction from an arbitrary proper analytic filling. Retain the reduced main component and resolve; B.4.4 needs no central reducedness. Finite actual H1 orbits follow from proper connected double-curve families and basepoint conjugation. Exact unipotents have no nonzero finite-orbit vector. Multiplicities use finite local r-monodromy; no semistable-reduction theorem is invoked. Affine origins and comparison with B.4.19 remain separate. Exact code PASS; initial minor-sign assertion retained.
```

**Current passage**

```text
Root and boundary_d full-source PASS; root also passed the explicit reduction from an arbitrary proper analytic filling. Retain the reduced main component and resolve; B.4.4 needs no central reducedness. Finite actual H1 orbits follow from proper connected double-curve families and basepoint conjugation. Exact unipotents have no nonzero finite-orbit vector. Multiplicities use finite local r-monodromy; no semistable-reduction theorem is invoked. The separate affine-loop control is proved in B.4.32 and used in B.4.33; no extending identification of individual origins is asserted. Exact code PASS; initial minor-sign assertion retained.
```

## sections/B_global_loop_defect_results.csv / B.4.32 / notes

**Previous passage**

```text
Root final full-source PASS; E and AB working-proof PASS. The actual finite/cusp affine overlaps add only δ radial loops; two extending sections give the same normalized class; the full rank-three quotient has zero common fixed space. Arbitrary singular fillings are reduced and resolved first. Only a loop class is controlled, not a bounded comparison of origins.
```

**Current passage**

```text
Root and limits_ab final full-source PASS; E working-proof PASS. Independent AB full-source referee and exact symbolic all-degree audit saved. The actual finite/cusp affine overlaps add only δ radial loops; two extending sections give the same normalized class; the full rank-three quotient has zero common fixed space. Arbitrary singular fillings are reduced and resolved first. Only a loop class is controlled, not a bounded comparison of origins.
```
