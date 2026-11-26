"""Make the first-page restriction morphism and theorem navigation explicit."""
from S6_SERIES_PUBLISH_c3_edit import *

changes = [
('II-C3-FIRSTPART-SERIES-PROSE',['D08'],'the-series-and-this-paper',
 r'''monodromy, and the higher-dimensional complex manifolds built from it.
The table gives the main result of each paper and the papers it uses.''',
 r'''monodromy, and the higher-dimensional complex manifolds built from it.''',
 'The table headers already identify its contents; the mathematical series paragraph remains.'),
('II-C3-FIRSTPART-C-CONSTRUCTION',['D04'],'series:II:C',
 r'''$c_3(Y)=0$ and $b_3(Y)=2$; the compact construction
\ref{cdp:st:D.2.7} attains this value with''',
 r'''$c_3(Y)=0$ and $b_3(Y)=2$; the compact construction in
\cref{cdp:st:D.2.7} attains this value with''',
 'Use the current typed statement reference for the cited compact construction.'),
('II-C3-FIRSTPART-C-STATUS-REF',['D04'],'series:II:C',
 r'''\textit{Relation to literature.} The sign and equality theorem
\ref{cdp:st:C.2.G.1} extends the standard-family Euler value of''',
 r'''\textit{Relation to literature.} The sign and equality criterion in
\cref{cdp:st:C.2.G.1} extends the standard-family Euler value of''',
 'The body statement type is supplied by its current reference.'),
('II-C3-FIRSTPART-D-SCOPE',['D02','D11'],'series:II:D',
 r'''Let $f:Y\to B$ be a proper holomorphic map from a smooth complex
threefold to a smooth complex curve, with connected fibres and
smooth general fibre a complex two-torus. Every reduced fibre
support has even Euler number, with arbitrary singularities and
multiplicities. This assertion imposes no compactness, K\"ahler
or Betti-number condition on $Y$.''',
 r'''Let $f:Y\to B$ be a proper holomorphic map from a smooth,
possibly noncompact, complex threefold to a smooth complex curve,
with connected fibres and smooth general fibre a complex two-torus.
Every reduced fibre support has even Euler number, with arbitrary
singularities and multiplicities.''',
 'The initial unrestricted smooth-threefold hypothesis gives exactly the original domain; the proof and all parity conclusions are unchanged. State noncompactness there and remove the repeated defensive scope sentence.'),
('II-C3-FIRSTPART-D-RESTRICTION',['D20','D22'],'series:II:D',
 r''' \pi:\widetilde Y\to Y,
 \qquad e((\widetilde Y_b)_{\rm red})=2k,
 \qquad \pi|_{B\setminus\{b\}}\text{ a biholomorphism}.''',
 r''' \begin{gathered}
 \pi:\widetilde Y\to Y,\qquad e((\widetilde Y_b)_{\rm red})=2k,\\
 \pi:\widetilde Y|_{B\setminus\{b\}}
       \xrightarrow{\ \simeq\ }Y|_{B\setminus\{b\}}.
 \end{gathered}''',
 'The original subscript named a base subset as though it were a domain of pi. The displayed restriction is the exact base-restricted morphism: each blowup centre lies over b, its ideal is the unit ideal off b, and the blowup and its inverse there are the identity. No statement scope changes.'),
('II-C3-FIRSTPART-G-STATUS-REF',['D04'],'series:II:G',
 r'''\textit{Relation to literature.} The minimal parameter covering
\ref{ii:LR:covering} is determined for the scalar action and good-root''',
 r'''\textit{Relation to literature.} The minimal parameter covering in
\cref{ii:LR:covering} is determined for the scalar action and good-root''',
 'Use the current typed statement reference for the covering theorem.'),
]
for key,kinds,owner,old,new,reason in changes:
    apply_edit(old,new,key,kinds,owner,'First part, '+owner,reason,
               'Root reread complete current abstract, series paragraph/table, all main theorems and their outlines, known/new table and methodology; each bounded old/new change read in full.')
add_event('the-series-and-this-paper;series:II:C;series:II:D;series:II:G',
          'II-C3-FIRSTPART-NAVIGATION', 'used and rechecked in this run',
          'Root reread the complete first part through methodology. Theorem D now displays the exact base-restricted blowup morphism and places its noncompact scope in the first hypothesis; three bare references now give statement types. All mathematical hypotheses and conclusions are preserved. Marked-point definitions, exact source-status locators, final counts and final organization remain pending. No new independent check or complete main-theorem gate is claimed.',
          'First-part bounded navigation and restriction map',source=__file__)

assessments = {
 'D01':'The mathematical series scope and dependency table contain no production history.',
 'D02':'The paragraph and table have no defensive assertion or redundant unused hypothesis.',
 'D03':'No prompt-directed rebuttal or unsupported refutation occurs.',
 'D04':'The first-part series table uses paper numerals and mathematical titles, not run labels.',
 'D05':'No prompt item supplies an object, hypothesis or reference.',
 'D06':'No inaccessible external numbering is printed in this unit.',
 'D07':'The series paragraph/table contain no model, worker or run terminology.',
 'D08':'The redundant table-preview sentence was removed in II-C3-FIRSTPART-SERIES-PROSE; the remaining paragraph states the series scope.',
 'D09':'There is no program path or implementation dump in the paragraph/table.',
 'D11':'No repeated scope disclaimer remains.',
 'D12':'The unit has one mathematical scope paragraph and the one required common series table.',
 'D13':'No unnumbered mathematical definition, lemma or proof is introduced here.',
 'D17':'No known theorem is re-proved in the introductory series paragraph.',
 'D19':'This unit has no numbered formula or manual equation tag.',
 'D20':'The table and paragraph use the common (3,4,infinity), sphere and smooth-monodromy notation.',
 'D21':'No empirical or program agreement is stated as proof.',
 'D22':'The paragraph/table introduces no unsupported auxiliary choice or parameter.',
 'D25':'The full current paragraph/table reading found no local mathematical contradiction; the final cross-paper dependency correspondence remains D24 open.'
}
for kind,basis in assessments.items():
    set_unit_status('the-series-and-this-paper',kind,'done',
                    basis+' Root read the entire current unit. D14/D15/D18/D23/D24 and structure remain pending at their global gates.',
                    'CHECK_EVENTS.tsv: II-C3-FIRSTPART-NAVIGATION')
print('Bounded first-part edits recorded; 18 stable local rows of the complete series unit closed.')
