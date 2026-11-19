# Recheck of S6_02_PUSH Lemma A.3.1 and Theorem A.3.2 against Engel's Conjecture 8.2 (19 Nov 2026)

**Who.** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8 (the agent of the S6_06_BLIND intake and the gap-4 check), at the main session's word, as the last gate before the outreach mail to Philip Engel. Check events: `ENGEL_A31_A32_RECHECK_20261119_CHECK_EVENTS.tsv` beside this note.

**Sources.**
- S6_02_PUSH final: `returns/S6_02_PUSH_final_20261115T2217Z_unzipped/S6_02_PUSH/sections/AB_push.tex`, §A.3 (Lemma A.3.1, Theorem A.3.2; p. 12 of the paper PDF), with the set-up of §A.1 (L = O_S(P − O), J = L ⊗ T*L^{-1} = π*O_B(1), R = P_S(O ⊕ L), Q = R/(s₀(x) ~ s_∞(Tx)), T = t_{6P}). The run is by GPT-6 Astra (ChatGPT Pro mode).
- S6_06_BLIND P2.10-P2.11: `returns/S6_06_BLIND_checkpoint_36_20261118T1547Z_unzipped/`; the proof is in `notes/part2.tex` of its checkpoint 21 (nested), ll. 286-312. The run is by GPT-6 Astra (ChatGPT Pro mode).
- P. Engel, "Complex structures on S^6", arXiv:2609.38442v1. The e-print was downloaded into a new empty folder (my scratchpad, `engel_2609.38442v1_src/`; `S6.tex`, dated 29 Sep 2026).
- B. Fantechi and L. Göttsche, "Riemann-Roch theorems and elliptic genus for virtually smooth schemes", arXiv:0706.0988 (the e-print, `virtualRR16.tex` of 7 Jun 2007, downloaded into a new empty folder); published in Geom. Topol. 14 (2010).

## Verdict

**A.3.1 and A.3.2 hold.** e_vir(Q) = 0 and e(X(u)) = 2, so no proper flat filling of the untwisted family has central fibre Q. This refutes Conjecture 8.2 for the central fibre Engel describes. One point of wording, below, matters for the mail.

1. **The general statement (A.3.1) is right and known in the algebraic case.**
   - Fantechi-Göttsche prove it for algebraic families: the theorem labelled `FultonChern` (Theorem 4.19 in the arXiv source; S6_02 cites the published numbering, Theorem 5.8 and Remark 5.9, which I did not check). It reads: for a proper lci scheme X, e^vir(X) = deg c_F(X) = ∫ c_d(T_X^vir); this number is invariant under lci deformations, and it equals e(X₀) for a smoothing X₀. Their proof rests on Fulton, *Intersection theory*, Ex. 4.2.6.
   - Engel's X(u) are not algebraic (algebraic dimension 1), so the analytic version is needed. S6_02's proof gives it:
     - flatness keeps the family relatively lci near Z, by lifting a regular sequence (Nakayama);
     - the perfect relative cotangent complex gives a topological K-class that restricts to T_{X_t} and to T_Z^vir;
     - [X_t] − [Z] bounds the preimage of a radial segment, and the singular set has real codimension 2;
     - Gauss-Bonnet holds on the smooth fibre.
   - I checked each step. S6_06_BLIND's P2.11 gives the same argument independently.
2. **The computation for Q.** I re-derived it in general.
   - Locally Q is xy = 0. On the branch Y = {x = 0} with double divisor D, T_M|_Y − O(Q)|_Y = T_Y + A − A(D), where A = N_{Y/M}. In K-theory, A − A(D) = −[A(D)|_D], and A(D)|_D = N_{D/Y} ⊗ N_{D/Y'} = T¹_Q.
   - So ν*T_Q^vir = T_R − i_{0*}T¹ − i_{∞*}T¹, which is S6_02's formula, with T¹ = L ⊗ T*L^{-1} = J.
   - Expanding the Chern class with an extension of T¹ of class ε, and writing t = ε|_D = c₁(T¹), the correction from both branches is −2c₂(S) + c₁(S)·t − t².
   - Hence e_vir(Q) = e(R) − 2e(S) + ∫_S (c₁(S)·t − t²). This is S6_06's formula. S6_02's form is the case j² = 0 on R, where the t² term vanishes; the two forms agree.
   - For Q: e(R) = 2·e(S) = 24 (S is the rational elliptic surface, e(S) = 12); the two sections give 12 + 12; and t = c₁(J) = F with c₁(S) = −K_S = F and F² = 0, so the last term is F·F − F² = 0. Thus **e_vir(Q) = 24 − (12 + 12) + 0 = 0**.
   - Cross-check by nearby cycles: a smoothing xy = uφ with φ ∈ H⁰(J) has nearby Euler number e(R) − 2e(S) + e(C), where C = {φ = 0} lies in the class t, and e(C) = c₁(S)·t − t² by adjunction. With C an elliptic fibre this is 0 again; it is S6_02's "direct check".
3. **e(X(u)) = 2.**
   - Engel proves χ_top(Y) = 2 for the twisted Y (Proposition 7.2, `euler-characteristic`). The same argument gives χ(X(u)) = 2 for the untwisted X(u).
   - Away from the cusp fibre, the circle in the C^*-scaling acts freely on X(u), as S6_02 shows: a scalar equal to an iterate of uφ is the identity. Those parts contribute 0.
   - The Mumford fibre over ∞ has exactly two zero-dimensional toric strata, and every other stratum contains a factor C^*. So the total is 2, and the logarithmic transforms at 0 and 1 do not change it.
4. **Conjecture 8.2 is quoted correctly.** Its number: §8 "Additional remarks", Remark 8.1, then Conjecture 8.2, with theorems numbered within sections. Its text (v1, S6.tex ll. 1673-1676):

   > There is a flat, proper filling 𝒳 → Δ and the central fiber X(0) is non-normal. The normalization is P_S(O ⊕ M) and the normalization map glues the zero and infinity sections via t_{6P}.

   It follows Engel's description of the limit (ll. 1668-1671): "Take the P¹-bundle P_S(O ⊕ M) and glue the zero section to the infinity section by t_{6P}." That glued space is S6_02's Q, with M = L.

## The point of wording, for the mail

- The literal statement fixes X(0)'s normalization and the identification its normalization map makes. It does not fix X(0)'s analytic structure along the glued surface.
- The refutation covers X(0) = Q, the normal-crossings gluing that Engel describes, which is lci.
- It does not cover a non-seminormal central fibre with the same normalization and the same identification, for example one whose two branches meet with higher contact. Such a fibre need not be lci; where it is lci, its virtual class differs. For contact k the transversal A_{2k−1} Milnor fibre has χ = 2 − 2k.
- So S6_02's "false as worded" should read, in the mail: **there is no flat proper filling whose central fibre is the space obtained by gluing the zero and infinity sections of P_S(O ⊕ M) by t_{6P}**, since that space has virtual Euler number 0 and X(u) has Euler number 2. The proper nodal filling of A.1.2 (S6_02) and S6_06_BLIND's P2.10 are fillings with other central fibres.
