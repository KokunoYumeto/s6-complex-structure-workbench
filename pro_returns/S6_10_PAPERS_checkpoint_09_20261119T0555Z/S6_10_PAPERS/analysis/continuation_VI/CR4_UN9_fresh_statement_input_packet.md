# Clean statement and input packet: CR.4 and UN.9

This packet contains no target proof or target reduction. The reviewer should write the complete proposed comparison before opening either target proof or the Paper VI owner's comparison receipts.

## Actual setting

A proper holomorphic map from a smooth complex threefold to a smooth curve has nearby smooth fibres that are complex two-tori. Work over a sufficiently small disc containing a single specified singular value. At the point under review, the full fibre is a unit times a common positive power of one reduced local equation. Its full reduced critical locus is a smooth curve; this assumption concerns the reduced support of the Jacobian ideal. No reducedness of that Jacobian ideal is supplied. The generic transverse singularity is exactly the type specified in the target statement.

## Permitted boundary setup

Choose a sufficiently small closed ball around the germ such that its boundary is transverse to the smooth critical curve and to the smooth stratum of the zero hypersurface. The critical curve meets the boundary in a compact link. Shrink so that the generic transverse type holds at every point of that link. No uniform boundary transversality for any new family is assumed; that comparison, if used, must be proved.

## Target statements

```latex
\begin{proposition}[A smooth critical curve with generic cusp is a constant cusp]\label{cdp:st:C.2.CR.4}
\Uses{the hypotheses, notation and definitions stated here; \cref{cdp:st:A.5.17}; \cref{cdp:eq:C.CR.17}; \cref{cdp:st:A.5.15}; \cref{cdp:eq:C.CR.18}}


Let a reduced hypersurface germ $\{f=0\}$ in a smooth
complex threefold occur in a fibre whose nearby smooth
fibres are complex two-tori. Suppose that the full reduced
critical locus of $f$ near the point is a smooth curve
and that the generic transverse singularity is an ordinary
cusp. Then there are local holomorphic coordinates in which
\[
                            f=X^2+Y^3.             \tag{C.CR.15}\label{cdp:eq:C.CR.15}
\]
An analytic unit and a common full-fibre multiplicity may
be retained in the original map: they do not change this
assertion about the reduced hypersurface.
\end{proposition}
```

```latex
\begin{proposition}[A smooth full critical curve with generic node is a product node]\label{cdp:st:C.2.UN.9}
\Uses{the hypotheses, notation and definitions stated here; \cref{cdp:eq:C.UNNODE.2}; \cref{cdp:st:A.5.15}; \cref{cdp:eq:C.UNNODE.3}}


Let a reduced hypersurface germ $\{f=0\}$ in a smooth
complex threefold occur in a fibre of a proper torus-surface
degeneration. Suppose that the full reduced critical locus
of $f$ is a smooth curve and its generic transverse
singularity is an ordinary node. There are local
holomorphic coordinates in which
\[
                            f=XY.                  \tag{C.UNNODE.1}\label{cdp:eq:C.UNNODE.1}
\]
The conclusion about the reduced hypersurface also holds
when the actual map has a holomorphic unit and a common
positive multiplicity.
\end{proposition}
```

## Cited input statements

```latex
\begin{proposition}[Hirzebruch germs cannot occur in a torus degeneration]\label{cdp:st:A.5.15}
\Uses{the hypotheses, notation and definitions stated here; \cref{cdp:eq:A.J.33a}; \cref{cdp:eq:A.J.33b}; \cite[Theorem L1 and Example 2.4(a)]{Nemethi1991Join}; \cite[Theorem 4.1 and Lemma 4.6]{MPW2005Hirzebruch}; \cref{cdp:eq:A.J.35}; \cite[Theorem 4.2(2)]{MPW2005Hirzebruch}; \cref{cdp:eq:A.J.34}; \cref{cdp:eq:A.J.37}}


Let $f:Y\to C_0$ be a proper holomorphic map from a
smooth complex threefold to a smooth curve, with smooth
nearby fibres complex two-tori. There is no point of
a fibre at which, in holomorphic ambient coordinates
$(x,y,z)$ and a coordinate on the base, the map has
the equation
\[
 f(x,y,z)=u(x,y,z)\bigl(x^a-y^bz^c\bigr)^m,
 \quad a\ge2,\quad b,c,m\ge1,                                    \tag{A.J.33}\label{cdp:eq:A.J.33}
\]
where $u$ is a holomorphic unit. No Betti-number
assumption on $Y$ is needed. This includes the pinch
point, every germ $x^2-y^{2k}z^{2r+1}$ with
$k\ge1$, $r\ge0$, and the reducible germ
$x^2-y^2z^2$.
\end{proposition}
```

```latex
\begin{proposition}[Isolated singularities are excluded and suspension germs are transverse products]\label{cdp:st:A.5.17}
\Uses{the hypotheses, notation and definitions stated here; \cref{cdp:st:A.5.15}; \cite[Lemma 6.1 and Appendix B]{Milnor1968}; \cref{cdp:eq:A.J.40}; \cref{cdp:eq:A.J.39}}


Let $f:Y\to C_0$ have the hypotheses of \ref{cdp:st:A.5.15}.
No local equation $f=u h^m$, with $u$ a holomorphic
unit and $m\ge1$, can have a reduced equation $h$
with an isolated critical point at the origin.
Suppose its local equation at a point of a fibre is
\[
             f=(x^a-g(y,z))^m,
             \qquad a\ge2,\quad m\ge1,             \tag{A.J.38}\label{cdp:eq:A.J.38}
\]
where $g\ne0$ and $g(0,0)=0$. Then the reduced
plane germ $\{g=0\}_{\rm red}$ is smooth. If
$b$ is its multiplicity in $\operatorname{div}(g)$,
there are local holomorphic coordinates in which
$f=(x^a-y^b)^m$.
Consequently, at every point where the full fibre
is a uniform multiple of its reduced support and
the reduced equation has a nonzero Hessian, its
critical surface germ is a constant
transverse $A_{b-1}$ product. A nonordinary change
of transverse type at a point with nonzero Hessian
is excluded.
\end{proposition}
```

## Exact local input from the cited Hirzebruch calculation

The cited local construction in A.5.15 gives, in an arbitrarily small nonzero local level of either X²+Y²Z or Y³+X²Z, a compact spherical homology class represented by a continuous map from S² with self-intersection −4. Embeddedness is not supplied or required. The primary inputs for that construction are Némethi1991Join, Theorem L1 and Example2.4(a), and MPW2005Hirzebruch, Theorem4.2(2), as listed in A.5.15. This local input does not itself say that a level of a perturbed germ embeds in an original global torus fibre; establishing the actual comparison is part of the requested fresh work.

Other standard tools available with their usual hypotheses are the holomorphic splitting lemma with parameters, Weierstrass preparation, the proper-submersion theorem for compact manifolds with transverse boundary, and asphericity of the complex two-torus via its universal cover C². Any use must retain the actual coordinate maps and boundary hypotheses.
