"""Edit the wholly read KM unit; each source change is a defect row."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_poincare", "c8-III-foundations-KM-")
    label = "maps:src:D.2.12"
    old_header = r"\begin{theorem}[seven further unbounded one-log families]\hypertarget{tag-02KM}{}\label{maps:src:D.2.12}"
    data_start = "Let $G$ be the marked Mordell--Weil generator"
    data_end = "\\end{array}\\qquad (\\text{entry }i=\\ell_i).\n\\]"
    start = e.text.index(data_start)
    end = e.text.index(data_end, start) + len(data_end)
    data = e.text[start:end]
    definition = (r"\subsection{Seven elliptic profiles with unbounded logarithmic multiplicity}" + "\n\n"
                  + r"\begin{definition}[Seven marked elliptic profiles]" + "\n"
                  + r"\hypertarget{tag-Q115}{}\label{mapsIII:def:seven-log-profiles}" + "\n"
                  + r"{\normalfont\scriptsize tag Q115}\par" + "\n" + data + "\n"
                  + r"\end{definition}" + "\n\n"
                  + r"\begin{theorem}[Seven families with unbounded logarithmic multiplicity]\hypertarget{tag-02KM}{}\label{maps:src:D.2.12}")
    e.replace(data, r"For each profile of Definition~\ref{mapsIII:def:seven-log-profiles}, put",
              "D13", label,
              "Move the complete ordered surface, P/Q, zero-fibre and additive-vector data into one numbered definition before use; preserve every table entry and parameter marking.")
    e.replace(old_header, definition, "D14", label,
              "Give the complete seven-family construction its own mathematical subsection and place the full numbered marked datum before its theorem.")
    e.replace("For each profile of Definition~\\ref{mapsIII:def:seven-log-profiles}, put\nPut\n",
              "For each profile of Definition~\\ref{mapsIII:def:seven-log-profiles}, put\n",
              "D23", label, "Join the theorem directly to the relocated definition without a duplicate introductory verb.")
    old = r"""Use the projective period matrices
\[
A=\begin{pmatrix}0&1\\-1&1\end{pmatrix},\quad
B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Their actions are $A(\tau)=1/(1-\tau)$ and $B(\tau)=-1/\tau$.
At $\rho=e^{\pi i/3}$ and $i$ their derivatives are respectively
$e^{2\pi i/3}$ and $-1$, fixing the positive local orientations.
The cusp matrix $-(AB)^{-1}=\left(\begin{smallmatrix}1&0\\-1&1\end{smallmatrix}\right)$
is a positive primitive Picard--Lefschetz matrix. Local oriented
periods identify the projective elliptic local system with the
pullback of this system by $J$."""
    new = r"""Use the positively oriented projective period matrices $A,B$ of
Remark~\ref{mapsIII:rem:positive-projective-periods}. Its period
isomorphism and inverse identify the projective elliptic local system
with the pullback by $J$, with the finite and cusp orientations fixed
there."""
    e.replace(old, new, "D12", label,
              "The exact shared period prerequisite has one owner in Q102 before OG. Replace the identical KM derivation by its numbered reference; retain the same A,B and positive peripheral convention used by the ribbon calculation.")
    changes = [
        ("We first give actual elliptic surfaces and the maps identifying their\nmarked integral local systems. Use the equation",
         "The marked elliptic surfaces have Weierstrass equations", "D08",
         "Replace an announcement of forthcoming work by the concrete equation that supplies the seven geometric inputs."),
        ("Here are the integral markings of these actual models. At $j=1/2$",
         "For the integral markings, at $j=1/2$", "D08",
         "State the root-labelling construction directly; keep all paths, sheet permutations and inverse maps."),
        (r"\emph{Identifying the actual section cocycle.}",
         r"\emph{The section cocycle and the normalized Poincar\'e line.}", "D16",
         "Name the mathematical content of this proof phase, including the line normalization that fixes the cocycle height."),
        ("its third is the supplied local generator $g$", "its third is the local generator $g$", "D08",
         "The printed integral matrix defines the generator; no supplied-data workflow qualifier is needed."),
        ("We prove that the actual Mordell--Weil generator has $k=\\pm1$.\n\nWe now give the actual divisor-line isomorphism to the circle\nmodel. For $\\operatorname{Im}\\tau>0$ define",
         "The divisor-line isomorphism to the circle model determines the\nMordell--Weil generator's coordinate $k$. For $\\operatorname{Im}\\tau>0$ define", "D08",
         "Give the purpose of the theta construction without two announcements; preserve the complete degree and height proof of k=±1."),
        ("Thus the degree of the pulled-back Poincare line is $-\\mathcal B$.",
         "Thus the degree of the pulled-back Poincar\\'e line is $-\\mathcal B$.", "D23",
         "Restore the mathematical name's accent in the clutching-degree calculation."),
        ("marking. This completes the geometric and section realization.\n", "marking.\n", "D11",
         "Remove the closing recapitulation after the explicit geometric and section maps have established the result."),
        ("This marking follows directly from the Poincare line bundle.",
         "This marking follows from the Poincar\\'e line bundle.", "D23",
         "Restore the accent and state the specific line-bundle derivation directly."),
        ("\\ref{maps:src:D.2.6}, equivalently", "Theorem~\\ref{maps:src:D.2.6}, equivalently", "D04",
         "Print the kind of the numbered primitive toroidal-filling prerequisite rather than a bare reference number."),
        ("The universal coefficient theorem and Poincare--Lefschetz\n", "The universal coefficient theorem and Poincar\\'e--Lefschetz\n", "D23",
         "Restore the accented duality name at its actual use."),
        ("These are integral maps on the indicated lattices.\n", "\n", "D11",
         "Remove the redundant sentence after the explicit integer right inverse and quotient section."),
    ]
    for old, new, kind, reason in changes:
        e.replace(old, new, kind, label, reason)
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:seven-log-profiles",), tags=("Q115",))


if __name__ == "__main__":
    main()
