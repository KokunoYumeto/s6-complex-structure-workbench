"""Explicit maps and exact known-result credit from the current fan/norm review."""
def repair_f30(t):
 old=r'''Conjugating the negative-weight line makes the circle representation positive on both summands.'''
 new=r'''Equip each line with a Hermitian form, conjugate-linear in its first argument.
The actual complex-linear map
\(\overline L\longrightarrow L^*\),
\(\bar v\longmapsto h(v,-)\), identifies the conjugate line
with its dual and transports its circle weight from \(-1\) to \(+1\).
Applying this map to the negative-weight summand makes both circle
weights positive.'''
 assert old in t;t=t.replace(old,new,1)
 old=r'''a topologically trivial \(SU(2)\) bundle on the sphere.'''
 new=r'''a topologically trivial \(SU(2)\) bundle on the sphere.
For an explicit nullhomotopy of its equatorial transition, choose a
smooth \(\vartheta:[0,1]\to[0,\pi/2]\), equal to a positive
constant times \(r\) near zero and to \(\pi/2\) near one.
With \(a=\sin\vartheta(r)e^{i\theta}\) and
\(b=\cos\vartheta(r)\), the matrix
\[
 \begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix}\in SU(2)
\]
extends smoothly over the disk and has boundary
\(\operatorname{diag}(e^{i\theta},e^{-i\theta})\).
The even Taylor expansion of \(b\) and the smooth radial factor
\(\sin\vartheta(r)/r\) prove smoothness at the center.'''
 assert old in t;t=t.replace(old,new,1)
 return t
change('night:P3F.30',repair_f30,
 'Print the Hermitian conjugate-line duality and the explicit SU(2) disk extension that carry the two resolved weight bundles to their opposite retained Hopf base factors.')

def repair_f35(t):
 old=r'''\item The full argument has passed independent audit.'''
 new=r'''\item For the original reference fan, the fixed rational curve,
its normal weights and every finite-subgroup fixed set are already
computed in \cite[Proposition 9.24 and Remarks 9.25--9.26,
pp.~82--83]{AC26}. The proof below establishes the actual
integral-basis classification, periodic flop maps and prime fixed-set
calculation for every allowed one-vertex fan. Its reference-fan
specialization uses precisely the same quotient-lattice map.'''
 assert old in t;t=t.replace(old,new,1)
 return t
change('night:P3F.35',repair_f35,
 'Replace a historical global audit sentence by exact credit to the original reference-fan result, retaining the complete general-fan application and the actual integral quotient-lattice maps.')

def repair_k19(t):
 old=r'''An additional inversion would
change the marked linear monodromy from trace two to
trace minus two and is not the outer monodromy of this
\(I_N\) source cap.'''
 new=r'''In the retained symplectic marking the linear monodromy is
\(R_N=\left(\begin{smallmatrix}1&N\\0&1\end{smallmatrix}\right)\).
Composing with inversion gives \(-R_N\). Their traces are
\(2\) and \(-2\); since \(\operatorname{tr}(P R_NP^{-1})
=\operatorname{tr}(R_N)\) for every invertible marking matrix
\(P\), no change of marking identifies the latter map with the
specified outer monodromy. Thus the retained cap maps have exactly
the translation component action used above.'''
 assert old in t;return t.replace(old,new,1)
change('night:P3K.19',repair_k19,
 'Display the actual unipotent monodromy and its inversion composite, and prove the marking obstruction by the invariant trace rather than an unsupported categorical exclusion.')
