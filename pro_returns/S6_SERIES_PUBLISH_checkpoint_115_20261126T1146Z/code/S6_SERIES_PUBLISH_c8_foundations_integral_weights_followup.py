"""Exact LI readback clarifications, including the integral norm-map reason."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("weighted_integral_homology", "C8-FND-INTEGRAL-WEIGHTS-FOLLOWUP-")
    owner = "maps:src:D.2.41"
    e.replace("For $u,v\\in\\Lambda$ set\nFor $u,v\\in\\Lambda=\\mathbb Z^4$ set\n", "For $u,v\\in\\Lambda$ set\n", "D23", owner,
              "Remove the repeated introductory sentence caught in the whole edited-source reading; the basis and complete cochain formula remain.")
    old = "Place an unfilled site last, and take the first $r$ base loops\nas independent generators. The based insertions $J_i$ use\nthese same stems and the final inverse word.\n"
    new = r"""Place an unfilled site last, and take the first $r$ base loops
as independent generators. Put
\[
 K=\ker\bigl([A_0-I\ \cdots\ A_{r-1}-I]:
              \Lambda^r\longrightarrow\Lambda\bigr).
\]
The based insertions $J_i:\operatorname{Fix}A_i\longrightarrow K$
use these same stems and the final inverse word. At a logarithmic
site write $m>0$ and $v\in\Lambda$ for its order and invariant
power, so $A_i^m=I$ and $A_iv=v$, and put
$N_m=\sum_{\nu=0}^{m-1}A_i^\nu$. At a regular site $A_i=I$.
"""
    e.replace(old, new, "D05", owner,
              "Define the exact target graph kernel, fixed-domain peripheral maps and full logarithmic order/power/norm before BC4; all are the same objects used in the complete proof.")
    e.replace("Write its abelianization as $\\mathbb Z^{r_1}\\oplus A_1$.\nThe free ranks and complete integral homology are\n\\eqref{maps:eq:D.WP8} and~\\eqref{maps:eq:D.WP9}, using $r=r_1$\nand the full torsion group $T$ just defined.", "Write its abelianization as $\\mathbb Z^{r_1}\\oplus\\mathcal A_1$.\nThe free ranks and complete integral homology are\n\\eqref{maps:eq:D.WP8} and~\\eqref{maps:eq:D.WP9}, using $r=r_1$,\n$A_1=\\mathcal A_1$ and the full torsion group $T$ just defined.", "D20", owner,
              "Name the finite H1 group separately from the boundary matrix A_1, with an explicit identity substitution into the existing homology table. Every finite group and rank is unchanged.")
    old = "The five displayed columns respect these relations: the cyclic\nsum vanishes on $(A_i-I)\\lambda$, the remaining wedge term is a\ncolumn of $(\\Lambda^2A_i-I)$, and the root relation reads\n$\\sum_{\\nu<m}c_i(A_i^\\nu v)=mc_i(v)$.\n"
    new = r"""The five displayed columns respect these relations as follows.
Every $\Lambda^2A_i$ acts trivially on $C$, including the final
inverse word. For an independent site, \eqref{maps:eq:D.BC8}
therefore gives
\[
 c_i(u)+c_i(w)-c_i(u+w)=p(A_iu,A_iw)-p(u,w)\quad\text{in }C.
\]
For the last site put $B_j=A_{j+1}\cdots A_{r-1}A_r$.
The polar defect of the second line of \eqref{maps:eq:D.BC3}
is, in the same group,
\[
 -\sum_{j<r}\bigl(p(A_jB_ju,A_jB_jw)-p(B_ju,B_jw)\bigr)
             =p(A_ru,A_rw)-p(u,w),
\]
by telescoping the ordered suffixes. Thus the same polar formula
holds for every site. Put
$s_{i,m}(u)=\sum_{\nu<m}c_i(A_i^\nu u)$ in $C$.
Its polar defect telescopes to
$p(A_i^mu,A_i^mw)-p(u,w)=0$, so $s_{i,m}$ is additive.
Cyclic reindexing gives $s_{i,m}(A_iu)=s_{i,m}(u)$, and hence
$s_{i,m}((A_i-I)\lambda)=0$. The remaining wedge term is a
return relation because $A_iv=v$:
\[
 ((A_i-I)\lambda)\wedge v
              =(\Lambda^2A_i-I)(\lambda\wedge v).
\]
The root relation reads $s_{i,m}(v)=mc_i(v)$.
On $\operatorname{Fix}A_i$ the same polar formula is zero,
so the fixed-normal map is additive there as well.
"""
    e.replace(old, new, "D22", owner,
              "Supply the needed reason for the asserted relation map: both independent and final-word corrections have the same polar defect in the full coinvariant, the norm polar sum telescopes, and cyclic reindexing gives additivity and vanishing on (A_i-I)lambda. This proves the existing full Thom-source assertion integrally at even factors; it does not refute any original intermediate conclusion.")
    e.replace("For an affine lift $Ax+\\eta$ with $P\\eta=v/m$, put\n", "For an affine lift $A_ix+\\eta$ with $P\\eta=v/m$, put\n", "D20", owner,
              "Use the actual weighted site's A_i consistently in its affine conjugacy; identity on that matrix is the symbol map and inverse.")
    old = "The narrow multiplicative original and Mumford patterns are\nidentified by those same marked local maps. The finite choices\nat $\\mathrm{III}^*$ and $\\mathrm{IV}^*$ account for the extra\n$36$ patterns."
    new = r"""At a narrow zero-Chern multiplicative site, use the integral
period basis $(l,h,p,w)$ in the rank-one part of the proof of
Theorem~\ref{maps:src:D.2.40}, with $r_0=\gcd(d,\nu)$.
Identity on this basis carries the two marked boundary maps
to their common normalization diagram. Both fibre kernels are
$\mathbb Z\langle l\wedge p,l\wedge w\rangle$, and all three
fixed normals bound. In wedge order $12,13,14,23,24,34$, the
four complementary coordinates and their section are
\[
 Q(y)=(y_{12},y_{23},y_{24},y_{34}),\qquad
 \sigma(z)=z_1e_{12}+z_2e_{23}+z_3e_{24}+z_4e_{34}.
\]
The inverse cap coordinates read the first coefficient of the
component sum and the three graph-circle/torus products in that
diagram. Thus $Q\sigma=I$ gives the same complete marked
boundary kernel for these two choices, with every node and line
unit carried by the stated period maps. The finite choices
at $\mathrm{III}^*$ and $\mathrm{IV}^*$ account for the extra
$36$ patterns."""
    e.replace(old, new, "D20", owner,
              "State the original/Mumford comparison at its actual boundary-kernel scope through the full integral rank-one basis, quotient, section and inverse cap coordinates. This supplies the exact diagram map used by the pattern enumeration without adding a smooth identification.")
    e.finish()


if __name__ == "__main__":
    main()
