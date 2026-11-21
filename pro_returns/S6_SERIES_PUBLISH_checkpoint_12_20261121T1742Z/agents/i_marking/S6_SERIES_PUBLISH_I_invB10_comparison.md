# Paper I inv:B1.0 — complete-proof comparison and check receipt

## Outcome

PASS for the exact statement `inv:B1.0`, including its integral basis columns, relabelling of base indices, four finite intertwining identities, circle class, both affine signs/denominators, and reversed-meridian marking. The complete target proof agrees with the frozen statement-directed derivation. No mathematical error was found and no source-edit guard is proposed. The main TeX was not modified by this checker.

## Chronology and actual exposure

The pre-proof inputs were exactly the target statement, authenticated primary T0,T1,C,local T1,delta_E data, three receiving definitions, the literal receiving (PD7) affine chart formula, and a literal primary Engel positive-root convention. The task brief disclosed the existence of overlapping checks by other agents and suggested the nullspace method. The other agents' mathematical comparisons and scripts were not read before the derivation freeze.

The derivation was frozen at **2026-11-21T03:44:15.367303+00:00**, SHA256 `074f727dbd67c8b98966b9d4b5c08df1e1fabdf944dc3b0a6612bdafa2ed690b`. The freeze manifest has SHA256 `856f2c733d5c23bd3d5d4356f39c3255efe715a6d5338b09c300268d355ef5d1`.

The complete current target proof was first opened at **2026-11-21T03:44:34.215270+00:00**, after that freeze. The source snapshot had SHA256 `3b272246a072bcf423cea040c0eaec5ce2a8f30da5ab06a8fb7651a4c2ffdd1e`. The exact target statement hash is `63b398c91601705b9a934e7233e04fdc9cb0a2dd2bdad6d8a74352cf262531e1`, matching the initial statement intake; the full proof hash is `5d128edc1bc7c3162948474fba81a7897cd53b0bcde9b34b44a1774a88b09f3c`. Target source lines were 6226–6264 in that snapshot.

After the proof comparison, the checker inspected only lines 1–19 of `code/S6_SERIES_PUBLISH_I_conventions.py`, first opened at **2026-11-21T03:44:54.788952+00:00**. Those lines contain the earlier exact marking verifier. Later TeX-replacement bodies were not opened. The full script hash is `775e509a8da9d7f68e39020ae9289b183c05fed0a5f15cba351825b1f56c7f6b`; the actually read excerpt hash is `fb043997e70d643769862340a9de0c1a2050f9d1fc3ac4aa718facabbc0d49ec`. That earlier script was not run or imported by this checker.

The checker then read the CHECK_EVENTS header and existing inv:B1.0 rows for exact schema and accounting. That exposure occurred after freezing and proof comparison. No check is transferred to any alias or overlapping statement. The separate follow-on target `night:P5.7` statement/proof remains unopened.

## Claim-by-claim comparison

| Exact claim | Frozen derivation and new computation | Complete target proof | Resolution |
|---|---|---|---|
| Common integral basis and T0,T1 | Used authenticated primary input with Theorem 5.1 p. 13 and equation (6.1) p. 16 locators | Prints the same T0,T1 and cites those exact locators | Exact matrices agree |
| Base indices (0,1,infinity) -> (1,2,0) | Explicit point-label map 0 -> p1, 1 -> p2, infinity -> p0 | Uses the receiving base convention | Same point labels |
| P integral and determinant -1 | Gives explicit inverse coordinate map; four exact coordinate solves and fraction-free determinant elimination | States determinant -1 by computation | Exact inverse and determinant agree |
| T0 P=P A1, T1 P=P A2 | Forms all 32 homogeneous equations for an unknown X; rank 14; reconstructs P from free coordinates (x31,x41)=(0,-1) | Verifies the displayed products | Both equations established |
| delta_E=P hatdelta | Solves P d=delta_E and obtains d=e4 | Reads P's fourth column | Same circle vector (-2,-1,3,0) |
| A_j v_j=v_j | Derives the complete two fixed-vector kernels and reconstructs the stated v1,v2 | States fixedness in the affine inversion argument | Exact invariant vectors agree |
| a0=-P v1/3, a1=-P v2/4 | Derives actual inverse affine action, conjugates by explicit Phi_P, and solves for a0=(0,0,0,1/3), a1=(-3,-1,3,-1)/4 | Inverts the affine deck generator and applies P | Same signs and denominators |
| Q=P S and integrality | Recovers S by solving P*s_j=q_j for every column; gives S inverse=S; determinants S=1, Q=-1 | Displays Q=P S and gives determinant S=1 | Same exact lattice maps |
| T0 Q=Q A1^-1, T1 Q=Q A2^-1 | Forms all 32 equations T_i Y A_i=Y; rank 14; reconstructs Q; uses proved integral inverse of A_i | Verifies the displayed inverse products | Both equations established |

## Exact relation between the computational methods

The earlier program uses SymPy to compute P*H, determinants, T0*P, P*A1, T1*P, P*A2, and the corresponding Q identities with A1.inv(), A2.inv(). The new program is `S6_SERIES_PUBLISH_I_invB10_exact_reconstruction.py`, written and executed before the proof was read, with standard-library exact rational arithmetic.

For positive meridians its operator is

L(X)=(T0*X-X*A1, T1*X-X*A2).

The legacy product check evaluates L at the displayed P. The new method constructs the 32-by-16 coefficient matrix of L before inserting a candidate, computes ker(L) by invertible exact row operations, and reconstructs the entire lattice

X(r,k)=-k*P+r*delta_E*gamma, r,k in Z.

It selects the statement's P by its two free coordinates (0,-1). Thus the relationship between the computations is explicitly evaluation of L at P versus full kernel reconstruction followed by selecting P. The new calculation also proves the exact residual shear: circle normalization fixes k=-1 and leaves P+r*delta_E*gamma=P*(I+r*d*gamma). This ambiguity is recorded as a limitation on uniqueness, not an error in the proposition, which displays its chosen P.

For reversed meridians the operator is

Lrev(Y)=(T0*Y*A1-Y, T1*Y*A2-Y).

The program reconstructs ker(Lrev), obtains Y(r,k)=k*Q+r*delta_E*gamma, and selects Q at (r,k)=(0,1). Integral inverses of A1,A2 convert these equations into the two stated inverse intertwining equations. The coordinate-map, circle, and affine-vector assertions are verified by exact linear solves; determinants use fraction-free Bareiss elimination. The output contains the complete row-operation certificates with exact replay.

This substantiates a different computational method, beyond changing a library. Both computations intentionally share the same statement matrices and authenticated primary transcriptions. Independent primary-source authentication by this checker is not claimed. The program's algebraic equivalence to the target equations is exhibited above, rather than asserting unrelated methods.

## Evidence and remaining limits

The exact reconstruction program has SHA256 `ac1f6ad9b1b002a863ba4e2c0f3cce4bf7d8c38916fd5ac186a006cb15aea9a3`. Its complete output has SHA256 `7aac359947e6cd8f71a2d60b9e611c34341ca658597d1eef4590b5a00061a670`. Every assertion passed, with positive/reversed ranks both 14, det(P)=-1, det(Q)=-1, det(S)=1, det(A1)=det(A2)=1.

All frozen files were rehashed after proof and legacy exposure; every hash still matched the freeze manifest. No correction to the frozen derivation was required.

This receipt records one targeted proof-check evidence group, with a separate computation row in that same group. The source authentication was supplied by the provenance agent; this checker did not open the primary page images. The supplied C/local-T1 matrices were not needed for this target and were not given additional computation credit. This result carries no literature-novelty determination, no check of entire-family equivalence, no uniqueness theorem, and no automatic credit for any other statement.

## Files

All paths are relative to `work/agents/i_marking/` unless a different directory is shown:

- `S6_SERIES_PUBLISH_I_invB10_frozen_derivation.md`
- `S6_SERIES_PUBLISH_I_invB10_freeze_manifest.json`
- `S6_SERIES_PUBLISH_I_invB10_exact_reconstruction.py`
- `S6_SERIES_PUBLISH_I_invB10_exact_reconstruction_output.json`
- `S6_SERIES_PUBLISH_I_invB10_postfreeze_proof_exposure.json`
- `S6_SERIES_PUBLISH_I_invB10_legacy_method_exposure.json`
- `S6_SERIES_PUBLISH_I_invB10_CHECK_EVENTS.tsv`

No edit guard is proposed.
