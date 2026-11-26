#!/usr/bin/env python3
"""Assemble the LH receiver from its frozen proof and reviewed auxiliaries."""
from hashlib import sha256
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_odd_weighted"
PREFIX = "S6_SERIES_PUBLISH_III_02LH_"
frozen = {
    "fresh_derivation.md": "23e7026ce52f00005d7d4248f33b4975900e3c64b9905a06b614ecde06cbf0d8",
    "fresh_local_maps.md": "71eb34b0e8735b77d34e3bfe7a48240b2acde421a0a2fdc8ea7b96bc4cc79ee0",
}
texts = {}
for name, expected in frozen.items():
    raw = (LANE / (PREFIX+name)).read_bytes()
    assert sha256(raw).hexdigest() == expected
    texts[name] = raw.decode()
main = texts["fresh_derivation.md"]
local = texts["fresh_local_maps.md"]
post = (LANE / (PREFIX+"post_exposure_derivation.md")).read_text()


def between(text, start, end=None):
    i = text.index(start)
    return text[i:] if end is None else text[i:text.index(end, i)]


def section(text, number):
    start = re.search(r"(?m)^## "+str(number)+r"\. .*$", text)
    assert start
    later = re.search(r"(?m)^## [0-9]+\. ", text[start.end():])
    end = start.end()+later.start() if later else len(text)
    return text[start.start():end]


def replace(text, old, new):
    assert old in text, old[:120]
    return text.replace(old, new)


intro = r"""Let \((a,b,*)\) be the given natural row, and write
\[
 g=\gcd(a,D)=\gcd(a,Db),\qquad
 A_i(D)=S_D^{-1}A_iS_D,\qquad
 S_D=\operatorname{diag}(1,1,1,D).
\]
Here \(D=d>0\) denotes the translation iterate. The equality of
the two gcds uses \(\gcd(a,b)=1\).
Put \(C_D=(\Lambda^2\Lambda)_{\{A_i(D)\}}\) and
\(K_D=K=\ker[A_i(D)-I]_{i<N-1}\).
Write \(B_i,g_i\) for the defining elliptic matrix and section
cocycle of \ref{maps:src:D.2.23}. Put
\[
 J_{\rm ell}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 \beta_i^1=-g_i^tJ_{\rm ell}B_i,\qquad
 A_i=\begin{pmatrix}
 B_i&0&b g_i\\
 a\beta_i^1&1&c_i\\
 0&0&1
 \end{pmatrix}.
\]
At \(I_\nu\), choose the primitive Tate basis \(u,r\) with
\(B_i-I=\nu uu^tJ_{\rm ell}\), \(g_i=\kappa u\), and
\[
 c_i=-ab\kappa^2/\nu+[i=*]/\nu.
\]
At an additive site,
\(c_i=ab\beta_i^1(B_i-I)^{-1}g_i\).
The defining component-degree equations make these matrices
integral and give their ordered product equal to the identity.
The first three entries of the gamma column are multiplied by
D under the actual iterate. All other entries are unchanged.

With the last site omitted, put
\[
 U_2=[B_i-I]_i,\qquad
 U_3=\left[\binom{B_i-I}{\beta_i^1}\right]_i .
\]
The maximal-minor calculations of \ref{maps:src:D.2.37} give
integer sections \(R_2,R_3\) with
\(U_2R_2=I_2\), \(U_3R_3=I_3\), on each defining profile.
For completeness, take a Bezout combination of the maximal
minors, insert each adjugate in its column positions, and add
with those coefficients. Multiplication gives the stated
sections. Their identities contain no weight parameter.
The weight-one degree-one relation matrix also has its section
\(G_1R_1=I_3\).
"""

degree_one = section(main, 1)
degree_one = replace(
    degree_one,
    "Use the defining profile matrices U2,U3 and their primitive integer\n"
    "right inverses R2,R3 from the admitted LD calculation. Write G_D for",
    "Write G_D for",
)
wedge_part = section(main, 2)
wedge_part = replace(
    wedge_part, "The LD polynomial preimages, valid for every D, give",
    r"""The preimages can be written before dividing by any gcd.
On the two angular columns the relation map is \(B_i-I\), so
inserting \(R_2\) gives preimages of \(e_{1\delta},e_{2\delta}\).
For an elliptic vector \(\lambda\), the remaining coordinates
of the relation on \(\lambda\wedge\gamma\) are
\[
 (Db\,\beta_i^1\lambda,\ (B_i-I)\lambda,\
                              a\beta_i^1\lambda).
\]
Insert \(R_3\) in these elliptic-gamma column positions. Its
three images, modulo the two angular coordinates, are
\(e_{1\gamma},e_{2\gamma},Db\,e_{12}+a\,\delta\gamma\).
Subtract their angular coordinates using the first two
preimages. These integer operations are linear in D and give""",
)

elliptic = section(post, 3)
elliptic = replace(
    elliptic, "## 3. D.OW7 and the two vanishing-word exceptions",
    "## 3. The elliptic image and the exact angular rim",
)
elliptic = replace(
    elliptic,
    "The new post-exposure program retains all 172 full matrices,\n"
    "all right inverses and every Bezout minor witness. It checks\n"
    "the matrix products and the polynomial weighted wedge identity.\n"
    "It does not use or execute the historical target program.\n",
    "The displayed minor sections give every integral preimage.\n",
)
elliptic = replace(
    elliptic,
    r"                 \mathbb Z^2/\operatorname{im}E=0.",
    r"""                 \mathbb Z^2/\operatorname{im}E=0.
 \tag{D.OW7}\hypertarget{tag-0232}{}\label{maps:eq:D.OW7}""",
)
elliptic = replace(
    elliptic,
    "The two OS46/II rows do not contradict this assertion.",
    "On the two OS46/II rows the inverse is particularly explicit.",
)
elliptic = replace(
    elliptic,
    "The original-star\n"
    "discs used in the fresh fundamental-group proof supply the\n"
    "remaining vanishing relation.",
    "The original-star discs in the fundamental-group calculation below\n"
    "supply the remaining vanishing relation.",
)
elliptic = replace(
    elliptic,
    "D.OW7 is true on all 172\nrows; it is not a refuted assertion.",
    r"\eqref{maps:eq:D.OW7} holds on all 172 natural rows.",
)

graph = section(main, 3)
graph = replace(
    graph,
    "The admitted real-period map and inverse are in\n"
    "agents/continuation7_iii_nonstar/S6_SERIES_PUBLISH_III_02L1_fresh_graph_maps.md,\n"
    "Section 1 and Section 3 through its noncanonical-lift paragraph.\n"
    "Those exact bounded passages were read for this derivation.\n",
    "Use the real-period map and its inverse from\n"
    r"\ref{maps:src:D.2.26} and \ref{maps:src:D.2.31}."+"\n",
)
graph_start = between(graph, "## 3.", "Give C_D the trivial")
graph_start = graph_start.replace(
    "## 3. The actual marked graph and its doubled projection",
    "## 4. The marked graph and its integral involution section",
)
involution = section(post, 1)
involution = between(involution, "Use the actual period exponential",
                     "The cocycle used in the frozen derivation")
involution = involution.replace(
    "from the fresh\nproof", "above").replace(
    "in the fresh proof", "above")
involution = replace(
    involution,
    r"       \xrightarrow{\epsilon}K_D\longrightarrow0.",
    r"""       \xrightarrow{\epsilon}K_D\longrightarrow0.
 \tag{D.OW5}\hypertarget{tag-0230}{}\label{maps:eq:D.OW5}""",
)
involution = replace(
    involution, r" s_\iota(k)=x-\tfrac12(x+\iota x)",
    r""" s_\iota(k)=x-\tfrac12(x+\iota x)
 \tag{D.OW6}\hypertarget{tag-0231}{}\label{maps:eq:D.OW6}""",
)
involution = replace(
    involution,
    "They prove the\noriginal D.OW5--D.OW6 marking, including every odd torsion class.",
    "They give the integral marking, including every odd torsion class.",
)
cocycle = between(graph, "Give C_D the trivial",
                  "The edge projection gives the other coordinate")
cocycle = replace(
    cocycle, "For the admitted weight-one marked graph",
    r"For the weight-one marked graph of \ref{maps:src:D.2.31}",
)
cocycle = replace(
    cocycle, "by the admitted LD/L7 exterior construction",
    r"by the exterior construction of \ref{maps:src:D.2.31} and \ref{maps:src:D.2.37}",
)
same = between(section(post, 1), "If \\(y=s_\\iota(k)\\)")
same = replace(
    same,
    "The cocycle marking therefore sends",
    "The cocycle marking therefore sends",
)
same = (
    "The cocycle is invariant under inversion, because both wedge\n"
    "arguments change sign.\n\n"+same
)
same = same.replace(
    "Its two inverse maps\nare precisely the involution maps just displayed.",
    "Thus it has the same two inverse maps as the involution marking.",
)
graph_end = between(graph, "The edge projection gives the other coordinate")
norms = between(section(post, 2), "A literal fixed normal",
                "The positive normal meridian")
normal = section(main, 4)
normal = normal.replace("## 4. ", "## 5. ", 1)
normal = normal.replace("from\nthe admitted finite-root construction",
                        r"of \ref{maps:src:D.2.29}")
normal = normal.replace(
    "These calculations use the actual normal parametrizations",
    "These calculations use the normal parametrizations",
)
normal += r"""
In the abelian subgroup generated by \(v,\mu_i\), the root
normal has ordered generators \((\mu_i,\mu_i^m-v)\). The change
from \((v,\mu_i)\) and its inverse are
\[
 \begin{pmatrix}0&-1\\1&m\end{pmatrix},\qquad
 \begin{pmatrix}m&1\\-1&0\end{pmatrix}.
\]
Their determinant is one, so the normal orientation gives
the same torus class as the fixed \(v\)-sweep.
"""

finite = section(main, 5)
finite = finite.replace("## 5. ", "## 6. ", 1)
finite = replace(
    finite, "Use the actual root-disc construction admitted in L4 and LA,",
    r"Use the root-disc construction of \ref{maps:src:D.2.29} and \ref{maps:src:D.2.34},",
)
finite = finite.replace("The admitted line gauges", "The line gauges")
finite = finite.replace("in\nSection 4", "computed above")
finite = replace(
    finite,
    "This fact uses the full\nweighted projected lattice, not an assumed old fixed basis.",
    "This applies to the projected lattice at every weight.",
)
shears = section(main, 6).replace("## 6. ", "## 7. ", 1)

local_body = between(local, "## 1.")
local_body = local_body.replace(
    "The fresh calculation saves all these matrices.\n", "")
local_body = local_body.replace(
    "The admitted normalization complex", "The normalization complex of "
    r"\ref{maps:src:D.2.34}")
local_body = local_body.replace(
    "At a zero-Chern original, use the admitted frames", "At a zero-Chern original, use the frames")
local_body = local_body.replace(
    "The admitted positive-roof map uses the\n"
    "actual sum of D roofs. Its inverse restores that roof.",
    r"""Let \(r_D(x)\) be the sum of the D positive contraction roofs
along the translated orbit. In a collar with coordinate
\(0\leq t\leq r_D(x)\), the roof map is
\((x,t)\mapsto(x,t/r_D(x))\); its inverse is
\((x,s)\mapsto(x,sr_D(x))\). At the endpoints use the stated
mapping-torus gluing, so these maps descend.""",
)
local_body = local_body.replace(
    "the\nadmitted flat degree-zero ruled component",
    "the flat degree-zero ruled component of "
    r"\ref{maps:src:D.2.31}",
)
local_body = local_body.replace("The admitted basis", "The period basis")
local_body = local_body.replace(
    "The admitted lifted flow, its endpoint line ratio,",
    r"The lifted flow of \ref{maps:src:D.2.32}--\ref{maps:src:D.2.33}, its endpoint line ratio,",
)
local_body = local_body.replace(
    "the line-flow and roof inverse described in LD/L8/L9.",
    r"the inverse line flow of \ref{maps:src:D.2.32}--\ref{maps:src:D.2.33} "
    "and the inverse roof map displayed above.",
)
local_body = local_body.replace(
    "These are actual kernel maps from the admitted\nGysin constructions.",
    "These kernel maps use the displayed Gysin projection and its section.",
)
local_body = local_body.replace(
    "The fresh calculation computes the saturated span\n"
    "of the return image and (L29) or (L30), verifies (L31), and\n"
    "constructs its quotient and section (L7).",
    "Taking the saturated span of the return image and the extra\n"
    "generator gives the quotient and section in (L7).",
)
local_body = local_body.replace(
    "in the admitted raw\nprofiles", "in the defining profiles")
local_body = local_body.replace(
    "the admitted\ngeometric normal", "the geometric normal of "
    r"\ref{maps:src:D.2.33}")
local_body = local_body.replace(
    "in the common exterior quotient of LH", "in the common exterior quotient")
local_body = local_body.replace(
    "In the common exterior quotient of LH", "In the common exterior quotient")
local_body = local_body.replace(
    "In the exterior of LH", "In the exterior")
local_body = local_body.replace(
    "by the mixed unit\nrelations\nof Section 2", "by the mixed unit relations above")
local_body = local_body.replace(
    "relations of the main proof", "relations above")
local_body = local_body.replace(
    "the mixed unit\nrelations of the main proof", "the mixed unit relations above")
local_body = local_body.replace(
    "The complete homology algorithm\nbelow needs only its rank and free kernel, but the splitting\nuses these integer columns.",
    "The free-rank calculation uses its rank, and the integral\n"
    "splitting uses all these integer columns.",
)
local_body = local_body.replace(
    "No equality of the D-powered orbits with the old orbits is\n"
    "asserted when D shares a component order.",
    "The orbit count is taken after raising the actual permutation to D.",
)
local_body = local_body.replace(
    "No unrecorded change of marking is\nused to identify a kernel.",
    "These paired shears preserve the marked kernel.",
)
local_body = local_body.replace(
    "No rank-only argument is used to discard torsion.",
    "The full Wang quotient retains its torsion in this calculation.",
)
local_body = local_body.replace(
    "For a multiplicative fibre, its central cycle has",
    r"""The nearby elliptic area specializes to the whole central
fibre \(\sum_C\mu_C[C]\), followed by the orbit quotient.
Its coefficient on an orbit O is
\(\sum_{C\in O}\mu_C>0\). The fixed angular-return torus
\(\delta\wedge\ell_D\) has angular-return coefficient \(g_D>0\),
where \(g_D\) is its primitive return length. The flat angular
gauge gives its product map; projecting to that coordinate and
dividing by \(g_D\) on its image is its inverse. The component
coefficients are read in the orbit basis. These two images are
independent. The rational fibre coinvariant has dimension two,
so its map to the cap is injective. This applies to every
zero-Chern additive original, including the original odd stars.

For a multiplicative fibre, its central cycle has""",
)
# Use collar-compatible smooth representatives of the line and roof maps.
local_body = local_body.replace(
    r"[w,x,s]\longmapsto[e^{s\log u(x)}w,x,s]",
    r"[w,x,s]\longmapsto[e^{\zeta(s)\log u(x)}w,x,s]",
)
local_body = local_body.replace(
    "removes the endpoint line multiplier; the inverse uses its\n"
    "negative exponent.",
    r"""removes the endpoint line multiplier. Here \(\zeta\) is smooth,
zero near 0 and one near 1. The inverse uses the negative
exponent. Constancy at the two ends makes these maps smooth
in the mapping-torus collar coordinates.""",
)
local_body = local_body.replace(
    r"""Let \(r_D(x)\) be the sum of the D positive contraction roofs
along the translated orbit. In a collar with coordinate
\(0\leq t\leq r_D(x)\), the roof map is
\((x,t)\mapsto(x,t/r_D(x))\); its inverse is
\((x,s)\mapsto(x,sr_D(x))\). At the endpoints use the stated
mapping-torus gluing, so these maps descend.""",
    r"""Let \(r_D(x)\) be the sum of the D positive contraction roofs.
On the compact plumbing collar choose \(c>0\) with
\(c\max r_D<1\), and a smooth nonnegative function
\(\phi\) supported in \((0,1)\), with integral one.
Put \(\Phi(s)=\int_0^s\phi(t)\,dt\) and
\[
 f_x(t)=ct+(1-cr_D(x))\Phi(t/r_D(x)),\qquad
              0\leq t\leq r_D(x).
\]
Then \(f_x(0)=0\), \(f_x(r_D(x))=1\), and
\[
 f_x'(t)=c+(1-cr_D(x))\phi(t/r_D(x))/r_D(x)>0.
\]
The roof map is \((x,t)\mapsto(x,f_x(t))\), with inverse
\((x,s)\mapsto(x,f_x^{-1}(s))\).
Near the two ends its coordinates are \(ct\) and
\(1-c(r_D(x)-t)\), so the mapping-torus transition has the
same constant slope c on both sides. The maps therefore
descend smoothly and carry the actual variable roof.""",
)
local_body = local_body.replace(
    "This establishes (L4) on the fibre image; it\n"
    "does not assert that every component cycle is fixed by every deck\n"
    "map.",
    "This establishes (L4) on the fibre image.",
)
local_body = local_body.replace(
    "Sections 2--5", "The cap calculations below")
local_body = local_body.replace(
    "Section 3", "the zero-Chern and rank-one constructions")
local_body = local_body.replace(
    "Section 4", "the principal-bundle construction")
local_body = re.sub(
    r"(?m)^## ([1-6])\. (.*)$",
    lambda m:"## "+str(7+int(m[1]))+". "+m[2], local_body)
# Separate the local kernel-coordinate names from the global graph kernel.
local_body = local_body.replace(
    r"kernel basis \(K_D\)", r"kernel basis \(\mathsf K_D\)")
local_body = local_body.replace(
    r"inverse \(L_D\)", r"inverse \(\mathsf L_D\)")
local_body = local_body.replace(
    r"L_DK_D", r"\mathsf L_D\mathsf K_D").replace(
    r"K_DL_D", r"\mathsf K_D\mathsf L_D")

matrix = between(section(main, 7), "The full target")
matrix = "## 14. The complete relation matrix\n\n"+matrix
matrix = matrix.replace(
    "in the companion\nnote", "displayed above")
relative = section(main, 8).replace("## 8. ", "## 15. ", 1)
relative = relative.replace("and the companion\nbases", "and the cap bases above")
relative = relative.replace(
    "in the\ncompanion note", "above")
relative = relative.replace(
    "This is the admitted D.WP11 construction with all the\n"
    "new angular coordinates retained.",
    r"This is \eqref{maps:eq:D.WP11} with its complete angular coordinates.",
)
group = section(main, 9).replace("## 9. ", "## 16. ", 1)
group = group.replace(
    "in the admitted LD group proof", r"in the group proof of \ref{maps:src:D.2.37}")
ranks = section(main, 10).replace("## 10. ", "## 17. ", 1)
ranks = ranks.replace(
    "The admitted weight-one inverse", "The weight-one inverse of "
    r"\ref{maps:src:D.2.31}")
ranks = ranks.replace(
    "in the companion (L11)", "in (L11)")

scope = r"""## 18. The two pattern sets

The all-star-original set has 459 patterns. The broad set has 495,
allowing finite-good \(III^*,IV^*\) replacements while keeping odd
\(I_\nu^*\) caps original. Their inclusion fixes each labelled
choice, and the retraction replaces only a finite-good \(III^*\)
or \(IV^*\) choice by its original cap. Reading the allowed
independent choices at those positions describes every inverse
image of the retraction. Its composite with inclusion is identity.

At each of the 172 natural rows, form the product of its allowed
choices away from the selected cusp. The zero-Chern original and
Mumford choice have the same complete boundary kernel by their
node-chart and flat-gauge maps and their common saturated fibre
kernel. At a nonzero-Chern original the extra Gysin generator
has nonzero rational value \(-Db/(gq)\) or \(-Db/(g\nu)\);
the quotient functional therefore detects its class outside the
Mumford kernel. The invertible rational map \(\Lambda^2S_D\)
preserves both assertions. Finite choices keep their order,
power vector and all five Thom columns. These rules give the
following finite product enumeration, in which the two columns
retain their literal pattern maps.

| Profile | All star caps original | Broad finite-good scope |
|:---|---:|---:|
| OS43/II | 4 | 8 |
| OS43/default | 6 | 12 |
| OS45/II | 12 | 12 |
| OS45/default | 12 | 12 |
| OS46/II | 4 | 4 |
| OS46/default | 6 | 6 |
| OS47/II | 24 | 24 |
| OS47/III | 24 | 24 |
| OS47/default | 30 | 30 |
| OS49/II | 4 | 8 |
| OS49/III | 8 | 16 |
| OS49/default | 14 | 28 |
| OS50/II | 4 | 4 |
| OS50/IV | 8 | 8 |
| OS50/default | 14 | 14 |
| OS55/II | 24 | 24 |
| OS55/default | 30 | 30 |
| OS56/II | 46 | 46 |
| OS56/III | 54 | 54 |
| OS56/IV | 54 | 54 |
| OS56/default | 77 | 77 |
| Total | 459 | 495 |

The formulas for the graph, finite actions, kernel transfer and
relative attachment hold for every positive d with odd g and
every finite number of regular sites. The integer operations
retain every allowed order, numerator, affine power and clutch.
"""
even = section(post, 4)
even = between(even, "Take the natural OS43/default row")
even = "## 19. The role of oddness\n\n"+even
even = even.replace(
    "proved before taking an odd\nhalf", "obtained before taking an odd half")
even = even.replace(
    "This is a concrete two-primary ambiguity in the stipulated\nmarking conditions.",
    "Thus the anti-invariance and zero-evaluation conditions can have\n"
    "two different integral lifts when both a and D are even.",
)

# Mathematical references for auxiliary display tags; only the seven original
# permanent OW tags survive in the receiving theorem and proof.
refs = {
    "F": "the displayed full wedge image",
    "C": "the displayed integral cocycle",
    "P": "the covering naturality identity",
    "S": "the integral graph splitting",
    "J": "the last peripheral insertion",
    "N1": "the norm-image construction",
    "N2": "the projected-lattice coordinates",
    "N3": "the projected power coordinates",
    "N4": "the two freeness conditions",
    "N5": "the holomorphic averaging formula",
    "N6": "the core presentation",
    "N7": "the root boundary map",
    "N8": "the core power relation",
    "H1": "the peripheral sweep shear",
    "H2": "the wedge-norm identity",
    "K1": r"\eqref{maps:eq:D.OW4}",
    "B1": r"\eqref{maps:eq:D.OW2}",
    "B2": r"\eqref{maps:eq:D.OW3}",
    "B3": "the full unchanged-cap columns",
    "G1": "the exterior degree-one presentation",
    "G2": "the logarithmic normal-disc columns",
    "G3": "the finite-first second-homology quotient",
    "G4": "the free relative component group",
    "G5": "the cusp component-disc columns",
    "G6": "the integral relative sequence",
    "G7": "the displayed relative splitting",
    "P1": "the inverse vanishing-word formulas",
    "P2": "the local root-path presentation",
    "P3": "the full Seifert presentation",
    "P4": "the abelianization matrix",
    "P5": "the rational Euler equation",
    "R1": "the rational period isomorphism",
    "R2": "the scalar delta-sweep relation",
    "R3": "the rank of the full boundary cokernel",
    "R4": "the relative component rank",
    "R5": "the bridge-kernel rank",
    "R6": "the displayed second Betti number",
    "R7": "the displayed third Betti number",
    "R8": "the integral homology table",
    "L1": r"the covering \(p_D\)",
    "L2": "the fibre transfer",
    "L3": "the two covering-square identities",
    "L4": "the transfer identity on the fibre image",
    "L5": r"\eqref{maps:eq:D.OW4}",
    "L6": "the reversible kernel Smith map",
    "L7": "the quotient and kernel inverse identities",
    "L8": "the cover and transfer on fibre images",
    "L9": "the short-period matrix C",
    "L10": "the cusp normalization matrix",
    "L11": "the cusp homology table",
    "L12": "the interleaved cusp period basis",
    "L13": "the cusp fibre quotient and section",
    "L14": "the cusp boundary degree-one coordinates",
    "L15": "the ray-character normal-disc map",
    "L16": "the two disc-kernel equations",
    "L17": "the integral component-disc kernel basis",
    "L18": "the exterior cusp normal-disc columns",
    "L19": "the exponential line gauge",
    "L20": "the additive orbit homology",
    "L21": "the multiplicative orbit homology",
    "L22": "the primitive rank-one period basis",
    "L23": "the four rank-one specialization maps",
    "L24": "the non-narrow period basis",
    "L25": "the primitive component Chern vector",
    "L26": "the nonzero-Chern cap homology",
    "L27": "the additive fibre shear",
    "L28": "the primitive Gysin covector",
    "L29": "the additive extra kernel generator",
    "L30": "the multiplicative extra kernel generator",
    "L31": "the cover and alternating-value formulas",
    "L32": "the full additive fixed basis",
    "L33": "the marked global fixed-normal image",
    "L34": "the boundary Wang sequence",
    "L35": "the general component-disc boundary",
}
body = "\n\n".join([
    intro, degree_one, wedge_part, elliptic, graph_start, involution,
    cocycle, same, graph_end, norms, normal, finite, shears, local_body,
    matrix, relative, group, ranks, scope, even,
])
body = body.replace("Equations (L3)--(L4)", "The covering-square and transfer identities")
body = body.replace("Equations (H1)--(H2)", "The sweep and norm identities")
body = body.replace("(B1)--(B3)", "the full relation matrix")
body = body.replace("Equations (G7), (R3) and (R5)",
                    "The relative splitting and the two rank formulas")
for key, value in refs.items():
    body = re.sub(r"\s*\\tag\{"+re.escape(key)+r"\}", "", body)
    body = body.replace("("+key+")", value)
body = body.replace(
    "in the fresh proof", "above").replace(
    "of the fresh proof", "above")
body = body.replace("in the frozen derivation", "above")
body = body.replace("the admitted ", "the ").replace("The admitted ", "The ")
body = body.replace("admitted ", "")
body = body.replace("The companion fresh file", "The cap construction")
body = body.replace("Section 1", "the degree-one image construction")
body = body.replace("Section 2", "the full wedge-image calculation")
body = body.replace("Section 3", "the marked graph construction")
body = body.replace("Section 4", "the normal-torus calculation")
body = body.replace("Section 5", "the finite quotient construction")
body = body.replace("Section 6", "the peripheral shear construction")
body = body.replace("Section 7", "the unchanged-cap kernels")
body = body.replace("Section 8", "the relative attachment construction")
body = body.replace("Section 9", "the fundamental-group calculation")
body = body.replace("Section 10", "the degree-one image construction0")
body = body.replace("the degree-one image construction0", "the free-rank calculation")
body = body.replace("the companion", "the displayed")
body = body.replace("Bezout", "Bézout").replace("Poincare", "Poincaré")
body = body.replace(
    "No primitivity of \\(A-I\\)\nis imposed.",
    "The projected-lattice calculation retains all nonunit factors of \\(A-I\\).")
body = body.replace("rather than declared units", "with their values")
body = body.replace(
    "There is no unknown torsion component in the\nnorm sweep.",
    "The norm sweep has zero torsion coordinate.")
body = body.replace("None of this construction uses", "This construction applies without")
body = body.replace(
    "including when it has torsion", "with all its torsion generators")
body = body.replace(
    "not discarded", "retained")
body = body.replace(
    "rather than one alternating functional", "with all fibre coordinates")
body = body.replace(
    "No bound on their number or orders is used.",
    "Their number is any finite nonnegative integer and their orders are arbitrary.")
body = body.replace(
    "since the underlying 2-by-2\nmatrix", "since the underlying two-by-two\nmatrix")
body = body.replace(
    "because the four mixed unit\nrelations of the main proof include both elliptic-angular\ncoordinates.",
    r"by \eqref{maps:eq:D.OW7} and its displayed wedge preimages.")
body = body.replace(
    "Thus its actions on the\ntwo ends of the graph sequence are respectively",
    "The cellular filtration over the base vertex and edges has\n"
    "degree-two fibre quotient C_D and edge-cycle kernel K_D.\n"
    "The edge boundary is [A_i(D)-I]; its two-step filtration gives\n"
    "the exact sequence below, with no higher base cells. Thus the\n"
    "involution acts on its two ends respectively")
body = body.replace(r"A_i\lambda=\lambda", r"A_i(D)\lambda=\lambda")
body = body.replace(r"A_i^m=I", r"A_i(D)^m=I")
body = body.replace(r"A_i^j\lambda", r"A_i(D)^j\lambda")
body = body.replace(
    "q_D value zero", "q_D value zero")
body = body.replace(
    "anti-invariant.\nIts marked evaluation is zero.",
    "anti-invariant. Its marked evaluation is zero.")
body = body.replace(
    r"\((0,J_i u)\), not merely a vanishing free coordinate.",
    r"\((0,J_i u)\), including a zero torsion coordinate.")
body = body.replace(
    "bar cycle [x|y]-[y|x]", r"bar cycle \([x|y]-[y|x]\)")
body = body.replace(
    "Its coboundary on (x,w),(y,z),(t,u)",
    r"Its coboundary on \((x,w),(y,z),(t,u)\)")
body = body.replace(
    "For integers u,v with ua+vD=g,", r"For integers \(u,v\) with \(ua+vD=g\),")
body = body.replace(
    "an integer multiple of (Db,a)", r"an integer multiple of \((Db,a)\)")
body = body.replace("its exact Z/g\nsummand", r"its exact \(\mathbb Z/g\)"+"\nsummand")
body = body.replace(
    "Equationsthe", "The")
body = re.sub(
    r"Equations\s+the two covering-square identities--the transfer identity on the fibre image",
    "The covering-square and transfer identities", body)
body = body.replace(
    "the transfer identity on the fibre image on the fibre image",
    "the transfer identity on the fibre image")
body = body.replace(
    "In the local marking the cusp boundary degree-one coordinates",
    "In the cusp boundary degree-one marking")
body = body.replace(
    "Formula the ray-character normal-disc map becomes",
    "The ray-character normal-disc map becomes")
body = body.replace(
    "component and the four primitive classes the four rank-one specialization maps",
    "component and the four primitive classes displayed above")
body = body.replace(
    "gives the quotient and section in the quotient and kernel inverse identities",
    "gives the displayed quotient and kernel inverse identities")
body = body.replace(
    r"the geometric normal of \ref{maps:src:D.2.33} section of u",
    r"the geometric u-normal of \ref{maps:src:D.2.33}")
body = body.replace(
    "actual period inverse, retained.",
    "actual period inverse.")
body = body.replace(
    "Formula the general component-disc boundary supplies",
    "The general component-disc boundary supplies")
body = body.replace(
    "explicit columns the exterior cusp normal-disc columns",
    "explicit exterior cusp normal-disc columns")
body = body.replace(
    "the full unchanged-cap columns primitive integer\nbases",
    "the full unchanged-cap columns use primitive integer\nbases")
body = body.replace(
    "In a free presentation for the exterior degree-one presentation",
    "In a free presentation of the exterior degree-one group")
body = body.replace(
    "the full integer cokernel the full relation matrix",
    "the integer cokernel of the full relation matrix")
body = body.replace("translation DQ", r"translation \(DQ\)")
body = body.replace("On mc-v", r"On \(mc-v\)")
body = body.replace("and r=0 otherwise", r"and \(r=0\) otherwise")

# Use the paper's d consistently for the iterate, leaving permanent identities.
# Within mathematics D always denotes the iterate; permanent identifiers D.*
# are left unchanged. This also changes concatenated products Db and G_Dz.
weight_parts = re.split(r"(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))", body)
for i in range(len(weight_parts)):
    if i % 2:
        weight_parts[i] = re.sub(r"D(?!\.)", "d", weight_parts[i])
    else:
        weight_parts[i] = re.sub(r"\bD\b(?!\.[A-Za-z0-9])", "d", weight_parts[i])
body = "".join(weight_parts)
body = body.replace(r"Here \(d=d>0\) denotes the translation iterate.",
                    "The translation iterate is positive.")

# Put prose identifiers in math mode, keeping all existing math/TeX intact.
tokens = {
    "U2": r"U_2", "U3": r"U_3", "R2": r"R_2", "R3": r"R_3",
    "R1": r"R_1", "K_bas": r"K_{\mathrm{bas}}",
    "gamma": r"\gamma", "delta": r"\delta", "lambda": r"\lambda",
    "alpha": r"\alpha", "beta": r"\beta", "rho": r"\rho",
    "nu": r"\nu", "kappa": r"\kappa", "chi": r"\chi",
    "epsilon": r"\epsilon", "tau": r"\tau", "theta": r"\theta",
    "Gamma": r"\Gamma", "H1": r"H_1", "H2": r"H_2", "H3": r"H_3",
    "H4": r"H_4", "H0": r"H_0", "L=0": r"L=0", "L>0": r"L>0",
    "gcd(a,b)=1": r"\gcd(a,b)=1", "g exceeds one": r"g>1",
    "e1": r"e_1", "e2": r"e_2", "e3": r"e_3", "G1": r"G_1",
}
parts = re.split(r"(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))", body)
identifier = re.compile(
    r"(?<![A-Za-z_\\])(?:"
    +"|".join(re.escape(t) for t in sorted(tokens, key=len, reverse=True))
    +r"|[A-Za-z]+_[A-Za-z0-9*]+)(?![A-Za-z_])"
)
greek = {"lambda": r"\lambda", "omega": r"\omega", "xi": r"\xi",
         "ell": r"\ell", "sigma": r"\sigma"}


def math_identifier(m):
    word = m[0]
    if word in tokens:
        value = tokens[word]
    else:
        name, sub = word.split("_", 1)
        sub = sub.replace("D", "d")
        value = greek.get(name, name)+"_{"+greek.get(sub, sub)+"}"
    return r"\("+value+r"\)"


for i in range(0, len(parts), 2):
    parts[i] = identifier.sub(math_identifier, parts[i])
body = "".join(parts)
body = re.sub(r"(?m)^## [0-9]+\. (.*)$",
              lambda m:r"\emph{"+m[1]+".}", body)


def table(m):
    lines = m[0].strip().splitlines()
    cells = [[s.strip() for s in line.strip("|").split("|")] for line in lines]
    assert len(cells) > 2
    output = [r"\begin{center}", r"\small", r"\begin{tabular}{lrr}"]
    for i, row in enumerate(cells):
        if i == 1:
            continue
        output.append(" & ".join(row)+r" \\")
        if i == 0:
            output.append(r"\hline")
    output += [r"\end{tabular}", r"\end{center}"]
    return "\n".join(output)+"\n"


body = re.sub(r"(?m)(?:^\|[^\n]+\|\n)+", table, body)
assert not re.search(r"\\tag\{(?!D\.OW[5-7]\})", body)
assert not re.search(r"\((?:L|N|G|P|R|B)[0-9]+\)", body)
work = LANE / (PREFIX+"receiving_proof_work.md")
work.write_text(body, encoding="utf-8", newline="\n")
p = subprocess.run(
    ["pandoc", "--from=markdown+tex_math_single_backslash+raw_tex",
     "--to=latex", "--wrap=preserve"],
    input=body, text=True, capture_output=True, check=True,
)
assert not p.stderr, p.stderr
proof = "\\begin{proof}\n"+p.stdout.rstrip()+"\n\\end{proof}\n"
proof = proof.replace("\\tightlist\n", "")
statement = (LANE / (PREFIX+"receiving_statement_part.tex")).read_text().rstrip()
receiver = statement+"\n\n"+proof
assert not any(ord(c) < 32 and c not in "\n\t" for c in receiver)
(LANE / (PREFIX+"receiving.tex")).write_text(
    receiver, encoding="utf-8", newline="\n")
for name, expected in frozen.items():
    assert sha256((LANE / (PREFIX+name)).read_bytes()).hexdigest() == expected
print("PASS both frozen fresh mathematical sources unchanged")
print("PASS receiving theorem and proof assembled with eight permanent labels/targets")
print("RECEIVER_LINES", len(receiver.splitlines()))
print("RECEIVER_SHA256", sha256(receiver.encode()).hexdigest())
