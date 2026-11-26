from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p=Package('cusp','subsection Cuspidal transverse type / earlier local transport')
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
transport=r'''\begin{lemma}[Boundary transport for a holomorphic deformation]\hypertarget{tag-P295}{}\label{lem:II:boundary-deformation-transport}
\StatementRecord{lem:II:boundary-deformation-transport}{proved}{P295}{\cite[\S3 and \S3.1, arXiv v1, pp.~3--4]{SiersmaTibar2017Deformation}}
Let $g_\tau$ be a holomorphic family of functions on a neighbourhood of a closed ball $B\subset\C^3$, for parameters $\tau$ near zero, and suppose that every critical value of $g_0$ in $B$ is zero. Choose the ball transverse to the smooth strata of $g_0^{-1}(0)$. Assume the following product data near the critical set on its boundary. Finitely many coordinate families, depending smoothly on $\tau$ and holomorphically on the source variables, identify $g_\tau$ with a fixed holomorphic function $q(w)$ independent of at least one complex coordinate $z$. Each $q$ has only the critical value zero in the chosen chart, and some real direction in the $z$ coordinates is transverse to $\partial B$. These charts cover all boundary critical points for small $\tau$; on the rest of the zero-level boundary the restriction of $g_0$ to $\partial B$ is a submersion.

After shrinking the parameter neighbourhood and target disc, the deformation is trivial on the boundary in the sense of \cite[\S3, p.~3]{SiersmaTibar2017Deformation}. Each $g_\tau$ has only finitely many critical values in $B$, and there is a common nonzero regular value $b$ for which parameter transport identifies
\[
 B\cap g_\tau^{-1}(b)\simeq B\cap g_0^{-1}(b)
\]
by an orientation-preserving diffeomorphism. A compact class in a local regular fibre at an interior point of $B$, with value in the chosen target disc, can be transported locally to a value regular for the whole ball, included in that fibre in $B$, transported along a path avoiding its critical values to the $b$-fibre, and then transported to $g_0^{-1}(b)$. These maps preserve the intersection form on compact two-dimensional classes. A class represented by a map from $S^2$ is sent to the class of the composite map from $S^2$. The construction composes over nested balls and successive small deformations.

For a local expression $\xi\circ F=g_0^m$ of a map to a smooth curve, its final inclusion is into $F^{-1}(b^m)$. When that fibre is a complex two-torus, every transported spherical class has square zero.
\end{lemma}
\begin{proof}
In a product chart, a real $z$-direction gives a field $W$ with $dg_\tau(W)=0$ and $d\rho(W)\ne0$ near the relevant boundary point, where $\rho$ defines the sphere. Holding the product coordinates fixed while changing a real parameter gives a field $V$ satisfying
\[
 dg_\tau(V)+\partial_\tau g_\tau=0.
\]
Replace it by $V-d\rho(V)W/d\rho(W)$. This still solves the displayed equation and is tangent to the fixed boundary. Away from the critical set, boundary submersivity supplies a solution of the same linear equations. A partition of unity preserves the equations and boundary tangency. Its flow on the compact boundary gives a trivialization preserving the function and its critical strata. The same product directions show uniform transversality of small nonzero levels near the critical boundary; openness and compactness give it on the remaining boundary. This verifies the admissibility hypothesis in \cite[\S3, p.~3]{SiersmaTibar2017Deformation} for the specified maps.

A positive-dimensional critical component meeting the boundary has value zero by the product charts. Any other positive-dimensional component would be a compact positive-dimensional analytic subset of the interior of a coordinate ball, which the maximum principle excludes. The remaining critical components are isolated, and compactness and local finiteness of analytic components make them finite. All their values tend uniformly to zero as $\tau\to0$: otherwise a convergent sequence of critical points would limit to a critical point of $g_0$ with a nonzero value. Choose $b$ small and then the parameters smaller so that every critical value has modulus less than $|b|/2$. The family of $b$-levels is a proper submersion with transverse boundary, so boundary-tangent horizontal fields give the parameter diffeomorphism.

For a compact class on a local regular fibre, smooth local transport near its compact representative permits an arbitrarily small change of target value. Choose the resulting value $b_\tau$ regular also for the whole ball. The excluded set of values is finite, so a path $\gamma$ in the target disc joins $b_\tau$ to $b$ through regular values. Lifting $\dot\gamma$ by boundary-tangent solutions of $dg_\tau(V)=\dot\gamma$ gives the target transport. Thus the maps are the local transport and inclusion, this target transport, and the inverse parameter transport at $b$, in that order. Each diffeomorphism preserves the complex orientation; the inclusions and transports preserve intersection numbers computed with compact representatives in the interiors. Repeating these maps first in an inner ball and then in an outer ball proves the nested assertion. Finally $g_0=b$ lies in $\xi\circ F=b^m$. A sphere in a two-torus lifts to its contractible universal cover, so its homology class and square are zero.
\end{proof}
'''

oldcusp=block(source,'night:P4.28')
oldcr4=block(source,'cdp:st:C.2.CR.4')
cusp=oldcusp
oldhead='\n'.join(cusp.splitlines()[:2])
newhead=r'''\begin{proposition}[Local rigidity of a transverse cusp]\hypertarget{tag-02X0}{}\label{night:P4.28}\label{stmt:P4.28}
\hypertarget{tag-01BT}{}\label{cdp:st:C.2.CR.4}
\StatementRecord{night:P4.28}{proved}{02X0}{\cref{lem:II:boundary-deformation-transport,night:P4.16,night:P4.18,cdp:st:A.5.15}}
\StatementRecord{cdp:st:C.2.CR.4}{proved}{01BT}{\cref{lem:II:boundary-deformation-transport,night:P4.16,night:P4.18,cdp:st:A.5.15}}'''
cusp=cusp.replace(oldhead,newhead,1)
a=cusp.index('Let $p$ lie');b=cusp.index(r'\end{proposition}',a)
old=cusp[a:b]
new=r'''Let $p$ lie on a fibre of a holomorphic map $F$ from a smooth complex threefold to a smooth curve, with nearby smooth fibres complex two-tori. Suppose that the reduced singular locus of the fibre support is a smooth curve near $p$, and that its generic transverse plane-curve germ is an ordinary cusp. Every reduced local defining function $g$ then has holomorphic coordinates in which
\[
                         g=X^2+Y^3.
\tag{C.CR.15}\hypertarget{tag-00D1}{}\label{cdp:eq:C.CR.15}
\]
In particular the germ of the support is the product of that cusp with a smooth curve and its normalization is smooth. A local unit and the common full-fibre multiplicity are retained through the explicit root and coordinate maps in the proof.
'''
cusp=cusp[:a]+new+cusp[b:]
p.record('D12,D14','night:P4.28',old,new,'The complete CR.4 local domain is the proved domain of the existing P4.28 argument. The merged statement retains both the exact function normal form and the smooth normalization conclusion. The full map F and its locally derived common multiplicity are explicit; no global Betti assumption is used or added.')

a=cusp.index('We use the admissible-deformation construction of');b=cusp.index(r'\item Choose coordinates $(x,y,z)$',a)
old=cusp[a:b]
new=r'''Every component of the critical germ of $g$ has constant value, which is zero because it contains $p$. Thus, after shrinking, its full reduced critical locus is precisely the smooth singular curve $C$.

Choose a Milnor ball transverse to this curve. The deformations below retain transverse type $A_2$ near its boundary: the parameter Morse lemma and a cube root of the remaining unit give product charts with function $a^2+b^3$ and the third coordinate along the curve. These are the product data of \cref{lem:II:boundary-deformation-transport}. That lemma transports their compact local classes into the original level $g=b$, and the equality $\xi\circ F=g^m$ identifies its inclusion into the torus fibre with parameter $b^m$. Every transported spherical class consequently has square zero.
'''
cusp=cusp[:a]+new+cusp[b:]
# The original map was called f in this paragraph; retain its exact F-name here.
cusp=cusp.replace(r'$\xi\circ f=u g_{\rm red}^{\,m}$',r'$\xi\circ F=u g_{\rm red}^{\,m}$',1)
cusp=cusp.replace(r'$\xi\circ f=g^m$',r'$\xi\circ F=g^m$',1)
p.record('D12,D14','night:P4.28',old,new,'P295 keeps the full boundary field, finite-critical-value, target-path, parameter-flow and compact-intersection construction. The cusp application checks its A2 product charts and the exact original-map power equality, which follows here from local irreducibility.')

a=cusp.index(r'\item It remains to exclude Hessian rank zero at $p$');b=cusp.index(r'\item Both a zero Hessian',a)
old=cusp[a:b]
new=r'''\item Suppose that the Hessian has rank zero at $p$, so $h(0)=0$. Write $k(z)y^3$ for the cubic coefficient on the kernel of its quadratic normal form. Both $h$ and $k$ are nonzero generically. Consider
\[
                  g_{\epsilon,\delta}
                      =g+\epsilon x^2+\delta y^3.
\tag{C.CR.16}\hypertarget{tag-00D2}{}\label{cdp:eq:C.CR.16}
\]
Choose a small regular value $-\epsilon$ of $h$ with a simple preimage $z_\epsilon$ near zero, and choose $\delta$ with $k(z_\epsilon)+\delta\ne0$. Such choices exist by one-variable preparation and the density of regular values; only finitely many values of $\delta$ are excluded after fixing $\epsilon$. The quadratic normal coefficient is $h(z)+\epsilon$, and the kernel cubic is a unit at the selected point. On the fixed boundary both coefficients remain nonzero for small parameters, so its product-cusp charts persist.

\item Here is the common preparation map, also used for the second family below. For a function $G$ with the indicated critical axis, quadratic normal form $h_G(z)x^2$ and nonzero kernel cubic at the point, Weierstrass preparation in $y$ gives
\[
 G=UP,\qquad P=y^3+a(x,z)y^2+b(x,z)y+c(x,z),
\]
with $U$ a unit. At $x=0$, one has $P(0,y,z)=y^3$, so $a,b,c$ vanish there. The critical-curve equation gives $c_x(0,z)=0$. Differentiating $UP$ on that curve gives $G_{xy}=U b_x$; its zero mixed quadratic entry therefore gives $b_x(0,z)=0$. Thus $x\mid a$ and $x^2\mid b,c$. The invertible substitution $y=Y-a/3$ gives
\[
 P=Y^3+x^2\bigl(\beta(x,z)Y+\gamma(x,z)\bigr).
\tag{C.CR.17}\hypertarget{tag-00D3}{}\label{cdp:eq:C.CR.17}
\]
Indeed its two depressed coefficients are $b-a^2/3$ and $c-ab/3+2a^3/27$, both divisible by $x^2$. The function $\gamma(0,z)$ is the quadratic normal coefficient of $G$ divided by $U(0,0,z)$.

For $G=g_{\epsilon,\delta}$ at the selected point, $\gamma(0,z)$ has a simple zero. Hence
\[
 Z=\beta(x,z)Y+\gamma(x,z)
\]
is an invertible change of the curve coordinate and gives $G=U(Y^3+x^2Z)$. In these new coordinates the map
\[
 (\widehat x,\widehat Y,\widehat Z)=U^{1/3}(x,Y,Z)
\]
has invertible Jacobian and satisfies $\widehat Y^3+\widehat x^{\,2}\widehat Z=U(Y^3+x^2Z)$. Thus the exact function form, after renaming the coordinates, is
\[
                              Y^3+x^2Z.
\tag{C.CR.18}\hypertarget{tag-00D4}{}\label{cdp:eq:C.CR.18}
\]
The permutation and sign change $(x',y',z')=(Y,x,-Z)$ gives $(x')^3-(y')^2z'$. The compact spherical cycle of \cref{cdp:st:A.5.15,night:P4.18}, with exponents $(3,2,1)$, has square $-2(2/\gcd(2,1))(1/\gcd(2,1))=-4$. It is the class of the explicit continuous map from $S^2$; no embedded representative is required. Ordinary degree-three scaling places its compact representative in an arbitrarily small local nonzero level. The direct parameter path in \eqref{cdp:eq:C.CR.16} and \cref{lem:II:boundary-deformation-transport} carry that class into the original torus, a contradiction.

\item The prepared two-stage family uses the same calculation with its full coordinate map. First choose a small $\delta$ for which $g_{0,\delta}=g+\delta y^3$ has nonzero kernel cubic at the origin. Let $\Phi_\delta$ be the preceding Tschirnhaus coordinate change and write
\[
 g_{0,\delta}\circ\Phi_\delta^{-1}
       =U_\delta\{Y^3+x^2H_\delta(x,Y,z)\},\qquad
 H_\delta=\beta_\delta Y+\gamma_\delta.
\]
Here $H_\delta(0,0,z)=h(z)/U_\delta(0,0,z)$ is nonzero generically and vanishes at zero. Keeping $U_\delta$ fixed gives the holomorphic family
\[
 \widehat g_{\delta,\eta}
       =U_\delta\{Y^3+x^2(H_\delta+\eta)\}.
\]
The relation to the first family in the same coordinates is the exact identity
\[
 g_{\epsilon,\delta}\circ\Phi_\delta^{-1}
       =U_\delta\{Y^3+x^2(H_\delta+\epsilon/U_\delta)\}.
\]
At $\eta=0$ the prepared family is exactly the first-stage function through $\Phi_\delta$. For a small generic $\eta$, the function $H_\delta(0,0,z)+\eta$ has a simple zero. The coordinate $Z=H_\delta+\eta$ and the same simultaneous cube-root scaling give \eqref{cdp:eq:C.CR.18}, with the same compact spherical cycle.

These transports use nested balls. Fix the original ball $B_1$ for $g\to g+\delta y^3$, whose boundary retains transverse type $A_2$. There are only finitely many additional critical points by \cref{lem:II:boundary-deformation-transport}. Choose a smaller ball $B_2$ about the origin in the preparation chart, avoiding those points, with boundary transverse to the critical curve where $h(z)\ne0$. The second perturbation retains type $A_2$ there, and the lemma transports its compact class to a regular fibre of $g+\delta y^3$ inside $B_2$. Choose that value regular also for $B_1$. Inclusion and target transport in $B_1$, followed by the inverse first parameter transport, place it in $g=b$ and then in the torus $\xi=b^m$. These are the same interior inclusions and orientation-preserving maps, so the compact square remains $-4$.
'''
cusp=cusp[:a]+new+cusp[b:]
p.record('D12,D14','night:P4.28',old,new,'The entire P4.28 and CR.4 perturbation proofs were read. A single Weierstrass/Tschirnhaus calculation serves the preserved direct family g+epsilon x^2+delta y^3 and the prepared family U_delta(Y^3+x^2(H_delta+eta)). The exact identity under Phi_delta displays how the direct family adds epsilon/U_delta in the prepared coordinates; no parameter-preserving identification is asserted. Both original coordinate/unit transformations, the nested-ball transport and the stronger square −4 spherical-class conclusion remain.')

old='is the identity on the $z$ coordinate.\n'
new=r'''is the identity on the $z$ coordinate. For any other reduced defining function $g'=v g$, the unit $v$ is retained through the invertible coordinate change $X'=v^{1/2}X$, $Y'=v^{1/3}Y$, with the curve coordinate fixed. It gives $g'=(X')^2+(Y')^3$ exactly. This also proves the function assertion in \eqref{cdp:eq:C.CR.15} for a reduced generator chosen before the full-map unit was absorbed.
'''
assert old in cusp
cusp=cusp.replace(old,new,1)
p.record('D25','night:P4.28','CR.4 states the exact function form while P4.28 first absorbs the unit in the full map.','After obtaining g=X^2+Y^3 for the full-map root, use (X,Y,z)→(v^(1/2)X,v^(1/3)Y,z) for g′=vg.','This is an explicit local biholomorphism: its Jacobian at the origin is diagonal with nonzero unit factors, and its two powers sum to vg. Thus the exact CR.4 function assertion and the original full-fibre power map are both preserved.')
old='positive order. For the deformation\n'
new='positive order. The reduced plane zero set of $y^3h_1(y,z)$ then has a component through the origin besides $y=0$, since $h_1(0,z)$ is not identically zero, and is singular there. For the deformation\n'
assert old in cusp
cusp=cusp.replace(old,new,1)
p.record('D12','night:P4.28','CR.4 rank-one Hessian case uses its Morse residual u(y,z), while P4.28 uses h1(y,z).','The same parameter-Morse coordinates identify u with h1; retain the singular reduced plane support at a zero and the explicit h1+eta deformation giving the square −6 cycle.','This keeps the stronger concrete deformation already in P4.28 while removing the repeated separate suspension argument. The common Morse coordinate map and residual function are written explicitly.')
cusp=p.clean(cusp,'night:P4.28')
fragment=transport+'\n'+cusp
p.guard('P295 and merged cusp owner',oldcusp,fragment,'Place the proved boundary-transport input directly before the common cusp owner and retain both statement identities and all equations there.')
p.guard('Remove repeated CR4 owner',oldcr4,'','The complete local statement and proof are owned earlier by P4.28 with the CR.4 tag/label alias; C.CR.15–18 and every construction map are retained there.')
p.record('D10,D12,D16','cdp:st:C.2.CR.4',oldcr4,'The same tag01BT and statement label occur at the earlier merged P4.28 owner, with its exact local domain and C.CR.15–18.','There is one proved cusp owner. Its explicit normalization, general reduced-generator coordinate map, original full-fibre root and two perturbation constructions cover all conclusions of both old statements. The later CR.4 block is removed only after this complete receiving construction is supplied.')
p.record('D17,D18','lem:II:boundary-deformation-transport','The boundary comparison is separately proved in P4.28 and CR.4, and later invoked for other product transverse types.','P295 gives the exact product-coordinate and boundary-field hypotheses, with the explicit local/target/parameter inclusion maps; the torus conclusion uses the stated equality xi F=g0^m.','Freshly opened arXiv1512.02840v1, SHA256 b889ac5d0826e5e539a3df5db1f523d81cc343cccf9de395cd42eb1cebc05c58; read pp.1–4, in particular the admissibility definition and Milnor-data comparison Section3 p.3 and the semilocal critical-value/local-fibre data Section3.1 pp.3–4. The boundary-chart verification and exact compact-cycle maps remain because the source requires admissibility and does not identify the present full-fibre function automatically.')
p.record('D10,D16','lem:II:boundary-deformation-transport','The general parameter-lifting and compact-cycle construction occurs inside cusp-specific proofs.','P295 is a titled numbered owner with a stable label, permanent tag, explicit product-chart input and the full original-function conclusion.','The proof shows the boundary field, target and parameter paths, nested inclusions and intersection preservation. The original-map equality needed to reach a torus is a visible datum; no unconditional unequal-multiplicity conclusion is added.')
p.record('D25','lem:II:boundary-deformation-transport','P4R.14/P4R.15/P4.41/P4.45 invoke P4.28 boundary transport on reduced functions in the broad standing setting.','Their product-chart transport is covered by P295, but unequal full-fibre multiplicities still require an explicit map from the actual weighted function to the fibre carrying the sphere. Those unchanged applications remain open.','The complete current proofs of P4R.14/P4R.15/P4.41/P4.45 and P4.29 were read. P4.29, CR.5 and UN.10 have irreducible full fibre mS; the cusp itself is locally irreducible. No common-power equality is silently assumed for the four broader consumers, no statement is weakened, and no refutation or counterexample is claimed.')
for row in p.rows:
    row['old_location']=row['statement_id']+' / complete current proof'
p.write(fragment)
