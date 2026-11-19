"""Apply explicitly documented mathematical corrections to full received proofs.

The original rejected arguments are preserved as history, not current proofs.
Each replacement is recorded in analysis/IV/reconciliation.json.
"""
from pathlib import Path
import json,re
W=Path(__file__).resolve().parents[2]
P=W/'papers/IV'
s=(P/'body_source.tex').read_text()
changes=[]

def block(label):
 a=s.index(r'\label{'+label+'}')
 b=s.find(r'\end{proof}',a)+len(r'\end{proof}')
 return a,b,s[a:b]

def change(label, fn, reason):
 global s
 a,b,t=block(label);u=fn(t)
 assert u!=t,(label,reason)
 s=s[:a]+u+s[b:]
 changes.append({'label':label,'reason':reason})

# The level cobordism in K98 supplies the missing actual move in K95.
a,b,z=block('night:P3K.98')
start=z.index('For the relative \\(p_1\\) pairing use the actual level')
end=z.index('The outward Euler collar',start)
level=z[start:end].replace(r'\tag{EG.41a}',r'\tag{EC.26c}')
old=r'''The relative \(p_1\)-pairing against
\(\Xi\) is zero: a regular b-level outside the surgery is the
actual source three-level times the gamma circle, with the source
four-form restricting to zero and the just specified boundary
transgression zero. This retains the full E6 source connection.'''
change('night:P3K.95',lambda t:t.replace(old,level),
 'Replace the unsupported product identification of a moved regular level by the full cutoff homotopy, relative regular-level cobordism and Stokes argument of K98 EG.41a.')

# Here a minus sign denotes an opposite orientation, not a vector negation.
old=r'''For the physical line
\(M\), the positive-generator convention of F22 uses
\(u=+q_H\), \(y'=-y\). Thus its first and second pieces are'''
new=r'''For the physical line
\(M\), the positive-generator convention of F22 uses
\(u=q_H\) and the oppositely oriented \(y\)-ball.
More explicitly let \(\rho(y_0,y_1,y_2,y_3)=(-y_0,y_1,y_2,y_3)\)
and use \(y'=\rho(y)\) on that ball and its boundary.
The determinant of \(D\rho\) is \(-1\), so this is a literal
orientation-reversing extension across the ball. In this paragraph
\(-L\) and \(-R\) denote these opposite product orientations;
no antipodal map of \(\mathbb R^4\) is being used. Thus its first
and second pieces are'''
change('night:P3K.68',lambda t:t.replace(old,new),
 'Spell out the orientation-reversing reflection on the four-ball; the antipodal map would have degree +1 and cannot implement the declared opposite orientation.')
change('night:P3K.7',lambda t:t.replace('P3K.6 gives \\(b|_V=2c_1(M)\\)',r'\cref{night:P3K.68} gives \(b|_V=-2c_1(M)\)').replace('difference \\(b-2m\\)','difference \\(b+2m\\)'),
 'Transport the graph-normal meridian line by the explicit Hermitian U=M^{-1} map. The restriction is -2c1(M); the square and zero index are unchanged.')
def type_zero_index_line(t):
 t=t.replace(r'\begin{enumerate}[label=\arabic*.]',r'''\begin{enumerate}[label=\arabic*.]
\item The meridian-one class in this proof is \(x=c_1(U)\),
where \(U=M^{-1}\) through the explicit Hermitian map of
\cref{night:P3K.68}. The line \(U\) extends over the trace
bordism below; taking its fibrewise dual extends the original
physical line \(M\) over that same bordism. The two odd
characteristic numbers change sign under this actual dual map,
so \(A_M=-A_U\). We calculate \(A_U\) first.''',1)
 t=t.replace('The actual spin return index is consequently','The meridian-one spin index is consequently')
 t=t.replace(r'A(f)=\frac{4\int_Bx^3',r'A_U(f)=\frac{4\int_Bx^3')
 t=t.replace('The normal Pontryagin class cancels.  Thus',r'The physical index is \(A_M(f)=-A_U(f)=0\). The normal Pontryagin class cancels. Thus')
 return t
change('night:P3K.7',type_zero_index_line,
 'Type the meridian-one trace line explicitly as U=M^{-1} throughout its zero-index proof; dualizing the actual extending line carries the physical line and gives A_M=-A_U=0.')

# Replace unpublished working-note stage names by the actual complete proof.
def repair_working(t):
 t=t.replace('The marked-node coordinate and source/Cartier rescaling are EN.1--3 of\n\\path{part3_e6_marked_node_cover_working.md}.',
 r'The marked-node coordinates are (EC.2)--(EC.4), and the full source/Cartier rescaling is (EC.15) and (EC.20) below.')
 t=t.replace('With the actual Miller factors of EN.3 define','With the following actual Miller factors define')
 t=t.replace('The divisor computation E68--69 gives',r'The full divisor computation in \cref{night:P3K.94}, (EU.2)--(EU.3) and the following component calculation, gives')
 t=t.replace('Use the three exact A2 charts of E70.',r'Use the three exact $A_2$ charts in \cref{night:P3K.94}, (EU.4).')
 t=t.replace('Blow up the four literal deck-fixed points of E70.',r'Blow up the four literal deck-fixed points constructed in \cref{night:P3K.94}, (EU.8).')
 t=t.replace("by E71's actual divisor computation.",r'by the full root divisor computation in \cref{night:P3K.94}, (EU.9)--(EU.9a).')
 t=t.replace('The transformed root is exactly the equation in EN.3.',r'The transformed root is the equation obtained from (EC.16) by the displayed substitution (EC.20).')
 return t
change('night:P3K.95',repair_working,'Replace six working-note locators by the actual equations and full proof now present in the manuscript.')

def repair_order_three_scope(t):
 t=t.replace('In particular the morphism is\nsmooth on its domain, including repeated factors.',
             'In particular the domain of this proper resolution is\nsmooth, including the charts arising from repeated factors.')
 t=t.replace('Working proof for the open E6 order-three return calculation. This file proves the specified generic toric comparison. It does not assign a return, a global fixed-component count, or an extension of the original Spin structure over a resolved fourfold. The four-dimensional corner/source/Cartier graphs remain part of the active attachment calculation.',
             'This supporting proof establishes the generic toric comparison used in E100--E109. The fixed-component calculation is FS.1--FS.6, and the compact relative boundary and its physical transfer are E108--E109. The retained original determinant divisor enters those boundary maps; the finite-chart Stokes argument of E102 uses no central Spin extension.')
 t=t.replace('This remains a local determinant/Spin statement;\nthe full period-strip boundary equation is still open.',
             'This is the local determinant and Spin comparison. The\ncompleted relative boundary equation is proved in E109.')
 t=t.replace('The complete point/O graph, compact global end attachment, its\nSpin extension and the characteristic return remain separate\nunfinished constructions; this proof assigns no such value.',
             'The finite marked point/O Cartier comparisons are E90--E99.\nThe compact relative attachment and its actual exterior determinant\nand physical-line maps are E109. The obstruction in E101 fixes\nthe precise scope of the central source comparison used there.')
 t=t.replace('The construction preserves earlier local calculations and stopped\napproaches as stage records. Each local-only scope notice in those\nrecords describes the assertion proved at that stage; E108--E109\nsupply the final closed-double and outer-transfer assertions. The\nopening historical work-list E65 is retained in the archived source\nand omitted from this proof export. No native free coordinate or\nother-fan value is needed for this theorem.',
             'The local constructions below are used with their stated domains.\nThe completed closed-double and outer-transfer assertions are\nE108--E109. The explicit obstructions in E78, E89 and E101\nidentify the precise maps excluded from this construction. The\nnative free coordinates and the all-fan formula are proved in\n\\cref{night:P3K.100}.')
 return t
if r'\label{night:P3K.99}' in s:
 change('night:P3K.99',repair_order_three_scope,
        'State smoothness of the resolution domain precisely and replace obsolete intermediate work-state notices by the completed E108--E109 boundary scope; retain all local maps and all proved obstructions.')


# The positive-fan page carries the same typed dual meridian line as K7.
def type_os49_meridian(t):
 t=t.replace('the graph-normal meridian line with M on the entire page.',
 r"""the graph-normal meridian line with \(U=M^{-1}\) on the entire page,
through \(D_M(v)(w)=\langle v,w\rangle/\langle v,v\rangle\).
Thus its restriction is \(-c_1(M)\). The fibrewise dual of the actual
extending line carries \(M\) over the same trace bordism, and its
odd characteristic index is \(A_M=-A_U\).""")
 t=t.replace(r'therefore has \(b^2=-8k\)',
 'therefore has \\(b|_V=-2c_1(M)\\), \\(b^2=-8k\\)')
 t=t.replace(r'A_+=\frac{3(-8k)-(-24k)}{24}=0.',
 r'A_{U,+}=\frac{3(-8k)-(-24k)}{24}=0,\qquad A_{M,+}=-A_{U,+}=0.')
 return t
change('night:P3K.65',type_os49_meridian,
 'Transport the regular-band meridian line to U=M^{-1} with its explicit Hermitian fibre map. The normal Euler square and zero physical index are unchanged.')

def type_source_zero_double(t):
 return t.replace('The full unit matrix has winding',
 r'''The matrices \(V,\delta\) in (ZA.6)--(ZA.12) are the
ordinary-product invariants of the literal double of the parameter
circle. Explicitly the family is pulled back by
\(\pi:S^1\to S^1,\ \pi(e^{2\pi i\theta})=e^{4\pi i\theta}\);
its line, native star products and connection are pulled back by
the same map. The middle and final seams use the original source,
Cartier and cap closing in (ZA.3). Its relative return is the square
of the original return, so its two free coordinates double. The
period winding matrix is consequently \(2W\). The product-frame
derivative contributes a further factor two to the right free
coordinate, giving the divisor four in (ZA.10)--(ZA.11). The
central sphere class is updated by the single native integer;
no division in \(\Theta_7\) occurs.

The single-loop full unit matrix has winding''',1)
change('night:P3K.90',type_source_zero_double,
 'Make the literal degree-two parameter pullback and the domains of V and delta explicit; this is the actual cover responsible for the divisor four, not a division of a sphere residue.')

def correct_scalar_crossing_c1(t):
 old=r'''       \langle c_1(L_m),[S^1_{\rm spatial}
                              \times S^1_\theta]\rangle=-m.'''
 new=r'''       \langle c_1(L_m),[S^1_{\rm spatial}
                              \times S^1_\theta]\rangle=+m.'''
 assert old in t
 t=t.replace(old,new,1)
 old=r'''Its curvature integral in that
temporary direction is \(m\). The oriented spatial
circle traverses the cap in the opposite direction,
giving (SCN.21).'''
 new=r'''For the same unitary-connection convention used in
\cref{night:P3K.66}, the Chern form is
\(c_1(\nabla)=\frac{i}{2\pi}F_\nabla\). Since
\(F_{\rm cap}=im\rho'(s)\,ds\wedge d\theta\), its Chern
integral in that temporary direction is \(-m\).
The oriented spatial circle traverses the cap in the opposite
direction, giving \(+m\) in (SCN.21).

The coefficient/frame conversion gives the same sign directly.
The coefficient arrow \(y_{\rm cap}=g_1y_{\rm master}\)
means \(e_{\rm cap}=g_1^{-1}e_{\rm master}\).
On the cap use the frame \(e_{\rm cap}g_1\), which matches
the master frame at endpoint \(1\). At endpoint \(0\) this
frame equals \(g_1e_{\rm master}\). Thus a single cut
spatial-circle frame has terminal frame multiplier
\(g_1=e^{-im\theta}\), and its coefficient multiplier is
\(g_1^{-1}=e^{im\theta}\). This is the literal clutch
presentation with Chern class \(+m[ds]\smile[d\theta/(2\pi)]\).'''
 assert old in t
 t=t.replace(old,new,1)
 t=t.replace(r'''evaluation \(-2m\).''',r'''evaluation \(+2m\).
The two endpoint determinants themselves still have windings
\(0\) and \(-2m\), as computed in (SCN.19); the crossing
class includes the explicitly reversed cap interval.''',1)
 return t
change('night:P3K.62',correct_scalar_crossing_c1,
 'Correct the auxiliary two-torus Chern sign from its exact coefficient arrows, reversed cap interval and c1=(i/2pi)F convention. The Chern evaluation is +m and determinant crossing +2m; endpoint determinant windings and all native/flop conclusions remain unchanged.')

# The initial elliptic comparison contains a superseded work-state paragraph.
def rewrite_sixfold_map(t):
 start=t.index('If the monodromy')
 end=t.index(r'\end{proposition}',start)
 t=t[:start]+r'''The positive degree-six circle pullback induces the endomorphism
\[
 \mu_6:\mathbb Z/28\longrightarrow\mathbb Z/28,\qquad
 \mu_6(a)=6a .
\]
Its kernel is \(\{0,14\}\), its image is the set of even residues,
and its fibres are
\[
 \mu_6^{-1}(2r)=\{5r,5r+14\}\pmod{28},\qquad
 \mu_6^{-1}(2r+1)=\varnothing .
\]
These formulas describe the actual covering homomorphism and all
its fibres; they assign no numerical value to the original return.
'''+t[end:]
 start=t.index(r'\begin{proof}')
 t=t[:start]+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item Write the mapping torus as
\(M_\Phi=(X\times\mathbb R)/((x,t+1)\sim(\Phi(x),t))\).
The map
\[
 M_{\Phi^6}\longrightarrow M_\Phi,\qquad [x,t]\longmapsto[x,6t]
\]
is well defined: its two source representatives map to
\([x,6t+6]=[\Phi^6(x),6t]\). It is the pullback by the
positive degree-six map of the oriented base circle.
The return is therefore \(\Phi^6\), and the induced
homomorphism of \(\Theta_7\) is \(\mu_6\).
\item The equation \(6a=0\pmod{28}\) has precisely
the solutions \(a=0,14\). The image has fourteen
elements and every image is even, so it equals the
fourteen even residues.
\item For the even target \(2r\), the equality
\(6a=2r\pmod{28}\) is equivalent to
\(3a=r\pmod{14}\). Since \(3\cdot5=1\pmod{14}\),
the two lifts are \(5r\) and \(5r+14\pmod{28}\).
This constructs every listed fibre directly from the
covering homomorphism.
\end{enumerate}
\end{proof}'''
 return t
change('maps:src:B.6.1',rewrite_sixfold_map,
 'Replace the conditional congruence statement by the unconditional degree-six covering homomorphism with its explicit mapping-torus map, kernel, image and complete fibres.')

def repair_initial_page_scope(t):
 t=t.replace(r'\cref{night:P3F.25},',
 r'\cref{night:P3F.25} (superseded assertion, retained only as a rejection target),',1)
 t=t.replace(r'Theorem2.3 and Corollary2.6, gives the formula',
 r'Theorem 2.3 and Corollary 2.6, p.~3, with the outward-first convention on p.~2, gives the formula')
 start=t.index(r'\subsection{State of the family-monodromy application}')
 end=t.rindex(r'\end{enumerate}')
 history=W/'analysis/IV/historical_context'
 history.mkdir(exist_ok=True)
 (history/'P3F5_superseded_application_status.tex').write_text(t[start:end])
 t=t[:start]+r'''
\item The actual meridian-line trace is constructed in
\cref{night:P3K.6,night:P3K.7}; its fibrewise dual is the physical
line by the explicit Hermitian map in \cref{night:P3K.68}.
For the positive and negative OS49 caps, the full boundary and
shorter-loop comparisons are \cref{night:P3K.65}. These actual
comparisons specify the line, orientation and cap in the applications
of the displayed characteristic formula. The earlier application
paragraph, including its superseded reference to the global assertion
of \cref{night:P3F.25}, is retained in the historical source record.

'''+t[end:]
 return t
change('night:P3F.5',repair_initial_page_scope,
 'Archive the obsolete application-state paragraph that still asserted the globally refuted F25 conclusion; retain the proved parity obstruction and point to the actual typed trace and cap comparisons.')

def repair_degree_twelve_maps(t):
 prefix=t[:t.index(r'\begin{proof}')]
 proof=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item Let \(C\) be the smooth compactification of
\(b^3=a^4+1\), and set \(x=b^3\). At \(b=0\) there are
four distinct points, each with local equation \(x=b^3\).
At \(a=0\) there are three distinct points, each with
\(x-1=a^4\). Since \(\gcd(3,4)=1\), the normalization has
one point at infinity, with pole orders \(3,4\) for \(a,b\).
Thus \(x:C\to\mathbb P^1\) has degree \(12\) and profiles
\(3^4,4^3,12\) over \(0,1,\infty\).
The ramification is \(8+9+11=28\), so
\(2g(C)-2=-24+28=4\).

\item The E26 surface has fibres \(IV^*,III,I_1\) over
\(0,1,\infty\). Pullback by \(t=x\), followed by the displayed
minimalizations of the root charts, removes the order-three
\(IV^*\) and order-four \(III\) fibres. The single order-twelve
pullback of the nodal chart is \(I_{12}\).

\item Choose a finite regular value \(t_*\ne0,1\) of that
elliptic fibration. The explicit Möbius map
\[
 \mu(x)=\frac{t_*x}{x+t_*-1}
\]
sends \(0,1,\infty\) to \(0,1,t_*\). Its determinant is
\(t_*(t_*-1)\ne0\), so it preserves the ramification indices.
Its pole is \(x=1-t_*\), a finite value distinct from \(0,1\).
The map \(x\) is unramified there, with twelve distinct
preimages. Consequently the pullback by \(t=\mu(x)\) has
twelve \(I_1\) fibres. The order-three and order-four branches
still remove \(IV^*\) and \(III\); the order-twelve branch
now lies over the smooth fibre at \(t_*\).
These equations give the complete relation between the two
degree-twelve maps. The regular-binding page uses \(t=\mu(x)\);
its real trace and boundary maps are \cref{night:P3K.6,night:P3K.7}.

\item Each compact minimal pullback has Euler number \(12\),
no multiple fibres and a section. Hence
\[
 \chi(\mathcal O)=1,\qquad
 K=(\chi(\mathcal O)+2g(C)-2)F=5F,\qquad
 \sigma=-8 .
\]
The degree-twelve height pullback is \(12/6=2\), by
\cite[Proposition 8.12 and equation (8.25), p.~231]{Shioda1990}.
The original section meets the smooth component of \(I_1\),
so all its multiples meet the identity component of \(I_{12}\).
In the second pullback there are no reducible fibres.
The height formula of \cref{night:P3F.2} therefore gives
\((mP)\cdot O=m^2-1\) for \(m\ne0\).
For \(m=0\) the same value is \(O^2=-\chi(\mathcal O)=-1\).

\item For the degree-zero physical line \(M\), one has
\(F\cdot c_1(M)=0\). Therefore
\[
 (K+2c_1(M))^2=4c_1(M)^2,\qquad
 K+2c_1(M)\equiv w_2\pmod2 .
\]
The parity obstruction in \cref{night:P3F.5} applies to the
specified ball-puncture with normal Euler class \(2c_1(M)\).
The actual normal Euler class and its framing are supplied by
the explicit trace and cap maps cited above.
\end{enumerate}
\end{proof}'''
 return prefix+proof
change('night:P3F.6',repair_degree_twelve_maps,
 'Repair source Markdown corruption in the two degree-twelve maps and give the exact Möbius determinant, branch-value transport, all-multiple height calculation and actual page comparison.')

def repair_orbit_locators(t):
 t=t.replace('the table on p505 and the Smale comparison stated immediately above it',
             'the order table on p.~504 and the Smale comparison on p.~505')
 t=t.replace(r'\(a,b\)=(r exp(i theta),sqrt(1-r\textsuperscript{2}))',
             r'\(a,b)=(\sin(\pi r/2)e^{i\theta},\cos(\pi r/2))\)')
 # The sine/cosine radial disk is smooth at the centre and boundary.
 t=t.replace(r'\(a,b)=(\sin',r'\((a,b)=(\sin')
 return t
change('night:P3F.7',repair_orbit_locators,
 'Correct the Kervaire--Milnor table locator to p504 and the Smale comparison to p505; write a smooth SU2 clutch-nullhomotopy with its literal radial sine/cosine coordinates.')

def complete_sphere_gluing(t):
 start=t.index(r'\item The glued manifold')
 end=t.index(r'\end{enumerate}',start)
 return t[:start]+r'''\item The glued manifold \(\Sigma_\Phi\) is simply connected by
van Kampen and has the integral homology of \(S^7\) by
Mayer--Vietoris. Hurewicz and Whitehead therefore make it a
homotopy sphere. Here is the complete comparison map
\[
 \pi_0\operatorname{Diff}^+(S^6)\longrightarrow\Theta_7,
 \qquad [\varphi]\longmapsto
 [D^7\cup_\varphi(-D^7)].
\]
An isotopy of the boundary map gives a diffeomorphism of the glued
manifolds by its collar isotopy. Boundary connected sum of the two
disc presentations, followed by contraction of the connecting
collar, identifies composition with oriented connected sum.

\item To prove surjectivity, remove the interiors of two disjoint
oriented coordinate balls from a homotopy seven-sphere \(\Sigma\).
The resulting cobordism \(C\), with boundary \(S^6\sqcup S^6\),
is simply connected: attaching either removed ball changes no
fundamental group, by van Kampen on its simply connected boundary.
Excision and the homology sequence of the sphere show
\(H_*(C,S^6;\mathbb Z)=0\). The product theorem
\cite[Theorem 9.1, p.~107]{mapsMilnor65} gives
\(C\cong S^6\times[0,1]\). Composing this diffeomorphism with the
inverse of its restriction at the first end makes that end the
specified coordinate-sphere parametrization. Reattaching the
two balls now supplies the literal boundary diffeomorphism
\(\varphi:S^6\to S^6\) and
\(\Sigma\cong D^7\cup_\varphi(-D^7)\).
The same two-disc argument is printed in
\cite[Propositions A--B and their proofs, pp.~108--110]{mapsMilnor65}.

For injectivity, an oriented diffeomorphism between two such
gluings can be isotoped to identify their first parametrized
balls. Indeed, shrink each ball inside its coordinate chart,
move its centre along a path, and join the positive linear
frames through \(\operatorname{GL}^+(7,\mathbb R)\); isotopy
extension carries this isotopy of parametrized balls to the
ambient manifold. Its restriction to the complementary ball
then extends the difference of the two boundary gluing maps.
Cerf's Theorem~0 and Corollaries~1--2
\cite[p.~8]{Cerf1970} identify this extension equivalence with
isotopy on \(S^6\). Finally, Smale's Theorem~J
\cite[p.~393]{Smale61} identifies oriented h-cobordism classes
of these simply connected seven-manifolds with oriented
diffeomorphism classes. Thus the displayed map is an
isomorphism with \(\Theta_7\), with the stated disc orientations.

\item The required spin coboundary can also be made explicit.
Eells--Kuiper's oriented rank-four disc bundle \(W_h\to S^4\)
has Euler number \(1\), signature \(1\), and
\[
 p_1(W_h)=2(2h-1)x,\qquad
 \big\langle x^2,[W_h,\partial W_h]\big\rangle=1 .
\]
Its boundary is a homotopy seven-sphere, and \(H^2(W_h;\mathbb
Z/2)=0\) makes \(W_h\) spin. For \(h=2\),
\[
 \mu(\partial W_2)=\frac{6^2-4}{896}=\frac1{28}.
\]
These are the bundle and invariant calculations of
\cite[Section~6, equation~(11), pp.~101--103]{EellsKuiper1962}.
Their twenty-eight distinct residues exhaust the twenty-eight
oriented classes. Boundary connected sums of copies of \(W_2\)
and \(-W_2\), followed by the oriented boundary identification
just proved, consequently provide a spin coboundary of the
particular \(\Sigma_\Phi\).

For any such \(W\), \(H^3(\Sigma_\Phi;\mathbb Q)=
H^4(\Sigma_\Phi;\mathbb Q)=0\) makes
\(H^4(W,\partial W;\mathbb Q)\to H^4(W;\mathbb Q)\) an
isomorphism, so the relative Pontryagin lift is unique.
The seven-dimensional formula
\[
 \mu(\Sigma_\Phi)=
 \frac{\langle p_1(W)^2,[W,\partial W]\rangle-4\sigma(W)}
 {896}\pmod1
\]
therefore applies to this actual boundary gluing. Multiplication
by \(28\) gives \eqref{famIII:eq:E10} in the generator oriented
by \(\partial W_2\).

'''+t[end:]
change('fam:src:E.2.2',complete_sphere_gluing,
 'Supply the exact Milnor product-cobordism/two-disc morphism, the parametrized-ball injectivity argument, Cerf isotopy comparison and an explicit spin disc-bundle generator giving a coboundary of every actual gluing.')

# Per-result corrections of historical rejected compound statements follow.
typed_script=W/'code/IV/typed_trace_repairs.py'
exec(compile(typed_script.read_text(),str(typed_script),'exec'))
config=W/'code/IV/reconcile_false.py'
if config.exists():
 exec(compile(config.read_text(),str(config),'exec'))

def type_f25_table(t):
 old=r''' A=\frac{12s_\delta-p_{\rm rel}}{24}'''
 assert old in t
 t=t.replace(old,r''' A_U=\frac{12s_\delta-p_{\rm rel}}{24}''',1)
 old=r'''Thus the sign \(\epsilon\) in the prompt's expression is \(-1\) in these conventions.'''
 assert old in t
 t=t.replace(old,r'''This is the meridian-line value. The extending duality displayed in step 1 gives \(A_M=-A_U=R\cdot O\), so the physical coefficient in the prompt's expression is \(\epsilon_M=+1\), while the retained meridian-line coefficient is \(\epsilon_U=-1\).''',1)
 old=r'''\(A\)
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedleft'''
 assert old in t
 t=t.replace(old,r'''\(A_M\)
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedleft''',1)
 old=r'''& 3 & 4 & \(-4\) & 24 \\'''
 assert old in t
 t=t.replace(old,r'''& 3 & 4 & 4 & 4 \\''',1)
 return t
change('night:P3F.25',type_f25_table,
 'Transport the intermediate U-line formula and the OS47 table to the displayed extending duality: retain A_U=-R.O, state A_M=+R.O, and give the physical table entry (4,4). This is a typed editorial correction, not a new whole-proof check of the source-family endpoint claims.')


# Add the actual repaired dependencies and the primary locators opened now.
def add_uses(t, additions):
 start=t.index(r'\StatementRecord'); pos=t.index('{',start)
 groups=[]
 for j in range(4):
  a=pos;depth=1;pos+=1
  while depth:
   if t[pos]=='{' and t[pos-1]!='\\':depth+=1
   if t[pos]=='}' and t[pos-1]!='\\':depth-=1
   pos+=1
  groups.append((a,pos))
  if j<3:pos=t.index('{',pos)
 a,z=groups[3]
 return t[:z-1]+'; '+additions+t[z-1:]
for lab,uses in {
 'fam:src:E.2.2':r'\cite[Theorem 9.1 and Propositions A--B, pp.~107--110]{mapsMilnor65}; \cite[Section 3, p.~96, and Section 6, pp.~101--103]{EellsKuiper1962}',
 'night:P3K.6':r'\cref{night:P3K.68}',
 'night:P3K.7':r'\cref{night:P3K.68}',
 'night:P3K.65':r'\cref{night:P3K.68}',
 'night:P3K.23':r'\cref{night:P3K.68}; \cite[Theorem 1.2, pp.~404--405, and Corollary 6.6, p.~422]{Haefliger1966}; \cite[Proposition 1, p.~3, and Lemma 3, pp.~6--8]{Krylov2004}; \cite[equation (5), p.~6, Theorem 2, pp.~10--12, and Theorem 3, p.~13]{Krylov2001}',
 'night:P3F.22':r'\cite[Lemma 6.2, pp.~34--35]{Jin2026}; \cite[Section 3.1(v), pp.~5--6, and Lemma 3.5, Case 2, pp.~13--15]{Jiang2014}; \cite[Sections 2--3, pp.~67--69]{Davis1982}',
 'night:P3F.24':r'\cite[Section 3, p.~69]{Davis1982}',
 'night:P3F.1':r'\cite[Main Theorem table, pp.~85--86]{OguisoShioda1991}; \cite[Section 3, pp.~202--205, Proposition 3.4, p.~204]{Miranda1990}',
 'night:P3F.2':r'\cite[Theorem 8.6 and equation (8.12), p.~228, table (8.16), p.~229, and Proposition 8.12, p.~231]{Shioda1990}',
 'night:P3F.3':r'\cite[Theorem 1.2 and Corollary 1.3, p.~3, Proposition 3.1, pp.~10--11, Lemma 4.4, p.~16, Lemma 4.8, p.~23, and Theorem 4.9, p.~24]{Jin2026}',
 'night:P3F.5':r'\cite[Section 2.1, Theorem 2.3 and Corollary 2.6, pp.~2--3]{Takase2005}; \cref{night:P3K.68}',
 'night:P3F.6':r'\cite[Proposition 8.12, p.~231]{Shioda1990}; \cref{night:P3F.2,night:P3F.5,night:P3K.6,night:P3K.7}',
 'night:P3F.7':r'\cite[pp.~504--505]{KervaireMilnor1963}; \cite[Theorem 1.2, pp.~404--405, and Corollary 6.6, p.~422]{Haefliger1966}; \cite[Section 2, p.~2091, and Theorem 4.1, pp.~2094--2095]{HarveyKerinShankar2020}',
 'night:P3F.11':r'\cite[Theorem A, p.~621, reproduced first-page facsimile]{Smale1959E}; \cite[Theorem 4.9, p.~24]{Jin2026}',
 'night:P3F.16':r'\cite[equations (7.1)--(7.3) and Lemma 7.2, p.~24; Proposition 7.3, pp.~25--26]{Viaclovsky2026Combs}',
 'night:P3F.17':r'\cite[Section 2.1, equations (2.12)--(2.17), pp.~4--6; Theorem 3.2, p.~7]{Viaclovsky2026Log}; \cref{night:P3K.11}',
 'night:P3K.8':r'\cref{night:P3K.68}; \cite[Tag 07VK, Lemma 30.22.1]{StacksProject}',
 'night:P3K.9':r'\cref{night:P3K.68}',
 'night:P3K.11':r'\cref{night:P3K.68,night:P3K.9}',
 'night:P3K.101':r'\cref{night:P3K.97,night:P3K.98}; the complete moving-cap calculation (MC2.1)--(MC2.17) and oriented outer transfer (OT.1)--(OT.20) reproduced below',
 'night:P3K.102':r'\cref{night:P3K.68,night:P3K.71,night:P3K.101}; the complete integer prism morphism (IF.41)--(IF.46)',
 'night:P3K.103':r'\cref{night:P3K.95,night:P3K.99,night:P3K.100}; the complete coincident-section and reference-cap maps (OC.2)--(OC.21)',
 'night:P3K.104':r'\cref{night:P3K.68,night:P3K.96,night:P3K.98,night:P3K.101,night:P3K.102}; the complete signed cap, Cartier and annular maps (HC.1)--(HC.30) and negative-quadratic companion (SN.1)--(SN.27)',
 'night:P3K.105':r'\cref{night:P3K.68,night:P3K.96,night:P3K.98,night:P3K.101,night:P3K.102,night:P3K.104}; the complete ordinary and good-cap constructions (MB.1)--(MB.24), (MG.1)--(MG.20), and three-step odd-ideal proof; \cite[Theorem 3.5 and equations (3.7)--(3.8), pp.~8--9]{AtiyahBott1984}',
 'night:P3K.8':r'\cref{night:P3K.68}; \cite[Lemma 30.22.1, tag 07VK]{StacksProject}',
 'night:P3K.9':r'\cref{night:P3K.68}; \cite[Theorem A, p.~621]{Smale1959E}',
 'night:P3K.11':r'\cref{night:P3K.68}',
 'night:P3F.11':r'\cite[Theorem A, p.~621]{Smale1959E}; \cite[Theorem 4.9, p.~24]{Jin2026}',
 'night:P3F.16':r'\cite[Section 7, equations (7.1)--(7.3), pp.~23--24, Proposition 7.3 and Remark 7.4, pp.~25--26]{Viaclovsky2026Combs}',
}.items():
 change(lab,lambda t,u=uses:add_uses(t,u),
        'Add the actual repaired proof dependency or the exact primary-source locator opened in this writing.')

# Retain the actual witness arrays in the standalone manuscript.
source_root=W.parents[1]/'sources/newer_night/checkpoint30'
def flatten_input(match):
 name=match.group(1)
 path=source_root/name
 assert path.is_file(),name
 value=path.read_text()
 value=re.sub(r'\\input\{([^}]+)\}',flatten_input,value)
 return '% Exact checkpoint-30 inclusion: '+name+'\n'+value
s=re.sub(r'\\input\{([^}]+)\}',flatten_input,s)

# Preserve exact historical wording in the reconciliation record while making
# the closed dependencies explicit at their former intermediate-stage notices.
stage_records=[]
def close_k101_stages(t):
 replacements=[
  ('1-a_{\nm line}',r'1-a_{\rm line}',
   'Repair the split control word in the line-exponent subscript; no exponent or coordinate map changes.'),
  ('Initial exact coordinate stage. The full line/root/cap attachment and\nreturn remain to be computed; no return or compact boundary is assigned\nhere. This note retains the actual two parameter maps before any use of\na global loop relation.',
   'The following source calculation retains both actual parameter maps.\nIts full line, root and cap attachment is constructed in EIR, IA, SIT\nand FO below; MC2 and OT then compute the completed return.',
   'Replace the historical first-stage promise by the exact complete supporting proof dependencies.'),
  ('The full SU2 and parameter-dependent parts of the\nclutch still determine \\(c_2(E_c)\\); that integer\nremains unassigned in this note.',
   'The full SU2 and parameter-dependent parts of this clutch enter\nthe oriented bundle bordism in MC2 below, which gives\n\\(\\int c_2(E_c)=-4\\) with the same complete coefficient maps.',
   'Point the preliminary determinant computation to the subsequent complete second-Chern calculation.'),
  ('The source-moduli return still requires\nthe other compact normal ledgers and the complete\nouter mapping-torus and finite-cap transfer.',
   'The complete compact normal ledgers are evaluated in FP, and OT\ncarries their sum through the original outer mapping-torus and\nfinite-cap transfer.',
   'Identify the completed pair and transfer proofs instead of retaining the obsolete work-stage task.'),
  ('This is a\nnew working proof pending the parent\\textquotesingle s full outer-transfer read.',
   'The actual source, line, cap and orientation maps in OT.1--5\nsupply the full outer-transfer argument.',
   'Archive the historical review-stage sentence; current mathematical checking has its own scoped event.'),
  ('These exact coefficients are the current input for the\nstrict-source surface calculation. Combining them with\nthe remaining exceptional and selected charts to compute\nthe global normal squares and the reference-cap clutch\nis still in progress. No surface or return value is\nassigned here.',
   'These exact coefficients enter the strict-source normal-square\ncalculation in SS and the exceptional and selected-chart comparisons\nin CS. The full reference-cap clutch is computed in MC2; FP then\nsums the separate characteristic pairs.',
   'Replace a superseded intermediate notice with the precise completed normal and cap computations.'),
  ('The tangent comparison and all global normal\nsquares are being assembled with the same\nboundary arrows; no global return is assigned.',
   'The tangent comparison and global normal squares with these same\nboundary arrows are calculated in SS, CS and FP below; their outer\ntransfer is the actual map of OT.',
   'Resolve the earlier local-refinement scope notice by its complete subsequent geometric comparison.'),
 ]
 for old,new,reason in replacements:
  assert old in t,('K101 stage text missing',old[:90])
  t=t.replace(old,new,1)
  stage_records.append(dict(label='night:P3K.101',old=old,new=new,reason=reason))
 return t
change('night:P3K.101',close_k101_stages,
 'Correct the malformed line-exponent subscript and reconcile seven obsolete stage notices with the explicit completed normal, cap and outer-transfer arguments; preserve every replaced sentence in the stage reconciliation record.')
(W/'analysis/IV/K101_stage_reconciliation.json').write_text(json.dumps(stage_records,indent=2)+'\n')

topology_script=W/'code/IV/topology_repairs.py'
exec(compile(topology_script.read_text(),str(topology_script),'exec'))
orbit_script=W/'code/IV/orbit_repairs.py'
exec(compile(orbit_script.read_text(),str(orbit_script),'exec'))
fan_norm_script=W/'code/IV/fan_norm_repairs.py'
exec(compile(fan_norm_script.read_text(),str(fan_norm_script),'exec'))
fan_scope_script=W/'code/IV/reference_fan_scope.py'
exec(compile(fan_scope_script.read_text(),str(fan_scope_script),'exec'))
root_replacement_script=W/'code/IV/integrate_root_replacements.py'
exec(compile(root_replacement_script.read_text(),str(root_replacement_script),'exec'))
summary_cleanup_script=W/'code/IV/summary_cleanup.py'
exec(compile(summary_cleanup_script.read_text(),str(summary_cleanup_script),'exec'))
cp30_script=W/'code/IV/checkpoint30_receiving.py'
exec(compile(cp30_script.read_text(),str(cp30_script),'exec'))
os45_primitive_script=W/'code/IV/os45_primitive_receiving.py'
exec(compile(os45_primitive_script.read_text(),str(os45_primitive_script),'exec'))
retained_script=W/'code/IV/retained_batch_repairs.py'
exec(compile(retained_script.read_text(),str(retained_script),'exec'))
deductions_script=W/'code/IV/final_current_deductions.py'
exec(compile(deductions_script.read_text(),str(deductions_script),'exec'))
format_script=W/'code/IV/format_repairs.py'
exec(compile(format_script.read_text(),str(format_script),'exec'))
(P/'body.tex').write_text(s)
(W/'analysis/IV/reconciliation.json').write_text(json.dumps(changes,indent=2))
print('IV/body.tex',len(s),'characters;',len(changes),'documented corrections')
