"""Publication edits of the wholly read LF/LJ repaired unit."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units

root=Path(__file__).resolve().parent.parent
p=root/'agents/continuation8_iii_integration/units/weighted/three_primary_types.tex'
lane=root/'agents/continuation8_iii_weighted_units'
original=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='7ce8d5629d5faeeab749ec554c4aede2162704d65f35d0035b734375106457b9'
text=original
edits=[]
new_labels=[]
new_targets=[]
equations={}

def replace(owner,old,new,kinds,reason,count=1):
 global text
 assert text.count(old)==count,(owner,old[:160],count,text.count(old))
 for _ in range(count):
  a=text.index(old)
  edits.append((owner,kinds,text.count('\n',0,a)+1,old,new,reason))
  text=text[:a]+new+text[a+len(old):]

def between(start,stop):
 a=text.index(start);b=text.index(stop,a);return text[a:b]

def identity(tag,label):
 new_targets.append('tag-'+tag);new_labels.append(label)
 return r'\hypertarget{tag-'+tag+r'}{}\label{'+label+'}'

# LF's full input table and actual surgery model precede one theorem.
end=text.index(r'\end{theorem}')+len(r'\end{theorem}')
old=text[:end]
ta=old.index(r'\[');tb=old.index(r'\]',old.index(r'\label{maps:eq:D.T31}'))+2
table=old[ta:tb]
ma=old.index(r'\[',tb);mb=old.index('The complete Zhubr data are',ma)
model=old[ma:mb].replace('For example it is the graph of the degree-three map','Take the graph of the degree-three map')
result=old[mb:]
definition=r'''\subsection{Three-primary smooth types}

\subsubsection{Order three}

\begin{definition}[Minimal order-three data]'''+identity('Q223','maps:def:minimal-three-data')+r'''
{\normalfont\scriptsize tag Q223}\par
Use the ordered elliptic data of
Definition~\ref{mapsIII:def:elliptic-marked-data} and choose a pattern
below. Use the prescribed primitive Mumford fan at every multiplicative
site, the listed additive cap and ordinary clutch $e\gamma$,
$e\in\mathbb Z$. The logarithmic sites are precisely the listed
additive sites. At a finite site of linear monodromy order $d_i$,
allow every multiplicity $m=d_i k$, $k>0$, and every free affine lift.
Selected positions are $i-1$ in the input definition's peripheral order.

'''+table+'\n\n'+model+r'''These choices are the \emph{minimal order-three data}.
\end{definition}

\begin{theorem}[Order-three smooth type]\hypertarget{tag-02LF}{}\label{maps:src:D.2.39}
{\normalfont\scriptsize tag 02LF}\par
Every simply connected output $X$ of
Definition~\ref{maps:def:minimal-three-data} is orientation-preservingly
diffeomorphic to $M_{3,0}$ with the marking specified in the proof.
'''+result
replace('LF',old,definition,'D04;D05;D10;D11;D13;D14;D16;D26',
 'Put all eight patterns/seven rows, full finite multiples and affine lifts, ordinary clutch, prescribed fans and the actual degree-three graph surgery in Q223. Preserve T31/T32/T33 and the full marked classification in one theorem.')

# Label the already proved universal identities used again by LJ.
lf_specs=[
 ('Q224','maps:eq:three-primary-homology',r' H_5(K(\mathbb Z/3,2);\mathbb Z)=0,'),
 ('Q225','maps:eq:third-power-detector',r' Q_3:H^2(-;\mathbb F_3)\longrightarrow'),
 ('Q226','maps:eq:third-power-cochain',r' P_3(v)=(v^3,0)+(\Sigma^*v^2\delta v,1)'),
 ('Q227','maps:eq:third-power-suspension',r'                      Q_3(\sigma v)=0,'),
 ('Q228','maps:eq:three-primary-bordism',r' \Omega^{\mathrm{Spin}}_6(K(\mathbb Z/3,2))')]
for tag,label,marker in lf_specs:
 at=text.index(marker);a=text.rfind(r'\[',0,at);b=text.index(r'\]',at)+2
 old=text[a:b]
 new=old.replace(r'\[',r'\begin{equation}',1)
 new=new[:-2]+identity(tag,label)+'\n'+r'\end{equation}'
 replace('LF',old,new,'D06;D10;D19','Give the retained universal identity its own live equation label and fresh Q2 tag, so the identical target calculation is proved once and reused precisely.')

# LJ's input is the actual natural minimal construction, not its output table.
old=between(r'\begin{theorem}[the mixed','The complete oriented table is')
model_a=old.index(r'\[');models=old[model_a:]
new=r'''\subsubsection{Orders six, fifteen and thirty}

\begin{definition}[Mixed three-primary data]'''+identity('Q229','maps:def:mixed-three-data')+r'''
{\normalfont\scriptsize tag Q229}\par
Use the ordered data of Definition~\ref{mapsIII:def:elliptic-marked-data}
and the natural initial pairs of \ref{maps:src:D.2.22}. Choose minimal
additive fillings of \ref{maps:src:D.2.26} with residual
$c\in\{6,15,30\}$ and trivial orbifold obstruction. Use the prescribed
primitive Mumford fan at every multiplicative site. The logarithmic
sites are precisely the chosen additive sites. At a finite site of
linear monodromy order $d_i$, allow $m=d_i k$ for every $k>0$ and
every free affine lift; retain every ordinary integer clutch $e\gamma$.
All orientations are the complex orientations. Selected positions are
$i-1$ in the input definition's peripheral order.

Use $M_0,M_1$ from Definition~\ref{maps:def:minimal-two-data},
$M_{3,0}$ from Definition~\ref{maps:def:minimal-three-data}, and
$Z_{5,\epsilon}$ from Definition~\ref{maps:def:minimal-mixed-data},
with their stated primitive markings. Put
'''+models+r'''
These choices are the \emph{mixed three-primary data}.
\end{definition}

\begin{theorem}[Mixed three-primary smooth types]\hypertarget{tag-02LJ}{}\label{maps:src:D.2.42}
{\normalfont\scriptsize tag 02LJ}\par
The data of Definition~\ref{maps:def:mixed-three-data} give fourteen
patterns. Every simply connected output has the oriented type below
for every permitted finite multiplicity, affine lift and ordinary clutch.
'''
replace('LJ',old,new,'D04;D05;D10;D11;D13;D14;D16;D26',
 'Define the complete natural minimal residual6/15/30 inputs in Q229, with unrestricted allowed finite/affine parameters. Reuse the actual earlier models through their unchanged primitive markings; preserve the complete corrected14-row classification and all full invariants.')
replace('LJ','Zero positions use the recorded zero-based indexing.','Selected positions use the index $i-1$ of\nDefinition~\\ref{mapsIII:def:elliptic-marked-data}.','D04;D06;D20','State the exact input-index map and its inverse, instead of a recorded-array convention.')
replace('LJ','At the selected cusp write its raw data as','At the selected cusp write its marked data as','D04;D08','Use the mathematical component marking.')

# The universal K(Z/3,2) target and operation are literally the earlier
# objects, with the coefficient-generator identity e <-> e3.
old=between('The primary divided-power computation gives','Restrict the whole-circle \\(U_3\\) of Section 8')
new=r'''Use the coefficient map $e\mapsto e_3$ on $\mathbb Z/3$,
with inverse $e_3\mapsto e$. The induced Eilenberg--Mac Lane map
identifies the positive reduction generator in
\eqref{maps:eq:three-primary-homology} with $\gamma_3(e_3)$.
Under this same map the detector is
\eqref{maps:eq:third-power-detector}, with coefficient map
$\gamma_3(e_3)\mapsto1$ and inverse $j\mapsto j\gamma_3(e_3)$.
The coefficient-one cochain construction is
\eqref{maps:eq:third-power-cochain}, and the left-interval suspension
and its slant inverse are those of
\eqref{maps:eq:third-power-suspension}. These are statements about
the same universal target and natural operation. Applying them to the
classifying map for $U_3$ therefore retains the complete $\mathbb Z/9$
coefficient group. The fixed curves and their restrictions for the
present data are computed below.

'''
replace('LJ',old,new,'D06;D11;D12;D17;D22;D27',
 'Remove the repeated K(Z3,2), detector and odd-suspension derivation only through e↔e3 and the same positive CP3 generator, coefficient-one operation and signed interval map. Earlier LF proves these universal target statements; LJ retains its own14-row geometry. Thomas general cochain source scope is recorded in the review; the used specialization is p3,m1.')
equations.update({72:('Q224','maps:eq:three-primary-homology'),73:('Q225','maps:eq:third-power-detector'),74:('Q226','maps:eq:third-power-cochain'),75:('Q227','maps:eq:third-power-suspension')})
old=between('For completeness the three-primary spin-bordism map is','\\paragraph{11. Refined Pontryagin coordinates')
new=r'''Compose the actual classifying map $X\to K(\mathbb Z/c,2)$
with reduction $s\mapsto e_3$. The target group and maps are exactly
\eqref{maps:eq:three-primary-bordism}; its inverse fundamental-class
map is $j\gamma_3(e_3)\mapsto j\zeta$. This applies to the resulting
bordism class of this map because the calculation is a target-group
isomorphism. The full zero coordinate just computed forces $j=0$,
hence also $P=0$. The resulting three-primary bordism class is the
class of the actual $M_{3,0}$ of
Definition~\ref{maps:def:minimal-three-data}.

'''
replace('LJ',old,new,'D06;D11;D12;D17;D22;D27',
 'Reuse the identical target-group isomorphism with its explicit inverse after the actual coefficient projection Zc→Z3. This retains the arbitrary-source scope and never assumes H2(X)=Z3.')
old=between('The order-two model \\(M_1\\) and its positive cube','Puncture the model manifolds in oriented discs')
new=r'''The models in Definitions~\ref{maps:def:minimal-two-data},
\ref{maps:def:minimal-three-data} and
\ref{maps:def:minimal-mixed-data} have their original orientations,
normal framings and primitive generators. The degree-two tube,
degree-three graph and positive conic are the identical embeddings
used in their defining proofs. Their generator identifications are
the identity, with the identity inverse. Those proofs give
$(P,h)(M_t)=(te_2,t\gamma_3(e_2))$, $(P,h)(M_{3,0})=(0,0)$,
and $(P,h)(Z_{5,\epsilon})=(\epsilon e_5,0)$, with simple
connectivity, spin and zero free third homology. We now transport
these complete marked classes through the actual connected sums.

'''
replace('LJ',old,new,'D06;D11;D12;D17;D22;D27',
 'Remove the repeated surgery-trace derivations only after identifying the same embeddings, unique framings, positive generator, trace maps and complete P/h data with LB,LF,LC. Retain the entire new connected-sum construction, marking inverse and recognition.')

# Put full coefficient/CW maps before the first full invariant use.
crt=between(r'\paragraph{12. Full coprime homotopy, detector, and bordism maps.}',r'\paragraph{13. Marked connected sums, recognition, and the refined count.}')
crt_new=crt.replace('Substitution of (85),(87),(88) proves (3).','The computed primary evaluations will determine (3) through these maps.')
crt_new=crt_new.replace('They give \\(P_6=3t\\), \\(P_{15}=3\\epsilon\\), \\(P_{30}=15t\\).','These are the inverse maps for the refined primary coefficients.')
replace('LJ',crt,'','D14','Move the entire coprime CW/CRT/bordism construction before its use; no part of its homotopy inverse or full detector maps is deleted.')
where=r'\paragraph{9. The full order-nine detector and localization.}'
replace('LJ',where,crt_new+'\n'+where,'D14;D22','Prove the full coprime map and its inverse before reconstructing any complete invariant. The later primary evaluations use this established map.')
replace('LJ','Naturality and the exact CRT maps in Section 12 now determine \\(P_c\\)\nas in the table.',
 r'''The exact CRT maps now give $P_6=3t$, $P_{15}=3\epsilon$ and
$P_{30}=15t$. Substitution of (85),(87),(88) into (98) gives
the full fundamental-class coefficients in (3).''',
 'D06;D14;D22','Apply the already proved CRT inverses after all actual primary evaluations; retain the full18/45/90 class, not merely its ordinary cube.')

# Remove production prose while retaining each exact mathematical fact.
changes=[
 ('Use only the defining matrices, section cocycles, component coordinates,\nand heights in the authorized raw fixture.',
  'Use the ordered matrices, section cocycles, component coordinates\nand heights of Definition~\\ref{mapsIII:def:elliptic-marked-data}.','D04;D05;D06;D09','Use the mathematical input definition rather than an authorized fixture.'),
 ('In the raw\ncomponent group','In the marked\ncomponent group','D04;D08','Name the component marking.'),
 ('conditions established in the admitted KX construction.','conditions of \\ref{maps:src:D.2.22}.','D06;D07','Use the earlier mathematical statement, not admission status.'),
 ('The positive-valuation Tate labelling sends the raw component label','The positive-valuation Tate labelling sends the input component label','D04;D20','Retain the exact reflection of the specified component coordinate.'),
 ('Thus the raw enumeration does not change the\nphysical sign of \\(G\\).','Thus this enumeration retains the physical sign of \\(G\\)\nthrough the displayed reflection.','D08;D22','State the actual sign transport.'),
 ('The admitted L1 cap and rank maps prove these criteria.','The cap and rank maps of \\ref{maps:src:D.2.26} prove these criteria.','D06;D07','Cite the actual primitive/original/finite cap result.'),
 ('The program expands these choices over the sixteen nonstar profiles,\nthen selects \\(c\\in\\{6,15,30\\}\\); it does not use the target table as\nits input. It obtains exactly the fourteen rows of the theorem.',
  'Expanding these choices over the sixteen nonstar profiles and\nretaining $c\\in\\{6,15,30\\}$ gives exactly the fourteen patterns\nin \\eqref{maps:eq:D.MT1}.','D01;D07;D09;D21','Keep the complete finite exhaustion from explicit component equations; move program-input history to records.'),
 ('Every profile has generator height \\(1/30\\). There is at most one\nadditive site. The raw matrices and cocycles, including all nonzero\nentries, are printed for every row in the new output.',
  'Each of these profiles has generator height $1/30$ and at most\none additive site. Its matrices and cocycles are the ordered entries\nof Definition~\\ref{mapsIII:def:elliptic-marked-data}.','D04;D06;D09','Locate the complete actual matrices and cocycles without saved-array output.'),
 ('The program checks integrality, both inverse products,\n\\(T_i^*\\omega=\\omega\\), \\(T_i\\delta=\\delta\\), \\(\\chi T_i=\\chi\\),\nand the ordered product \\(\\prod T_i=I\\).',
  'Substitution gives integral matrices and both inverse products,\n$T_i^*\\omega=\\omega$, $T_i\\delta=\\delta$, $\\chi T_i=\\chi$,\nand the ordered product $\\prod T_i=I$.','D07;D09;D21;D22','State the exact finite matrix identities and their substitution proof; the retained computation is corroborating evidence.'),
 ('The retained literal integer section \\(R_2\\) satisfies','Tracked integer row and column reduction gives a section $R_2$ satisfying','D08;D09;D22','Specify the actual constructive integer reduction.'),
 ('Its sparse representation prints every nonzero entry; its full matrix\nis recovered by inserting zero elsewhere. Thus the inverse quotient maps\nare','Its columns give the monodromy-cylinder preimages. The inverse quotient maps\nare','D09;D22','Retain the chain interpretation of the right inverse instead of its sparse serialization.'),
 ('For \\(B=[j_iF_i]\\), the output retains \\(V_0,Q_0,R_G\\) such that','For $B=[j_iF_i]$, the tracked integer reductions give $V_0,Q_0,R_G$ with','D09;D22','Define the graph maps by the stated integral construction.'),
 ('of \\(D\\); its three nonzero Smith entries are one. The program checks\neach equation and that every nonzero Smith entry of \\(B\\) is one, with\nnullity one.','of $D$; its three nonzero Smith entries are one. The same reduction\nof $B$ has unit nonzero Smith entries and nullity one.','D09;D21;D22','State the exact integral image/index facts used by the graph inverse.'),
 ('The normalized toric conductor sequence gives these exact cycles and\nthe normal chains bounding both fixed sweeps. The program verifies each\nfibre map, its integral section and its vanishing on the Wang image.',
  'The normalization/conductor sequence gives these cycles and\nthe normal chains bounding both fixed sweeps. Substitution in the\ndisplayed sections gives the identity and their Wang-image vanishing.','D09;D21;D22','Give the actual cycle and section identities.'),
 ('This is the admitted same-germ product/mapping-torus construction.','These inverse maps identify the original cap and its indicated mapping torus.','D07;D22;D27','Refer to the actual roof and line maps, with all units retained.'),
 ('The program retains these sections. The fixed basis is','These two sections recover the stated generators. The fixed basis is','D09;D22','Keep the actual integral section conclusion.'),
 ('The program retains an integral right inverse of\n\\([T-I\\mid\\beta_0\\mid\\ell]\\) and a literal \\(y\\) with','Integer reduction of $[T-I\\mid\\beta_0\\mid\\ell]$ gives a right\ninverse and an integral $y$ with','D09;D22','Use the explicit integer construction for the finite coinvariant inverse.'),
 ('The program proves (33)--(34) symbolically for both signs, with no\nbound on \\(m,e,r\\).','Substituting $A_0=\\varepsilon e$, $B_0=-\\varepsilon$ and\n$me-n=\\varepsilon$ proves (33)--(34) for both signs and all\nintegers $m,e,r$ in the stated domain.','D09;D21;D22;D26','Retain the all-parameter identities with their direct symbolic reason.'),
 ('All these integral matrices and their inverses are retained in the output.','Their determinants are one; the displayed products with their inverse matrices are the identity.','D09;D22','Replace output retention with the actual inverse calculation.'),
 ('point on the ruled normalization. The new raw calculation gives,\nfor every \\(p\\in\\{2,3,5\\}\\) dividing \\(c\\), exactly one such site,','point on the ruled normalization. Substitution of the ordered\ncomponent data gives, for each $p\\in\\{2,3,5\\}$ dividing $c$, exactly one such site,','D01;D04;D09;D22','Use the actual finite component criterion.'),
 ('The full basis and its inverse\nare printed. This prevents an inference of fixed points from the\nnonprimitive physical first period.','The displayed basis and its inverse identify that primitive\nconductor and its nontrivial scalar translation.','D08;D09;D22;D27','State the actual geometric implication of the retained primitive matrix.'),
 ('The program proves the identity symbolically. The inverse period map','Direct expansion proves the identity. The inverse period map','D09;D21;D22','Use the explicit polynomial pullback and its inverse.'),
 ('The program retains the integer section','Integer reduction of these angular columns gives the section','D09;D22','Keep the constructive integer section rather than program bookkeeping.'),
 ('The admitted divided-power result gives','The order-two projection in \\eqref{maps:eq:MP_local_61} and the\norder-five calculation of \\ref{maps:src:D.1.10} give','D06;D07','Supply exact previously proved homology/projection locators.'),
 ('checks the middle equality from the raw \\(\\kappa_i\\), then recovers','gives the middle equality from the marked $\\kappa_i$ and recovers','D04;D09;D22','Retain the independent physical-weight identity and exact generator conversion.'),
 ('For completeness the raw physical weights in the current rows are:','The physical weights in the fourteen patterns are:','D04;D08','Identify the actual finite table.'),
 ('For the two-primary projection use the exact primary quotient read\nin Zhubr §§3.7,3.12, printed pp.803,807:','For the two-primary projection use Zhubr\'s exact quotient\n\\cite[Sections~3.7 and~3.12, pp.~803,807]{manZhubr75}:','D06;D07;D18','Use a scholarly source locator rather than a reading-history clause.'),
 ('orders are the inverse maps; the program verifies both composites\non every element.','orders are the inverse maps: each displayed coefficient has residue\none in its own factor and zero in the other factors.','D09;D21;D22;D27','Give the exact arithmetic proof of both CRT composites.'),
 ('and \\(v^3\\) on \\(\\mu\\). The second program verifies these identities\nfor all units at the three relevant orders.','and $v^3$ on $\\mu$.','D09;D21','Retain the preceding all-unit algebraic proof; move the checking program to records.'),
 ('The program verifies both composites on every coefficient.','Substitution in each row gives $\\Phi^{-1}\\Phi=1$ and\n$\\Phi\\Phi^{-1}=1$ on every coefficient.','D09;D21;D22;D27','State the actual marking inverse calculation.')]
for old,new,kinds,why in changes: replace('LJ',old,new,kinds,why)
tail=between(r'\paragraph{14. Exact arithmetic checks.}',r'\end{proof}')
replace('LJ',tail,'','D01;D07;D08;D09;D21','Move all program paths and exact finite execution counts to the local review and proposed final program table. Retain every preceding all-parameter mathematical proof.')

# Actual period-variable maps and bounded notation clarifications.
replace('LF','For its holomorphic comparison put $D_0=\\operatorname{diag}(a,-b)$',
 r'''For the nonzero elliptic short period $\omega_s$, set
$z_E=z_{\rm add}/\omega_s$, with inverse $z_{\rm add}=\omega_s z_E$.
Put $\tau=\omega_l/\omega_s$, $\zeta_G=G_{\rm lift}/\omega_s$,
and $z=e^{2\pi i z_E}$; its inverse logarithm is taken modulo the
same short period. Let $\rho_L$ be the forward line-period logarithm.
For the holomorphic comparison put $D_0=\operatorname{diag}(a,-b)$''',
 'D20;D22;D27','Declare the actual period division, inverse multiplication and exponential coordinate; no unit or lattice is changed.')
replace('LJ','The same actual holomorphic line is seen as follows. The theta ratio\n\\(\\vartheta(z-a\\zeta_G)/\\vartheta(z)\\), with reciprocal inverse,',
 r'''For the nonzero short period $\omega_s$, use
$z_E=z_{\rm add}/\omega_s$, with inverse $z_{\rm add}=\omega_s z_E$.
Put $\tau_E=\omega_l/\omega_s$, $\zeta_G=G_{\rm lift}/\omega_s$,
and $z=e^{2\pi i z_E}$; the inverse logarithm is modulo the short
period. Let $\rho_L$ be the forward line-period logarithm.
The theta ratio
$\vartheta(z_E-a\zeta_G)/\vartheta(z_E)$, with reciprocal inverse,''',
 'D20;D22;D27','Separate the additive theta argument and its exact inverse from the multiplicative physical coordinate.')
replace('LF',r'F_t',r'F_{r_Y}','D20','Separate the number of free base loops from a Borel variable.')
replace('LF',r'\qquad t=0\text{ or }1.',r'\qquad r_Y=0\text{ or }1.','D20','Use the declared free rank.')
replace('LJ',r'F_h',r'F_{r_Y}','D20','Separate the free rank from the deck map h.',2)
replace('LJ',r'\qquad h=0\text{ or }1.',r'\qquad r_Y=0\text{ or }1.','D20','Use the declared free rank.')
replace('LJ','The square supports differ by','The supports of the tensor squares differ by','D20;D22','Specify the additive support under tensor product.')
replace('LJ','Here \\(\\Omega_6^{\\rm Spin}(\\mathrm{pt})=0\\), also following from\nZhubr\'s injective pair for coefficient group zero.',
 r'''Here $\Omega_6^{\rm Spin}(\mathrm{pt})=0$, by
\ref{maps:src:D.1.11} for coefficient group zero, whose injective
pair $(P,h)$ has zero target.''','D06;D20','Locate the exact earlier coefficient-zero statement.')

# Mathematical proof headings replace manual section-number references.
section_names={4:'the cap-map construction',5:'the primitive rank-one construction',6:'the prescribed-cusp construction',8:'the common global Borel comparison',12:'the coprime homotopy and coefficient maps'}
for number,name in section_names.items():
 token='Section '+str(number)
 n=text.count(token)
 if n: replace('LJ',token,name,'D06;D19','Replace a manual local section reference by the actual named proof construction.',n)
replace('LJ','Sections 4--11 prove','The cap, line and localization constructions prove','D06;D19','Use the complete retained mathematical scope rather than obsolete paragraph numbers.')
replace('LJ','the raw \\(\\kappa_i\\)','the marked $\\kappa_i$','D04;D20','Use the declared input marking.') if 'the raw \\(\\kappa_i\\)' in text else None

# Make the full OS names explicit without changing any table entry.
for m in reversed(list(re.finditer(r'(?m)^(?P<row>\d+&)?(?P<os>56)(?P<suf>/(?:II|III))?&',text))):
 old=m[0];new=(m['row'] or '')+r'\mathrm{OS56}'+(r'/\mathrm{'+m['suf'][1:]+'}' if m['suf'] else '')+'&'
 owner='LF' if m.start()<text.index(r'\subsubsection{Orders six') else 'LJ'
 edits.append((owner,'D04;D20',text.count('\n',0,m.start())+1,old,new,'Spell out the actual OS profile name; every pattern coordinate is unchanged.'))
 text=text[:m.start()]+new+text[m.end():]
replace('LF',r'\text{default}',r'\mathrm{OS56}','D04','Use the actual base-profile name.',3)
for prof in ['II','III']:
 for m in reversed(list(re.finditer(r'(?m)^'+prof+r'&(?=\d)',text))):
  old=m[0];new=r'\mathrm{OS56}/\mathrm{'+prof+'}&'
  edits.append(('LF','D04;D20',text.count('\n',0,m.start())+1,old,new,'Give the full profile in the selected-cusp table.'))
  text=text[:m.start()]+new+text[m.end():]
for line in [x for x in text.splitlines() if x.startswith(' &43&') or x.startswith(' &49/III&')]:
 new=re.sub(r'(?<=&)(43|45|46|47|49|50|55|56)(/(?:II|III|IV))?',lambda m:r'\mathrm{OS'+m[1]+'}'+(r'/\mathrm{'+m[2][1:]+'}' if m[2] else ''),line)
 replace('LJ',line,new,'D04;D20','Use complete profile names in the172-row count table without altering any count or order.')

# Convert manual mathematical proof headings into automatic ordered steps.
for a,b in reversed([(m.start(),text.index(r'\end{proof}',m.end())) for m in re.finditer(r'\begin{proof}',text)]):
 block=text[a:b]
 heads=list(re.finditer(r'\\paragraph\{([^\n]+)\}',block))
 assert heads
 for h in reversed(heads):
  title=re.sub(r'^\d+[a-z]?\.\s*','',h[1]).replace('Exhaustion from the defining raw profiles.','Exhaustion of minimal fillings.')
  repl=r'\item \emph{'+title+'}'
  block=block[:h.start()]+repl+block[h.end():]
 block=block.replace(r'\begin{proof}',r'\begin{proof}'+'\n'+r'\begin{enumerate}',1)+r'\end{enumerate}'+'\n'
 old=text[a:b];owner='LF' if a<text.index(r'\subsubsection{Orders six') else 'LJ'
 replace(owner,old,block,'D13;D14;D19','Use one ordered proof with automatic stage numbers; retain every mathematical stage after the separately recorded exact consolidations.')

# New identities for all retained LJ local equations. Existing MT2/MT3
# identities own former56/92. Four universal identities point to LF.
equations.update({56:('020K','maps:eq:D.MT2'),92:('020L','maps:eq:D.MT3')})
manual=list(re.finditer(r'\\qquad\\textnormal\{\((\d+)\)\}',text))
assert len(manual)==97 and len({m[1] for m in manual})==97
alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
next_index=82
for n in sorted(int(m[1]) for m in manual):
 if n not in equations:
  tag='Q2'+alphabet[next_index//36]+alphabet[next_index%36];next_index+=1
  equations[n]=(tag,'maps:eq:MT_local_'+str(n))
for m in reversed(manual):
 n=int(m[1]);tag,label=equations[n]
 a=text.rfind(r'\[',0,m.start());b=text.index(r'\]',m.end())+2
 old=text[a:b]
 if n in (56,92):
  new=old.replace(m[0],'')
 else:
  new=old.replace(m[0],'').replace(r'\[',r'\begin{equation}',1)
  new=new[:-2]+identity(tag,label)+'\n'+r'\end{equation}'
 replace('LJ',old,new,'D06;D10;D19','Replace local equation('+str(n)+') by its exact permanent identity '+tag+'/'+label+'; preserve every retained mathematical term and every old permanent label.')

# Inspect the prior complete occurrence list: O(1), S1_(3) and SO(4)
# are mathematical arguments, not equation references.
lj=text.index(r'\subsubsection{Orders six')
refs=list(re.finditer(r'\((\d+)\)',text[lj:]))
reference_count=0
for m in reversed(refs):
 a=lj+m.start();b=lj+m.end();n=int(m[1])
 if text[a-1:a]=='O' or text[max(0,a-2):a]=='_{':
  assert n in (1,3,4);continue
 assert n in equations,(n,text[a-60:b+60])
 old=m[0];new=r'\eqref{'+equations[n][1]+'}'
 edits.append(('LJ','D06;D19',text.count('\n',0,a)+1,old,new,'Replace this exact literal equation reference by the retained identity; functional arguments and circle-weight notation are explicitly excluded.'))
 text=text[:a]+new+text[b:];reference_count+=1

before=text
text,changes,issues=presentation.statement_records_to_small_tags(text)
assert not changes and not issues
text,changes,issues,aliases=presentation.remove_manual_equation_tags(text)
assert not issues
for c in changes:
 owner='LF' if c.start<before.index(r'\subsubsection{Orders six') else 'LJ'
 edits.append((owner,c.kind,before.count('\n',0,c.start)+1,c.old,c.new,c.reason))
assert not presentation.unresolved_literal_equation_references(text,aliases)
units.check_permanent_identifiers(original,text,new_labels,new_targets)
assert text.count(r'\begin{definition}')==text.count(r'\end{definition}')==2
assert text.count(r'\begin{theorem}')==text.count(r'\end{theorem}')==2
assert text.count(r'\begin{proof}')==text.count(r'\end{proof}')==2
assert r'\path{' not in text and r'\StatementRecord' not in text
assert r'\tag{' not in text and '\r' not in text

fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
for i,(owner,kinds,line,old,new,why) in enumerate(edits,1):
 for kind in kinds.split(';'):
  rows.append([f'III-C8-THREE-PUB-{i:03d}-{kind}',kind,'maps:src:D.2.'+('39' if owner=='LF' else '42'),f'three_primary_types.tex sequential edit line{line}','pending page concordance','weighted/three_primary_types.tex','pending final build',old,new,why,'whole input/evidence and exact edit read; complete candidate readback pending; global gates open'])
p.write_text(text,newline='\n')
with (lane/'S6_SERIES_PUBLISH_THREE_publication_defects.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
with (lane/'S6_SERIES_PUBLISH_THREE_equation_identities.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['former_local_number','tag','label','scope'])
 for n,(tag,label) in sorted(equations.items()):w.writerow([n,tag,label,'exact retained identity;72–75 reuse the identical universal LF proof;56/92 retain their original permanent identities'])
print('UTC',datetime.now(timezone.utc).isoformat())
print('LINES',len(original.splitlines()),'TO',len(text.splitlines()),'EXACT_EDITS',len(edits),'SINGLE_TYPE_ROWS',len(rows))
print('DEFINITIONS_Q223_Q229; LF_UNIVERSAL_EQUATIONS_Q224_Q228; NEW_LJ_EQUATIONS95; TRUE_LITERAL_REFERENCES',reference_count)
print('NEXT_TAG','Q2'+alphabet[next_index//36]+alphabet[next_index%36],'OLD_IDENTITIES_PRESERVED; SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0')
