from S6_SERIES_PUBLISH_c3_edit import *
import json

apply_edit(r'''The Remmert--Stein extension across the origin
is an analytic curve germ; a power $F^h$ fixes
one of its branches.''',r'''Apply the Remmert--Stein extension theorem
\cite[Expos\'e~13, \S1, Corollary~1, p.~13-1]{Stein1954Extension}
with removed set $\{0\}$ and the lifted curve of dimension one.
Its closure is analytic across the origin. A power $F^h$ fixes
one of its finitely many branches.''',
    'II-C3-HOPF-EXTENSION',['D18'],'night:P4.24','Step 4',
    'Opened the exact primary theorem by Stein and the corollary proof in Expose14§4. Its removed set is the origin of dimension zero and the analytic set is the lifted one-dimensional curve.')
apply_edit(r'''Its double
dual $Q^{**}$ is locally free
\cite[Tag~0B3N]{StacksProject}, and''',r'''For every $p\in T$, the stalk $(Q^{**})_p$ is a finite
reflexive module over the regular local analytic ring
$\mathcal O_{T,p}$ of dimension two. Apply the local-ring
argument of \cite[Tag~0B3N]{StacksProject} to this module
over that same ring; it is free. Hence $Q^{**}$ is locally
free, and''',
    'II-C3-HOPF-REFLEXIVE',['D18'],'night:P4.24','Step 9',
    'Opened all of Stacks0B3N and its local argument; makes the analytic-to-algebraic input exact through the identical regular local ring and stalk module, with no unsupported global category transfer.')
for index,old,new,why in [
    (1,r'''\item We first construct on $T_0$ a nonsingular
holomorphic foliation tangent to every compact
curve. Khaled''',r'''\item On $T_0$ we construct a nonsingular holomorphic foliation
tangent to every compact curve. Khaled''','Removes the proof-roadmap qualifier.'),
    (2,r'''This proves the foliation assertion.

\item Pull this foliation''',r'''\item Pull this foliation''','Removes a repeated closing summary of the two completed foliation cases.'),
    (3,r'''The only singularities of
the foliation are simple saddles. To verify
this assertion and its multiplicities, at a
regular point use coordinates''',r'''At a regular point use coordinates''','The immediately following charts establish the saddle assertion and its multiplicity directly.'),
    (4,r'''Writing $R'=\mu^*R+cE$ gives $c\in\mathbb Z$,
without any positivity requirement on $c$.''',r'''Writing $R'=\mu^*R+cE$ gives $c\in\mathbb Z$.''','The displayed integer range already states the exact coefficient scope.'),
    (5,r'''\item We now identify the conductor maps.
The reduced conductor''',r'''\item The reduced conductor''','Begins directly with the conductor geometry used in the proof.')]:
    apply_edit(old,new,f'II-C3-HOPF-REGISTER-{index:02}',['D02' if index==4 else 'D08'],
               'night:P4.24','Complete receiving proof reading',why)

anchor=r'\bibitem[Steinberg(1965)]{Steinberg1965}'
bib=r'''\bibitem[Stein(1954)]{Stein1954Extension}
Karl Stein.
\newblock Un th\'eor\`eme sur le prolongement des ensembles analytiques.
\newblock \emph{S\'eminaire Henri Cartan}, 6 (1953--1954),
expos\'es 13 (15 March 1954), 1--10, and 14 (22 March 1954), 1--8.
\newblock URLs \url{https://www.numdam.org/item/SHC_1953-1954__6__A13_0/},
\url{https://www.numdam.org/item/SHC_1953-1954__6__A14_0/}.

'''
apply_edit(anchor,bib+anchor,'II-C3-STEIN-EXTENSION-BIB',['D18'],
           'Stein1954Extension','Bibliography','Adds both opened original seminar parts; no DOI is assigned in the publisher record.')
metadata={r['source']:r for r in map(json.loads,(ROOT/'code/S6_SERIES_PUBLISH_c3_primary_fetch.out').read_text().splitlines())}
readings=[
    dict(source='Stein 1954 extension',url=metadata['Stein1954Exp13']['url'],
         version='Seminaire Henri Cartan6(1953–1954),Expose13(15Mar1954) and14(22Mar1954), Numdam scans',
         locus='Expose13§1 pp13-1–13-2, theorem and Corollary1; Expose14§4 pp14-1–14-2, complete corollary proof',
         sha256=metadata['Stein1954Exp13']['sha256']+'; Expose14: '+metadata['Stein1954Exp14']['sha256'],
         own_word_summary='An analytic set of pure dimension k extends analytically across an analytic removed set whose local dimension is strictly smaller than k. The corollary is deduced by a local induction from the fundamental extension lemma.',
         use='night:P4.24: lifted compact curve in punctured C2, removed point dimension0 and curve dimension1'),
    dict(source='Stacks Project 0B3N',url=metadata['Stacks0B3N']['url'],
         version='Live official tag0B3N, read22Nov2026; displayed Lemma31.13.15',
         locus='Full lemma and complete proof, especially regular local ring of dimension2',
         sha256=metadata['Stacks0B3N']['sha256'],
         own_word_summary='A finite reflexive module over a two-dimensional regular local ring has depth two and is free. The sheaf assertion is obtained by applying this to stalks.',
         use='night:P4.24: the identical analytic stalk ring O(T,p) and module (Q double dual)p')
]
for row in readings:row['date_utc']=now()
print('Primary rows',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',readings,'source'))
print('Final local Hopf citations and register edits admitted.')
