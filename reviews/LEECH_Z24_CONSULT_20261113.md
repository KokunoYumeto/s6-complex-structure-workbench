# Consult, 13 Nov 2026: is H_2(Delta_{0,6}) = Z^24 related to the Leech and Niemeier lattices?

By the S6 survey agent (Claude Fable 5.2). Answer to `LEECH_Z24_QUESTION_20261113.md`.

**Limits of this answer.** A context guard stopped all file reading and all commands before I could re-open the
workbench files. So: (1) every argument below is by hand, with no program run today; (2) the workbench quotations
are from my reading of 12 November and from reader D1's and D2's notes, with the locators recorded then, not
re-verified today. Verbatim quotes are marked "verbatim"; the rest is paraphrase. Notation: L = H_2(Delta_{0,6}; Z)
with the form induced from Z^105; chi its S_6-character; c a 6-cycle.

## 1. What comes out, in short

1. **The Coxeter-number route does land on a Niemeier root system, but on A_4^6 (h = 5), not on the h = 6 lattices.**
   Restricted to the stabilizer S_5 of a leaf, L (x) Q is isomorphic to (A_4 (x) Q) (x) Q[P^1(F_5)] = A_4^6 (x) Q,
   where S_5 acts on each A_4 as its Weyl group and permutes the six copies as PGL_2(5) acts on P^1(F_5).
   Proved below by characters (section 2, P5). A_4^6 is the root system of the Niemeier lattice with Coxeter
   number 5, and PGL_2(5) is its glue group G_2.
2. **For the full S_6 there is no such lattice.** No even unimodular lattice of rank 24 (Leech or any of the 23 with
   roots) admits S_6 acting by isometries with character chi. Proved below (P4), using closed route (a) for Leech.
3. **With the form induced from Z^105 there is no gluing in either direction.** det L = 13 times a square, so
   L (x) Q is not similar to the rational space of any even unimodular lattice (P2).
4. **24 = b_3(M_{0,6}) is the same 24** (P1).

## 2. Proved (by hand; to be machine-checked)

**P1. H_2(Delta_{0,6}; Q) = H^3(M_{0,6}; Q)^dual, S_6-equivariantly.** The reduced homology of the boundary complex
of a normal-crossings compactification is the weight-zero part of compactly supported cohomology:
H~_{i-1}(Delta) = W_0 H^i_c (Deligne; Payne, "Boundary complexes and weight filtrations"). H^3(M_{0,6}) is pure of
Tate type (3,3) (arrangement complement), so H^3_c = (H^3)^dual(-3) has weight 0 entirely. Hence rank 24 on both
sides is one fact. Status: known theorems applied; signs and the integral statement not checked.

**P2. No gluing with the induced form.** det L = 5^8 * 11^10 * 13^5 = 13 * (square). (i) An overlattice of index k
has determinant det L / k^2, so L has no unimodular overlattice. (ii) Two lattices of full rank in one rational
quadratic space have determinants differing by a rational square, and rescaling a rank-24 form by m multiplies the
determinant by m^24. Every even unimodular lattice has determinant 1. So L is not isometric to a finite-index
sublattice or overlattice of sqrt(m) N for any Niemeier or Leech lattice N and any rational m. That the primes
5, 11, 13 divide |Co_0| gives no gluing. This is for the induced form only: the S_6-invariant forms are a
3-parameter family (a_1, a_2, a_3 on the pieces of dimension 10, 5, 9), and the discriminant class changes by
a_2 * a_3, so other invariant forms have square discriminant. They are covered by P4.

**P3. Frame shape of the Coxeter element on L.** From chi(c) = 1, chi(c^2) = 3, chi(c^3) = -8, chi(1) = 24:
Frame shape 1 * 2 * 6^5 / 3^3, characteristic polynomial Phi_1^4 Phi_2^6 Phi_3^2 Phi_6^5.
- Coxeter element of N(A_5^4 D_4): Frame 2 * 6^5 / (1^5 * 3), polynomial Phi_2^6 Phi_3^4 Phi_6^5 (traces -5, -3, -8).
  It shares Phi_2^6 Phi_6^5 with ours (the 16-dimensional part where c^3 = -1) and the value -8 at c^3; it differs
  by Phi_3^2 against Phi_1^4. Not equal: refuted.
- Coxeter element of N(D_4^6): Frame 2^6 * 6^6 / (1^6 * 3^6), traces -6, 6, -24. Refuted.
- The workbench's "residue six-cycle" on N(A_5^4 D_4) (the coordinate 6-cycle C on each A_5 block, identity on D_4):
  Frame 6^4 * 1^4 / 1^4 = Phi_1^4 Phi_2^4 Phi_3^4 Phi_6^4, traces 0, 0, 0. Its fixed lattice has rank 4 (the D_4),
  and our c also has a fixed space of dimension 4, but the characters differ. Refuted as an equivariant match.
- 1 * 2 * 6^5 / 3^3 is not a Frame shape of Co_0, because its square has trace 3 (closed route (a)).

**P4. No even unimodular lattice of rank 24 carries S_6 with character chi.**
- Leech: closed route (a). I confirm the order-3 Frame shapes of Co_0 from memory of Kondo's table: 3^12/1^12,
  1^6 3^6, 3^9/1^3, 3^8, traces -12, 6, -3, 0. Check: GAP, `CharacterTable("2.Co1")`, the degree-24 character on
  the classes of element order 3.
- Lemma A (order 5). For g of order 5 in O(N), trace(g) is the sum over the g-fixed components of the trace on
  that component, and a component of type A_1, A_2, A_3 or D_4 has no automorphism of order 5, so it contributes
  its rank. Hence trace >= 4 > -1 whenever no fixed component is of type A_n (n >= 4), D_n (n >= 5) or E.
  This excludes A_1^24, A_2^12, A_3^8, D_4^6 (route (b) is this lemma).
- Lemma B (A_6 fixes the components). A_6 is simple, so it permutes the components trivially unless N has at least
  six isomorphic components and A_6 embeds in G_2; that happens only for A_1^24, A_2^12, D_4^6, excluded by
  Lemma A. In all other N, A_6 fixes each component, and chi restricted to A_6 is 10 + 5 + 9 (three distinct
  irreducibles), so the 10 lies in one component C. Type A_n: A_6 maps to S_{n+1}; the subgroups of A_6 of index
  at most 25 are A_6, A_5 (two classes), 3^2:4, S_4 (two classes), 3^2:2, with permutation characters 1, 1+5,
  1+9, 1+5+9, 1+5+5+9; none contains the 10. Type D_n: signed permutations; the 10 occurs only in the induction of
  the sign of S_4 (degree 15) and of the sign character of 3^2:2 (degree 20), so n >= 15. Type E: rank at most 8.
  Type D_4: no element of order 5. So N is D_24 or D_16 E_8 (route (c) is a case of this lemma).
- D_16 E_8: S_6 fixes both components and no sub-sum of 10, 5, 9 equals 8. Excluded.
- D_24: O(N) is signed permutations of 24 coordinates, so chi is a sum of inductions of sign characters from
  subgroups whose indices add up to 24. chi is multiplicity-free with constituents 10, 5, 9, so each orbit has
  size in {5, 9, 10, 14, 15, 19, 24}; S_6 has subgroups of index 10 and 15 but none of index 5, 9, 14, 19 or 24
  (no subgroup of order 30), and 24 is neither 10 + 14 nor 15 + 9 with admissible parts. Excluded.

**P5. The leaf stabilizer and A_4^6.** Res_{S_5} chi has values 24 at 1, -1 at the 5-cycles and 0 elsewhere (read
off the given table). That is Ind_{C_5}^{S_5}(zeta) for a primitive character zeta of C_5 = <5-cycle>.
C_5 is generated by a Coxeter element of W(A_4) = S_5 and zeta = e^{2 pi i / h}, h = 5. Since
Ind_{C_5}^{F_20}(zeta) = Q(zeta_5) = A_4 (x) Q as a module for F_20 = N(C_5), and S_5/F_20 = P^1(F_5) (six points,
the six Sylow 5-subgroups): Ind_{C_5}^{S_5}(zeta) = V(4,1) (x) Q[S_5/F_20]. So
Res_{S_5}(L (x) Q) = (A_4 (x) Q) (x) Q[P^1(F_5)]: six copies of the A_4 root lattice, permuted by S_5 = PGL_2(5)
and each acted on by its Weyl group. The same holds after twisting the permutation of the six copies by any sign
character of F_20, because the twist is trivial on C_5.
What this is: the 24 of L is 6 * 4 = (number of Sylow 5-subgroups of S_5) * rank(A_4), and the six objects are
the six points that the outer automorphism of S_6 produces from five. The transitive S_5 inside S_6 is the image
of the leaf stabilizer under that outer automorphism; consistently, the 5-dimensional piece V(3,3) of chi is the
A_5 root-lattice representation V(5,1) twisted by the outer automorphism and by the sign.

## 3. Statements still to test, each with its computation

**T1 (N(A_4^6) as an S_5-lattice in L (x) Q).** The glue code of N(A_4^6) is generated by [1 (0 1 4 4 1)] and its
cyclic shifts over Z/5 (Conway-Sloane, Table 16.1); its group is G_1.G_2 = 2.PGL_2(5), acting by signed
permutations. Statement: this extension splits, i.e. there is a homomorphism s: S_5 -> {+-1} wr S_6 lifting
PGL_2(5) and preserving the code. If so, g -> (Weyl element g on every component) * s(g) is an embedding of S_5 in
O(N(A_4^6)) whose character is Res_{S_5} chi, by P5. Computation: list the 240 signed permutations preserving the
code and test for a complement to +-1 (a few lines of GAP or Python). If it does not split, the statement holds for
A_5 = PSL_2(5) at least; test that.

**T2 (which invariant forms).** Hom_{S_5}(A_4^6 (x) Q, L (x) Q) has dimension 5 (the norm of Res chi). Compute it
from `delta06_lattice.py`, pull back the 3-parameter family of S_6-invariant forms, and decide whether some member
restricts to a multiple of the root form of A_4^6, and whether the image of N(A_4^6) is then an integral lattice
containing or contained in L. With the induced form itself the answer is no, by P2.

**T3 (Leech with S_5).** Statement: Co_0 has a subgroup S_5 whose 5-elements have Frame shape 5^5/1 (trace -1) and
all of whose other non-identity elements have trace 0 (Frame shapes 2^12, 3^8, 4^6, 6^4). Traces alone do not
exclude it. Computation: GAP, `PossibleClassFusions(CharacterTable("S5"), CharacterTable("2.Co1"))`, keep the
fusions on which the degree-24 character restricts to (24,0,0,0,0,-1,0); if one survives, search the maximal
subgroups containing 5C elements. The S_5 of T1 does not pass to the Leech neighbour of N(A_4^6) by the holy
construction, because its Weyl elements move the Weyl vector rho; the subgroup fixing rho (the standard complement)
has 5-elements of trace 4.

**T4 (the three isotypic sublattices).** Compute L_10, L_5, L_9 = L cap (isotypic part), their Gram matrices,
determinants and the index of their sum in L; this says where 5, 11, 13 come from. Statement to test: L_5 is
similar to one of the four S_6-invariant lattices between A_5 and A_5^* (with S_6 acting through outer automorphism
times sign), and L_10 to an invariant lattice in Lambda^2(A_5).

**T5 (the holy construction with rho/h).** As stated it does not apply to L: L has no roots (minimum 14), so it
has no Weyl vector and no Coxeter number. What can be tested is the neighbour of the lattice produced by T1/T2:
for N(A_4^6), h = 5 is prime, so the only neighbour along rho/d is d = 5, the Leech lattice.

## 4. What the workbench files say (locators from the 12 November reading)

- `27_s6_key_advances_frozen_2026-09-06.tex`, section 4, l. 199-212, verbatim: "Start with the marked root lattice
  $R=A_5^{\perp4}\perp D_4$ and its Niemeier overlattice $N$, with $[N:R]=72$. Its rank is $24$; $72$ is the glue
  index, not a dimension." and "K=\{x\in N:(\rho_N,x)\equiv0\pmod6\}, \Le=K+\Z(\rho_N/6-\alpha)" and "The fourth
  extension $M$, fixed by this action, has root system $A_2^{12}$ and $72$ roots." This is the holy construction
  with rho/h for h = 6.
- `workbench\README.md`, verbatim: "It proves the index-72 `A5^4 D4` glue, full splitting
  `O(N)=W(A5^4 D4) semidirect L(GL2(F3))`, the Weyl position of the commuting residue six-cycle, marked
  flag-weight maps, and exact shell and finite-sample count maps. The abstract quotient is credited to
  Cheng–Duncan–Harvey, Table 3." Source: `es_niemeier_shared.tex`, `esn:fa:thm:full-quotient`,
  `esn:fa:thm:residue-weyl` (reader D1: l. 682-921 and 1616-1868).
- `ledgers\literature_sources.md`, verbatim: "proves that the residue six-cycle belongs to the Weyl group and
  centralizes that chosen section."
- `es_niemeier_residue_fixed_neighbor.tex`, `esrf:thm:common-J`, l. 313-346 (reader D1's transcription of the
  statement): r = C^2 on each A_5 block (coordinate shift by 2), identity on D_4; r in W(N), r^3 = 1; the three
  Leech lattices Lambda_j = {x + k sigma_j/6 : x in N, (sigma_j, x) + k = 0 mod 6}, sigma_j = r^j rho. So the
  workbench's six-cycle C is a Coxeter element of each W(A_5) = S_6 block: the same group and the same element as
  ours, in a different 24-dimensional representation (P3).
- Reader D1's computation (notes D1-13, item 2; not in the workbench): the d-neighbour of N(A_5^4 D_4) along its
  Weyl vector is A_2^12 for d = 2, A_1^24 for d = 3 and Leech for d = 6.
- `erdos_straus_koide_s6_bridge.tex` and `s6_erdos_straus_koide_bridge_preprint.tex` (workbench README, verbatim:
  "the marked selector/terminal bijection and the shared modulo-840 lattice, full Weyl quotient and
  prime-dependent shell maps"): the 24 there is the number of residue classes r = 1 mod 24 modulo 840, from which
  N(A_5^4 D_4) is built (reader D1; file lines not re-opened). I know of no S_6-action on those 24 classes in the
  file; whether the 24 classes carry chi under some action is not addressed there.
- `koide_arithmetic_preprint.tex` and `koide_*.tex` (reader D2): the form a^2 - 3q^2 - 18n^2, ideals of Z[sqrt 3],
  the quaternion order of reduced discriminant 108. I recall no rank-24 lattice and no Coxeter number in it, and
  the primes 5, 11, 13 do not occur; I could not re-open it to confirm.

## 5. Order of work

T1 first (minutes; it decides whether N(A_4^6) sits S_5-equivariantly in the rational space of L), then T4 and T2
with the existing script, then T3 in GAP. P4 should be re-run by machine on the 23 lattices before it is quoted.
