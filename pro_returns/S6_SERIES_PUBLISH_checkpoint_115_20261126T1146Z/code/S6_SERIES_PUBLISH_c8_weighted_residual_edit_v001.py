"""Publication edit of the wholly read LL/LM unit, including one bounded wall-map repair."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import sympy as sp
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units

root=Path(__file__).resolve().parent.parent
p=root/'agents/continuation8_iii_integration/units/weighted/residual_even_types.tex'
lane=root/'agents/continuation8_iii_weighted_units'
original=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='e49edaf4acbcebff50ca0da3faeeb21662b7a644c3b6f6069bcb6dd580d722ca'
text=original
edits=[]
new_labels=[]
new_targets=[]

def replace(owner,old,new,kinds,why,count=1):
 global text
 assert text.count(old)==count,(owner,old[:180],count,text.count(old))
 for _ in range(count):
  a=text.index(old)
  edits.append((owner,kinds,text.count('\n',0,a)+1,old,new,why))
  text=text[:a]+new+text[a+len(old):]

def between(start,stop):
 a=text.index(start);b=text.index(stop,a);return text[a:b]

def identity(tag,label):
 new_labels.append(label);new_targets.append('tag-'+tag)
 return r'\hypertarget{tag-'+tag+r'}{}\label{'+label+'}'

# Define the actual semistable inputs and the two embedded surgery models.
old=text[:text.index(r'\end{theorem}')+len(r'\end{theorem}')]
display=old[old.index(r'\['):old.index(r'\]')+2]
models=old[old.index('The manifold $Z_{c,0}$'):old.index(r'\end{theorem}')]
new=r'''\subsection{Residual orders four, eight and twenty}

\subsubsection{Semistable orders four and eight}

\begin{definition}[Semistable residual data]'''+identity('Q24X','maps:def:semistable-residual-data')+r'''
{\normalfont\scriptsize tag Q24X}\par
Use the ordered elliptic data of
Definition~\ref{mapsIII:def:elliptic-marked-data}. Choose OS55 with
$(a,b)=(5,4)$ and selected position $i_0\in\{2,3,4\}$, or OS45
with $(a,b)=(1,8)$ and $i_0\in\{1,2,3,4\}$. Both profiles are
the base semistable profiles. The selected position is $i_0=i-1$
in the input definition's peripheral order; the inverse is $i=i_0+1$.
Use the prescribed primitive Mumford cap at every multiplicative
site and ordinary clutch $e\gamma$, $e=\pm1$. These are all the
fillings in this definition. Put $c=b$.

Define two oriented spin surgeries, using the unique homotopy class
of normal framing of each specified embedded sphere.
'''+models+r'''These choices are the \emph{semistable residual data}.
\end{definition}

\begin{theorem}[Semistable residual smooth types]\hypertarget{tag-02LL}{}\label{maps:src:D.2.44}
{\normalfont\scriptsize tag 02LL}\par
Every output of Definition~\ref{maps:def:semistable-residual-data}
is simply connected and satisfies
'''+display+r'''
Here $P$ is Zhubr's refined quarter-Pontryagin class. Every cyclic
generator gives the displayed values. The outputs with $P=0$
are oriented diffeomorphic to $Z_{c,0}$, and those with $P=c/2$
are oriented diffeomorphic to $Z_{c,1}$, with the markings in the proof.
\end{theorem}'''
replace('LL',old,new,'D04;D05;D10;D11;D13;D14;D16;D26',
 'Put all seven semistable patterns, both ordinary signs, prescribed primitive fans, exact Q110 index map and the actual surgery models in numbered definition Q24X. Keep one full theorem and proof; preserve D44.1 and all conclusions.')
for old,new in [(r'\ z=',r'\ i_0='),(r'1&i=z',r'1&i=i_0'),(r'0&i\ne z',r'0&i\ne i_0'),(r'\det C_z=1',r'\det C_{i_0}=1'),(r'Write $C=C_z$',r'Write $C=C_{i_0}$'),(r'\mathrm{OS}&c&z&',r'\mathrm{OS}&c&i_0&')]:
 n=text.count(old)
 if n:replace('LL',old,new,'D20','Use i_0 only for the selected input position; preserve the separate complex and character variables z.',n)

# Retain the full primitive-cap quotient and give each positive wall its
# exact coordinate, not only their sum. This also supplies LM's repair.
old='Each double curve projects into a one-dimensional edge of that\ndual complex, so its fourth coordinate is zero. The sum of the\npositive wall degrees is $(1,-1,1)$. Hence the actual sum of the\nthree complex double curves has integral preimage'
new=r'''Each double curve projects into a one-dimensional edge of that
dual complex, so its fourth coordinate is zero. Denote the first
three quotient coordinates by $x,y,z$ in the displayed order.
The Cartier evaluations and the zero fourth coordinate determine
the curves in the entire integral cap group. In vertical, horizontal
and diagonal order, the resulting classes are
\begin{equation}
 [C_v]=x-y,\qquad [C_h]=z-y,\qquad [C_d]=y.
'''+identity('Q24Z','maps:eq:primitive-cusp-wall-classes')+r'''
\end{equation}
Indeed their coordinate columns are exactly $M$. Its displayed
integral inverse sends $(x,y,z)$ to $(x,z,x+y+z)$ in the wall
basis. Composing either way gives the identity. The representatives
$A_1\wedge B_1-A_2\wedge B_1$,
$A_2\wedge B_2-A_2\wedge B_1$ and $A_2\wedge B_1$ have these
coordinates; subtracting the two primitive relations gives the
inverse specialization coordinates. Their sum is $(1,-1,1)$.
Hence the three complex double curves together have integral preimage'''
replace('LL',old,new,'D19;D22;D26',
 'Label Q24Z the individual positive wall classes forced by the existing exact Cartier matrix and full four-coordinate primitive-cap quotient. Give M and its inverse at homology scope, using the dual-complex projection to fix the fourth coordinate. The original total D44.12 is unchanged.')

# LM's complete construction domain is a numbered definition, with the
# identical earlier c=4,8 models rather than a repeated model definition.
old=between(r'\begin{theorem}[the remaining minimal','All the manifolds in \\eqref{maps:eq:D45.1}')
start=old.index(r'\[');end=old.index(r'\]',old.index(r'\label{maps:eq:D45.1}'))+2
table=old[start:end]
params=old[old.index('Indices are zero-based.'):old.index('Write $Z_{c,0}$')]
params=params.replace('Indices are zero-based.','Selected positions are $i-1$ in Definition~\\ref{mapsIII:def:elliptic-marked-data},\nwith inverse $i=i_0+1$ for a selected index $i_0$.')
new=r'''\subsubsection{Additive caps and order twenty}

\begin{definition}[Residual additive data]'''+identity('Q24Y','maps:def:additive-residual-data')+r'''
{\normalfont\scriptsize tag Q24Y}\par
Use Definition~\ref{mapsIII:def:elliptic-marked-data}, the primitive
Mumford cap at every multiplicative site, the prescribed fan at
the selected position, and the additive fillings in this table:
'''+table+'\n'+params+r'''
These listed sites are all the logarithmic sites in this definition.
Use the identical oriented models $Z_{c,0},Z_{c,1}$, $c=4,8$,
of Definition~\ref{maps:def:semistable-residual-data}, with their
specified embeddings, normal framings and primitive generators.
Use $Z_{5,1}$ from Definition~\ref{maps:def:minimal-odd-data},
marked by its refined generator, with fundamental-class invariant zero.
These choices are the \emph{residual additive data}.
\end{definition}

\begin{theorem}[Residual additive smooth types]\hypertarget{tag-02LM}{}\label{maps:src:D.2.45}
{\normalfont\scriptsize tag 02LM}\par
'''
replace('LM',old,new,'D04;D05;D10;D11;D12;D13;D14;D16;D26',
 'Place all eleven patterns, all m=6k>0, e,r, n-me=±1, primitive fixed lift and every affine twist in Q24Y. Identify the same earlier models with unchanged embeddings/framings/generators. Keep the full seven-row theorem and all finite alternatives.')
replace('LM','All the manifolds in \\eqref{maps:eq:D45.1}',
 'All outputs of Definition~\\ref{maps:def:additive-residual-data}',
 'D13;D26','Bind the full theorem to its complete numbered mathematical inputs.')

# Bounded D25: the three old representatives had only the correct sum.
old=between('The annular specialization maps send the three positive complex','For precision, the alternative Jordan basis')
new=r'''Apply the primitive-cap specialization of
\eqref{maps:eq:primitive-cusp-wall-classes} with
$(A_1,B_1,A_2,B_2)=(H_1,H_2,H_3,H_4)$. This is the identity
on the ordered unit fan, its normal-disc and monodromy-cylinder
relations, and its dual long-period torus. The inverse sends those
four named vectors back to the same $A_1,B_1,A_2,B_2$.
Thus the vertical, horizontal and diagonal curves have representatives
\[
 H_1\wedge H_2+H_2\wedge H_3,\qquad
 H_3\wedge H_4+H_2\wedge H_3,\qquad
 -H_2\wedge H_3.
\]
Their sum is $H_1\wedge H_2+H_2\wedge H_3+H_3\wedge H_4$,
with $\Omega$-value $a-ab\kappa-b+ab^2\kappa^2$.
The local annuli lie in the two smooth charts along each edge.
The charts $q/(X_1X_2),X_2,X_1$ and
$q/X_2,X_1X_2,X_1^{-1}$ overlap by
$(x,y,w)\mapsto(wx,wy,w^{-1})$, whose inverse is
$(x',y',w')\mapsto(w'x',w'y',(w')^{-1})$.
Their oriented collapsing annuli cap the adjacent triangles.
The complete quotient and its Cartier dual identify their other
boundaries with the three classes above, including the zero
long-period two-torus coordinate.

The alternative Jordan basis'''
replace('LM',old,new,'D25;D22;D26',
 'Correct only the individual critical-curve representatives. The old H1H2,H2H3,H3H4 give degrees K11,-K12,K22 rather than K11-K12,K22-K12,K12. Q24Z supplies the complete cap map and inverse under the exact ordered basis identity. Their sum, all eleven critical totals, every bounding chain, λ, full P/µ and every smooth assignment remain unchanged.')
# The boundary marker is shared with the replacement tail.
replace('LM','The alternative Jordan basisFor precision, the alternative Jordan basis',
 'The alternative Jordan basis','D23','Join the retained exact Jordan-coordinate comparison to the repaired paragraph.')

# Replace saved-array slices by the corresponding explicit homomorphisms.
replace('LL',r''' q=Q\bigl(F^{-1}(v-\Omega(v)s_0)\bigr)_{\mathrm{last\ five}},
 \qquad Rq=v-\Omega(v)s_0.''',r''' q=Q\pi F^{-1}(v-\Omega(v)s_0),
 \qquad Rq=v-\Omega(v)s_0.''','D09;D20;D22',
 'Use the last-five-coordinate projection π as a named homomorphism, not a saved-array slice; retain the same chain section.')
replace('LL','with\n$RQ=K_0$, $\\Omega(s_0)=1$. Therefore',
 'with\n$RQ=K_0$, $\\Omega(s_0)=1$. Let $\\pi$ be projection onto\nthe five $K_0$ coordinates, with inclusion $z\\mapsto(0,z)$\nas its section. Therefore','D09;D20;D22','Define the coordinate projection and its section at the precise integral lattice scope.')
old=r'''five rows of $F^{-1}R$ gives $U(F^{-1}R)_{2:6}V=(I_5,0)$.
Every pivot is one for the seven displayed rows.
The section is $V_{:,1:5}U$, and multiplying it back gives $I_5$.'''
new=r'''coordinates of $F^{-1}R$ gives
$U\pi F^{-1}RV=(I_5,0)$, where $\pi$ projects onto those five
coordinates. Every pivot is one for the seven displayed rows.
Let $\iota$ include $\mathbb Z^5$ as the first five coordinates
of the relation-column module. The section is $V\iota U$;
the displayed identity gives $\pi F^{-1}RV\iota U=I_5$.'''
replace('LM',old,new,'D09;D20;D22',
 'Express the tracked Euclidean section by actual projection/inclusion homomorphisms and prove the composite; retain all determinant signs and the complete five-dimensional return image.')

# Prove the full K4/K5 coefficient, homotopy and bordism maps before use.
old=between('We also give the full homotopy and bordism splitting.','For the connected sum make the classifying maps constant')
new=old.replace('We also give the full homotopy and bordism splitting.',
 'The full coefficient splitting at order twenty is as follows.')
new=new.replace('Here $\\Omega^{\\mathrm{Spin}}_6(\\mathrm{pt})=0$, also obtained\nfrom the injective pair $(P,h)$ at coefficient group zero.',
 'Here $\\Omega^{\\mathrm{Spin}}_6(\\mathrm{pt})=0$ by\n\\ref{maps:src:D.1.11} at coefficient group zero: its injective\npair $(P,h)$ has zero target.')
replace('LM',old,'','D14','Move the complete coprime K4/K5 CW and spin-bordism map with its full inverse before the first reconstruction of µ at order20. No mathematical step is omitted.')
where=r'\item \emph{The common Borel character and the complete fundamental class.}'
replace('LM',where,where+'\n'+new,'D14;D22',
 'Establish the full coefficient/CW/bordism splitting before the common-character localization and full order20 detector.')

# Remove only the repeated model proof after specifying identical objects.
old=between('The attaching two-spheres defining $Z_{c,0}$ and $Z_{c,1}$','For $b=20$ the connected sum')
new=r'''For $c=4,8$ use the embeddings, framings and trace maps of
\ref{maps:src:D.2.44}. The sphere defining $Z_{c,0}$ is its
$c$-fold tube; the sphere defining $Z_{c,1}$ is its conic-disjoint
projective line tubed to $c/2$ negatively oriented product spheres.
Their rank-four spin framings are identical, with unique homotopy
class because $\pi_2SO(4)=0$. The coefficient maps are
$x\mapsto s$ and $(t,x)\mapsto((c/2)s,s)$, with inverse
$s\mapsto[x]$ on each quotient. These are exactly the earlier
trace maps, so the identity and its inverse identify the marked
manifolds. That proof gives simple connectivity, the unique spin
structure, $H_2=H_3=\mathbb Z/c$, zero free third Betti number,
and the full values $(P,\mu)=(0,0)$ or $((c/2)s,0)$.

For $b=20$ the connected sum'''
replace('LM',old,new,'D12;D17;D22;D27',
 'Reuse the same c4/8 surgery construction only after identifying the actual tube and conic-disjoint embeddings, unique normal framings, coefficient maps/inverses, full P/µ and homology from LL. Retain all new order20 connected-sum and marking proofs.')
replace('LM','For $b=20$ the connected sumFor $b=20$ the connected sum',
 'For $b=20$ the connected sum','D23','Join the retained new order20 model argument.')

# Exact prose and source-locator changes; all mathematical maps remain.
changes=[
 ('LL','We retain the precise local marking that extends this line across\nthe prescribed caps.','The local extension across the prescribed caps uses the following marking.','D08','State the mathematical line extension without workflow language.'),
 ('LL',"The inverse reads these same physical coordinates through that\ninteger inverse.","Applying the integer inverse recovers the physical coordinates.",'D08;D20','Name the inverse coordinate map.'),
 ('LL',"$Z=U+\\Pi B'$, retain the full period matrix", "$Z=U+\\Pi B'$, use the full period matrix",'D08','Keep the full period matrix and every unit.'),
 ('LL','Equivalently one can retain','Equivalently, use','D08','Keep the complete common-character calculation.'),
 ('LL','Retain $W$ and fill its ordinary cap with zero shear, obtaining $Y$.','Fill the ordinary cap of $W$ with zero shear, obtaining $Y$.','D08','State the characteristic-trace construction.'),
 ('LL','retaining $i_2\\alpha$ and the integral endpoint class $\\omega_1$.','preserving $i_2\\alpha$ and the integral endpoint class $\\omega_1$.','D08','Name preservation of the endpoint classes.'),
 ('LL','For completeness, lift the marked spin bordism class through the','Lift the marked spin bordism class through the','D02','Retain the full free-lift map and inverse without defensive narration.'),
 ('LL','The characteristic-bordism\naxiom is used at its published scope, with simply connected\nendpoints; its earlier bordism proof is the source of that axiom\n\\cite[pp.471,479]{manZhubr2010Gamma}.',
  'The characteristic-bordism axiom applies to these simply connected\nendpoints and this characteristic oriented cobordism\n\\cite[pp.~471,479]{manZhubr2010Gamma}.','D01;D08;D18;D26','Keep the exact endpoint and characteristic scope; record the inherited-axiom history only in the review.'),
 ('LL','the proved smooth equivariant line','the smooth equivariant line','D08','Refer to the constructed mathematical object.'),
 ('LL','elements, not only primitive roots.','elements of every order.','D02;D11','State the full per-element index scope positively.'),
 ('LL','We first record the precise primary construction used to compare a\nregular three-torus with a torsion three-sphere.',
  'Brown\'s framed construction compares a regular three-torus with\na torsion three-sphere as follows.','D01;D08','State the purpose of the retained complete framed duality proof.'),
 ('LL','\\item  For clarity we also fix the sphere convention. The homomorphism','\\item The sphere convention is determined by the homomorphism','D02;D08','Retain the explicit Spin3/stable map without narration.'),
 ('LL','Brown\'s identity already supplies its parity;\nthis construction additionally verifies its geometric\nrealization without changing the prescribed spin structure.',
  'The embedded sphere has Brown\'s parity and the prescribed spin\nstructure by these framed ambient surgeries.','D02;D08;D22','Keep the actual integral-class sphere construction and its induced parity.'),
 ('LL','For the forward implication take the admissible three-frame supplied by that\ntheorem.','For the forward implication take the admissible three-frame in that\ntheorem.','D08','Use the theorem at its specified two-primary frame scope.'),
 ('LL','generator, not twice that generator. The latter factor two\nbelongs to the different map $SO(3)\\to SO$, as is also seen\nfrom $\\lambda=-c_2$ for this complex rank-two normal calculation.',
  'generator, since $\\lambda=-c_2$ for the real bundle underlying\nthis complex rank-two bundle. Under the adjoint map $SO(3)\\to SO$\nthe class is instead $-2c_2$, giving the factor two computed above.','D02;D20;D22','State both exact representation maps and their characteristic classes; retain the degree-one Bott residue and the separate factor-two map.'),
 ('LL','to obtain the actual decision','to obtain','D08','State the exact refined parity formula.'),
 ('LL','We now compute the integer in \\eqref{maps:eq:D44.9}, retaining the\nactual fan marking of \\eqref{maps:eq:D44.10}.',
  'Compute the integer in \\eqref{maps:eq:D44.9} in the prescribed\nfan marking of \\eqref{maps:eq:D44.10}.','D08','Keep the same unit fan and exact local markings.'),
 ('LM','The raw periods, fixed lift and all filling parameters.','The periods, fixed lift and filling parameters.','D04;D08;D16','Use a mathematical proof-stage title.'),
 ('LM','To retain its integral section, choose','For its integral section, choose','D08','Keep the explicit Bézout basis.'),
 ('LM','Here are the full remaining attachment maps.','The remaining attachment maps are as follows.','D08','State the cap homomorphisms.'),
 ('LM','Here $\\lambda=p_1/2$ is the integral spin class, including its\nrelative version. No vanishing of its absolute torsion value is used.',
  'Here $\\lambda=p_1/2$ is the integral spin class, including its\nrelative version. Its absolute value is computed from the complete\ncritical class in the next step.','D02;D11;D26','Preserve the full integral relative class; later λ=8 at b20 explicitly supplies its nonzero absolute scope.'),
 ('LM','A unit triangle in $S$\ncoordinates has different adjacent Cartier gradients unless those\ncones have been carried by this same map.',
  'The Cartier gradients in $S$ coordinates are the inverse-transpose\nimages of those on $\\Sigma$, with inverse the transpose map.','D02;D20;D22','Use the exact fan/character transport rather than a negative contrast with an untransported fan.'),
 ('LM','Its disjointness will retain the actual rational\nlink before halving. Absolute \\eqref{maps:eq:D45.7} already gives',
  'This support preserves the rational link before halving.\nThe absolute image of \\eqref{maps:eq:D45.7} gives','D08;D22','Keep the support argument that fixes the full rational link.'),
 ('LM','This is precisely the source\'s two-primary frame-selection scope.\nIts obstruction is the full integral refined class.',
  'The sphere has the required two-primary basis class, and the\ncomplementary obstruction is the full integral refined class.','D08;D18;D26','Keep the exact source hypothesis and full integral obstruction, without source-scope narration.'),
 ('LM','The parity convention can be read directly on the surgery handle.','The surgery handle fixes the parity convention.','D08','Retain the complete quaternion coefficient map.'),
 ('LM','also has even parity. This argument uses a global three-frame\nand local complementary trivializations, and does not require\na global full framing when $\\lambda$ is nonzero.',
  'also has even parity. The global three-frame and these local\ncomplementary trivializations therefore determine the full-order\ncomparison, including the order-twenty manifolds.','D02;D11;D26','Retain the actual odd-copy transport and local complement extension at b20; make no full-tangent trivialization assertion.'),
 ('LM','In particular the order-five part at $b=20$ has been retained.',
  'This formula includes the order-five coordinate at $b=20$.','D08;D26','State the full refined coefficient scope.'),
 ('LM','The proposed general frame-variation formula in the source is\nunused; its proved sphere criterion and the displayed obstruction\nidentity suffice. The original-$II$ change',
  'The original-$II$ change','D01;D02;D11','Remove source-history defensiveness; the preceding complete sphere-selection and integer-transgression proofs stay in place and their precise published scope is recorded in the review.'),
 ('LM','Let $W$ retain the regular piece and all multiplicative caps,','Let $W$ be the union of the regular piece and all multiplicative caps,','D08','Define the exterior directly.'),
 ('LM','The remaining coordinates are the fibre coordinate and retained','The remaining coordinates are the fibre coordinate and','D08','Keep every surviving sweep coordinate.'),
 ('LM','The same $h$ is read by every fixed-point section.','Every fixed-point section pulls back this same $h$.','D08;D20','Name the actual common Borel pullback map.'),
 ('LM','with all finite data retained.','for every finite datum in Definition~\\ref{maps:def:additive-residual-data}.','D08;D26','State the full unbounded finite-parameter scope.')]
for owner,old,new,kinds,why in changes:replace(owner,old,new,kinds,why)

# Remaining occurrence-level prose changes preserve all mathematical nouns.
for pattern,replacement,reason in [
 (r'\bactual\s+','', 'Remove workflow emphasis while retaining the full stated mathematical object, map and proof.'),
 (r'\bactually\s+','', 'State the proved bundle assertion directly.'),
 (r'\bliteral\s+','', 'State the integral cycle or equality directly.'),
 (r'\bretaining\b','preserving','Use mathematical preservation, not process narration.'),
 (r'\bare retained\b','remain unchanged','State preservation of the complete chart units.'),
 (r'\bis retained\b','is included','State the included mathematical chain term.'),
 (r'\bretains\b','preserves','Use the mathematical preservation relation.')]:
 for m in reversed(list(re.finditer(pattern,text))):
  owner='LL' if m.start()<text.index(r'\subsubsection{Additive caps') else 'LM'
  edits.append((owner,'D08',text.count('\n',0,m.start())+1,m[0],replacement,reason))
  text=text[:m.start()]+replacement+text[m.end():]
for old,new in [(r'\mathrm{default}',r'\mathrm{base}'),('Bezout',r"B\'ezout"),('Kunneth',r"K\"unneth"),(' etale',' \'etale')]:
 for m in reversed(list(re.finditer(re.escape(old),text))):
  owner='LL' if m.start()<text.index(r'\subsubsection{Additive caps') else 'LM'
  edits.append((owner,'D20' if old==r'\mathrm{default}' else 'D23',text.count('\n',0,m.start())+1,m[0],new,
   'Use Q110 base-profile notation without changing any ordered datum.' if old==r'\mathrm{default}' else 'Correct the mathematical diacritic.'))
  text=text[:m.start()]+new+text[m.end():]

# Explicit OS names identify the same input profiles in each finite table.
for m in reversed(list(re.finditer(r'(?m)^(45|55)(/II|/\\mathrm\{base\})?&',text))):
 new=r'\mathrm{OS'+m[1]+'}'+(r'/\mathrm{II}' if m[2]=='/II' else m[2] or '')+'&'
 owner='LL' if m.start()<text.index(r'\subsubsection{Additive caps') else 'LM'
 edits.append((owner,'D04;D20',text.count('\n',0,m.start())+1,m[0],new,'Spell out the OS profile name; preserve every input, weight, critical total and invariant.'))
 text=text[:m.start()]+new+text[m.end():]

# Exact arithmetic for the bounded repair; it is not independent-check credit.
M=sp.Matrix([[1,0,0],[-1,-1,1],[0,1,0]])
Mi=sp.Matrix([[1,0,0],[0,0,1],[1,1,1]])
assert M*Mi==Mi*M==sp.eye(3)
assert M*sp.ones(3,1)==sp.Matrix([1,-1,1])
row=sp.Matrix([[1,8,56]])
assert row*M==sp.Matrix([[-7,48,8]])
assert sum(row*M)==1-8+56==49
print('WALL_MAP',str(M.tolist()),'INVERSE',str(Mi.tolist()),'BOTH_COMPOSITES_IDENTITY')
print('OS45_II_ZERO2_ACTUAL_DEGREES',list(row*M),'OLD_INDIVIDUAL_DEGREES',[1,-8,56],'COMMON_SUM',49)

before=text
text,changes,issues=presentation.statement_records_to_small_tags(text)
assert not changes and not issues
text,changes,issues,aliases=presentation.remove_manual_equation_tags(text)
assert not issues
for c in changes:
 owner='LL' if c.start<before.index(r'\subsubsection{Additive caps') else 'LM'
 edits.append((owner,c.kind,before.count('\n',0,c.start)+1,c.old,c.new,c.reason))
assert not presentation.unresolved_literal_equation_references(text,aliases)
units.check_permanent_identifiers(original,text,new_labels,new_targets)
assert text.count(r'\begin{definition}')==text.count(r'\end{definition}')==2
assert text.count(r'\begin{theorem}')==text.count(r'\end{theorem}')==2
assert text.count(r'\begin{proof}')==text.count(r'\end{proof}')==2
assert r'\tag{' not in text and '\r' not in text

fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
for i,(owner,kinds,line,old,new,why) in enumerate(edits,1):
 for kind in kinds.split(';'):
  rows.append([f'III-C8-RESIDUAL-PUB-{i:03d}-{kind}',kind,'maps:src:D.2.'+('44' if owner=='LL' else '45'),
   f'residual_even_types.tex sequential edit line{line}','pending page concordance','weighted/residual_even_types.tex','pending final build',old,new,why,
   'whole input and admitted evidence read; complete candidate readback pending; global gates open'])
p.write_text(text,newline='\n')
with (lane/'S6_SERIES_PUBLISH_RESIDUAL_publication_defects.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
print('UTC',datetime.now(timezone.utc).isoformat(),'LINES',len(original.splitlines()),'TO',len(text.splitlines()),'EXACT_EDITS',len(edits),'SINGLE_TYPE_ROWS',len(rows))
print('Q24X_Q24Y_DEFINITIONS; Q24Z_INDIVIDUAL_WALL_IDENTITY; NEXT_TAG_Q250; OLD_IDENTITIES_PRESERVED')
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),'SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0')
