"""Transport the older meridian-one calculations by the explicit U=M^{-1} map."""
def type_k8(t):
 marker=r'\begin{enumerate}[label=\arabic*.]'
 t=t.replace(marker,marker+r'''
\item Write \(U=M^{-1}\) for the meridian-one line carried by the
real trace of \cref{night:P3K.7}. The actual Hermitian coefficient map
\[
 D_M(v)(w)=\frac{\langle v,w\rangle}{\langle v,v\rangle},
 \qquad D_M(e^{i\theta}v)=e^{-i\theta}D_M(v)
\]
of \cref{night:P3K.68} extends by dualizing the line on the whole
trace. Thus \(x=c_1(U)\), and the determinant restricts on the
page to \(b=-2c_1(M)\). The index calculated below is \(A_U\);
the physical comparison is \(A_M=-A_U\).''',1)
 t=t.replace('-K_S+2c_1(M)', '-K_S-2c_1(M)')
 t=t.replace('M+nF','M^{-1}+nF')
 t=t.replace(r' A=\operatorname{ind}',r' A_U=\operatorname{ind}')
 t=t.replace(r' A=\operatorname{ind}',r' A_U=\operatorname{ind}')
 t=t.replace(r'\par\medskip\noindent\textbf{Acyclicity from explicit sections.}\enspace',
 r'''\par\medskip\noindent\textbf{Acyclicity from explicit sections.}\enspace
The actual twist is the dual Picard line \(M^{-1}\), corresponding
to the section \(-P_*\). Fibre inversion is the exact map carrying
the two choices \(P_*\) and \(-P_*\); the calculation below retains
both and proves their nonidentity specializations.''')
 t=t.replace(r'\end{enumerate}',r'''\item The extending duality map gives
\(A_M=-A_U=0\) for this same actual return. No change of cap,
parameter direction or boundary gauge has been made in obtaining
the physical zero.
\end{enumerate}''',1)
 return t
change('night:P3K.8',type_k8,
 'Correct the spin-c base twist from M+nF to M^{-1}+nF using the exact extending Hermitian duality map U=M^{-1}; retain the explicit P and -P fibre inversion and both zero indices.')

def type_k9(t):
 t=t.replace(r'''return has Jin characteristic numbers \((k,\ell)=(-6,-24)\).''',
 r'''return has meridian-line Jin numbers
\((k_U,\ell_U)=(-6,-24)\) and physical-line numbers
\((k_M,\ell_M)=(6,24)\), where \(U=M^{-1}\).''')
 t=t.replace(r''' k=-1,\qquad \ell=-4.''',
 r''' (k_U,\ell_U)=(-1,-4),\qquad (k_M,\ell_M)=(1,4).''',1)
 marker=r'\begin{enumerate}[label=\arabic*.]'
 t=t.replace(marker,marker+r'''
\item In the normal-frame calculation below \(k,\ell\) denote the
\(U\)-line numbers. Dualize the actual extending line on the same
oriented Jin completion using \(D_M\) from \cref{night:P3K.68}.
It replaces \(c_1(U)\) by \(c_1(M)=-c_1(U)\) and leaves the tangent
bundle and the full normal-frame clutch fixed. Consequently
\[
 (k_M,\ell_M)=(-k_U,-\ell_U),\qquad A_M=-A_U.
\]
For the same gauge degree \(n\), a change
\((k_U,\ell_U)\mapsto(k_U+n,\ell_U+4n)\) becomes
\((k_M,\ell_M)\mapsto(k_M-n,\ell_M-4n)\).
As \(n\) ranges over \(\mathbb Z\), these are precisely the
framing changes stated above.''',1)
 t=t.replace(r'\end{enumerate}',r'''\item Applying that actual duality to the computed sixfold
pair gives \((6,24)\), and to its descended pair gives \((1,4)\).
Both conventions have index zero, with their stated physical
circle and the same descended rotating frame.
\end{enumerate}''',1)
 return t
change('night:P3K.9',type_k9,
 'Retain (-6,-24) and (-1,-4) as U-line values and prove the physical M-line pairs (6,24) and (1,4) by dualizing the same extending line; transport the precise gauge degree and all framing descent maps.')

def type_k11(t):
 t=t.replace(r'''                  (k,\ell)=(-KL,-4KL).''',
 r''' (k_U,\ell_U)=(-KL,-4KL),\qquad
 (k_M,\ell_M)=(KL,4KL).''',1)
 marker=r'\begin{enumerate}[label=\arabic*.]'
 t=t.replace(marker,marker+r'''
\item Retain the two explicitly related lines \(U=M^{-1}\) and
\(M\). The symbols \(k,\ell\) in the detailed cochain and framing
calculation below denote the meridian-line values \(k_U,\ell_U\).
The extending duality map of \cref{night:P3K.68,night:P3K.9}
gives \((k_M,\ell_M)=(-k_U,-\ell_U)\) on the same oriented
completion. The source-parameter shear and all logarithmic
characteristic classes below are unchanged by this coefficient
duality.''',1)
 t=t.replace(r'\end{enumerate}',r'''\item The final duality therefore gives the physical pair
\((KL,4KL)\) in the stated positive-gamma marking.
For either sphere sign the physical index is
\(A_M=-A_U=0\), using the actual inverse loop for the negative
sign, as constructed above.
\end{enumerate}''',1)
 return t
change('night:P3K.11',type_k11,
 'Transport the higher-order rotating-frame pair by the same actual extending-line duality: retain the original U pair and display the physical M pair (KL,4KL), without changing the proven period, covering degree or zero index.')

change('night:P3F.8',lambda t:t.replace(
 r'''P3K.9 evaluates its characteristic pair as\(-6,-24\), including the normal-frame comparison, and descends it to\(-1,-4\) for one parameter loop.''',
 r'''\cref{night:P3K.9} evaluates the meridian-line pair as
\((-6,-24)\), with descended pair \((-1,-4)\). The explicit
extending duality \(U=M^{-1}\) gives the physical pairs
\((6,24)\) and \((1,4)\), respectively, with that same
normal-frame comparison.'''),
 'Type the downstream K9 pair in the actual orbit-return comparison and carry both signs by the exact line duality.')
change('night:P3F.4',lambda t:t.replace(
 'P3K.6--9 derive the characteristic numbers from its charts and its specified descended rotating framing.',
 r'''\cref{night:P3K.6,night:P3K.7,night:P3K.9} derives these
numbers for the meridian line \(U\) with its specified descended
rotating frame. The actual dual line \(M\) has pair \((1,4)\);
both pairs lie in the same explicitly extending primitive-sphere
twist subgroup.'''),
 'Retain the valid numerical Hopf-lift example while explicitly typing its U line and the dual physical M example.')
change('night:P3F.14',lambda t:t.replace(
 'Write a=c1\\(L_+\\), b=c1\\(L_-\\), d=c1\\(TS\\).',
 r'''Write \(a=c_1(L_+)\), \(b=c_1(L_-)\), and \(d=c_1(TS)\).
Use the meridian-one hyperplane line \(U\) on the displayed Hopf
quotient, so \(x=c_1(U)\). The actual physical-line application
is transported through \(U=M^{-1}\) by \cref{night:P3K.68};
the zero calculation below is preserved by that explicit map.'''),
 'Type the Hopf-boundary Euler class as the meridian-one hyperplane line before applying the spin-c polynomial.')

def smoothing_map_k1(t):
 old='The smoothing is\n'+r'\(S^3\times D^3\), whose second integral cohomology vanishes.'
 new=r'''For the smoothing \(uv-Xw=1\), the explicit linear coordinates
\[
 z_1=(u+v)/2,\quad z_2=(u-v)/(2i),\quad
 z_3=(X+w)/(2i),\quad z_4=(X-w)/2
\]
give \(\sum z_j^2=1\). Write \(z=p+iq\) with real \(p,q\).
Then \(|p|^2-|q|^2=1\) and \(p\cdot q=0\), so the maps
\[
 (a,b)\longmapsto\sqrt{1+|b|^2}\,a+ib,\qquad
 z\longmapsto (p/|p|,q)
\]
are inverse between \(TS^3\) and the affine smoothing.
A radial compact cut is the disc bundle of \(TS^3\).
For a unit quaternion \(a\), writing \(b=a\,\xi\) with
\(\xi\in\operatorname{Im}\mathbb H\) gives its literal
trivialization \(S^3\times D^3\). Hence its second integral
cohomology vanishes.'''
 assert old in t
 return t.replace(old,new)
change('night:P3K.1',smoothing_map_k1,
 'Supply the explicit linear quadric map, tangent-bundle parametrization and quaternionic trivialization of the smoothing used in the line-extension obstruction.')

change('night:P3F.10',lambda t:t.replace(
 r'H\textsuperscript{2}(C°,j\_\emph{Lambda\_E).',
 r'\(H^2(C^\circ,j_*\Lambda_E)\).').replace(
 r'j\_}Lambda\_E',r'\(j_*\Lambda_E\)'),
 'Repair the damaged Markdown star in the invariant-lattice extension notation, preserving the full integral obstruction argument.')
change('night:P3F.12',lambda t:t.replace(
 r'y\textsuperscript{12=t}4/\(t-1\)\^{}3',
 r'\(y^{12}=t^4/(t-1)^3\)').replace(
 r'j\_\emph{Lambda\_E gives H\textsuperscript{2}(C,j\_}Lambda\_E)=0',
 r'\(j_*\Lambda_E\) gives \(H^2(C,j_*\Lambda_E)=0\)'),
 'Repair the literal component-cover equation and invariant-lattice extension typography without changing their maps.')
change('night:P3F.17',lambda t:t.replace(
 'The fully signed higher-parameter comparison is developed in P3K.11 and is under audit at this checkpoint.',
 r'The full signed parameter and framing comparison is the explicit construction of \cref{night:P3K.11}; its U and M characteristic pairs are related there by the extending line duality.'),
 'Replace the obsolete intermediate audit notice by the complete typed higher-parameter comparison.')

def type_f21(t):
 old=r'''The actual signed comparison is proved in P3F.25 by the real trace P3K.6--7: the return invariant is the negative of this displayed page expression, so \(A=-4\), with oriented class \(24\) in \(\Theta_7\).'''
 assert old in t
 t=t.replace(old,r'''The real trace gives the meridian-line value \(A_U=-4\). The actual extending duality \(U=M^{-1}\), with the cap and inverse-clutch maps of \cref{night:P3K.68}, gives \(A_M=-A_U=4\), and hence the physical oriented class \(4\) in \(\Theta_7\). Both line conventions are retained in \cref{night:P3F.25}.''',1)
 old=r'''Consequently this page expression gives the signed return integer A=-4, and P3F.22 gives its oriented class24 modulo28.'''
 assert old in t
 t=t.replace(old,r'''Consequently this page expression gives \(A_U=-4\) for the meridian-one line. Dualizing that extending line on the same oriented completion gives \(A_M=4\); the explicit cap exchange and inverse-clutch map of \cref{night:P3K.68} give its physical oriented class \(4\pmod{28}\).''',1)
 return t
change('night:P3F.21',type_f21,
 'Type two stale OS47 sign conclusions in this historically Proved source block: retain U-index -4 and transport by the actual extending duality to physical M-index +4 and oriented class4. This editorial repair does not itself assign whole-proof credit.')

def repair_k80_f0(t):
 old=r'\cref{night:P3F.0}'
 assert t.count(old)==1
 return t.replace(old,r'the complete annular map \(F_0\) in \cref{night:P3K.49}, RCZ.5--7',1)
change('night:P3K.80',repair_k80_f0,
 'The source CSV depends_on field contains nonexistent P3F.0; no such statement is in the source. K80 explicitly identifies its actual F_0 as the complete annular map of RCZ.5–7 in K49, whose source and target, fixed reference and chain maps are printed there. Replace the phantom statement reference by that exact local construction; no alias or proof-check credit is invented.')
