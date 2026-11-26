"""Exact locator and wording corrections from the full edited finite-cap read."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("finite_primitive_caps", "C8-FND-FINITE-CAPS-FOLLOW-")
    e.replace("$g=1$ or $q$, with the counts in \\eqref{maps:eq:D.AF1}.\n",
              "$g=1$ at $68$ positions and $g=q>1$ at $34$ positions.\n",
              "D20", "maps:src:D.2.30",
              "Replace the equation locator, which defines g but contains no counts, by the exact enumeration values already asserted and proved in this theorem.")
    e.replace("generators $\\gamma,c_i$, with their actual root numerators;\n",
              "generators $\\gamma,c_i$, with their root numerators;\n",
              "D08", "maps:src:D.2.29",
              "State the already specified marked numerators directly; the generator map and inverse remain.")
    e.replace("Its actual contracting numerator is $\\gamma^*(v)=gn$.\n",
              "Its contracting numerator is $\\gamma^*(v)=gn$.\n",
              "D08", "maps:src:D.2.30",
              "Use the exact displayed numerator without an unnecessary qualifier.")
    e.finish()


if __name__ == "__main__":
    main()
