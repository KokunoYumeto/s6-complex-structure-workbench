\section{From the original stable framing to the collapse map}\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section}
The following complete arguments are retained as re-derivations of their classical prerequisites. Source-specific calculations and their hypotheses are stated explicitly.



Ten sections prove the full original framing and collapse construction, both bordism/homotopy directions and their inverse comparisons, suspension and stable bounding, the exact original complex tangent-framing homotopy, and two complete worked exercises. The stable degree-six class and the subsequent surgery calculation are proved in the included receiving companions, culminating in the \cref{courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-original-smooth-map}.

The receiving manifold is the original compact smooth six-manifold \(X\) of lesson 7. The included stable-framing proof supplies a specified isomorphism


```{=latex}
\begin{equation}
\tau:TX\oplus\mathbf1_{\mathbb R}\longrightarrow
                  X\times\mathbb R^7.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.1}
\end{equation}
```


Keep this map and its inverse, rather than replacing them by a frame chosen without reference to the construction. The following formulas also cover a compact smooth \(n\)-manifold \(M\) without boundary, with a specified isomorphism


```{=latex}
\begin{equation}
\tau:TM\oplus\mathbf1_{\mathbb R}^{\,k}
            \longrightarrow M\times\mathbb R^{n+k}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.2}
\end{equation}
```


They will be applied with \(M=X,n=6,k=1\).

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-original-embedding}

\subsection{An embedding retaining the original charts}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-1}\label{courseIII:pontryagin-thom:1}

Choose finitely many original coordinate charts \((U_i,\psi_i)\), compact subsets \(K_i\subset U_i\) whose interiors cover \(M\), and smooth functions \(\chi_i\) supported in \(U_i\) and equal to one on a neighborhood of \(K_i\). Such functions are obtained from the positive smooth cutoff on two nested coordinate balls and a finite refinement of the compact cover. Extend both \(\chi_i\) and \(\chi_i\psi_i\) by zero outside \(U_i\); their supports lie in compact subsets of \(U_i\), so these extensions are smooth. Let the number of charts be \(L\) and put \(N=(n+1)L\). Define the actual map


```{=latex}
\begin{equation}
j:M\longrightarrow\mathbb R^N,\qquad
 j(m)=\bigl(\chi_i(m),\,\chi_i(m)\psi_i(m)\bigr)_{i=1}^{L}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.3}
\end{equation}
```


Its full derivative is


```{=latex}
\begin{equation}
Dj_m(v)=
 \bigl(d\chi_i(v),\,
       d\chi_i(v)\psi_i(m)+\chi_i(m)D\psi_i(v)\bigr)_{i=1}^{L}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.4}
\end{equation}
```


For each \(m\), some \(\chi_i\) is identically one near \(m\). The corresponding coordinate block of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.4} is \(D\psi_i\), which is injective. Thus \(j\) is an immersion. If \(j(m)=j(m')\), choose such an \(i\). Equality of the first component gives \(\chi_i(m')=1\), so both points are in \(U_i\). Equality of the remaining block gives \(\psi_i(m)=\psi_i(m')\), hence \(m=m'\). The continuous injection \(j\) from compact \(M\) to the Hausdorff space \(\mathbb R^N\) is a homeomorphism onto its image. Together with the immersion property this proves that \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.3} is a smooth embedding.

Use the standard ambient Euclidean inner product solely to define the normal subbundle


```{=latex}
\begin{equation}
\nu_m=\{y\in\mathbb R^N:\langle y,Dj_m(v)\rangle=0
                                  \text{ for every }v\in T_mM\}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.5}
\end{equation}
```


In any one of the original coordinates write \(J\) for the \(N\)-by-\(n\) matrix of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.4}, and put


```{=latex}
\begin{equation}
H=J^{\mathsf T}J,\qquad
 P_\nu=I_N-JH^{-1}J^{\mathsf T}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.6}
\end{equation}
```


The matrix \(H\) is positive definite because \(J\) has full column rank. Direct multiplication shows


```{=latex}
\begin{equation}
P_\nu^{\,2}=P_\nu,\qquad
 P_\nu J=0,\qquad
 P_\nu^{\mathsf T}=P_\nu.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.7}
\end{equation}
```


Thus \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.6} is the actual orthogonal projection onto \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.5}.

The projection is independent of the chosen coordinate representation. Under the change \(J\mapsto JA\) with \(A\) invertible, its entire product becomes


```{=latex}
\begin{equation}
JA\bigl(A^{\mathsf T}HA\bigr)^{-1}A^{\mathsf T}J^{\mathsf T}
       =JH^{-1}J^{\mathsf T}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.8}
\end{equation}
```


Every coordinate matrix \(A\) has been retained in this comparison. Any other original metric on \(M\) continues to exist as its original matrix; \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.6} defines the particular ambient projection used in the construction and makes no identification of that metric with \(H\).

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-stable-normal-frame}

\subsection{The exact map from the tangent framing to a normal framing}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-2}\label{courseIII:pontryagin-thom:2}

Stabilize the embedding by the specified zero inclusion


```{=latex}
\begin{equation}
j':M\longrightarrow\mathbb R^{N+n+k},\qquad j'(m)=(j(m),0).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.1}
\end{equation}
```


Its actual normal bundle is \(\nu\oplus\mathbf1_{\mathbb R}^{\,n+k}\). Its rank is


```{=latex}
\begin{equation}
r=(N-n)+(n+k)=N+k.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.2}
\end{equation}
```


For \(y\in\nu_m\) and \(u\in\mathbb R^{n+k}\), write


```{=latex}
\begin{equation}
(v,b)=\tau_m^{-1}(u)\in T_mM\oplus\mathbb R^k.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.3}
\end{equation}
```


Define


```{=latex}
\begin{equation}
\begin{aligned}
 \alpha_m:\nu_m\oplus\mathbb R^{n+k}&\longrightarrow
                                 \mathbb R^N\oplus\mathbb R^k,\\
 \alpha_m(y,u)&=(y+Jv,b).
 \end{aligned}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.4}
\end{equation}
```


This is a bundle isomorphism. Its full inverse, with domain
\((a,b)\in\mathbb R^N\oplus\mathbb R^k\), is


```{=latex}
\begin{equation}
\alpha_m^{-1}(a,b)
    =\left(P_\nu a,\,
       \tau_m\bigl(H^{-1}J^{\mathsf T}a,b\bigr)\right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.5}
\end{equation}
```


Indeed \(P_\nu a+JH^{-1}J^{\mathsf T}a=a\), so \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.4} after \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.5} is the identity. Conversely \(J^{\mathsf T}y=0\) for \(y\in\nu_m\), whence applying \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.5} to \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.4} gives


```{=latex}
\begin{equation}
P_\nu(y+Jv)=y,\qquad
 H^{-1}J^{\mathsf T}(y+Jv)=v,\qquad
 \tau_m(v,b)=u.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.6}
\end{equation}
```


This proves the other composite exactly. Equations \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.8} and the coordinate transformation rule for \(\tau_m\) prove that \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.4}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.5} agree on overlapping original charts.

For each standard coordinate vector \(e_\ell\) of
\(\mathbb R^r=\mathbb R^N\oplus\mathbb R^k\), let


```{=latex}
\begin{equation}
E_\ell(m)=\alpha_m^{-1}(e_\ell)
       \in\nu_m\oplus\mathbb R^{n+k}
       \subset\mathbb R^{N+n+k},\qquad 1\leq\ell\leq r.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.7}
\end{equation}
```


These are the ordered original normal-frame vectors produced by the tangent framing. Write \(E\) for their ambient matrix and retain its entire Gram matrix


```{=latex}
\begin{equation}
G(m)=E(m)^{\mathsf T}E(m).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.8}
\end{equation}
```


It is positive definite. There is no orthonormal-frame substitution in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.7}.

The orientation sign can also be read without dropping the permutation. Give \(\nu\) the orientation for which \(TM\) followed by \(\nu\) has the ambient orientation. If \(\tau\) preserves the specified orientation of \(TM\oplus\mathbb R^k\), then the determinant sign of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.4}, from the ordered domain \(\nu,\,\mathbb R^{n+k}\) to the ordered target \(\mathbb R^N,\,\mathbb R^k\), is


```{=latex}
\begin{equation}
(-1)^{n(N-n)}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.9}
\end{equation}
```


To verify this, use \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.3} to write the domain order as \(\nu,TM,\mathbb R^k\). The target order is \(TM,\nu,\mathbb R^k\). Moving the \(n\) tangent vectors past the \(N-n\) normal vectors gives exactly \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.9}; the other two maps preserve the stated orientations. If the determinant sign of \(\tau\) is negative, multiply \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.9} by that sign. For \(n=6\), the permutation factor is \(+1\) for every original \(N\). For lesson 7, \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.1} has ambient dimension \(N+7\) and the ordered normal frame has rank \(r=N+1\).

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-full-tube-and-collapse}

\subsection{The original-radius tube and its smooth collapse}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-3}\label{courseIII:pontryagin-thom:3}

For a positive number \(\epsilon\), retain the actual ellipsoidal fiber condition


```{=latex}
\begin{equation}
\mathcal U_\epsilon=
 \{(m,A)\in M\times\mathbb R^r:
                 \rho(m,A)=A^{\mathsf T}G(m)A<\epsilon^2\}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.1}
\end{equation}
```


Define


```{=latex}
\begin{equation}
\Gamma(m,A)=j'(m)+E(m)A.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.2}
\end{equation}
```


Its full derivative is


```{=latex}
\begin{equation}
D\Gamma_{(m,A)}(v,B)
   =Dj'_m(v)+(DE_m[v])A+E(m)B.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.3}
\end{equation}
```


At \(A=0\), the first and last blocks are complementary tangent and normal subspaces. In original tangent coordinates the full inverse at the zero section is


```{=latex}
\begin{equation}
V\longmapsto
 \left(H^{-1}(J')^{\mathsf T}V,\,
              G^{-1}E^{\mathsf T}V\right),
 \qquad J'=\begin{pmatrix}J\\0\end{pmatrix}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.4}
\end{equation}
```


The cross-products \((J')^{\mathsf T}E\) are zero and the two diagonal Gram matrices are \(H\) and \(G\), proving \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.4}. Away from the zero section the full matrix is


```{=latex}
\begin{equation}
\bigl[J'_1+(DE[\partial_1])A,\ldots,
           J'_n+(DE[\partial_n])A,\ E\bigr],
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.5}
\end{equation}
```


where the first block means the \(n\) columns specified separately in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.3}. Its inverse is the inverse of this entire matrix, including all \(DE\) terms.

There is a single positive tube bound for which \(\Gamma\) is a diffeomorphism onto its open image. First, compactness and the invertible zero-section derivative give a neighborhood of the entire zero section on which the derivative is invertible. The least eigenvalue of \(G\) has a positive lower bound, so a sufficiently small normal-radius bound places the whole tube in that neighborhood. If global injectivity failed for every such bound, choose distinct pairs \((m_j,A_j),(m'_j,A'_j)\) with equal images and both original normal lengths tending to zero. Compactness gives a subsequence with limits \(m,m'\). Equality of images then implies \(j'(m)=j'(m')\), hence \(m=m'\). Both pairs converge to \((m,0)\), contradicting the local inverse-function theorem there. Thus a sufficiently small single bound gives injectivity. A bijective local diffeomorphism onto its image has the smooth local inverses as its global inverse. Choose the retained \(\epsilon\) so that \(2\epsilon\) is less than this proved bound. Then \(\Gamma\) is a diffeomorphism on the larger tube \(\mathcal U_{2\epsilon}\) as well as on \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.1}. These larger-tube coordinates remain valid across the actual collapse boundary \(\rho=\epsilon^2\).

Regard \(S^{N+n+k}\) as the one-point compactification of the actual ambient coordinate space in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.1}. Write \(\infty\) for the added basepoint. In the target unit sphere \(S^r\subset\mathbb R^{r+1}\), retain the two specified points


```{=latex}
\begin{equation}
q_-=(0,-1),\qquad q_+=(0,1)
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.6}
\end{equation}
```


and the exact inverse stereographic coordinate map


```{=latex}
\begin{equation}
\sigma(Z)=
 \left(\frac{2Z}{1+Z^{\mathsf T}Z},
       \frac{Z^{\mathsf T}Z-1}{1+Z^{\mathsf T}Z}\right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.7}
\end{equation}
```


For \(\rho<\epsilon^2\), put


```{=latex}
\begin{equation}
\lambda(\rho)=\exp\!\left(\frac{\rho}{\epsilon^2-\rho}\right),
 \qquad Z(m,A)=\lambda(\rho(m,A))A.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.8}
\end{equation}
```


The collapse map with all its original fiber data is


```{=latex}
\begin{equation}
\mathcal P:S^{N+n+k}\longrightarrow S^r,\qquad
 \mathcal P(\Gamma(m,A))=\sigma(Z(m,A)),\qquad
 \mathcal P=q_+\ \hbox{outside }\Gamma(\mathcal U_\epsilon).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.9}
\end{equation}
```


In particular \(\mathcal P(\infty)=q_+\). This is a smooth based map.

Here are the boundary and regular-value verifications. In the target chart centered at \(q_+\), \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.7} has coordinate


```{=latex}
\begin{equation}
\frac{Z}{Z^{\mathsf T}Z}
  =\exp\!\left(-\frac{\rho}{\epsilon^2-\rho}\right)
                   \frac{A}{A^{\mathsf T}A}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.10}
\end{equation}
```


Near the tube boundary \(\rho=\epsilon^2\), the vector \(A\) is bounded away from zero, since the largest eigenvalue of \(G\) is uniformly bounded above. The exponential in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.10} is


```{=latex}
\begin{equation}
\exp(1)\exp\!\left(-\frac{\epsilon^2}{\epsilon^2-\rho}\right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.11}
\end{equation}
```


Every derivative of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.11} is a finite sum of a polynomial in
\((\epsilon^2-\rho)^{-1}\), derivatives of \(\rho\), and the same exponentially decaying factor. It tends to zero faster than every power of \(\epsilon^2-\rho\). Multiplication by the smooth bounded local derivatives of \(A/(A^{\mathsf T}A)\) therefore gives a smooth zero extension of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.10} across the boundary. The map is constant on a neighborhood of the ambient basepoint because the closed tube is contained in a bounded set. These facts prove smoothness of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.9} everywhere.

The full differential inside the tube is retained as follows:


```{=latex}
\begin{equation}
\begin{aligned}
 d\rho&=2A^{\mathsf T}G\,dA+A^{\mathsf T}(dG)A,\\
 dZ&=\lambda(\rho)\left(dA+
               \frac{\epsilon^2}{(\epsilon^2-\rho)^2}A\,d\rho\right),\\
 D\sigma_Z(B)&=
 \left(\frac{2B}{1+Z^{\mathsf T}Z}
      -\frac{4Z(Z^{\mathsf T}B)}{(1+Z^{\mathsf T}Z)^2},
       \frac{4Z^{\mathsf T}B}{(1+Z^{\mathsf T}Z)^2}\right),\\
 D\mathcal P&=D\sigma_Z\circ DZ\circ(D\Gamma)^{-1}.
\end{aligned}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.12}
\end{equation}
```


Thus the original Gram matrix, its derivatives, the original tube radius and every off-zero derivative of \(E\) remain present.

The inverse image of \(q_-\) is exactly \(j'(M)\): inside the tube, \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.7} equals \(q_-\) exactly when \(Z=0\), equivalently \(A=0\); outside the tube its value is the different point \(q_+\). At the zero section, \(\lambda(0)=1\) and \(dZ=dA\). In the target chart


```{=latex}
\begin{equation}
\kappa_-(Y,t)=\frac{Y}{1-t},
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.13}
\end{equation}
```


we have \(\kappa_-\sigma(Z)=Z\). Therefore


```{=latex}
\begin{equation}
D(\kappa_-\mathcal P)_{j'(m)}E_\ell(m)=e_\ell,\qquad
 \ker D(\kappa_-\mathcal P)_{j'(m)}=Dj'_m(T_mM).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.14}
\end{equation}
```


This proves that \(q_-\) is a regular value and that its ordered inverse-image normal framing is exactly \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.7}. In the ambient target tangent coordinates the derivative is \(2e_\ell\), since \(D\sigma_0(B)=(2B,0)\); the target frame used by \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.13} is correspondingly \((2e_\ell,0)\). The factor two has not been removed.

For an explicit comparison with the usual boundary orientation on the target unit sphere, put its outward normal first. At the south pole the determinant of that ordered ambient frame is


```{=latex}
\begin{equation}
\det\bigl[q_-,(2e_1,0),\ldots,(2e_r,0)\bigr]
                       =(-1)^{r+1}2^r.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.15}
\end{equation}
```


The last-coordinate vector moves past all \(r\) tangent vectors and has its own negative sign, which proves the formula. Thus the target coordinate frame used throughout has sign \((-1)^{r+1}\) relative to that boundary orientation. All inverse-image frames here use the specified \(\kappa_-\) coordinate frame; \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.15} is the exact orientation conversion whenever the outward-normal-first sphere convention is invoked.

These constructions give the required exact map from the original stable tangent framing to a smooth sphere map with its prescribed regular framed inverse image.

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-bordism-to-homotopy}

\subsection{An actual framed bordism gives an actual based homotopy}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-4}\label{courseIII:pontryagin-thom:4}

Fix \(D=n+r\). An embedded framed bordism for the present construction consists of a compact smooth \((n+1)\)-manifold


```{=latex}
\begin{equation}
W\subset\mathbb R^D\times[0,1]
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.1}
\end{equation}
```


with a specified ordered normal frame \(E_W\) of rank \(r\), and specified product collars at both ends. In those collars its embedding and frame are exactly


```{=latex}
\begin{equation}
(m,t)\longmapsto(j_i(m),t),\qquad
 E_W(m,t)=\begin{pmatrix}E_i(m)\\0\end{pmatrix},
 \quad i=0,1.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.2}
\end{equation}
```


There are no other intersections with the boundary of the cylinder. Each \(j_i\) is an embedding of the corresponding compact \(n\)-manifold, and \(E_i\) is its original ordered normal frame.

The smooth tube proof of \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-3} applies to \(W\), with the boundary handled by the exact product coordinates \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.2}. In particular, there is an actual tube


```{=latex}
\begin{equation}
\Gamma_W(w,A)=w+E_W(w)A,\qquad
 \rho_W(w,A)=A^{\mathsf T}G_W(w)A,\qquad
 G_W=E_W^{\mathsf T}E_W,
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.3}
\end{equation}
```


that is injective with invertible derivative on a fixed larger-radius neighborhood. It can be chosen inside \(\mathbb R^D\times[0,1]\). To check the latter point, choose smaller product collars first. In these collars the last component of \(E_W\) is zero, so the normal displacement leaves \(t\) unchanged. The rest of \(W\) is compact and has positive distance from both boundary hyperplanes. Choose the normal-radius bound smaller than that distance. The displacement has Euclidean length \(\sqrt{\rho_W}\), so it cannot cross either boundary there.

Choose one positive \(\epsilon\) strictly inside that tube bound, retaining a larger valid tube of radius \(2\epsilon\). Replace \((\Gamma,\rho)\) by \((\Gamma_W,\rho_W)\) in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.8}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.10}, and set the map equal to \(q_+\) outside the smaller tube. This gives a smooth map on the original cylinder


```{=latex}
\begin{equation}
\mathcal P_W:\mathbb R^D\times[0,1]\longrightarrow S^r.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.4}
\end{equation}
```


The flatness calculation \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.10}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.11} proves its smoothness across the tube boundary; the larger tube gives the actual boundary coordinates required by that calculation.

Since \(W\) is compact, the projection of the closed tube to \(\mathbb R^D\) is bounded. Consequently \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.4} is equal to \(q_+\) outside a single compact set in the spatial variables, uniformly for all \(t\). It therefore extends to a based homotopy


```{=latex}
\begin{equation}
\mathcal H:S^D\times[0,1]\longrightarrow S^r,\qquad
 \mathcal H(\infty,t)=q_+.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.5}
\end{equation}
```


The endpoint restrictions are exactly the collapse maps for \((j_0,E_0)\) and \((j_1,E_1)\) with the same displayed radius \(\epsilon\), because \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.2} identifies all their tube coordinates and Gram matrices.

If the originally specified endpoint maps have radii \(\epsilon_0,\epsilon_1\), first choose the common \(\epsilon\) with


```{=latex}
\begin{equation}
0<\epsilon\leq\min(\epsilon_0,\epsilon_1).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.6}
\end{equation}
```


For each endpoint, interpolate from \(\epsilon_i\) to \(\epsilon\) inside the interval between those two actual positive values, using a smooth parameter function constant near its endpoints. Every tube used is contained in the original valid endpoint tube, since its radius is at most \(\epsilon_i\). Formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.9} with this varying radius is jointly smooth by the same flatness argument and gives a based homotopy of endpoint collapse maps. Its full interior derivative includes the extra radius term:


```{=latex}
\begin{equation}
dZ=\lambda(\rho)\left[
 dA+
 A\left(
 \frac{\epsilon^2}{(\epsilon^2-\rho)^2}\,d\rho
 -\frac{2\epsilon\rho}{(\epsilon^2-\rho)^2}\,d\epsilon
 \right)\right].
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.7}
\end{equation}
```


Here \(\epsilon\) denotes the actual varying radius at that parameter value, and \(d\rho\) is the entire expression in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.12}. Thus neither original endpoint radius has been replaced without its explicit comparison. Concatenate these two endpoint-radius homotopies with \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.5}, using parameter functions constant near the concatenation points. This gives a smooth based homotopy between the originally specified endpoint maps.

For orientation, orient the ambient cylinder by


```{=latex}
\begin{equation}
dt\wedge dx_1\wedge\cdots\wedge dx_D
   =(-1)^D\,dx_1\wedge\cdots\wedge dx_D\wedge dt.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.8}
\end{equation}
```


The sign in this comparison retains the displayed spatial-then-time coordinates of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.1}. Orient a regular inverse image by placing its tangent vectors before the specified target normal-frame vectors. Near an end, the order \((\partial_t,TM_i,E_i)\) agrees with \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.8} when \((TM_i,E_i)\) has the original spatial orientation. Thus \(W\) has orientation \(dt\) followed by the original orientation of \(M_i\) on each collar. The outward-normal-first boundary convention consequently gives


```{=latex}
\begin{equation}
\partial W=(-M_0)\ \sqcup\ M_1.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.9}
\end{equation}
```


At \(t=0\), the outward normal is \(-\partial_t\), giving the first sign; at \(t=1\), it is \(+\partial_t\), giving the second. The regular-value calculation \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.14} on the whole tube also shows that the inverse-image normal frame of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.4} is exactly \(E_W\), including the target tangent factor two. This completes the direction from the given embedded framed bordism to the given based sphere homotopy.

The reverse construction follows. The endpoint germs in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.2}, including their full normal frames, will be retained.

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-relative-regular-value}

\subsection{The relative regular-value construction and its exact frame}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-5}\label{courseIII:pontryagin-thom:5}

Let \(D=n+r\), with \(r\geq1\). A based map here sends the specified \(\infty\in S^D=(\mathbb R^D)^+\) to the specified \(q_+\in S^r\). We first justify passage between continuous homotopies and smooth maps that are constant near the basepoint.

For a continuous based homotopy \(F:S^D\times[0,1]\to S^r\), compactness of its basepoint line gives one neighborhood \(U\) of \(\infty\) whose entire image is in the target chart


```{=latex}
\begin{equation}
\kappa_+(Y,t)=\frac{Y}{1+t}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.1}
\end{equation}
```


Choose a smooth spatial cutoff \(\chi\) equal to zero on a smaller neighborhood of \(\infty\) and equal to one outside \(U\). Within \(U\), replace the original coordinate \(w=\kappa_+F\) by


```{=latex}
\begin{equation}
w_s=\bigl(1-s+s\chi\bigr)w,\qquad 0\leq s\leq1.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.2}
\end{equation}
```


Outside \(U\) retain \(F\). These maps agree wherever \(\chi=1\), give a continuous based homotopy, and at \(s=1\) are constant on a whole spatial neighborhood of the basepoint. The target chart is all of \(\mathbb R^r\), so no coordinate-domain condition is lost by this multiplication. If the original endpoint maps are already constant on basepoint neighborhoods, choose \(U\) inside both of those neighborhoods. Then \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.2} leaves both endpoint maps fixed. For smooth input the full coordinate derivative is


```{=latex}
\begin{equation}
dw_s=(1-s+s\chi)\,dw+
            w\bigl(s\,d\chi+(\chi-1)\,ds\bigr).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.3}
\end{equation}
```



Reparametrize the original homotopy parameter by a smooth function that is zero near zero and one near one. The endpoint maps then occupy exact product collars. Smooth approximation relative these collars and the constant basepoint neighborhood has the following direct construction. Regard the target sphere as its original unit sphere in \(\mathbb R^{r+1}\). On the compact source choose a finite cover on which the oscillation of \(F\) is less than \(\eta\), a subordinate smooth partition \(\psi_i\), and points \(p_i\) in those sets. The Euclidean-valued map \(F_0=\sum_i\psi_i F(p_i)\) is smooth and satisfies \(\|F_0-F\|<\eta\). A cutoff \(\zeta\), equal to one on the prescribed smaller collars and supported where \(F\) is already smooth, gives


```{=latex}
\begin{equation}
\widetilde F=\zeta F+(1-\zeta)F_0,\qquad
 F^{\mathrm{sm}}=\frac{\widetilde F}
                       {\sqrt{\widetilde F^{\mathsf T}\widetilde F}}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.4}
\end{equation}
```


Take \(\eta<1/2\). Every vector on the straight segment from \(F\) to \(\widetilde F\) then has length at least \(1-\eta>0\). Applying the displayed radial retraction to that whole segment gives the required relative homotopy. Its derivative at a nonzero vector \(v\), applied to \(b\), is


```{=latex}
\begin{equation}
D\mathfrak r_v(b)=\frac{b}{\sqrt{v^{\mathsf T}v}}
       -\frac{v(v^{\mathsf T}b)}{(v^{\mathsf T}v)^{3/2}}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.5}
\end{equation}
```


The construction works on boundary charts as well, since smooth partitions on a manifold with boundary can be obtained by restricting partitions on its doubled collar charts. Thus smooth based representatives constant near \(\infty\), and smooth based homotopies constant on endpoint collars, calculate the original continuous based homotopy classes. The norm factors in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.4}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.5} belong to the explicit retraction; no original sphere radius or input map is silently replaced.

We now arrange regularity at the *specified* point \(q_-\). This keeps the target point and its frame, rather than substituting a nearby regular value. The following argument applies either to a single smooth map on \(S^D\) or to a smooth homotopy on \(S^D\times[0,1]\). In the latter case suppose that \(q_-\) is already regular for the two endpoint maps, which are constant in their time collars.

On the open set where \(F\ne q_+\), put \(Q=\kappa_-F\). Choose a smooth target cutoff \(\psi(Q)\) with compact support, equal to one near \(Q=0\). Choose a smooth source cutoff \(\beta\), zero on the prescribed endpoint and basepoint neighborhoods and positive at every other possible nonregular inverse image of \(q_-\). It may be chosen zero only in slightly smaller fixed collars and the basepoint neighborhood; on their transition regions the original endpoint regularity or the absence of \(q_-\) already holds. For \(a\) in a sufficiently small open ball in \(\mathbb R^r\), set


```{=latex}
\begin{equation}
Q_a(p)=Q(p)+\beta(p)\psi(Q(p))a,\qquad
 F_a(p)=\sigma(Q_a(p)).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.6}
\end{equation}
```


Outside the support of the target cutoff use \(F_a=F\). Compact support in the target coordinate chart proves smooth pasting across its excluded point \(q_+\). The same formula with \(sa\) gives a homotopy fixed on all the prescribed neighborhoods. The full derivative is


```{=latex}
\begin{equation}
dQ_a=
 \bigl[I_r+\beta\,a\otimes D\psi_Q\bigr]\,dQ
       +\psi(Q)\,a\,d\beta+\beta\psi(Q)\,da.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.7}
\end{equation}
```



At a zero of \(Q_a\), either \(\beta\psi(Q)\ne0\), in which case the parameter derivative in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.7} is onto, or \(\beta\psi(Q)=0\). In the second case \(Q_a=Q=0\), hence \(\psi(Q)=1\), and \(\beta=0\). Here the original map is regular and \(d\beta=0\), since the nonnegative smooth \(\beta\) is zero there. Thus the source derivative is onto. The universal zero set of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.6} is consequently a smooth manifold. Apply Sard's theorem to its projection to the parameter ball. A parameter outside the critical values gives a regular inverse image for \(F_a\). To see the exact linear implication, its tangent space is


```{=latex}
\begin{equation}
\{(v,b):D_pQ_a(v)+\beta\psi(Q)b=0\}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.8}
\end{equation}
```


If the parameter projection from \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.8} is onto, subtracting a tangent lift of each parameter vector from an arbitrary universal lift proves that \(D_pQ_a\) is onto. Conversely, if \(D_pQ_a\) is onto, it solves \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.8} for every \(b\), proving that projection is onto. The already fixed boundary collars require no perturbation. A countable interior chart cover suffices for Sard; there are only the two boundary strata, on which regularity was retained. This proves the asserted relative regularity. The use of Sard is the same foundational smooth-analysis input as in the included relative Morse proof, \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-1}; the parameter and endpoint comparisons here are proved explicitly.

Let first \(F:S^D\to S^r\) be one such transverse map. Its inverse image


```{=latex}
\begin{equation}
M_F=F^{-1}(q_-)\subset\mathbb R^D
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.9}
\end{equation}
```


is a compact smooth \(n\)-manifold. Compactness follows in \(S^D\), and the inverse image is disjoint from a whole basepoint neighborhood. At \(x\in M_F\), retain the actual \(r\)-by-\(D\) matrix


```{=latex}
\begin{equation}
L_x=D(\kappa_-F)_x.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.10}
\end{equation}
```


It has full row rank. The ordered inverse-image normal frame is the matrix


```{=latex}
\begin{equation}
E_F=L^{\mathsf T}(LL^{\mathsf T})^{-1}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.11}
\end{equation}
```


Indeed \(LE_F=I_r\), every column lies in \((\ker L)^\perp\), and that orthogonal complement has dimension \(r\). Hence \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.11} is exactly the inverse of \(L\) on the Euclidean normal bundle. Its full Gram matrix and the normal projection are


```{=latex}
\begin{equation}
G_F=E_F^{\mathsf T}E_F=(LL^{\mathsf T})^{-1},
 \qquad
 P_F=E_FL=L^{\mathsf T}(LL^{\mathsf T})^{-1}L.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.12}
\end{equation}
```


Matrix multiplication gives \(P_F^2=P_F=P_F^{\mathsf T}\). Smoothness follows from the everywhere invertible \(LL^{\mathsf T}\). In the target's ambient tangent coordinates the original frame is \((2e_\ell,0)\), so \(DF(E_{F,\ell})=(2e_\ell,0)\), retaining the factor in Section 3.

For a transverse homotopy \(\mathcal H\), the same construction gives


```{=latex}
\begin{equation}
W=\mathcal H^{-1}(q_-)\subset\mathbb R^D\times[0,1],
 \qquad
 L_W=\bigl[D_x(\kappa_-\mathcal H)\ \ 
                    \partial_t(\kappa_-\mathcal H)\bigr],
 \qquad
 E_W=L_W^{\mathsf T}(L_WL_W^{\mathsf T})^{-1}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.13}
\end{equation}
```


The compactness argument is uniform along the entire basepoint line. On each endpoint collar the last column of \(L_W\) is zero, so \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.13} is exactly \((E_{F_i},0)^{\mathsf T}\). Its inverse image is exactly \(M_{F_i}\times[0,\delta_i)\), or the corresponding upper collar. Thus \(W\) has precisely the product collars \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.2}, and the orientation computation \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.8}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.9} applies without any new sign choice.

In particular, if the endpoints are the original collapse maps of \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-3}, their recovered endpoint frames are the original \(E_i\): both \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.11} and \(E_i\) lie in the normal bundle and are right inverses to the same \(L_i\), whose restriction to that bundle is an isomorphism. This proves equality of the matrices, not only equality up to a change of frame. A based homotopy between the original collapse maps therefore gives an actual embedded framed bordism with exactly those endpoint frames.

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-inverse-tube-comparison}

\subsection{A transverse map is homotopic to the collapse of its own inverse image}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-6}\label{courseIII:pontryagin-thom:6}

Keep the actual \(F,M_F,E_F,G_F\) of \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-5}; write them \(F,M,E,G\) within this section. Choose an original valid linear tube


```{=latex}
\begin{equation}
\Gamma(m,A)=j(m)+E(m)A
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.1}
\end{equation}
```


as in \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-3}, where now \(j\) is the actual inclusion of \(M=F^{-1}(q_-)\) in \(\mathbb R^D\). Retain any specified collapse radius \(\epsilon\) with a larger valid tube. We construct a homotopy to that particular collapse.

Near the zero section define the full coordinate function


```{=latex}
\begin{equation}
\Phi(m,A)=\kappa_-F(\Gamma(m,A)).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.2}
\end{equation}
```


It satisfies \(\Phi(m,0)=0\), \(D_A\Phi(m,0)=I_r\), and \(D_m\Phi(m,0)=0\). Compactness permits a single \(b>0\) such that \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.2} is defined for \(\|A\|<2b\) and


```{=latex}
\begin{equation}
\|D_A\Phi(m,A)-I_r\|<\tfrac12
       \quad\hbox{for every }m,\ \|A\|\leq b.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.3}
\end{equation}
```


In particular \(\|\Phi(m,A)-A\|\leq\|A\|/2\). For each \(\|z\|<b/2\), the iteration of


```{=latex}
\begin{equation}
A\longmapsto z-\bigl(\Phi(m,A)-A\bigr)
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.4}
\end{equation}
```


maps the closed ball \(\|A\|\leq b\) to itself and is a contraction with ratio less than \(1/2\). Its geometric difference estimate proves existence and uniqueness of a fixed point \(a(m,z)\), with \(\|a(m,z)\|\leq2\|z\|<b\). The inverse function theorem then proves smooth dependence on \(m,z\). On overlapping original charts these solutions agree by uniqueness. Their exact derivatives are


```{=latex}
\begin{equation}
D_za=(D_A\Phi)^{-1},\qquad
 D_ma=-(D_A\Phi)^{-1}D_m\Phi,
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.5}
\end{equation}
```


evaluated at \((m,a(m,z))\). Define


```{=latex}
\begin{equation}
T(m,z)=\Gamma(m,a(m,z)).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.6}
\end{equation}
```


This is an actual tube with \(F(T(m,z))=\sigma(z)\), \(T(m,0)=j(m)\), \(D_zT(m,0)=E(m)\). Its full derivative, before restricting to the zero section, is


```{=latex}
\begin{equation}
DT(v,B)=Jv+(DE[v])a+
             E(D_A\Phi)^{-1}\bigl(B-D_m\Phi(v)\bigr).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.7}
\end{equation}
```


No derivative of the original frame or of \(F\) is discarded.

For a sufficiently small \(\delta>0\), the *entire* inverse image of the target ball \(\sigma(B_\delta^r)\) is \(T(M\times B_\delta^r)\). To prove the assertion globally, take the complement in the compact sphere \(S^D\) of \(\Gamma(M\times B_{b/2}^r)\). It is compact and contains no inverse image of \(q_-\). Its image under \(F\) therefore has a positive distance from \(q_-\). Choose \(\delta<b/4\) so that the closure of \(\sigma(B_\delta^r)\) misses that image. Every inverse image then has \(\|A\|<b/2\), and the uniqueness in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.4} identifies it with \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.6}. Conversely every point of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.6} has the required image by its defining equation. This proves both inclusions, including exclusion of extra components.

Here is an explicit target homotopy that discards only values outside that ball and retains the derivative at \(q_-\). Parameterize the original unit target sphere by


```{=latex}
\begin{equation}
(Y,t)=(\sin\theta\,u,-\cos\theta),\quad
       0\leq\theta\leq\pi,\quad u\in S^{r-1},\qquad
 z=\tan(\theta/2)u.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.8}
\end{equation}
```


At the two poles the value is independent of \(u\). Set \(\theta_\delta=2\arctan\delta\), and define


```{=latex}
\begin{equation}
B_\delta(\theta)=
 \begin{cases}
 2\arctan\!\left[
 \tan(\theta/2)
 \exp\!\left(\dfrac{\tan^2(\theta/2)}
                   {\delta^2-\tan^2(\theta/2)}\right)\right],
                                  &0\leq\theta<\theta_\delta,\\
 \pi,                            &\theta_\delta\leq\theta\leq\pi.
 \end{cases}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.9}
\end{equation}
```


The difference \(\pi-B_\delta\) is smooth and flat at \(\theta_\delta\): use
\( \pi-2\arctan v=2\arctan(v^{-1})\) for \(v>0\) and the exponential estimate \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.11}. Near zero \(B_\delta\) is a smooth odd function of \(\theta\), with derivative one; near \(\pi\) it is constant. Thus


```{=latex}
\begin{equation}
\theta_s=(1-s)\theta+sB_\delta(\theta),\qquad
 c_s(\sin\theta\,u,-\cos\theta)
                =(\sin\theta_s\,u,-\cos\theta_s)
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.10}
\end{equation}
```


defines a jointly smooth based homotopy, including both poles. More explicitly near zero, \(\sin\theta_s/\sin\theta\) is a smooth function of \(\theta^2\), and \(\cos\theta_s\) is smooth in \(\theta^2\); near the other pole use \(v=\pi-\theta\) and
\(\pi-\theta_s=(1-s)v\). These expressions prove smoothness in the original Cartesian sphere charts, also for \(r=1\).

We have \(c_0=1\), and in the chart \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.13},


```{=latex}
\begin{equation}
c_1(\sigma(z))=
 \begin{cases}
 \sigma\!\left(\exp\!\left(\dfrac{z^{\mathsf T}z}
                                  {\delta^2-z^{\mathsf T}z}\right)z\right),
                                           &\|z\|<\delta,\\
 q_+,                                      &\|z\|\geq\delta.
 \end{cases}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.11}
\end{equation}
```


At every time, the only inverse image of \(q_-\) under \(c_s\) is \(q_-\), and its derivative in the original \(z\)-coordinates is \(I_r\). Consequently \(c_sF\) keeps the exact inverse-image frame \(E\). At \(s=1\), \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.11} and the proved global inverse-image equality show that \(c_1F\) is precisely the collapse constructed in the curved tube \(T\) with the displayed coordinate radius \(\delta\).

Next compare that tube to the original linear tube, retaining the frame throughout. In the actual ambient coordinate space define


```{=latex}
\begin{equation}
T_s(m,z)=(1-s)T(m,z)+s\Gamma(m,z),\quad 0\leq s\leq1.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.12}
\end{equation}
```


At \(z=0\) its value is \(j(m)\) and its derivative is \([J,E]\), independently of \(s\). These matrices are invertible. Compactness of \(M\times[0,1]\), the local inverse function theorem with parameter, and the collision-sequence argument of \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-3} give one radius on which *every* \(T_s\) is a tube. In that last argument a putative sequence of collisions also has a convergent parameter subsequence \(s_\nu\to s_*\); the parameter-dependent local inverse at \((m,0,s_*)\) contradicts the collisions. Reduce \(\delta\), if needed, so that all \(T_s\) are valid on \(M\times B_{2\delta}^r\). This reduction is made before \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.9} is used. Formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.11} in the coordinates \(T_s\), extended by \(q_+\), is now a smooth based homotopy of collapse maps. Smoothness with parameter at its boundary follows from the larger tubes and the same flat exponential. Its full tube differential is


```{=latex}
\begin{equation}
dT_s=(1-s)\,DT+s\,D\Gamma+(\Gamma-T)\,ds.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.13}
\end{equation}
```


Every endpoint and every frame derivative in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.7}, \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.13} remains part of this comparison.

Finally compare the coordinate ball to the original ellipsoid. Make the preceding \(\delta\) still smaller so that


```{=latex}
\begin{equation}
\delta^2\max_{m\in M}\lambda_{\max}(G(m))\leq\epsilon^2.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.14}
\end{equation}
```


In the fixed original tube \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.1}, put


```{=latex}
\begin{equation}
B_s(m)=(1-s)\frac{I_r}{\delta^2}
                         +s\frac{G(m)}{\epsilon^2},
 \qquad q_s(m,A)=A^{\mathsf T}B_s(m)A.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.15}
\end{equation}
```


Every \(B_s\) is positive definite. Condition \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.14} implies
\(B_s\geq G/\epsilon^2\), so \(q_s<1\) stays inside the original valid \(\epsilon\)-tube. Use


```{=latex}
\begin{equation}
Z_s=\exp\!\left(\frac{q_s}{1-q_s}\right)A
       \quad(q_s<1),\qquad \mathcal P_s=q_+\quad(q_s\geq1),
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.16}
\end{equation}
```


with \(\mathcal P_s(\Gamma(m,A))=\sigma(Z_s)\) on the first region. This is jointly smooth by flatness, with uniform positive eigenvalue bounds for \(B_s\). It begins at the linear coordinate-ball collapse and ends at exactly \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.8}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.9} with the original \(G,\epsilon\). The complete differentials are


```{=latex}
\begin{equation}
\begin{aligned}
 dq_s&=2A^{\mathsf T}B_s\,dA+A^{\mathsf T}(dB_s)A,\\
 dB_s&=\frac{s}{\epsilon^2}\,dG+
             \left(\frac{G}{\epsilon^2}
                         -\frac{I_r}{\delta^2}\right)ds,\\
 dZ_s&=\exp\!\left(\frac{q_s}{1-q_s}\right)
               \left(dA+\frac{A\,dq_s}{(1-q_s)^2}\right).
 \end{aligned}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.17}
\end{equation}
```


The original \(\epsilon,\delta\) are fixed in this interpolation; their separate radius variation, when required, is exactly \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.7}. Equations \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.15}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.17} are the proved comparison between the two fiber domains and their full formulas.

Concatenate \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.10}, \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.12} and \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.16}, using smooth parameter functions constant near the joins. This proves that the original transverse map \(F\) is based homotopic to the collapse of its own actual framed inverse image, with its originally specified linear tube and radius.

If \(M\) is empty, compactness gives a target ball about \(q_-\) missed by all of \(F\). Then \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.10} makes \(F\) constant at \(q_+\), and the collapse of the empty manifold is that same constant map. This includes the empty case of the inverse assertion.

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-bijection}

\subsection{The two constructions are inverse in each stated ambient dimension}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-7}\label{courseIII:pontryagin-thom:7}

Let \(\mathcal B_{n,r}\) denote the set of compact smooth \(n\)-submanifolds without boundary in \(\mathbb R^{n+r}\), each with an ordered Euclidean normal frame of rank \(r\), modulo the embedded framed bordisms of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.1}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.2}. Reparametrizing product collars allows smooth concatenation of two bordisms; the constant cylinder supplies reflexivity. Reversing the height parameter and transporting its full normal vectors by \((x,t)\mapsto(x,1-t)\) supplies symmetry. Thus this is an equivalence relation. The induced boundary orientation is always the one calculated in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.8}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.9}.

The collapse construction and the regular-inverse-image construction give mutually inverse maps


```{=latex}
\begin{equation}
\mathcal B_{n,r}\ \underset{\mathcal R}{\overset{\mathcal P}{\rightleftarrows}}\
                  [S^{n+r},S^r]_* ,\qquad r\geq1.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:7.1}
\end{equation}
```


Here the bracket denotes continuous based homotopy classes with the specified basepoints, and the normal frame in \(\mathcal R\) is exactly \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.11}. We verify every choice and composite.

For \(\mathcal P\), two valid collapse radii give homotopic maps by \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.7}. A framed bordism gives a based homotopy by Section 4. The linear tube is determined by the given embedding and full normal frame; the construction makes no additional choice of orthonormal frame. Hence \(\mathcal P\) is well-defined.

For \(\mathcal R\), equations \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.1}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.8} give a smooth transverse representative of any based class. Two such representatives of one class have a continuous based homotopy. Apply \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.2}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.5} relative its smooth endpoint collars, and then \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.6}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.8} relative those collars. The inverse image \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.13} is an embedded framed bordism with precisely their frames \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.11}. Thus both approximation and transverse-parameter choices give the same element of \(\mathcal B_{n,r}\), and \(\mathcal R\) is well-defined.

The composite \(\mathcal R\mathcal P\) recovers the original submanifold as a set and as an embedded smooth manifold, and recovers every original frame vector by \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.14} and the uniqueness after \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.13}. Therefore this composite is the identity. The other composite is the identity by the three explicit homotopies of Section 6. This proves \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:7.1}.

The based null-homotopy case will be used directly later. If the collapse of a particular original \((M,E)\) is null-homotopic, \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-5} applied to a homotopy to the constant \(q_+\) map gives a compact embedded \((n+1)\)-manifold with one boundary component, whose normal frame extends exactly \(E\). Conversely such a framed bounding manifold gives a null-homotopy by \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-4} with an empty upper endpoint. This statement retains the original boundary embedding, collar and frame; it does not infer a bounding manifold merely from stable parallelizability.

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-stabilization-and-original-framing}

\subsection{Suspension, stable bounding and the original complex tangent framing}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-8}\label{courseIII:pontryagin-thom:8}

We specify the suspension coordinates before identifying its inverse image. The one-point compactification of a product has the exact based homeomorphism


```{=latex}
\begin{equation}
(\mathbb R^D\times\mathbb R)^+
       \longrightarrow(\mathbb R^D)^+\wedge\mathbb R^+.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.1}
\end{equation}
```


It takes each finite \((x,u)\) to its two classes and takes the added point to the collapsed wedge. The quotient of the compact product on the right by its closed wedge is compact Hausdorff; its complement is exactly \(\mathbb R^D\times\mathbb R\). The displayed bijection is continuous, including the added point because complements of neighborhoods there are compact subsets of that complement. This proves \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.1} as a homeomorphism. The order of the new coordinate is spatial \(x\), then \(u\).

Identify the target \((\mathbb R^r)^+\) with the original unit \(S^r\) by \(\sigma\). For a based map \(F\), its reduced suspension, in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.1}, is represented by


```{=latex}
\begin{equation}
\widehat{\Sigma F}(x,u)=
 \begin{cases}
 \sigma_{r+1}\bigl(Q(x),u\bigr),&
          F(x)\ne q_+,\quad Q=\kappa_-F,\\
 q_+,&F(x)=q_+,
 \end{cases}
 \qquad
 \widehat{\Sigma F}(\infty)=q_+.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.2}
\end{equation}
```


Here \(\sigma_{r+1}\) is the full formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.7} in \(r+1\) coordinates; in particular its denominator is
\(1+Q^{\mathsf T}Q+u^2\). Formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.2} is the smash of the given \(F\) and the identity of \(\mathbb R^+\), so it represents the original suspension homomorphism, with no coordinate permutation.

It is also useful to check continuity and finite-coordinate smoothness directly. As \(F(x)\to q_+\) through the other chart, \(\|Q\|\to\infty\). As \(|u|\to\infty\), the last coordinate already forces \(\|(Q,u)\|\to\infty\). For any fixed bound on \(\|Q\|\), its possible source points form a compact set away from the based point, since \(F(\infty)=q_+\). These observations prove continuity at the collapsed points and at infinity. Near a finite point with \(F(x)=q_+\), use the actual \(w=\kappa_+F(x)\). The target north-chart coordinate of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.2} is exactly


```{=latex}
\begin{equation}
\left(\frac{w}{1+u^2w^{\mathsf T}w},
       \frac{u\,w^{\mathsf T}w}{1+u^2w^{\mathsf T}w}\right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.3}
\end{equation}
```


The denominator is at least one. This proves smoothness across \(w=0\). For example with \(v=w^{\mathsf T}w\), \(a=1+u^2v\), the full differential is


```{=latex}
\begin{equation}
dv=2w^{\mathsf T}dw,\quad da=2uv\,du+u^2\,dv,\quad
 d\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.3}=
 \left(\frac{dw}{a}-\frac{w\,da}{a^2},
       \frac{v\,du+u\,dv}{a}-\frac{uv\,da}{a^2}\right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.4}
\end{equation}
```


At the source point at infinity only continuity is required for the suspension class. The relative procedure \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.2}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.5} makes a smooth representative constant near that point while leaving the whole regular-inverse-image neighborhood unchanged.

For transverse \(F\), the inverse image of the target's specified south pole under \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.2} is exactly \(M_F\times\{0\}\). In its target south coordinates the derivative is


```{=latex}
\begin{equation}
\begin{pmatrix}L&0\\0&1\end{pmatrix}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.5}
\end{equation}
```


Consequently the recovered original normal frame, Gram matrix and linear-tube squared length are


```{=latex}
\begin{equation}
E^+=
 \begin{pmatrix}E&0\\0&1\end{pmatrix},\qquad
 G^+=\begin{pmatrix}G&0\\0&1\end{pmatrix},\qquad
 \rho^+(m,A,u)=A^{\mathsf T}G(m)A+u^2.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.6}
\end{equation}
```


This keeps the old \(G\) and appends the specified unit coordinate. The ambient tangent target factor is again two for every coordinate. The frame order is \(E_1,\ldots,E_r,e_u\); the source orientation order is the old spatial orientation followed by \(u\), so no permutation sign occurs here. Applying \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-6} to the smoothed \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.2} proves that it is homotopic to the collapse with this exact frame and any specified valid radius. In particular \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:7.1} commutes with suspension and the geometric operation \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.6}.

Define the stable group in degree \(n\geq0\) by the directed limit


```{=latex}
\begin{equation}
\pi_n^{\,S}=\underset{r\longrightarrow\infty}{\operatorname{colim}}\,
                   \pi_{n+r}(S^r),
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.7}
\end{equation}
```


where the transition maps are precisely \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.2}. One may begin with \(r\geq2\), where the homotopy groups in this limit are abelian; dropping finitely many initial terms changes no directed limit. We use no stable-range theorem to replace this limit by a particular finite term. A class represented at rank \(r\) equals zero in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.7} exactly when its image after some finite number \(s\geq0\) of these transitions is zero. This follows from the definition of the directed-limit equivalence: representatives \(a_r,b_t\) are equivalent precisely when their images agree at some common finite stage. The usual group law is compatible with these transitions because the two hemispheres defining addition suspend to the corresponding two pieces of the suspended source; the common boundary still maps to the basepoint.

Combining that definition with \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:7.1}, \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.5} and \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.6} proves the exact geometric assertion needed here:


```{=latex}
\begin{equation}
\begin{gathered}
 \bigl[\mathcal P(M,E)\bigr]=0\text{ in }\pi_n^{\,S}
 \\
 \Longleftrightarrow
 \\
 (M\times\{0\},E\oplus I_s)
 \text{ bounds an embedded framed manifold}
 \\
 \text{for some finite }s.
 \end{gathered}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.8}
\end{equation}
```


The ambient boundary space on the right is \(\mathbb R^{n+r+s}\), and the bounding manifold lies in its product with \([0,1]\), with the original \(M\) at height zero and an empty upper boundary. Thus the notation \(M\times\{0\}\) in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.8} uses exactly \(s\) appended zero coordinates. Both directions are actual constructions: suspend, use \cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-5} on a null-homotopy, or collapse the bounding manifold and use Section 4. No existence of a stable null-homotopy is asserted by \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.8} without its calculation.

We finally prove the comparison back to the original tangent framing for the particular complex manifold in lesson 7. First record this comparison for arbitrary data \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.2}. The normal frame \(E\) of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.7} gives a stable tangent framing


```{=latex}
\begin{equation}
\begin{aligned}
 \tau_E:T_mM\oplus\mathbb R^N\oplus\mathbb R^k
       &\longrightarrow \mathbb R^N\oplus\mathbb R^{n+k},\\
 \tau_E(v,a,b)&=
 \left(Jv+P_\nu a,\
             \tau\bigl(H^{-1}J^{\mathsf T}a,b\bigr)\right).
 \end{aligned}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.9}
\end{equation}
```


This is the full tangent-plus-normal map \(Dj'(v)+E(a,b)\), using \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.5}. Define also the specified stabilization of the original framing


```{=latex}
\begin{equation}
\tau_{\mathrm{st}}(v,a,b)=(a,\tau(v,b)).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.10}
\end{equation}
```


The coordinate orders in these two formulas agree. Put \(Q=H^{-1}J^{\mathsf T}\), so \(QJ=I\), \(QP_\nu=0\), and \(P_\nu+JQ=I_N\). The exact comparison is


```{=latex}
\begin{equation}
S_m(v,a,b)=(Qa,\ P_\nu a+Jv,\ b),\qquad
 S_m^2=I,\qquad
 \tau_E=\tau_{\mathrm{st}}S_m.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.11}
\end{equation}
```


Each equality follows by substituting these three matrix identities. Relative to the decomposition \(a=P_\nu a+JQa\), the map \(S_m\) exchanges the two \(n\)-dimensional tangent summands and fixes every other summand. Its determinant sign is therefore \((-1)^n\). In general an orientation calculation alone would not make this bundle automorphism homotopic to the identity.

For the original \(M=X\), retain its original almost-complex tangent operator \(\mathcal J\), with \(\mathcal J^2=-I\). It is provided by the original complex charts, independently of the later smooth-sphere recognition. This gives the following explicit homotopy, which proves the additional comparison we actually need. For \(0\leq t\leq1\), put \(\theta=\pi t/2\), \(\varphi=\pi t\), \(u=Qa\), \(y=P_\nu a\), and set


```{=latex}
\begin{equation}
\begin{aligned}
 C_\varphi&=\cos\varphi\,I+\sin\varphi\,\mathcal J,\qquad
       C_\varphi^{-1}=\cos\varphi\,I-\sin\varphi\,\mathcal J,\\
 v_t&=\cos\theta\,v+\sin\theta\,u,\\
 a_t&=y+J C_\varphi(-\sin\theta\,v+\cos\theta\,u),\\
 S_{m,t}(v,a,b)&=(v_t,a_t,b).
 \end{aligned}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.12}
\end{equation}
```


Multiplication gives the displayed inverse of \(C_\varphi\), since \(\mathcal J^2=-I\). The rotation on the ordered pair \((v,u)\), then \(C_\varphi\) on its second component, then the original splitting \(a=y+Ju\), are all isomorphisms. Thus every \(S_{m,t}\) is invertible. At \(t=0\) it is the identity; at \(t=1\), \(v_t=u\) and \(C_\pi(-v)=v\), so it is exactly \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.11}. All coefficients are smooth in \(m,t\), and the original \(J,H,\mathcal J\) make the formula agree in overlapping original charts. We have proved the actual framing homotopy


```{=latex}
\begin{equation}
\tau_{\mathrm{st}}S_{m,t}:\quad
                  \tau_{\mathrm{st}}\simeq\tau_E.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.13}
\end{equation}
```


This comparison uses the original almost-complex structure at an explicit point in the proof. The \cref{courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-general-stable-framing} now proves the same endpoint homotopy for every stably framed six-manifold, after at most one further specified identity coordinate. It uses the original stable frame on the even-rank bundle, constructs its full rotation and cancels the auxiliary minus signs with a second explicit rotation. Its equations (7.9)–(7.19) retain this chapter's original J, H, Q, normal projection and both framing maps. That independent bundle calculation supplies the full tangent-framed bordism use of the normal-framed bijection; the original complex-specific homotopy \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.12} remains unchanged. For example the full variation of its extra factor is


```{=latex}
\begin{equation}
dC_\varphi=
 (-\sin\varphi\,I+\cos\varphi\,\mathcal J)\,d\varphi
                                      +\sin\varphi\,d\mathcal J,
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.14}
\end{equation}
```


and the derivative of \(a_t=y+JC_\varphi(-\sin\theta v+\cos\theta u)\) includes \(dy\), \(dJ\), \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.14}, and the full derivative of the last parenthesis. Thus the varying original complex operator is retained, not treated as a constant matrix.

For completeness, a normal-framed bounding manifold obtained in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.8} has an actual stable tangent framing. If \(K\) is a matrix of its tangent inclusion in the ambient \(\mathbb R^{n+r+s}\times\mathbb R\), and \(E_W\) its normal frame, the isomorphism and its inverse are


```{=latex}
\begin{equation}
(v,A)\longmapsto Kv+E_WA,\qquad
 z\longmapsto
 \left((K^{\mathsf T}K)^{-1}K^{\mathsf T}z,\
       (E_W^{\mathsf T}E_W)^{-1}E_W^{\mathsf T}z\right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.15}
\end{equation}
```


Here \(K^{\mathsf T}E_W=0\), so direct multiplication proves both composites. The formulas are independent of tangent chart choices by the same calculation as \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.8}.

On its product boundary collar, write a tangent vector as \(v+a\,\partial_t\). Formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.15} becomes


```{=latex}
\begin{equation}
(v+a\,\partial_t,A)\longmapsto
                         \bigl(Dj(v)+(E\oplus I_s)A,\ a\bigr).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.16}
\end{equation}
```


The spatial-then-time order is shown explicitly. Reordering it to time-first multiplies the orientation by \((-1)^{n+r+s}\), exactly as in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.8}. The lower boundary orientation is \(-M\) as a cobordism from \(M\) to the empty manifold; forgetting that incoming-versus-outgoing convention leaves the specified underlying framed boundary identification unchanged. Equation \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.16} restricts to \(\tau_E\) with the \(s\) added factors and the displayed collar line. Reverse the parameter in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.13}, make it constant near both ends, and use it on a smaller collar. This changes the boundary framing to the specified stabilization \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.10} of the original \(\tau\), while retaining the framing on the rest of the bounding manifold. At the outer seam it equals the old frame on a whole neighborhood, so it pastes smoothly. The same argument applies after every appended identity factor.

Consequently the framed bounding construction, when the stable class of the actual collapse has been proved zero, receives the original complex six-manifold and its original stable tangent framing. Its input is not merely an abstract manifold with an unspecified stable trivialization.

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-worked-exercises}

\subsection{Two complete worked exercises}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-9}

\subsubsection{Exercise 9.1. A sheared original frame on a circle}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:exercise-9.1}\label{courseIII:pontryagin-thom:9.1}

Fix \(a,b,d>0\) and \(c\in\mathbb R\). Embed the original circle by \(j(\theta)=(a\cos\theta,a\sin\theta,0)\), and prescribe the ordered normal frame


```{=latex}
\begin{equation}
E_1=(b\cos\theta,b\sin\theta,0),\qquad
 E_2=(c\cos\theta,c\sin\theta,d).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.1}
\end{equation}
```


Compute the complete tube, its inverse, the inverse-image framing matrix, the Gram condition and the orientation. Determine the collapse derivative and a valid original radius.

**Solution.** Write \(R=a+bA_1+cA_2\). The actual tube is


```{=latex}
\begin{equation}
\Gamma(\theta,A_1,A_2)
       =(R\cos\theta,R\sin\theta,dA_2),\qquad
 G=\begin{pmatrix}b^2&bc\\bc&c^2+d^2\end{pmatrix}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.2}
\end{equation}
```


Its original squared normal length is


```{=latex}
\begin{equation}
\rho=b^2A_1^2+2bcA_1A_2+(c^2+d^2)A_2^2
                   =(bA_1+cA_2)^2+d^2A_2^2.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.3}
\end{equation}
```


In particular \(G\) is positive definite: its first principal minor is \(b^2>0\), and its determinant is \(b^2d^2>0\). The mixed term is present whenever \(c\ne0\).

Choose \(0<\epsilon<a/2\). On \(\rho<(2\epsilon)^2\), we have \(|bA_1+cA_2|<2\epsilon<a\), so \(R>0\). For an image point \((x,y,z)\), the inverse coordinates are


```{=latex}
\begin{equation}
\begin{aligned}
 R&=\sqrt{x^2+y^2},\qquad
 (\cos\theta,\sin\theta)=(x/R,y/R),\\
 A_2&=z/d,\qquad
 A_1=\frac{R-a-cz/d}{b}.
 \end{aligned}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.4}
\end{equation}
```


The angular statement is a smooth circle-valued inverse, with the usual local angular charts where a single real angle is needed. Substitution of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.4} into \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.2} and the reverse substitution both give the identity. Thus this is an actual tube on the larger radius required in Section 3. The original \(\rho\) becomes \((R-a)^2+z^2\) *under the displayed map*; \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.3} remains its complete expression in the given frame coordinates.

Differentiate \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.4} on the zero section. The two rows of the inverse-image matrix are


```{=latex}
\begin{equation}
L=
 \begin{pmatrix}
  \cos\theta/b&\sin\theta/b&-c/(bd)\\
  0&0&1/d
 \end{pmatrix},
 \qquad
 LL^{\mathsf T}=
 \begin{pmatrix}
 (c^2+d^2)/(b^2d^2)&-c/(bd^2)\\
 -c/(bd^2)&1/d^2
 \end{pmatrix}=G^{-1}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.5}
\end{equation}
```


Matrix multiplication gives \(LE=I_2\) and
\(L(-a\sin\theta,a\cos\theta,0)^{\mathsf T}=0\). The columns of \(E\) are perpendicular to that tangent. Therefore \(L^{\mathsf T}(LL^{\mathsf T})^{-1}=E\), recovering exactly the two vectors in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.1}, including \(b,c,d\).

The full tube derivative has columns


```{=latex}
\begin{equation}
\left[
 \begin{pmatrix}-R\sin\theta\\R\cos\theta\\0\end{pmatrix},
 \begin{pmatrix}b\cos\theta\\b\sin\theta\\0\end{pmatrix},
 \begin{pmatrix}c\cos\theta\\c\sin\theta\\d\end{pmatrix}
 \right],
 \qquad \det D\Gamma=-Rbd.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.6}
\end{equation}
```


It is invertible on the whole stated tube. At the zero section the determinant is \(-abd<0\). Consequently the inverse-image orientation defined by tangent-then-\((E_1,E_2)\) is the *negative* of increasing \(\theta\). This sign is part of the framed example.

On \(\rho<\epsilon^2\), put
\(\lambda=\exp(\rho/(\epsilon^2-\rho))\). The actual target map is


```{=latex}
\begin{equation}
\mathcal P(\Gamma)=
 \left(
 \frac{2\lambda A_1}{1+\lambda^2(A_1^2+A_2^2)},
 \frac{2\lambda A_2}{1+\lambda^2(A_1^2+A_2^2)},
 \frac{\lambda^2(A_1^2+A_2^2)-1}
      {1+\lambda^2(A_1^2+A_2^2)}
 \right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.7}
\end{equation}
```


Outside that tube it is \(q_+\). At \(A=0\), its derivative on an ambient source vector \(v\) is


```{=latex}
\begin{equation}
D\mathcal P(v)=\bigl(2(Lv)_1,2(Lv)_2,0\bigr).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.8}
\end{equation}
```


Equations \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.5}, \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.8} give \(D\mathcal P(E_1)=(2,0,0)\) and \(D\mathcal P(E_2)=(0,2,0)\). Along the entire boundary \(\rho=\epsilon^2\), formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.10} proves the smooth extension to \(q_+\). No factor of the sheared frame, its mixed Gram term, or the target tangent factor two is lost.

\subsubsection{Exercise 9.2. The tangent-framing comparison with nonorthogonal matrices}
\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:exercise-9.2}\label{courseIII:pontryagin-thom:9.2}

At one tangent fiber retain the coordinate matrices


```{=latex}
\begin{equation}
J=\begin{pmatrix}2&0\\0&3\\1&1\end{pmatrix},\qquad
 \tau=\begin{pmatrix}2&1&0\\0&3&1\\1&0&2\end{pmatrix},
 \qquad
 \mathcal J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.9}
\end{equation}
```


Here \(n=2,N=3,k=1\); the last input of \(\tau\) is the original stable line. Calculate the complete \(E,G\), prove \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.11}, and give the derivative of the homotopy \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.12} in its parameter with the fiber held fixed.

**Solution.** Direct products give


```{=latex}
\begin{equation}
\begin{gathered}
 H=\begin{pmatrix}5&1\\1&10\end{pmatrix},\quad
 H^{-1}=\frac1{49}\begin{pmatrix}10&-1\\-1&5\end{pmatrix},\\
 Q=\frac1{49}\begin{pmatrix}20&-3&9\\-2&15&4\end{pmatrix},\qquad
 P_\nu=\frac1{49}\begin{pmatrix}9&6&-18\\6&4&-12\\-18&-12&36\end{pmatrix}.
 \end{gathered}
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.10}
\end{equation}
```


For instance \(P_\nu=vv^{\mathsf T}/49\) with \(v=(-3,-2,6)^{\mathsf T}\), where \(v^{\mathsf T}v=49\) and \(J^{\mathsf T}v=0\). Hence \(P_\nu^2=P_\nu\), \(P_\nu J=0\), and the displayed \(Q\) has \(QJ=I_2\), \(QP_\nu=0\), \(JQ+P_\nu=I_3\).

Equation \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.5}, retaining \(\tau\) and its stable column, gives


```{=latex}
\begin{equation}
E=\frac1{49}
 \begin{pmatrix}
 9&6&-18&0\\
 6&4&-12&0\\
 -18&-12&36&0\\
 38&9&22&0\\
 -6&45&12&49\\
 20&-3&9&98
 \end{pmatrix},\qquad
 G=\frac1{2401}
 \begin{pmatrix}
 2321&306&62&1666\\
 306&2311&123&1911\\
 62&123&2473&1470\\
 1666&1911&1470&12005
 \end{pmatrix}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.11}
\end{equation}
```


The second matrix is the product \(E^{\mathsf T}E\), with every off-diagonal entry retained. Its determinant is \(169/49>0\). More directly, \(\det\tau=13\ne0\), and the exact inverse in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.4} shows that \(E\) has full column rank; hence \(A^{\mathsf T}GA=\|EA\|^2>0\) for \(A\ne0\). This proves positive definiteness without mistaking a positive determinant alone for that property.

The matrix of \(S\), in the original order \(v\in\mathbb R^2,a\in\mathbb R^3,b\in\mathbb R\), is


```{=latex}
\begin{equation}
S=\begin{pmatrix}
 0_{2\times2}&Q&0\\
 J&P_\nu&0\\
 0&0&1
 \end{pmatrix}.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.12}
\end{equation}
```


Squaring gives diagonal blocks \(QJ=I_2\), \(JQ+P_\nu^2=I_3\), \(1\), and off-diagonal blocks \(QP_\nu=0,P_\nu J=0\). Thus \(S^2=I_6\). Applying \(\tau_{\mathrm{st}}\) gives


```{=latex}
\begin{equation}
\tau_{\mathrm{st}}S(v,a,b)
       =(P_\nu a+Jv,\tau(Qa,b))=\tau_E(v,a,b).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.13}
\end{equation}
```


The exchange of two two-dimensional summands has sign \((-1)^2=+1\); the formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.12}, using the actual \(\mathcal J\) in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.9}, proves the stronger assertion that \(S\) is connected to the identity through the displayed invertible matrices.

For its derivative write


```{=latex}
\begin{equation}
U=\cos\theta\,v+\sin\theta\,u,\qquad
 V=-\sin\theta\,v+\cos\theta\,u,\qquad u=Qa.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.14}
\end{equation}
```


Since \(\theta'=\pi/2\), \(\varphi'=\pi\), we have


```{=latex}
\begin{equation}
U'=\tfrac\pi2 V,\qquad V'=-\tfrac\pi2 U,\qquad
 C_\varphi'=\pi\mathcal J C_\varphi.
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.15}
\end{equation}
```


The last equality follows by multiplying \(\mathcal J(\cos\varphi I+\sin\varphi\mathcal J)\) and using \(\mathcal J^2=-I\). The full parameter derivative at this fixed fiber is therefore


```{=latex}
\begin{equation}
\frac{d}{dt}S_{m,t}(v,a,b)=
 \left(\tfrac\pi2 V,\
   J\left[\pi\mathcal J C_\varphi V
                      -\tfrac\pi2 C_\varphi U\right],\
   0\right).
 \label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.16}
\end{equation}
```


If the basepoint \(m\) varies too, the additional \(dJ,dQ,dP_\nu,d\mathcal J\) terms are exactly those of \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.12}, \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.14}; \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.16} asserts only the specified parameter derivative. The original coordinate matrices in \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.9} need not be orthogonal for any of these identities.



Illustration description: The original sheared-frame ellipsoid, its exact meridian collapse on the unit target sphere, and the three explicit inverse homotopies.




The figure uses the original frame of Exercise 9.1 with the displayed constants. The left panel shows its actual Gram ellipsoid; the right is the target slice with second coordinate zero. The three marked ray parameters give numerical samples of the exact formula \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.7}. The lower row records the proved maps \eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.9}–\eqref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.17}, including the original Gram matrix and final radius. The target tangent factor two remains visible. These samples illustrate the exact proof and do not replace it.

\label{courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-sources-and-scope}

