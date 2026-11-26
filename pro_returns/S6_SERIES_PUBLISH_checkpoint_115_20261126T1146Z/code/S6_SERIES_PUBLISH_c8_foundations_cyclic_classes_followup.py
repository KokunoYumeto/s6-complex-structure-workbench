"""Correct the exact new input permutation and readback notation in the owned unit."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor

e = Editor("cyclic_invariants", "c8-III-foundations-cyclic-classes-followup-", group="root")
e.replace(r""" (a,b_1,b_2,b_3)\longmapsto(a,b_2,b_1,b_3)
 \quad\text{in the basis }(H,E_A,E_B,E_C);
\]
its inverse is the same permutation.""", r""" (a,b_1,b_2,b_3)\longmapsto(a,b_3,b_1,b_2)
 \quad\text{in the basis }(H,E_A,E_B,E_C).
\]
The inverse sends $(a,c_A,c_B,c_C)$ to $(a,c_B,c_C,c_A)$:
the ray identifications are $(E_1,E_2,E_3)=(E_B,E_C,E_A)$.""",
          "D25", "mapsIII:def:cyclic-cohomology-data",
          "The newly introduced publication definition mistakenly swapped the first two exceptional coordinates. KB's wholly read exact ray basis is E1=-e1=EB, E2=e1-e2=EC, E3=e2=EA. Replace that false new intermediate coordinate map by its exact three-cycle and inverse. No original theorem, proof value or scope changes; this occurs before canonical application.")
e.replace("and write $G=\\mathbb Z/d$ for its deck group. Its differential is the complex bundle\n",
          "and write $G=\\mathbb Z/d$ for its deck group. The covering differential is the complex bundle\n",
          "D23", "maps:src:D.1.5", "Name the covering as the domain of the derivative after introducing its deck group.")
e.replace("Its cochain map sends a local-system cochain to the lifted cochain\n", "For a deck generator $g$ and $\\lambda^d=1$, its cochain map\nsends a local-system cochain to the lifted cochain\n",
          "D20", "maps:src:D.1.5", "State the generator and eigenvalue used in the already proved coefficient-lift map.")
e.replace(r"""$H^4(W;\mathbb C)\cong\bigoplus_jH^4(D_j;\mathbb C)$ by
restriction to the normalized components $D_j\cong dP_6$:""", r"""$H^4(W;\mathbb C)\cong\bigoplus_jH^4(\overline D_j;\mathbb C)$ by
pullback along the normalization maps $\nu_j$ of
Definition~\ref{mapsIII:def:cyclic-cohomology-data}:""",
          "D20", "maps:src:D.1.5", "Use the actual normalization domains, distinguished from their image divisor cycles by Q142, for the degree-four restriction isomorphism.")
e.replace(r"H^4(M;\mathbb C)\longrightarrow\bigoplus_jH^4(D_j;\mathbb C)",
          r"H^4(M;\mathbb C)\longrightarrow\bigoplus_jH^4(\overline D_j;\mathbb C)",
          "D20", "maps:src:D.1.5", "Keep the displayed total restriction target identical to the preceding normalized-component domains; the pullbacks and injectivity are unchanged.")
e.finish()
