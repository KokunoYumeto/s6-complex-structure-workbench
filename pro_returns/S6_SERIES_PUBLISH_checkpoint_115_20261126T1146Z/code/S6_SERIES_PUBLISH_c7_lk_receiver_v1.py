#!/usr/bin/env python3
"""Assemble the one-proof LK receiver from wholly read mathematical sources."""
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT / "agents/continuation7_iii_general_cusp/S6_SERIES_PUBLISH_III_02LK_fresh_derivation.md"
POST = ROOT / "agents/continuation7_iii_general_cusp_receiving/S6_SERIES_PUBLISH_III_02LK_post_exposure_derivation.md"
OUT = POST.with_name("S6_SERIES_PUBLISH_III_02LK_receiving.tex")
fresh, post = FRESH.read_text(), POST.read_text()
assert sha256(FRESH.read_bytes()).hexdigest() == "83191425a6141af9e3e125622493df5c44dfb909ff77c65af6f1ea6d90995f90"
TAGS = {1:"01YY", 2:"01Z4", 3:"01Z5", 4:"01Z6", 5:"01Z7",
        6:"01Z8", 7:"01Z9", 8:"01ZA", 9:"01ZB", 10:"01YZ",
        11:"01Z0", 12:"01Z1", 13:"01Z2", 14:"01Z3"}


def section(text, number):
    return re.split(r"^## "+str(number)+r"\. [^\n]+\n", text, flags=re.M)[1].split("\n## ")[0].strip()


def replace(text, old, new):
    assert text.count(old) == 1, (old[:140], text.count(old))
    return text.replace(old, new)


def unnumber(text):
    return re.sub(r"\s*\\tag\{\d+\}", "", text)


def mark(text, needle, number):
    hits = [m for m in re.finditer(r"\\\[(.*?)\\\]", text, flags=re.S) if needle in m.group(1)]
    assert len(hits) == 1, (number, needle, len(hits))
    m = hits[0]
    block = (r"\begin{equation}\hypertarget{tag-"+TAGS[number]+"}{}"+
             r"\label{maps:eq:D.GC"+str(number)+"}\n"+
             m.group(1).strip()+"\n"+r"\end{equation}")
    return text[:m.start()]+block+text[m.end():]


statement = r"""\begin{theorem}[A triangular cusp and its boundary kernel]\hypertarget{tag-02LK}{}\label{maps:src:D.2.43}
Let \(N_L\) be the smooth triangular Mumford cusp for the unit-triangle
fan and a full short-period sublattice \(L\subset\mathbb Z^2\).
The two periods may have nonvanishing holomorphic unit factors.
Write \(s\mid t\) for the positive Smith factors of \(L\), and put
\(D=st\). Let \(M_L=\partial N_L\), and let \(\Lambda=\mathbb Z^4\)
be the nearby torus lattice. Its return is \(A=I+N\), where
\(N^2=0\) and the long-to-short map has Smith factors \(s,t\).
Set \(F=\ker(A-I)\), the primitive short lattice.

Then \(\pi_1(N_L)=L\), with the long loops mapped to their period
displacements. Its integral homology is
\[
 \begin{array}{c|ccccc}
 j&0&1&2&3&4\\ \hline
 H_j(N_L;\mathbb Z)&\mathbb Z&\mathbb Z^2&
 \mathbb Z^{D+3}\oplus\mathbb Z/s&\mathbb Z^2&\mathbb Z^D .
 \end{array}
\]
All higher groups vanish, and \(\chi(N_L)=2D\). The fibre kernel is
\[
 \ker\{H_2(T^4;\mathbb Z)\to H_2(N_L;\mathbb Z)\}
 =(\Lambda^2A-I)\Lambda^2\Lambda+\Lambda^2F.
\]
It is saturated exactly when \(s=1\). The fibre image is
\(\mathbb Z^4\oplus\mathbb Z/s\), and its cokernel in \(H_2(N_L)\)
is free of rank \(D-1\).

The two fixed angular normal tori bound and project to a basis of
\(F\) in the Wang sequence. Together with the fibre kernel they
give the full boundary kernel. In particular,
\[
 \begin{split}
 H_1(M_L;\mathbb Z)&=\mathbb Z^3\oplus\mathbb Z/s\oplus\mathbb Z/t,\\
 H_2(M_L;\mathbb Z)&=\mathbb Z^6\oplus(\mathbb Z/s)^2,\\
 \ker\{H_2(M_L;\mathbb Z)\to H_2(N_L;\mathbb Z)\}
                &\cong\mathbb Z^2\oplus\mathbb Z/s.
 \end{split}
\]
The killed torsion is the primitive angular area modulo the
monodromy image; the other boundary torsion coordinate maps
isomorphically to the cap torsion.

Let \(\theta\) be the positive \(q\)-meridian. Index the normalized
components by \(\bar v\in\mathbb Z^2/L\). The positive transverse
disc to that component has boundary
\[
 \theta+\bar v
 \quad\hbox{in }\mathbb Z\theta\oplus\mathbb Z^2/L
                  \subset H_1(M_L;\mathbb Z).
\]
These are all columns of
\(H_2(N_L,M_L)=H^4(N_L)=\mathbb Z^D\to H_1(M_L)\).
The component differences map to their differences in
\(\mathbb Z^2/L\).
\end{theorem}
"""
for needle, n in [(r"\begin{array}",1), (r"\ker\{H_2(T^4",2),
                  (r"\begin{split}",3), (r"\theta+\bar v",4)]:
    statement = mark(statement, needle, n)

s1 = section(fresh, 1)
s1 = re.sub(r"\bB\b", "B_0", s1)
s1 = replace(s1, "These are the toroidal maps used below.", "These character maps also fix the boundary markings.")
s1 = replace(s1, "The computations below may\ntherefore be made with unit factors one and transported by\nthis specified family map; no identification through monodromy\nalone is made.",
             "The unit-one calculations therefore transport through this\nfamily map with their lattice and boundary markings.")
s1 += r"""

These units also extend to the full short lattice. Put
\(K(q)=(b_1(q),b_2(q))\) and define, for \(v\in\mathbb Z^2\),
\[
 \Psi_v(z,q)=(q^v\exp(K(q)B_0^{-1}v)z,q).
\]
Then \(\Psi_{v+w}=\Psi_v\Psi_w\), and \(\Psi_{B_0e_j}\) is the
given period. The inverse is \(\Psi_{-v}\). The same character
charts extend this full action, whose leading logarithmic period
matrix is the identity; the preceding free-action and properness
proofs apply. The identity of covering charts induces the
degree-\(D\) map \(N_L\to N_{\mathbb Z^2}\).
Its local inverse sheets are labelled by \(\mathbb Z^2/L\) and
given by the maps \(\Psi_v\). Changing a logarithm changes this
extension by a finite unit character trivial on \(L\), and fixes
the given \(L\)-quotient and its boundary marking.
"""

s2 = section(fresh, 2)
s2 = replace(s2, "This\nis the local branch-retaining triangulation of admitted KB,\nperformed on the \\(L\\)-quotient itself.",
             r"The local branch construction in \ref{maps:src:D.1.2}"+
             "\napplies to these charts on the \\(L\\)-quotient.")
s2 = replace(s2, "The degree-two row is the map constructed\nnext, including all its integral relations.",
             "We compute the degree-two row with its integral relations below.")

s3 = section(post, 2)
s3 = replace(s3, "Write \\(a=x-1,b=y-1\\), and use the original matrices",
             r"Let \(R=\mathbb Z[x^{\pm1},y^{\pm1}]\), \(I=(x-1,y-1)\),"+
             "\nand put \\(a=x-1,b=y-1\\). In the cyclic divisor order\n"+
             r"\((E_1,H-E_1-E_2,E_2,H-E_2-E_3,E_3,H-E_1-E_3)\),"+
             "\ntake the second deck generator with reversed sign. The\n"+
             "opposite-pair weights are then \\(x^{-1},y,xy\\). The\n"+
             "coordinate map \\(E=\\operatorname{diag}(1,-1)\\) sends\n"+
             "\\(L\\) to \\(EL\\), with component map \\([v]\\mapsto[Ev]\\)\n"+
             "and inverse \\([w]\\mapsto[Ew]\\). The resulting restriction\n"+
             "and cancelled matrices are")
s3 = replace(s3, " \\end{pmatrix},\n \\qquad\n F=", " \\end{pmatrix}.\n\\]\n\\[\n F=")
s3 = replace(s3, "The\nfrozen four-boundary-curve basis converts by the integral matrix\nwhose columns are \\(E_1,H-E_1-E_2,E_2,H-E_2-E_3\\); its inverse\nis the four displayed blowup formulas in the frozen proof.",
             r"The four curves \(D_0=E_1,D_1=H-E_1-E_2,D_2=E_2,D_3=H-E_2-E_3\)"+
             "\nalso form an integral basis. Its inverse is\n"+
             r"\(E_1=D_0,\ E_2=D_2,\ H=D_0+D_1+D_2,\ E_3=D_0+D_1-D_3\).")
s3 = replace(s3, "The cancellation omitted from the original is explicitly", "The cancellation is")
s3 = replace(s3, "The original comparison matrices are", "Set")
s3 = replace(s3, "Multiplication gives \\(F=TCS\\), with\n\\(\\det T=-x^{-2}y^{-2}\\), \\(\\det S=-x^2y^2\\).\nThus the printed D.GC5--D.GC7 matrices and equality stand.",
             "Multiplication gives\n\\[\n T^{-1}F=CS.\n\\]\n"+
             "The determinants are \\(\\det T=-x^{-2}y^{-2}\\) and\n"+
             "\\(\\det S=-x^2y^2\\).")
s3 = replace(s3, "This proves D.GC8 as an \\(R\\)-module, with the displayed morphism.",
             "Thus the displayed morphism gives\n\\[\n"+
             r" H_2(\widetilde N_L;\mathbb Z)\cong I^2"+
             "\n\\]\nas an \\(R\\)-module.")
s3 = mark(s3, r"B=\begin{pmatrix}", 5)
s3 = mark(s3, r"F=\begin{pmatrix}", 6)
s3 = mark(s3, r"T^{-1}F=CS", 7)
s3 = mark(s3, r"H_2(\widetilde N_L", 8)

s4 = section(post, 4)
s4 = replace(s4, "The disc-difference basis and inverse in\nthe frozen proof give an explicit integral basis of this same\nlattice, with its full index \\(D\\) in the augmentation group.",
             "An integer Smith decomposition of this lattice constraint\n"+
             "gives its basis and inverse coordinates; its index in the\n"+
             "augmentation group is \\(D\\).")
s4 = replace(s4, "Now use both exact sequences in D.GC9. The relevant segment is",
             "Use the exact sequences\n\\[\n\\begin{gathered}\n"+
             r"0\to I\to R\to\mathbb Z\to0,"+"\n"+
             r"0\to I^2\to I\to\mathbb Z^2\to0,"+"\n"+
             "\\end{gathered}\n\\]\n"+
             "where the last action is trivial. Their relevant Tor segment is")
s4 = replace(s4, r" \longrightarrow J_L\longrightarrow0.",
             r" \longrightarrow I\otimes_R S_L"+
             "\n"+r" \longrightarrow\mathbb Z^2\longrightarrow0.")
s4 = replace(s4, "with both inverse maps. This proves D.GC12 and fixes its finite\ncoordinate as the image under beta of the primitive column\n\\(\\alpha_L/s\\). KS checked the sign and the derivative inverse\nat this bounded algebraic scope as well.",
             "with both inverse maps. Its finite coordinate is the image\n"+
             "under \\(\\beta\\) of the primitive column \\(\\alpha_L/s\\).")
s4 = replace(s4, "This agrees under the chain\nmaps of sections 2--3 with the two frozen normalization cycles.",
             "The chain maps above carry these two generators to the\n"+
             "two degree-three normalization cycles.")
s4 = s4.split("\nKS checked only")[0].strip()
s4 = mark(s4, r"0\to I\to R", 9)
s4 = mark(s4, r"\mathbb Z\xrightarrow{\alpha_L}", 10)
s4 = mark(s4, r"\alpha_L(1)=u\otimes v", 11)
s4 = mark(s4, r"I^2\otimes_R S_L"+"\n       "+r"\simeq J_L", 12)

s5 = section(fresh, 5)
s5 = s5[s5.index("The normalization spectral sequence"):]
s5 = replace(s5, "The only remaining extension is a copy of \\(\\mathbb Z\\)\nover (6), which splits integrally.",
             "The degree-zero row is the triangular torus \\(\\mathbb R^2/L\\).\n"+
             "Subdividing each Koszul square into its two triangles, with\n"+
             "inverse cellular collapse, gives its groups \\(\\mathbb Z,L,\\mathbb Z\\).\n"+
             "The only remaining extension is a copy of \\(\\mathbb Z\\) over\n"+
             r"\eqref{maps:eq:D.GC12}, which splits integrally.")
s5 = replace(s5, "then use \\(f,g\\) from Section 3 and\nthe quotient inverse of Section 4.",
             "then use the normalization chain equivalence and\n"+
             "the integral quotient inverse above.")
array_start = s5.index("It follows that\n\\[")
array_end = s5.index("\nFor the fundamental group", array_start)
s5 = s5[:array_start]+r"""Combining the normalization rows proves \eqref{maps:eq:D.GC1}.
Their total real dimension is four, so higher homology vanishes.
The displayed groups give \(\chi(N_L)=2D\).
"""+s5[array_end:]
s5 = s5.replace("columns\nof \\(B\\)", "columns\nof \\(B_0\\)")
s5 = s5.replace("displacement \\(B e_j\\)", "displacement \\(B_0 e_j\\)")
s5 = s5.replace("Equation (7)", r"\eqref{maps:eq:D.GC1}")

s6 = section(fresh, 6)
s6 = re.sub(r"\bB\b", "B_0", s6)
s6 = replace(s6, "This is a change of marked periods of the same fan, with\nthe explicit real-period map and its inverse. It does not\nchange the fan or its component incidence.",
             "This changes the marked periods through the real-period map\n"+
             "and its inverse, while retaining the same fan and component incidence.")
s6 = s6.replace("of (10)", "of this return")
s6 = s6.replace("in (16)", "in the marked boundary group")

s7 = section(fresh, 7)
start = s7.index("The short angular area")
end = s7.index("\nWe now determine", start)
angular = section(post, 5).split("\nThe two fixed-normal")[0]
angular = angular[:angular.index("\nThis proves the original")]
s7 = s7[:start]+angular+s7[end:]
s7 = replace(s7, "Integral UCT and (7) give", r"Integral UCT, \eqref{maps:eq:D.GC1} and duality give")
s7 = replace(s7, r" H_3(N_L,M_L)=H^3(N_L)=\mathbb Z^2\oplus\mathbb Z/s.",
             r"\begin{gathered}"+
             "\n"+r"H_3(N_L,M_L)=H^3(N_L)=\mathbb Z^2\oplus\mathbb Z/s,"+
             "\n"+r"H_2(N_L,M_L)=H^4(N_L)=\mathbb Z^D."+
             "\n"+r"\end{gathered}")
s7 = replace(s7, "These are explicit maps;\nthe normalization torsion generator (4) has its separate\nexplicit branch-cycle representative. The change of\ncoordinates sends that representative through \\(g\\) from\nSection 3 and the branch augmentation, and then applies\nthe boundary inverse described after (26). Its inverse\nincludes the fibre representative in the same branch\ncomplex and applies (5). The chain maps and the integral\npreimage rule there specify both composites, including\nthe unit relating any two chosen cyclic coordinates.",
             "To compare this coordinate with \\(\\beta(\\alpha_L/s)\\),\n"+
             "use the normalization chain maps and branch augmentation,\n"+
             "then the boundary preimage rule below. The inverse inserts\n"+
             "the fibre representative in that same branch complex and\n"+
             "uses the period-ideal derivative inverse. Their composites\n"+
             "fix the respective cyclic classes, so these maps determine\n"+
             "the unit relating the two chosen cyclic coordinates.")
refs = {"in (17)":"in the first relative group",
        "in (14)":"in the fibre coinvariants",
        "coordinates (13)":"six-bivector coordinates",
        "(12) and (18)":"the return image and the boundary kernel",
        "of (7)":"of the cap",
        "by (18)":"by the full boundary kernel",
        "in (19)":"in the displayed fibre kernel",
        "in (13)":"in the six-bivector basis"}
for old,new in refs.items():
    s7=s7.replace(old,new)
s7=mark(unnumber(s7),r"H_3(N_L,M_L)",14)

s8=section(fresh,8)
s8 = re.sub(r"\bB\b", "B_0", s8)
s8=s8.replace("UCT and (7)",r"UCT and \eqref{maps:eq:D.GC1}")
s8=s8.replace("in (16)","in the marked boundary coordinates")
s8=s8.replace("in (24)","in the residual-difference list")
s8=s8.replace("exactly (23)",r"exactly \(\Gamma(z)=0\)")
s8=s8.replace("For (24)","For a residual-difference vector")
s8=s8.replace("Reading (25)","Reading the displayed inverse coordinates")
s8=s8.replace("The full pair sequence, (18), and (23)","The full pair sequence and the computed boundary and disc maps")
s8=s8.replace("in Section 7","above")
s8=s8.replace("in Section 2","above")
s8=s8.replace("use (25)","use the inverse disc coordinates")
s8=s8.replace("in (13)","in the six-bivector basis")
s8=s8.replace("by precisely (18)","by precisely the full boundary kernel")
s8=replace(s8, "It also gives the exact change to the normalization\ncoordinate (4) by the composite described in Section 7.\nHence the\ncokernel is free of rank \\(D-1\\), and these maps\nprove the claimed full boundary and fibre statements\nin every marking. They also give another explicit\nbasis for the homology group already computed in (7).",
             "It also gives the inverse comparison with the normalization\n"+
             "torsion coordinate specified above. The cokernel is therefore\n"+
             "free of rank \\(D-1\\).")
for old,new in {"by (26)":"by the pair sequence",
                "(22)":"the component-meridian formula",
                "(23)":r"the map \(\Gamma\)",
                "(26)":"the displayed pair sequence"}.items():
    s8=s8.replace(old,new)

titles=["Fan charts, covers and units","The central fibre and branch resolution",
        "The normalization module","Integral finite-cover homology",
        "The cap and its fundamental group","Boundary coordinates",
        "The full boundary kernel","Component discs and quotient inverses"]
pieces=[s1,s2,s3,s4,s5,s6,s7,s8]
body=[]
for title,text in zip(titles,pieces):
    text=unnumber(text)
    text=re.sub(r"\bactual ", "", text)
    text=text.replace("For completeness ", "")
    text=text.replace("without choosing\na rational divisor basis", "in an integral divisor basis")
    body.append("\\medskip\n\\noindent\\emph{"+title+".}\n"+text.strip()+"\n")
proof="\\begin{proof}\n"+"\n".join(body)+"\\end{proof}\n"
proof=mark(proof,r"\operatorname{im}(\Lambda^2A-I)",13)
result=statement+"\n"+proof
assert result.count(r"\begin{theorem}") == result.count(r"\end{theorem}") == 1
assert result.count(r"\begin{proof}") == result.count(r"\end{proof}") == 1
for n,tag in TAGS.items():
    assert result.count(r"\label{maps:eq:D.GC"+str(n)+"}") == 1
    assert result.count(r"\hypertarget{tag-"+tag+"}") == 1
assert result.count(r"\label{maps:src:D.2.43}") == 1
for bad in ("frozen", "admitted", "original proof", "D.GC9", "KS checked", r"\tag{"):
    assert bad not in result, bad
assert not re.search(r"\((?:[0-9]|[12][0-9])\)", result), "unresolved handwritten equation reference"
assert all(ord(c)>=32 or c in "\n\t" for c in result)
OUT.write_text(result)
print("WROTE", OUT.relative_to(ROOT))
print("LINES", len(result.splitlines()))
print("SHA256", sha256(OUT.read_bytes()).hexdigest())
print("PASS one theorem, one proof, all fifteen permanent identities, LF/control check")

