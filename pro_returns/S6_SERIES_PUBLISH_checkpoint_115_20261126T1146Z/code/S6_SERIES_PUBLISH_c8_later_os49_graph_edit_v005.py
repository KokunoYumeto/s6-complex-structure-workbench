#!/usr/bin/env python3
"""Complete graph/cap publication pass after whole source and sign-map reading."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import csv,difflib,re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
PATH=ROOT/'agents/continuation8_iii_integration/units/later/os49_graph_caps.tex'
old=PATH.read_text()
assert sha256(old.encode()).hexdigest()=='ec69fff80fe15ca0ff534c34525607a0a45459a32637c51c43cb0fde44c59ac5'
new=old
changes=[]

def record(kind,sid,before,after,reason,pos):
    changes.append(dict(type=kind,statement_id=sid,
      old_location='os49_graph_caps.tex v003 sequential line '+str(new[:pos].count('\n')+1),
      old_page='pending final concordance',new_location='same result and full proof',
      new_page='pending final build',old_text=before,new_text=after,reason=reason,
      review_status='whole source and admitted comparisons read; exact maps proved; final readback pending'))

def edit(before,after,kind,reason,sid,count=1):
    global new
    assert new.count(before)==count,(before,new.count(before),count)
    for match in re.finditer(re.escape(before),new):
        record(kind,sid,before,after,reason,match.start())
    new=new.replace(before,after)

for tag,num,title in [('02S8','31','Return of the positive-diagonal family'),
                      ('02S9','32','Return for all sphere caps')]:
    match=re.search(r'\\begin\{theorem\}\[[^\n]*\]\\hypertarget\{tag-'+tag+r'\}\{\}',new)
    assert match
    edit(match[0],'\\subsection{'+title+'}\n'+match[0],'D14',
         'Create a genuine mathematical subsection containing the sole full statement and proof.',
         'night:P3F.'+num)
    edit('\\textnormal{\\small tag '+tag+'.}',
         '{\\normalfont\\scriptsize tag '+tag+'}\\par','D10',
         'Use the common small visible tag while retaining its permanent identities.',
         'night:P3F.'+num)

for text in ['The positive fan and source line.','The page and its compact model.',
             'The cusp product and based marking.','The compatible core arc.',
             'The global graph class.','The cap sphere and its normal Euler number.',
             'The integral square and return.','The closing map and its origins.',
             'The finite cap and page line.','Transport of the graph and the return.']:
    sid='night:P3F.32' if text in ['The closing map and its origins.','The finite cap and page line.','Transport of the graph and the return.'] else 'night:P3F.31'
    edit('\\textit{'+text+'}','\\paragraph{'+text+'}','D16',
         'Use a mathematical proof paragraph below the actual subsection; retain all nearby anchors.',sid)
edit('In the admitted finite origin the cap generator is',
     'In the finite origin of \\cref{night:P3F.26}, the cap generator is','D07',
     'Replace admission language by the preceding geometric construction.','night:P3F.32')
needle='the positive full root loop has winding \\(2mn\\).\n\\end{theorem}'
addition=r'''the positive full root loop has winding \(2mn\).
With the native C2 comparison of \cref{night:P3K.65}, the
negative-diagonal filling has positive-loop class \(-3k\) for
\(\lambda=r^{3k}\), and class \(-k\) for
\(\lambda=w^k\), \(w=r^3\), for both numerator signs and every
fixed integral delta character in this cap family.
\end{theorem}'''
edit(needle,addition,'D13',
     'Place the retained final negative-diagonal comparison conclusions in the formal statement with their exact parameter and native-frame scope.','night:P3F.32')

sa_start=new.index('\\begin{theorem}\\hypertarget{tag-02SA}')
sb_start=new.index('\\begin{theorem}\\hypertarget{tag-02SB}')
sa_old=new[sa_start:sb_start]
sa=r'''\subsection{The complete free affine sector}
\begin{theorem}[The free OS49 affine caps]\hypertarget{tag-02SA}{}\label{night:P3F.33}\label{stmt:P3F.33}
{\normalfont\scriptsize tag 02SA}\par
Let \(m=3k\), \(k>0\), and let \(n,d\in\mathbb Z\).
The explicit OS49 affine cap with
\(\ell=n(e_\gamma-e_u)+d\delta\) is free exactly when
\[
 \gcd(k,n,d)=1,\qquad
 3\nmid n\ \text{or}\ 3\mid k.
 \tag{P3F.33.1}
\]
Every such completed filling has fundamental group
\(\mathbb Z/|n|\), with \(\mathbb Z/0=\mathbb Z\).
Its sphere sector is exactly \(n=\pm1\); these members are
standard smooth six-spheres.
\end{theorem}
\begin{proof}
Keep the marked root charts and integral order-three matrix
\(A=T_A^{-t}\) of \cref{night:P3F.26}. On the central torus
the generator is
\[
 \alpha(z)=Az+\ell/m,\qquad
 \ell=n(1,-1,0,0)^t+d\delta.
\]
The root-disc coordinate is multiplied by \(e^{-2\pi i/m}\).

\paragraph{All stabilizers on the root chart.}
\hypertarget{tag-0008}{}\label{all-stabilizers-on-the-actual-root-chart}
A nonidentity root rotation has no fixed point away from the
central fibre. For \(j=3r\), one has \(A^j=I\), and
\(\alpha^j\) is translation by \(r\ell/k\). It has a fixed
point precisely when
\[
 k\mid rn,\qquad k\mid rd.
\]
No \(1\le r<k\) satisfies both conditions exactly when
\(\gcd(k,n,d)=1\).

For \(3\nmid j\), the images of \(A^j-I\) and \(A-I\)
agree: \(A^2-I=-A^2(A-I)\), with inverse factor \(-A\).
The primitive quotient \(\Lambda/(A-I)\Lambda\) has coordinates
\[
 \psi,\qquad h=-w+3\delta.
\]
Its coordinate map and inverse are
\[
 [v]\longmapsto(\psi(v),h(v)),\qquad
 (a,b)\longmapsto[a e_\gamma-b e_w].
\]
Indeed the displayed matrix gives
\((A-I)\Lambda=\mathbb Z e_u+\mathbb Z(3e_w+e_\delta)\),
which is exactly the kernel of these two coordinates.
Their values on \(\ell\) are \(n,3d\). The fixed-point
equation is therefore soluble exactly when
\[
 m\mid jn,\qquad m\mid3jd.
 \tag{P3F.33.2}
\]
To prove sufficiency, choose the integral vector with these two
coordinates using the displayed inverse, and subtract
\(j\ell/m\). The resulting vector \(y\) lies in the real image
of \(B-I\), where \(B=A^j\). On that image
\((B-I)^{-1}y=-(B+2I)y/3\), since \(I+B+B^2=0\) there.
This gives an actual point of the underlying complex torus
solving the affine fixed-point equation.

Put \(g=\gcd(m,n,3d)\). The integers in
\eqref{os49:eq:affine-fixed-point-test} are precisely the multiples
of \(m/g\). There is no such \(j<m\) with \(3\nmid j\)
exactly when \(3\mid m/g\). Under \(\gcd(k,n,d)=1\), every
prime other than three dividing g would divide k,n,d and is
excluded. If \(3\nmid n\), then \(g=1\). If \(3\mid n\)
and \(3\mid k\), the gcd condition gives \(3\nmid d\), so
\(g=3\) and \(3\mid m/g=k\). If \(3\mid n\) and
\(3\nmid k\), one has \(g=3\) and \(3\nmid m/g=k\).
These cases prove exactly
\eqref{os49:eq:free-affine-cap-criterion} for every group element.
The free triple \((m,n,d)=(9,3,1)\) exhibits the case
\(3\mid n\); its delta displacement supplies the required
nonintegral translation for the remaining stabilizers.

\paragraph{The fundamental-group presentation.}
\hypertarget{tag-034U}{}\label{the-full-fundamental-group-presentation}
The cap universal cover has deck generators \(\Lambda\) and
the lifted root rotation \(\alpha\), with relations
\[
 [\Lambda,\Lambda]=1,\qquad
 \alpha v\alpha^{-1}=Av,\qquad \alpha^m=\ell.
\]
Attach it by the punctured torus maps of \cref{night:P3F.26}.
The original type-II and cusp pieces impose its proved primitive
relation lattice: \(u,w,\delta\) and their section meridians
vanish, leaving gamma. The base relation kills the remaining
meridian \(\alpha\). The power relation becomes \(n\gamma=0\),
and the conjugation relations vanish because \(\psi A=\psi\).
The quotient and inverse maps are
\[
 v\longmapsto\psi(v)\pmod n,\quad\alpha\longmapsto0,
 \qquad 1\pmod n\longmapsto[e_\gamma].
\]
They give \(\pi_1(X)=\mathbb Z/|n|\), also for \(n=0\).
For \(|n|\ne1\) this group excludes a sphere. For \(n=\pm1\),
\cref{night:P3F.29} proves integral sphere homology and simple
connectivity for every k,d; the common blowup maps of
\cref{night:P3F.31} carry this topology to the positive fan.
Both displayed diagonal fillings are therefore standard smooth
six-spheres exactly in the stated sector.
\end{proof}

'''
edit(sa_old,sa,'D12',
     'Replace the repeated statement and enumerated proof fragments by one complete formal statement and one proof; retain every stabilizer, noncoprime example and group relation, and print the exact quotient/right-inverse maps. The obsolete still-uncomputed sentence is removed because SB proves those groups immediately below.',
     'night:P3F.33')

sb_start=new.index('\\begin{theorem}\\hypertarget{tag-02SB}')
sb_old=new[sb_start:]
sb=r'''\subsection{Integral homology of every free cap}
\begin{theorem}[Homology of the free OS49 affine caps]\hypertarget{tag-02SB}{}\label{night:P3F.34}\label{stmt:P3F.34}
{\normalfont\scriptsize tag 02SB}\par
Use the complete free sector of \cref{night:P3F.33}, and put
\(m=3k\), \(g=\gcd(m,n,3d)\in\{1,3\}\).
For \(n\ne0\), the completed threefold has
\[
 \begin{aligned}
 H_1(X)&=H_4(X)=\mathbb Z/|n|,\\
 H_2(X)&=H_3(X)=\mathbb Z/|n|\oplus\mathbb Z/g,\\
 H_5(X)&=0,\qquad H_0(X)=H_6(X)=\mathbb Z.
 \end{aligned}
 \tag{P3F.34.1}
\]
For \(n=0\), the free criterion is \(3\mid k\) and
\(\gcd(k,d)=1\), and the groups are
\[
 H_1=H_5=\mathbb Z,\quad
 H_2=H_3=\mathbb Z^2\oplus\mathbb Z/3,\quad
 H_4=\mathbb Z^2,\quad H_0=H_6=\mathbb Z.
 \tag{P3F.34.2}
\]
The free triple \((m,n,d)=(9,3,1)\) has
\(H_2=H_3=(\mathbb Z/3)^2\). On the entire coprime sector
\(\gcd(n,3k)=1\), one has \(g=1\), giving the homology of
\cref{maps:src:D.2.11} through the exact family map of
\cref{os49:rem:type-c-marking}.
\end{theorem}
\begin{proof}
\paragraph{The fixed exterior and the oriented boundary circle.}
\hypertarget{tag-034T}{}\label{the-fixed-exterior-and-the-actual-boundary-circle}
Remove a closed finite-cap neighbourhood and fix the same scalar
\(\lambda\) and ordinary, type-II and cusp charts. The exterior
\(V\) and its marked boundary \(E\) are then fixed for every
\(m,n,d\). Begin with the positive exterior meridian \(\mu\)
of \cref{night:P3F.26,night:P3F.29}. For the affine roof
\[
 T_{A,a}=(T^4\times[0,1])/((x,1)\sim(Ax+a,0)),
\]
the linear roof map and inverse are
\[
 U([x,t])=[x+tA^{-1}a,t],\qquad
 U^{-1}([y,t])=[y-tA^{-1}a,t].
\]
At the endpoints \(a=A(A^{-1}a)\) verifies the gluing.
The based lift \(x(t)=-tA^{-1}a\) maps to the zero-section
base loop. The vector a is the actual root-gluing lift; the
map fixes every marked fibre period and adds no integral period.

Use the clockwise base generator \(\alpha=-\mu\). Its roof
has linear part \(A^{-1}\), through the maps
\[
 R([y,t])=[Ay,1-t],\qquad
 R^{-1}([z,s])=[A^{-1}z,1-s].
\]
The endpoint relation \([Ay,1]=[y,0]\) in the target verifies
both arrows, and their composites are the identity. The full
based map and inverse are therefore
\[
 RU([x,t])=[Ax+ta,1-t],\qquad
 U^{-1}R^{-1}([z,s])=[A^{-1}(z-(1-s)a),1-s].
\]
On the marked fibre over the base point they are the identity.
They preserve its complex orientation. The coordinate s has
clockwise base orientation; the physical positive base orientation
is \(-ds\). If \(\eta_+\) is dual to \(\mu\), and \(\eta\)
is dual to \(\alpha\), the induced maps and their inverses are
\[
 \psi\longmapsto\psi,\quad h\longmapsto h,\quad
 \eta_+\longmapsto-\eta,\qquad h=-w+3\delta.
\]
The invariant forms and integral image lattices for A and its
inverse agree by \(A^{-1}-I=-A^{-1}(A-I)\), with inverse
factor \(-A\). These based maps specify one fixed pair \((V,E)\);
only the finite-cap logarithmic attachment varies.

The root generator is
\[
 g(z,s)=(Az+\ell/m,e^{-2\pi i/m}s),\qquad
 \ell=n(e_\gamma-e_u)+d\delta.
\]
Its logarithmic collar and inverse are addition and subtraction
of \(\log s\,\Pi(s)\ell/(2\pi i)\).
The positive exterior meridian maps to \(g^{-1}\), and
\(\alpha\) maps to g. Thus the complex-positive normal circle is
\(\nu_+=m\mu+\ell\). Hold the cap point fixed and traverse
\(s(t)=s_0e^{-2\pi it}\). The logarithm drops by t, the ordinary
fibre coordinate changes by \(-t\Pi\ell\), and the ordinary
base winds clockwise m times. This clockwise normal circle is
\[
 \beta_{m,n,d}=m\alpha-\ell=-\nu_+.
 \tag{P3F.34.3}
\]
Its values on \((\psi,h,\eta)\) are \((-n,-3d,m)\).
The circle-parameter map \(e^{2\pi it}\mapsto e^{-2\pi it}\)
and its identical inverse have degree \(-1\).
The root quotient gives a free geometric normal circle action,
including the cases where this abelianized vector is divisible.

Keep the complex orientations of the completed X and the central
cap B. If \(\Theta_+\) is the complex-normal Thom generator, use
\(\Theta_-=-\Theta_+\) for the clockwise parameter. The maps
between Thom identifications multiply every shifted group by
\(-1\), with the same inverse. Accordingly
\((\pi_\beta)_*=-(\pi_{\nu_+})_*\) in fibre integration.
These choices fix the signs of both the transfers and the pair
sequence used below.

The cap retracts onto the compact flat four-manifold
\(B=B_{m,n,d}=T^4/\langle g\rangle\).
Its rational cohomology is the invariant exterior algebra, with
Betti numbers \((1,2,2,2,1)\), so its Euler characteristic is zero.
Abelianizing \(g^m=\ell\) and the conjugation relations gives
\[
 H_1(B)=\mathbb Z^3/\langle(-n,-3d,m)\rangle
       =\mathbb Z^2\oplus\mathbb Z/g,
\]
and its first-cohomology pullback is the exact lattice
\[
 L_{m,n,d}=H^1(B)
 =\ker\bigl[(-n,-3d,m):\mathbb Z^3\longrightarrow\mathbb Z\bigr].
 \tag{P3F.34.4}
\]

\paragraph{An integral basis of the boundary two-cohomology.}
\hypertarget{tag-000A}{}\label{an-integral-basis-of-the-boundary-two-cohomology}
In the clockwise roof put
\[
 u_2=\psi h,\qquad v_2=(\psi+u)w,\qquad
 p=\eta\psi,\qquad q=\eta h/3.
\]
Under the preceding roof reversal, \(u_2,v_2\) are fixed,
and \(p_+=\eta_+\psi,q_+=\eta_+h/3\) map to \(-p,-q\);
the inverse has the same signs. We establish that
\((u_2,v_2,p,q)\) is an integral basis, retaining the division
by three in q.

Use the reference cap \((m,n,d)=(3,1,0)\), with projection
\(\pi_0\). The integral class \(-\psi\) evaluates to one on
\(\beta=3\alpha-\ell_0\). The function
\(f=e^{-2\pi i\psi}\) is well defined on the linear roof and
has weight one under this oriented circle action. The maps
\[
 E\longrightarrow B\times S^1,\qquad x\longmapsto(\pi_0(x),f(x)),
 \qquad (b,z)\longmapsto z\cdot\sigma(b),
\]
are inverse, where \(\sigma(b)=f(x)^{-1}\cdot x\) for any
point x over b. Weight-one equivariance makes this section
independent of the chosen x. This proves the integral product
splitting with precisely the marked circle.

The first-cohomology pullback from B has basis
\(h,3\psi+\eta\). The complete finite specialization in
\cref{night:P3F.29} identifies its integral two-cohomology
with the full fibre invariant lattice \(\langle u_2,v_2\rangle\).
Its boundary pullback is
\[
 u_2+q,\qquad v_2.
\]
Indeed these invariant forms are horizontal for
\(3\alpha-\ell_0\). Averaging forms over the finite torus
cover computes all rational cohomology. The kernel of restriction
is the rational span of p,q, and contraction determines the
displayed correction uniquely. The product classes supplied by
\(-\psi\) are \((-\psi)h=-u_2\) and
\((-\psi)(3\psi+\eta)=p\). Hence
\((v_2,u_2+q,u_2,p)\) is an integral basis. The inverse change
recovers \(q=(u_2+q)-u_2\) and fixes the other three classes,
giving the asserted basis without discarding the factor three.

\paragraph{The exterior restriction lattice.}
\hypertarget{tag-01O2}{}\label{determine-the-exterior-restriction-without-guessing-a-splitting}
Fill V by the reference cap. The resulting manifold is the
sphere of \cref{night:P3F.26}. Integral Mayer--Vietoris gives
\[
 H^2(V)=\mathbb Z^2,\qquad H_1(V)=\mathbb Z,\qquad
 H_2(V)=\mathbb Z^2.
\]
Restriction embeds \(H^2(V)\) as a direct summand of
\(H^2(E)\), complementary to the cap pullback just computed.
The generator of \(H_1(V)\) is gamma by the same marked
van Kampen quotient.

Project two exterior restriction basis vectors modulo v2 to
\(U_1,U_2\in\mathbb Z^3\), in the order \((u_2,p,q)\), and
write \(W=U_1\times U_2\). For the period-one clockwise normal
action, direct contraction of the wedge factors gives the integral
fibre integrations
\[
 \begin{aligned}
 (\pi_\beta)_*u_2&=3d\psi-nh,&
 (\pi_\beta)_*v_2&=0,\\
 (\pi_\beta)_*p&=m\psi+n\eta,&
 (\pi_\beta)_*q&=kh+d\eta.
 \end{aligned}
 \tag{P3F.34.5}
\]
The factors \(\psi+u\) and w both vanish on beta, giving the
second formula. The division by three in q gives exactly k,d
in the fourth. These are the clockwise transfers associated to
\(\Theta_-\); the positive-normal transfers are their negatives.

For every \(k>0,d\in\mathbb Z\), the \(n=1\) filling is the
sphere proved in \cref{night:P3F.29}. Its pair sequence makes
\(H_1(B_{3k,1,d})\to H_2(V)\) an integral isomorphism.
The dual is the restriction of
\eqref{os49:eq:normal-circle-integration} to \(H^2(V)\).
The determinant of its two columns, in the primitive kernel
lattice, is \(\pm(W_1k-W_2d+W_3)\). Its absolute value is one
for every positive k and every integer d. Varying d and then k
therefore gives
\[
 W_1=W_2=0,\qquad W_3=\varepsilon\in\{1,-1\}.
\]
Write the projected columns as \((a_1,b_1,0),(a_2,b_2,0)\).
They have no q component: the first two components of their
cross product vanish and their u2,p minor is the unit epsilon.
The exact exterior basis map and inverse use
\[
 M=\begin{pmatrix}a_1&a_2\\b_1&b_2\end{pmatrix},\qquad
 M^{-1}=\varepsilon\begin{pmatrix}b_2&-a_2\\-b_1&a_1\end{pmatrix}.
\]
Multiply the row of exterior basis classes by \(M^{-1}\); the
inverse multiplies by M. Their restrictions are u2,p modulo
multiples of v2, whose transfer is zero.

\paragraph{The Smith invariants and the full homology.}
\hypertarget{tag-0353}{}\label{the-two-smith-invariants-and-every-homology-group}
In this explicit exterior basis the dual transfer has columns
\[
 v_1=(3d,-n,0),\qquad v_2=(m,0,n)
 \quad\text{in }L_{m,n,d}.
 \tag{P3F.34.6}
\]
For \(n\ne0\), their cross product is
\[
 v_1\times v_2=n(-n,-3d,m).
\]
The primitive normal of \(L_{m,n,d}\) is
\((-n,-3d,m)/g\), so their index is \(g|n|\).
The gcd of their entries is g. This kernel lattice is primitive
in \(\mathbb Z^3\), so a vector's integral divisibility inside
it agrees with its ambient divisibility. Thus its first Smith
invariant is g and its second is \(|n|\). The freeness proof
gives \(g\in\{1,3\}\) and \(g\mid n\).

Use the pair sequence for \(X=V\cup N(B)\), with the clockwise
Thom identification \(H_j(N(B),E)=H_{j-2}(B)\) specified above.
Its relevant part is
\[
 H_1(B)\longrightarrow H_2(V)\longrightarrow H_2(X)
 \longrightarrow H_0(B)\xrightarrow{\ -n\ }H_1(V).
\]
The last arrow is \(-n\), since \(\beta\) maps to
\(-n\gamma\) in the exterior. Its comparison to the
complex-positive Thom sequence multiplies \(H_0(B)\) by
\(-1\) and fixes \(H_1(V)\), with identical inverse.
For \(n\ne0\) it is injective. Torsion in \(H_1(B)\) maps
to zero in free \(H_2(V)\); the transpose of the free transfer
has the computed Smith invariants. Consequently
\[
 H_2(X)=\mathbb Z/g\oplus\mathbb Z/|n|.
\]
The fundamental group calculation of \cref{night:P3F.33}
gives \(H_1(X)=\mathbb Z/|n|\). Euler additivity gives
\(\chi(X)=2\), since V and E are fixed, every flat cap has
Euler characteristic zero and the reference filling is a sphere.
The rational groups in degrees one and two vanish. Poincar\'e
duality and this Euler characteristic give zero in every middle
rational degree. Integral duality and the universal coefficient
theorem then give
\[
 H_3(X)\cong\operatorname{Ext}(H_2(X),\mathbb Z),\qquad
 H_4(X)\cong\operatorname{Ext}(H_1(X),\mathbb Z),\qquad H_5(X)=0.
\]
This proves \eqref{os49:eq:free-cap-nonzero-homology}.

For \(n=0\), freeness gives \(3\mid k\) and \(\gcd(k,d)=1\).
The target kernel has basis \(\psi,kh+d\eta\). Choose integers
a,b with \(ad+bk=1\). The transfer columns are
\(3d\psi,3k\psi\), and
\(a(3d\psi)+b(3k\psi)=3\psi\). Their image is therefore
exactly \(3\mathbb Z\psi\), with cokernel
\(C=\mathbb Z\oplus\mathbb Z/3\).
The pair sequence gives \(0\to C\xrightarrow{i}H_2(X)
\xrightarrow{p}\mathbb Z\to0\).
Choose z with \(p(z)=1\). Its splitting and inverse are
\[
 (c,r)\longmapsto i(c)+rz,\qquad
 x\longmapsto\bigl(i^{-1}(x-p(x)z),p(x)\bigr).
\]
Thus \(H_2(X)=\mathbb Z^2\oplus\mathbb Z/3\).
The group calculation gives \(H_1(X)=\mathbb Z\);
duality gives \(H_5(X)=\mathbb Z,H_4(X)=\mathbb Z^2\).
Euler characteristic two makes the third Betti number two, and
integral duality identifies its torsion with that of H2. These
are exactly \eqref{os49:eq:free-cap-zero-homology}.
\end{proof}
'''
edit(sb_old,sb,'D12',
     'Give SB one complete statement and proof with all zero/nonzero groups. Preserve the free domain and coprime specialization; print the full based roof, circle/Thom orientation, reference splitting, exterior inverse basis and zero-case splitting. Remove production/CSV/sample-program prose.',
     'night:P3F.34')

semantic=[
('D25','Its positively marked circle, up to the common orientation convention, is the actual loop',
 'This clockwise normal circle is',
 'The full based roof and inverse give alpha=-mu and beta=-nu_+; the degree-minus-one circle map and signed Thom identification retain every transfer column.'),
('D25',r'\xrightarrow{\ n\ }H_1(V)',r'\xrightarrow{\ -n\ }H_1(V)',
 'Repair the last arrow in the clockwise Thom sequence only after root/collar, normal circle and all transfer generators agree; the exact comparison multiplies H_0(B) by -1 and fixes H_1(V). No homology conclusion changes.'),
('D20',r'After an integral change of basis in \(H^2(V)\), the dual transfer map has the two columns',
 'In this explicit exterior basis the dual transfer has columns',
 'The full proof now prints U/R and inverses, the reference product map and inverse, M/M inverse, and the Bezout/free-extension inverse maps; no integral comparison is left unspecified.'),
('D13','The complete $n=0$\ngroups are also computed below.',
 r'For \(n=0\), the free criterion is \(3\mid k\) and',
 'Move both complete homology displays into the formal theorem with unchanged conclusions and their permanent equation identities.'),
('D09',r'The executable check builds a primitive integral basis of \(P3F.34.4\), expresses \(P3F.34.6\) in that basis, and computes its Smith form for all sampled free triples.',
 '',
 'The inspected historical code computes ambient minors; no retained actual output stream was available. Remove this inaccurate implementation claim from the proof and record the exact source scope separately.'),
('D26','This example refutes an unrestricted reading of the cyclic\nformula in the short CSV summary.',
 'On the entire coprime sector\n'+r'\(\gcd(n,3k)=1\), one has \(g=1\)',
 'Retain the precise KL hypothesis and its actual Q30N family map; preserve the (9,3,1) free example and larger free domain. Move CSV/historical interpretation to the review record.')]
for kind,before,after,reason in semantic:
    assert before in sb_old,(kind,before)
    assert not after or after in new,(kind,after)
    record(kind,'night:P3F.34',before,after,reason,new.index('\\label{night:P3F.34}'))

equations=[
('P3F.31.1','Q30E','os49:eq:positive-diagonal-fan'),
('P3F.33.1','Q30F','os49:eq:free-affine-cap-criterion'),
('P3F.33.2','Q30G','os49:eq:affine-fixed-point-test'),
('P3F.34.1','Q30H','os49:eq:free-cap-nonzero-homology'),
('P3F.34.2','Q30I','os49:eq:free-cap-zero-homology'),
('P3F.34.3','Q30J','os49:eq:clockwise-normal-circle'),
('P3F.34.4','Q30K','os49:eq:cap-dual-lattice'),
('P3F.34.5','Q30L','os49:eq:normal-circle-integration'),
('P3F.34.6','Q30M','os49:eq:free-cap-transfer-columns')]
aliases=[]
for token,tag,label in equations:
    sid='night:'+token.rsplit('.',1)[0]
    before='\\tag{'+token+'}'
    edit(before,before+'\\hypertarget{tag-'+tag+'}{}\\label{'+label+'}',
         'D19','Give the formerly manual-only equation a permanent descriptive identity before converting to the global automatic counter.',sid)
    aliases.append(dict(old_printed_token=token,new_tag=tag,new_label=label,
                        source_file=str(PATH.relative_to(ROOT))))
candidate,number_changes,issues,unused_aliases=presentation.remove_manual_equation_tags(new)
assert not issues,issues
for change in number_changes:
    record(change.kind,change.statement_label or 'sec:III:os49-night',change.old,change.new,change.reason,change.start)
new=candidate
assert '\\StatementRecord' not in new
assert '\\tag{' not in new
units.check_permanent_identifiers(old,new,
    allowed_labels=[row['new_label'] for row in aliases],
    allowed_targets=['tag-'+row['new_tag'] for row in aliases])

table=OUT/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_defects.tsv'
with table.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for item in changes:
    item['change_id']='c8-III-os49_graph_caps-'+str(len(rows)+1).zfill(3)
    rows.append(item)
PATH.write_text(new)
with table.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
alias_path=OUT/'S6_SERIES_PUBLISH_III_os49_graph_equation_aliases.tsv'
with alias_path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=list(aliases[0]),delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(aliases)
(OUT/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_v005.diff').write_text(
    ''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),
                               fromfile='graph_v003',tofile='graph_v005')))
print('UTC',datetime.now(timezone.utc).isoformat())
print('OUTPUT',len(new.splitlines()),sha256(new.encode()).hexdigest())
print('LOCAL_EDITS',len(changes),'TOTAL_ROWS',len(rows),'NEW_EQUATION_IDENTITIES',len(aliases))
print('ALL_PERMANENT_IDENTITIES_PRESERVED; FOUR_ACTUAL_SUBSECTIONS')
print('BOUNDED_SB_ORIENTATION_AND_LAST_ARROW_REPAIR; ALL_GROUPS_AND_FREE_DOMAINS_RETAINED')
print('NO_CANONICAL_OR_SHARED_LEDGER_WRITES; NO_INDEPENDENT_CREDIT')



