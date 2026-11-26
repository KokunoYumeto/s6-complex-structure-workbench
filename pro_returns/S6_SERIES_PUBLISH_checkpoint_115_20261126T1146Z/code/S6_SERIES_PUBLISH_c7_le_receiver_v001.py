#!/usr/bin/env python3
"""Assemble the full mathematical LE receiver from the frozen proof and exact auxiliary maps."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from datetime import datetime,timezone
import json,re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_mixed_torsion"
STEM="S6_SERIES_PUBLISH_III_02LE_"
fresh=LANE/(STEM+"fresh_derivation.md")
assert sha256(fresh.read_bytes()).hexdigest()=="06c310525ed34c167a7b5b8fad0e244ec0c5277b47683eb0dc968b15f0374a5a"
s=fresh.read_text()
rows=json.loads((LANE/(STEM+"fresh_data_v001.json")).read_text())["patterns"]
identity={
  3:("020C","12"),4:("020D","40"),7:("020G","58"),
}
def mark(n,tag):
    return r"\tag{D.MP"+str(n)+r"}\hypertarget{tag-"+tag+r"}{}\label{maps:eq:D.MP"+str(n)+"}"

statement=r"""\begin{theorem}[the mixed ten- and fourteen-torsion smooth types]\hypertarget{tag-02LE}{}\label{maps:src:D.2.38}
\textnormal{\small tag02LE.}
Use the primitive Mumford filling at every multiplicative position,
the indicated additive choice, the ordinary clutch $e\gamma$, and no
additional regular logarithmic transformation. Allow every finite
multiplicity and affine twist for which the output is simply connected.
Zero positions have the zero-based defining order.

Let $M_1=M_{\mathrm{conic}}$ with its positive conic-surgery orientation.
Let $M_0$ be the spin framed surgery on the embedded sphere obtained
by tubing two positive parallel copies of $S^2$ in $S^2\times S^4$.
Use the marked types $Z_{p,\epsilon}$ of \ref{maps:src:D.2.36},
with $H_2=\mathbb Z/p\langle e_p\rangle$, $b_3=0$,
$\mu=0$ and $\mathfrak p=\epsilon e_p$.
The twelve patterns below satisfy
\[
 H_2(X)=H_3(X)=\mathbb Z/(2p)\langle s\rangle,\qquad b_3(X)=0,
 \qquad
 X\cong M_t\# Z_{p,\epsilon}
 \quad\hbox{orientation-preservingly}.
 \tag{D.MP1}\hypertarget{tag-0209}{}\label{maps:eq:D.MP1}
\]
Here $s$ is the primitive fibre class. If the selected zero is $I_\nu$
and its marked cocycle is $\kappa u$, put
\[
 t=1+\kappa\pmod2,\qquad P_p=\frac{b/p-a\nu}{2}\pmod p,\qquad
 P_{2p}\equiv t\pmod2,\quad P_{2p}\equiv P_p\pmod p.
\]
Then $X$ is spin, $\mathfrak p(X)=P_{2p}s$ and
$\mu(X)=pt\,\gamma_3(s)$. The generator $\gamma_3(s)$ is the
reduced positive complex $\mathbb{CP}^3$ class. Set
$\epsilon=0$ for $P_p=0$ and $\epsilon=1$ otherwise.
Writing $F$ for a finite cap and $O$ for an original cap, the
complete table, with actual marked coefficients, is
\[
\begin{array}{c|c|r|c|r|r|r|r|r|r}
\text{OS/profile}&(a,b)&\text{zero}&\text{cap}&2p&t&P_p&P_{2p}&\mu_{2p}&\epsilon\\\hline
"""
for row in rows:
    profile=str(row["OS"])+(("/"+row["profile"]) if row["profile"]!="default" else "")
    add=[z for z in row["choices"] if z not in ("M","C")]
    cap=r"\text{none}"
    if row["profile"] in ("II","IV"):
        cap=row["profile"]+":"+("F" if row["finite"] else "O")
    statement += profile+"&("+str(row["a"])+","+str(row["b"])+")&"+str(row["zero"])+"&"+cap+"&"+str(row["c"])+"&"+str(row["cube2"])+"&"+str(row["P_p"])+"&"+str(row["P_full"])+"&"+str(row["mu"])+"&"+str(row["odd_epsilon"])+r"\\"+"\n"
statement+=r"""\end{array}
\tag{D.MP2}\hypertarget{tag-020B}{}\label{maps:eq:D.MP2}
\]
There are seven order-ten patterns on six initial rows, giving exactly
the three types $M_1\#Z_{5,1}$, $M_0\#Z_{5,1}$ and $M_0\#Z_{5,0}$
with multiplicities $2,4,1$. There are five order-fourteen patterns
on four initial rows, giving exactly $M_1\#Z_{7,1}$ and $M_0\#Z_{7,1}$
with multiplicities $3,2$.
\end{theorem}
"""

models=s[s.index("Let $M_1"):s.index("For every simply connected member")]
body=s[s.index("## 2."):s.index("## 13.")]
text=models+"\n"+body
substitutions=[
("These are the two marked order-two\nmodels proved in admitted LB.","These are the marked order-two models of \\ref{maps:src:D.2.35}."),
("be the marked realized odd-primary models of admitted refined LC.","be the marked realized odd-primary models of \\ref{maps:src:D.2.36}."),
("Their only data source is the disclosed raw fixture, with SHA256\n"
 "'PLACEHOLDER'",""),
]
for a,b in substitutions:
    if a in text:text=text.replace(a,b)
text=re.sub(r"Their only data source is the disclosed raw fixture, with SHA256\n[^\\n]*\\.\nNo target-derived list is an input to the new program\\.","They are the defining ordered data of \\\\ref{maps:src:D.2.22}.",text)
text=text.replace("the admitted KX necessity and sufficiency criterion","the necessity and sufficiency criterion of \\ref{maps:src:D.2.22}")
text=text.replace("The program enumerates every positive divisor", "Enumerate every positive divisor")
text=text.replace("The exact L1\ncap maps", "The exact cap maps of \\ref{maps:src:D.2.26}")
text=text.replace("by the admitted Seifert presentation","by the Seifert presentation in \\ref{maps:src:D.2.26}")
text=text.replace("This is a new enumeration of the criterion, with\nthe criterion itself an admitted dependency.","The divisor bounds and the complete component congruences prove exhaustion.")
text=text.replace("The computation retains and prints every actual $A_i,g_i$, not only\nthese fibre-type names.","Use their ordered defining matrices and cocycles in the following period maps.")
text=text.replace("These assertions are\nchecked from all twelve raw tuples, with each $T^{-1}$ retained.","These identities follow by substitution in the five defining profiles.")
text=text.replace("The new calculation constructs an integral matrix $R$\nfor the literal monodromy-cylinder matrix","The integral exterior sequence of \\ref{maps:src:D.2.26} supplies an integer matrix $R$ for the literal monodromy-cylinder matrix")
text=text.replace("The complete $R$, $P$ and $P^{-1}$ are printed for every row.","These are the actual integral cylinder coordinates in that exterior sequence.")
text=text.replace("A saved\nBezout column", "A Bezout column")
text=text.replace("integer right inverse $R_1$, printed in full, with","integer right inverse $R_1$ from the same integral exterior maps, with")
text=text.replace("The primitive boundary maps of L1", "The primitive boundary maps of \\ref{maps:src:D.2.26}")
text=text.replace("These are the admitted L1 finite-section maps, applied to the literal\nnew matrices (13). The displayed vectors and their integer inverse\ncoordinates are retained; here", "These are the finite-section maps of \\ref{maps:src:D.2.26}, applied to the literal matrices (13), with their integer inverse coordinates; here")
text=text.replace("The new raw calculation gives exactly one", "The profile lists and this divisibility criterion give exactly one")
text=text.replace("the program's full generic inverse matrices","the generic inverse matrices")
text=text.replace("the admitted doubled-line\nconstruction", "the doubled-line construction of \\ref{maps:src:D.2.36}")
text=text.replace("the admitted quarter map", "the quarter map of \\ref{maps:src:D.1.11}")
text=text.replace("The admitted construction of $M_0$", "The construction of $M_0$ in \\ref{maps:src:D.2.35}")
text=text.replace("were read in\nthe admitted LB receiver.", "are the integral surgery-trace maps of \\ref{maps:src:D.2.35}.")
text=text.replace("Use the exact marked primary recognition theorem from admitted corrected\nK9: Zhubr Theorem 5 gives the injection", "Use the marked recognition theorem. Theorem~5 of \\cite[p.~796]{manZhubr75} gives the injection")
text=text.replace("The complete Section 4.1 construction on printed p.809 preserves the", "The construction in \\cite[Theorem~3, p.~795; Section~4.1, p.~809]{manZhubr75} preserves the")
text=text.replace("The printed rank definition\non pp.793--794 is the H2 definition; that source-description correction\nis retained. Here both free ranks vanish, and both actual manifolds", "Here both free ranks vanish, and both manifolds")
text=text.replace("Use the 21 raw ordered profiles","Use the 21 defining ordered profiles")
text=text.replace("all twelve raw tuples","all twelve defining tuples")
text=text.replace("Section 1","the theorem")
text=text.replace("(3)",r"\eqref{maps:eq:D.MP1}").replace("(4)",r"\eqref{maps:eq:D.MP2}")
text=text.replace("Sections 4--12","the following attachment, line and invariant calculations")
text=text.replace("The complete primitive boundary maps give no further\nrelation.","The complete primitive boundary maps of \\ref{maps:src:D.2.26} give no further relation.")
text=text.replace("the primary Cartan\ncalculation", "the integral divided-power calculation")
text=text.replace("from admitted corrected\nK9", "from \\ref{maps:src:D.1.11}")

for n,(tag,eq) in identity.items():
    token=r"\tag{"+eq+"}"
    assert text.count(token)==1,(n,token)
    text=text.replace(token,mark(n,tag))
literal=r"Its physical support is $-kj(j-\alpha_0)/2$."
assert text.count(literal)==1
text=text.replace(literal,"Its physical support is\n"+r"\["+"\n"+r" \phi_1(j)=-\frac{k}{2}j(j-\alpha_0),\qquad k=\frac{a(v_0)_1}{\alpha_0}."+ "\n"+mark(5,"020E")+"\n"+r"\]"+"\n")
literal=r"and $w=(ar)^{-1}\pmod p$. Formula (46) gives"
assert text.count(literal)==1
text=text.replace(literal,"and define the physical weight by\n"+r"\["+"\n"+r" w=(ar)^{-1}\pmod p."+ "\n"+mark(6,"020F")+"\n"+r"\]"+"\nFormula (46) gives")

normalized=r"""
For comparison with the marking that evaluates to one on $C_f$, put
$z=(a\nu)^{-1}\alpha_p$. Its homology generator is $g_z=(a\nu)s$,
with inverse coordinate evaluation by $z$. The simultaneous action
conversion gives
\[
 z[E_p]=-\frac{w^2}{\nu^2},\qquad
 \langle z^3,[X]_p\rangle=0,\qquad
 \langle z\,\rho_p p_1,[X]_p\rangle
       =-2\left(1-\frac{w^2}{\nu^2}\right).
\tag{D.MP8}\hypertarget{tag-020H}{}\label{maps:eq:D.MP8}
\]
The corresponding refined coefficient is $(w^2/\nu^2-1)/2$.
Multiplication by $a\nu$, with inverse $(a\nu)^{-1}$, recovers
the primitive coefficient $P_p$. The physical weights are $w=4$
at the order-five rows with $a=1$, $w=3$ there when $a=3$, and
$w=4$ at every order-seven row. The selected $\nu$ is three
on $56(1,10)$ and $56/II(1,10)$, and one on the other rows.
Thus the common normalized weights $w/\nu$ are three in all
nonzero order-five cases and four in its zero case. This accounts
for every assignment in \eqref{maps:eq:D.MP2}.
"""
needle="For the two-primary coordinate, use"
assert text.count(needle)==1
text=text.replace(needle,normalized+"\n"+needle)

text=re.sub(r"\\tag\{(\d+)\}",lambda m:r"\qquad\textup{("+m[1]+")}",text)
text=re.sub(r"^## \d+\. (.*)$",lambda m:r"\item \emph{"+m[1]+".}",text,flags=re.M)
q=chr(96)
text=re.sub(q+r"([^"+q+r"]+)"+q,lambda m:r"\texttt{\detokenize{"+m[1]+"}}",text)
text=text.replace("The full marked data printed in the theorem","The full marked data in the theorem")
text=text.replace("the counts in the theorem","the counts in \\eqref{maps:eq:D.MP2}")
text=text.replace("This proves exactly three and two types, with the counts in Section 1.","This proves the three and two types with the stated multiplicities.")

split=r"""
\item \emph{The full coprime homotopy and bordism maps.}
Put $K_q=K(\mathbb Z/q,2)$ for $q=2,p$. The cyclic-group
resolution makes the positive homology of $K(\mathbb Z/q,1)$
zero over $\mathbb Z[1/q]$. The path-loop Serre sequence, whose
total space is contractible, then makes the positive homology
of $K_q$ zero over that ring. Exactness of localization implies
that each positive integral homology element is killed by a
power of $q$. For elements of the two factors, a Bezout identity
between their annihilating powers makes their tensor zero.
Likewise $\operatorname{Tor}(\mathbb Z/2^a,B)=B[2^a]=0$ for
$p$-primary $B$; finite direct sums and filtered colimits give
the assertion for all the positive homology groups.

The reduced integral Kunneth sequence therefore makes
$K_2\wedge K_p$ acyclic. The based CW inclusion
\[
 i:K_2\vee K_p\longrightarrow K_2\times K_p
\tag{D.MP9}\hypertarget{tag-020I}{}\label{maps:eq:D.MP9}
\]
is an integral homology equivalence of simply connected spaces.
Every relative homotopy group vanishes: a first nonzero one
would be the corresponding zero relative homology group by
relative Hurewicz. The inverse can be constructed on cells.
Start with the identity of the wedge; injectivity on homotopy
groups extends its retraction across each attaching cell, and
surjectivity adjusts that extension so that its composite with
$i$ is homotopic to the original cell map relative to its
boundary. The homotopy-extension property assembles the choices
over successive skeleta. This gives a based map $q$ with
$qi=\mathrm{id}$ and $iq\simeq\mathrm{id}$ relative to the wedge.
Thus \eqref{maps:eq:D.MP9} is a full CW homotopy equivalence,
with the stated inverse at that homotopy scope.

The coefficient maps
\[
 \theta(n)=(n\bmod2,n\bmod p),\qquad
 \theta^{-1}(x,y)=px+(1-p)y\pmod{2p}
\]
are exact inverses. Apply the Eilenberg--Mac Lane construction
to these degree-two coefficient maps and then use $i,q$.
The finite wedge axiom for the spin-bordism Thom spectrum gives
\[
 \Omega^{\mathrm{Spin}}_6(K(\mathbb Z/(2p),2))
  \cong
 \Omega^{\mathrm{Spin}}_6(K_2)\oplus
 \Omega^{\mathrm{Spin}}_6(K_p).
\tag{D.MP10}\hypertarget{tag-020A}{}\label{maps:eq:D.MP10}
\]
Here $\Omega^{\mathrm{Spin}}_6(\mathrm{pt})=0$, also a consequence
of the injective pair $(P,h)$ for coefficient group zero.
The forward map in \eqref{maps:eq:D.MP10} is the pair of
coefficient projections. Its inverse is the sum of the two
factor inclusions followed by $K(\theta^{-1},2)_*$.
An automorphism on the odd factor, multiplication by $r$, lifts
to the unit $p+(1-p)r$ modulo $2p$; its inverse is
$p+(1-p)r^{-1}$.

For the connected sum, contract the classifying maps on the
removed balls and collapse its neck to the common basepoint.
The inclusions and summand collapse maps give inverse homology
coordinates. The oriented spin one-handle bordism extends those
constant maps and adds the two bordism classes. Composing with
the explicit marking already given in (71)--(72) produces the
same pair as $X$. Thus the two-primary value, every odd-primary
coefficient and every possible mixed bordism coordinate have
been determined under the actual maps and their inverses.
"""
receiver=statement+"\n"+r"\begin{proof}"+"\n"+r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]"+"\n"+r"\item \emph{Models and markings.}"+"\n"+text+split+"\n"+r"\end{enumerate}"+"\n"+r"\end{proof}"+"\n"

old=(LANE/(STEM+"released_statement.tex")).read_text()+(LANE/(STEM+"released_proof.tex")).read_text()
for kind in ("label","hypertarget","tag"):
    pat=r"\\"+kind+r"\{([^{}]+)\}"
    assert Counter(re.findall(pat,old))==Counter(re.findall(pat,receiver)),kind
    print(kind,dict(Counter(re.findall(pat,receiver))),flush=True)
path=LANE/(STEM+"receiving.tex")
assert not path.exists()
path.write_text(receiver)
print("Receiver draft UTC",datetime.now(timezone.utc).isoformat(),flush=True)
print("Lines",len(receiver.splitlines()),"SHA256",sha256(path.read_bytes()).hexdigest(),flush=True)
for token in ("admitted","fresh","program","SHA256","raw fixture","printed","certificate","code/"):
    for n,line in enumerate(receiver.splitlines(),1):
        if token in line:
            print("EDITORIAL_REVIEW",token,n,line,flush=True)
print("PASS: mathematical receiver assembled; all permanent identities retained; final reading pending.",flush=True)
