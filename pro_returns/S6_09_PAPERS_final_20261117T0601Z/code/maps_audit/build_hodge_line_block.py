"""Transfer the full Hodge-line prerequisite, keeping source concordance."""
from pathlib import Path
import re,json,hashlib
R=Path('/workspace/scratch/037cd144174c');O=R/'deliverables/work/maps_audit'
p=R/'sources/workbench/analytic_picard.tex';t=p.read_text()
start=t.index(r'\begin{lemma}[determinant characters and the Hodge line]')
end=t.index(r'\end{proof}',start)+len(r'\end{proof}')
s=t[start:end].replace(r'\Verified','')
s=s.replace('Equation (2.3d) in', 'The period equivariance in')
s=s.replace(r'\label{lem:hodge-line-audit}',r'\label{mapsI:hodge:line}')
s=re.sub(r'\\(cref|ref|eqref)\{([^}]+)\}',lambda m:'\\'+m[1]+'{'+','.join('wb:'+x.strip() for x in m[2].split(','))+'}',s)
old='''The weights \\(8,3,12\\) give the same automorphy factor as \\(e\\);
the sign at \\(z_2\\) is fixed by its linearizing coordinate.'''
new=r'''The classical modular weights are $4,6,12$
\cite[Chapter~VII, Theorems~3--4 and Proposition~8]{Serre1973}.
Thus the squares of the automorphy factors of $\Theta$ and $e$ agree.
Their quotient is a constant sign for each generator. At $z_1$, the
zero of $\Theta$ has order two, so its factor has limiting value
$\zeta_1^2=-1/\rho=\det R_{g_1}(z_1)$. At $z_2$, its zero has order
one, so that limit is $\zeta_2=-i=1/i=\det R_{g_2}(z_2)$.
These limits fix both signs. At the cusp the normalized Fourier
expansions give a single-valued square root with nonzero constant
term, hence factor one under $\tau\mapsto\tau-1$.
Consequently $\Theta$ has exactly the automorphy factor of $e$.'''
assert old in s;s=s.replace(old,new)
tags=re.findall(r'\\tag\{([^}]+)\}',s)
for tag in tags:
 s=s.replace(r'\tag{'+tag+'}',r'\tag{HL.'+tag+'}').replace('('+tag+')','(HL.'+tag+')')
intro=r'''\subsection{The relative Hodge line}
Put $e=d\zeta_1\wedge d\zeta_2$ on the marked torus family.
Retain the negative-phase coordinates $s_j\circ g_j=\zeta_js_j$,
with $(m_1,m_2)=(3,4)$, $\zeta_j=e^{-2\pi i/m_j}$,
$t_j=s_j^{m_j}$, and $f^{-1}(p_j)=m_jS_j$.
'''
out=O/'paperI_hodge_line.tex';out.write_text(intro+s+'\n')
record={'source_file':str(p.relative_to(R)),'source_label':'lem:hodge-line-audit',
 'source_start_line':t.count('\n',0,start)+1,'source_end_line':t.count('\n',0,end)+1,
 'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'output_file':str(out.relative_to(R)),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'printed_label':'mapsI:hodge:line','alias':'wb:lem:hodge-line-audit',
 'paper':'I','kind':'Lemma; working-edition rederivation',
 'proof_preservation':'Full source statement and full proof transferred. Automorphy sign step expanded; source tags prefixed HL; raw geometry number replaced by internal label.',
 'external_labels':sorted(set(re.findall(r'wb:[^}]+',s))),
 'check':{'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
 'scope':'Full proof read and rederived: determinant matrices, finite unit gauge, invariant module, etale divisor pullback, cusp volume form, modular root and both elliptic signs. Serre exact modular statements opened and matched.',
 'limits':'Uses the actual period-equivariance, free finite fillings and unimodular cusp charts already proved in Paper I. No independent recertification of those entire constructions is asserted.'}}
(O/'paperI_hodge_line_manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['source_start_line','source_end_line','printed_label','external_labels']},indent=2))
