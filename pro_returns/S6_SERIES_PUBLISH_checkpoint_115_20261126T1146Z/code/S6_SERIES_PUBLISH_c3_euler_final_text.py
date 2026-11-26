"""Read and edit the final Euler theorem; keep pending interface checks open."""
from S6_SERIES_PUBLISH_c3_edit import *
import hashlib

source=SOURCE.read_text()
a=source.index(r'\section{Euler sign and equality for arbitrary torus fibres}')
b=source.index(r'\clearpage',a)
old_unit=source[a:b]
edits=[]
def change(old,new,types,reason):
 assert old_unit.count(old)==1,old
 edits.append((old,new,types,reason))

change(r'''are finite unramified covers. Each description concerns the
normalization and resolution maps of the actual fibre. In
particular the full-fibre and conductor multiplicities are
retained.''',r'''are finite unramified covers. These are the normalization
and resolution maps of each full fibre, with its given
component and conductor multiplicities.''',['D02','D08','D11'],
 'State the identical normalization/resolution maps and full multiplicities positively, once in the theorem.')

heads=[
('\\item \n\\noindent\\textbf{Step 1. The base is rational and the local\nfinite character is available on every full fibre.}',r'\item \textbf{The base and the finite character.}'),
('\\medskip\\noindent\\textbf{Step 2. A normal irreducible support\nis smooth and has a finite unramified torus cover.}',r'\item \textbf{Smooth supports.}'),
('\\medskip\\noindent\\textbf{Step 3. The irreducible nonnormal\nnormalization falls into three explicit resolution classes.}',r'\item \textbf{Normalization resolutions.}'),
('\\medskip\\noindent\\textbf{Step 4. Every irreducible support has\nthe claimed exact Euler value and normalization.}',r'\item \textbf{Irreducible supports.}'),
('\\medskip\\noindent\\textbf{Step 5. Arbitrary reducible supports\nhave nonnegative Euler number, with the stated equality data.}',r'\item \textbf{Reducible supports.}'),
('\\medskip\\noindent\\textbf{Step 6. The global sum is zero or two.}',r'\item \textbf{The global Euler sum.}'),
('\\medskip\\noindent\\textbf{Step 7. Vanishing is equivalent to\nthe listed geometric data on every fibre.}',r'\item \textbf{The equality criterion.}')]
for old,new in heads:change(old,new,['D08','D23'],'Give each of the seven existing proof steps its own numbered item and a short mathematical heading.')

change(r'''\ref{cdp:st:C.2.MH.2}. The construction is on the original
full fibre and requires no change of its multiplicity.''',r'''\ref{cdp:st:C.2.MH.2}, on the full Cartier fibre $f^*(b)$.''',['D02','D08'],
 'Identify the exact full-fibre object in the finite-character application.')
change(r'''It is K\"ahler by the even-$b_1$ criterion, and the
surface classification identifies it as a torus; the
precise classification facts are
\cite[Proposition~2.1 and Theorem~2.2, pp.~842--843]{Peters2021}.
Thus $e(S)=0$.''',r'''It is K\"ahler by the even-$b_1$ criterion in
\cite[Proposition~2.1, p.~842]{Peters2021}.
Its rationally trivial canonical class excludes an exceptional
curve, whose canonical intersection would be $-1$.
Every effective pluricanonical divisor has zero K\"ahler area
and hence is empty, so every nonzero pluricanonical space has
dimension one. In the classification of
\cite[Theorem~2.2, p.~843]{Peters2021}, the remaining
Kodaira-dimension-zero case with $b_1=4$ is a torus;
the ruled alternative has canonical intersection $-2$ with
a ruling fibre and is excluded by the same Chern class.
The degree-$m$ unramified central cover therefore gives
$e(S)=e(S')/m=0$, where $S'$ denotes that cover.''',['D22'],
 'Spell out the exact classification application: transported c1=0 excludes exceptional/ruling curves and positive pluricanonical growth by Kähler area. With b1=4 the cited classification selects the torus. State the precise finite-cover Euler map.')
change(r'''genus, or a resolution of class VII. The actual maps
$Z\to T\to S$ remain the maps in every subsequent
comparison.''',r'''genus, or a resolution of class VII. We apply the following
results to these same maps $Z\to T\to S$.''',['D08'],
 'Specify the common maps in the following applications without process language.')
change(r'''and $e(S)=0$. Its proof uses the effective conductor,
the local trace inequality, and the fundamental group
of this support; no assertion about the other fibre
supports enters that local inequality.''',r'''and $e(S)=0$. The irreducible-support assertion of that
proposition uses the effective conductor, local trace
inequality and fundamental group of this same $S$.''',['D02','D08'],
 'Identify the exact single-support clause of P4.26; its separate global normal-crossing clause is not needed for this application.')
change(r'''calculations force the actual normalization to be
smooth and minimal, with $e(S)=0$. These arguments
are local comparisons for the given irreducible
support; they do not invoke the irreducible-or-normal-
crossings hypothesis on all fibres in
\SeriesRef{night:P4.58}. This proves the asserted exact
irreducible classification in the present scope.''',r'''calculations make $T$ smooth and minimal, with $e(S)=0$.
These are the single-support conclusions for the
normalization map $T\to S$ fixed in step~3.''',['D02','D08','D11'],
 'Use the already explicit single-support hypotheses and the identical normalization map, removing the repeated disclaimer about a different global theorem.')
change(r'''component supplies a nonzero effective divisor with
rationally trivial first Chern class. Its positive
pairing with a proposed K\"ahler form excludes a
K\"ahler resolution.''',r'''component gives a nonzero effective divisor with
rationally trivial first Chern class. Integration against
a K\"ahler form would give both positive area and zero
cohomological pairing, so the resolution is non-K\"ahler.''',['D08','D22'],
 'Write the exact incompatible pairings that exclude a Kähler resolution.')
change('gives the actual Picard restriction to each elliptic','gives the Picard restriction to each elliptic',['D08'],'Remove a process qualifier; the Picard restriction map is unchanged.')
change(r'''Proposition~\ref{cdp:st:C.2.INT.3} now applies to the
entire reduced support. With $A_i$ its normalization
conductor and $C$ its reduced image, its actual
normalization map gives''',r'''Proposition~\ref{cdp:st:C.2.INT.3} applies to this
reduced support. Write $\nu:\coprod_iT_i\to S$ for its
normalization, $A_i$ for the reduced conductor on $T_i$,
and $C$ for the reduced conductor image. Restriction of
$\nu$ gives an isomorphism
$\coprod_i(T_i\setminus A_i)\simeq S\setminus C$, and hence''',['D08','D20','D22'],
 'Name the normalization map and the exact open isomorphism giving Euler additivity; distinguish the reduced topological conductor from the scheme conductor used in duality.')
change(r'''The proof retains the scheme conductor in the
coherent-duality argument and all contractions in
the topological calculation. It proves both
directions of the equality characterization:''',r'''The scheme conductor enters the coherent-duality argument
of that proposition, and the exceptional loci enter its
topological calculation. Its equality characterization gives''',['D08'],
 'Name the precise geometric inputs of the cited equality argument.')

for num,tag in [('1','00KW'),('2','00KX')]:
 pattern=r'\\\[\n((?:(?!\\\]).)*?)\s*\\tag\{C\.G\.'+num+r'\}\\hypertarget\{tag-'+tag+r'\}\{\}\\label\{cdp:eq:C\.G\.'+num+r'\}\n\\\]'
 m=re.search(pattern,old_unit,re.S);assert m,num
 new='\\begin{equation}\n'+m[1].rstrip()+'\n \\hypertarget{tag-'+tag+'}{}\\label{cdp:eq:C.G.'+num+'}\n\\end{equation}'
 change(m[0],new,['D19'],'Use automatic section equation numbering while preserving the equation label and permanent target.')

for i,(old,new,types,reason) in enumerate(edits,1):
 apply_edit(old,new,f'II-C3-EULER-FINAL-{i:02}',types,'cdp:st:C.2.G.1',
  'Euler sign and equality for arbitrary torus fibres',reason,
  'Root read complete old unit. Complete receiving proof is read after these exact edits; interface receiver verification remains pending.')

text=SOURCE.read_text();a=text.index(r'\section{Euler sign and equality for arbitrary torus fibres}');b=text.index(r'\clearpage',a)
unit=text[a:b]
replacement=re.sub(r'(?:Proposition~)?\\SeriesRef\{([^}]+)\}',r'\\cref{\1}',unit)
replacement=re.sub(r'(?:Proposition~)?\\ref\{([^}]+)\}',r'\\cref{\1}',replacement)
assert replacement!=unit
apply_edit(unit,replacement,'II-C3-EULER-TYPED-REFERENCES',['D04','D06'],
 'cdp:st:C.2.G.1','Complete final Euler theorem unit',
 'Use typed references to this paper\'s exact local theorem owners throughout the complete unit. All referenced label identities remain unchanged except deletion of the redundant global P4.58 disclaimer.',
 'Root read the complete original unit and all exact bounded changes; full receiving unit and its same-map applications are read before status closure.')
assert identifiers(old_unit)==identifiers(replacement)
assert replacement.count(r'\item ')==7
print('Complete receiving unit follows:\n'+replacement)
