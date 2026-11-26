"""Exact follow-ups found in the complete edited original-cap reading."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("original_cap_homology", "C8-FND-ORIGINAL-CAPS-FOLLOW-")
    e.replace(
        "free affine twists of Theorem~\\ref{maps:src:D.2.30}. Keep the\npreceding marked zero-free multiplicative and unique rank-two\nzero models. Allow any number of regular logarithmic sites,\n",
        "free affine twists of Theorem~\\ref{maps:src:D.2.30}. Use the\nmarked zero-free multiplicative and unique rank-two zero models\nof Theorem~\\ref{maps:src:D.2.23}. Allow any number of regular logarithmic sites,\n",
        "D06", "mapsIII:def:zero-chern-original-data",
        "Name the exact KY construction that supplies these marked models instead of an unbounded preceding-text pointer.")
    e.replace(
        "every permitted positive order and an integer clutch $e$.\nFor an original additive cap let $\\rho_i$ be the number of\n",
        "every permitted positive order and an integer clutch $e$.\nA filling pattern is the ordered list of options at the additive\nsites of one natural initial row.\nFor an original additive cap let $\\rho_i$ be the number of\n",
        "D13", "mapsIII:def:zero-chern-original-data",
        "Move the named filling-pattern definition into the numbered input definition before the theorem's first use, with exactly the same ordered rows and sites.")
    e.replace(
        "A pattern is the ordered list of options at the additive sites of\none of these rows. The displayed option rule determines all 228\nlists, with the row and site markings fixed. Parts 6--7 include every\n",
        "The displayed option rule determines all 228 filling patterns,\nwith the row and site markings fixed. Parts 6--7 include every\n",
        "D12", "maps:src:D.2.31",
        "Use the pattern definition now owned by Q126; retain the complete option rule, enumeration and all-parameter proof references.")
    e.replace(
        "For example, the OS47 default row with the \\(I_2\\) zero and\n",
        "For example, the OS47 base row with the \\(I_2\\) zero and\n",
        "D20", "maps:src:D.2.31",
        "Apply the same explicit default-to-base row-name bijection already made in the three profile tables; every profile, zero, parameter and fan matrix stays fixed.")
    e.replace(
        "where \\(g\\) goes from complement to attached boundary and its\ninverse uses \\(\\alpha_z^{-1}\\). The cap action is\n",
        "where \\(\\alpha_z\\) is the rotation in the first real two-plane\nof Definition~\\ref{mapsIII:def:twisted-smale-suspension}. The map\n\\(g\\) goes from complement to attached boundary and its\ninverse uses \\(\\alpha_z^{-1}\\). The cap action is\n",
        "D05", "maps:src:D.2.31",
        "Restore the precise rotation definition when the common framed reconstruction is cited through Q118/KQ; its orientation, gluing direction and inverse remain explicit.")
    e.replace(
        "and, for \\(R>1\\), choose \\(x,y\\) with\n\\(\\lambda(x,y)=1/R\\). The explicit mutually inverse coordinates are\n",
        "and, for \\(R>1\\), choose \\(x\\) of order \\(R\\) and \\(y\\) with\n\\(\\lambda(x,y)=1/R\\). Write\n\\(\\operatorname{num}_R([k/R])=k\\bmod R\\). The explicit mutually inverse coordinates are\n",
        "D05", "maps:src:D.2.31",
        "Retain the original maximal-order generator hypothesis and define the linking numerator coordinate used by the displayed map and inverse.")
    e.replace(
        "and the even-dimensional product swaps preserve the orientation.\n",
        "and the product swaps whose dimension products are even preserve the orientation.\n",
        "D20", "maps:src:D.2.31",
        "State the actual orientation sign (-1)^(pq) for the product swaps; the S3-by-S2 factors have even dimension product without both dimensions being even.")
    e.replace(
        "Let \\(L\\) be the number of nonzero-Chern original additives, and set\n\\[\n \\beta=\\sum_{\\mathrm{zero\\ Chern\\ originals}}(\\rho_i-1)\n       +\\sum_{\\mathrm{nonzero\\ Chern\\ originals}}(s_i-2).\n\\]\n",
        "Use \\(L\\) and \\(\\beta\\) from\nDefinition~\\ref{mapsIII:def:all-original-additive-data}.\n",
        "D12", "maps:src:D.2.32",
        "Use the single numbered definition of these original-cap counts; the preserved OC2 equation remains at that definition and no calculation changes.")
    e.finish()


if __name__ == "__main__":
    main()
