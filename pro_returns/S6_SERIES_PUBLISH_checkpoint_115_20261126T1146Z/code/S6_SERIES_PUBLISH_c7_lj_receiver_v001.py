#!/usr/bin/env python3
"""Assemble the complete LJ receiver from the frozen proof and explicit repairs."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import re

W=Path(__file__).resolve().parents[1]
LANE=W/"agents/continuation7_iii_mixed_three_receiving"
fresh=W/"agents/continuation7_iii_mixed_three/S6_SERIES_PUBLISH_III_02LJ_fresh_derivation.md"
blob=fresh.read_bytes()
assert sha256(blob).hexdigest()=="ae75303e6b234eb94a85e795a08c5611659bd8939e315fe4f1c413f4c865d4e4"

statement=r"""\begin{theorem}[the mixed six-, fifteen-, and thirty-torsion types]\hypertarget{tag-02LJ}{}\label{maps:src:D.2.42}
\textnormal{\small tag02LJ.}
\StatementRecord{maps:src:D.2.42}{proved}{02LJ}{\SeriesRef{maps:src:D.2.39}, \SeriesRef{maps:src:D.2.36}, \SeriesRef{maps:src:D.2.26}, \SeriesRef{maps:src:D.2.35}, \SeriesRef{maps:eq:D.OP4}, \SeriesRef{maps:eq:D.MT2}, \SeriesRef{maps:eq:D.T37}, \SeriesRef{maps:eq:D.T38}, \SeriesRef{maps:eq:D.C27}, \SeriesRef{maps:src:D.2.8}, \SeriesRef{maps:src:D.1.10}, \SeriesRef{maps:eq:D.MP9}, \SeriesRef{maps:eq:D.MP10}; \cite[(3.3)--(3.6), p.~268]{ffThomas56}; \cite[Theorem~I(ii), pp.~897--898]{ffThomas1959Suspension}; \cite[Theorems~3 and~5; \S4.1, pp.~809--810]{manZhubr75}}

Consider the fourteen minimal patterns below, with the prescribed
primitive Mumford fan at every multiplicative site, the indicated
additive choice, and no additional regular logarithmic transformation.
Allow every finite multiplicity, affine twist and ordinary clutch
\(e\gamma\) producing a simply connected output.
All orientations are the complex orientations.

Let \(M_1=M_{\mathrm{conic}}\), and let \(M_0\) be the spin framed
surgery on the sphere obtained by tubing two parallel positive
\(S^2\) factors in \(S^2\times S^4\), as in
\ref{maps:src:D.2.35}. Let \(M_{3,0}\) be the framed degree-three
surgery of \ref{maps:src:D.2.39}, and use the marked models
\(Z_{5,\epsilon}\) of \ref{maps:src:D.2.36}, with
\(P(Z_{5,\epsilon})=\epsilon e_5\) and full fundamental class zero.
Put
\[
 Y_{6,t}=M_t\#M_{3,0},\qquad
 Y_{15,\epsilon}=M_{3,0}\#Z_{5,\epsilon},\qquad
 Y_{30,t}=M_t\#M_{3,0}\#Z_{5,0}.
\]
The complete oriented table is
\[
\begin{array}{r|l|r|r|r|l|r|l}
 &\mathrm{OS/profile}&a&b&\mathrm{zero}&\mathrm{additive}&c&\mathrm{type}\\\hline
1&56/II&1&6&2&II\ \mathrm{log}&6&Y_{6,0}\\
2&56/II&1&6&2&II\ \mathrm{original}&6&Y_{6,0}\\
3&56&1&6&0&\mathrm{none}&6&Y_{6,1}\\
4&56&5&6&3&\mathrm{none}&6&Y_{6,1}\\
5&56&5&6&4&\mathrm{none}&6&Y_{6,0}\\
6&56/II&1&15&0&II\ \mathrm{log}&15&Y_{15,1}\\
7&56/II&1&15&0&II\ \mathrm{original}&15&Y_{15,1}\\
8&56/III&1&30&3&III\ \mathrm{log}&15&Y_{15,0}\\
9&56/III&2&15&3&III\ \mathrm{original}&15&Y_{15,1}\\
10&56&1&15&2&\mathrm{none}&15&Y_{15,1}\\
11&56&2&15&3&\mathrm{none}&15&Y_{15,1}\\
12&56&2&15&4&\mathrm{none}&15&Y_{15,1}\\
13&56&1&30&3&\mathrm{none}&30&Y_{30,1}\\
14&56&1&30&4&\mathrm{none}&30&Y_{30,0}
\end{array}
\tag{D.MT1}\hypertarget{tag-020J}{}\label{maps:eq:D.MT1}
\]
Zero positions use the recorded zero-based indexing.
There are two oriented types in each sector. At \(c=6\) their
multiplicities are three for \(t=0\) and two for \(t=1\);
at \(c=15\) they are one for \(\epsilon=0\) and six for
\(\epsilon=1\); at \(c=30\) each occurs once.

Every output is spin and has
\[
 H_2(X)=H_3(X)=\mathbb Z/c,\quad
 H_1(X)=H_4(X)=H_5(X)=0,\quad
 H_0(X)=H_6(X)=\mathbb Z,\quad b_3(X)=0.
\]
In the physical fibre marking \(s\) specified in the proof, let
\(\gamma_3(s)\) be the positive \(\mathbb{CP}^3\) reduction generator
of \(H_6(K(\mathbb Z/c,2);\mathbb Z)=\mathbb Z/(3c)\).
At the selected cusp write its raw data as \((\nu,\kappa)\).
The complete primary coefficients are
\[
 t=1+\kappa\pmod2\quad(2\mid c),\qquad
 P_p=\frac{b/p-a\nu}{2}\pmod p\quad(p=3,5;\ p\mid c).
\]
Here \(P_3=0\), and \(P_5\) is either \(0\) or \(3\);
write \(\epsilon=[P_5\ne0]\). The full invariants are
\[
\begin{array}{c|c|c}
c&P(X)&\mu(X)\\\hline
6&3t\,s&9t\,\gamma_3(s)\pmod{18}\\
15&3\epsilon\,s&0\pmod{45}\\
30&15t\,s&45t\,\gamma_3(s)\pmod{90}.
\end{array}
\]
In particular the full three-primary coordinate is zero in
\(\mathbb Z/9\), for every allowed finite parameter.
\end{theorem}"""

body=blob.decode().split("## 2. Exhaustion",1)[1]
body="## 2. Exhaustion"+body.split("## 14. Computation",1)[0]
body=body.split("Relative to the statement-only target table,",1)[0]
body=body.replace("Section 1","the theorem")
body=body.replace("The new program independently enumerates",
                  "An exact enumeration proceeds through")
body=body.replace("The new second computation","The physical-weight computation")
body=body.replace("in the now admitted LF receiver; its eight-row conclusion is not used",
                  r"in \ref{maps:src:D.2.39}; its eight-row conclusion is not used")
body=body.replace("This is the concrete marked model in the admitted LF receiver.",
                  r"This is the concrete marked model of \ref{maps:src:D.2.39}.")

extra=r"""
### 10a. Relative equivariant injection and the complete three-primary bordism class

The same conclusion also verifies the degree-six restriction assertion
on the whole circle Borel space. Choose disjoint invariant tubular
neighbourhoods \(N\) of \(C_f\sqcup E_3\), and put
\(Y=X\setminus\operatorname{int}N\). The established fixed-set
calculation shows that no point of \(Y\) has stabilizer divisible by
three. It has no circle-fixed point either, since such a point is
fixed by \(C_3\). The circle action on \(Y\) is locally free.
In a slice with finite stabilizer \(H\), the fibre of the map
from its Borel construction to its orbit slice is \(BH\).
The usual averaging homotopy on positive group cochains divides
by \(|H|\), which is a unit in \(\mathbb Z/9\). It contracts the
positive-degree cochains, while degree zero is the coefficient
identity. The slice maps and their restrictions to boundary collars
therefore give, by descent over a triangulation of the compact
five-dimensional orbit pair,
\[
 H^*((Y,\partial Y)_{S^1};\mathbb Z/9)
       \simeq H^*(Y/S^1,\partial Y/S^1;\mathbb Z/9).
\]
These are the pullback isomorphism and its inverse obtained by the
degree-zero augmentation and the displayed averaging contraction
on slice fibres. Excision identifies the left side with
\(H^*((X,N)_{S^1};\mathbb Z/9)\). The orbit pair has dimension five,
so its degree-six group is zero. The long exact sequence thus
makes restriction
\[
 H^6(X_{S^1};\mathbb Z/9)\longrightarrow
 H^6((C_f)_{S^1}\sqcup(E_3)_{S^1};\mathbb Z/9)
\]
injective.

Here the actual rational Borel space is the projective bundle with
relation \(z(z-kT)=0\), rather than an unspecified replacement of
its action. The integral lift \(Az\) has cube
\(A^3k^2zT^2\), which is zero modulo nine. The elliptic restriction
is the signed suspension class already computed. Their normalized
third powers are therefore both zero. This proves the whole-circle
restriction argument using the actual actions and also agrees with
the explicit \(C_9\) localization maps above.

For completeness the three-primary spin-bordism map is
\[
 \Omega_6^{\rm Spin}(K(\mathbb Z/3,2))
       =\mathbb Z/9\langle\zeta\rangle,\qquad
 h(j\zeta)=j\gamma_3(e_3),\qquad P(j\zeta)=j e_3\pmod3 .
\]
The free-lift generators have \(P(\epsilon)=6\), \(h(\epsilon)=0\),
and \(\zeta\) is positive \(\mathbb{CP}^3\) reduction.
After reduction to \(\mathbb Z/3\), injectivity of \((P,h)\)
kills \(\epsilon\). The class \(\zeta\) has order exactly nine:
its fundamental class has that order, and \(9\zeta\) has both
invariants zero. The free-lift epimorphism and this injection
give the displayed group and maps
\cite[\S\S3.11--3.14 and Theorem~5]{manZhubr75}.
The inverse of \(h\) is \(j\gamma_3(e_3)\mapsto j\zeta\).
This statement applies to the bordism class of any classifying
map \(X\to K(\mathbb Z/3,2)\); it places no requirement that the
whole \(H_2(X)\) be \(\mathbb Z/3\).
Thus the zero full coordinate above gives exactly the
three-primary class of \(M_{3,0}\).

"""
body=body.replace("## 11.",extra+"## 11.",1)
body=body.replace(
    r" \tag{56}",
    r" \qquad\textnormal{(56)}\tag{D.MT2}\hypertarget{tag-020K}{}\label{maps:eq:D.MT2}")
body=body.replace(
    r" \tag{92}",
    r" \qquad\textnormal{(92)}\tag{D.MT3}\hypertarget{tag-020L}{}\label{maps:eq:D.MT3}")
body=re.sub(r"\\tag\{([0-9]+)\}",r"\\qquad\\textnormal{(\1)}",body)
body=body.replace(
    "Cartan's",
    "Cartan's",1)
body=body.replace(
    "Theorem 3, printed p.795, with the construction",
    r"Theorem 3, printed p.795, with the construction")

def convert(lines):
    out=[];i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith("## ") or line.startswith("### "):
            title=re.sub(r"^#+ ","",line)
            out.append(r"\paragraph{"+title+r".}")
        elif line.startswith("|"):
            table=[]
            while i<len(lines) and lines[i].startswith("|"):
                row=[cell.strip() for cell in lines[i].strip("|").split("|")]
                if not all(re.fullmatch(r"[-:]+",v) for v in row):
                    table.append(row)
                i+=1
            width=len(table[0]);assert all(len(row)==width for row in table)
            out.append(r"\begin{center}\begin{tabular}{"+("|".join(["l"]*width))+r"}")
            for k,row in enumerate(table):
                out.append(" & ".join(row)+r"\\")
                if k==0:out.append(r"\hline")
            out.append(r"\end{tabular}\end{center}")
            continue
        else:
            assert chr(96) not in line
            out.append(line)
        i+=1
    return "\n".join(out)

proof=r"\begin{proof}"+"\n"+convert(body.strip().splitlines())+"\n"+r"\end{proof}"
proof=proof.replace(
    "The exact recognition scope is the primary one recorded in the\ncorrected admitted K9 receiver.",
    r"The recognition scope is that of Theorem~5 and the marked"
    "\n"+r"construction and uniqueness proof in Section~4.1"
    "\n"+r"\cite[pp.~795--796,809--810]{manZhubr75}.")
proof=proof.replace(
    "The Cartan and Browder--Thomas construction",
    "The Cartan and Browder--Thomas construction")

aux=r"""The exact calculation uses the defining raw elliptic matrices and
section cocycles. The sources
\path{code/S6_SERIES_PUBLISH_c7_lj_mixed_three_v001.py} and
\path{code/S6_SERIES_PUBLISH_c7_lj_action_coefficients_v001.py}
retain all fourteen patterns, every integral period, cap and graph
section, and the physical action and generator inverses.
Coalescing the two pairs that differ only by original versus finite
\(II\) caps gives twelve marked rows. The post-exposure validation
\path{code/S6_SERIES_PUBLISH_c7_lj_post_exposure_v001.py}
rechecks all \(464\) semicharacter substitutions on those rows,
all \(52\) adapted multiplicative matrices and the three finite
normal coefficients \(6,15,15\). The pattern-by-pattern refinement
run has \(528\) substitutions because the two \(II\) choices are
retained separately. The full order-nine operation, the all-parameter
line comparison and the marked oriented recognition are proved above;
the arithmetic checks support their stated finite lattice inputs."""

receiver=statement+"\n\n"+proof+"\n\n"+aux+"\n"
path=LANE/"S6_SERIES_PUBLISH_III_02LJ_receiving.tex"
assert receiver.count(r"\begin{proof}")==receiver.count(r"\end{proof}")==1
assert receiver.count(r"\begin{theorem}")==receiver.count(r"\end{theorem}")==1
for pat in (r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}",r"\\tag\{([^}]+)\}"):
    originals="".join((LANE/f"S6_SERIES_PUBLISH_III_02LJ_released_{part}.tex").read_text()
                      for part in ("statement","proof"))
    assert sorted(re.findall(pat,receiver))==sorted(re.findall(pat,originals))
assert fresh.read_bytes()==blob
path.write_text(receiver)
print("COMPLETE",datetime.now(timezone.utc).isoformat())
print("RECEIVER",path.relative_to(W),"LINES",len(receiver.splitlines()),
      "SHA256",sha256(path.read_bytes()).hexdigest())
print("IDENTITIES",re.findall(r"\\(?:label|hypertarget|tag)\{([^}]+)\}",receiver))
print("PASS exact permanent identity multisets; one theorem/proof; frozen fresh unchanged.")
