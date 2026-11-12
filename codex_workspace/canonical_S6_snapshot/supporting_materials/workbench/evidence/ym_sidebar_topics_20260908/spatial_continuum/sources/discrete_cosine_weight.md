# Exact centered-vertex quadratic multiplier in the discrete cosine basis

This derivation proves the quadratic multiplier's uniform off-diagonal decay, including the reflection near twice the number of vertices, and to compute the fourth-moment diagonal and its exact average. No continuum replacement of the vertex coordinates is made.

Let \(L\geq0\) be an integer and let \(N=2L+1\). The vertex coordinate is the original integer \(n\in\{-L,\ldots,L\}\). Define
\[
 t_n=\frac{n+L+\tfrac12}{N}=\frac12+\frac nN,\qquad
 c_l=2-\delta_{l0},\qquad
 v_l(n)=\sqrt{\frac{c_l}{N}}\cos(\pi l t_n),
 \quad 0\leq l\leq N-1.
 \tag{D1}
\]
The real Hilbert space uses counting measure on the vertices. Define the multiplication operator
\[
 (\mathsf Z f)(n)=\left(\frac nN\right)^2f(n)
 \quad\hbox{and}\quad
 Z_{lm}=\sum_{n=-L}^L v_l(n)\left(\frac nN\right)^2v_m(n).
 \tag{D2}
\]
Consequently \(\mathsf Z^2\) is multiplication by \(n^4/N^4\), and the matrix square \(Z^2\) denotes this same operator in the orthonormal basis (D1).

## 1. Exact cosine coefficients

For an integer \(k\), put
\[
 a_k=\frac1N\sum_{n=-L}^L
       \left(\frac nN\right)^2\cos(\pi k t_n),
 \qquad
 b_k=\frac1N\sum_{n=-L}^L
       \left(\frac nN\right)^4\cos(\pi k t_n).
 \tag{D3}
\]
Both sequences are even in \(k\). Reflection \(n\mapsto-n\), which sends \(t_n\) to \(1-t_n\), gives
\[
 a_k=b_k=0\quad(k\text{ odd}).
 \tag{D4}
\]
Indeed \(\cos(\pi k(1-t))=(-1)^k\cos(\pi kt)\) for integral \(k\). Since \(Nt_n=n+L+\tfrac12\), the exact alias identities, for every integer \(k\), are
\[
 a_{k+2N}=-a_k,\quad a_{2N-k}=-a_k,\qquad
 b_{k+2N}=-b_k,\quad b_{2N-k}=-b_k .
 \tag{D5}
\]
These signs are essential. They follow by adding or subtracting \(2\pi(n+L+\tfrac12)\) inside the cosine.

The zero coefficients are
\[
 a_0=\frac{N^2-1}{12N^2},
 \qquad
 b_0=\mu_{4,N}
 =\frac{(N^2-1)(3N^2-7)}{240N^4}
 =\frac1{80}-\frac1{24N^2}+\frac7{240N^4}.
 \tag{D6}
\]
For completeness, the finite sums used here are
\[
 \sum_{n=-L}^L n^2=\frac{L(L+1)(2L+1)}3,
 \qquad
 \sum_{n=-L}^L n^4
 =\frac{L(L+1)(2L+1)(3L^2+3L-1)}{15}.
 \tag{D7}
\]
Each identity holds at \(L=0\); subtracting its right side at \(L-1\) from its right side at \(L\) gives respectively \(2L^2\) and \(2L^4\), which proves (D7) by induction. Substitution \(L(L+1)=(N^2-1)/4\) gives (D6).

For an even \(k\) with \(0<k<2N\), write
\[
 \alpha=\frac{\pi k}{2N}.
\]
Then the exact nonzero-frequency formulas are
\[
 \boxed{\displaystyle
 a_k=\frac{\cos\alpha}{2N^2\sin^2\alpha}},
 \tag{D8}
\]
\[
 \boxed{\displaystyle
 b_k=
 \frac{\cos\alpha\bigl((N^2+1)\sin^2\alpha-6\bigr)}
      {4N^4\sin^4\alpha}}.
 \tag{D9}
\]
Here and below the formulas are used only where their displayed denominators are nonzero.

To prove these formulas directly, the finite geometric sum gives the entire function
\[
 F_N(x)=\frac1N\sum_{n=-L}^Le^{ixn/N}
       =\frac{\sin(x/2)}{N\sin(x/(2N))},
 \tag{D10}
\]
where removable singularities on the right are filled using the finite sum. Write \(F_N=f g\), with \(f(x)=\sin(x/2)\) and \(g(x)=N^{-1}\csc(x/(2N))\). At \(x=2\pi r\), for \(1\leq r\leq N-1\),
\[
 f=0,\quad f'=\tfrac12(-1)^r,\quad f''=0,
 \quad f'''=-\tfrac18(-1)^r,\quad f''''=0.
\]
Termwise differentiation of the finite sum and
\(\cos(2\pi r t_n)=(-1)^r\cos(2\pi r n/N)\) therefore give
\[
 a_{2r}=(-1)^{r+1}F_N''(2\pi r)=-g'(2\pi r),
 \qquad
 b_{2r}=(-1)^rF_N''''(2\pi r)
        =2g'''(2\pi r)-\tfrac12g'(2\pi r).
 \tag{D11}
\]
The needed derivatives, with \(\alpha=x/(2N)\), are
\[
 g'(x)=-\frac{\cos\alpha}{2N^2\sin^2\alpha},
 \qquad
 g'''(x)=-\frac{\cos\alpha(6-\sin^2\alpha)}
                         {8N^4\sin^4\alpha}.
 \tag{D12}
\]
For the second identity one may differentiate
\((\csc\alpha)'=-\cos\alpha/\sin^2\alpha\) twice: the second derivative is
\((1+\cos^2\alpha)/\sin^3\alpha\), and its derivative is
\(-\cos\alpha(6-\sin^2\alpha)/\sin^4\alpha\).
Equations (D11) and (D12) prove (D8) and (D9).

## 2. Uniform matrix decay, including the reflected alias

The cosine product identity gives the exact matrix
\[
 \boxed{\displaystyle
 Z_{lm}=\frac{\sqrt{c_lc_m}}2
            \bigl(a_{l-m}+a_{l+m}\bigr)}.
 \tag{D13}
\]
In particular \(Z_{lm}=0\) whenever \(l-m\) is odd. For \(1\leq k\leq2N-1\), set
\[
 d(k)=\min(k,2N-k).
\]
For nonzero even \(k\), \(0<\pi d(k)/(2N)\leq\pi/2\), and the elementary concavity bound \(\sin u\geq 2u/\pi\) on \([0,\pi/2]\) yields
\[
 |a_k|\leq\frac1{2d(k)^2}.
 \tag{D14}
\]
The same inequality holds for odd \(k\) because its left side is zero.

Let \(\delta=|l-m|\geq1\) and \(s=l+m\). Then \(s\geq\delta\), and
\[
 2N-s-\delta=2\bigl(N-\max(l,m)\bigr)\geq2.
 \tag{D15}
\]
It follows that \(d(s)\geq\delta\). Also \(d(\delta)=\delta\), because \(0<\delta<N\). As \(\sqrt{c_lc_m}/2\leq1\), (D13)--(D15) imply
\[
 |Z_{lm}|\leq\frac1{\delta^2}\quad(l\ne m).
 \tag{D16}
\]
The diagonal obeys
\[
 0\leq Z_{ll}\leq \frac{L^2}{N^2}<\frac14
 \quad(N\geq1),
 \tag{D17}
\]
because \(v_l\) has unit norm and (D2) is nonnegative multiplication bounded above by \(L^2/N^2\). The strict final inequality also holds for \(N=1\), where the multiplier is zero.
Consequently the requested single uniform bound is
\[
 \boxed{\displaystyle
 |Z_{lm}|\leq\frac4{(1+|l-m|)^2}
 \quad(0\leq l,m<N)}.
 \tag{D18}
\]
There is no assumption that \(l+m\) stays away from \(2N\). Equation (D15) treats that endpoint exactly. If a smaller constant is useful, \(4\) in (D18) can be replaced by \(9/4\): every nonzero off-diagonal entry has the even separation \(\delta\geq2\), so \((1+\delta)^2/\delta^2\leq9/4\), while (D17) covers the diagonal.

We supply the orthonormality used above. The finite midpoint sum
\[
 \sum_{r=0}^{N-1}\cos\left(\frac{\pi k(r+\tfrac12)}N\right)
 =\frac{\sin(\pi k)}{2\sin(\pi k/(2N))}=0
 \quad(1\leq k\leq2N-1)
 \tag{D19}
\]
follows by the finite geometric series and taking its real part. The denominator is nonzero in this range. At \(k=0\) the sum is \(N\). Applying the cosine product formula proves
\(\sum_n v_l(n)v_m(n)=\delta_{lm}\). There are \(N\) vectors in an \(N\)-dimensional space, so the transform is also complete.

Two useful consequences of (D18), valid for every row \(l\), are
\[
 \sum_{\substack{0\leq m<N\\|m-l|\geq R}}|Z_{lm}|^2
 \leq\frac{32}{3R^3}\quad(R\geq1\text{ integral}),
 \tag{D20}
\]
\[
 \sum_{m=0}^{N-1}|m-l|^2|Z_{lm}|^2\leq64.
 \tag{D21}
\]
There are at most two indices at each positive separation. For (D20), use
\(\sum_{d=R}^{\infty}(1+d)^{-4}\leq\int_R^\infty x^{-4}\,dx\).
For (D21), use \(d^2/(1+d)^4\leq d^{-2}\) and
\(\sum_{d=1}^\infty d^{-2}\leq1+\int_1^\infty x^{-2}\,dx=2\).
Thus these estimates include finite sections and endpoints without extending the actual matrix.

## 3. Fourth-moment diagonal, endpoint rate, and exact mean

Completeness and the multiplication identity in (D2) give
\[
 (Z^2)_{ll}=\sum_{m=0}^{N-1}|Z_{lm}|^2
          =\sum_{n=-L}^L\frac{n^4}{N^4}v_l(n)^2.
 \tag{D22}
\]
For \(l=0\) this equals \(\mu_{4,N}\). For \(1\leq l<N\), the cosine square identity gives the exact expression
\[
 \boxed{\displaystyle
 (Z^2)_{ll}=\mu_{4,N}+b_{2l}
 =\mu_{4,N}
 +\frac{\cos(\pi l/N)
             \bigl((N^2+1)\sin^2(\pi l/N)-6\bigr)}
            {4N^4\sin^4(\pi l/N)}}.
 \tag{D23}
\]
Let \(r_l=\min(l,N-l)\), for \(1\leq l<N\). Then \(r_l\geq1\), and
\(\sin(\pi l/N)=\sin(\pi r_l/N)\geq 2r_l/N\). Applying this bound separately to the two terms obtained from the numerator of (D9) proves
\[
 \begin{aligned}
 |b_{2l}|
 &\leq\frac{N^2+1}{16N^2r_l^2}
       +\frac3{32r_l^4}\\
 &\leq\frac7{32r_l^2}
 \leq\frac7{8(1+r_l)^2}.
 \end{aligned}
 \tag{D24}
\]
Furthermore
\[
 \left|\mu_{4,N}-\frac1{80}\right|
 =\frac{10N^2-7}{240N^4}\leq\frac1{24N^2}.
 \tag{D25}
\]
For odd \(N\geq3\), \(r_l\leq(N-1)/2\) and therefore \(1+r_l\leq N\). Combining (D23)--(D25) yields the explicit uniform endpoint estimate
\[
 \boxed{\displaystyle
 \left|(Z^2)_{ll}-\frac1{80}\right|
 \leq\frac{11}{12(1+\min(l,N-l))^2}
 \leq\frac1{(1+\min(l,N-l))^2}
 \quad(1\leq l<N)}.
 \tag{D26}
\]
For \(l=0\), (D25) supplies the sharper \(O(N^{-2})\) bound; the last inequality of (D26), interpreted with \(\min(0,N)=0\), also holds. For \(N=1\) the sole diagonal is zero and this same last bound is valid. In particular, along any sequence of actual indices satisfying
\(\min(l,N-l)\to\infty\), the diagonal converges to \(1/80\).

The finite-\(N\) average is exact:
\[
 \boxed{\displaystyle
 \frac1N\sum_{l=0}^{N-1}(Z^2)_{ll}
 =\frac1{N^5}\sum_{n=-L}^L n^4
 =\frac{(N^2-1)(3N^2-7)}{240N^4}.}
 \tag{D27}
\]
Indeed summing (D22) and using \(\sum_l v_l(n)^2=1\) proves the first equality. Alternatively, \(b_{2(N-l)}=-b_{2l}\) in (D5) pairs every \(l=1,\ldots,N-1\) with a distinct partner, since \(N\) is odd, and their corrections in (D23) cancel. This verifies (D27) directly in mode coordinates.

## 4. Endpoint qualifications

The endpoint dependence in (D26) cannot in general be replaced by dependence on \(l\) alone. For each fixed integer \(r\geq1\), (D9) and the limits \(N\sin(\pi r/N)\to\pi r\), \(\cos(\pi r/N)\to1\) give
\[
 \lim_{\substack{N\to\infty\\N\ {\rm odd}}} b_{2r}
 =\frac1{4\pi^2r^2}-\frac3{2\pi^4r^4},
 \qquad
 b_{2(N-r)}=-b_{2r}.
 \tag{D28}
\]
For \(r=1\) the displayed limit is positive, since \(\pi^2>6\). Hence the diagonal at \(l=N-1\) does not approach \(1/80\). This is a real reflected endpoint contribution, already controlled by (D26), and not a failure of the off-diagonal bound (D18).

The exact mean \(1/80\) arises from the original multiplier \(n^4/N^4\) on the original centered vertices. Replacing \(n/N\) by an endpoint grid coordinate, or replacing the vertex quadrature by an integral before deriving (D6), would discard the explicit terms \(-1/(24N^2)+7/(240N^4)\).
