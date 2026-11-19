# Prereading derivation11: P1A.5 analytic boundary non-extension

19 November2026. The target statement and its definition of analytic extension have been read; the P1A.5 target proof has not. Its cited input P2.4 was opened as an existing input, so this reviewer is now exposed to that Paper I proof and makes no later prereading claim for it. P2.4 recovers its marked base from the relative pluricanonical direct image. I derive the actual fourfold version below, rather than identifying the two dimensions without a map.

## 1. The moving pluricanonical pencil in the actual fourfold

P1A.1 supplies K_M=h*L^-6 on the5,4 root base, with rho_*L^r of coarse degree floor(4r/5)+floor(-3r/4). At r=24 this degree is19-18=1. Hence

    H0(M,K_M^-4)=H0(Bhat,L^24)=H0(P1,O(1)),

with dimension2. The first equality uses the given connected-fibre pushforward h_*O_M=O_Bhat. On each root chart every invariant section of L^24 is its fixed local monomial times a section of the coarse O(1). The ratio of two independent sections cancels that same monomial; thus the moving part of the complete system |K^-4| is exactly the marked base map h, up to a projective change of coordinate. This is the exact replacement for P2.4's K^-2 pencil on the threefold.

## 2. Recovering the base over an alleged full-disc extension

Assume the extension asserted impossible by P1A.5 exists. Its known part is only a nonempty open parameter sector in the admissible half-plane; nothing here assumes it fills the punctured disc in advance. Take the reduced irreducible component containing that known family and resolve it by the analytic resolution input used in P2.4. Properness and the proper-image theorem imply that the singular and non-submersion values of the total family over the disc form an analytic subset. They avoid the known open sector. Shrinking the disc therefore makes the resolved family p:Z->Delta a smooth proper family away from the central point. The resolution is unchanged there on the known sector.

Set J=omega_(Z/Delta)^-4. Grauert coherence gives p_*J coherent. Multiplication by the disc coordinate is injective on J and hence on p_*J, so this direct image is torsion-free and free over the one-dimensional smooth base. Its generic rank is2 because it is2 on the known open sector. The failure of base change or constancy of h0 is analytic and avoids that sector; after shrinking it occurs at most at0. A frame of p_*J therefore defines the fibrewise complete moving pencil away from0 and a meromorphic map Z-->P1 over the disc.

Resolve its graph. This is the actual graph of the coherent evaluation map, whose sections have only finite-order parameter singularities. It is not the closure of an arbitrary holomorphic map with an essential singularity. The modification is proper and is an isomorphism where the moving pencil was already a holomorphic map. On the known sector it recovers h up to a projective coordinate change. Non-invertibility of its base ideal is analytic; its image in the disc avoids the known sector, so after shrinking no additional graph modification is needed over noncentral fibres.

The critical image of the proper map to P1 times Delta is analytic. On the known sector it consists of exactly the order5 fibre, order4 fibre and nodal-cusp fibre, with their distinct local types. Any nonvertical component of the critical image meets that sector, so there are exactly those three moving critical values away from0. Vertical exceptions project to a discrete subset of the disc and can be removed by shrinking. The three distinct types label the values; after normalization they are meromorphic sections over the disc. If a further finite cover is required to choose a branch of an intermediate parameter description, it is allowed: the same argument will exclude the resulting extension as well.

The unique projective transformation taking these three meromorphic sections to the fixed values infinity,0,a has meromorphic coefficients. Composing with it gives the actual marked base map after one further proper graph resolution. Away from0 the values are distinct, so this transformation is holomorphic and invertible there. We thus have a proper holomorphic map

    (h_ext,p):Z' -> P1 times Delta

whose restriction to the known sector is exactly the given marked map. For lambda in U=P1 minus{0,infinity,a}, this is a smooth proper family of threefolds over U times Delta*, after removing the analytic exceptional locus if needed. Its fibres on the known sector are precisely the constructed complex tori.

## 3. Torus fibres and period planes on the analytically continued open set

The torus property needed for the contradiction is required only outside a proper analytic subset, and can be proved by actual differential forms. On the smooth part of the preceding proper family, the coherent direct image of relative holomorphic1-forms has generic rank3, as it does on the known torus sector. Remove its analytic base-change and non-locally-free locus. Evaluation of this rank3 bundle into the relative cotangent bundle has full rank at every point over that sector. The rank-deficiency locus is analytic in the total space, and its proper image is an analytic subset of the base. Remove that image as well. Fibrewise exterior differentiation of these sections vanishes on the known sector, hence vanishes identically by the analytic identity theorem. The remaining fibres consequently have three everywhere independent closed holomorphic1-forms.

Their dual vector fields commute because the forms are closed. On each compact fibre the vector fields are complete; the resulting holomorphic C^3 action has full tangent rank everywhere and is transitive. Its stabilizer is discrete, so the fibre is C^3/Gamma; compactness makes Gamma a full real lattice. Thus every remaining fibre is a complex torus. This argument supplies the exact map from the continued forms to the torus structure and does not invoke an unproved closedness of the torus locus in a deformation space.

Ehresmann transport on the proper smooth part identifies H1 with the existing rank-six local system. Integrating the three closed forms gives the holomorphic period3-plane in its complexification. Work on the universal cover of the regular base to fix its integral marking. On the known nonempty sector this plane is the explicit F_xi=(sigma+xi alpha e)(P). The same equality then holds by holomorphic continuation wherever the period plane is defined: both sides are holomorphic maps to the same Grassmannian, the right side being the supplied graph and meromorphic only at the parameter infinity itself. A parameter-loop monodromy only changes the integral marking; it does not change the real-transversality assertion used next.

Denote by E the union of the proper analytic exceptional subsets removed above. Locally in the complex surface U times Delta*, E has real dimension at most2. A nonempty smooth real hypersurface of that surface has dimension3 and cannot be contained in E. This dimension statement is all that is needed; no assertion that every continued fibre is a torus is made.

## 4. Finite boundary points produce a transverse-plane contradiction

Let xi0 be a finite boundary point, Im(xi0)=c_*=-h_min. A point lambda where h takes its minimum may be a finite root point rather than a point of U. Nevertheless continuity at the roots gives points of U with h arbitrarily close to h_min; if h equals its minimum on an open set, those points already lie in U. Thus for every sufficiently small parameter disc around xi0 there are lambda in U and xi in that disc with

    Im(xi)+h(lambda)=0.

For fixed lambda, the real part of xi is free. More generally this equation defines a smooth real hypersurface in U times the parameter disc, because its derivative with respect to Im(xi) is1. It has nonempty open pieces with noncentral parameter; these cannot all lie in E. Choose a point outside E on this hypersurface. The corresponding fibre is a compact complex torus, so its holomorphic period plane must have zero intersection with its complex conjugate. But its plane is the analytically continued F_xi, and the already derived exact height criterion gives F_xi intersect conjugate(F_xi) nonzero. This is a contradiction.

For a finite ramified change xi-xi0=t^m times a holomorphic unit, its derivative is nonzero off t=0 after shrinking. The inverse image of the same hypersurface is therefore still a nonempty smooth real hypersurface off0. The identical contradiction survives every such finite cover. No choice of a branch or of a lift removes it.

## 5. Infinity and all permitted central spaces

At infinity the boundary coordinate is u=1/xi. Fix any regular lambda. The values

    xi=R-i h(lambda),  u=1/(R-i h(lambda))

satisfy the same failure of real transversality and tend to u=0 as real R tends to either infinity. Varying lambda and R supplies local3-real-dimensional hypersurface pieces in U times the punctured u-disc. The map u->1/u has nonzero derivative there, so these pieces again cannot be contained in E. At a point outside E the continued smooth torus fibre would have the forbidden plane F_(1/u). This contradicts the existence of the extension at infinity. Replacing u by any finite ramified coordinate retains the same off-centre hypersurface argument.

The proof never assumes that the central total-space fibre is smooth, reduced, irreducible, or equal to a torus fibration before modification. Extra central components were discarded only after choosing the component containing the prescribed nonempty open family, and all resolutions/graph modifications are proper. The contradiction occurs at a noncentral smooth torus fibre of the extended marked map. Therefore the allowed singularities, multiplicities and additional central components in the definition of P1A.5 do not evade it.

This completes the proposed full rederivation before opening the target proof. The proper-image, coherence and base-change inputs are the precise analytic inputs cited in P2.4; the new fourfold computation is the K^-4 moving pencil above. Any additional printed intermediate argument will be compared separately and not retroactively described as preread.
