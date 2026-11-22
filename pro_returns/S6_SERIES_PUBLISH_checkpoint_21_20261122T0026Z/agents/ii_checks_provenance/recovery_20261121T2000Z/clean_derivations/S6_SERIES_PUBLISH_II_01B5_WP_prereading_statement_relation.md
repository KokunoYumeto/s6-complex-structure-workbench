# Prereading statement relation: 01B5 / cdp:st:A.5.15 and 02WP / night:P4.18

This is an exact duplicate-scope/coordinate-transport derivation, not a proposed additional independent proof of the already admitted binomial exclusion. Both target proofs and their historical methods remain closed while this relation is written. The current statement-only files and receiver metadata were read. Their hidden StatementRecord citations are metadata; no cited proof or proof-internal formula was extracted. Root reports WP admitted as CLEAN05; no admission was reverified here.

## 1. Exact analytic coordinate map, including its inverse

Write h(x,y,z)=x^a−y^bz^c, with a≥2 and b,c≥1, and let f=u h^m with m≥1 and u a nonvanishing holomorphic germ. Put

    w_x=b+c,  w_y=w_z=a,  d=a(b+c).

The equality a w_x=b w_y+c w_z=d says that h is weighted homogeneous of degree d. On a sufficiently small simply connected ambient neighbourhood choose a holomorphic logarithm of u, hence a root v=u^(1/(md)) with v(0)=v₀≠0. Define

    Φ(x,y,z)=(v(x,y,z)^(b+c)x, v(x,y,z)^a y, v(x,y,z)^a z).

Direct substitution gives h∘Φ=v^d h and therefore

    (h^m)∘Φ=v^(md) h^m=u h^m=f.                        (1)

The derivative DΦ(0) is diagonal with nonzero diagonal entries v₀^(b+c),v₀^a,v₀^a, since the derivative of v is multiplied by x,y,z in the other terms. Here is also an explicit analytic inverse construction. For q=(X,Y,Z), solve the scalar equation

    τ^(md)=u(τ^(−b−c)X,τ^(−a)Y,τ^(−a)Z),  τ(0)=v₀.    (2)

At (q,τ)=(0,v₀) its derivative in τ is md·v₀^(md−1)≠0. The holomorphic implicit-function theorem therefore gives the unique germ τ(q) with this initial value. Set

    Ψ(X,Y,Z)=(τ(q)^(−b−c)X,τ(q)^(−a)Y,τ(q)^(−a)Z).

Equation (2) and the chosen branch imply v(Ψ(q))=τ(q), since both are md-th roots of the same unit with the same value at the origin. Thus Φ∘Ψ=id. Taking q=Φ(p), the germ v(p) solves (2); uniqueness gives τ(Φ(p))=v(p), and hence Ψ∘Φ=id. This proves both inverse identities, not only a formal change of leading terms.

The base coordinate in (1) is unchanged. On every sufficiently small nonzero level, Φ gives the actual local analytic isomorphism {f=t}→{h^m=t}; the m roots of t are retained. The map is only a change of the ambient coordinate chart, so it changes none of the global hypotheses on the given proper fibration. It does not require a global extension of Φ.

The polynomial h is reduced even when gcd(a,b,c)>1. Its distinct binomial factors in characteristic zero have no repeated factor: a repeated irreducible factor would divide h and its derivative a x^(a−1), hence divide x, but x does not divide h. Thus the reduced-germ hypothesis in WP is met for every exponent triple in B5.

## 2. Complete scope comparison

| Feature | Current B5 | Current WP exclusion | Exact transport |
|---|---|---|---|
| Total space | smooth complex threefold | smooth total threefold | identity on the given threefold; Φ is a local chart change |
| Base and map | proper holomorphic map to a smooth curve | proper holomorphic degeneration of two-tori | restrict the smooth curve to its coordinate disc; properness and smooth nearby torus fibres persist |
| Nearby fibres | complex two-tori | complex two-tori | unchanged given fibres; equation (1) compares the local fibre pieces |
| Exponents | a≥2,b,c,m≥1 | a≥2,b,c≥1 and common positive multiplicity | exactly the same integers |
| Reduced germ | x^a−y^bz^c | x^a−y^bz^c | reducedness proved above |
| Unit | arbitrary holomorphic unit u | equation specified as a reduced germ with common multiplicity | Φ and Ψ remove u from the full map, preserving m and the base coordinate |
| Compactness, Betti numbers, global irreducibility | no extra assumption | no extra assumption in the current explicit exclusion | none is introduced by any step of the coordinate construction |

The implication from WP's exclusion to B5 is equation (1) applied to every permitted u and m. The reverse implication between the exclusion clauses is the specialization u=1. Thus these exclusion clauses have the same mathematical domain and conclusion after the displayed analytic maps.

WP additionally asserts that the affine nearby fibre of the binomial polynomial contains a spherical class of nonzero square, and supplies a normalization/differential statement for a named example. Those additional assertions are retained WP content; they do not follow merely by restating B5's exclusion. No claim of equivalence of the entire WP statement with the shorter B5 statement is made.

## 3. Every named special case

* The pinch point is x²−y²z: a=2,b=2,c=1,m=1, and every positive m is included by the common-multiplicity clause.
* The family x²−y^(2k)z^(2r+1) has a=2,b=2k,c=2r+1 with k≥1,r≥0; these are exactly positive b,c in the stated range.
* The reducible germ x²−y²z² has a=b=c=2 and factors as (x−yz)(x+yz), with distinct reduced factors. Neither current exclusion imposes irreducibility of the reduced support.
* WP's x²−z³y⁴ is the same polynomial as x²−y⁴z³, with a=2,b=4,c=3, and is the k=2,r=1 case of B5's named family. Its additional smooth-normalization/divisorial-rank-drop assertion must remain in the retained WP content.

## 4. Receiver map and preserved identifiers

The all-five-current-source coded-reference scan is bound in the two incoming-use JSON files. It prints no receiving proof prose. The statement label has twenty coded occurrences: seven hidden StatementRecord occurrences, one preamble reference-binding declaration, one visible front/main-results occurrence, and eleven visible statement/proof occurrences across seven owning statements. The last thirteen count reported by the generic helper includes the one preamble binding; it must not be presented as thirteen printed uses.

The seven owning receivers are A.5.17, A.5.18, A.5.21, C.2.CR.4, C.2.UN.9, C.2.IRR.1 and C.2.RAT.1. Their exact complete statement-only files were read; their unrelated proofs remain closed. A.5.17 explicitly imports the full B5 hypotheses, so a retained owning statement must keep those hypotheses available at the B5 label rather than replacing them by a vague pointer. The other six receivers retain precisely the same exclusion domain because the statement relation above adds no hypotheses.

The A.J.33 equation label has three coded occurrences: one preamble reference binding, one occurrence in B5's own proof, and one following unowned body occurrence. The latter body context has not been read before the B5 freeze, so no claim about its proof or editorial disposition is made yet. These locations are retained for the postrelease complete-context review.

A consolidation must preserve at least the B5 tag01B5 and label cdp:st:A.5.15; equation tag0062, label cdp:eq:A.J.33 and its exact binomial/multiplicity domain; WP tag02WP and both night:P4.18/stmt:P4.18 labels; and every additional tag/label found when the two existing full blocks are eventually reconciled. The old event history remains unchanged. The retained mathematical owner must include the explicit B5 ambient/fibration hypotheses and equation, together with the stronger spherical-class and named normalization assertions already present in WP. Its single proof can then carry the exact unit map above. Location, dependency order and the final retired-owner representation are root's canonical integration decision after the full original-proof comparison.

## 5. Credit and current gate

This record establishes the exact statement relation before the B5 target proof is read. It is not a new independent check of the binomial exclusion, and contributes zero targeted/independent/computation events. No canonical source or ledger has been changed. The subsequent B5 full-proof comparison and precise consolidation guards remain pending; an eventual used-and-rechecked event can describe only an actually completed full comparison, never an independent re-proof inferred from this equivalence.
