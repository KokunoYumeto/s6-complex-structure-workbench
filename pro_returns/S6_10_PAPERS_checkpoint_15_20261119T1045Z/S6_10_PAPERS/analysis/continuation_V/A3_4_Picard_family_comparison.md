# A.3.4: comparison of the isolated actual Picard-family restriction

The complete pretarget derivation was frozen at 10:31:48.164171 UTC in `A3_4_root_cover_before_read.md`. Its section F uses the supplied actual Picard family and writes the pullback/tensor family on the fixed smooth central surface. The isolated receiving paragraph was opened only afterward, during checkpoint15 source/record freeze.

The receiving expression is exactly

    E_B=(Omega^1_{U_c_prime} tensor p_c^*B)|_{S_c_prime}.

In section F let j be U_c_prime -> U_c -> Y, let i be S_c_prime -> U_c_prime, and set f=(j o i) x id_Pic(Y). The constructed family is pr_S^*(i^*Omega^1_Uprime) tensor f^*P. For the actual inclusion i_B:S_c_prime -> S_c_prime x Pic(Y), x -> (x,B), the identity f o i_B=(j o i, B) gives

    i_B^*(pr_S^*(i^*Omega^1_Uprime) tensor f^*P)
      = i^*Omega^1_Uprime tensor (j o i)^*B
      = (Omega^1_Uprime tensor p_c^*(B|U_c))|S_c_prime.

Thus the printed E_B is the restriction of exactly the family written before target reading, under identity maps on the fixed cover, surface and Picard parameter. The suffix c merely indexes the chosen fibre and does not change the morphism.

PASS for this geometric pullback/tensor-family assertion. The preceding receiving sentences about the exponential sequence and exponentiation of Cech cocycles belong to ledger's separately frozen proof; they were visible in this bounded excerpt but receive no new prereading credit from this note. This note does not claim the analytic finite-kernel argument, a fresh construction of the Picard family, or a whole-row re-proof. No numerical computation occurs. Registration remains staged until checkpoint15 release.
