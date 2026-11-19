# Fresh derivation of the displayed order-two translation in P1A.4

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Only the clean `analysis/continuation_V/P1A4_statement_input_packet.md` has been read. P1A.4's printed proof, including step5, remains unread. The requested representative is tau=w/2 with w=(0,1,1,1,1,1)^t in the supplied integral homology marking.

## Holomorphic translation and exact finite-chart compatibility

On the simply connected smooth base cover, the flat vector tau is a holomorphic section of the complexified flat bundle. Evaluation on the holomorphic three-plane F gives a holomorphic section of F^dual, and quotient by the supplied integral lattice gives a translation of the actual torus family. The admissible condition F∩bar(F)=0 says that the evaluation map from Lambda_R to F^dual is a real-linear isomorphism. Thus tau is nonzero modulo that lattice and has exact order two, since w is integral and tau is not integral.

Direct multiplication of the supplied matrices gives

(M1−I)tau=(0,3,−1,−3,0,0)^t,

(M2−I)tau=(0,0,−3,0,0,0)^t.

Both differences belong to Lambda. Therefore the translation section is invariant under both marked monodromies, and hence under their generated group. On a finite root chart the translation map T_tau(t,x)=(t,x+tau) commutes with the given affine deck map d_i(t,x)=(zeta_m t,M_i x+v_i/m): their fibre coordinates differ exactly by tau−M_i tau∈Lambda. The affine v_i/m terms cancel in this equality; none is omitted or changed. T_tau is holomorphic throughout the smooth root family, including its central torus, and descends through the actual free finite quotient. The same calculation makes the translations agree on every prescribed affine gluing overlap.

## Actual cusp marking and toric-chart extension

Put u=(1,1,1,0,0,0)^t/2 in the supplied cusp marking S. Direct multiplication gives

S u−tau=(0,0,0,−1,0,−1)^t∈Lambda.

Thus the same translation point is represented in cusp coordinates by u: its period-coordinate part is zero, and its three additive coordinates are (1/2,1/2,1/2). In the prescribed multiplicative coordinates x_j=exp(2pi i z_j), its actual map is

(x1,x2,x3,q)↦(−x1,−x2,−x3,q).

Here is the extension on every chart, without replacing the fan. A maximal cone has the four supplied height-one lattice generators n_i=(p_i,1), with integer unimodular matrix N having those columns. Let m_i be the rows of N^{-1}; the toric chart coordinates are z_i=chi^{m_i}. The torus element g=(−1,−1,−1,1) therefore acts by

z_i↦chi^{m_i}(g)z_i,

where each coefficient is the explicit sign (−1)^{m_i1+m_i2+m_i3}. It is an invertible holomorphic diagonal coordinate map on the full affine chart. The sum of the four m_i is the base character (0,0,0,1), because every n_i has height one. Consequently the product of the signs is one, and q=product_i z_i is preserved. On a monomial overlap the signs transform by exactly the same integer character matrix as the coordinates; hence the maps agree on the overlap. This produces an automorphism of the specified toric union itself and does not require a permutation or replacement of any cone.

For every period deck transformation (x,q)↦(exp(2pi i C(q)nu)q^nu x,q), the displayed sign multiplication commutes with it coordinate by coordinate. It therefore descends to the actual analytic quotient used in the compact cusp filling. Its restriction on the punctured cusp is the evaluation translation tau already identified through S, so the cusp and finite-chart extensions glue to the same compact-family automorphism.

Every local map squares to the identity. Its restriction to a smooth torus fibre is the nonzero point tau, so its global order is exactly two. This establishes the requested representative on the whole compact family, without using the group computation or splitting conclusion of P1A.4.

## Fresh arithmetic certificate

`code/continuation_VI/P1A4_tau_fresh.py` is newly authored from the packet. It checks both integral differences, the exact S-marking equality, unimodularity, all six fundamental Kuhn charts and their thirty-six character-transition identities. The universal chart and deck-commutation arguments are the written ones above; the finite calculation checks their supplied integral data.
