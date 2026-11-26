"""Assemble one LT statement and proof from the frozen derivation and repairs."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
FRESH = ROOT / "agents/continuation7_iii_invariant_chern_fresh"
P = "S6_SERIES_PUBLISH_III_02LT_"
print("START", datetime.now(timezone.utc).isoformat())
fresh_raw = (FRESH / (P + "fresh_derivation.md")).read_bytes()
assert sha256(fresh_raw).hexdigest() == "53b54211c8562b23795caf8e434dee89d6f8553bd31a2f7f200e9d1f5b303068"
fresh = fresh_raw.decode()
released = (LANE / (P + "released_statement.tex")).read_text()
statement = released[released.index(r"\begin{theorem}"):]
statement = re.sub(r"\\StatementRecord[^\n]*", r"\\textnormal{\\small tag 02LT.}", statement)
statement = statement.replace("invariant-Chern original additive caps and their integral extension",
                              "invariant-Chern additive caps")
statement = statement.replace("the canonical new corrected star degrees",
                              "the star degrees of the line bundles in Theorem~\\ref{maps:src:D.2.50}")
statement = statement.replace("There is no omitted finite normal index.", "")
statement = statement.replace("there is no omitted finite normal index.", "")
scope_start = statement.index("For $h>1$,")
scope_end = statement.index(r"\end{theorem}", scope_start)
statement = statement[:scope_start] + r"""For $h>1$, the cone determines a torsion coordinate from the
cellular representative of a marked torus. The individual torsion
coordinates of the two mixed elliptic--long tori and the second
fixed-normal torus require those representatives. The image and
cokernel assertions above hold for every invariant degree vector;
the complete marked-kernel assertion is in the sector $h=1$.

""" + statement[scope_end:]
statement = re.sub(r"\\tag\{D\.IC[1-8]\}", "", statement)
statement = statement.replace(r"\[", r"\begin{equation}").replace(r"\]", r"\end{equation}")

proof = fresh[fresh.index("## 1."):fresh.index("## 12.")]
changes = [
("We use the actual positive roof and neighbourhood retraction from the\npermitted LU construction, sections 2--3, with the following maps made\nexplicit.",
 "Take the neighbourhood retraction for the original filling in\nTheorem~\\ref{maps:src:D.2.31}. We describe its lift and the return maps."),
("The actual component-group marking supplied by the permitted LU\ninput, section 1, is",
 "The marked section cocycle reads the component class by"),
("We use the actual section logarithm and the unit-preserving line\nmaps of the permitted LU construction, sections 2 and 5.\nMore explicitly,",
 "Use the section logarithm and lift its translation to the line bundle.\nExplicitly,"),
("The canonical correction in the permitted LU divisor construction\nis",
 "The component divisor of Theorem~\\ref{maps:src:D.2.50} is"),
("This proves both group lists in the clean statement.",
 "This gives \\eqref{maps:eq:D.IC4} and \\eqref{maps:eq:D.IC5}."),
("without an equivariant retraction assumption", "with the displayed homotopies"),
("no equality of monodromy\nmatrices is used to identify two analytic germs",
 "the maps are defined on the given analytic germ"),
("They have not been\nreplaced by a primitive vector or divided by an orbit length.",
 "The component clutch degree is $c_i$ at each component."),
("integrally, with the\ndisplayed right inverse; no saturation has been inserted.",
 "integrally, with the displayed right inverse."),
("not an inference from a determinant or from equal group orders",
 "with inverse given by an integral change of logarithm"),
("not a substitute identification by\nmonodromy", "with the displayed inverse"),
("without a\nprimitive-rank assertion standing in place of an inverse",
 "with the displayed inverse"),
("The literal area (9) need not be confused with a chosen split\nrepresentative. Under (15), its coordinates are precisely",
 "Under the splitting (15), the area (9) has coordinates"),
("This explicitly resolves the possible extension between the\norbit part and the scalar-long part.",
 "The maps identify the orbit part and the scalar-long subgroup."),
("at the level of its image, by the boundary (14).\nThis gives a section onto the free direction as well as onto the\ntorsion direction. It specifies the inverse by actual cell\ncoordinates; it does not assert a closed formula for the two\nindividual mixed torsion columns.",
 "at the level of its image, by the boundary (14).\nThis gives a section onto both the free and the torsion directions,\nread in the cellular coordinates of the specified torus."),
("This is an integral lift of every element of \\(\\operatorname{Fix}(A)\\)\nto the boundary kernel. No finite normal index remains.",
 "This is an integral lift of every element of \\(\\operatorname{Fix}(A)\\)\nto the boundary kernel."),
("The construction leaves the actual scalar correction \\(b\\) in\nplace. It proves the complete image and cokernel without asserting\ngeneric marked values for the second normal or the mixed fibre\ntorsion columns.",
 "The integer or residue \\(b\\) is read from the specified cellular\nrepresentative; these choices retain all line-frame contributions."),
("the maps of sections 1--2", "the component and roof maps above"),
("Section 9 proves", "The preceding projection calculation proves"),
("All the marked maps of section 10 apply", "All the marked maps for $h=1$ apply"),
("The two corrected star vectors with their inverse relabellings",
 "The two star degree vectors and their component markings"),
("The literal area", "The area"),
]
for old, new in changes:
    assert old in proof, old
    proof = proof.replace(old, new)
proof = re.sub(r"^## \d+\. (.*)$", r"\\paragraph{\1.}", proof, flags=re.M)
proof = proof.replace(r"\(", "$").replace(r"\)", "$")
table_start = proof.index("| Type | Multiplicities and action |")
table_end = proof.index("\n\nThe multiplicity-one", table_start)
proof = proof[:table_start] + r"""\begin{itemize}
\item Type $II$ has one component of multiplicity one and the identity action.
\item Type $III$ has two multiplicity-one components; the nontrivial
component class interchanges them.
\item Type $IV$ has three multiplicity-one components; a generator cycles them.
\item Type $IV^*$ has a central multiplicity-three vertex and three
arms with multiplicities two and one. A generator cycles the three arms.
\item Type $III^*$ has chain multiplicities $(1,2,3,4,3,2,1)$ and
one extra multiplicity-two vertex at the centre. The nontrivial
component class reflects the chain and fixes the extra vertex.
\item For $I_n^*$, $n=1,3$, the four outer multiplicities are one and
the $n+1$ inner multiplicities are two. A component generator cycles
the four outer vertices and reflects the inner chain; its square
pairs the outer vertices and fixes the inner chain.
\end{itemize}""" + proof[table_end:]
bullet_start = proof.index("* $R:")
bullet_end = proof.index("\n\nThen ", bullet_start)
bullets = proof[bullet_start:bullet_end]
bullets = re.sub(r"^\* ", r"\\item ", bullets, flags=re.M)
proof = proof[:bullet_start] + "\\begin{itemize}\n" + bullets + "\n\\end{itemize}" + proof[bullet_end:]

extension = r"""
\paragraph{The two extension maps.}
The orbit relations themselves are
\begin{equation}\hypertarget{tag-0206}{}\label{maps:eq:D.IC9}
 e_{i+1}-e_i+c_jt=0 .
\end{equation}
Elimination gives $e_i=e_0-i c_jt$ and $l_jc_jt=0$ on each orbit.
The partial-sum formula gives exactly the same scalar coordinate,
since
\[
 c^tK(x-sRx)=\sum_jc_j\sum_{i=0}^{l_j-1}i x_{j,i}.
\]
The projection onto component orbits has exact sequence
\[
0\longrightarrow\mathbb Z/h
\xrightarrow{[a]\mapsto[(0,a)]}H_2(U)
\xrightarrow{[(x,t)]\mapsto Rx}\ker d^t
\longrightarrow0 ,
\]
with section $u\mapsto[(su,0)]$.

For the mapping torus of the circle bundle $E$, put
$D=h/g$ and choose $\beta$ with $c^t\beta=g$.
Its Wang sequence has left term
$C=\ker c^t/A_0(\ker c^t)$.
The following maps are inverse:
\[
 [x]\longmapsto
 \left(Rx,\left[-c^tK(x-sRx)/g\right]_D\right),\qquad
 (u,[a]_D)\longmapsto[su-aA_0\beta].
\]
The division is integral. Replacing $x$ by $x+A_0y$ with $c^ty=0$
changes the residue by a multiple of $D$, since $y-KA_0y$ is
orbit-constant. Replacing $a$ by $a+D$ changes its image by
$A_0(\eta-D\beta)$, whose preimage has zero Chern evaluation.
For $z=x-sRx$ and a representative $a$ of the displayed residue,
$k=(c^tKz+ag)/h$ is integral and
\[
 x-(sRx-aA_0\beta)=A_0(Kz+a\beta-k\eta),\qquad
 c^t(Kz+a\beta-k\eta)=0 .
\]
These are the two inverse identities.
In these coordinates the whole sequence is
\[
0\longrightarrow\ker d^t\oplus\mathbb Z/D
\xrightarrow{(u,[a])\mapsto(u,[ga]_h)}
\ker d^t\oplus\mathbb Z/h
\xrightarrow{(u,[b])\mapsto[b]_g}\mathbb Z/g
\longrightarrow0 .
\]
Its torsion generator has the sign
$[(-A_0\beta,0)]=[(0,g)]$, by $d_3(0,\beta)=(A_0\beta,g)$.
A section exists exactly when $\gcd(g,D)=1$:
the scalar image of $1$ must satisfy $b\equiv1\pmod g$ and
$D\mid b$. Choose $aD+bg=1$. The section is
$[n]_g\mapsto(0,[aDn]_h)$; the full splitting and inverse are
\[
\begin{aligned}
 ((u,[v]_D),[n]_g)&\longmapsto(u,[gv+aDn]_h),\\
 (u,[t]_h)&\longmapsto
 \left((u,[(t-aDn)/g]_D),[n]_g\right),\quad n\equiv t\pmod g .
\end{aligned}
\]
All changes of representatives give the indicated moduli.
For $c=0$, this sequence is split by the infinite class $t$.
For example, at type $III$ with $Q=0$ and $M=\mathcal O(C_1)$,
$c=(2,-2)$ and $g=h=2$, so the Wang sequence splits.
For $I_1^*$ in the affine $D_5$ order with near leaves $0,1$
and far leaves $4,5$, the invariant divisor $(0,0,2,4,3,3)$
under $(0\,1)(4\,5)$ has degrees $(2,2,0,0,-2,-2)$.
Its canonical line arrow, multiplied by a constant contraction,
has $g=2,h=4$ and gives a nonsplit Wang sequence.
Thus the splitting behaviour is determined by the stated
integer criterion, while the homology groups are always as displayed.

"""
marker = r"\paragraph{The other groups and the fundamental group.}"
assert marker in proof
proof = proof.replace(marker, extension + marker)

zero_normal = r"""
\paragraph{The zero-degree scalar-long coordinate.}
The scalar-long subgroup for $c=0$ can contain a nonzero normal image.
Take a type $II$ neighbourhood $N$ with section and base coordinate $u$,
put $F=\operatorname{div}(u)$, $Q=0$, and $M=\mathcal O(F)$.
The global nonvanishing frame is $\tau=1/u$, and its canonical section
is $1=u\tau$. A constant contraction $\lambda$, $0<|\lambda|<1$,
gives
\[
 U=N\times(\mathbb C^*/\lambda^{\mathbb Z})
   \simeq N\times S^1_\delta\times S^1_\gamma .
\]
The inverse of the frame coordinate sends $W$ to $W\tau$.
On the punctured neighbourhood the canonical tensor map and its inverse are
\[
 I(p,w)=(p,u(p)w),\qquad I^{-1}(p,W)=(p,W/u(p)).
\]
Writing $\mu_0$ for the meridian in the extending frame, these maps give
\[
 I_*\mu=\mu_0+\delta,\quad I_*\delta=\delta,\quad I_*\gamma=\gamma,
 \qquad I_*^{-1}\mu_0=\mu-\delta .
\]
Here $q_Q=1,z=0,\ell=\gamma$. The torus
$\gamma\wedge\mu_0$ bounds the section disc times the long circle, so
the marked second normal has image
\[
 [\gamma\wedge\mu]=[\gamma\wedge(\mu_0+\delta)]=-t .
\]
The inverse meridian change contributes $+t$.
Projection to the two circle factors and inclusion at a fixed point
of $N$ are inverse on this subgroup, proving that $t$ is primitive
and has infinite order. This class is already in the fibre image.

"""
marker = r"\paragraph{Complete marked maps when $h=1$.}"
assert marker in proof
proof = proof.replace(marker, zero_normal + marker)

# Convert each original fresh equation tag to a permanent receiving label.
proof = re.sub(r"\\tag\{(\d+[a-z]?)\}",
               lambda m: r"\label{maps:eq:IC_local_" + m.group(1) + "}", proof)
# Only solitary numbers/letters in parentheses denote these equation references.
proof = re.sub(r"\((\d+[a-z]?)\)",
               lambda m: r"\eqref{maps:eq:IC_local_" + m.group(1) + "}", proof)
proof = proof.replace(r"\[", r"\begin{equation}").replace(r"\]", r"\end{equation}")
proof = "\\begin{proof}\n" + proof.strip() + "\n\\end{proof}\n"
receiver = statement.strip() + "\n\n" + proof
for forbidden in ("permitted LU", "clean statement", "fresh proof", "## ",
                  "No finite normal", r"\tag{", "sections 1--2", "Section 9"):
    assert forbidden not in receiver, forbidden
assert receiver.count(r"\begin{theorem}") == receiver.count(r"\end{theorem}") == 1
assert receiver.count(r"\begin{proof}") == receiver.count(r"\end{proof}") == 1
assert receiver.count(r"\begin{equation}") == receiver.count(r"\end{equation}")
assert not any(ord(ch) < 32 and ch not in "\n\t" for ch in receiver)
old_ids = re.findall(r"\\(?:hypertarget|label)\{([^}]+)\}", statement)
assert len(old_ids) == len(set(old_ids))
for kind, key in (("hypertarget", "tag-0206"), ("label", "maps:eq:D.IC9")):
    assert receiver.count("\\" + kind + "{" + key + "}") == 1
for name, text in (("receiving_statement.tex", statement.strip() + "\n"),
                   ("receiving_proof.tex", proof),
                   ("receiving.tex", receiver)):
    path = LANE / (P + name)
    assert not path.exists(), path
    path.write_text(text, encoding="utf-8", newline="\n")
    raw = path.read_bytes()
    print("FILE", path.relative_to(ROOT), len(raw), len(raw.splitlines()), sha256(raw).hexdigest())
print("FRESH_UNCHANGED", sha256((FRESH / (P + "fresh_derivation.md")).read_bytes()).hexdigest())
print("ONE_THEOREM_ONE_PROOF", True)
print("END", datetime.now(timezone.utc).isoformat())
