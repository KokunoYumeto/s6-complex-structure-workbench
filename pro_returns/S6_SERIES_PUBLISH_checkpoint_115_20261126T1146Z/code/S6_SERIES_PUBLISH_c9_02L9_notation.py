#!/usr/bin/env python3
"""Full original-multiplicative proof: exact scoped object names."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02L9", "maps:src:D.2.33", "cdf87fcc953a8009d3e687ad8e081531349f33a9de12bedf5caba14211a271f0", "323–329",
           "This agent read the complete 540-line statement/proof; reading_findings read the actual page images. Traced the cap and explicitly bound period unit, elliptic section and fibre quotient, fixed-rank/count scalars and peripheral generators, every later use of the Bezout integer through the basis matrices and fibre evaluation, and all final enumeration-count and numeric-header roles. Preserved all actual chart maps, inverses, Chern data and enumeration entries.",
           image_reader="reading_findings (this agent's contribution is the full source-context review)")

p.exact("holomorphic-period-unit",
        r"""The nearby long path
$z(t)=z_0\exp(t\log(q^\nu U(q)))$ crosses the successive node
annuli once around the graph. Its endpoints differ by the
given elliptic long period.""",
        r"""Write the marked elliptic long-period multiplier as
$q^\nu U_{\rm hol}(q)$, where $U_{\rm hol}$ is its nonzero
holomorphic unit on the base disc. The nearby long path
$z(t)=z_0\exp(t\log(q^\nu U_{\rm hol}(q)))$ crosses the successive node
annuli once around the graph. Its endpoints differ by the
given elliptic long period.""",
        "U_hol is explicitly bound to the nonzero holomorphic unit of the marked elliptic long-period multiplier. The earlier paragraph states that the elliptic long period has valuation nu and that every period unit is transported with its exponent; the old path already writes that multiplier as q^nu U(q). Thus U_hol(q)=U(q) pointwise, equivalently q^(-nu) times the same multiplier away from q=0, with the same extending unit at q=0. Multiplication back by q^nu recovers the complete multiplier. The chosen logarithm, path z(t), endpoints and node crossings remain unchanged. The cap U and all its homology/boundary maps keep their existing name.")

bezout_reason = ("z_Bez=z is the same integer in a kappa x+nu z_Bez=1. Identity on the pair (x,z_Bez) preserves beta_0=xu+z_Bez delta, both short-plane inverse rows, the two Wang preimages, the kernel-change matrix and its displayed inverse. The later fibre value remains -aBx-b z_Bez=-(b/nu)(a kappa x+nu z_Bez)=-b/nu. The separately bound period path z(t), node coordinate z and final enumeration count z retain their explicit domains.")
p.scope("bezout-definition-and-wang-preimages",
        r"Choose $x,z\in\mathbb Z$", "Write the marked elliptic long-period multiplier as",
        p.literals([("z", r"z_{\rm Bez}", 5)]), bezout_reason)
p.exact("bezout-kernel-basis-and-inverse",
        r""" \begin{pmatrix}1&0&0\\0&\nu&x\\0&-a\kappa&z\end{pmatrix},
 \qquad
 \begin{pmatrix}1&0&0\\0&z&-x\\0&a\kappa&\nu\end{pmatrix}""",
        r""" \begin{pmatrix}1&0&0\\0&\nu&x\\0&-a\kappa&z_{\rm Bez}\end{pmatrix},
 \qquad
 \begin{pmatrix}1&0&0\\0&z_{\rm Bez}&-x\\0&a\kappa&\nu\end{pmatrix}""", bezout_reason)
p.exact("bezout-fibre-evaluation",
        r""" \omega(k)=-aBx-bz
          =-\frac b\nu(a\kappa x+\nu z)=-b/\nu.""",
        r""" \omega(k)=-aBx-bz_{\rm Bez}
          =-\frac b\nu(a\kappa x+\nu z_{\rm Bez})=-b/\nu.""", bezout_reason)

p.exact("zero-chern-fibre-quotient",
        r" Q(y)=(y_{12},y_{23},y_{24},y_{34}),\qquad",
        r" Q_{\rm fib}(y)=(y_{12},y_{23},y_{24},y_{34}),\qquad",
        "Q_fib=Q is the identical map from the six exterior coordinates of (v,t,delta,w) to the four displayed fibre-image coordinates. The stated sigma inserts those coordinates, so Q_fib sigma=id; the reverse error is y_13 e_13+y_14 e_14, the same two Wang-image generators for the displayed I+E_12 return. This proves the identical quotient and section. The elliptic section Q=bG and shear Q_j retain their original names and inverse maps.")

p.scope("fixed-ranks-and-boundary-count",
        "At boundary $i$, let the fixed rank", "An integral basis of this kernel",
        p.literals([("c_i", r"r_i^{\rm fix}", 6), ("N", r"N_{\rm bd}", 3)]),
        "r_i^fix=c_i is the same integer rank of the fixed lattice at boundary i, and N_bd=N is the same number of boundary circles. Identity on these integer counts preserves the boundary rank r_i^fix+1, ordinary cap rank r_i^fix, nonzero-Chern cap rank r_i^fix-1 and the exact sum yielding L+r. The peripheral group generators c_i, component Chern degrees c_j and original Kodaira neighbourhood N retain their original objects and maps.")

p.scope("enumeration-site-counts", "On a row let $f$ count", "target homology isomorphisms",
        p.symbols([("f", r"f_{\rm en}"), ("c", r"c_{\rm en}"), ("z", r"z_{\rm en}")]),
        "f_en=f, c_en=c and z_en=z are the identical nonnegative counts of finite additive, nonzero-Chern multiplicative and zero-Chern multiplicative sites. The identity on the ordered triple preserves both exponents f_en+c_en and f_en+c_en+z_en. The quotient still forgets exactly the same z_en choices and its section still selects the same primitive fillings. Each count has three occurrences in this paragraph. The previously defined functions, component coordinates and period path retain their own names and point maps.")
p.exact("upright-numeric-count-headers",
        r"\mathrm{OS}&\mathrm{profile}&R&K&P&A\\ \hline",
        r"\mathrm{OS}&\mathrm{profile}&\mathrm R&\mathrm K&\mathrm P&\mathrm A\\ \hline",
        "The four numeric table headers are upright R,K,P,A, denoting in their already specified order the counts of initial rows, nonzero-Chern multiplicative positions, kernel patterns and individual choices. The map assigns every old numeric cell to itself in the same row and column; reading the same cell is its inverse. All twenty-one profile rows and the total row are byte-identical. The existing italic maps, groups and matrices R,K,P,A retain their mathematical symbols.")

p.finish()
