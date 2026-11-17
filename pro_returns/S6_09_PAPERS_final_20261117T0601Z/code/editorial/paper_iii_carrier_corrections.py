"""Apply checked corrections at their actual uses in the namespaced carriers.

Call ``transform`` on the joined, expanded ``wb:`` carrier text, or on the
whole joined Paper III body, before cross-paper reference resolution and
``add_uses``.  The function is idempotent.  It does not assemble or write a
manuscript.  It also accepts one namespaced carrier source at a time; a final
call after appending the repair files removes the two consumed prose copies.

The original sources remain unchanged.  The complete compact-chart argument
is inserted into its original proof.  The original framed-torus proof, the
distinct extension homotopy, the general wedge lemma, and the finite-band
repair remain complete.  The four missing ``cusp-spec`` dependencies are
restored by a complete nonspectral period/quotient calculation.

Evidence: work/cdp_audit/carrier_integration_audit.json and the five repair
files in work/maps_audit/.  Full receiving proofs of the five working source
files were previously checked by /root/maps_audit; this event checks the
listed replacements and their actual receiving contexts.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "deliverables/work"


def _repair(name: str) -> str:
    s = (WORK / "maps_audit" / (name + ".tex")).read_text()
    return "\n".join(x for x in s.splitlines() if not x.lstrip().startswith("%")) .strip()


def _replace_guarded(s: str, old: str, new: str, guard: str, tag: str) -> str:
    marker = "% checked carrier correction: " + tag
    count = s.count(old)
    if count:
        if count != 1:
            raise ValueError(f"Carrier correction {tag}: expected one old block, found {count}")
        return s.replace(old, marker + "\n" + new, 1)
    if guard in s and marker not in s:
        raise ValueError(f"Carrier correction {tag}: source guard exists but anchor changed")
    return s


DECK_OLD = r"""where \(\Delta=\pi_1(B^\circ)\) acts diagonally through the deck action
on \(\mathfrak h_z^\circ\) and the restricted monodromy on
\(L_\Lambda\)."""

DECK_NEW = r"""where \(\Delta\) is the actual triangle deck group of
\(\mathfrak h_z^\circ\to B^\circ\).  It acts diagonally by its deck action
and by the restricted integral monodromy on \(L_\Lambda\).
The deck representation maps \(\pi_1(B^\circ)\) onto \(\Delta\);
these two groups are not identified.  Equivalently, one can replace
\(\mathfrak h_z^\circ\) by the universal cover of \(B^\circ\) and
take the quotient by \(\pi_1(B^\circ)\).
The invariant-lattice calculation uses the image of the monodromy
representation, while finite base covers correspond to finite-index
subgroups of \(\pi_1(B^\circ)\)."""

KUMMER_OLD = r"""The logarithmic-position regions associated with any two fixed toric
charts are bounded.  Hence only finitely many $\bar\lambda$ can translate
one of them to meet the other.  Local finiteness of the fan reduces the
same assertion for compact sets to finitely many chart pairs, proving
proper discontinuity.  Finally, reducing
$B_{N,v}^{-1}y(\xi,v)$ modulo $\mathbb Z^2$ places every orbit meeting a
closed subdisc in finitely many closed unit toric charts.  Their union is
compact.  This proves properness of $f_N$.  """

WEDGE_OLD = r"""Since \(\mathcal C\) is a simply connected
finite three-complex, Hurewicz supplies a sphere representing the
\(H_2\)-generator, and the Whitehead exact sequence makes
\(\pi_3(\mathcal C)\to H_3(\mathcal C)\) surjective.  A wedge of
representing maps
\(S^2\vee S^3\to\mathcal C\) is a homology equivalence between simply
connected CW complexes, hence a homotopy equivalence."""

WEDGE_NEW = r"""Since \(\mathcal C\) is simply connected, Hurewicz gives a based
map \(a:S^2\to\mathcal C\) inducing an isomorphism on \(H_2\)
and on \(\pi_2\).  Replace this map by its mapping-cylinder
inclusion \(S^2\hookrightarrow M_a\), with
\(M_a\simeq\mathcal C\).  Both spaces are simply connected and
the map on \(\pi_2\) is an isomorphism, so the pair is
\(2\)-connected.  Relative Hurewicz gives
\[
 \pi_3(M_a,S^2)\cong H_3(M_a,S^2;\mathbb Z).
\]
The homology exact sequence identifies the right side with
\(H_3(M_a;\mathbb Z)=\mathbb Z\): the preceding group
\(H_3(S^2)\) is zero, and the following map on \(H_2\) is an
isomorphism.  The homotopy exact sequence makes
\(\pi_3(M_a)\to\pi_3(M_a,S^2)\) surjective, since its next
map has image in the zero kernel of
\(\pi_2(S^2)\to\pi_2(M_a)\).  Naturality of Hurewicz therefore
gives a based map \(b:S^3\to\mathcal C\) representing an integral
generator of \(H_3(\mathcal C)\).  The wedge \(a\vee b\) is an
integral homology equivalence in every degree.  The homological
Whitehead theorem, with its complete proof in
\cref{mapsI:pf:theorem:5.1}, makes this map a homotopy equivalence."""

NULL_OLD = r"""The one-copy class
\([\widehat q_3]\in\pi_6(S^3)\) is now zero by
Theorem~\ref{wb:cusp-null:thm}; the one-copy class
\([\widehat q_\gamma]\in\pi_6(S^2)\) remains open."""

NULL_NEW = r"""The one-copy class
\([\widehat q_3]\in\pi_6(S^3)\) is zero by the complete framed-torus
proof in \cref{wb:cusp-null:thm}.  Both this class and
\([\widehat q_\gamma]\in\pi_6(S^2)\) also vanish by the extension
homotopy in \cref{mapsIII:angle-forgotten-one-copy-null}.  That proof
uses the original formulas after forgetting the base angle and fixes
the chosen point of the central fibre throughout.  It supplies based
nullhomotopies of all their positive smash powers.  The retained-angle
map has a different target and is outside that assertion."""

CHANGES = [
    {
        "id": "carrier-deck-group",
        "result": "WORK:cusp-spec-globalization-obstruction",
        "source": "sources/workbench/cusp_globalization_replacement.tex:49–58",
        "action": "Replace Delta=pi1(B°) at its defining quotient by the actual triangle deck group; retain the universal-cover alternative and finite-index scope.",
        "proof": "work/maps_audit/globalization_deck_group_correction.tex",
    },
    {
        "id": "carrier-compact-chart-control",
        "result": "WORK:cusp-cover-extension-theorem",
        "source": "sources/workbench/cusp_toric_cover_completion.tex:191–221",
        "action": "Replace the false bounded-whole-chart assertion and abbreviated properness step by the complete compact-subset proof, with compact chart pieces and the properness of f_N explicitly specified.",
        "proof": "work/maps_audit/kummer_compact_chart_repair.tex",
    },
    {
        "id": "carrier-relative-hurewicz",
        "result": "WORK:cusp-cone-target-homotopy-types",
        "source": "sources/workbench/cusp_sphere_route_strengthening.tex:839–877",
        "action": "Expand the H3 spherical-generator step by the complete mapping-cylinder, relative-Hurewicz and exact-sequence argument. Preserve the separate general lemma and all subsequent smash calculations.",
        "proof": "work/maps_audit/carrier_three_complex_wedge.tex",
    },
    {
        "id": "carrier-one-copy-status",
        "result": "WORK:cusp-cone-sphere-map-homotopy-status",
        "source": "sources/workbench/cusp_sphere_route_strengthening.tex:659–676",
        "action": "Replace the obsolete open circle-class sentence by both actual angle-forgotten one-copy vanishing conclusions. Preserve the original framed-torus proof, universal two-copy order proof and full additional extension proof.",
        "proof": "work/maps_audit/carrier_nullhomotopy_by_extension.tex",
    },
    {
        "id": "carrier-missing-prerequisites",
        "result": "Four missing wb:cusp-spec references",
        "source": "sources/workbench/cusp_spectral_geometry.tex:4–153,190–241,722–770,866–944",
        "action": "Restore only the required period definitions, complete inverse-transpose computation, exact compact quotient and geometric systolic/ball proofs. No Laplacian, eigenvalue, counting-law or other spectral theorem is imported.",
        "proof": "work/cdp_audit/carrier_radial_prerequisites.tex",
    },
    {
        "id": "finite-degree-three-location",
        "result": "WORK:prop:actual-finite-band-maps",
        "source": "sources/workbench/topology_reduction.tex:731–734,772–780",
        "action": "No further III replacement: that original statement is absent from III and was already corrected at the actual statement and proof in I, mapsI:top:prop:actual-finite-band-maps, with the complete repair at mapsI:top:finite-degree-three (I Proposition E.11). Preserve the complete III re-derivation if retained by the assembler.",
        "proof": "work/maps_audit/finite_degree_three_correction.tex",
    },
    {
        "id": "carrier-known-S12-routing",
        "result": "WORK:cusp-cone-S12-almost-complex-obstruction",
        "source": "sources/workbench/cusp_cone_sphere_routes.tex:640–786",
        "action": "Move the complete proposition and all three full proofs to the known-results appendix, explicitly credit Borel–Serre Section15 Proposition15.1 p434 at the statement, and retain a numbered forward reference at the original use. Preserve the following independent cusp-cone-obstructions theorem.",
        "proof": "work/maps_audit/carrier_source_checks.json",
    },
]


def _route_known_obstruction(s: str) -> str:
    """Move the whole source block once the joined known appendix exists."""
    marker = "% BEGIN relocated classical S12 obstruction 2026-11-17"
    appendix = r"\label{app:III:known}"
    label = r"\label{wb:cusp-cone-S12-almost-complex-obstruction}"
    if marker in s or appendix not in s or label not in s:
        return s
    pos = s.index(label)
    start = s.rfind(r"\begin{proposition}", 0, pos)
    if start < 0:
        raise ValueError("S12 obstruction proposition beginning not found")
    proof_start = s.index(r"\begin{proof}", pos)
    stop = s.index(r"\end{proof}", proof_start) + len(r"\end{proof}")
    block = s[start:stop]
    if r"\label{wb:cusp-cone-obstructions}" in block:
        raise ValueError("S12 move would absorb the following independent theorem")
    proof = block[block.index(r"\begin{proof}"):]
    caption_old = r"\begin{proposition}[Exact almost-complex obstruction on \(S^{12}\)]"
    caption_new = r"\begin{proposition}[Borel--Serre obstruction on \(S^{12}\), with three complete proofs]"
    if caption_old not in block:
        raise ValueError("S12 obstruction caption changed before credit routing")
    block = block.replace(caption_old, caption_new, 1)
    block = block.replace(
        label,
        label + "\n" + r"""The obstruction is the classical theorem of Borel and Serre
\cite[\S15, Proposition~15.1 and the following remark, p.~434]{BorelSerre1953}.
The complete statement and the three distinct derivations are retained here.""",
        1,
    )
    assert block[block.index(r"\begin{proof}"):] == proof
    forward = r"""The obstruction to an almost-complex structure on \(S^{12}\),
with all three complete classical proofs, is given in
\cref{wb:cusp-cone-S12-almost-complex-obstruction}.
"""
    s = s[:start] + forward + s[stop:]
    dest = s.index(appendix) + len(appendix)
    addition = ("\n\n" + marker + "\n"
                + "\\subsection{Classical almost-complex sphere obstructions}\n"
                + block + "\n% END relocated classical S12 obstruction 2026-11-17\n\n")
    return s[:dest] + addition + s[dest:]


def transform(s: str) -> str:
    """Return the corrected namespaced carrier text; fail on changed anchors."""
    # Consume the unlabelled appended prose copies only after using their
    # complete mathematical content at the original statements/proofs below.
    s = _replace_guarded(
        s, DECK_OLD, DECK_NEW,
        r"\label{wb:cusp-spec-global-kernel-family}", "deck-group",
    )

    compact = _repair("kummer_compact_chart_repair")
    compact_body = compact.split("\n", 1)[1].strip()
    compact_body = compact_body.replace(
        "A compact set meets a finite chart subcover, so this applies\n"
        "to every compact set on the dense-torus locus.",
        "Every point of a compact set has a neighbourhood whose closure\n"
        "is compact in one maximal chart.  Choose a finite such cover;\n"
        "the intersections with these compact closures give finitely many\n"
        "compact chart pieces covering the original set.  Applying the\n"
        "preceding estimate to these pieces bounds all of its logarithmic\n"
        "positions on the dense-torus locus.",
    )
    compact_body = compact_body.replace(
        "For properness of the quotient map, reduce",
        "To prove that $f_N$ is proper, reduce",
    )
    compact_body = compact_body.replace(
        "Therefore every such orbit has a representative in finitely many\n"
        "closed unit polydiscs, a compact subset of the smooth Hausdorff toric\n"
        "space.",
        "Fix a closed subdisc strictly inside the chosen action disc.\n"
        "Every orbit over that subdisc has a representative in finitely\n"
        "many closed unit polydiscs intersected with its inverse image.\n"
        "These intersections are closed subsets of compact polydiscs\n"
        "in the ambient smooth Hausdorff toric space, and all lie in the\n"
        "domain where the modified action is defined.",
    )
    s = _replace_guarded(
        s, KUMMER_OLD, compact_body + "\n\n",
        r"\label{wb:cusp-cover-extension-theorem}", "compact-chart-control",
    )
    s = _replace_guarded(
        s, WEDGE_OLD, WEDGE_NEW,
        r"\label{wb:cusp-cone-target-homotopy-types}", "relative-hurewicz",
    )
    s = _replace_guarded(
        s, NULL_OLD, NULL_NEW,
        r"\label{wb:cusp-cone-sphere-map-homotopy-status}", "one-copy-status",
    )

    # The missing labels carry necessary nonspectral data, so they cannot be
    # replaced by a generic reference to the cone-descent lemma.
    global_label = r"\label{wb:cusp-spec-globalization-obstruction}"
    prerequisite_label = r"\label{mapsIII:carrier-radial-prerequisites}"
    if global_label in s and prerequisite_label not in s:
        pos = s.index(global_label)
        start = s.rfind(r"\begin{theorem}", 0, pos)
        if start < 0:
            raise ValueError("Could not locate the globalization theorem beginning")
        extra = (WORK / "cdp_audit/carrier_radial_prerequisites.tex").read_text().strip()
        s = s[:start] + extra + "\n\n" + s[start:]

    if "% checked carrier correction: deck-group" in s:
        raw = _repair("globalization_deck_group_correction")
        if s.count(raw) > 1:
            raise ValueError("Multiple appended deck-group repair copies")
        s = s.replace(raw, "")
    if "% checked carrier correction: compact-chart-control" in s:
        if s.count(compact) > 1:
            raise ValueError("Multiple appended compact-chart repair copies")
        s = s.replace(compact, "")
    return _route_known_obstruction(s)
