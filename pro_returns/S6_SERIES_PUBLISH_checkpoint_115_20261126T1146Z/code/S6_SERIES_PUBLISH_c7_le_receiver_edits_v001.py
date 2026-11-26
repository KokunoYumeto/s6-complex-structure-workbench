#!/usr/bin/env python3
"""Final local LE receiver edits after a complete mathematical reread."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from collections import Counter
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_mixed_torsion"
P=LANE/"S6_SERIES_PUBLISH_III_02LE_receiving.tex"
old=P.read_text()
assert sha256(P.read_bytes()).hexdigest()=="32e267fd918080601867cd1c20196d6e9ee2c2b8273dc1ae359d5bd897366cdf"
s=old
print("Start UTC",datetime.now(timezone.utc).isoformat(),flush=True)
print("Input SHA256",sha256(P.read_bytes()).hexdigest(),flush=True)

def replace(a,b,count=1):
    global s
    assert s.count(a)==count,(a,s.count(a),count)
    s=s.replace(a,b)
    print("OLD:",a,"\nNEW:",b,flush=True)

replace(r"H_2(X)=H_3(X)=\mathbb Z/(2p)\langle s\rangle,\qquad b_3(X)=0,",
        r"H_2(X)=\mathbb Z/(2p)\langle s\rangle,\quad H_3(X)=\mathbb Z/(2p),\quad b_3(X)=0,")
replace("complete table, with actual marked coefficients, is",
        r"complete table, where $\mu_{2p}$ is the coefficient of $\gamma_3(s)$, is")
replace("Their only data source is the disclosed raw fixture, with SHA256\n"
        r"\texttt{\detokenize{6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522}}."
        "\nNo target-derived list is an input to the new program.",
        r"These are the defining ordered data of \ref{maps:src:D.2.22}.")
replace("Enumerate every positive divisor $a$ of $d/\\nu$, sets\n"
        "$b=d/(a\\nu)$, and tests (6)--(7) and the raw component congruences.",
        "For every positive divisor $a$ of $d/\\nu$, set\n"
        "$b=d/(a\\nu)$ and test (6)--(7) and the component congruences.")
replace("The only finite orders are six at $II$, and three at\n"
        "the finite $IV$.",
        "The finite local monodromy orders $d_i$ are six at $II$ and three at\n"
        "the finite $IV$; the multiplicity $m=d_i k$ remains arbitrary.")
replace("Every entry is integral; the ordered product is identity,",
        r"""Put $c=\beta(bz)+w$. The inverse on the same marked lattice is
\[
 T^{-1}=
 \begin{pmatrix}
 A^{-1}&0&-bA^{-1}g\\
 -\beta A^{-1}&1&b\beta A^{-1}g-c\\
 0&0&1
 \end{pmatrix}.
\]
Multiplication on either side gives the identity.
Every entry is integral; the ordered product is identity,""")
replace("free and restriction in degree-two cohomology from $W$ to $V$\n"
        "is injective over the integers and over each finite field used below.",
        r"""free and restriction in degree-two cohomology from $W$ to $V$
is injective over the integers and over each finite field used below.
The exterior retracts over a graph. Its homology sequence has the
free fibre coinvariant group (16) and a subgroup of the free
degree-one cylinder group, so $H_2(V)$ is free as well.
The same graph presentation gives free $H_1(V)$; consequently
$H^2(V;\mathbb Z)$ is free.""")
replace(r"By Section 3 and the sweep values",r"By item~3 and the sweep values")
replace(r"The exact tensor comparison of Section 7",r"The exact tensor comparison of item~7")
replace(r"\pi_2(SO\eqref{maps:eq:D.MP2})",r"\pi_2(SO(4))")
replace("To recover the complete integral class, use the integral divided-power calculation, with the marked generator $s=1\\in\\mathbb Z/(2p)$:",
        r"""For the complete integral class, the order-two calculation in
\ref{maps:src:D.2.35} gives $H_6(K(\mathbb Z/2,2);\mathbb Z)=\mathbb Z/2$
with generator the reduced positive complex $\mathbb{CP}^3$ and
detector its mod-two cube. For $p=5,7$, \ref{maps:src:D.1.10}
gives the corresponding cyclic group and cube detector.
The full coprime homotopy maps of item~13 then give, with
$s=1\in\mathbb Z/(2p)$,""")
replace("The positive generator is the image of the complex-oriented CP3 under\n"
        "integer reduction. Here $3\\nmid2p$, so the ordinary cyclic cube is\n"
        "its full detector; the even-degree-six Ext ambiguity evaluates to zero\n"
        "on integral cycles.",
        r"""The positive generator is the image of the complex-oriented
$\mathbb{CP}^3$ under integer reduction. Its two primary projections
are the generators just specified. Thus the pair of ordinary cube
evaluations detects the complete integral group; the inverse maps
are explicit below.""")
replace("Zhubr's printed pp.803 and807:",
        r"\cite[Sections~3.7 and~3.12, pp.~803, 807]{manZhubr75}:")
replace("full marked data printed in the theorem:", "full marked data in the theorem:")
replace("Every type listed in \\eqref{maps:eq:D.MP2} and its order-fourteen counterpart is realized.",
        "Every type listed in \\eqref{maps:eq:D.MP2} is realized.")
replace("Equation (67) then gives", "The quotient (67) then gives")
replace("with the stated inverse at that homotopy scope.",
        "with the stated inverse at that homotopy scope. The coefficient maps\n"
        "below may be implemented by the Eilenberg--Mac Lane functor on\n"
        "degree-two chain complexes in simplicial abelian groups; in that\n"
        "model their two composites are literally the identity.")
for n,label in ((12,"D.MP3"),(40,"D.MP4"),(58,"D.MP7")):
    target="("+str(n)+")"
    if target in s:
        print("LOCAL_REFERENCE",target,"->",label,"count",s.count(target),flush=True)
        s=s.replace(target,r"\eqref{maps:eq:"+label+"}")
for kind in ("label","hypertarget","tag"):
    pat=r"\\"+kind+r"\{([^{}]+)\}"
    assert Counter(re.findall(pat,old))==Counter(re.findall(pat,s)),kind
for token in ("StatementRecord","SeriesRef","SHA256","raw fixture","the program",
              "new program","admitted","fresh","SO\\eqref"):
    assert token not in s,token
assert "\r" not in s
P.write_text(s)
print("Output lines",len(s.splitlines()),flush=True)
print("Output SHA256",sha256(P.read_bytes()).hexdigest(),flush=True)
print("Completed UTC",datetime.now(timezone.utc).isoformat(),flush=True)
print("PASS: exact local edits; permanent identities and frozen inputs unchanged.",flush=True)
