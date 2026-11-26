from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *

name = 'section_contraction'
unit = 'subsec:II:section-fibre-contractions'
pkg = Package(name, unit)
main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
old74 = block(main, 'cdp:st:C.2.UN.74')
old64 = block(main, 'cdp:st:C.2.UN.64')
(OUT / 'S6_SERIES_PUBLISH_II_sec11_section_contraction_UN74_input.tex').write_text(old74 + '\n', newline='\n')
(OUT / 'S6_SERIES_PUBLISH_II_sec11_section_contraction_UN64_input.tex').write_text(old64 + '\n', newline='\n')
new74 = old74
oldhead = new74.splitlines()[0]
newhead = r'''\begin{proposition}[Contraction of a section and ruling-fibre boundary]\hypertarget{tag-P335}{}\label{prop:II:section-fibre-contraction}
\hypertarget{tag-01EL}{}\label{cdp:st:C.2.UN.74}'''
new74 = pkg.edit(new74, oldhead, newhead, 'D12,D14,D16', 'cdp:st:C.2.UN.74', 'Give the complete weighted construction one earlier owner before UN64; retain the original statement identity as an alias.')
oldrecord = next(x for x in new74.splitlines() if x.startswith(r'\StatementRecord'))
newrecord = r'''\StatementRecord{prop:II:section-fibre-contraction}{proved}{P335}{\cref{cdp:st:C.2.UN.17,lem:II:blowup-topology}; \cite[Main Theorem, pp.~483--484; \S3, pp.~499--501]{Nakano1970}; \cite[\S2, Theorem~2\(^{\prime}\) and proof, pp.~640--642; Proposition~9\(^{\prime}\) and proof, p.~642]{FujikiNakano1971}}
\StatementRecord{cdp:st:C.2.UN.74}{proved}{01EL}{}'''
new74 = pkg.edit(new74, oldrecord, newrecord, 'D12,D14,D17,D18', 'cdp:st:C.2.UN.74', 'Declare the exact earlier canonical/blowup inputs and the reopened analytic contraction loci; remove the dependency on the later specialization UN64.')
new74 = pkg.edit(new74, 'Thus the full fibre weights on the ruling-fibre\nboundary enter the actual root line $M$; they are\nnot discarded.', 'The full fibre weights on the ruling-fibre\nboundary determine the displayed power of the normal line $M$.', 'D02,D11,D20', 'cdp:st:C.2.UN.74', 'State the retained power isomorphism directly; its full multiplicities and torsion information are unchanged.')
new74 = pkg.edit(new74, 'For the underlying reduced supports,', r'''Put $S=(f^{-1}(0))_{\mathrm{red}}$ and
$S'=(f'^{-1}(0))_{\mathrm{red}}$. Their invariants satisfy''', 'D20', 'cdp:st:C.2.UN.74', 'Name the two full reduced supports used in the Euler formula and identify S as the complete inverse image of S\u2032.')
oldsource = r'''If $m_T=m_P$, the restriction is precisely
$\OO_{\PP^1}(-1)$. The corrected theorem of
\cite[\S2, Theorem~2' and Proposition~9']{FujikiNakano1971},
in the form used in \ref{cdp:st:C.2.UN.64}, supplies the actual
smooth blowdown along $p:T\to B$. It identifies
$U$ with the ordinary blowup of a smooth curve
in a smooth threefold $U'$. Conversely an
ordinary such blowup has normal degree minus
one, so \eqref{cdp:eq:C.RC.8} forces $m_T=m_P$.'''
newsource = r'''If $m_T=m_P$, the restriction is $\OO_{\PP^1}(-1)$.
Apply the analytic contraction theorem of
\cite[Main Theorem, pp.~483--484]{Nakano1970}, using the
normal-line criterion established in
\cite[\S2, Theorem~2\(^{\prime}\) and proof, pp.~640--642;
Proposition~9\(^{\prime}\) and proof, p.~642]{FujikiNakano1971}.
In the source's notation, $(\widetilde X,S,M,r)=(U,T,B,2)$:
$T$ is the specified holomorphic projective-line bundle and
$\OO_U(T)|_{p^{-1}(b)}=\OO_{\PP^1}(-1)$ for every $b$.
Its local morphism restricts to this same $p$, and identifies
the neighbourhood with the ordinary blowup of a smooth
codimension-two centre. The local morphisms glue to the identity
off $T$ by \cite[\S3.2, pp.~500--501]{Nakano1970}.
They give the proper blowdown $\pi:U\to U'$ onto a smooth
threefold, with $U=\operatorname{Bl}_B U'$.
Conversely an ordinary such blowup has normal degree minus
one, so \eqref{cdp:eq:C.RC.8} forces $m_T=m_P$.'''
new74 = pkg.edit(new74, oldsource, newsource, 'D12,D14,D17,D18,D20', 'cdp:st:C.2.UN.74', 'The freshly opened corrected source applies to exactly the given ruling and normal line; its chart maps and exterior gluing replace the reference to the later terminal case.')
new74 = pkg.edit(new74, 'It remains to prove the claimed structure\nat the centre rather than infer it from a\nnumerical normal degree.', 'The images of the boundary components are determined by\ntheir first normal terms along the centre, as follows.', 'D02,D08', 'cdp:st:C.2.UN.74', 'Introduce the retained first-normal-term comparison directly.')
new74 = pkg.edit(new74, 'The exceptional divisor of\nthe ordinary blowup is the\nlines projectivization of\nthis very $V$,', r'''The exceptional divisor of
the ordinary blowup is $\PP_B(V)$, where $\PP_B(V)$
parametrizes lines in $V$,''', 'D20', 'cdp:st:C.2.UN.74', 'State the projectivization convention at its unique general owner and preserve the specified subline.')
new74 = pkg.edit(new74, 'When $r=0$ the extension\nis precisely the one\nretained in \\ref{cdp:st:C.2.UN.64}.', r'''When $r=0$ in the full reduced case, the same formulas give
$M=\OO_B$, $L=K_B$ and the endpoint-framed sequence
$0\to K_B\to V\xrightarrow{df'}\OO_B\to0$;
its extension class is the element of $H^1(B,K_B)$
defined by these normal maps.''', 'D12,D14,D20', 'cdp:st:C.2.UN.74', 'Expose the exact r=0 specialization at the earlier general owner; it uses no later premise and retains both extension endpoints.')
new74 = pkg.edit(new74, r'''\item Restrict the actual vertical
canonical evaluation section
on $U'$ to $B$. Its line
isomorphism is''', r'''\item Apply \cref{cdp:st:C.2.UN.17} to the descended proper
torus family. Ordinary pullback gives
$f'_*K_{U'}\to f_*K_U$. Its inverse restricts a form on $U$
to $U\setminus T$, transports it through the isomorphism
$U\setminus T\simeq U'\setminus B$, and extends its coefficients
in smooth volume frames across $B$ by Hartogs' theorem.
Both compositions are the identity on the common open set
and hence everywhere. Thus a generator downstairs pulls back to a
generator upstairs. Restrict its vertical canonical line to
$B$; the resulting isomorphism is''', 'D20,D25', 'cdp:st:C.2.UN.74', 'Make explicit the generator identification already used by the original Jacobian/order calculation, for this exact ordinary blowup; no additional family or canonical normalization is assumed.')
oldeuler = r'''The actual blowup gives
$S\setminus T\simeq S'\setminus B$,
whereas $T$ is a
projective-line bundle
of Euler number $2e(B)$.
Hence $e(S)-e(S')=e(B)$,
independently of the
full multiplicities.'''
neweuler = r'''Apply \cref{lem:II:blowup-topology} to the same
ordinary blowup $\pi$, the smooth compact centre $B$ and
the compact reduced support $S'\supset B$. Its full reduced
inverse image is $S$, with exceptional divisor $T=\PP_B(V)$.
The complement isomorphism $S\setminus T\simeq S'\setminus B$
therefore gives $e(S)-e(S')=e(B)=2-2g(B)$ through that
owner's blowup comparison, for all the stated fibre weights.'''
new74 = pkg.edit(new74, oldeuler, neweuler, 'D12,D20', 'cdp:st:C.2.UN.74', 'Apply the earlier blowup owner to the identical compact full inverse-image support and codimension-two centre.')
new74 = pkg.edit(new74, 'As in \\ref{cdp:st:C.2.UN.64}, the actual\nlocal blowdowns glue to\nthe identity off $T$.\nThis proves the compact\nversion as well.', 'The local blowdowns glue to the identity off $T$ by the\nsame source overlap maps already used above. Thus, on a\ncompact total space, they define the stated contraction\nover the original compact base.', 'D12,D14,D17', 'cdp:st:C.2.UN.74', 'The compact statement follows from the same analytic source gluing; it has no forward dependence on UN64.')
new74 = pkg.clean(new74, 'cdp:st:C.2.UN.74')
new74 = new74.replace(r'\ref{', r'\cref{')
fragment = '\\subsection{Section and ruling-fibre contractions}\\label{' + unit + '}\n\n' + new74
heading = r'\subsection{Terminal ruled contractions}\label{subsec:II:terminal-ruled-contractions}'
pkg.guard('P335-before-terminal', heading, fragment + '\n' + heading, 'Insert the complete general weighted owner immediately before its r=0 terminal specialization.')
pkg.guard('UN74-transfer', old74, '', 'All UN74 statement, proof, equation labels and targets move to the earlier P335 owner; no duplicate construction remains here.')

new64 = old64
start = old64.index('For the contractions, use the analytic blowdown theorem')
stop = old64.index(r'\item In the plane-line case the normal line', start)
oldcurve = old64[start:stop]
matrix_start = oldcurve.index('Serre duality gives')
matrix_tail = oldcurve[matrix_start:]
newcurve = r'''\item In the section case, apply
\cref{prop:II:section-fibre-contraction} to the same family and ruling,
with $(p,m_T,m_P,r)=(q,1,1,0)$. The only boundary is $C$,
so there are no $Q_j$ or marked points $b_j$. The normal lines
in that proposition are $M=\OO_B$ and $L=K_B$ by
\eqref{cdp:eq:C.RC.6}. Its blowdown is therefore the given ruling
contraction, $P\to P'$ is the Cartier blowup isomorphism, and
$df'$ is the normal quotient $V\twoheadrightarrow\OO_B$ with
no zero on $B$. Thus $f'$ is a submersion along the centre.
The exceptional divisor and its marked section are exactly
$(\PP_B(V),\PP_B(K_B))$; \eqref{cdp:eq:C.RC.10} with $M=\OO_B$
gives $N_{T/U}=\OO_{\PP_B(V)}(-1)=\OO_T(-C)$.
These are all the maps and the reduced SNC conclusion in
\eqref{cdp:eq:C.EL.3}, including the Euler equality from
\eqref{cdp:eq:C.RC.7}. The extension keeps its subline $K_B$
and its quotient trivialization $df'$.

''' + matrix_tail
new64 = pkg.edit(new64, oldcurve, newcurve, 'D12,D14,D17,D20', 'cdp:st:C.2.UN.64', 'The complete repeated ruled blowdown, submersion, Cartier restriction and normal-extension proof is the exact r=0,m=1 application of P335. Preserve the subsequent extension cocycle and compact realizations.')
new64 = pkg.edit(new64, 'The same analytic theorem, with centre a point, produces an\nordinary point blowdown onto a smooth threefold.', 'Apply \\cite[Main Theorem, pp.~483--484; \\S3, pp.~499--501]{Nakano1970},\nwith the normal-line criterion of\n\\cite[\\S2, Theorem~2\\(^{\\prime}\\) and proof, pp.~640--642;\nProposition~9\\(^{\\prime}\\) and proof, p.~642]{FujikiNakano1971},\nto $(\\widetilde X,S,M,r)=(U,T,\\{p\\},3)$. It gives an\nordinary point blowdown onto a smooth threefold.', 'D17,D18,D20', 'cdp:st:C.2.UN.64', 'The plane case retains its direct corrected analytic source application with the explicit source data; the P335 ruling case does not silently substitute a different fibre dimension.')
oldeuler64 = r'''\item For a curve contraction, the map is an isomorphism off $T$,
with fibre $\PP^1$ over each point of $B$. Additivity gives
$e(S)-e(S')=e(T)-e(B)=e(B)=2-2g(B)$.
For a point contraction it gives $e(T)-1=3-1=2$.'''
neweuler64 = r'''\item The curve-contraction Euler equality is the same
$r=0$ specialization of \eqref{cdp:eq:C.RC.7}. For the point
contraction apply \cref{lem:II:blowup-topology} to the point
centre and the compact full inverse-image support: its
exceptional fibre is $\PP^2$, giving $e(T)-1=3-1=2$.'''
new64 = pkg.edit(new64, oldeuler64, neweuler64, 'D12', 'cdp:st:C.2.UN.64', 'Use the same earlier blowup maps for both Euler defects without repeating their additivity proof.')
oldrecord64 = next(x for x in new64.splitlines() if x.startswith(r'\StatementRecord'))
newrecord64 = oldrecord64.replace(r'\cref{cdp:st:C.2.UN.17}', r'\cref{cdp:st:C.2.UN.17,prop:II:section-fibre-contraction,lem:II:blowup-topology}')
new64 = pkg.edit(new64, oldrecord64, newrecord64, 'D12,D14', 'cdp:st:C.2.UN.64', 'Record the earlier general construction and blowup comparison; all original direct source and compact-period inputs remain.')
pkg.guard('UN64-application', old64, new64, 'Complete old/receiving UN64 comparison; only the bounded common construction, source map and Euler applications change.')
(OUT / 'S6_SERIES_PUBLISH_II_sec11_section_contraction_UN64_receiving.tex').write_text(new64 + '\n', newline='\n')
for row in pkg.rows:
    if row['statement_id'] == 'cdp:st:C.2.UN.64':
        row['old_location'] = 'subsec:II:terminal-ruled-contractions / cdp:st:C.2.UN.64'
        row['new_location'] = 'subsec:II:terminal-ruled-contractions / cdp:st:C.2.UN.64'
pkg.write(fragment)

receiving = main
for g in pkg.guards:
    assert receiving.count(g['old']) == 1, (g['key'], receiving.count(g['old']))
    receiving = receiving.replace(g['old'], g['new'], 1)
for pattern in [r'\\label\{([^{}]+)\}', r'\\hypertarget\{([^{}]+)\}']:
    for x in set(re.findall(pattern, old74 + old64)):
        assert re.findall(pattern, receiving).count(x) == re.findall(pattern, main).count(x), x
print('Three guards replay once; all old statement/equation label and target multiplicities retained. No shared main write.')
