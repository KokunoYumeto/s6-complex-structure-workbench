#!/usr/bin/env python3
"""Build the LD receiver from frozen derivations and reviewed post-exposure maps."""
from hashlib import sha256
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
BASE="S6_SERIES_PUBLISH_III_02LD_"
fresh=(LANE/(BASE+"fresh_derivation.md")).read_text()
assert sha256(fresh.encode()).hexdigest()=="8b72bf89e09ce2750b192c7216d94b1b63b436f50554f9a446374a9057ee0284"
post=(LANE/(BASE+"post_exposure_derivation.md")).read_text()
body=fresh[fresh.index("## 1."):fresh.index("## 10.")]
body=(r"Let \(d_0\) be the denominator of the generator height. "
      r"The selected fibre has type \(I_{n_*}\), with \(ab=d_0/n_*\) "
      r"and \(\gcd(a,b)=1\). Put \(\chi=\gamma^*\)."+"\n\n"+body)

def change(old,new):
    global body
    assert body.count(old)==1,(old[:100],body.count(old))
    body=body.replace(old,new,1)

def remove_between(start,end):
    global body
    i=body.index(start);j=body.index(end,i)
    body=body[:i]+body[j:]

# Replace the source-process framing by the mathematical construction inputs.
change("KY's actual section-line coordinates give",
       r"The section-line coordinates of \ref{maps:src:D.2.23} give")
change("The fresh raw-only calculation checks the integrality of every entry\nand the ordered product identity for every one of the 172 rows.",
       "Substitution of the defining elliptic matrices and section cocycles gives\nintegral entries and the ordered product identity on all 172 rows.")
change("For completeness, those 172 rows are reselected as follows.",
       "The finite selection of the 172 rows is as follows.")
change("Enumerating their\nfinite positive factor pairs, without reading a target table,\ngives exactly 172 marked rows.",
       "Enumerating these positive factor pairs gives exactly 172 marked rows.")
change("For each of the 21 raw profiles, the new program computes integer\nmatrices",
       "For each of the 21 defining profiles, integer maximal-minor elimination gives\nmatrices")
change("coefficient and adding gives (2.6). Both products are checked over\nthe integers, and all matrices and preimages are retained in the\nnew exterior data JSON. Thus (2.6) supplies actual inverse sections.",
       "coefficient and adding gives (2.6). On each of the 21 profiles the\ngcd of those maximal minors is one in both degrees. Multiplication\ntherefore gives the displayed integer right inverses.")
remove_between("The new coefficient certificate constructs", "### 2.3")
change("We use the integral fibre class furnished by the admitted L7\nexterior proof.",
       r"We use the integral exterior fibre class of \ref{maps:src:D.2.31}.")
change("origin-disc meridians stated there and in L9.",
       r"origin-disc meridians of \ref{maps:src:D.2.31} and \ref{maps:src:D.2.33}.")
change("The KB normalization calculation applies to this very subgroup.",
       "The normalization complex of the periodic triangular cusp applies to this subgroup.")
change("Over \\(R_D=\\mathbb Z[t]/(t^D-1)\\)",
       "Over \\(\\mathcal R_D=\\mathbb Z[t]/(t^D-1)\\)")
change("The fresh calculation builds\nthese permutations and their D-th powers explicitly.",
       "Raising these permutations to the Dth power and using the inverse\nexponent gives their component bases.")
change("The admitted L7\nand L4/L6 maps prove both weight-one wedge and vector factors.\nThe new finite program checks the vector factors and the\nliteral conjugacy identities directly from the raw data.",
       r"The weight-one vector and wedge maps of \ref{maps:src:D.2.31},"
       "\n"+r"\ref{maps:src:D.2.29} and \ref{maps:src:D.2.30} have unit nonzero Smith factors.")
change("Use the actual zero-degree line frames on the normalized\ncomponents from L7.",
       r"Use the zero-degree component line frames of \ref{maps:src:D.2.31}.")
change("roofs on the D translates; the smooth roof reparametrization\nand its inverse from L7 apply to that actual positive function.",
       r"roofs on the D translates; the positive-roof map and its inverse of"
       "\n"+r"\ref{maps:src:D.2.31} apply to that function.")
change("The integral line-frame map \\(S_P\\) from L7 is unchanged.",
       r"The integral line-frame map \(S_P\) of \ref{maps:src:D.2.31} is unchanged.")
change("Let \\(U_j\\) be its component-orbit basis,",
       r"""Let \(K_0\subset N\) be the central Kodaira fibre in its plumbing
neighbourhood. Its inclusion is an integral homology equivalence
and commutes with the translation. The induced map of mapping
tori is therefore a map of their Wang complexes
\(\operatorname{Cone}(t_*-I)\), inducing an isomorphism on homology.
After product with the angular circle, its degree-two map sends
the component-orbit cycles and angular-return torus to the same
cycles in the cap. Their inverse coordinates are given below.

Let \(U_j\) be its component-orbit basis,""")
change("gauge of L8, or equivalently compose its endpoint isotopy",
       r"gauge of \ref{maps:src:D.2.32}, and compose its endpoint isotopy")
change("composition of the original L9 lifted holomorphic flow,",
       r"composition of the lifted holomorphic flow of \ref{maps:src:D.2.33},")
change("The logarithm and reciprocal gauge used in L9 therefore",
       r"The logarithm and reciprocal gauge of \ref{maps:src:D.2.33} therefore")
change("projection and its Gysin inverse, as in L9.",
       r"projection and its Gysin inverse in \ref{maps:src:D.2.33}.")
change("with \\(QR_\\pi=I\\); the new program retains this map.",
       "with \\(QR_\\pi=I\\).")
remove_between("The new program verifies the moving-plane inverse as", "### 6.2")
change("the admitted KY proof.",r"\ref{maps:src:D.2.23}.")
change("by the admitted L7\nintegral map and inverse.",r"by the integral map and inverse of \ref{maps:src:D.2.31}.")
change("identity, and every map above restricts to its admitted\nunweighted counterpart.",
       "identity, and every map above restricts to its weight-one counterpart.")

# Give the additional original d=0 assertion by exact image and quotient maps.
zero=post[post.index("Let \\(G_0\\)"):post.index("The new program computes both complete constant matrices")]
zero=zero.replace("in the fresh proof","above").replace("The primitive raw profile matrix","The primitive profile matrix")
zero=zero.replace("The five polynomial wedge preimages in the fresh proof","The five polynomial wedge preimages above")
zero=zero.replace("G_0",r"\widetilde G_0")
body=body.replace("### 2.3",r"\emph{The constant specialization.}"+"\n\n"+zero+"\n### 2.3",1)

# Preserve the permanent graph formula with both homology degrees.
graph=r"""The edge projection and the marked fibre class give
\[
 H_1(V_D)=\mathbb Z\gamma\oplus\mathbb Z^{N-1},\qquad
 H_2(V_D)=\mathbb Zs\oplus K_D.
 \tag{D.WP10}\hypertarget{tag-027P}{}\label{maps:eq:D.WP10}
\]
"""
change("The map\n\\[\n H_2(V_D;\\mathbb Z)",
       graph+"\nThe corresponding map\n\\[\n H_2(V_D;\\mathbb Z)")

# Insert the complete cusp Wang quotient and section in its actual lattice.
cusp=post[post.index("The ordered integral basis"):post.index("## 4.")]
cusp=cusp.replace("The new program checks all these identities\nas polynomials in D.",
                  "Substitution verifies these polynomial identities for every D.")
cusp=cusp.replace("SCe",r"S_{\rm bas}Ce")
cusp=cusp.replace("This\nsettles every assertion in original proof item 9, including its\nintegral boundary group.","")
cusp="Write \\(S_{\\rm bas}=(u,\\delta)\\) and put \\(L=(r,\\gamma)\\). "+cusp
start=body.index("The boundary return has short-column matrix")
end=body.index("Put \\(W_D=V_D\\cup N_D\\)",start)
body=body[:start]+cusp+"\n"+body[end:]

# Replace the global proof by the full finite-first relative maps, preserving
# the two exact original sequence/rank displays.
start=body.index("We first filled the cusp by (3.3)")
end=body.index("## 8.",start)
relative=post[post.index("Attach the k finite"):post.index("## 5.")]
relative=relative.replace("in the fresh\nproof","above").replace("in the fresh proof","above")
relative=relative.replace("already proved","proved above")
relative=relative.replace("This is the original display D.WP11 with its full integral maps.\n","")
relative=relative.replace("This is the original D.WP12, including every torsion-index effect\ninside the kernel basis. ",
                          "The integral basis includes every torsion-index effect. ")
relative=relative.replace(r"\longrightarrow0,\qquad C_D=\operatorname{coker}B .",
                          r"\longrightarrow0,\qquad C_D=\operatorname{coker}B ."
                          "\n"+r"\tag{D.WP11}\hypertarget{tag-027Q}{}\label{maps:eq:D.WP11}")
relative=relative.replace("                         D-1+\\beta+L+r.\n",
                          " \\operatorname{rank}\\ker\\Gamma=D-1+\\beta+L+r.\n"
                          r"\tag{D.WP12}\hypertarget{tag-027R}{}\label{maps:eq:D.WP12}"+"\n")
relative=relative.replace("The map from the free component group to H1(E) has rank",
                          "Denote the component-disc boundary map by \\(\\Gamma\\). "
                          "Its rank is")
relative=relative[:relative.index("The common inclusion of V identifies")]+r"""
The exact sequence and the integral section constructed above give
\[
              H_2(X)=C_D\oplus\mathbb Z^{D-1+\beta+L+r}.
\]
Its inverse reads the relative component coordinates and then the
remaining exterior class modulo B.
"""
body=body[:start]+relative+"\n"+body[end:]

examples=r"""\emph{Existence at every finite-good position.}

There are 102 finite-good positions in the 172 rows. In the fixed
basis \(F_1=(\delta,\ell_1)\), the norm-coordinate basis \(H_1\)
has the following projected coordinates
\(w_\pm=hH_1^{-1}(1,\pm1)^t\). Here q is the component-group order.

| q | \(g_0\) | Positions | \(w_+\) | \(w_-\) |
|---:|---:|---:|:---|:---|
|1|1|34|(1,1)|(1,-1)|
|2|1|17|(2,1)|(2,-1)|
|2|2|17|(1,2)|(1,-2)|
|3|1|17|(3,1)|(3,-1)|
|3|3|17|(1,3)|(1,-3)|

These follow by summing \(I+A_1+\cdots+A_1^{h-1}\) and applying
the fixed-coordinate inverse \((x_\delta,x_\gamma/g_0)\):
\(H_1=\operatorname{diag}(h/q,h)\) when \(g_0=1\), and
\(H_1=\operatorname{diag}(h,h/q)\) when \(g_0=q>1\).
Both displayed vectors are primitive in every case.

The integral conjugacy \(H_D\) above satisfies
\[
 H_D\delta=\delta,\qquad H_D\ell_1=\epsilon\ell_D,\qquad
 P_DH_D=H_DP_1,\qquad P_D=N_h(A(D))/h .
\]
Its inverse has last column
\((-\epsilon(1-\epsilon D)bz,0,\epsilon)\).
Since \(\epsilon D\equiv1\pmod{g_0}\), both matrices are integral.
Thus it identifies the two projected lattices with inverse
\(H_D^{-1}\), and
\[
       H_D^{-1}(\delta+\ell_D)=\delta+\epsilon\ell_1 .
\]
In the projected basis \(\operatorname{diag}(1,\epsilon)H_1\),
the vector \(\delta+\ell_D\) therefore has coordinates
\(w_\epsilon\). Any other integral basis is related by a
unimodular matrix V, giving the coordinate maps
\(w_\epsilon\mapsto V^{-1}w_\epsilon\) and its inverse V.
Consequently \(\delta+\ell_D\) is primitive in the projected
lattice for every permitted D. Its delta coordinate in Lambda
is one. For every \(m=hk\) both criteria in
\eqref{maps:eq:D.WP5} hold, with t=1. This proves existence
of every finite-good option used in the catalogue.

"""
body=body.replace("### 6.2",examples+"\n### 6.2",1)

# The finite selection and both literal star scopes are part of the theorem.
start=body.index("## 9.")
enum=body[start:]
enum=enum[enum.index("Let \\(\\mathcal P\\)"):]
enum=enum[:enum.index("The whole set of 495 row-and-site records")]
enum=enum.replace("the fresh proof","the preceding construction")
enum=enum.replace("The new program gives the following complete totals.",
                  "The finite factor and site-option enumeration gives the following totals.")
enum=enum.replace("in the supplied raw\ndata.","in the defining profile data.")
enum=enum.replace("without using a historical target table.","by the displayed inverse.")
enum=enum.replace("The precise 36 broad patterns omitted by S are below.\nThe zero column is the one-based selected site, and\neach option string follows the raw ordered fibre list.\nThe final column is the projection pi.",
r"""The 36 patterns in the broad set outside the all-star-original subset
are distributed as follows. The map \(\pi\) changes exactly the
\(\mathrm{III}^*/\mathrm{IV}^*\) finite label F to O.
Its inverse over a given pattern lists the permitted independent
O/F values at those positions. The inclusion is the all-O section.

| OS | Profile | Omitted patterns |
|---:|:---|---:|
|43|default|6|
|43|II|4|
|49|default|14|
|49|II|4|
|49|III|8|

The local map changed by this projection is exactly the finite
Thom map versus the original fixed-normal map and its possible
fibre column. Thus the formulas hold on all 495 patterns and
restrict through the inclusion to the 459-pattern subset.
""")
# The finite rule and the five profile counts replace the redundant 36-row listing.
enum=enum[:enum.index("| OS | Profile | a | b | Zero | Broad pattern | Projection |")] if "| OS | Profile | a | b | Zero | Broad pattern | Projection |" in enum else enum
body=body[:start]+"## 9. Enumeration and the two starred-cap scopes\n\n"+enum

# Remove implementation narration and replace defensive clauses by their maps.
phrases={
"In particular no replacement\nof this multiplier by a constant is used. ":"",
"The inverse identification over a chosen sheet is the inverse period\nexponential with the new gamma coordinate, not an asserted\nidentification of two analytic germs.":"The inverse over a chosen sheet is the period exponential with the new gamma coordinate.",
"This construction does not\nmake a change of fan based on an equality of monodromy.":"The identity on the infinite charts keeps the fan and every chart unit fixed.",
"section s_0; no saturation or finite-index assumption is used.":"section s_0.",
"component invariants and quotients, not two unmarked germs.":"component invariants and quotients.",
"these\nmaps integrally, including the III/IV transitive cases;\nthere is no hidden division of an ordinary fibre by q.":"these\nmaps integrally, including the transitive III and IV cases.",
"and is not being identified with this\nnormal torus without those additional shears.":"and their inverse section changes must include those additional shears.",
"give both inverse lattice maps, without replacing P Lambda\nby the smaller fixed integral lattice.":"give both inverse maps for the projected lattice.",
"it does not in general change it by\n\\(m\\lambda\\).":"its norm is \\(N_m\\lambda\\).",
"without discarding the fifth column.":"with the root column included.",
"This proves the exact\nrelation and does not remove the torsion from the core\nbefore taking the normal map.":"This proves the exact relation in the normal map from the full core group.",
"No identification of these two lift conventions is\nused without the displayed norm morphism.":"The norm morphism is the change of peripheral power in both cases.",
"They settle the\nexception without asserting that the cusp alone kills\nthe index-three quotient.":"The original star cap therefore kills the remaining index-three quotient.",
"No bound on their number or orders is used.":"The same eliminations apply to every finite number of sites and every positive order.",
"retain exact integral groups and not only their orders.":"give the integral dual groups and their inverse coordinates.",
"This proves every target group at both Euler values\nand at every permitted D, with all orders, affine\ncoordinates, regular sites and clutch integers\nunrestricted as stated.":"This proves the displayed homology groups for every allowed parameter.",
"This proves\nthe target's rank-one correction in both cases using\nthe actual period lattice and the actual fan.":"This proves the rank-one component contribution using its period lattice and fan.",
"original. Section 9 records separately the statement's\nnarrower literal reading that retains every starred cap.":"original. The all-star-original subset is described in the enumeration.",
"These are exactly the target's D.WP6--D.WP7 columns,\nevaluated by the primitive graph inverse in (2.13).":r"These are \eqref{maps:eq:D.WP6}--\eqref{maps:eq:D.WP7}, evaluated in the primitive graph coordinates.",
}
for old,new in phrases.items():
    assert old in body,old[:100]
    body=body.replace(old,new)

# Make finite computation assertions positive and local.
body=body.replace("The cached component coordinate","The defining component coordinate")
body=body.replace("the cached component indexing","the defining component indexing")
body=body.replace("the original raw matrices","the defining matrices")
body=body.replace("raw profiles","defining profiles").replace("raw profile","defining profile")
body=body.replace("recorded lattice","marked lattice")
body=body.replace("actual ","").replace("admitted ","")
body=body.replace("fresh ","")
body=body.replace("retained original","kept original")
body=body.replace("new fixed","weight-D fixed")
body=body.replace("the new lattice","the weight-D lattice")
body=body.replace("the new gamma","the weight-D gamma")
body=body.replace("new suspension","weight-D suspension")
body=body.replace("Poincare","Poincaré").replace("Bezout","Bézout").replace("Neron","Néron")
body=re.sub(r"\bP1\b",lambda m:r"\(\mathbb P^1\)",body)
body=body.replace("from KY",r"of \ref{maps:src:D.2.23}")
body=body.replace("the L9 calculation",r"\ref{maps:src:D.2.33}")
body=body.replace("the cached component coordinate","the defining component coordinate")
body=body.replace("cached component indexing","defining component indexing")
body=body.replace("as checked from\ntheir defining residues in",r"by the defining residue maps in")
body=body.replace("It obtains them","Obtain them")
body=body.replace("The mixed wedge calculation therefore prove","The mixed wedge calculation proves")
body=body.replace("It leaves the equation the component-degree equation",
                  "It preserves the component-degree equation")

# Replace auxiliary local display numbers by mathematical names or permanent references.
body=re.sub(r"\s*\\tag\{[0-9]+\.[0-9]+\}","",body)
refs={
"1.1":r"the covering \(p_D\)",
"1.2":r"\eqref{maps:eq:D.WP2}",
"2.1":r"the displayed section-line matrix",
"2.4":r"the component-degree equation",
"2.6":r"the identities \(U_2R_2=I_2,\ U_3R_3=I_3\)",
"2.7":r"the formula for \(R_D\)",
"2.8":r"the displayed mixed wedge coordinates",
"2.9":r"the three mixed wedge generators",
"2.10":r"\eqref{maps:eq:D.WP3}",
"2.11":r"the displayed wedge-image basis",
"2.12":r"\eqref{maps:eq:D.WP10}",
"2.13":r"the last peripheral insertion formula",
"3.1":r"the displayed cusp homology",
"3.2":r"the cusp relative sequence",
"3.3":r"the displayed cusp-relative decomposition",
"4.1":r"the two component-permutation identities",
"5.1":r"the displayed additive matrix",
"5.2":r"the conjugacy \(A(D)H_D=H_DA(1)\)",
"5.3":r"the displayed fixed basis and inverse",
"5.4":r"the displayed component decomposition",
"5.5":r"the fibre formula \(f_D\)",
"5.6":r"\eqref{maps:eq:D.WP7}",
"5.7":r"the displayed component-kernel basis",
"5.8":r"the additive value \(\omega_D(k_D)=-Db/q\)",
"5.9":r"the three additive kernel columns",
"5.10":r"the displayed multiplicative matrix",
"5.11":r"the multiplicative value \(\omega_D(k_D)=-Db/\nu\)",
"6.1":r"the map \(Q=H^{-1}F^{-1}N_h\)",
"6.2":r"the projected-lattice formula",
"6.3":r"the projected coordinates \(w\)",
"6.4":r"\eqref{maps:eq:D.WP5}",
"6.5":r"the displayed presentation of \(H_1(F_0)\)",
"6.6":r"the displayed core homology",
"6.7":r"the root boundary map",
"6.8":r"\eqref{maps:eq:D.WP6}",
"7.1":r"the relative cokernel identification",
"7.3":r"\eqref{maps:eq:D.WP11}--\eqref{maps:eq:D.WP12}",
"8.1":r"the vertical quotient",
"8.5":r"the displayed Euler criterion",
"8.6":r"the scalar graph relation",
}
body=body.replace("Equations (2.8)--(2.9)","The mixed wedge calculation")
body=body.replace("Equations (5.4)--(5.5)","The component decomposition and fibre map")
body=body.replace("(6.1)--(6.2)","the projection and its section")
body=body.replace("(8.5)--(8.6)","the Euler criterion and scalar graph relation")
body=re.sub(r"\bEquation\s+(?=\([0-9])","",body)
for key,value in refs.items():
    body=body.replace("("+key+")",value)
sec={
"Section 2":"the component-coordinate comparison",
"Section 4":"the component-orbit calculation",
"Section 5.3":"the additive product construction",
"Section 5.4":"the multiplicative period construction",
"Section 5.5":"the zero-Chern multiplicative construction",
"Section 5":"the cap constructions",
"Section 6.4":"the regular and clutch construction",
"Section 6":"the finite quotient construction",
"Section 7":"the relative attachment argument",
"Section 8":"the fundamental-group calculation",
"Section 9":"the enumeration",
}
for key in sorted(sec,key=len,reverse=True):
    body=body.replace(key,sec[key])
body=body.replace("by the identities","using the identities")
body=body.replace("Equation\n","")
body=body.replace("By the conjugacy","Using the conjugacy")
body=body.replace("By the identities","Using the identities")
body=body.replace("The formula for", "The formula for")
body=re.sub(r"(?m)^the (covering|formula|displayed)",lambda m:"The "+m[1],body)
body=body.replace("These are exactly the target's","These are")
body=body.replace("the original display D.WP11","the relative sequence")

# Unify the iteration variable with the theorem while preserving D_B.
body=body.replace("D","d").replace("d_B","D_B")
body=body.replace("d.WP","D.WP").replace("maps:src:d.","maps:src:D.")
body=body.replace("d7",r"\(D_7\)")
body=body.replace("K_D","K").replace("K_d","K")
body=body.replace("If K is its basis matrix, the square matrix\n\\([R_d\\ K]\\)",
                  "If \\(K_{\\rm bas}\\) is its basis matrix, the square matrix\n\\([R_d\\ K_{\\rm bas}]\\)")
body=body.replace("K coordinates","kernel coordinates")
body=body.replace("K_D coordinates","kernel coordinates")
body=body.replace("It leaves the equation the component-degree equation",
                  "It preserves the component-degree equation")
body=body.replace("matrix \\(C_a\\). the identities",
                  "matrix \\(C_a\\). The identities")
body=body.replace("U_3R_3=I_3\\) gives","U_3R_3=I_3\\) give")
body=body.replace("zero. the displayed cusp homology gives",
                  "zero. The cusp homology gives")
body=body.replace("The mixed wedge calculation therefore prove",
                  "The mixed wedge calculation proves")
body=body.replace("The root boundary map the root boundary map",
                  "The root boundary map")
body=body.replace("period inclusion the covering", "covering")
body=body.replace("the finite factor enumeration the component-degree equation",
                  "the finite factor enumeration given by the component-degree equation")
body=body.replace("sites. the zero-Chern multiplicative construction",
                  "sites. The zero-Chern multiplicative construction")
body=body.replace("denote the component-disc", "Denote the component-disc")
body=body.replace("The weighted cusp, with its boundary torsion retained",
                  "The weighted cusp and its integral boundary")
body=body.replace("Additive lattices, including the retained odd stars",
                  "Additive lattices and odd-star fillings")
body=body.replace("These are the charts used on both\nsides, with the original units retained.",
                  "These charts use the same original units on both sides.")
body=body.replace("Their node identifications and the\nlinearized translation units are retained.",
                  "Use their node identifications and linearized translation units.")
body=body.replace("The u and its conjugates",r"The vector \(u\) and its conjugates")
body=body.replace("The kernel of Q is its image:",
                  "The kernel of Q is the image of A-I:")
body=body.replace("changes the power by\n\\(N_m\\lambda\\); its norm is \\(N_m\\lambda\\).",
                  "changes the power by \\(N_m\\lambda\\).")
body=body.replace("Its inverse over a given pattern lists the permitted independent\nO/F values at those positions.",
                  "The inverse image of a pattern consists of the independently\npermitted O/F values at those positions.")
body=body.replace("image j[r delta]",r"image \(j[r\wedge\delta]\)")
body=body.replace("Subtracting j[r delta]",r"Subtracting \(j[r\wedge\delta]\)")
body=body.replace("chi A_i(d)=chi",r"\(\chi A_i(d)=\chi\)")
body=body.replace("chi(lambda)",r"\(\chi(\lambda)\)")
body=body.replace("has rank nu-2",r"has rank \(\nu-2\)")
body=body.replace("rank nu-2",r"rank \(\nu-2\)")
body=body.replace("equal to A1",r"equal to \(A_1\)")
body=body.replace("first d translates. The translation",
                  "first d translates. Its divisor is\n"
                  r"\(\sum_{j=0}^{d-1}t_{-jQ}^{\,*}\operatorname{div}(u)\), with"
                  "\nall orbit repetitions included. The translation")
body=body.replace("This proves the rank-one component contribution using its period lattice and fan.",
                  "This proves the rank-one component contribution using its period lattice and fan.\n"
                  "The two factorizations cover all 436 zero-free rank-one positions:\n"
                  "316 have narrow P and 120 have non-narrow P. In the narrow case\n"
                  "the long covector has vertical content nu and gamma entry coprime\n"
                  "to nu; in the non-narrow case its vertical content is one.\n"
                  "These statements follow directly from the displayed primitive factors.")
body=body.replace("cover the covering","covering")
body=body.replace("the two component-permutation identities identifies",
                  "the two component-permutation identities identify")
body=body.replace("vector. the component-orbit calculation",
                  "vector. The component-orbit calculation")
body=body.replace("coefficients. the component-orbit calculation",
                  "coefficients. The component-orbit calculation")
body=body.replace("It preserves the component-degree equation unchanged",
                  "It preserves the component-degree equation")
body=body.replace("homomorphism H2 to Z",r"homomorphism \(H_2\to\mathbb Z\)")
body=body.replace(r"{\rm bas}",r"{\mathrm{bas}}")
body=body.replace("the actual\n","the\n").replace("actual\n","")
body=body.replace("retains the actual","uses the").replace("retain the actual","use the")
body=body.replace("Every other boundary is disjoint from these normal discs, and\nits degree-two map lands in the first summand. This is the\nspecific reason that the genuine boundary \\(\\mathbb Z/d\\)\ndoes not create an extra global torsion term.",
                  "Every other boundary has zero relative component-disc coordinate,\n"
                  "so its degree-two map lands in the first summand. The displayed\n"
                  "relative maps account for the boundary \\(\\mathbb Z/d\\).")
body=body.replace("The theorem's formula in terms of powers of the recorded\npermutation is valid without replacing that permutation\nby a numerical orbit count.",
                  "Raising the component permutation to its dth power gives these\n"
                  "orbit invariants and their inverse indexing maps.")
body=re.sub(r"\b(III|IV)\*",lambda m:r"\(\mathrm{"+m[1]+r"}^*\)",body)
body=re.sub(r"\bI([13])\*",lambda m:r"\(I_"+m[1]+r"^*\)",body)
def gcd_math(match):
    expression=match[0]
    expression=re.sub(r"\b(kappa|nu|gamma|delta)\b",lambda m:"\\"+m[1],expression)
    return r"\("+expression.replace("gcd",r"\gcd",1)+r"\)"
body=re.sub(r"(?<!\\)\bgcd\([^()\n]+\)(?:-1)?(?:=[0-9]+)?",gcd_math,body)
body=body.replace("d=0 is not used as a geometric covering.",
                  "d=0 denotes only the polynomial specialization.")
body=body.replace("this does not assume either physical direction is a fan edge.",
                  "the inverse C transports the fan thimbles to both physical directions.")
body=body.replace("this equality is also checked integrally.",
                  "the projector gives its integer image and inverse coordinates.")
body=body.replace("There is no finite core torsion,\nbecause this vector is primitive.",
                  "Primitivity of this vector makes the core homology free.")

# Replace prose identifiers outside existing mathematical delimiters.
tokens={
"omega_D":r"\omega_d","omega_d":r"\omega_d","omega_1":r"\omega_1",
"xi_1":r"\xi_1","xi_D":r"\xi_d","xi_d":r"\xi_d",
"R_pi":r"R_\pi","gamma":r"\gamma","delta":r"\delta","epsilon":r"\epsilon",
"beta":r"\beta","kappa":r"\kappa","nu":r"\nu","chi":r"\chi",
"g_0":r"g_0","ell_D":r"\ell_d","ell_d":r"\ell_d",
"s_0":r"s_0","A-I":r"A-I","H1":r"H_1","H2":r"H_2","H3":r"H_3",
"H4":r"H_4","H0":r"H_0","Lambda":r"\Lambda","ker P":r"\ker P",
"A_i(d)":r"A_i(d)","I_n*":r"I_n^*","e12":r"e_{12}","C0":r"C_0",
"A2":r"A_2","L>0":r"L>0","L=0":r"L=0",
"A=I":r"A=I","A=A_i(d)":r"A=A_i(d)",
"lambda":r"\lambda","tau":r"\tau","theta":r"\theta","rho":r"\rho",
"pi":r"\pi","e1":r"e_1","e2":r"e_2","u>1":r"u>1",
"u=1":r"u=1","a=1":r"a=1","a=4":r"a=4","d=0":r"d=0",
"d=1":r"d=1","t=1":r"t=1","x=0":r"x=0",
"sigma^d":r"\sigma^d","sigma":r"\sigma",
}
parts=re.split(r"(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))",body)
plain_pattern=re.compile(
    r"(?<![A-Za-z_\\])(?:H[0-6]\([^()\n]+\)|"+
    "|".join(re.escape(word) for word in sorted(tokens,key=len,reverse=True))+
    r"|[A-Za-z]+_[A-Za-z0-9*]+)(?![A-Za-z_])")
greek={"lambda":r"\lambda","omega":r"\omega","xi":r"\xi","ell":r"\ell"}
def plain_math(match):
    value=match[0]
    if value in tokens:
        math=tokens[value]
    elif re.fullmatch(r"H[0-6]\([^()\n]+\)",value):
        math="H_"+value[1]+value[2:]
    else:
        name,sub=value.split("_",1)
        sub=greek.get(sub,sub)
        math=greek.get(name,name)+"_"+("{"+sub+"}" if len(sub)>1 else sub)
    return r"\("+math+r"\)"
for i in range(0,len(parts),2):
    parts[i]=plain_pattern.sub(plain_math,parts[i])
body="".join(parts)

# Paragraph headings and compact TeX tables, with no new permanent labels.
body=re.sub(r"(?m)^#{2,3} [0-9]+(?:\.[0-9]+)?\.? (.+)$",
            lambda m:r"\emph{"+m[1]+".}",body)
def table(match):
    lines=match[0].strip().splitlines()
    rows=[[x.strip() for x in line.strip().strip("|").split("|")] for line in lines]
    assert len(rows)>2
    n=len(rows[0])
    rendered=[]
    for index,row in enumerate(rows):
        if index==1:continue
        cells=[]
        for c in row:
            c=re.sub(r"\*\*([^*]+)\*\*",r"\\textbf{\1}",c)
            cells.append(c)
        rendered.append(" & ".join(cells)+r" \\")
        if index==0:rendered.append(r"\hline")
    return "\n\\begin{center}\n\\small\n\\begin{tabular}{"+("l"*n)+"}\n"+"\n".join(rendered)+"\n\\end{tabular}\n\\end{center}\n"
body=re.sub(r"(?m)(?:^\|[^\n]+\|\n)+",table,body)
assert not re.search(r"\([1-9]\.[0-9]+\)",body),re.findall(r"\([1-9]\.[0-9]+\)",body)
work=LANE/(BASE+"receiving_proof_work.md")
work.write_text(body,newline="\n")
p=subprocess.run(["pandoc","--from=markdown+tex_math_single_backslash+raw_tex","--to=latex","--wrap=preserve"],
                 input=body,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
assert not p.stderr,p.stderr
proof="\\begin{proof}\n"+p.stdout.rstrip()+"\n\\end{proof}\n"
proof=proof.replace("\\tightlist\n","").replace("\\def\\labelenumi{\\arabic{enumi}.}\n","")
statement=(LANE/(BASE+"receiving_statement_part.tex")).read_text().rstrip()
receiver=statement+"\n\n"+proof
assert not any(ord(c)<32 and c not in "\n\t" for c in receiver)
(LANE/(BASE+"receiving.tex")).write_text(receiver,newline="\n")
print("PASS frozen main derivation unchanged; receiver written from owned mathematical sources.")
print("RECEIVER_LINES",len(receiver.splitlines()))
print("RECEIVER_SHA256",sha256(receiver.encode()).hexdigest())

