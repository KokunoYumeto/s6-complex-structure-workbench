"""Repair KT's signed increment sentence using the common literal convention."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_catalogue", "c8-III-foundations-catalogue-sign-")
    e.replace("The following tables specify the ordered elliptic matrices and\ngenerator cocycles. A row",
              "The following tables specify the ordered elliptic matrices and\nnegative Abel--Jacobi cocycles of $G$, in the convention of\nTheorem~\\ref{maps:src:D.2.12}. A row", "D20", "mapsIII:def:elliptic-marked-data",
              "State the already used negative-increment convention at the common data definition, so each later component calculation has one literal sign convention.")
    e.replace(r"""Let \(A_i\) be a local elliptic monodromy and \(g_i\) the
section cocycle of \(G\). Continuing an elliptic logarithm of
\(kG\) adds \(kg_i\); changing that logarithm by the integral
period \(v\) changes the increment by \((A_i-I)v\).
The component class is therefore
\[
 [kg_i]\in\mathbb Z^2/(A_i-I)\mathbb Z^2,
\]
with its inverse change obtained by subtracting \(v\).""", r"""Let \(A_i\) be a local elliptic monodromy and \(g_i\) the
negative Abel--Jacobi cocycle of \(G\). The negative increment
for \(kG\) is \(kg_i\); a change of logarithm branch contributes
the coboundary \((A_i-I)v\), with inverse contribution
\(-(A_i-I)v\). In this marking the component class is
\[
 [kg_i]\in\mathbb Z^2/(A_i-I)\mathbb Z^2.
\]
The map \([x]\mapsto[-x]\), whose inverse is itself, gives the
positive-increment marking. It fixes the zero class and preserves
the order of every component class.""", "D25", "maps:src:D.2.19",
              "The original sentence called kg_i the positive logarithmic increment, contrary to the same table's negative-Abel--Jacobi convention in KM/KY. State the signed increment, branch coboundary and exact self-inverse sign map. Narrowness, component orders, the full component-degree test, all 104/88/348 counts and the theorem conclusion are unchanged.")
    e.finish()


if __name__ == "__main__":
    main()
