"""Print the exact component and product pullback identifications from readback."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor

e = Editor("cyclic_invariants", "c8-III-foundations-cyclic-cubics-followup-", group="root")
e.replace(r"\quad\text{in }H^2(\mathrm dP_6;R).", r"\quad\text{in }H^2(\overline D_j;R).",
          "D20", "maps:src:D.1.9", "Use the same normalized component domain as the map nu_j and its projection formula, through Q142's marked dP6 identification.")
e.replace(r"""Their composites induce the identity on $\pi_2$, and all other
homotopy groups vanish. The integral K\"unneth cross-product map is""", r"""Their composites induce the identity on $\pi_2$, and all other
homotopy groups vanish. Under this equivalence, the classes in
Definition~\ref{mapsIII:def:fundamental-class-invariant} are the
pullbacks of the free-factor $x_i$ and cyclic-factor $u_0$ by
the two product projections. Restriction to the corresponding
factor is inverse on each of these summands. We use the same
symbols for these pullbacks. The integral K\"unneth cross-product map is""",
          "D20", "maps:src:D.1.10", "Write the exact projection pullbacks and inverse factor restrictions relating the numbered global coordinates to the local factor generators before the mixed pairing table.")
e.finish()
