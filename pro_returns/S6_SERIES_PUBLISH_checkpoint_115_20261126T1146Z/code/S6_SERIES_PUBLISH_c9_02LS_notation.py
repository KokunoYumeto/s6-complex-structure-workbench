#!/usr/bin/env python3
"""Bind the exact Smith kernel coordinate maps in the full 02LS proof."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02LS", "maps:src:D.2.50", "15fdb387fa3248c0998660aabb8d3f711858032fe0ef4ebfedbd751238a4af32", "407–416",
           "Traced the primitive graph lattice K=ker D, the last seventeen Smith basis columns and their inverse rows, all three fixed-normal coordinate uses, and the later separately bound ordinary/singular kernel matrices. Bound the actual basis map and its coordinate inverse explicitly, preserving every boundary entry and actual bar/cap map.")

reason = ("K remains the subgroup ker(D:Z^20→Z^4). Let E:Z^17→Z^20 insert three leading zeros. "
          "The existing Smith choice gives K_0=V_D E and K_0^vee=E^t V_D^-1, so K_0^vee K_0=I_17. "
          "For x in ker D, U_D D V_D has exactly three nonzero unit diagonal entries, hence the first three coordinates of V_D^-1 x vanish; therefore K_0 K_0^vee x=x. "
          "These exact inverse maps express each existing graph lattice element in the already chosen seventeen coordinates. For a fixed u, D J_i u=(T_i-I)u=0. "
          "For the ordinary map, D J_o u=(I-T_0 T_1 T_2 T_3 T_4)u=0 by the ordered-product identity, so all three displayed arguments lie in that same kernel. "
          "The bar correction, ordinary Thom columns, matrices and integer entries are unchanged; the three K^-1 expressions now name this explicit coordinate inverse.")

p.exact("smith-kernel-map", """The exact Smith factors of $D$ are $1,1,1$, so $K$ is primitive
of rank $17$. If $U_DDV_D$ is its Smith form, columns $4$
through $20$ of $V_D$ form the chosen basis and the corresponding
rows of $V_D^{-1}$ give its inverse on $K$. The nonzero Smith
factors of $R$ are $1,1,1,1,2$. Thus the fibre coinvariant is""",
        r"""The exact Smith factors of $D$ are $1,1,1$, so $K$ is primitive
of rank $17$. If $U_DDV_D$ is its Smith form, let
$K_0:\mathbb Z^{17}\to K\subset\mathbb Z^{20}$ be the matrix of
columns $4$ through $20$ of $V_D$, and let $K_0^{\vee}$ be the
matrix of the corresponding rows of $V_D^{-1}$. Thus
\[
 K_0^{\vee}K_0=I_{17},\qquad
 K_0K_0^{\vee}|_K=\operatorname{id}_K.
\]
We use $K_0^{\vee}$ to read the chosen graph coordinates below.
The nonzero Smith factors of $R$ are $1,1,1,1,2$. Thus the fibre coinvariant is""", reason)

for suffix in ("J_i u", "J_o u", "J_o v"):
    p.exact("kernel-coordinate-" + suffix.replace(" ", "-"), "K^{-1}" + suffix, "K_0^{\\vee}" + suffix, reason)

p.finish()
