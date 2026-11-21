# Prerelease independent derivation

Checker: i_provenance_recovery. Written 2026-11-21T21:24:19.177179+00:00. Both IK and DU own printed proofs remain closed. Prior exposures are disclosed: Paper I, the safe statement packets, the now independently frozen/released named torsion lemma03IF, and the unnumbered W.4/W.5 coordinate proofs displayed by the broader03IF release. The I9 ancillary proof’s final invocation of IK’s stated section was also seen post-I9-freeze; it did not expose IK’s own proof. The W.4/W.5 exact statements and source-bound nonproof global setup are declared inputs. This derivation proves the target conclusions anew from those inputs.

## Exact notation transport

The existing nonproof definitions give T=ker(Omega_S->j_*Omega_{S_reg}), Q=Omega_S/T and the explicit existing equality Q=tildeOmega_S. The proved03IF input identifies T with Tor(Omega_S). The map from Q to j_*Omega_{S_reg} is [omega]->omega|reg. Its kernel is zero by that exact kernel definition, and its image is the image of restriction; its inverse on that image takes a local restricted differential to the class of any local lift, independent of the lift because differences lie in T. This constructs the quotient/image identification, without imposing a new meaning on tildeOmega. The map Omega_S->tildeOmega is the quotient map omega->[omega].

Owner: wbII:prop:conductor, tag03IK.

The supplied global map g:Xcal->Delta has nonempty full fibre S=(g=0), reduced normal crossings in a smooth threefold. The ideal(g) is globally generated and g is a nonzerodivisor, so the conormal bundle is O_S through h->[hg] mod g^2, and its differential sends h to h*dg|S. This is precisely the declared W.4 injection. Let F=Omega_Xcal|S tensor A, a locally free sheaf. Tensor the supplied exact conductor square W.5 by F; local freeness preserves exactness, and the finite-normalization projection formula identifies its first nontrivial term with eta_*eta^*F directsum F|D. The map is s->(eta^*s,s|D), and the next map is difference of the two restrictions to tildeD.

In a local model g=u*x*y, the coefficients of dg|S are u*y,u*x (the xy*du term is zero on S), and their pullbacks vanish on tildeD. In the triple model g=u*x*y*z they are u*yz,u*xz,u*xy and likewise vanish on every branch conductor; at a smooth point the conductor is empty. Thus the global pair(eta^*(dg|S) tensor e,0) lies in the kernel of the difference map. Exactness constructs a unique section s of F with those two specified restrictions. This is a global construction: locally exact descent gives local sections, and their equality on overlaps follows from injectivity of F->eta_*eta^*F, which in a local frame is the injection of a reduced ring into its normalization.

For further explicitness, at a double point write the normalized coefficients of e in a local frame of A as(e1(y,z),e2(x,z)). A representative of s is u*(e1*y*dx+e2*x*dy). At a triple point it is u*(e1(y,z)*yz*dx+e2(x,z)*xz*dy+e3(x,y)*xy*dz). Each coefficient is in the conductor ideal, respectively(x,y) and(xy,xz,yz), and has the prescribed pullback; arbitrary lifts differing by a branch equation give zero after multiplication by the indicated conductor monomial. The formulas agree under frame or coordinate changes because their normalized pullback is the fixed global dg tensor e and descent is unique. They give s|D=0 as a sheaf restriction, not merely pointwise vanishing. The section is nonzero: on each regular branch dg is nonzero and e is a unit.

On S_reg the normalization is an isomorphism, so rho(s) is the image of the conormal differential times the local section e and is zero. The exact kernel equality above therefore places rho(s) in Tor(Omega_S) tensor A. Its image under the quotient to tildeOmega tensor A is zero.

For(a), rho(s)=0 means s is in the kernel sheaf of Omega_X|S tensor A->Omega_S tensor A. W.4 identifies this kernel with A through sigma->dg tensor sigma, so there is a unique global sigma with that equality. Pulling to the normalization gives dg*(eta^*sigma-e)=0. The factor dg is nonzero at a generic smooth point of every normalization component; the scalar difference is holomorphic, so the identity theorem makes it zero on each component. Thus eta^*sigma=e. At any point of S, the coefficient a of sigma in a local frame pulls back to a unit on each branch. A coefficient in the maximal ideal would vanish at every point over that point, so a is a unit; sigma is nowhere vanishing. Conversely such a sigma gives dg tensor sigma with the required normalized restriction and zero conductor restriction, hence equals s by uniqueness and has rho(s)=0.

For(b), assume the stated compact connected S and nontrivial A. A section sigma pulls back, relative to e, to a holomorphic function on every compact connected normalization component, hence a constant c_j. At an intersection of components, the two values of the descended sigma in the one-dimensional fibre A_p agree; since both corresponding e-values are nonzero, one constant vanishes exactly when the other does. The finite incidence graph of the irreducible components is connected: a disconnection would partition the compact finite union S into two disjoint closed unions, contrary to connectedness. Hence a nonzero sigma has all c_j nonzero and is nowhere vanishing by the local unit test just given. The map O_S->A sending1 to sigma would then be an isomorphism, with inverse division by its unit coefficient in each frame. Since A is nontrivial, no nonzero sigma exists. As N* is O_S, the conormal global-section term is zero, while s is nonzero, so s cannot come from that term. This proves every part of the target.

## Bound inputs

[
  {
    "path": "agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03IK_statement_inputs.tex",
    "sha256": "6f949cf8dc66a850d886721d82438c8a122996dd6df403dca8ad78a755262c0b"
  },
  {
    "path": "agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_03IK_cited_input_supplement.tex",
    "sha256": "33bcbcdf149af83d5cadd8c75b42d60b486f058663757d7f2711535de3f257a2"
  },
  {
    "path": "agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_03IK_03DU_setup_inputs.tex",
    "sha256": "2e9029fb1adf51dfd0ebb87048afb0db065d75dad065314e9155d1d3c89d5387"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_IK_DU_existing_notation_inputs.json",
    "sha256": "b1d05935395d5ae5eeebd159b9f2eb536be6efa82e8ea7fd48dbe9694bc8ccf5"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_03IF_freeze_pointer.json",
    "sha256": "14e3dc7ac32666602d7d27b3e4a0f87ec0e44eab578307899daf5636f282efcf"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_03IF_release_pointer.json",
    "sha256": "7857e12464a4c84168433ac79848d930f442d25f01a4bbe616a3a51a749f7fd8"
  }
]
