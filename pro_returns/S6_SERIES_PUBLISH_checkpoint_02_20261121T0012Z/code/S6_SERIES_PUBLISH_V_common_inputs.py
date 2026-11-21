#!/usr/bin/env python3
from pathlib import Path
import re
from S6_SERIES_PUBLISH_editing import Editor, block, ROOT

e=Editor('V')
resolved=block(e.text,'maps:src:E.1.2')
step=re.search(r'\\item Take the fan over the periodic Kuhn tetrahedra\s*(.*?)\n\\item The map',resolved,re.S)
if not step: raise ValueError('shared cusp step')
shared=step[1]
fan=re.search(r'\\\[.*?\\label\{maps:eq:E\.4\}\s*\\\]',shared,re.S)[0]
action=re.search(r'\\\[\s*\(x,t_c\).*?\\label\{maps:eq:E\.5\}\s*\\\]',shared,re.S)[0]
action=action.replace('t_c','q').replace('C_3','C')
newresolved=resolved.replace(step[0],
 r'\item Apply \cref{night:P1.9} to the bounded holomorphic correction $C_3$ in \eqref{maps:eq:E.2}.'+'\n'
 r'The fan is \eqref{maps:eq:E.4}; its action is \eqref{maps:eq:E.5} with $(q,C)=(t_c,C_3)$.'+'\n'
 r'This identifies the quotient $N_3^C$ by the identity on its dense torus and gives a smooth proper filling.'+'\n\n'
 r'\item The map',1)
e.replace(resolved,newresolved,'D12','State and prove the shared marked Kuhn filling once, before both global constructions.','maps:src:E.1.2')
cusp=block(e.text,'night:P1.9')
newcusp=cusp.replace('\\begin{proof}',
 r'\begin{proof}'+'\n'
 r'The fan consists of the cones over the tetrahedra'+'\n'+fan+'\n'
 r'The period-lattice action is'+'\n'+action+'\n',1)
e.replace(cusp,newcusp,'D14','Move the defining fan and period action to their common local theorem; the specialization to the product is explicit.','night:P1.9')

memo=(ROOT/'agents/v_topology/S6_SERIES_PUBLISH_V_common_cusp_move.md').read_text()
lemma=re.search(r'```latex\n(.*?)\n```',memo,re.S)[1]
lemma=lemma.replace('\\begin{lemma}[Smooth dependence on the bounded cusp correction]',
 r'\begin{lemma}[Smooth dependence on the bounded cusp correction]'+'\n'
 r'\hypertarget{tag-PV01}{}\label{pub:V:cusp-smooth-dependence}'+'\n'
 r'\StatementRecord{pub:V:cusp-smooth-dependence}{proved}{PV01}{}',1)
lemma=lemma.replace('The toric charts have coordinates',
 r'For the linear deformation $C_t=tC$, \cite[Theorem~8.7, arXiv v1, pp.~57--58]{Yang2026} applies directly to $D(q,s)=sC(q)$ for $|s|<2$.'+'\n'
 r'For a smooth bounded family the same local charts give the following comparison. The toric charts have coordinates',1)
e.replace(newcusp,newcusp+'\n\n'+lemma,'D13','Give the already used parameter-flow comparison its own statement and complete proof.','pub:V:cusp-smooth-dependence')

old=r'''The proof of Theorem \SeriesRef{maps:src:E.1.2} used only boundedness of $C$,
integrality of the standard cusp, and unimodularity of that
fan.  It therefore proves smoothness, proper discontinuity
and properness for this model without a symmetry condition
on $C$.  Glue by the displayed integral marking and use no
additional cusp translation.'''
new=r'''The local filling theorem \cref{night:P1.9} applies to this bounded
holomorphic correction. It gives smoothness, proper discontinuity
and properness in the prescribed marking. We glue with zero cusp
translation.'''
e.replace(old,new,'D14','Use the local theorem directly, removing dependence on the later fibre-product construction.','maps:src:F.3.7')
old=r'''on the cusp use the stratum-preserving
parameter vector fields and uniform properness estimate of
Theorem \SeriesRef{maps:src:E.1.3}.'''
new=r'''on the cusp use the marked, stratum-preserving comparison of
\cref{pub:V:cusp-smooth-dependence}.'''
e.replace(old,new,'D14','Use the common smooth-dependence lemma in both global constructions.','maps:src:F.3.7')

collapse=block(e.text,'night:P1.11')
first=re.search(r'\\item We first remove the unit matrix.*?We may therefore calculate at \$C\(q\)=0\$\.',collapse,re.S)
if not first: raise ValueError('collapse deformation')
replacement=r'''\item Apply \cref{pub:V:cusp-smooth-dependence} to $C_t(q)=tC(q)$.
The comparison preserves the central strata, the integral marking,
and the real oriented logarithmic boundary; it therefore intertwines
the collapse maps. We calculate with $C(q)=0$.'''
e.replace(first[0],replacement,'D12','Use one proof of smooth dependence on the bounded cusp correction.','night:P1.11')
if 'The family is proper by \\cref{maps:src:F.3.7}.' in e.text:
 e.replace('The family is proper by \\cref{maps:src:F.3.7}.','The local family is proper by \\cref{night:P1.9}.','D14','Local properness is an earlier cusp input.','night:P1.11')
e.save()
