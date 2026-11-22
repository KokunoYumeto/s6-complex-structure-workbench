# Independent prereading derivation: 01G4 / cdp:st:D.1.6

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build.
The root-separated manual packet SHA is f69dcf5b6ea5c858a2550bfb1334b29d1fd1556901267017249bdeb4171ff835. The mixed target statement/argument remains unopened. This derivation treats Wang's construction and its stated global homology as cited primary inputs and proves the deductions and all displayed matrix claims independently.

## Exact primary edition and construction inputs

The attached source order_two_rational_homology_sphere_new.tex has SHA1ae1686d7ebb4e538c0aee38adce5643b3e51fe955ed6796e0cfc61cc6cf9c29. Downloading arXiv2609.11541v2 source gave gzip SHA b4abc15ec39725226f6b2025680dc2124c646445ea81f5d12bb763a6ded1187c; its TeX member is byte-identical to the attached source. The arXiv submission history dates v2 to8 November2026,09:52:51UTC. Its20-page PDF has SHA e857b38a987b095ce2760ebed68f1b21bc37a7434e53e1e9a0683d5723ed766f. Primary-input receipt v2 SHA4d2893d5b849072d52adbe2a0157bbbeaeff717972f4002c3b6fed387244e0c6 records exact source offsets and full extracted statements. Failed web-tool arXiv opens are not used as evidence; the actual urllib downloads succeeded and are retained.

Actually read cited inputs: Theorem1.1p2 and Theorem3.1p8 give compact smooth simply connected X2(λ) and H0=H6=Z, H2=H3=Z/2, H1=H4=H5=0. Lemma2.6p4 gives the primitive exponent vectors (2,1) at0 and (1,0) atα+. Proposition2.7p4 gives the one-component rank-one fillings. Proposition2.8p6 gives the rank-two fibre with irreducible normalization dP6. Proposition2.10p7 gives the free logarithmic quotient and central fibre3B with B bielliptic. Proposition4.4, equation(20),p11 gives the four cohomology matrices in the exact manual-packet marking. The primary source period-basis definition and rank-one uniformization proof paragraphs were also read as external construction inputs; no II target proof was supplied or opened.

The primitive (2,1) direction is concrete: the monomial coordinate change (z,v)↦(x,y)=(v,v2/z) has inverse (x,y)↦(x2/y,x), an integral exponent matrix of determinant1. Its image valuation vector is (1,0). Thus the primitive period quotient has one lattice vertex in its period direction, consistent with the one-component assertion of Proposition2.7; an I2 fibre of the starting elliptic surface does not itself create two components in this explicitly transformed torus filling.

## Universal coefficient calculation

For cohomology with integer coefficients the universal coefficient sequence has terms Ext(H_{q-1},Z) and Hom(H_q,Z). At q=1, H0 is free and H1=0, so H1(X,Z)=0. At q=2, H1=0 and Hom(Z/2,Z)=0, so H2(X,Z)=0. The nonzero torsion H2(X,Z) in homology has therefore not been confused with degree-two cohomology: the explicit universal coefficient maps give the stated zero group. The rational b1 and b2 are zero as well.

## Integral monodromy, fixed classes and the exact dual map

Use the manual packet's ordered matrices B*,B2,B+,B− on V=H1(F,Z) in the primary cohomology marking (ψ,u,w,δ). Here H1 denotes cohomology in this paragraph; its dual Λ=Hom(V,Z) is the integral homology lattice. Evaluation is the perfect pairing α^t λ. Parallel transport preserving this pairing requires
(B_i α)^t(A_i λ)=α^tλ,
so B_i^t A_i=I and A_i=B_i^−t. This proves the precise coordinate transport used for homology, rather than merely relabelling the printed cohomology matrices.

The fresh exact program multiplies B*B2B+B− in the displayed order and obtains I4. It checks all four determinants are1 and B_i^tA_i=I4 with rational Gauss–Jordan inverses whose entries are integral. These are new calculations from the manual matrix data.

For v=(a,b,c,d)^t, (B−−I)v=(-d,c,0,0)^t. Thus a common fixed vector has c=d=0. Then (B+−I)v=(0,b,−b,0)^t forces b=0. Every B_i fixes e1, so the common integral fixed lattice is exactly Ze1; rational fixed dimension is one.

Let D_i=A_i−I and let M be the4×16 horizontal concatenation of these differences in the same order. Since B_i e1=e1, the first row of every A_i is e1^t; hence every column of M has first coordinate zero. The following exact columns generate every such vector:
- D− column1=e4;
- D− column2=−e3;
- D+ column2=−e2−e3.
Therefore e2=D− column2−D+ column2, e3=−D− column2, and e4=D− column1. The image of M is exactly Ze2⊕Ze3⊕Ze4, with no finite-index loss. The quotient map [v]↦v1 to Z has inverse n↦[ne1]. In particular the integral coinvariants are free of rank one. A unimodular minor formed from these columns has absolute determinant1; the program additionally computes the determinantal divisors(1,1,1,0), hence the Smith diagonal(1,1,1,0). This explicit basis-and-quotient proof supplies the integral result without relying on a Smith implementation.

Over Q, duality identifies the dual of the homology coinvariant space with the common fixed cohomology space: a functional on Λ factors through the quotient precisely when it annihilates all(A_i−I)Λ, equivalently B_i fixes it. The demonstrated integral maps already show both ranks are one. Thus t'=1.

## Fibre components and the corrected complement count

The primary construction has four exceptional base values∞,0,α+,α−. Their reductions have respectively one bielliptic component, one rank-one component, one rank-one component, and one component dominated birationally by the irreducible dP6 normalization. Consequently the total reduced component count is4. The multiplicity3 at∞ does not multiply the number of distinct irreducible components; the reduction map has the same underlying irreducible topological support.

The numerical identity can also be derived directly. On U_base=P1 minus these four values the fibration is a smooth proper torus bundle. The base retracts onto a bouquet of three circles and has π2=0. The fibre fundamental group injects, and the quotient is a free group of rank3, whose generator lifts supply a splitting. Abelianizing with the same explicit semidirect-product map as above gives
rank H1(U_total,Z)=3+rank Λ_π1(U_base)=3+1=4.
For D equal to the union of the four exceptional fibre supports, the long exact sequence of(X,D), rational Poincaré duality and b1(X)=b2(X)=0 give
H4(D,Q) ≅ H5(X,D;Q) ≅ H1(X\D;Q).
The last map is Lefschetz duality; these compact analytic sets are triangulable. The top homology H4(D,Q) has a basis of its four irreducible component classes, because singular and intersection sets have real dimension at most2. Its dimension therefore is r. This establishes r=4−1+t'=4 from the actual topology. Substituting the full four-dimensional fibre H1 instead produces4−1+4=7, whose mismatch is located in the exact coinvariant quotient already proved.

The separate coherent-direct-image receiver D.1.13 is not used as an input or conclusion here; no unreleased target argument from that statement was opened.

## Fresh computation and status

Fresh program SHA836a1e0b329113a2f155d076f2ad3caa6672e375ba0f06e139bc44090b8f3487; output SHA b9a03670ba017a155708650225b2c32a9e58b21ccfd2b7aae71b172b37a94c64. The method is standard-library Fraction elimination, explicit integral image witnesses, permutation determinants and gcds of minors. No old target program was read. The initial console-only serialization correction is preserved and predates this freeze. Every manual-packet conclusion has been derived; actual comparison with the embedded II proof begins only after this freeze. This document adds no event.
