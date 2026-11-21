# 033O — push:src:E.5.2 — derivation before opening the target argument

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build.
The statement packet has been read. An overbroad bibliography-key search displayed exactly the citation sentence identifying the input matrices with primary Proposition 4.2. Root explicitly permitted this source-locator-only metadata; the exact exposure is archived in S6_SERIES_PUBLISH_II_citation_search_exposure_2059.txt and its JSON receipt. No target matrix calculation, centralizer argument, or lattice argument has been read. The primary manuscript statements labelled mat and mum were then opened as cited inputs, without their proofs.

## Coordinate transport and exact matrix calculation

Let a cohomology column alpha and a dual homology column v pair by alpha^t v. Preservation of evaluation requires (T alpha)^t(H v)=alpha^t v for every alpha,v. Thus T^t H=I, giving exactly H=(T^{-1})^t. Conversely this formula makes the pairing identity hold. There is no tacit reuse of a cohomology matrix on ordinary dual homology.

The fresh standard-library Fraction program S6_SERIES_PUBLISH_II_033O_fresh_exact.py obtains

    H_* = [[1,0,0,0],[-2,0,-1,0],[0,1,0,0],[1,1,0,1]],
    H_1 = [[1,0,0,0],[0,1,0,0],[-2,-1,1,0],[-2,-1,0,1]],
    H_2 = [[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
    H_3 = [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]].

It verifies all four pairing identities, the prescribed ordered cohomology product T_* T_1 T_2 T_3=I, and H_*^4=I. All arithmetic is exact. The output file preserves every matrix and computed kernel.

## Centralizers

For an unknown 4 by 4 matrix X, form the 64 linear equations X H_i-H_i X=0, with its 16 entries ordered row by row. Exact Fraction row elimination has rank 14 and nullspace basis E_41,I. Both displayed matrices are also checked directly to commute with all H_i and are independent. Therefore every solution, and every element of the simultaneous rational homology centralizer, is a unique a I+b E_41. Repeating the same equation construction for the cohomology matrices gives E_14,I. This repetition independently checks the transpose transport; alternatively transposition is a bijection between commuting solutions after inversion of all monodromy matrices.

## Integral fixed lattices and norm

Write v=(a,b,c,d)^t in the named ordinary dual basis. The equations (H_*-I)v=0 are -2a-b-c=0, b-c=0, a+b=0. Their integral solutions are exactly (a,-a,-a,d), with arbitrary integers a,d. The map (a,d)->a ell+d delta-hat is therefore an isomorphism Z^2 -> Lambda^(H_*), with inverse v->(v_1,v_4).

The exact norm matrix I+H_*+H_*^2+H_*^3 is

    [[4,0,0,0],[-4,0,0,0],[-4,0,0,0],[0,2,-2,4]].

Its columns are 4 ell, 2 delta-hat, -2 delta-hat, 4 delta-hat. These columns generate exactly 4 Z ell + 2 Z delta-hat, since both stated generators occur as columns and the remaining columns are their integer multiples. The quotient isomorphism is explicitly

    [a ell+d delta-hat] -> (a mod 4,d mod 2),

with inverse represented by those same two basis vectors. Its kernel is precisely the norm image, proving the asserted Z/4 plus Z/2 without replacing an integral lattice calculation by its rational span.

At the three reduced fibres the exact differences give

    (H_1-I)v = -(2a+b)(w-hat+delta-hat),
    (H_2-I)v = c u-hat,
    (H_3-I)v = -b w-hat+a delta-hat.

Their images are respectively Z(w-hat+delta-hat), Z u-hat, and Z w-hat+Z delta-hat: in the first expression choose b=-1,a=0; in the second choose c=1; in the third choose b=-1 and a=1 separately. All are primitive, as their displayed generators extend to an integral basis. Their kernels are, respectively, a(psi-hat-2u-hat)+c w-hat+d delta-hat; a psi-hat+b u-hat+d delta-hat; and c w-hat+d delta-hat. These parameterizations give every integer solution and the exact inverse coordinate maps, proving all three invariant lattice claims.

## Identification with geometric vanishing cycles

The primary statement mum supplies the specialization maps for these specific reduced fillings: pi_1(F)->pi_1(W) is surjective, and H^q(W,Z)->H^q(F,Z) identifies with monodromy invariants for all q. In particular H^2(W,Z) is free, as a subgroup of H^2(F,Z). The integral universal coefficient exact sequence then gives torsion-free H_1(W,Z). The induced surjection s:H_1(F,Z)->H_1(W,Z) has dual s^*:H^1(W,Z)->H^1(F,Z) with image ker(T-I). Naturality of evaluation gives ker(s)=Ann(ker(T-I)): the converse follows because characters separate elements of the free group H_1(W,Z).

Over Q this annihilator is im((T-I)^t), which equals im(H-I), since H-I=-T^{-t}(T^t-I), and T^{-t} preserves that image. The explicitly computed integral images above are primitive; hence they equal the full integral annihilators. This identifies the geometric specialization kernels, not merely an abstract isomorphic lattice, with the three displayed K_i. Thus the use of the phrase primitive vanishing lattice is supported by the primary specialization morphism and its exact dual pairing.

Every claim of the statement has been derived. No old target program has been opened. The fresh code and its complete exact output will be frozen by hash with this derivation before the target argument is released.

## Immutable evidence bindings before freeze

- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_SX_033C_033O_primary_inputs.json — SHA256 `343d8f24b8129b9ba403c472618454a47f998cfa2f288c3f519c5864ee62a6ce`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_citation_search_exposure_2059.json — SHA256 `ce712d0d916420f6fed07b91273b88e69120efc25452ce8ec254d2bd9d1c04c9`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_citation_search_exposure_2059.txt — SHA256 `5f8128705845bb67c6374f42582d5297d774a9a8ed450ccea04370a3517c8e44`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_033O_fresh_exact.py — SHA256 `356d2663742eadb85339257f8f54e8fec6d8aaa787c3b1229cce8f9c870f1f72`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_033O_fresh_exact_output.json — SHA256 `085f502e425f62ccc8b7ed559659831dc75a4e2365c718b89b04dddc5dfc250a`.
