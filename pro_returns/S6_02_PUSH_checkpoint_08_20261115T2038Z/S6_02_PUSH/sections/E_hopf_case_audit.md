# Negative-slope specialization: Hopf-case source and obstruction audit

Status at 15 November 2026, after checkpoint05: **the negative-slope fixed-divisor obstruction is resolved by E.2.9–E.2.10**. The full exclusion of arbitrary holomorphic Hopf-surface algebraic reductions on a complex six-sphere has not been established and is not needed for that conclusion. The parent and boundary-D agents independently refereed the complete E.2.8–E.2.10 sources and passed them. Sections1–9 below retain the source audit and unsuccessful classification routes in their historical scope; Section10 records the subsequent vanishing proof that supersedes their fixed-divisor gap.

## 1. The exact question remaining after E.2.5–7

In a smooth one-sided specialization of known members, write A=12kl and D=kl−3k−4l. The unique relative fractional canonical line L satisfies L^D=K_rel^A. Its two limiting sections have a holomorphic ratio, by the valid non-holomorphic-map theorem, but may have a common divisor E0. For D>0, E.2.6 removes this divisor and the possible target degree. For D<0, a horizontal component of E0 would restrict to a nonzero effective antipluricanonical divisor on a smooth general fibre F of the central algebraic reduction. Because c1(KF)=0, this makes F non-Kähler with Kodaira dimension −infinity, hence class VII with b1=1. Also c2(F)=0, since TF⊕O is TX restricted to F and H4(X,Z)=0; thus b2(F)=0. The known classification then leaves Hopf surfaces once the presence of a curve excludes the Inoue case. The proof of E.2.8 only needs b1=1 and deliberately avoids choosing a primary cover or excluding secondary Hopf surfaces by an unproved integral monodromy argument.

## 2. The proved component-count repair and normalization obstruction

For a finite nonempty set Sigma containing all critical values, let s=|Sigma| and r be the total number of irreducible components of the reduced inverse image. Alexander duality gives b1(X minus A,Q)=r. The correct low-degree Leray sequence gives r=s−1+dim H1(F,Q)^mon, with the invariant subspace retained. If b1(F)=1, then r≤s, whereas each fibre is nonempty so r≥s. Equality forces irreducibility of every reduced fibre and trivial rational degree-one monodromy.

A horizontal prime H maps onto the base and meets each fibre S. Irreducibility prevents S from being contained in H. Its canonical section therefore gives a nonzero effective Cartier divisor on the reduced support S. At a local self-intersection, nonvanishing on every branch follows by pulling to the irreducible normalization and applying analytic continuation; it is not an inference from global irreducibility to local irreducibility. Pullback to a Kähler resolution of the normalization would give a nonzero effective divisor in a line with c1=0, contradicting positive Kähler area. Nonreduced fibre multiplicities cause no difficulty because the argument first passes to S_red.

This proves E.2.8, including its application to the negative-slope horizontal fixed divisor. It does not exclude fibre normalizations outside Fujiki class C.

The final source also includes the following companion, accepted independently by the root: without a rank-one assumption, each irreducible component of a reducible fibre meets another component by connectedness. The line of that other prime divisor restricts to a nonzero effective Cartier divisor with zero Chern class. The same positivity argument therefore puts the normalization of every component of a reducible fibre outside class C. This rules out ordinary projective blowup components as a proposed explanation of a collapsed-target smooth limit, but not the non-Kähler alternatives.

## 3. What was and was not recovered from CDP2020

The original publisher PDF was opened and Sections 4, 6 and 7 were read directly:

Campana, F., Demailly, J.-P., & Peternell, T. (2020). The algebraic dimension of compact complex threefolds with vanishing second Betti number. *Compositio Mathematica, 156*, 679–696. https://doi.org/10.1112/S0010437X19007802

Publisher full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf

Theorem2.1, p.679, concerns a non-holomorphic nonconstant meromorphic map to P1. It is the theorem used in E.2.5, with the independent LRS proof also recorded there. The different holomorphic-fibration assertion, Theorem2.2, and Corollary2.3 are not imported. Lemma4.2, p.684, replaces the monodromy invariant space by the full H1 group; E.2.8 repairs only the rational rank-one consequence by the explicit inequality above. It does not recover the claimed unrestricted direct-sum decomposition or integral torsion-freeness.

The singular-fibre reduction on p.692 goes through the cotangent sequence and then attempts to reduce to torsion-free differentials on the fibre. For a nonnormal fibre the torsion in its differential sheaf can support the missing sections. Irreducibility by itself does not remove that issue. Thus neither the Hopf-general-fibre subcase nor the Picard/cohomology assertions of Sections6–7 are promoted wholesale. Possible rank-one repairs of R1f_*O and the restriction map still do not prove the needed cotangent vanishing on arbitrary nonnormal fibres.

## 4. A concrete Hopf degeneration does not fit the canonical condition

Opened original publisher PDF:

Kerr, M., Laza, R., & Saito, M. (2022). Deformation of rational singularities and Hodge structure. *Algebraic Geometry, 9*(4), 476–501. https://doi.org/10.14231/AG-2022-014

https://content.algebraicgeometry.nl/2022-4/2022-4-014.pdf

Proposition1, p.478, has a projective central-fibre hypothesis. It cannot be silently changed to an arbitrary Moishezon analytic centre. Remark2.4, pp.493–494, discusses Kodaira's degeneration of Hopf surfaces with smooth total space and a central nonnormal rational surface. Its normalization is the first Hirzebruch surface, with two disjoint sections of self-intersections −1 and +1 identified. Its rational Betti numbers are (1,1,1,0,1), while those of a smooth Hopf surface are (1,1,0,1,1). Thus h2(O)=0 or rational normalization alone does not prohibit a singular Hopf limit.

For that particular model, however, the pullback of the dualizing line is K_F1+C_minus+C_plus=−2F, where F is a ruling fibre. This integral Chern class is nonzero. Such a reduced Cartier fibre cannot occur in the present six-sphere setting, where adjunction makes its dualizing Chern class zero (the fibre normal line is torsion in the multiple-fibre case). E.2.8 also excludes it when a horizontal divisor is present. This is an exclusion of the stated model, not a classification of all irreducible Hopf completions.

## 5. Isotriviality is suggestive but does not solve the completion problem

Opened author primary version:

Dloussky, G. (2006). On surfaces of class VII_0^+ with numerically anticanonical divisor. *American Journal of Mathematics, 128*(3), 639–670. https://doi.org/10.1353/ajm.2006.0021

https://arxiv.org/pdf/math/0406387 (version3, 13 April 2005), Section1.3, manuscript pp.12–13.

For primary Hopf surfaces the contraction trace and determinant are bounded holomorphic moduli and extend across parameter punctures. Over a punctured compact base curve their extensions are constant, and the determinant remains nonzero. This suggests generic isotriviality, allowing the known diagonal/resonant distinction. Constructing the appropriate relative primary covers for a family of secondary Hopf surfaces is a further step; it is not supplied by the rational rank-one calculation.

Even a proved isotrivial punctured Hopf family does not give a meromorphic comparison with every proper analytic completion. B.4.7 supplies an isotrivial Hopf family with a reducible centre. Its two components are excluded by the rank-one component count here, but its existence blocks any unrestricted compactification-uniqueness claim. The Kato family audited in B.4.10 has blown-up Hopf general fibres with b2>0 and a contraction eigenvalue tending to zero; it is not a counterexample to the narrower irreducible, minimal, fixed-nonzero-eigenvalue question. Neither example proves that narrow question.

## 6. The attempted elliptic-curve/Enoki route has a specific gap

The normalization of a horizontal divisor is itself outside class C: pull back f^*O(1), whose Chern class is zero on X, to any supposed Kähler resolution and use a nonempty fibre divisor. Since curves on the general Hopf fibre are elliptic, the resolved horizontal divisor has a general elliptic fibration after Stein factorization. One might try to force an elliptic component in every intersection with a singular fibre, then exclude a flat effective divisor supported on the rational cycle of an Enoki normalization.

The source statements about Enoki surfaces are precise. Teleman (2010), p.1758, recalls Enoki's characterization via an effective divisor with torsion Chern class. Toma (2008), pp.249–250, identifies the rational cycle as the only homologically trivial effective reduced divisor in the relevant Enoki case. Their original PDFs were opened:

- Teleman, A. (2010). Instantons and curves on class VII surfaces. *Annals of Mathematics, 172*(3), 1749–1804. https://doi.org/10.4007/annals.2010.172.1749 ; https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n3-p07-p.pdf
- Toma, M. (2008). On the Kähler rank of compact complex surfaces. *Bulletin de la Société Mathématique de France, 136*(2), 243–260. https://doi.org/10.24033/bsmf.2556 ; https://www.numdam.org/item/10.24033/bsmf.2556.pdf

The attempted application fails without an extra argument: an elliptic component in a fibre of the resolved horizontal divisor can be contracted on the map to the possibly singular divisor H. Exceptional elliptic curves can occur in resolutions of Gorenstein surface singularities. The remaining image in H intersect S can therefore consist of rational curves. It is not legitimate to assert survival of an elliptic component merely because the general curve is elliptic. Both the E and D agents identified and retained this gap.

## 7. Additional restrictions and failed shortcuts

- A nonzero effective antipluricanonical divisor on a surface with torsion canonical line is impossible; thus the horizontal obstruction lies in the non-torsion canonical case.
- The higher-degree local invariant-cycle assertion is unavailable in this non-Kähler setting. The Kodaira example above already illustrates a failed higher-degree comparison, so it cannot be used to force normalization cohomology.
- In diagonal nonresonant Hopf coordinates, multiplicities of the two anticanonical curves can impose divisibility conditions on the fractional root. Resonant non-diagonal cases have variable multiplicity and defeat that simple arithmetic exclusion. No uniform arithmetic obstruction is asserted.
- Standard classifications of semistable degenerations of two-dimensional tori impose Kähler or related hypotheses on the total degeneration. The actual limiting pencil divisor lies in a non-Kähler total family; no such hypothesis has been proved. Those classifications are not applied.
- A globally paired self-pinching conductor model retains a dual-circle fundamental-group quotient. That rules out that particular way of killing the Hopf fundamental group, but it is not a classification of arbitrary irreducible nonnormal fibres.

## 8. Exact primary inputs for E.2.8

Fujino, O. (2021). Minimal model theory for log surfaces in Fujiki's class C. *Nagoya Mathematical Journal, 244*, 256–282. https://doi.org/10.1017/nmj.2020.14

Opened publisher full text: Definition3.1, Remark3.2, Lemma3.3 and Corollary3.4. These identify compact normal class-C surfaces with those having a Kähler resolution; they also include Moishezon surfaces. The main minimal-model theorems are not used.

Barth, W. P., Hulek, K., Peters, C. A. M., & Van de Ven, A. (2004). *Compact complex surfaces* (2nd ed.). Springer. https://doi.org/10.1007/978-3-642-57739-0

Opened publisher metadata and the official two-page ChapterVI preview, pp.243–244, including Theorem1.1 and Table10: https://page-one.springer.com/pdf/preview/10.1007/978-3-642-57739-0_7 . These suffice for the non-Kähler Kodaira-dimension-minus-infinity implication b1=1. The remainder of the book was not represented as opened. Peters (2021), Theorem2.2, p.843, was independently opened as another published formulation of that classification table, but is not an extra theorem needed by E.2.8.

## 9. Search record and remaining goal

The searches on 15 November 2026 used both search engines and included: CDP2020 Hopf case and nonnormal differential torsion; Hopf degenerations with irreducible centre; fixed contraction trace and determinant; isotrivial Hopf completions; Kähler and Moishezon central-fibre hypotheses; non-Kähler local invariant cycles; effective flat divisors on class VII and Enoki surfaces; and degenerations of tori without a Kähler total-space hypothesis. Access metadata, primary URLs, and failed openings are retained in evidence/E_hopf_search_log.json. No claim of exhaustive literature coverage is made.

At the end of the classification attempts, the unresolved step was exclusion or classification of an irreducible singular fibre with non-Kähler normalization in the presence of the actual horizontal fixed divisor. Section10 resolves the fixed-divisor problem without that classification. Uniqueness of an interior smooth period completion and loss of fractional canonical sections on a different deformation branch remain independent E.2.4 gaps.

## 10. Subsequent resolution by horizontal twisting and Picard variation

E.2.9 observes that a horizontal divisor meeting every irreducible reduced fibre supplies a uniform vanishing argument. Negative twists kill sections of any vector bundle on each reduced fibre by descending finite-dimensional spaces, Krull intersection and analytic continuation. The finite O_S(−jS) filtration handles every thickened fibre mS. Compactness of P1 makes the fibrewise bound uniform; Gorenstein duality and constant-zero base change then give R2f_*B(NH)=0. A positive twist from P1 kills global H2 and H3. A separate negative H twist kills H0 on X. Because Pic(X)=H1(O_X) additively, a holomorphic affine line through these two Picard classes makes all three vanishings simultaneous outside finitely many proper analytic jumping loci. For B=TX this contradicts HRR chi(TX)=c3/2=1.

The proof uses the exact proper finite-complex and base-change statements of Bănică–Stănăşilă already opened in E.3.1, and the compact complete-intersection duality of Ramis–Ruget already audited there. It neither imports CDP2020 Theorem2.2 nor relies on the corrected generic exceptional-locus assertion of Grauert1960. The exact HRR polynomial check is saved in code/e_push_horizontal_vanishing.py, with its .out and .json; that computation verifies only the polynomial, not the analytic proof.

For the negative-slope fixed divisor, E.2.8 first forces irreducibility, and E.2.9 then excludes the hypothetical horizontal component. The connected-divisor-limit argument of E.2.6 now applies for either sign. E.2.10 therefore proves E0=0, target degree1, a proper flat relative intrinsic pencil, a general central torus fibre, an interior limiting period, and exclusion of a common smooth limit for two distinct multiplicity pairs. Interior-completion uniqueness and passage through a new deformation branch remain Open. The independent D referee is sections/D_E229_E2210_referee.md; the parent also read and passed the complete source.
