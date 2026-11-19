from pathlib import Path
import re
import subprocess

root=Path(__file__).resolve().parents[2]
md=(root/'notes/part4_a3_delta4_working.md').read_text()
body=md[md.index('Use the notation'):md.index('The original audit draft')]
tex=subprocess.run(
    ['pandoc','-f','markdown+tex_math_single_backslash-raw_tex',
     '-t','latex','--wrap=none'],
    input=body,text=True,capture_output=True,check=True).stdout
tex=re.sub(r'\\(?:subsection|subsubsection|paragraph)\{([^}]+)\}',
           lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par',
           tex)
header=r"""\subsection{The nonordinary three-branch tacnode sector}

\begin{statement}{P4R.17}{Proved}
In the remaining positive ruled case with uniform generic transverse
type $A_3$, every nonordinary three-branch critical-curve point has
local conductor defect strictly greater than nine. In particular,
the delta-four nonplanar cases have the explicit lower bounds
$13$, $21/2$, $11$, and $23/2$ below. The only three-branch germ
compatible with the total defect budget nine is the ordinary
nonplanar union of three coordinate axes.
\end{statement}
\begin{proof}
"""
footer=r"""
\end{proof}

The analytic model identities, primitive conormal lattices,
Hilbert--Burch minors, cubic obstruction, and jet generators are
checked exactly in \path{code/part4/a3_delta4.py}.
"""
(root/'notes/part4_a3_nonordinary.tex').write_text(header+tex+footer)
print(root/'notes/part4_a3_nonordinary.tex')
