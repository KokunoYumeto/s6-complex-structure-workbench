from pathlib import Path
import hashlib,json,datetime

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
before=HERE/'S6_SERIES_PUBLISH_II_01GL_current_original.tex'
text=before.read_text()
guards=[]

def replace(old,new,kind,reason,count=1):
    global text
    assert text.count(old)==count,(len(guards)+1,text.count(old),old)
    guards.append(dict(change_id=f'II-REC-C12-01GL-{len(guards)+1:02d}',
                       defect_type=kind,old=old,new=new,
                       expected_occurrences_in_owning_block=count,reason=reason))
    text=text.replace(old,new)

replace(r'''\cite[Proposition labelled
\texttt{prop: surface facts}]{LiuRollenske2026}''',
        r'''\cite[Proposition~2.1]{LiuRollenske2026}''','D06,D18',
        'Replace source-label prose by the exact proposition number in the bound arXiv v2 source and compiled aux.',2)
replace(r'''\cite[Theorem labelled \texttt{thm: main}]{LiuRollenske2026}''',
        r'''\cite[Theorem~5.1]{LiuRollenske2026}''','D06,D18',
        'Use the exact numbered topology theorem in the cited v2 edition.',2)
replace(r'''\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]''',
        r'''\begin{enumerate}[label=\arabic*.,leftmargin=*]''','D04,D23',
        'Replace the iteration marker by ordinary proof-step numbering.')
replace(r'''\item We derive the needed holomorphic invariants from the local models.
The commented-out holomorphic-invariants notes in the supplied
Liu--Rollenske source are not used as established results.

''','','D01,D02,D08',
        'Remove the source-workflow and omitted-notes announcement; the entire mathematical construction follows.')
replace(r'''It gives $y^2=x^3+tx+t$, with section $P=(-1,i)$; the multiple''',
        r'''Put $k=27/4$. Near $t_{\rm old}=0$, the new infinity coordinates are
$x_{\rm old}/[k(1-t_{\rm old})]^2$ and
$y_{\rm old}/[k(1-t_{\rm old})]^3$, and its base coordinate is
$t_{\rm old}/[k(1-t_{\rm old})]$. Near $t_{\rm old}=\infty$, put
$v=t_{\rm old}^{-1}$; the new fibre coordinates are
$v^2x_{\rm old},v^3y_{\rm old}$ and the new base coordinate is $k(v-1)$.
These charts extend the displayed maps to an isomorphism of the
Weierstrass models and their minimal resolutions, preserving $O$ and $P$.
They identify $\mathcal O(P-O)$ and its lifted translation; using the
transported linearization preserves the scale $u$.
The new equation is $y^2=x^3+tx+t$, with section $P=(-1,i)$; the multiple''',
        'D13','Supply the actual global coordinate and line-bundle transport at the two omitted affine-chart points.')
replace(r'''Its finite discriminant is $4t^3+27(t+\epsilon)^2$.
The nodal value''',
        r'''Its finite discriminant is $4t^3+27(t+\epsilon)^2$, whose discriminant
as a cubic in $t$ is $314928\epsilon^3(1-\epsilon)$.
The nodal value''','D13',
        'Bind the exact collision calculation supporting the stated three-node and cusp-splitting domains.')
replace(r'''\item These equations give a simultaneous construction of the compact
threefolds, including the central one. On a disc containing the cusp''',
        r'''\item On a disc containing the cusp''','D08',
        'Begin with the actual local family and retain the complete simultaneous-construction argument.')
replace(r'''there. The line bundle $\mathcal O(P_\epsilon-O)$ and its lifted
translation vary holomorphically; its multiplier has a zero only
at the separate simple nodal value chosen for the hexagonal filling.''',
        r'''there. Put $M_\epsilon=\mathcal O(P_\epsilon-O)$ and let $c(\epsilon)$
be the simple nodal value continuing $-27/4$. The identity
$\mathcal Hom(t_{2P}^*M,M)\simeq\mathcal O(F)$ in
\cite[Proposition~2.1]{LiuRollenske2026} persists in the smooth family
of elliptic surfaces: $H^1(\mathcal O)=H^2(\mathcal O)=0$ centrally
and nearby, so the exponential sequence identifies their Picard
groups with the fixed integral $H^2$ lattice. The two line bundles
have the same Chern class throughout the family. Their ratio is
trivial on every surface; Grauert's theorem makes this trivialization
holomorphic in $\epsilon$. The section of $\mathcal O(F_{c(\epsilon)})$
with divisor $F_{c(\epsilon)}$ therefore gives a holomorphic lifted
translation, agreeing with the original one at $\epsilon=0$.''',
        'D13','Write the precise line-bundle isomorphism and its relative trivialization needed for the simultaneous quotient.')
replace(r'''differentiable type by Ehresmann. The supplied topology theorem''',
        r'''differentiable type by Ehresmann. The topology theorem''','D01',
        'Remove the description of the source as supplied.')
replace(r'''\item Write $\mathfrak B=\mathbb P(1,4)$ and retain its convention
$\rho^*\mathcal O(1)=\mathcal O(4)$. On the central threefold the''',
        r'''\item Let $B$ be the reduced multiple fibre, so $f^*(\infty)=4B$.
The line $\mathcal O_Y(B)$, its canonical section and the isomorphism
$\mathcal O_Y(4B)\simeq f^*\mathcal O_{\mathbb P^1}(\infty)$ define
the root factorization $\bar f:Y\to\mathfrak B=\mathbb P(1,4)$.
For the coarse projection $\rho:\mathfrak B\to\mathbb P^1$ one has
$f=\rho\bar f$ and
$\rho^*\mathcal O_{\mathbb P^1}(1)=\mathcal O_{\mathfrak B}(4)$.
On the central threefold the''','D13',
        'Define the actual root morphism, its coarse projection and the line-bundle convention locally used by the proof.')
replace(r'''The finite-cover and hexagonal calculations are the same explicit
coordinate calculations as in \ref{cdp:st:E13}. Since the elliptic surface has''',
        r'''In a hexagonal chart $xyz=t-c(\epsilon)$, the form
$d\log x\wedge d\log y\wedge dt$ is $dx\wedge dy\wedge dz$.
At infinity the substitution
$t=r^{-4}$, $x=r^{-2}x'$, $y=r^{-3}y'$ gives the factor $-4r^{-4}$
in the surface form. The good three-form is invariant under the
free order-four affine action and descends to a nonvanishing frame.
These are the local canonical maps used in \ref{cdp:st:E13}.
Since the elliptic surface has''','D13',
        'State the actual finite and root-chart canonical-form transports, without extending E13 beyond its stated parameter domain.')
replace(r'''The same proof and good-reduction substitution as
in \ref{cdp:st:E13} give the logarithmic Lie bundle
$E=\mathcal O\oplus\mathcal O(-1)$, including at the central
cusp.''',
        r'''For a vector $V$ dual to $dx/(2y)$, the horizontal lift is
$\widetilde V=V-\alpha(V)v\partial_v$. The multiplicative
connection commutes with the lifted translation, by the normalized
group-law comparison in \ref{cdp:st:E13}. On the good-reduction
chart its relative form is
\[
 \alpha=\frac{y'+br^3}{x'+r^2}\frac{dx'}{2y'},\qquad
 \frac{dx}{2y}=r\,\frac{dx'}{2y'}.
\]
Together with the scalar vector $v\partial_v$, this transition gives
the logarithmic Lie bundle $E=\mathcal O\oplus\mathcal O(-1)$.''',
        'D13','Make the horizontal-lift and root-frame morphisms explicit for this exact elliptic equation.')
replace(r'''\item We justify the identification with $G=R^1\bar f_*\mathcal O$
at the cusp without assuming a limiting-period rule there.
The inverse pairing''',
        r'''\item Put $G=R^1\bar f_*\mathcal O$. The inverse pairing''',
        'D02,D08','Retain the exact Hartogs comparison while removing its announcement and defensive qualification.')
replace(r'''The inverse pairing associated with the invariant alternating
class gives $G\simeq E$''',
        r'''The inverse pairing associated with the invariant alternating
class gives $G\simeq E$''','D13',
        'Identity placeholder prohibited; this entry is removed below.')
# Do not retain a no-op as a publication edit.
guards.pop()
replace(r'''all remaining points
are smooth, nodal or the finite-cover points already computed in
\ref{cdp:st:E13}.''',
        r'''at a smooth fibre it is the pairing
$H^1(F,\mathbb C)/F^1\to(F^1)^*$; at a nodal fibre its quotient
frame consists of the graph-loop class and the elliptic normalization
class; and the good-reduction cover gives the frame at infinity.
These local pairing and normalization maps are the ones in
\ref{cdp:st:E13}, applied to the displayed connection and root transition.''',
        'D13','Specify the local morphisms used away from the cusp rather than invoking the small-parameter theorem as a family identification.')
replace(r'''with the branches equal to one at
zero, and then renaming the two new coordinates.''',
        r'''with the branches equal to one at
zero, and then renaming the two new coordinates only for this local
logarithmic-module calculation.''','D13',
        'Bound the local coordinate renaming so subsequent critical-curve equations retain their Weierstrass coordinates.')
replace(r'''\item The quotient at $W$ is $\eta_*K_{dP_6}$ with cohomology $(0,0,1)$.''',
        r'''\item Return to the Weierstrass coordinates. The preceding coordinate
change preserves the ideal $(x^2,y)$ and induces the identity on
$\mathbb C[x]/(x^2)$, since $\widetilde x\equiv x\bmod x^2$.
The quotient at $W$ is $\eta_*K_{dP_6}$ with cohomology $(0,0,1)$.''',
        'D13','Prove the exact ideal and jet-coordinate transport after the temporary logarithmic coordinate change.')
replace(r'''$N_{C/Y}=\mathcal O_C$. Put $Z=V(J)\subset C$. We now compute
the actual restriction map''',
        r'''$N_{C/Y}=\mathcal O_C$. Put $Z=V(J)\subset C$ and consider
the restriction map''','D08',
        'Remove the computation-status announcement while retaining the definition and the exact map.')
replace(r'''On $\Gamma\setminus\{0\}$ the calculation of \ref{cdp:st:E13} identifies it,
after a nonzero scalar change of target frame, with the row''',
        r'''At a node with coordinate $x$, the toric Lie line is generated by
$\widetilde V+\frac{b}{1+x}v\partial_v$: the horizontal lift has
line-coordinate component $-\alpha(V)=-b/(1+x)$ at that node.
The quotient to the elliptic Lie line, and hence the normalization
restriction under the pairing above, therefore sends
$(v\partial_v,\widetilde V)$ to
$(1,-b/(1+x))$, up to a common nonzero factor. This is the local
map in \ref{cdp:st:E13}. Thus on $\Gamma\setminus\{0\}$ restriction,
after a nonzero scalar change of target frame, has the row''',
        'D13','Derive the particular normalization functional for this family instead of silently transporting the E13 parameter range.')
replace(r'''The same frame can be chosen at zero. To check this last point,
normalize $C$. Its normalization is a $\mathbb P^1$-bundle''',
        r'''The normalization of $C$ is a $\mathbb P^1$-bundle''',
        'D08','Begin directly with the normalization used to prove extension of the target frame.')
replace(r'''It is a unit. This
proves the asserted holomorphic target-frame comparison.''',
        r'''It is a unit.''','D08',
        'Remove the empty closing recap after the unit argument.')
replace(r'''This is the required jet comparison, not an inference from the
rank at nearby reduced fibres.
''','','D02,D08',
        'Remove the negative proof-status recap after the explicit nonreduced-fibre matrix calculation.')
replace(r'''\item It remains to verify that the actual two-parameter family has
bijective Kodaira--Spencer map. In the above local trivialization
of its total space the map to the base is''',
        r'''\item In the above local trivialization
of the total space the map to the base is''','D08',
        'Start the Kodaira--Spencer computation with its exact local map.')
replace(r'''The inverse-function argument of \ref{cdp:st:E13} consequently makes the
Kuranishi ideal zero and proves miniversality. \ref{cdp:st:E6} and \ref{cdp:st:E1} give the
remaining assertions.''',
        r'''Present the Kuranishi local ring as
$\mathbb C\{z_1,z_2\}/I$. The classifying map of the constructed
bidisc, followed by the embedding in $H^1(T_Y)$, has invertible
differential and is a local analytic isomorphism by the inverse
function theorem. Every element of $I$ pulls back to zero, so $I=0$.
This is the ideal argument of \ref{cdp:st:E13}, and it proves that
the displayed family is locally miniversal over the full reduced germ.
The rank-two hypothesis in \ref{cdp:st:E6} is supplied for this
Liu--Rollenske construction by \ref{cdp:st:E7}. Thus all sufficiently
small deformations retain their torus fibration.
Their second Betti number remains zero, and \ref{cdp:st:E1}
identifies their meromorphic function field with the pullback of
$\mathcal M(\mathbb P^1)$, giving algebraic dimension one.''',
        'D13','Write the exact analytic-ideal argument and bind the fibration-retention hypothesis to the already completed E7 construction.')

out=HERE/'S6_SERIES_PUBLISH_II_01GL_proposed_v1.tex'
assert not out.exists()
out.write_text(text)
def bind(p):
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
receipt={'schema_version':1,'paper':'II','tag':'01GL','statement_owner':'cdp:st:E14',
         'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'original_full_block':bind(before),'proposed_full_block':bind(out),
         'guards':guards,'canonical_mutations':0,'events_added':0,
         'status':'preparation; final full-pair reading and comparison binding remain pending'}
path=HERE/'S6_SERIES_PUBLISH_II_clean_group12_preparation_v1.json'
assert not path.exists()
path.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'preparation':bind(path),'proposal':bind(out),'guard_count':len(guards),
                  'literal_occurrences':sum(x['expected_occurrences_in_owning_block'] for x in guards)}))
