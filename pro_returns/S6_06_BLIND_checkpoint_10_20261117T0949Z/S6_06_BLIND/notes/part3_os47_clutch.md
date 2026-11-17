# P3F.23. The positive OS47 parameter loop makes one positive gamma turn

**Proved.** For the explicitly closed OS47 family of P3F.21, put
\(\lambda=r^4\) and \(v=\log r/(2\pi i)\). In the fixed line
character \(V=\exp(2\pi i\zeta _2)\), its positive \(r\)-loop has
angular clutch
\[
 F(s,v+\theta)-F(s,v)
    =\theta\gamma(s,v)+2\theta(\theta-1)\delta,
 \qquad 0\leq\theta\leq1.                         \tag{P3F.23.1}
\]
Thus the rotation in the circle quotient is one positive gamma turn.
The remaining line gauge is periodic and has value one at both
endpoints. On the fourth-root cusp deck its winding is positive four.

**Proof.** Use the cusp parameter \(q=t-t_c\), and set
\(s=\log q/(2\pi i)\). Both the line section \(R=7G\) and the
translation point \(Q=2G\) meet the smooth identity component at
this \(I_1\) fibre. In a Tate coordinate and an invertible local
line frame the suspension period is consequently
\[
 \gamma(s,v)=\binom{\Gamma(q)}{C(q)+s+4v},\qquad
 \delta=\binom01,
\]
where \(\Gamma\) is a holomorphic logarithmic representative of
\(-Q\), and \(C\) is holomorphic. The sign in the second coordinate
comes from the actual multiplier \(\lambda q\): exponentiating
gives \(e^{2\pi iC}q r^4\).

The positive parameter deck must be distinguished from its inverse
closing isomorphism. At the fourth-root cap, the logarithmic gluing is
\(z\mapsto z+\log(s_\infty)/(2\pi i)\ell(c_{47})\), and
\(\ell(c_{47}+4)-\ell(c_{47})=4\delta\). Therefore the ordinary
positive deck translates by
\(-\log(t-t_c)/(2\pi i)\delta\), since its finite-cap expansion is
\(+\log q_\infty/(2\pi i)\delta\) plus a holomorphic unit logarithm.
In the chosen cusp coordinate this is exactly
\[
 (v,\zeta)\longmapsto(v+1,\zeta-s\delta).          \tag{P3F.23.2}
\]
Multiplication by \(h(t)=t-t_c\) is the inverse map, from
\(c_{47}+4\) to \(c_{47}\). Both directions extend by the local
argument in P3F.21. Parameter-independent changes of the ordinary
frame add the same term to the two origins below and cancel in their
difference.

On \(q=Q_0^4\), take the two explicit origins
\[
 o(s,v)=\binom{-\Gamma s/4}{-Cs/4-s^2/8-sv},\qquad
 \sigma(s,v)=\binom{\Gamma v}{Cv+2v^2-2v}.          \tag{P3F.23.3}
\]
Their deck differences are
\[
 \begin{aligned}
 o(s,v+1)-o(s,v)&=-s\delta,\\
 \sigma(s,v+1)-\sigma(s,v)&=-s\delta+\gamma(s,v),\\
 o(s+4,v)-o(s,v)&=-\gamma(s,v)-2\delta,\\
 \sigma(s+4,v)-\sigma(s,v)&=0.
 \end{aligned}                                   \tag{P3F.23.4}
\]
Each discrepancy beyond (P3F.23.2) is an actual integral lattice
period. Hence these origins descend to sections of the specified
torus torsor, with the cyclic cusp cover retained. The cusp origin
\(\sigma\) is holomorphic and bounded in \(q\) for each
\(r\ne0\); its characters act by units in the cusp toric charts,
so it extends there. Subtracting \(o\) removes the parameter deck.
Over any fixed nonzero \(q\), the remaining period multiplier is
\(e^{2\pi iC}q r^4\), and the standard four-node rank-one chain
\(X_i=V/r^i,\ Y_i=r^{i+1}/V,\ X_iY_i=r\) supplies the partial
parameter filling. Its zero-coordinate origin extends. Thus these
are the extending origins for the two actual collars, not arbitrary
polynomials satisfying only a finite-difference identity.

Their difference is
\[
 F=\sigma-o=
 \binom{\Gamma(s+4v)/4}
       {C(s+4v)/4+(s+4v)^2/8-2v}.
\]
Direct subtraction proves (P3F.23.1). The additional real delta
coefficient vanishes at \(\theta=0,1\), so its exponentiation is a
periodic unitary gauge homotopic to the constant gauge through
periodic gauges. It vanishes in the circle quotient. Furthermore
\[
 \begin{split}
 &[F(s+4,v+\theta)-F(s+4,v)]
       -[F(s,v+\theta)-F(s,v)]\\
 &\hspace{35mm}=4\theta\delta.
 \end{split}
\]
The corresponding transition is \(e^{8\pi i\theta}\), with winding
four. This is the retained line clutch for the actual positive
parameter loop. All equalities, including both endpoint values,
are independently executed in `code/part3/os47_origins.py`.
**End of proof.**
