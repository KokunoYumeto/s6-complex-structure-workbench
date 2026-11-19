# Fresh Chern-root derivation for Paper V P1A.2

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

This full derivation is written before reading P1A.2 or its proof, and before opening the cited Esole–Kang polynomial. Only the requested data have been supplied: M is a compact complex fourfold, c1=c3=0, the characteristic numbers c2²=2 and c4=6, and the requested quantity is χ(M,Ω_M²). The input theorem is Hirzebruch–Riemann–Roch in its compact-complex form, χ(M,E)=∫_M ch(E)Td(T_M). No claim concerning the other parts of P1A.2 is made here.

## The actual bundle expression

Pull T_M to its full flag bundle. The projective-bundle theorem makes the pullback on rational cohomology injective. Its filtration has line-bundle quotients with first Chern classes x1,…,x4. Exterior powers of the dual filtration have quotients L_i^*⊗L_j^*, i<j. Additivity and multiplicativity of the Chern character therefore give

ch(Ω_M²)=Σ_{i<j} exp(−x_i−x_j).

These equalities of symmetric polynomials descend through the injective pullback, so the formal root calculation computes the given cotangent exterior square itself. Put p_k=Σ_i x_i^k. The elementary-symmetric identities with c1=0 give p1=0, p2=−2c2, and p4=2c2²−4c4. The six pair sums occur in opposite complementary pairs because Σ_i x_i=0. Hence their odd powers sum to zero.

The constant term of the Chern character is six. The degree-two term is

(1/2)Σ_{i<j}(x_i+x_j)²=(1/2)(3p2+2c2)=−2c2.

For the degree-four term, the pure fourth powers contribute 3p4, the 3+1 terms contribute 4Σ_{i≠j}x_i³x_j=4(p3p1−p4)=−4p4, and the 2+2 terms contribute 6Σ_{i<j}x_i²x_j²=3(p2²−p4). Their sum is 3p2²−4p4=4c2²+16c4. Dividing by 4! gives

ch_4(Ω_M²)=(c2²+4c4)/6.

## Todd class, derived from its defining series

The defining root factor is Q(x)=x/(1−exp(−x))=exp(x/2)(x/2)/sinh(x/2). Since sinh(x/2)/(x/2)=1+x²/24+x⁴/1920+O(x⁶), taking the reciprocal and logarithm gives

log Q(x)=x/2−x²/24+x⁴/2880+O(x⁶).

Summing over the roots and exponentiating, with p1=0, yields Td_2=−p2/24=c2/12 and

Td_4=p4/2880+p2²/1152=(3c2²−c4)/720.

The odd Todd terms needed here vanish. Thus the top-degree HRR integrand is

6(3c2²−c4)/720+(−2c2)(c2/12)+(c2²+4c4)/6

= (18c2²−6c4−120c2²+120c2²+480c4)/720

= (3c2²+79c4)/120.

At the supplied characteristic numbers this is (3·2+79·6)/120=480/120=4. In fact the calculation only needs c1=0; the additional stated c3=0 hypothesis is compatible and is not used to discard an otherwise surviving term.

## Exposure boundary

The universal polynomial, all root sums, the Todd expansion and the final substitution above were written before opening either the target proof or Esole–Kang equation(1.2). A separately authored polynomial computation and the later primary-source comparison will be recorded after this file is committed. They will not be described as preceding this derivation.

## Subsequent source comparison and computation allocation

After the derivation was committed, the full primary Esole–Kang v1 text in `analysis/V/references_build/EsoleKang_v1.txt` was opened at equation(1.2), printed p.3. Its full expression is (79c4−19c1c3+3c2²+4c1²c2−c1⁴)/120. Setting c1=0 agrees exactly with the polynomial independently derived above. The target P1A.2 proof remains unread by this reviewer at this point.

Root then reported that the ledger reviewer had independently completed this same derivation and eleven exact computations before reading the target proof. The redundant long-running symbolic computation started by this reviewer was stopped, and its unfinished program was removed. This reviewer claims the written derivation and primary-source comparison only; the successful fresh computational evidence is the ledger reviewer's separate receipt.
