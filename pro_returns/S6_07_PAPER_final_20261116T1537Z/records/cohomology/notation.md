# Notation concordance: cohomology

The source statements retain the first-run convention: the coarse base is
`B=\mathbb P^1_t`, its points are `p_1=0`, `p_2=1`, `p_0=\infty`, the
standard finite multiplicities are 3 and 4, the root generators are
clockwise, and `\beta=\beta_{\mathrm{part}}+c`. No additional special-point
swap is required in these fragments. The alternate Engel marking `Q` in
INV is not used; the paper retains the FAM marking `P_{\mathrm{mark}}`.

## Symbol concordance

| Source symbol | Printed symbol | Reason and scope |
| --- | --- | --- |
| Dual lattice covectors `u,w` | `u_{\Lambda},w_{\Lambda}` | Distinguishes the period covectors from family parameters; the hatted lattice vectors stay unchanged. Local module generators named `u` are untouched. |
| INV logarithmic relative cotangent `E` or `\mathcal E` | `\mathcal E_{\rm cot}` | Keeps the relative cotangent bundle separate from the tangent bundle and elliptic curves. |
| FAM/PUSH/CDP root vertical tangent `\mathcal E` | `\mathcal E_{\rm tan}` | Distinguishes tangent and cotangent source conventions. |
| INV coarse direct-image bundle `G` | `G_B` | Separates the coarse and root-curve extensions. |
| FAM/PUSH/CDP root direct-image bundle `G` | `G_{\mathfrak B}` | Same distinction. |
| INV root curve `\mathcal B` | `\mathfrak B` | Matches the first-run convention. |
| Root-to-coarse map `\rho` | `\varpi` | Reserves `\rho` for the sixth root `e^{\pi i/3}`. |
| INV cotangent determinant line `N` | `N_{\rm det}` | Separates this line from the Bott--Chern ideal and from a cusp tube. |
| INV square-zero ideal `N` | `N_{BC}` | Only the ideal in inv:C3.3. |
| FAM/PUSH cusp normalization surface `E` | `P_6` | The degree-six del Pezzo surface; not an elliptic curve or a vector bundle. |
| Source B2.2 weighted variables `x` of weight 4, `y` of weight 3 | `x` of weight 3, `y` of weight 4 | Swapped consistently only in the valuation argument imported into inv:B3.3. |
| Source B2.2 auxiliary line `\mathcal L` | `\mathcal L_{\rm root}` | Separates the valuation argument from the integral Picard generator. |
| CDP residue indices `r_1(n),r_2(n)` | `r_3(n),r_4(n)` | The subscripts now record the actual root orders; the residue formulas are unchanged. |

Original statement IDs are retained with `inv:`, `fam:`, `push:`, or `cdp:`
prefixes. Internal equation labels receive the same run prefix. Label and
reference keys are protected before symbol substitutions; no mathematical
replacement is allowed inside an identifier. The source's references to
Part A now point to `sec:cotangent-images`, except the reference to its Hodge
diamond, which points to the more precise `sec:hodge`.

## Environments, packages, and macros

The fragments have no preamble or bibliography. They use `theorem`, `lemma`,
`proposition`, `corollary`, `definition`, `remark`, `announcement`, `cited`,
and `proof`, with the supplied `\uses{...}` macro after each formal
statement. The central preamble provides these environments and `\uses`.
Standard requirements are `amsmath`, `amssymb`, `amsthm`, `mathtools`,
`mathrsfs`, and the central table packages. Existing math operators such as
`\Hom`, `\Ext`, `\rank`, `\coker`, `\im`, `\Spec`, `\Proj`, `\Pic`,
`\End`, `\Sym`, `\Res`, `\ord`, `\tr`, and `\lcm` come from that preamble.
The proof shorthands use the central `\dbar` and `\dhat`; the master
normalizes any legacy `\dh` spelling to `\dhat` to avoid redefining the
standard T1 text command. No standard LaTeX command is redefined here.

## Content-preserving layout edits

Long proofs are divided into numbered steps by placing step labels at
existing source paragraph boundaries. Source formulas are not altered by
that operation. References and notation are normalized before recording
`statement_as_printed`; every stored printed statement is matched against
the generated fragment. Exact original source statements are retained
separately in `source_statement`.

## Final Appendix B cusp-coordinate correction

The final visual check identified a remaining notation collision in the
FAM A.5.2 re-derivation. In that appendix proof, the two occurrences of the
weight-twelve modular discriminant `\Delta(\tau)` become
`\Delta_{\rm mod}(\tau)`. The finite root-disc notation `\Delta_{s_j}` is
unchanged.

The source expressly calls the local equation `q=z_0z_1z_2` the original
cusp family. Only that coordinate and its subsequent occurrences in the
same cusp calculations are renamed to `t_c`: the convergent-series ring,
the toric gluing `u(q)q^{B_0\lambda}`, the relation
`\Delta(\tau)=q\,u(q)`, the field `q\partial_q`, and the differentials
`dq`. The last three now read `\Delta_{\rm mod}(\tau)=t_c\,u(t_c)`,
`t_c\partial_{t_c}`, and `dt_c`. Cohomological indices `q` in higher
direct images, degree conditions and cases are unchanged. No equality
between `t_c` and the modular nome `q_\tau` is introduced.

The exact scope and replacement counts are recorded in
`appendix_notation_changes.json`; `appendix_notation_fix.diff` records the
before/after appendix fragment. The generating script applies the same
finite list of replacements with count assertions, preserving all
statements, hypotheses and proof steps.

The same final scan found exactly one additional modular-discriminant
token in the main INV A1.0 proof. With the assembling editor's explicit
authorization, `\Delta(\tau)^{-1}` there is likewise renamed to
`\Delta_{\rm mod}(\tau)^{-1}`. Its surrounding cusp coordinate was
already `t_c`; no other main-fragment notation is changed. This additional
one-token correction is included in `appendix_notation_changes.json`.
