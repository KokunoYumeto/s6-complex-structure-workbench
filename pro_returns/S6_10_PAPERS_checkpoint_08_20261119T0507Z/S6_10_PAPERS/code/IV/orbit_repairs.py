"""Exact suspension-roof and orientation repair after the current orbit audit."""
def repair_k13(t):
 a=t.index('In a retained nonzero-linearization')
 b=t.index(r'\end{theorem}',a)
 t=t[:a]+r'''In a retained nonzero-linearization \(I_n\) neighbourhood, the
positive log-height action and the contracting log-norm action have
the explicit mapping-torus identifications below. Their interval
reversal transports the full source map and orientation. The
component-orbit cycles have intersection matrix \(hB_g\), where
\(g=\gcd(n,c)\), \(h=n/g\), and \(c\) is the actual
translation on component labels. For the retained neighbourhoods
of a semifree sphere member with the single standard fixed
\(\mathbb P^1\), the global orbit has \(H_2=0\); hence
\(g=1\) and the source translation is transitive.'''+ '\n'+t[b:]
 a=t.index(r'Let \(S_D\)')
 b=t.index(r'\item Label the fibre components',a)
 new=r'''Let \(S_D\) be the smooth elliptic-surface neighbourhood and
let the actual contracting line lift cover \(Q:S_D\to S_D\).
The Hermitian norm gives the explicit circle quotient
\([v]\mapsto(\pi(v),\log\|v\|)\). Put
\(\rho(p)=-\log(\|Bv\|/\|v\|)>0\), which is independent
of the nonzero vector in its line. In the log-norm coordinate
\(t=\log\|v\|\) and the log-height coordinate \(u=-t\),
the same actual lift is respectively
\[
 B_-(p,t)=(Qp,t-\rho(p)),\qquad
 A_+(p,u)=(Qp,u+\rho(p)).
\]
The coordinate map \(J(p,u)=(p,-u)\) intertwines them:
\(J A_+=B_-J\). On a compact smaller source neighbourhood
choose \(0<\delta<\min\rho\).

\item Choose a smooth nondecreasing function \(\eta:[0,1]\to[0,1]\),
constant zero near zero and one near one, with
\(\eta(1-s)=1-\eta(s)\). Such a function is obtained by
integrating a nonnegative symmetric bump supported in \((0,1)\)
and dividing by its positive integral. For \(L>\delta\), put
\[
 \tau_L(s)=\delta s+(L-\delta)\eta(s).
\]
Its derivative is positive; it equals \(\delta s\) near zero
and \(L+\delta(s-1)\) near one. Set
\(\ell(p)=\rho(Q^{-1}p)\). The actual positive-height
fundamental region is \(0\le u\le\ell(p)\), whose upper face
\((p,\ell(p))\) is sent by \(A_+^{-1}\) to
\((Q^{-1}p,0)\). Thus
\[
 \Psi_+:T_{Q^{-1}}\longrightarrow (S_D\times\mathbb R)/A_+,
 \qquad [p,s]\longmapsto[p,\tau_{\ell(p)}(s)]
\]
is a diffeomorphism. The two displayed end germs agree through
the full source-dependent translation \(A_+^{-1}\), including
its derivative, so this assertion holds smoothly across the seam.
Strict positivity gives the inverse on every interval. It preserves
the complex orientation of \(S_D\) followed by the positive
\(s\) and \(u\) directions.

\item For the contracting log-norm action the actual region is
\(0\le t\le\rho(p)\), and \(B_-\) sends its upper face to
\((Qp,0)\). The analogous map is
\[
 \Psi_-:T_Q\longrightarrow (S_D\times\mathbb R)/B_-,
 \qquad [p,s]\longmapsto[p,\tau_{\rho(p)}(s)].
\]
It is smooth at its seam for the same explicit end-germ calculation
and preserves the positive log-norm interval orientation. The exact
map relating the two descriptions is
\[
 R_Q:T_{Q^{-1}}\longrightarrow T_Q,
 \qquad [p,s]\longmapsto[Q^{-1}p,1-s],\qquad
 \Psi_-R_Q=J\Psi_+.
\]
To check the square, apply \(B_-^{-1}\) to
\((p,-\tau_{\ell(p)}(s))\); this gives
\((Q^{-1}p,\ell(p)-\tau_{\ell(p)}(s))\), which equals
\((Q^{-1}p,\tau_{\ell(p)}(1-s))\) by the chosen symmetry.
Both \(R_Q\) and \(J\) reverse the interval orientation.
In the following intersection calculation we use \(\Psi_+\)
and its positive-height orientation throughout.

'''
 t=t[:a]+new+t[b:]
 t=t.replace(r'(p,1)\sim(Qp,0)',r'(p,1)\sim(Q^{-1}p,0)')
 t=t.replace('is a smooth closed oriented three-manifold in \\(T_Q\\),\nbecause \\(Q\\)',
             'is a smooth closed oriented three-manifold in \\(T_{Q^{-1}}\\),\nbecause \\(Q^{-1}\\)')
 # Only the existing component-orbit trace contains that literal remaining
 # expression; the explicitly typed T_Q map above uses the standard name.
 return t
change('night:P3K.13',repair_k13,
 'Correct the variable positive-height roof to rho(Q^{-1}p), use its actual A^{-1} seam, and print both smooth quotient maps with the exact interval/source reversal. The orbit-sum intersection form and sphere transitivity survive with their orientation explicitly fixed.')

def repair_k15(t):
 old=r'''As in P3K.13, this interval fundamental
region is smoothly
reparametrized to the unit interval with compatible end collars.'''
 new=r'''Use the contracting-log-norm map \(\Psi_-\) of
\cref{night:P3K.13}, with \(Q=h\): its literal height is
\(\tau_{\rho(p)}(s)=\delta s+(\rho(p)-\delta)\eta(s)\).
The upper germ \(\rho(p)+\delta(s-1)\) is sent by the
displayed contracting action to \(\delta(s-1)\) at \(hp\).
This proves the smooth seam and its positive-interval orientation
without changing the generator \(H\), its source map or its
line phase.'''
 assert old in t;t=t.replace(old,new,1)
 old=r'''This gives an explicit orientation-preserving diffeomorphism
from the actual circle orbit of the cap to'''
 new=r'''This gives the explicit diffeomorphism from the actual circle
orbit of the cap to'''
 assert old in t;t=t.replace(old,new,1)
 old=r'''The principal circle line is also identified:'''
 new=r'''Its orientation convention is explicit: \(\Psi_-\) preserves
the complex source orientation followed by increasing log norm.
With the physical circle written first, the quotient orientation
is its negative. Indeed the complex line orientation is
\(dt\wedge d\theta\), and
\[
 d\theta\wedge(-\operatorname{or}S\wedge dt)
       =\operatorname{or}S\wedge dt\wedge d\theta.
\]
This is exactly the interval sign in the \(J,R_Q\) square of
\cref{night:P3K.13}. The intersection obstruction below uses
the stated increasing-log-norm convention on both cycles; changing
to the physical-circle-first convention changes every pairing by
this same sign and preserves its vanishing conclusion.

The principal circle line is also identified:'''
 assert old in t;t=t.replace(old,new,1)
 return t
change('night:P3K.15',repair_k15,
 'Specify the already correctly signed contracting log-norm roof by the explicit Psi_- map; retain H and all finite-kernel/scalar phases unchanged.')

def repair_k16(t):
 old=r'''the delta orbit of the contracting line quotient is the source
mapping torus of P3K.13.'''
 new=r'''the delta orbit of the contracting line quotient is identified
with its source mapping torus by the contracting-log-norm map
\(\Psi_-\) of \cref{night:P3K.13}, with precisely the
source lift and positive interval used in \cref{night:P3K.15}.'''
 assert old in t;return t.replace(old,new,1)
change('night:P3K.16',repair_k16,
 'Resolve the ordinary orbit projection to the exact negative-action log-norm chart Psi_-, retaining the same cap rotation, gamma marking and meridian matrix.')

def repair_k22(t):
 old='is the suspension coordinate, as in P3K.13.'
 new=r'''is the suspension coordinate of the contracting-action map
\(\Psi_-\) in \cref{night:P3K.13}, with the full line-phase
identification in \cref{night:P3K.15}. Thus its source return
is the stated \(t_{-G}\), with the positive interval orientation
used in this cellular cone.'''
 assert old in t;return t.replace(old,new,1)
change('night:P3K.22',repair_k22,
 'Identify the existing t_{-G} mapping torus with the exact contracting-action Psi_- chart. The cone differential T^{-1}-I and its positive suspension marking are preserved; this bounded repair is not a whole-proof check of K22.')

for label,uses in {
 'night:P3R.1':r'\cite[Section 3.1(v) and Remark 3.1, pp.~5--6]{Jiang2014}; \cite[Section 3, p.~69]{Davis1982}',
 'night:P3K.12':r'\cite[Corollary 1.8, p.~3; Proposition 2.2, pp.~5--6]{Satriano2012}; \cite[Theorem 4.4, p.~146; coefficient convention, p.~139]{Floyd1952}',
 'night:P3K.13':r'\cref{night:P3F.8}; the explicit maps $\Psi_+,\Psi_-,J,R_Q$ and the integral orbit cycles below',
 'night:P3K.14':r'\cref{night:P3F.2,night:P3K.13}',
 'night:P3K.15':r'\cref{night:P3K.13,night:P3F.8}; \cite[Theorem 4.4, p.~146]{Floyd1952}',
 'night:P3K.16':r'\cref{night:P3K.13,night:P3K.15,night:P3F.8,night:P3F.9}',
 'night:P3K.18':r'\cref{night:P3K.16,night:P3F.8}',
}.items():
 change(label,lambda t,u=uses:add_uses(t,u),'Record the exact current source or geometric dependency of the completed orbit review.')
