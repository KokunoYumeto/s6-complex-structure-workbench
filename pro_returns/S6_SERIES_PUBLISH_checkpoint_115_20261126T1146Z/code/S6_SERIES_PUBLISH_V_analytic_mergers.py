#!/usr/bin/env python3
from pathlib import Path
import re
from S6_SERIES_PUBLISH_editing import Editor, block, ROOT

e=Editor('V'); folder=ROOT/'agents/v_analytic'; retained=[]
def draft(name):
    return '\n'.join(l for l in (folder/name).read_text().splitlines() if not l.startswith('%')).strip()

old_lift=block(e.text,'maps:src:F.3.6')
old_domain=block(e.text,'night:P1.8')
merged=draft('S6_SERIES_PUBLISH_V_period_merger.tex')
# Keep the real scalar distinct from the monodromy matrix A.
merged=merged.replace('$A=\\alpha(r)$','$a_r=\\alpha(r)$').replace('$n=r/A$','$n=r/a_r$')
merged=merged.replace('\n A=i\\operatorname{contr}', '\n a_r=i\\operatorname{contr}')
merged=merged.replace('$A=2|a_0|^2y+O(1)$','$a_r=2|a_0|^2y+O(1)$')
e.replace(old_lift,merged,'D12','Combine existence, the cusp asymptotic and the exact transversality criterion in one lifted-period theorem.','maps:src:F.3.6')
e.replace(old_domain,'','D12','Both permanent theorem targets now identify the single lifted-period statement and proof.','night:P1.8')
retained += [('maps:src:F.3.6 old proof',old_lift),('night:P1.8 old proof',old_domain)]

old_h=block(e.text,'def:hb')
h=draft('S6_SERIES_PUBLISH_V_hb_definition.tex')
h=h.replace('\\label{def:hb}',r'\hypertarget{tag-PV03}{}\label{def:hb}'+'\n'+r'\StatementRecord{def:hb}{proved}{PV03}{}',1)
h=h.replace('\\label{rem:V:splitting-change}',r'\hypertarget{tag-PV04}{}\label{rem:V:splitting-change}',1)
h=h.replace('$\\langle u,\\bar u\\rangle$',r'$\operatorname{span}_{\mathbb C}\{u,\bar u\}$')
h=h.replace(' h_b(\\lambda)=\\frac{96}{625\\pi}',r' h_b(\lambda)=\frac{96}{625\pi}',1)
e.replace(old_h,h,'D20','Define one height and one splitting, prove well-definedness and the exact scalar transport, and give the alternative splitting only by its exact affine parameter map.','def:hb')

old_min=block(e.text,'night:P1.18')
minimum=draft('S6_SERIES_PUBLISH_V_minimum_compact.tex')
minimum=minimum.replace('are those of \\cref{night:P1.8}.','are those of \\cref{def:hb}.')
e.replace(old_min,minimum,'D09','Keep the rational connection, enclosure method, closed cover and strict bounds; transfer software configuration and the second normalization to the checking records.','night:P1.18')
retained.append(('night:P1.18 full implementation and alternate normalization',old_min))

filling=block(e.text,'maps:src:F.3.7')
parameter=draft('S6_SERIES_PUBLISH_V_parameter_morphism.tex')
parameter=parameter.replace('\\label{rem:V:conjugation-parameter}',
 r'\hypertarget{tag-PV05}{}\label{rem:V:conjugation-parameter}',1)
e.replace(filling,filling+'\n\n'+parameter,'D20','State the exact parameter morphism under simultaneous base/fibre conjugation: xi maps to minus its conjugate.','rem:V:conjugation-parameter')

# Put the pencil's defining equation and Hodge-bundle formula at their unique
# geometric proof, and retain only the extra rational-monodromy comparison.
geometric=block(e.text,'maps:src:F.3.5')
curve=re.search(r'\\\[\s*C_\\lambda:.*?\\label\{maps:eq:F\.7\}\s*\\\]',geometric,re.S)[0]
hodge=re.search(r'\\\[\s*\\mathcal E=.*?\\label\{maps:eq:F\.8\}\s*\\\]',geometric,re.S)[0]
pencil=block(e.text,'night:P1.4')
old_statement=pencil[pencil.index('The genus-two pencil',pencil.index('\\StatementRecord')):pencil.index('\\end{theorem}')]
new_statement=(r'The smooth projective models of the pencil'+'\n'+curve+'\n'
 r'have one nodal fibre away from $0,\infty$, at $\lambda_*=-256/3125$.'+'\n'
 r'The minimal good root orders at $0,\infty$ are $8,5$.'+'\n'
 r'On the root curve with reduced root divisors $D_0=[0]/8$ and $D_\infty=[\infty]/5$, the Hodge bundle is'+'\n'+hodge+'\n'
 r'Thus $T=\mathcal T=\mathcal O((2/5)[\infty]-(3/8)[0])$, and $\ell_0=T^3$ is generated meromorphically by $dx/y$.'+'\n'
 r'The extension at $\lambda_*$ is the dualizing Hodge extension.'+'\n')
newpencil=pencil.replace(old_statement,new_statement,1)
e.replace(pencil,newpencil,'D12','Give the pencil, root orders and Hodge bundle once, at their local geometric proof.','night:P1.4')
gs=geometric.index('Put $\\lambda_*'); ge=geometric.index('\\end{theorem}')
gstatement=r'''For $U=\mathbb P^1\setminus\{0,\infty,\lambda_*\}$, let
$\mathcal H_{\rm dR}$ be the polarized rational cohomology system
of the pencil in \cref{night:P1.4}. Its primitive exterior square
is rationally isomorphic to the rank-five quotient of the system
with matrices $A,B$ in \cref{pub:V:rank-six-data} by its invariant
first-coordinate line. The identification uses the explicit
companion and quotient maps below and the stated based meridians.
'''
newg=geometric[:gs]+gstatement+geometric[ge:]
newg=newg.replace('[the geometric rank-five quotient]','[The rational rank-five monodromy]')
first=re.search(r'\\item The discriminant.*?\\item We identify the representation\.',newg,re.S)[0]
replacement=r'''\item By \cref{night:P1.4}, the cusp is an ordinary node with
genus-one normalization. Cutting and regluing an annular neighborhood
gives a Dehn twist in the primitive nonseparating vanishing circle.
Its logarithm $N_H$ has square zero and rank one.
The finite characteristic polynomials, from the same theorem, are
$f(T)=T^4+T^3+T^2+T+1$ at infinity and $g(T)=T^4+1$ at zero.

\item We identify the representation.'''
newg=newg.replace(first,replacement,1)
root_repeat=re.search(r'At zero their expressions in the root coordinates are.*?proving \\eqref\{maps:eq:F\.8\}\.',newg,re.S)[0]
newg=newg.replace(root_repeat,'The root-divisor calculation is \\eqref{maps:eq:F.8}.',1)
e.replace(geometric,newg,'D12','Keep the companion/rational identification and nodal logarithmic comparison; cite the unique pencil and Hodge-bundle computation.','maps:src:F.3.5')

# Establish P's holomorphic splitting before the algebraic connection and
# height. This removes all circular exposition in the normalized lift.
lift=block(e.text,'night:P1.8')
prefix=re.search(r'On the root curve of orders five and eight,.*?\\sigma_b\$ and its marked contraction from \\cref\{night:P1\.15\}\.',lift,re.S)
if not prefix: raise ValueError('lift bundle prefix')
bundle=prefix[0]
bundle=bundle.replace('The wedge map is injective after primitive projection, as proved\nin \\cref{night:P1.5}.',
 'Every nonzero vector in $\\ell\\wedge\\mathcal H_D$ is decomposable, whereas the polarization bivector has nonzero square. Thus primitive projection is injective there.')
bundle=bundle.replace(' We use the algebraic choice\n$\\sigma_b$ and its marked contraction from \\cref{night:P1.15}.','')
rankthree=block(e.text,'night:P1.5')
newrank=rankthree[:rankthree.index('\\end{theorem}')]+r'''Moreover
$P\cong\mathcal O\oplus T^2\oplus T^4$,
$H^1(P^\vee)=0$, and $H^0(P^\vee)$ is the one-dimensional
space of contractions. Its inclusion into the rank-five quotient
lifts holomorphically to the rank-six extension.
\end{theorem}
\begin{proof}
'''+bundle+'\n'+r'\end{proof}'
e.replace(rankthree,'','D14','Move the bundle-splitting result after the rational and integral monodromy identifications.','night:P1.5')
anchor='\\subsection{The algebraic connection and its splitting}'
e.replace(anchor,newrank+'\n\n'+anchor,'D12','One wedge-bundle proof now includes the root-line calculation and holomorphic splitting used by the normalized connection.','night:P1.5')
e.replace(prefix[0],r'The holomorphic splitting and the one-dimensional space of its changes are given by \cref{night:P1.5}. We use the algebraic choice $\sigma_b$ of \cref{night:P1.15}.',
 'D12','Cite the preceding bundle proof in the lifted-period theorem.','night:P1.8')

connection=block(e.text,'night:P1.15')
connection_new=connection.replace(
 'All $H^1(L^j)$ for $j=0,\\pm1,\\pm2$ vanish by the coarse-degree\ncalculation already used in \\cref{night:P1.8}.',
 r'''For the coarse projection $\rho$ on the effective root curve,
\[
 \rho_*L^j=\mathcal O_{\mathbb P^1}
 \left(\left\lfloor\frac{4j}{5}\right\rfloor+
       \left\lfloor-\frac{3j}{4}\right\rfloor\right).
\]
The degree is zero for $j=0$ and minus one for $j=\pm1,\pm2$.
Finite stabilizer invariants are exact, so all five $H^1(L^j)$ vanish.''')
connection_new=connection_new.replace('The exact cusp identity of \\cref{night:P1.8} characterizes the contraction on this\nline by',
 'We fix the contraction on this kernel line by the exact companion identity')
e.replace(connection,connection_new,'D20','Give the root-line computation and cusp scalar at the point where the algebraic splitting is fixed.','night:P1.15')

e.save()
with (ROOT/'records/S6_SERIES_PUBLISH_V_removed_independent_proofs.tex').open('a') as f:
 for label,text in retained: f.write('\n% Retained as checking evidence: '+label+'\n'+text+'\n')
