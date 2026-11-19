"""Reader-facing corrections whose mathematical reasons are logged separately."""
from pathlib import Path
import re,importlib.util
P=Path(__file__).resolve().parents[2]/'papers/V'
s=(P/'body_source.tex').read_text()

# Three received statements contained their complete proof inside the theorem.
# Keep every proof paragraph, but put it in the numbered proof environment.
def numbered_inline_proof(label):
 global s
 a=s.index(r'\label{'+label+'}')
 b=s.index(r'\end{theorem}',a)
 p=s.index(r'\emph{Proof',a,b)
 q=s.index('}',p)+1
 end=s.find(r'\hfill$\square$',q,b)
 if end<0:end=b
 proof=s[q:end].strip()
 post=s[end+len(r'\hfill$\square$'):b] if end<b else ''
 # Split only top-level paragraphs; displayed environments remain whole.
 chunks=[];buf=[];depth=0
 for para in re.split(r'\n\s*\n',proof):
  if buf and depth==0:
   chunks.append('\n\n'.join(buf));buf=[]
  buf.append(para)
  depth+=len(re.findall(r'\\begin\{',para))-len(re.findall(r'\\end\{',para))
 if buf:chunks.append('\n\n'.join(buf))
 new=(r'\end{theorem}'+'\n'+r'\begin{proof}'+'\n'
      +r'\begin{enumerate}[label=\arabic*.]'+'\n'
      +'\n\n'.join(r'\item '+x for x in chunks)+'\n'
      +r'\end{enumerate}'+'\n'+r'\end{proof}'+'\n'+post)
 s=s[:p]+new+s[b+len(r'\end{theorem}'):]
for label in ['maps:src:F.2.33','maps:src:F.2.34','maps:src:F.2.35']:
 numbered_inline_proof(label)

# Use the currently opened equivalent index and lattice inputs, with their
# substitutions already written explicitly in the known-input section.
s=s.replace(
 r'''Hirzebruch, \emph{Topological Methods in Algebraic Geometry},
Theorem 24.5.4 and its corollary, give integrality of the Todd genus
for this compact almost complex manifold.  Expanding''',
 r'''The symbol-index interpretation in \S\ref{sec:V-known-inputs},
with the opened polynomial \cite[equation (1.2), p.~3]{ffEsoleKang},
gives integrality of the Todd genus. Expanding''')
s=s.replace(
 'The signature theorem in the same source, Theorem 8.2.2, applied to',
 r'The signature polynomial \cite[equation (1.4), p.~4]{ffEsoleKang}, applied to')
s=s.replace(
 r'''An even
unimodular form has signature divisible by eight, by Wall,
\emph{Classification of $(n-1)$-connected $2n$-manifolds},
Proposition 3, p.~173.  Hence it is odd.  Proposition 4 on that page
classifies indefinite unimodular forms by rank, signature, and
parity, and gives $I_{3,1}$.''',
 r'''The rank-at-most-four integral classification
\cite[Theorem 2.2.1, p.~61]{ffPetersSterk} applied to these
positive and negative indices gives the odd form \(I_{3,1}\).''')

# The following theorem supplies the global maps referred to by this old
# intermediate scope notice. Preserve the mathematical interface directly.
s=s.replace(
 r'''\emph{Scope of the chain result.}
The local finite pairs and the full cusp pair now have
effective marked chain models.  To turn them into a universal
integral homology calculation for arbitrary nonsurviving F.2
data, one must also implement the maps from these boundary
models to the common torus-bundle complement, with its
specified peripheral word and clutching translation.  The
local results alone do not assert that this remaining global
comparison has been completed.''',
 r'''The finite-pair and cusp-pair chain models enter the global
gluing cone of \cref{maps:src:F.2.35}. Its maps to the common
torus-bundle complement retain the specified peripheral word
and clutching translation.''')

# Replace one proof by the explicitly rederived characteristic-vector descent
# and the opened classical homotopy-sphere absorption theorem.
label=r'\label{maps:src:F.4.1}'
start=s.index(label)
a=s.index(r'\begin{proof}',start);b=s.index(r'\end{proof}',a)+len(r'\end{proof}')
s=s[:a]+(P/'diffeomorphism_proof.tex').read_text().strip()+s[b:]
record_start=s.index(r'\StatementRecord{maps:src:F.4.1}',start)
stmt_start=s.index('\n\n',record_start)
# The existing check record is retained. Replace its obsolete external Uses
# locators only, avoiding a false claim that the old Nagy source was opened now.
head=s[record_start:stmt_start]
head=head.replace(r'\cite[Corollary 1.9.4]{ffNikulin}',r'the explicit integral reflections below')
head=head.replace(r'\cite[Recollection 2.2, Definition 2.5 and Theorem 2.6]{ffBHS}',r'\cite[Definition 3.6 and Theorem 3.7(1), pp.~12--14]{IVVWallForm}')
head=head.replace(r'\cite[Theorem 1.4 and its proof in Section 9]{ffNagy2026}',r'\cite[Theorem A, p.~178]{IVVKramerStolz}')
s=s[:record_start]+head+s[stmt_start:]
s=s.replace('The complete Wall--Nikulin--Nagy argument',
 'The complete integral reflection, Wall-form and Kramer--Stolz argument')

# Supply the explicit deduction for the two source synthesis propositions,
# whose received source had no separate proof environment.
def add_deduction(label,uses,proof):
 global s
 a=s.index(r'\label{'+label+'}')
 b=s.index(r'\end{proposition}',a)+len(r'\end{proposition}')
 fragment=s[a:b]
 fragment=fragment.replace('{Definitions and the displayed constructions}', '{'+uses+'}')
 s=s[:a]+fragment+'\n'+proof+'\n'+s[b:]
add_deduction('maps:src:F.2.4',
 r'\cref{maps:src:F.2.16,maps:src:F.2.30,maps:src:F.2.31,maps:src:F.2.35,maps:src:F.2.36,maps:src:F.2.37,maps:src:F.2.38,maps:src:F.2.39}',
 r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item The integral intertwiner module and its centralizer order in
\cref{maps:src:F.2.36} decide simultaneous integral conjugacy. Enumerating
tuples in increasing height and then lexicographic order, and applying
that decision to each candidate, gives the canonical tuple and the
returned unimodular intertwiner of \cref{maps:src:F.2.37}. The supplied
tuple itself occurs by its own height, proving termination for this input.
\item The affine power vectors, integral normal closure and marked
extension presentation in \cref{maps:src:F.2.31} give the full fundamental
group. The finite-cap, cusp and complement maps of
\cref{maps:src:F.2.35} form the actual gluing cone, whose finite integer
differentials determine every integral homology group by Smith reduction.
All orders, affine numerators, the clutch vector and the cusp basis enter
those maps explicitly.
\item The unbounded conjugacy invariant of \cref{maps:src:F.2.16}
rules out any uniform finite height box: a finite box contains only
finitely many tuples and hence only finitely many values of that trace.
The survivor criterion and its smooth classification are exactly
\cref{maps:src:F.2.30}; the involution catalogue and complete algorithmic
assembly are \cref{maps:src:F.2.38,maps:src:F.2.39}.
\end{enumerate}
\end{proof}''')
add_deduction('maps:src:F.3.3',
 r'\cref{maps:src:F.3.4,maps:src:F.3.7,maps:src:F.3.8,maps:src:F.3.9,maps:src:F.3.10,maps:src:F.3.11}',
 r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item Every retained topological datum has determinant-one transport
and the marked primitive maximal cusp. Apply the explicit cusp graph
and relative holomorphic section construction of
\cref{maps:src:F.3.10,maps:src:F.3.11}. Its target plane is transverse
to its conjugate, and its difference from the specified cusp model is
bounded in the displayed cusp coordinate. Quotienting the resulting
holomorphic rank-three vector bundle by its integral period lattice
gives the required punctured-base family, as in \cref{maps:src:F.3.9}.
\item The displayed map from a polarized source would supply the
semisimple exterior-square local system excluded in
\cref{maps:src:F.3.4}. The actual section construction instead uses
the nine spray directions and the relative section maps proved in
\cref{maps:src:F.3.8,maps:src:F.3.10}. Its finite punctures remain
punctures; the theorem asserts precisely the bounded cusp conclusion
just obtained. The separately constructed explicit family has the
finite root-cap extensions proved in \cref{maps:src:F.3.7}.
\end{enumerate}
\end{proof}''')

# Known input rows stay in the compendium; the current manuscript uses the
# exact citation and the short substitution needed for the almost complex case.
for command in ['cref','ref']:
 s=s.replace('\\'+command+'{maps:src:F.1.2}',r'\S\ref{sec:V-known-inputs}')
 s=s.replace('\\'+command+'{maps:src:F.1.3}',r'\cite[Corollary 1.4, p.~4]{ffMandal}')
 s=s.replace('\\'+command+'{night:P1.6}',r'\cite[Theorem A, p.~178]{IVVKramerStolz}')
 s=s.replace('\\'+command+'{night:P1.14}',r'\cref{maps:src:F.4.1}')

# Exact locators opened in this writing.
replacements={
 r'\cite[(1.2)--(1.4)]{ffEsoleKang}':r'\cite[equations (1.2)--(1.4), pp.~3--4]{ffEsoleKang}',
 r'\cite[Theorem 2.2.1]{ffPetersSterk}':r'\cite[Theorem 2.2.1, p.~61]{ffPetersSterk}',
 r'\cite[Definition 4.2.4, Proposition 4.2.5 and Theorem 4.2.6]{ffDeligne}':r'\cite[Definition 4.2.4 and Proposition 4.2.5, p.~44; Theorem 4.2.6, p.~45]{ffDeligne}',
 r'\cite[Definition 2.1]{ffAlarconForstneric25}':r'\cite[Definition 2.1, p.~4]{ffAlarconForstneric25}',
 r'\cite[Proposition 7.13]{ffAlarconForstneric25}':r'\cite[Proposition 7.13 and preceding paragraph, pp.~23--24]{ffAlarconForstneric25}',
 r'\cite[Proposition 7.13(d)]{ffAlarconForstneric25}':r'\cite[Proposition 7.13(d), p.~24]{ffAlarconForstneric25}',
 r'\cite[Theorem 2.13]{ffAlarconForstneric25}':r'\cite[Theorem 2.13, p.~9]{ffAlarconForstneric25}',
 r'\cite[Theorem 1.2]{ffForstnericPrezelj02}':r'\cite[Theorem 1.2, preprint p.~3]{ffForstnericPrezelj02}',
 r'\cite[Lemma 2.1 and Theorem 2.4, \S2]{ffMandal}':r'\cite[Lemma 2.1, p.~5, and Theorem 2.4, p.~7]{ffMandal}',
}
for a,b in replacements.items():s=s.replace(a,b)
# This exact pagination belongs to the opened v5 preprint.
s=s.replace('{ffAlarconForstneric25}', '{IVVOkaOneV5}')
s=s.replace(r'\cite[Definition 7.7]{IVVOkaOneV5}',r'\cite[Definition 7.7, p.~22]{IVVOkaOneV5}')
s=s.replace(r'\cite[Lemma 5.1 and Theorem 6.1]{IVVOkaOneV5}',r'\cite[Lemma 5.1, pp.~14--17, and Theorem 6.1, pp.~17--19]{IVVOkaOneV5}')
s=s.replace(r'\cite[Theorem 3.4]{BHJ22}',r'\cite[Theorem 3.4, p.~6]{BHJ22}')
s=s.replace(r'\cite[Algorithm 8.3]{BHJ22}',r'\cite[Propositions 8.1--8.2 and Algorithm 8.3, p.~21]{BHJ22}')
s=s.replace(r'\cite[Algorithm 8.3]{rootBHJ22}',r'\cite[Algorithm 8.3, p.~21]{rootBHJ22}')
s=s.replace(r'\cite{rootBHJ22}',r'\cite[Algorithm 8.3 and its correctness proof, p.~21]{rootBHJ22}')
s=s.replace(r'\cite[Theorem 3.4 and Propositions 8.1--8.2]{rootBHJ22}',r'\cite[Theorem 3.4, p.~6; Propositions 8.1--8.2, p.~21]{rootBHJ22}')
s=s.replace(r'\cite{ffAchingerOgus20}',r'\cite[Theorem 4.1.1 and Lemmas 4.1.2--4.1.3, pp.~480--482]{ffAchingerOgus20}')

s=s.replace(r'\cite[Theorems 2.3--2.4]{rootScott83}',r'\cite[Theorems 2.3--2.4, p.~425; Euler-characteristic comparison, pp.~427--428]{rootScott83}')

s=s.replace(r'\cite[section on periodic toroidal quotients in arbitrary dimension]{manYang26}',r'\cite[Theorem 8.7, pp.~57--59, and Corollary 8.8, p.~59, attached source build]{manYang26}')

# The current proof invokes the preceding explicit torsion-map lemma.
needle=r'\StatementRecord{maps:src:F.2.6}'
at=s.index(needle);end=s.index('\n\n',at)
part=s[at:end]
part=part.replace('the hypotheses, notation and definitions stated here;',r'\cref{mapsaudit:order-four-torsion-transgression}; the hypotheses, notation and definitions stated here;',1)
s=s[:at]+part+s[end:]

# The received inline algorithm statements had no explicit dependency line.
for lab,uses in {
 'maps:src:F.2.33':r'\cref{maps:src:F.2.31}; the displayed affine actions and bar-chain maps',
 'maps:src:F.2.34':r'\cref{maps:src:F.2.33}; \cite[Theorem 4.1.1 and Lemmas 4.1.2--4.1.3, pp.~480--482]{ffAchingerOgus20}; \cite[Theorem 8.7, pp.~57--59, and Corollary 8.8, p.~59, attached source build]{manYang26}',
 'maps:src:F.2.35':r'\cref{maps:src:F.2.31,maps:src:F.2.33,maps:src:F.2.34}; the displayed complement and peripheral maps',
}.items():
 a=s.index(r'\StatementRecord{'+lab+'}');b=s.index('\n\n',a)
 h=s[a:b];assert '{Definitions and the displayed constructions}' in h
 s=s[:a]+h.replace('{Definitions and the displayed constructions}','{'+uses+'}')+s[b:]
a=s.index(r'\StatementRecord{night:P1.13}');b=s.index('\n',a)
h=s[a:b]
h=h.replace(r'{\cref{night:P1.12}}',
 r'{\cref{night:P1.12}; \S\ref{sec:V-known-inputs}; \cite[equations (1.2)--(1.4), pp.~3--4]{ffEsoleKang}; \cite[Theorem 2.2.1, p.~61]{ffPetersSterk}}')
s=s[:a]+h+s[b:]

# Retain every certified digit while allowing the radius its own line.
enclosure=re.compile(
 r'h_b\(1\)\\in\s*\[-1\.03427662241632179949424884537834605259496477790218821132'
 r'\s*\\\s*\\mathbin\{\\pm\}\\\s*8\.11\\cdot10\^\{-57\}\],')
def wrap_enclosure(match):
 return r'''\begin{aligned}
h_b(1)\in\bigl[&
-1.03427662241632179949424884537834605259496477790218821132\\
&\qquad\mathbin{\pm}8.11\cdot10^{-57}\bigr].
\end{aligned}'''
s,n_enclosures=enclosure.subn(wrap_enclosure,s)
assert n_enclosures==2,n_enclosures

known=(P/'known_inputs.tex').read_text()
known=known.replace(r'\subsection{Characteristic and lattice input}',r'\section{Geometric and characteristic conventions}\label{sec:V-known-inputs}')
known=known.replace(r'\cite[Corollary 1.4 and its proof in \S5]{ffMandal}',r'\cite[Corollary 1.4, p.~4, and its proof in \S5]{ffMandal}')
for a,b in replacements.items():known=known.replace(a,b)
marker=s.index(r'\section{')
s=s[:marker]+known+'\n\n'+s[marker:]
(P/'body.tex').write_text(s)
print('V/body.tex',len(s),'characters')
