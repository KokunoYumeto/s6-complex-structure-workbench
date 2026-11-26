#!/usr/bin/env python3
"""Prepare the complete tangent/normalization/resonance unit, without admission.

Use --reviewed only after the complete original and receiving proof blocks have
actually been read. The emitted events are exposed editorial comparisons.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents" / "continuation3_provenance" / "section12"
OUT.mkdir(parents=True, exist_ok=True)
source = (ROOT / "S6_SERIES_PUBLISH_II.tex").read_text()
start_marker = r"\section{Tangent cohomology, normalization restrictions and resonance}"
end_marker = r"\section{Constant-monodromy period comparison and compact examples}"
start = source.index(start_marker)
end = source.index(end_marker, start)
old_unit = source[start:end]
unit = old_unit
rows = []
proof_notes = {}

def replace(old, new, owner, typ, reason, where="complete statement/proof block"):
    global unit
    assert unit.count(old) == 1, (owner, typ, unit.count(old), old[:90])
    rows.append(dict(change_id=f"II-C3-TANGENT-{len(rows)+1:03d}", type=typ,
        statement_id=owner, old_location=where, old_page="cp35; final page concordance pending",
        new_location=where, new_page="integrated build pending", old_text=old, new_text=new,
        reason=reason, review_status="Complete old and receiving owner proof comparison required before --reviewed."))
    unit = unit.replace(old, new, 1)
    proof_notes.setdefault(owner, []).append(reason)

def block(text, label):
    point = text.index(r"\label{" + label + "}")
    start = text.rfind(r"\begin{proposition}", 0, point)
    finish = text.index(r"\end{proof}", point) + len(r"\end{proof}")
    return text[start:finish]

# Remove repeated summaries; each mathematical assertion remains at its full
# statement/proof owner. No theorem, equation label or permanent tag is deleted.
old = r"""\ref{cdp:st:C4a} is an explicit geometric instance of \ref{cdp:st:C4c}. The two vanishing groups on the support in \ref{cdp:st:B1}--\ref{cdp:st:B2} do not give its fibre test: their ambient space is one-dimensional. The compact quotient \ref{cdp:st:A.3.2} proves that the full multiple fibre cannot be replaced by one unshifted reduced-support test. \ref{cdp:st:C4c} supplies the fixed full-fibre obstruction in arbitrary torus fibrations. \ref{cdp:st:C4e} proves that its normalization target is nonzero for every twist, with arbitrary singularities and multiplicities."""
replace(old, "", "cdp:st:C4b", "D12;D13",
    "Remove the orphan recap. Its five claims are the already-stated C4a-to-C4c application, the exact B1/B2 counterexample, the A.3.2 full-fibre example, C4c's fixed fibre and C4e's normalization target. Their hypotheses and maps remain in those owners; C4b's complete proof remains.", "after C4b proof")
old = r"""The fixed fibre in \ref{cdp:st:C4d} carries an ambient section along the entire complex transgression line. For torus general fibre, \ref{cdp:st:C4c} strengthens this to all twists in the Picard group. For a general fibre with $h^1(\OO)=1$ and $h^2(\OO)=0$, \ref{cdp:st:A.5.13} identifies that line with the entire Picard group. The following proof treats both cases through their actual conductor schemes."""
replace(old, "", "cdp:st:C4d", "D12;D13",
    "The fixed-fibre and Picard-line comparisons occur explicitly in the receiving C4e proof. Remove this unnumbered preview without dropping either cohomological case or either morphism.", "after C4d proof")
old = r"""The local example \ref{cdp:st:A.2.5} has actual vertical inverse-Jacobian
poles, and \ref{cdp:st:A.2.6} has a critical curve that is not a local
complete intersection. Their local rings remain part of the
audit. The global conductor-duality arguments \ref{cdp:st:A.5.12}--\ref{cdp:st:A.5.13} prove
that a positive-genus conductor image in the persistent ruled
case is smooth, and the exact contractions above then remove
the vertical conductor. Thus neither local phenomenon leaves
an unproved step in the stated theorem. The assertion
is about the normalization of a reduced support and does not
claim that its full fibre has multiplicity one."""
replace(old, "", "cdp:st:C4e", "D01;D02;D11;D12;D13",
    "Remove the audit-facing defence and repeated scope paragraph. A.2.5/A.2.6 retain their local equations; the receiving persistent-fibre lemma retains the conductor-genus map and every blowdown argument. C4e states positively that its full fibre is mS for a positive integer m.", "after C4e proof")

# Expose exactly the stronger persistent-fibre conclusion already proved inside
# C4e; retain its full conductor proof once and let C4f cite the formal result.
old_c4e = block(unit, "cdp:st:C4e")
proof_start = old_c4e.index(r"\begin{proof}")
old_statement = old_c4e[:proof_start]
old_proof = old_c4e[proof_start:]
persist_start = old_proof.index(r"\ref{cdp:st:A.3.5} makes its support irreducible")
persist_end = old_proof.index(r"\item The equality $\pi_*\OO_Z=\OO_{\widetilde S}$")
persist_body = old_proof[persist_start:persist_end]
persist_body = persist_body.replace(
    r"\ref{cdp:st:A.3.5} makes its support irreducible, so it is $mS$ for a single positive integer $m$.",
    r"\ref{cdp:st:A.3.5} makes the support of $F$ irreducible, so $F=mS$ for a positive integer $m$.", 1)
persist_body = persist_body.replace(
    "Either case gives \\eqref{cdp:eq:C.21} immediately by Serre duality and descent from resolution.",
    "In either case the projection formula descends this triviality from the resolution to the normalization.")
persist_body = persist_body.replace(r"giving \eqref{cdp:eq:C.21}", "giving the asserted triviality")
persist_body = persist_body.replace(r"proves \eqref{cdp:eq:C.21}", "proves the asserted triviality")
persist_body = persist_body.replace(r"gives \eqref{cdp:eq:C.21}", "gives the asserted triviality")
assert r"\eqref{cdp:eq:C.21}" not in persist_body
lemma = r"""\begin{lemma}[Persistent sections and the normalization pullback]\hypertarget{tag-P263}{}\label{lem:II:persistent-normalization-pullback}
\StatementRecord{lem:II:persistent-normalization-pullback}{proved}{P263}{\SeriesRef{cdp:st:C.3.11}, \SeriesRef{cdp:st:A.3.5}, \SeriesRef{cdp:st:A.3.4}, \SeriesRef{cdp:st:A.5.2}, \SeriesRef{cdp:st:A.3.1}, \SeriesRef{cdp:st:A.4.9}, \SeriesRef{cdp:st:A.5.4}, \SeriesRef{cdp:st:A.5.3}, \SeriesRef{cdp:st:A.5.12}, \SeriesRef{cdp:st:A.5.13}, \SeriesRef{cdp:st:C2d}}
Let $f:Y\to\PP^1$ satisfy the integral CDP hypotheses stated in
\cref{cdp:st:C4d}, and let $F$ be a full fibre such that
\[
 H^0\bigl(F,(\Omega_Y^1\otimes M)|_F\bigr)\ne0
 \qquad(M\in\Pic(Y)).
\]
Then $F=mS$ for a positive integer $m$ and an irreducible nonnormal
reduced support $S$. For its normalization $\eta:T\to S$, the
pullback $\eta^*(M|_S)$ is trivial for every $M\in\Pic(Y)$.
\end{lemma}

\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item By \cref{cdp:st:C.3.11}, the general fibre is a two-torus
or a Hopf surface. In the Hopf case it has $h^1(\OO)=1$ and
$h^2(\OO)=0$, as used in the conductor bound below.
""" + persist_body + r"""\item Write $\pi:Z\to T$ for the normalization resolution.
The equality $\pi_*\OO_Z=\OO_T$ and the projection formula
identify the sections of a line on $T$ with those of its pullback.
Applying this to the line and its inverse descends the mutually
inverse trivializations obtained on $Z$. Since $S$ is irreducible,
$T$ is the normalization component selected above. Thus
$\eta^*(M|_S)\simeq\OO_T$ for every ambient line $M$.
\end{enumerate}
\end{proof}

"""
new_statement = old_statement.replace(
    "The assertion concerns the reduced support; no multiplicity-one conclusion is included.",
    "The full fibre over this support is $mS$ for a positive integer $m$.")
record = re.search(r"\\StatementRecord\{cdp:st:C4e\}.*", new_statement).group()
new_statement = new_statement.replace(record,
    r"\StatementRecord{cdp:st:C4e}{proved}{01FO}{\SeriesRef{cdp:st:C.1.1}, \SeriesRef{cdp:st:C.3.11}, \SeriesRef{cdp:st:C4c}, \SeriesRef{cdp:st:C4d}, \SeriesRef{cdp:st:A.5.13}, \SeriesRef{lem:II:persistent-normalization-pullback}}")
new_proof = r"""\begin{proof}
The index formula \cref{cdp:st:C.1.1} gives
$c_3(Y)=2-b_3(Y)$ and $c_3(Y)/2\in\Z$. Consequently
$c_3(Y)>0$ gives $b_3(Y)=0$.
By \cref{cdp:st:C.3.11}, the general fibre is a two-torus or a
Hopf surface. In the torus case \cref{cdp:st:C4c} supplies a fixed
full fibre with a nonzero ambient cotangent section for every
twist. In the Hopf case, $h^1(\OO)=1$ and $h^2(\OO)=0$;
\cref{cdp:st:C4d} gives persistence along the transgression line,
and \cref{cdp:st:A.5.13} identifies that line with $\Pic(Y)$.
In both cases, inversion and tensoring with $K_Y$ identify the
twisting parameter in the cited statements with every
$M\in\Pic(Y)$.

Lemma~\ref{lem:II:persistent-normalization-pullback} therefore
gives $F=mS$ with $S$ irreducible and nonnormal, and makes
$\eta^*(K_Y^{-1}\otimes L)$ trivial for every $L$.
The compact normal surface $T=\widetilde S$ is connected and
Cohen--Macaulay. Serre duality identifies the group in
\eqref{cdp:eq:C.21} with $H^0(T,\OO_T)^\vee=\C$.
\end{proof}"""
replace(old_c4e, lemma + new_statement + new_proof, "cdp:st:C4e", "D14;D02;D11",
    "Move the already-proved persistence argument to lemma P263 with exactly its integral ambient hypotheses and fixed-full-fibre all-twist hypothesis. The complete filtration, Gauduchon, conductor, blowdown and inverse-Jacobian proof is retained once. The original positive-Euler proposition retains its statement, obtains the fixed fibre through C4c/C4d and the Picard-line identification, and concludes by the same Serre pairing. C.22/C.22a/C.22b labels and targets travel with their proof.")
proof_notes["lem:II:persistent-normalization-pullback"] = [
    "Full proof transported from the persistent-fibre portion of C4e. The antecedent formerly obtained in its first step is now the lemma hypothesis. The original assumption c3>0 was used only to produce that antecedent; every subsequent argument is retained. Irreducibility identifies the chosen normalization component with T, and the final projection-formula descent is explicit."]

old = r"""\item The classification and exclusions cited in \ref{cdp:st:C4e} leave
exactly the two cohomological cases used in that proof:
torus general fibre, or $h^1(\OO)=1$, $h^2(\OO)=0$."""
new = r"""\item The classification \cref{cdp:st:C.3.11} gives the two
cohomological cases: torus general fibre, or a Hopf general fibre
with $h^1(\OO)=1$ and $h^2(\OO)=0$."""
replace(old, new, "cdp:st:C4f", "D06;D12",
    "Use the admitted final classification owner C.3.11. It supplies the same two cohomological cases used by the argument and removes the indirect reference to a prior proof's exclusion list.")
old = r"""\item Suppose the nonvanishing locus for $F=mS$ is the whole
Picard group. The proof of \ref{cdp:st:C4e}, beginning with its
fixed-fibre persistence assertion, proves that \eqref{cdp:eq:C.VC.2}
is zero. Its steps use the actual component filtration,
the inverse-Jacobian kernel, the Gauduchon bound, the
effective conductor comparison, the coherent conductor
genus bound, and the explicit constant-transverse-type
calculations. Each is independent of the Euler number
once persistence has been given."""
new = r"""\item Suppose the nonvanishing locus for $F=mS$ is the whole
Picard group. Lemma~\ref{lem:II:persistent-normalization-pullback}
makes $\eta_S^*(M|_S)$ trivial for every $M\in\Pic(Y)$.
This is exactly the vanishing of the homomorphism
\eqref{cdp:eq:C.VC.2}."""
replace(old, new, "cdp:st:C4f", "D14;D08",
    "Replace the informal invocation of a stronger part of C4e's proof by the exact persistent-fibre lemma. The applied map remains η_S^*:Pic(Y)→Pic(T_S), with the same domain and fixed support; no Euler hypothesis is imported.")
replace("The endpoint vanishings of C.1 then give", r"The endpoint vanishings of \cref{cdp:st:C.1.3} then give",
    "cdp:st:C4f", "D06", "Replace the obsolete C.1 shorthand by the exact current endpoint-vanishing proposition.")
replace(r"\CompendiumRef{II}{cdp:st:A.2.3}", r"\cref{cdp:st:A.2.3}",
    "lem:II:persistent-normalization-pullback", "D04;D06", "Resolve the normalization-kernel comparison to the same Paper II label rather than an internal compendium identifier.")

# Cite the actual primary family constructions. Their maps and local models
# establish the required premises before the deformation computations later on.
old = r"""every member of the two-parameter family in \ref{cdp:st:E13}, and every
member of the Liu--Rollenske family in \ref{cdp:st:E14}, there is a reduced"""
new = r"""every member of the two-parameter family of
\cite[Theorem~1.1, p.~2]{Viaclovsky2026Two}, and every member of
the Liu--Rollenske family of
\cite[Theorem~5.1, p.~21]{LiuRollenske2026}, there is a reduced"""
replace(old, new, "cdp:st:C4g", "D14;D18",
    "Identify both constructed families by their opened primary theorems, including the source parameter ranges. Their existence and topology are premises already proved there, so this assertion need not depend on later local deformation calculations.")
replace(r"\text{two-parameter \ref{cdp:st:E13}}", r"\text{two-parameter family}",
    "cdp:st:C4g", "D14", "The immediately preceding primary theorem citation identifies this row; remove the later construction pointer from the array label.")
replace(r"\text{Liu--Rollenske \ref{cdp:st:E14}}", r"\text{Liu--Rollenske family}",
    "cdp:st:C4g", "D14", "The immediately preceding primary theorem citation identifies this row; remove the later construction pointer from the array label.")
old = r"""\item The original local filling is the hexagonal toric quotient
in \ref{cdp:st:A.4.1}. The two-parameter construction in \ref{cdp:st:E13} places this
same filling at the simple nodal value where its specified
linearization vanishes; its other two simple nodal values
have rank-one fillings. The coordinate and line-bundle
comparisons of \ref{cdp:st:E14} place the hexagonal filling at its
separate simple node and the cuspidal quotient at the
remaining critical value. These local fillings identify the normalization of $W$ in each case
with the stated smooth rational surface."""
new = r"""\item The original local filling is the hexagonal toric quotient
in \cref{cdp:st:A.4.1}. For the two-parameter family,
\cite[Proposition~3.1 and its proof, pp.~6--7]{Viaclovsky2026Two}
gives the hexagonal filling at the zero of the linearization
and the two rank-one fillings at the other nodal values.
For the Liu--Rollenske family,
\cite[Proposition~2.5, p.~5]{LiuRollenske2026} identifies the
hexagonal fibre by gluing opposite boundary curves of
$\mathrm dP_6$. Thus the normalization map in all three cases
is the indicated opposite-side quotient of that surface."""
replace(old, new, "cdp:st:C4g", "D14;D18",
    "Replace later E13/E14 premise references with the exact opened local-filling propositions. The normalization map is explicitly the opposite-side quotient in each source, so the surface and morphism used for the Picard pullback coincide.")
old = "In the two other families\nthe integral homology is that of the six-sphere."
new = r"""In the other two families, the six-sphere topology is
\cite[Theorem~1.1, p.~2]{Viaclovsky2026Two} and
\cite[Theorem~5.1, p.~21]{LiuRollenske2026}."""
replace(old, new, "cdp:st:C4g", "D18", "Add exact primary locators to the homology premises used in the universal coefficient calculation.")
replace(r" \ref{cdp:st:C5b} gives the rank of the global normalization"+"\n"+"cohomology map for each integral twist in the original family.", "",
    "cdp:st:C4g", "D12;D14", "Remove the forward preview of C5b, which supplies no premise for this proof and repeats a later statement.")
old = r"""At the cusp in \ref{cdp:st:E14}, normalization of the
cuspidal rational curve makes its degree-zero line bundle
trivial. The lifted contracting action on this normalized
line complement is a product of a fixed automorphism of
$\PP^1$ and multiplication by a constant of modulus
strictly less than one on $\C^*$. Its quotient is a
$\PP^1$-bundle over the elliptic curve given by that
multiplicative period. The cusp normalization is
bijective; a proper continuous bijection between these
compact Hausdorff spaces is a homeomorphism. Hence
$e(C_{\rm cusp})=0$."""
new = r"""At the Liu--Rollenske cusp,
\cite[Lemma~3.10 and its proof, pp.~11--12]{LiuRollenske2026}
gives a homeomorphism over the base disc from the contraction
quotient to the cuspidal elliptic-surface neighbourhood times
$(S^1)^2$. It is obtained by trivializing the mapping torus
through the displayed isotopy of the translation and circle
multiplier. Restriction over the cusp identifies
$C_{\rm cusp}$ with the cuspidal rational curve times $(S^1)^2$.
Euler multiplicativity gives $e(C_{\rm cusp})=0$."""
replace(old, new, "cdp:st:C4g", "D17;D18;D14",
    "Use the opened primary topological product theorem, naming its base-preserving homeomorphism and its central-fibre restriction. Multiplication by e((S1)^2)=0 gives the same Euler value. This removes a reproof of the source's cusp calculation and the later E14 premise.")
old = r"""\item The explicit good-reduction covers in \ref{cdp:st:E13}--\ref{cdp:st:E14}
and the original root charts have the stated orders."""
new = r"""\item The fourth-root covers are
\cite[Lemma~3.2 and \S3.3, pp.~7--8]{Viaclovsky2026Two} and
\cite[Lemma~2.7 and Corollary~2.8, pp.~6--7]{LiuRollenske2026};
the original root charts have orders three and four."""
replace(old, new, "cdp:st:C4g", "D14;D18",
    "The opened primary root models supply the exact cover orders and free affine quotient construction. Retain the complete finite-order Picard-component and nilpotent-filtration argument, which covers the rational-homology members as well.")

# The branch exact sequence is credited through the exact local map, with the
# twisting/normal-line generalization and cohomology argument retained.
replace(r"The branch-normal quotient specializes to \citet[Lemma~6.11, p.~81]{DGKXv1} in the original family.", "",
    "cdp:st:C5a", "D13;D18", "Move the primary-source comparison into the proof where the local branch map is identified.", "between C5a statement and proof")
old_c5a = block(unit, "cdp:st:C5a")
a = old_c5a.index(r"\begin{proof}")
old = old_c5a[a:]
new = r"""\begin{proof}
On a chart $S=(z_1\cdots z_r=0)$, the morphism is
\[
 \sum_i a_i\partial_{z_i}
   \longmapsto (a_i|_{z_i=0})_{1\le i\le r}.
\]
This is the branch-coefficient morphism in the proof of
\cite[Lemma~6.11, p.~81]{DGKXv1}. Its exactness there uses only
this local coordinate description, which is identical on the
present normal-crossing charts. The normal-line transitions
identify its target with $\nu_*N_\nu$, and immersion adjunction
gives $N_\nu=K_{\widetilde S}\otimes\nu^*K_Y^{-1}$.
Tensor by $L$ and apply coherent cohomology. Exact finite
pushforward identifies the normalization term with its
cohomology on $\widetilde S$, giving \eqref{cdp:eq:C.4}.
Serre duality on that smooth compact surface identifies the
target with the stated dual section space. In particular,
$H^3(Y,\mathcal T\otimes L)=0$ makes the map surjective.
\end{proof}"""
replace(old, new, "cdp:st:C5a", "D17;D18",
    "Cite exactness of the identical local branch-coefficient morphism from DGKX v1 Lemma 6.11 rather than reproving its independent coefficient lifts and kernel. Retain the general normal-line adjunction, tensor map, finite-pushforward identification, long exact sequence and Serre target. This establishes the exact scope map from the source's local proof to the stated divisor.")

# The fixed data and their sign convention form one numbered definition, with
# the original transgression calculation retained as its well-definedness proof.
setup_start = unit.index("In this subsection $X=X_c$")
setup_end = unit.index(r"\begin{proposition}[Integral twists", setup_start)
old = unit[setup_start:setup_end]
new = r"""\begin{definition}[The marked Picard parameter]\hypertarget{tag-P261}{}\label{def:II:marked-Picard-parameter}
\StatementRecord{def:II:marked-Picard-parameter}{proved}{P261}{}
Let $X=X_c$ be the period construction of \cite[Setup and Main
Theorem, p.~2]{AC26}, with admissible parameter $c$, clockwise
affine vectors $v_1=(1,2,-4,0)^t$, $v_2=(-1,-3,3,0)^t$, and
untwisted cusp collar. Thus $p=12l_0-4l_1-3l_2=-1$.
Write $\mathfrak B=\PP(3,4)$, let $\rho:\mathfrak B\to B$ be its
coarse map, and let $\bar f:X\to\mathfrak B$ be the root
factorization. Put $\mathcal T=T_X(-\log W)$ and let
$\nu:\mathrm dP_6\to X$ normalize $W$.
The integral root lines are
\[
 M_n=\bar f^*\OO_{\mathfrak B}(n)
     =\OO_X(n(S_1-S_2)),\qquad n\in\Z.
\]
The exponential isomorphism $H^1(X,\OO_X)\to\Pic(X)$ identifies
$\Pic(X)$ with $\C$. Fix its coordinate by
$M_z=\exp(z\gamma^{0,1})$ and $M_1=\OO_X(S_1-S_2)$.
The period rows are the fixed $\tau,\mu,\beta_c$ of the setup;
their relation to the elliptic-quotient coordinates is described
in \cite[\S1.3, pp.~2--3]{Engel2026}.
\end{definition}

\begin{proof}[Well-definedness of the coordinate]
The clockwise transgression sends $12\gamma$ to $-p=1$.
Indeed, evaluation of the finite lifts on $v_1,v_2$ gives the
integral periods $4l_1,3l_2$, and the cusp contributes
$-12l_0$; their sum is $-p$. The exponential sequence therefore
gives $\exp(12\gamma^{0,1})=f^*\OO_B(1)$. Its injectivity and
the root relation identify $\exp(\gamma^{0,1})$ with
$\OO_X(S_1-S_2)$, fixing the sign used in $M_1$.
\end{proof}

"""
replace(old, new, "def:II:marked-Picard-parameter", "D13;D18",
    "Make the fixed family, root-stack lines, Picard coordinate and sign convention one numbered definition. The original clockwise transgression calculation is retained as its well-definedness proof. The AC setup and Engel's exact period/quotient discussion were opened at the indicated pages.", "start of integral/nonintegral resonance subsection")

# Expose the actual chain isomorphism behind the regular normal form.
old = r"""Thus $a$ has a simple zero; choosing its direction as the second cocycle frame and changing the vertical frame gives
\[
 a=(0,s),\qquad\kappa=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]"""
new = r"""Thus $a=s b(s)$ for a primitive holomorphic column $b$.
Permute the two cocycle coordinates so that $b_2$ is a unit and put
\[
 C=\begin{pmatrix}1&-b_1/b_2\\0&1/b_2\end{pmatrix},
 \qquad J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad R=J(\kappa C^t)^{-1}.
\]
The coefficient changes $a\mapsto Ca$ and
$\kappa\mapsto R\kappa C^t$ are induced by the cocycle and
vertical frame changes, extended to their exterior powers.
Their inverses are
$C^{-1}=\left(\begin{smallmatrix}1&b_1\\0&b_2\end{smallmatrix}\right)$
and $R^{-1}=\kappa C^tJ$. These holomorphic invertible maps
carry \eqref{cdp:eq:C.13} to
\[
 a=(0,s),\qquad\kappa=J.
\]"""
replace(old, new, "cdp:st:C5c", "D22",
    "Supply the explicit invertible coefficient/frame maps for the regular-resonance normal form: Cb=(0,1), RκC^t=J, with displayed inverses. These maps act on the two tensor factors and their exterior powers, hence give an actual isomorphism of the written local complex. The original module quotient calculations and resulting lengths remain unchanged.")

# Preserve the mathematical jump-locus result; discard the production history
# and the internal assertion being corrected, already replaced by C5b's rank.
closing_start = unit.index("Statements \\ref{cdp:st:C5b}--\\ref{cdp:st:C5c} reproduce")
old = unit[closing_start:]
new = r"""\begin{corollary}[The generic tangent tuple and its jump loci]\hypertarget{tag-P262}{}\label{cor:II:tangent-jump-loci}
\StatementRecord{cor:II:tangent-jump-loci}{proved}{P262}{\SeriesRef{cdp:st:C5b}, \SeriesRef{cdp:st:C5c}, \SeriesRef{cdp:st:C.1.1}}
For the marked family of \cref{def:II:marked-Picard-parameter},
$\chi(X,T_X\otimes M_z)=1$ for every $z\in\C$. Its generic
tangent tuple is $(0,0,1,0)$, attained at every real
nonintegral $z$. For each $q$ and each integer $k$ strictly larger
than the generic value of $h^q$, the set
\[
 \{z\in\C:h^q(X,T_X\otimes M_z)\ge k\}
\]
is a proper locally discrete complex analytic subset of the
Picard line. The nonzero degree-two group, index one and
$c_3(X)=2$ correct respectively parts (a), (b) and (c) of
\cite[Theorem~2.2, p.~680]{CDP2020} for this family.
\end{corollary}

\begin{proof}
The index is $c_3(X)/2=1$ by \cref{cdp:st:C.1.1}.
For real nonintegral $z$, \eqref{cdp:eq:C.10} has no regular
resonance and the nonreal generators of $\Lambda_1,\Lambda_2$
give $\ell_1(z)=\ell_2(z)=0$. Thus
\cref{cdp:st:C5c} gives $(0,0,1,0)$.
Choose a global $\bar\partial$-closed $(0,1)$-form $\alpha$
representing the chosen Picard coordinate. The operators
$\bar\partial+z\alpha$ define its holomorphic universal line
family on $X\times\C$. Proper coherent semicontinuity makes
each displayed cohomology threshold analytic. It is proper
because every real nonintegral parameter has the stated
generic tuple, so it is locally discrete in $\C$.
\end{proof}

"""
replace(old, new, "cor:II:tangent-jump-loci", "D01;D04;D08;D13;D18",
    "Transport the closing paragraph's index, generic tuple, real-parameter attainment and analytic jump-locus proof into one numbered corollary. Remove the internal S6_01 comparison and independence claim. C5b already gives the exact normalization-map exception; its statement and proof remain. The correction of published CDP20 is retained with its exact locator.", "after C5c proof")

# Local typography and pointer repairs are attributed to their complete owner.
for old, new, owner in [
    ("on the Kahler resolution", r'on the K\"ahler resolution', "lem:II:persistent-normalization-pullback"),
    ("of zero Kahler volume", r'of zero K\"ahler volume', "lem:II:persistent-normalization-pullback"),
    ("gives the etale conductor cover", r"gives the \'etale conductor cover", "lem:II:persistent-normalization-pullback"),
    ("exponentiated Cech cocycles", r"exponentiated \v Cech cocycles", "cdp:st:C4d")]:
    replace(old, new, owner, "D23", "Restore the mathematical name/accent; the associated morphism and proof step are unchanged.")

replace(" No factorization of $h$ through the blowdown is asserted or needed.", "",
    "lem:II:persistent-normalization-pullback", "D02",
    "The preceding displayed divisor pullback and intersection calculation already state exactly the map being used. Delete the defensive disclaimer; retain the complete coefficient calculation.")
replace("We derive the possible transverse reduced plane curves rather than assuming a list of singularities.",
    "We determine the transverse reduced plane curves from these conductor exponents.",
    "lem:II:persistent-normalization-pullback", "D02",
    "State the conductor-exponent computation directly; its complete branch-ring and intersection argument follows unchanged.")
replace("This conclusion permits nonreduced conductor image\nschemes and imposes no assumption on the original singular\ncurve. We can therefore apply", "We can therefore apply",
    "lem:II:persistent-normalization-pullback", "D02;D11",
    "Remove the repeated defensive scope sentence after the smoothness conclusion. The lemma already treats the entire reduced support and its actual conductor; both genus bounds and all scheme-theoretic proof steps are retained.")
replace("The generator exists under the stated rational Betti-number assumptions. Its normalization condition is a condition on an explicit integral cohomology class, with no tangent-cohomology vanishing assumed.",
    "The generator exists under the stated rational Betti-number assumptions; its normalization condition concerns the indicated integral cohomology class.",
    "cdp:st:C4a", "D02",
    "Retain the existence and precise integral normalization condition, and remove the defensive claim about an unassumed tangent vanishing. The full seven-step proof supplies the existence and the exact implication.")
for old, new, owner in [
    (r"let $\rho:\mathfrak B\to B$", r"let $\rho_B:\mathfrak B\to B$", "def:II:marked-Picard-parameter"),
    (r"gives $\rho_*\OO(n)=\OO_B(d(n))$", r"gives $\rho_{B*}\OO(n)=\OO_B(d(n))$", "cdp:st:C5b"),
    (r"higher direct images of $\rho$", r"higher direct images of $\rho_B$", "cdp:st:C5b"),
    (r"and then $\rho_*$", r"and then $\rho_{B*}$", "cdp:st:C5b")]:
    replace(old, new, owner, "D20",
        "Name the coarse map rho_B to distinguish its domain and codomain from the elliptic period rho=tau(z1) in C5c. This is the identity renaming of the same coarse morphism; its monomial frame map and pushforward remain unchanged.")
old_record = re.search(r"\\StatementRecord\{cdp:st:C4f\}.*", unit).group()
new_record = old_record.replace(r"\SeriesRef{cdp:st:C4e}", r"\SeriesRef{lem:II:persistent-normalization-pullback}, \SeriesRef{cdp:st:C.3.11}")
replace(old_record, new_record, "cdp:st:C4f", "D14",
    "Update the nonprinting dependency metadata to the exact receiving lemma and classification owner. The established tag-only header convention remains unchanged.")
old_record = re.search(r"\\StatementRecord\{cdp:st:C4g\}.*", unit).group()
new_record = r"\StatementRecord{cdp:st:C4g}{proved}{01FQ}{\SeriesRef{cdp:st:A.3.4}, \SeriesRef{cdp:st:A.4.1}, \SeriesRef{cdp:st:C.1.3}, \SeriesRef{cdp:st:D.1.9}; \cite[Theorem~1.1 and Proposition~3.1]{Viaclovsky2026Two}; \cite[Proposition~2.5, Lemma~3.10 and Theorem~5.1]{LiuRollenske2026}}"
replace(old_record, new_record, "cdp:st:C4g", "D14",
    "Match the nonprinting dependency metadata to the actual source inputs and prior fibre propositions, removing the later E13/E14/C5b references that no longer appear in the proof. The established tag-only header convention remains unchanged.")

# Equation numbers are assigned by the paper's section counter.  Retain every
# complete formula, label and permanent target, including aligned groups.
def owner_at(position):
    candidates = list(re.finditer(r"\\begin\{(?:proposition|lemma|corollary|definition)\}.*?\\label\{([^{}]+)\}", unit[:position], re.S))
    return candidates[-1].group(1) if candidates else "sec:II:12"

for match in list(re.finditer(r"\\\[(.*?)\\\]", unit, re.S))[::-1]:
    old = match.group(0)
    if not re.search(r"\\tag\{[^{}]+\}", old):
        continue
    label = re.search(r"\\label\{([^{}]+)\}", old).group(1)
    new = r"\begin{equation}" + re.sub(r"\\tag\{[^{}]+\}", "", match.group(1)) + r"\end{equation}"
    replace(old, new, owner_at(match.start()), "D19",
        "Convert the labelled bracket display to equation and remove only its inherited manual tag. Preserve the full formula and exact label/permanent target; the section counter supplies its receiving number.", "equation " + label)
for match in list(re.finditer(r"\\begin\{align\*\}(.*?)\\end\{align\*\}", unit, re.S))[::-1]:
    old = match.group(0)
    if not re.search(r"\\tag\{[^{}]+\}", old):
        continue
    body = re.sub(r"\\tag\{[^{}]+\}", "", match.group(1))
    target = re.search(r"\\hypertarget\{tag-[^{}]+\}\{\}\\label\{([^{}]+)\}", body)
    assert target, old
    label, anchor = target.group(1), target.group(0)
    body = body.replace(anchor, "")
    new = r"\begin{equation}"+"\n"+r"\begin{aligned}"+body+r"\end{aligned}"+"\n"+anchor+"\n"+r"\end{equation}"
    replace(old, new, owner_at(match.start()), "D19",
        "Keep the entire aligned formula as one equation/aligned group. Move its unchanged label and permanent target to the outer equation, eliminating the old manual tag while retaining the single-number scope.", "aligned equation " + label)

assert r"\tag{" not in unit
assert r"\CompendiumRef" not in unit
for command, prefix in [("label", ""), ("hypertarget", "tag-")]:
    pattern = r"\\" + command + r"\{(" + prefix + r"[^{}]+)\}"
    old_names, new_names = re.findall(pattern, old_unit), re.findall(pattern, unit)
    assert set(old_names).issubset(new_names), (command, set(old_names)-set(new_names))
    assert len(new_names) == len(set(new_names)), (command, "duplicate")

fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
def write_tsv(path, rows, names):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=names, delimiter="\t", lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)

args = argparse.ArgumentParser()
args.add_argument("--reviewed", action="store_true")
reviewed = args.parse_args().reviewed
if reviewed:
    for row in rows:
        row["review_status"] = "Complete original and receiving owner proof read and compared; actual scope maps recorded; no independent re-derivation claimed."
write_tsv(OUT / "S6_SERIES_PUBLISH_section12_defects.tsv", rows, fields)
(OUT / "S6_SERIES_PUBLISH_section12_proposed.tex").write_text(unit)

owners = ["cdp:st:C4c", "cdp:st:C4a", "cdp:st:C4b", "cdp:st:C4d", "cdp:st:C4e", "cdp:st:C4f", "cdp:st:C4g", "cdp:st:C5a", "cdp:st:C5b", "cdp:st:C5c", "lem:II:persistent-normalization-pullback", "def:II:marked-Picard-parameter", "cor:II:tangent-jump-loci"]
notes = {
    "cdp:st:C4c":"Read the entire finite-fibre criterion proof: analytic loci, full-measure non-torsion intersection, torsion Chern class on a smooth torus, top-degree base change, component-preserving positive twist, Leray converse and fixed irreducible support. All five steps retain their actual line-bundle maps.",
    "cdp:st:C4a":"Read all seven steps: integral transgression, irrational unitary characters, finite-order representatives in each Picard component, dual twisting by K_Y, normalization pullback, étale thickening filtration, finite-locus criterion and Euler equality. The proof and hypotheses are retained.",
    "cdp:st:C4b":"Read both proof steps, including the positive base twist contradiction and the exact identification with the previously proved normal-crossing fibre target. The Cartier-fibre adjunction and Serre pairing are unchanged.",
    "cdp:st:C4d":"Read all five steps and both cohomological cases: transgression flat local system, discrete parameter loci, smooth-fibre vanishing, full-thickening vanishing, and positive-Euler fixed nonnormal support. Only the duplicate preview and citation typography change.",
    "cdp:st:C4e":"Compared the complete original proof with its two receiving owners: the all-twist persistent-fibre argument is now the full lemma P263, while C4e retains fixed-fibre existence under c3>0 and the identical Serre-duality target. The positive integral index implies b3=0 explicitly.",
    "cdp:st:C4f":"Read both implications and all-twist nonvanishing. The persistent-fibre lemma now supplies the zero Picard pullback directly; the last ideal-layer injection, normalization submodule, base-fibre trivialization, torsion direct-image support and analytic continuation are unchanged.",
    "cdp:st:C4g":"Read all five steps. Opened AC26 pp.57,60, Two pp.2,6–8 and LR pp.5–7,11–12,21. The known local fillings and homology now have exact primary locators. The LR cusp uses the source's explicit homeomorphism over the disc, restricted to its central fibre. The finite-order Picard representatives and every nilpotent layer remain, including original-family d>1 members.",
    "cdp:st:C5a":"Opened DGKX v1 Lemma6.11 p.81. The coordinate morphism is literally the same normal-coefficient map on r local branches. Exactness is cited through that map; the general adjunction twist and the H2-to-H3 connecting-map identification remain fully justified.",
    "cdp:st:C5b":"Read all six steps: root-bundle and logarithmic tangent maps, scalar normalization complex, explicit frame inverses, δ0 quotient, δ1 doubled-point cokernel, the nontrivial cusp extension O(-6)→O(6), weighted monomial identification, stabilizer invariants, Leray filtration and semigroup evaluation. Formula payloads and all module maps are unchanged.",
    "cdp:st:C5c":"Read all six steps, including the Fourier comparison, regular cohomology quotients, order-three jet and frame maps, stabilizer characters, cusp chain homotopy, coherence/finiteness and normalization surjectivity. Added explicit C,R frame maps with their inverses for the regular normal form. Opened AC26 Remark3.12 p.19 and Atkin–Garvan v1 equations3.2/3.5 p.8; the latter gives g2'(ρ)=−3ig3(ρ)/π after g2=(4π^4/3)E4 and g3=(8π^6/27)E6, with E4(ρ)=0.",
    "lem:II:persistent-normalization-pullback":"Compared all nine receiving steps against the source C4e proof. The fixed full-fibre all-twist hypothesis is exactly the old step1 conclusion. The component filtration, inverse-Jacobian section locus, fixed resolution/Gauduchon argument, exact blowdown coefficient a=d−1, horizontal conductor cases, transverse plane-curve conductor calculation, elliptic image, minimal ruled contraction and two-point Picard support are retained, ending with the same projection-formula descent.",
    "def:II:marked-Picard-parameter":"Compared the original unnumbered setup and all of its transgression-sign proof with the new definition and well-definedness proof. Every vector, root line, parameter and exponential convention is preserved. AC's Setup p.2 and Engel§1.3 pp.2–3 were read at their actual period/quotient identification.",
    "cor:II:tangent-jump-loci":"Compared the mathematical content of the original closing paragraph with the receiving corollary and proof. The index, real nonintegral tuple and proper analytic cohomology thresholds survive; production-history claims and the already-stated normalization-map exception are not duplicated. The proper threshold condition is stated explicitly as k exceeding the generic hq.",
}
events = []
date = datetime.now(timezone.utc)
event_fields = next(csv.reader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
if reviewed:
    for owner in owners:
        row = {field:"" for field in event_fields}
        row.update(statement_id=owner, date=date.date().isoformat(),
            who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance",
            type="used and rechecked in this run", outcome=notes[owner]+" This is an exposed complete-proof/editorial comparison, not an independent derivation or final PDF reading.",
            event_id="publish:c3:tangent:"+owner, phase="publication text and proof comparison",
            source_file="agents/continuation3_provenance/section12/S6_SERIES_PUBLISH_section12_CHECK_EVENTS.tsv",
            source_event_type="used and rechecked in this run", evidence_group="publish:c3:tangent:"+owner,
            date_utc=date.isoformat(), where="sec:II:12: complete original and receiving proof/statement comparison")
        events.append(row)
    write_tsv(OUT / "S6_SERIES_PUBLISH_section12_CHECK_EVENTS.tsv", events, event_fields)
status = dict(unit="sec:II:12", original_source="S6_SERIES_PUBLISH_II.tex, checkpoint-35 section; preserved in supplied base archive and per-instance old/new rows",
    original_section_sha256=hashlib.sha256(old_unit.encode()).hexdigest(), proposed_section_sha256=hashlib.sha256(unit.encode()).hexdigest(),
    proposed_fragment="S6_SERIES_PUBLISH_section12_proposed.tex", edit_rows=len(rows), comparison_completed=reviewed,
    old_statement_owners=10, receiving_owners=13, new_tags={"P261":"def:II:marked-Picard-parameter","P262":"cor:II:tangent-jump-loci","P263":"lem:II:persistent-normalization-pullback"},
    shared_files_written=False, final_pdf_read=False, inherited_required_check_gate_recounted=False,
    remaining_integration=["Place E8 and E16 before C5b/C5c when ordering the complete later tangent/period/deformation part.","Resolve the other exact premise order with sections13–14; those blocks are the next assigned work.","Root integrates fragment, computes final counts and reads final rendered pages."],
    source_evidence="Primary PDFs remain outside the checkpoint; metadata and own paraphrases only in the section sources TSV and comparison events.")
status["all_class_pass"] = {f"D{i:02d}": (
    "Applied in exact old/new rows; original and receiving complete proofs compared" if any(f"D{i:02d}" in r["type"].split(";") for r in rows)
    else "Established tag-only headers and retained titles preserved; no reopening" if i in (10,16)
    else "No further instance found in the complete bounded text reading") for i in range(1,26)}
(OUT / "S6_SERIES_PUBLISH_section12_status.json").write_text(json.dumps(status,indent=2)+"\n")
(ROOT / "code" / "S6_SERIES_PUBLISH_c3_provenance_section12.out").write_text(json.dumps(status,indent=2)+"\n")
print(json.dumps(status,indent=2))
