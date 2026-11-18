#!/usr/bin/env python3
"""Export only the audited P3K.28 include; never rewrite the master."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,re,shutil

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/"notes/part3_joint_additive_returns_working.md"
stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
shutil.copy2(source,ROOT/"records"/f"pre_export_{stamp}_{source.name}")
text=source.read_text()
text=text.replace(
    "Submitted for independent audit as P3K.28.",
    "Proved as P3K.28 after the parent's complete independent audit.")
source.write_text(text)
proof=text[text.index("## "):]

def pandoc(s):
    return subprocess.run(
        ["pandoc","-f","markdown+tex_math_single_backslash+raw_tex",
         "-t","latex","--wrap=preserve"],
        input=s,text=True,capture_output=True,check=True).stdout.strip()

def table(match):
    rows=[[s.strip() for s in line.strip("|").split("|")]
          for line in match.group(0).strip().splitlines()]
    rows=[r for r in rows if not all(re.fullmatch(r"[-: ]+",s) for s in r)]
    assert len(rows[0])==4
    out=[r"\par\medskip{\small\noindent",
         r"\begin{tabularx}{\linewidth}{@{}"
         r">{\hsize=.65\hsize\linewidth=\hsize}X"
         r">{\hsize=1.05\hsize\linewidth=\hsize}X"
         r">{\hsize=1.05\hsize\linewidth=\hsize}X"
         r">{\hsize=1.25\hsize\linewidth=\hsize}X@{}}",
         r"\toprule"]
    for i,row in enumerate(rows):
        out.append(" & ".join(pandoc(s) for s in row)+r" \\")
        if i==0:out.append(r"\midrule")
    out.extend([r"\bottomrule",r"\end{tabularx}",r"}\par\medskip"])
    return "\n".join(out)+"\n"

proof=re.sub(r"(?m)(?:^\|.*\n)+",table,proof)
proof=re.sub(r"(?m)^## (.+)$",
             lambda m:r"\par\medskip\noindent\textbf{"+m.group(1)+r"}\par\nobreak",proof)
proof=re.sub(r"(?<![A-Za-z])(?:code|notes|records)/[A-Za-z0-9_./-]+",
             lambda m:r"\path{"+m.group(0).rstrip(".")+"}"+
             ("." if m.group(0).endswith(".") else ""),proof)
tex=pandoc(proof)
assert r"\begin{verbatim}" not in tex
assert "\x0c" not in tex
statement=r"""
For the actual two-cap sphere families of P3F.38, P3F.46 and P3F.47,
retain their signed norms and write
\[
 D=m_0n_\infty+m_\infty n_0=\varepsilon\in\{1,-1\},
 \qquad M=m_\infty m_0,\qquad \lambda=r^M .
\]
One positive loop in the actual parameter \(r\) has the signed return
\[
 A^{\rm phys}
 =\frac{Ma^2}{2d}
       -\frac{M(12-e_\infty-e_0)+m_0e_\infty'+m_\infty e_0'}{12},
\]
where \(h(G)=1/d\), the marked line point is \(aG\), and
\(e_i,e_i'\) are the original and actual resolved-root Euler numbers.
The exact values in all nine nonempty sectors appear below and hold
for both determinant signs. The single quadratic \(I_1^*\) cap of
P3F.36, on either source profile and with \(\lambda=r^2\),
has \(A^{\rm phys}=2\) for both \(n=1\) and \(n=-1\).
By the actual dual-line and inverse-closing map P3K.68, the physical Hopf-gluing class is \(A^{\rm phys}\bmod28\), with
\(\mu=A^{\rm phys}/28\bmod\mathbb Z\).
"""
out=(r"\subsection{Actual joint additive pages and signed returns}"+"\n"+
     r"\begin{statement}{P3K.28}{Proved}"+"\n"+statement+
     "\n"+r"\end{statement}"+"\n"+r"\begin{proof}"+"\n"+
     tex+"\n"+r"\end{proof}"+"\n")
dest=ROOT/"notes/part3_joint_additive_returns.tex"
dest.write_text(out)
preamble=(ROOT/"S6_06_BLIND_paper.tex").read_text().split(r"\begin{document}")[0]
(ROOT/"records/part3_joint_additive_returns_compile.tex").write_text(
    preamble+"\n"+r"\begin{document}"+"\n"+
    r"\input{notes/part3_joint_additive_returns.tex}"+"\n"+
    r"\end{document}"+"\n")
print("Exported P3K.28 to",dest.relative_to(ROOT))
print("Prepared separate standalone wrapper; root master untouched.")
