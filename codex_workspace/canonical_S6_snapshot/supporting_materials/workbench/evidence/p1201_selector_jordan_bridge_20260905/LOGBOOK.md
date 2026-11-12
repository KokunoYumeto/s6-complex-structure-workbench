# Fifteen-selector/Jordan bridge audit logbook

## Assignment and boundary

Parent task: `/root`.

Bounded independent audit of the proposed relation between the complete
(p=1201) selector census and the real fifteen-dimensional Jordan algebra
(\operatorname{Herm}_3(\mathbb H)).  Required: recover the exact
selector-to-Koide rank-one map; embed it coefficient-wise in the quaternionic
model; compute ranks, spans, closures, markings, symmetries and incidence;
interpret precisely “fifteen directions each containing infinitely many
primes”; prove a bridge or a sharp obstruction.  No canonical or remote edits,
no Lean, no child agents.

All work is isolated in
`C:\Users\user\Documents\math\agent_work\fifteen_bridge_audit_20260905`.

## Sources read

1. Current user turn:
   `C:\Users\user\.codex\attachments\e89564a4-78b4-4db7-a72a-e8de950eb574\pasted-text.txt`.
   Its live-web statements were treated as unfinished claims, not premises.
2. Earlier partial audit:
   `agent_work\fifteen_selector_jordan_bridge_20260905`.
3. Complete canonical selector/Koide sources:
   - `output\s6_consolidated_canonical_2026-08-26\supporting_materials\workbench\research\erdos_straus_koide_s6_bridge.tex`;
   - `output\s6_consolidated_canonical_2026-08-26\supporting_materials\workbench\research\erdos_straus_selector_crosswalk.tex`;
   - `agent_work\koide_es_v3_intake_20260904_1307\koide_es_extension_v3_complete\background\Koide_ES_exact_crosswalk_background.tex`.
4. Exact quaternionic model:
   `output\geometric_unity_15d_bridge_20260904\chapters\model.tex`.
5. Latest independently checked (p=1201) propagation:
   - `C:\Users\user\Documents\Erdos Strauss and related\Erdos-Straus-Foundation\logbook\20260905_P1201_AFFINE_SELECTOR_FAMILIES.md`;
   - `...\certificates\verify_p1201_affine_selector_families.py`;
   - `...\certificates\p1201_affine_selector_families_results.json`.

## Corrections to the partial audit

The earlier partial script used one common family
(h_k=h_0+6Rk, p_k=1201+24rtRk).  That is a valid restricted family but not
the native or least hard-preserving family.  The exact channel-specific laws
are:

- exterior: (h_k=h_0+Rk, p_k=p_0+4rtRk);
- middle: (h_k=h_0+k, p_k=p_0+4rtk);
- after intersection with (p\equiv361\pmod{840}):
  (p_n=1201+L_sn), (h_n=h_0+L_s/(4rt)n), with
  (L_E=\operatorname{lcm}(4rtR,840)) and
  (L_M=\operatorname{lcm}(4rt,840)).

The new checker uses these exact formulas.

## Exact findings

1. Reconstructed from definitions: 15 marked oriented states, split (7E+8M),
   with 15 pairwise distinct primitive rays ([r:t]), 11 unordered denominator
   triples, 10 distinct hard-prime progressions, and 3 positive Koide
   orientations (E23a, M31a, M39a).
2. Every marked ray carries an infinite prime family by Dirichlet because its
   exact residue class is reduced.  “Fifteen directions” means these fifteen
   fixed projective rays under scale propagation, not fifteen disjoint prime
   sets and not fifteen linearly independent vectors.
3. Exact cone map:
   
   \[
   \Gamma=h\begin{pmatrix}r^2&rt\\rt&t^2\end{pmatrix}
   =\begin{pmatrix}u&a\\a&v\end{pmatrix},\qquad uv=a^2.
   \]
   
   Lorentz coordinates (((u+v)/2,a,(u-v)/2)) lie on the null cone and the
   displayed orthogonal inverse gives the exact Koide vector over
   (\mathbb Q(\sqrt2,\sqrt3)).
4. Exact Jordan embedding:
   
   \[
   \iota(\Gamma)=\begin{pmatrix}u&a&0\\a&v&0\\0&0&0\end{pmatrix}.
   \]
   
   It is an injective real-linear Jordan homomorphism into the
   three-dimensional real-symmetric corner
   `$C_{\mathbb R}=\iota(\operatorname{Sym}_2(\mathbb R))
   =eJe\cap\operatorname{Herm}_3(\mathbb R)$`.  The full Peirce corner
   `$eJe\cong\operatorname{Herm}_2(\mathbb H)$` has dimension 6.
5. The 15 projective images are distinct rank-one idempotents after trace
   normalization, but their full 15-coordinate matrix has rank exactly 3.
   E31, E39, E339 give the explicit witness determinant (-930).  Since they
   span the Jordan corner, the Jordan closure is exactly that same
   3-dimensional corner.
6. Normalized orientation reversal has cycle type (1^7 2^4), matching a
   transvection on (\mathbb F_2^4\setminus0).  An explicit equivariant
   bijection exists, but the comparison is only one of (C_2)-sets.
7. Sharp incidence obstruction: the 15 selector points lie on a nonsingular
   real conic and have zero collinear triples; (PG(3,2)) has 35 three-point
   lines.  No bijection preserves these natural incidences.
8. Sharp symmetry obstruction: normalized reversal fixes three selector
   images spanning the corner but swaps four other pairs.  Therefore it cannot
   be induced by any linear or Jordan automorphism of the canonical corner.
9. A3 counts are 12 oriented roots, 6 unoriented roots, and 14 nonzero
   minuscule weights.  Rank-one idempotents of the full Jordan algebra form the
   continuum (\mathbb{HP}^2); the selector images occupy the proper
   (\mathbb{RP}^1) corner.

## Verification

- Upstream certificate run on 2026-09-05: `PASS`; output
  `states=15 canonical_triples=11 hard_progressions=10`; result payload
  SHA-256 `828c13a517ddb4a34f1ac55e8e090bffdb63a341568adb01942bf366d8343799`.
- New standard-library checker: `verify_fifteen_bridge.py`; successful exact
  output in `verification_output.txt`.
- Insertion-ready TeX compiled without warnings as a five-page standalone
  witness with `pdflatex -halt-on-error` using `compile_test.tex`.

## Deliverables

- `REPORT.md`: full audit and exact theorem/proof.
- `fifteen_selector_jordan_bridge.tex`: insertion-ready section.
- `verify_fifteen_bridge.py`: exact census, propagation and bridge checker.
- `verification_output.txt`: deterministic checker output.
- `compile_test.tex` and `compile_test.pdf`: standalone compile witness.

## Conclusion sent to parent

The structural bridge exists as an injection of the fifteen marked arithmetic
ray points into `$\mathbb{RP}^1\subset\mathbb{HP}^2$`.  Under the only coefficient-
preserving canonical embedding presently defined, those fifteen rays span and
Jordan-generate exactly the real-symmetric corner
`$C_{\mathbb R}=\iota(\operatorname{Sym}_2(\mathbb R))$`, dimension 3; this
corner is properly contained in the 6-dimensional Peirce corner.  The
count 15 is therefore not a fifteen-dimensional Jordan identification.  The
strongest next test is to derive, from selector channel/residual data, a
canonical conjugating element that moves different rays into distinct
conjugates of the real-symmetric Jordan corner and then recompute the
multi-prime span and Jordan closure.

