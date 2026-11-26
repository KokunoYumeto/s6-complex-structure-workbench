"""Authorized publication pass for the finite cohomology/Euler unit."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_cohomology", "III-C8-FND-COHOM-")
    old_heading = r"\subsection{Rational elliptic starting configurations and exact computations}"
    new_heading = r"\subsection{Integral cohomology, Euler numbers and clutching}"
    e.replace(old_heading, new_heading, "D14", "maps:src:D.2.2; maps:src:D.2.3",
              "Give the whole finite-computation/Euler unit its actual mathematical title.")
    e.replace("The complete credited statement and re-derivation are in \\CompendiumRef{III}{maps:src:D.2.1}.\n", "",
              "D06", "maps:src:D.2.2",
              "The exact 21 configurations and coefficients are already supplied in the admitted KU receiver. Delete the unresolved external compendium pointer; the input data become the numbered definition in this unit.")
    e.replace("The exact remaining classification questions and all established subcases are in \\cref{maps:src:D.2.4}.\n", "",
              "D13", "maps:src:D.2.3",
              "Remove the orphan forward organization sentence; the exact open-result synthesis is owned by the paper's final section.")
    e.replace("\\begin{proposition}[Euler checks and parameter sensitivity]",
              "\\begin{proposition}[Euler numbers and integral clutching]",
              "D16", "maps:src:D.2.3",
              "Use a mathematical title naming the Euler formula and the integer gluing parameter established in the proof.")
    e.replace("these types. The fibre configuration and multiplicities alone do\nnot specify the input topology: integer clutching must also be kept.",
              "these types. There are two compact fibrations with the same local\nfibre models and multiplicities whose fundamental groups are respectively\nthe trivial group and \\(\\mathbb Z/11\\mathbb Z\\). Their gluing maps differ\nby an integral cusp translation.",
              "D02", "maps:src:D.2.3",
              "State the precise positive clutching example that the admitted proof already constructs. Its identity maps on all local models and explicit nonisomorphism of the two fundamental groups remain the reason for topological sensitivity.")
    e.replace("A rank-one wheel is the cyclic quotient of the ruled components\nby their paired, disjoint zero and infinity sections. Its open\ncomponent strata are",
              "The open component strata of a rank-one wheel are",
              "D13", "maps:src:D.2.3",
              "Move the wheel's defining cyclic gluing into the preceding numbered definition; the complete stratified Euler proof remains here.")
    e.replace("For parameter sensitivity, retain the standard finite data",
              "For the integral-clutching example, take the standard finite data",
              "D08", "maps:src:D.2.3",
              "Introduce the actual geometric example by its mathematical parameter choice, preserving the admissibility inequalities and their existing series reference.")
    e.replace("identified local fibre data. This proves the need to retain\nthe integer clutching.",
              "identified local fibre data. The integral clutching parameter is\ntherefore detected by the fundamental group.",
              "D08", "maps:src:D.2.3",
              "Conclude with the invariant that detects the explicit integer shear rather than an instruction to retain data.")
    proposition_start = e.text.index("\\begin{proposition}[Euler numbers and integral clutching]")
    proposition = e.text[proposition_start:].rstrip()+"\n"
    e.replace(e.text[proposition_start:], "", "D14", "maps:src:D.2.3",
              "Move the whole Euler/clutching proposition and its sole proof before the finite cohomology result, so the geometric meaning of Euler localization and integer clutching is available first.")
    wheel = r"""\begin{definition}[Rank-one wheel]
\hypertarget{tag-Q105}{}\label{mapsIII:def:rank-one-wheel}
{\normalfont\scriptsize tag Q105}\par
A rank-one wheel is the cyclic gluing of finitely many ruled surfaces
over elliptic curves, with each infinity section identified with the
next zero section by an isomorphism of those elliptic curves. The zero
and infinity sections in each ruled surface are disjoint. This includes
one ruled surface with its two sections identified. The images of the
paired sections are called seams.
\end{definition}

"""
    e.replace(new_heading+"\n", new_heading+"\n\n"+wheel+proposition+"\n",
              "D14", "maps:src:D.2.3; mapsIII:def:rank-one-wheel",
              "Place the complete proposition/proof first, preceded by the explicit cyclic wheel definition moved from its proof. It still covers the one-component case and free finite torus quotients.")

    input_start = e.text.index("Consider the integral-cohomology and fundamental-group outputs for the")
    input_end = e.text.index("\n\nThese choices give fifty inputs.", input_start)
    inputs = e.text[input_start:input_end]
    e.replace(inputs, "", "D13", "maps:src:D.2.2",
              "Move the full configuration table, n values, marked generator, simple-zero rule and additive choices into one numbered definition. No row, order, coefficient or choice is discarded.")
    inputs = inputs.replace(
        "Consider the integral-cohomology and fundamental-group outputs for the\nmarked local cochain models of",
        "The finite input family \\(\\mathcal I\\) uses the marked local cochain models of",
    )
    inputs = inputs.replace("marked Mordell--Weil generator G and the following\nconfigurations and integers n:",
                            "marked Mordell--Weil generator $G$ and the following\nconfigurations and integers $n$:")
    inputs = inputs.replace("where m is its minimal", "where $m$ is its minimal")
    definition = (
        "\\begin{definition}[Finite marked-model input family]\n"
        "\\hypertarget{tag-Q106}{}\\label{mapsIII:def:finite-filling-inputs}\n"
        "{\\normalfont\\scriptsize tag Q106}\\par\n"+inputs+
        "\nThe set \\(\\mathcal I\\) consists of all these marked choices.\n\\end{definition}\n\n"
    )
    e.replace("\\begin{computed}[Integral cohomology of a finite filling family]",
              definition+"\\begin{computed}[Integral cohomology of a finite filling family]",
              "D13", "mapsIII:def:finite-filling-inputs",
              "Define the exact marked local-model input family before its computed result, retaining its documented output scope and every configuration/parameter entry. G, n and m are typeset as mathematical variables.")
    e.replace("\\textnormal{\\small tag 02KU.}\n\n\nThese choices give fifty inputs.",
              "{\\normalfont\\scriptsize tag 02KU}\\par\n"
              "The family \\(\\mathcal I\\) of Definition~\\ref{mapsIII:def:finite-filling-inputs}\n"
              "has fifty inputs. Consider their integral-cohomology and\nfundamental-group outputs.",
              "D13", "maps:src:D.2.2",
              "Refer to the preceding numbered input definition while explicitly retaining the admitted computed-output scope. The existing tag is printed in the common small-tag style.")
    e.replace("For a configuration C, let", "For a configuration $C$, let", "D23", "maps:src:D.2.2",
              "Typeset the configuration variable consistently with the displayed set A(C).")
    e.replace("The degree-i output consists of", "The degree-$i$ output consists of", "D23", "maps:src:D.2.2",
              "Typeset the degree index as the mathematical variable used in the rank and invariant-factor formulas.")
    e.replace("The torsion lists in degrees i and", "The torsion lists in degrees $i$ and", "D23", "maps:src:D.2.2",
              "Use mathematical type for the index in the exact complementary torsion comparison.")
    issues=e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:rank-one-wheel", "mapsIII:def:finite-filling-inputs"), tags=("Q105", "Q106"))


if __name__ == "__main__":
    main()
