"""Exact receiving-text edits following the recorded current proof reviews."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[2]
s=(P/'papers/IV/body.tex').read_text()
def block(label):
 a=s.index(r'\label{'+label+'}');b=s.index(r'\end{proof}',a)+len(r'\end{proof}');return s[a:b]
def proof(label):
 b=block(label);return b[b.index(r'\begin{proof}'):]
r={}
def add(label,old,new):
 assert old in block(label),(label,old[:100]);r.setdefault(label,[]).append({'old':old,'new':new})
add('push:src:C.3.6',proof('push:src:C.3.6'),r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item Put $h=h_2^{-1}h_1$ for the two equivariant lifts. The orbit-preserving theorem of Haefliger--Salem gives a smooth invariant map $g:X\to S^1$ with $h(x)=g(x)\cdot x$; see \citet[Theorem~3.1, original statement reproduced on PDF p.~6]{HaefligerSalem1991D,KarshonOrbitSlidesD} and the corrected torus formulation on PDF p.~2 of the latter source. Its equivariance hypothesis is satisfied by $h$. The original non-equivariant auxiliary Lemma~3.2 requires the correction recorded there: on $\mathbb C\setminus\{0\}$, complex conjugation has quotient $\bar z/z=e^{-2i\arg z}$, whose two limits along arguments $0$ and $\pi/2$ are $1$ and $-1$. This auxiliary counterexample and its correction are credited to that source.
\item The covering map $a\mapsto e^{2\pi ia}$ lifts $g$ to a smooth real function $a$ because $X$ is simply connected. The integer $a(\lambda x)-a(x)$ depends continuously on $\lambda\in S^1$ and vanishes at $\lambda=1$, so $a$ is invariant. Hence $h_s(x)=e^{2\pi isa(x)}\cdot x$ has inverse $h_{-s}$, and $h_2h_s$ is the required smooth equivariant isotopy between the two lifts.
\item On the free stratum the quotient is a principal circle bundle. Choose a connection and horizontally lift the compactly supported time-dependent vector field of the given orbit isotopy. Its invariant flow exists for the full compact time interval and extends by the identity near the fixed set. The two preceding steps compare its endpoint with every other equivariant lift of the same orbit map. This proves the stated independence of the resulting smooth isotopy class.
\end{enumerate}
\end{proof}''')
# The known retraction proof remains in the unchanged compendium.
add('push:src:C.3.8','The complete retraction argument below is retained.','The receiving argument records the quotient homotopy and the induced primitive class; the general retraction proof remains in the unchanged compendium.')
add('push:src:C.3.8',proof('push:src:C.3.8'),r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item By \citet[Proposition~7.2, p.~41; final proof on p.~50]{AC26}, the sufficiently small closed cusp body has a torus-equivariant strong deformation retraction $R_s:V\to V$ onto $W$. Restricting the acting torus to the specified scalar circle $\rho$ preserves the equivariance identity $R_s(\rho(\lambda)x)=\rho(\lambda)R_s(x)$.
\item Define $\overline R_s:V/\rho\to V/\rho$ by $\overline R_s([x])=[R_s(x)]$. The displayed identity makes this map well defined. Its continuity follows from the quotient map $V\times[0,1]\to(V/\rho)\times[0,1]$, which is closed since $V$ and the acting circle are compact. The maps start with the identity, end in $H=W/\rho$, and fix $H$ throughout. Thus they form the asserted strong deformation retraction.
\item Inclusion $H\hookrightarrow V/\rho$ consequently induces an integral homology isomorphism. It sends the fixed sphere to the same embedded sphere. By \cref{push:src:C.3.7} its class in $H_2(H;\mathbb Z)$ is primitive and nonzero, and these properties pass through that isomorphism. The boundary of any singular three-chain represents zero in homology. Therefore $F$ cannot be such a boundary in $V/\rho$, including the boundary of an embedded three-ball.
\end{enumerate}
\end{proof}''')
add('maps:src:B.6.18','The integer $B_0$ has not yet been evaluated for the given family,\nand this statement does not identify its reverse-surgery image\nin $\Theta_7$.',r'''For the retained reference fan, \cref{maps:src:B.6.20} computes $k=-1$; hence $B_0=0$ and $[\overline\Psi]=a^{-1}$. The reverse-surgery image is computed by the actual trace in \cref{maps:src:B.6.19}.''')
add('maps:src:B.6.18',r'This last arithmetic is checked in',r'The value $k=-1$ from \cref{maps:src:B.6.20} now gives $B_0=0$ in the displayed formula. This last arithmetic is also checked in')
add('maps:src:B.6.19','boundary $M_s\\sqcup(-M_\\Phi)$.  It is spin.  If $k\\ne0$,','boundary $M_s\\sqcup(-M_\\Phi)$. It is spin. Its cup coefficient is $k=-1$ by \\cref{maps:src:B.6.20}; for this nonzero coefficient,')
add('maps:src:B.6.19','In particular, if the actual integer $k$ is $-1$, then','For the computed value $k=-1$,')
add('maps:src:B.6.19','The last conclusion is conditional here on that still required\ninteger calculation; it does not follow from $\\ell=-4$ alone.','The signed cup calculation of \\cref{maps:src:B.6.20} and the oriented value $\\ell=-4$ enter the trace calculation below together.')
add('maps:src:B.6.19','In particular, when $k=-1$ its matrix is','For the computed value $k=-1$ its matrix is')
add('maps:src:B.6.19','the conditional conclusion \\eqref{maps:eq:B.6.34}.','the asserted conclusion \\eqref{maps:eq:B.6.34}.')
add('maps:src:B.6.20','Consequently the spin-trace calculation of \\ref{maps:src:B.6.19} gives the zero class\nin $\\Theta_7$ for the original minimal-family monodromy.','')
add('maps:src:B.6.20',r'''The exact normal-torus
Mayer--Vietoris calculation in \texttt{manifolds\_mapping\_quotient.py} gives
$H_2(Q)=\mathbb Z$, and the regular $gk$-torus maps to twice its generator.
The primitive degree-two class $x$ therefore has fibre restriction
$E_0=2G\wedge K$ after choosing the sign of $x$.''',r'''The Wang and surgery calculation of \cref{maps:src:B.6.17} gives $H^2(Q;\mathbb Z)=\mathbb Z$, with primitive generator the Euler class $x$ of the actual free circle bundle. Its restriction to a regular fibre is read directly from the lifted parameter closing in \cref{maps:src:B.6.16}: $S=I-2d\otimes g^*$. Quotienting by the $d$ circle leaves the regular $gk$-torus, and its lift changes the $d$ coordinate by $-2g$ at the parameter seam. Its circle clutching function therefore has degree $-2$ on the $g$ circle. The connection obtained by interpolating this clutch has curvature $\pm2G\wedge K$, with the common sign fixed by the chosen Euler convention. Choose the sign of $x$ so that its restriction is $E_0=2G\wedge K$. In particular this restriction is nonzero, so the restriction homomorphism on the one-dimensional space $H^2(Q;\mathbb Q)$ is injective. The companion normal-torus Mayer--Vietoris program verifies the same integer calculation; it supplies no additional proof premise.''')
add('maps:src:B.6.20','The integral normal-torus calculation gives the following representative\nof $x$ on the exterior:','The actual lifted circle monodromies give the following representative\nof $x$ on the exterior, through the explicit coboundary identity displayed below:')
add('maps:src:B.6.20','The conclusion about\n$\\Theta_7$ is now \\ref{maps:src:B.6.19}.','This completes the signed cup calculation.')
(P/'analysis/IV/root_replacements.json').write_text(json.dumps(r,indent=2))
print({k:len(v) for k,v in r.items()})
