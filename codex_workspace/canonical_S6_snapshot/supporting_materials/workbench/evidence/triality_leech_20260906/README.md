# Exact triality and marked Niemeier–Leech checks — 6 September 2026

The proof-bearing text is in the current higher-rung draft and the shared
`es_niemeier_leech.tex` and `es_niemeier_triality_bridge.tex` modules.
The checkers use exact integer/rational arithmetic; the isometry checker
also uses exact symbolic square roots through SymPy. Run the Python files
in this directory. No network access, external credentials or Lean build
is needed.

The checks cover all 72 original glue classes; every norm-two equality
candidate in the shifted Leech-neighbour cosets; the literal F4 reflection
matrix and representative corrections; the rank-24 isometry, inverse and
cyclic action; the ordered octonion product and Clifford identities; and
full 27-dimensional operator tests of the flag chart and inverse.
`check_marked_weyl.py` additionally checks the displayed images of the
Weyl vector and first simple root inside the three octonion sectors.

The accompanying proofs, not the finite test samples alone, establish
the identities for all allowed arguments. The classical Leech construction
is credited to Conway–Sloane and Borcherds; the Lie-group conventions to
Yokota and the real-flag results to Mare–Willems.

Two corrections were made during independent review: the transported
GL2(F3) complement, not the entire lattice isometry group, centralizes
the stated residue action; and `C v_D = c_D + (1,-1,0,0)`, not equality
of the chosen representatives. The latter difference lies in D4 and
therefore preserves the previously calculated discriminant action.

No raw conversation, private user input, authentication material, or
third-party full-text publication is included in this evidence directory.
