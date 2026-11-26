#!/usr/bin/env python3
"""Guarded publication edits for 039U and its shared distance proof."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

ROOT = Path(__file__).resolve().parents[1]
paths = {
    'regular': ROOT / 'agents/continuation8_iii_integration/units/root/regular_quotients.tex',
    'carriers': ROOT / 'agents/continuation8_iii_integration/units/later/further_cusp_carriers.tex',
    'metrics': ROOT / 'agents/continuation8_iii_integration/units/later/fixed_target_metrics.tex',
}
expected = {
    'regular': '0e16d43212a0b1e384a581fe548587093bd58e6f8e948335cf68574276b72f56',
    'carriers': '7c14f683021dce61503f2c5d7d79b711924b4f0daf4b365fb85de8c242f9ef5e',
    'metrics': 'b620874b9a1c7d0d704455bb611b45df506d092f335011af940ba36dda2fe7fe',
}
texts = {key: path.read_text() for key, path in paths.items()}
before_all = dict(texts)
for key, value in texts.items():
    assert hashlib.sha256(value.encode()).hexdigest() == expected[key], key
rows = []

def record(key, old, new, kind, sid, reason, line):
    rows.append(dict(change_id='c8-III-regular-%03d' % (len(rows) + 1),
        type=kind, statement_id=sid,
        old_location=str(paths[key].relative_to(ROOT)) + ':' + str(line),
        old_page='pending final concordance',
        new_location=str(paths[key].relative_to(ROOT)) + '; same owner unless explicitly moved',
        new_page='pending final build', old_text=old, new_text=new,
        reason=reason, review_status='staged; complete changed-source reading pending'))

def replace(key, old, new, kind, sid, reason):
    value = texts[key]
    assert value.count(old) == 1, (key, old[:90], value.count(old))
    line = value[:value.index(old)].count('\n') + 1
    record(key, old, new, kind, sid, reason, line)
    texts[key] = value.replace(old, new)

sid = 'wb:cusp-spec-globalization-obstruction'
candidate, edits, issues, aliases = presentation.remove_manual_equation_tags(texts['regular'])
assert aliases == ['G.1', 'G.2'] and not issues
assert not presentation.unresolved_literal_equation_references(candidate, aliases)
for edit in edits:
    record('regular', edit.old, edit.new, edit.kind, sid, edit.reason,
           texts['regular'][:edit.start].count('\n') + 1)
texts['regular'] = candidate

replace('regular', r'''\begin{theorem}[The maximal regular-locus
\texorpdfstring{\(\mathbb R^4\)}{R4} quotient and its compactification
obstruction]
\hypertarget{tag-039U}{}\label{wb:cusp-spec-globalization-obstruction}


Let
''', r'''\begin{definition}[Regular quotient data]
\hypertarget{tag-Q310}{}\label{mapsIII:def:regular-quotient-data}
{\normalfont\scriptsize tag Q310}\par
Let $f:X\to B$ be the three-fibre family of \cref{maps:src:B.5.2},
with $B^\circ=B\setminus\{p_0,p_1,p_2\}$ and
$J=f^{-1}(B^\circ)$. Use its period marking and the unrescaled
radial Euclidean fibre metrics of
\cref{wb:cusp-spec-radial-notation,wb:cusp-spec-native-quotient}.
Write
''', 'D10/D13/D16/D26', 'mapsIII:def:regular-quotient-data',
    'Place the operative fixed family, marking, metric and lattice data in one numbered definition; this is the same preceding family, with no changed parameter domain.')

generic = r'''Indeed, a distance chain without a free jump in $A$ has length at
least $d_E(x,y)$.  A chain containing such jumps has initial and final
pieces of total length at least $d_E(x,A)+d_E(y,A)$; deleting the
intermediate pieces gives that upper bound through projected paths.
Taking infima proves the formula, including the distance to the
collapsed point.  The projected paths also prove that it is a length
metric, and compactness identifies its topology with the quotient topology.'''
assert texts['carriers'].count(generic) == 1
new_owner = r'''\end{definition}

\begin{lemma}[Length metric after a closed-set collapse]
\hypertarget{tag-Q311}{}\label{mapsIII:lem:collapsed-subset-distance}
{\normalfont\scriptsize tag Q311}\par
For every compact length space $(E,d_E)$ and nonempty closed subset
$A\subset E$, collapsing $A$ to one point gives the quotient length metric
\[
 d_{E/A}([x],[y])
 =\min\{d_E(x,y),d_E(x,A)+d_E(y,A)\},\qquad
 d_{E/A}([x],*)=d_E(x,A).
\]
This metric induces the quotient topology. The quotient map identifies
only the points of $A$, so off the collapsed point its inverse takes
the unique representative in $E\setminus A$.
\end{lemma}
\begin{proof}
''' + generic + r'''
\end{proof}

\begin{theorem}[Global circle quotients and compactification obstructions]
\hypertarget{tag-039U}{}\label{wb:cusp-spec-globalization-obstruction}
{\normalfont\scriptsize tag 039U}\par
For the data of \cref{mapsIII:def:regular-quotient-data}, the following
statements hold.'''
replace('regular', 'Then the following statements hold.', new_owner,
    'D10/D12/D13/D16/D20', sid,
    'Close Q310, move the entire generic quotient-distance proof from 036J to the preceding Q311 owner, and retain one complete 039U statement/proof under its original label and tag. The relocation inverse returns the exact generic proof string to its recorded 036J position.')

replace('regular', r'''full-monodromy-invariant kernel and whose quotient systole tends to infinity
on the radial cusp''', r'''full-monodromy-invariant kernel, with the quotient norm induced by the
unrescaled Euclidean fibre metric, and whose quotient systole tends to
infinity on the radial cusp''', 'D11/D26', sid,
    'Make explicit the metric used in the original bounded-period proof; no scalar-rescaled class is introduced.')
replace('regular', 'The raw character is not invariant:', 'The character transforms by:',
    'D02/D08', sid, 'State the displayed affine character transformation directly; its nonintegral values and all finite data are unchanged.')
replace('regular', 'It instead descends equivariantly to the Seifert circle family',
    'It descends equivariantly to the Seifert circle family', 'D02/D08', sid,
    'Use direct mathematical prose for the same equivariant descent.')

replace('regular', r'''The cone constructions
\cref{wb:cusp-cone-S12-route} and \cref{wb:cusp-cone-S24-local-route} and \cref{wb:cusp-cone-S24-route}
retain the radial parameter and collapse the boundary cross-section in
their codomains. On their open radial strata, projection to the fixed
torus or circle recovers the quotient maps above. Moreover,
neither''', r'''For $A=(\mathbb R/\mathbb Z)^2$ or $\mathbb R/\mathbb Z$, the
projection $[r,z,a]\mapsto a$ from the positive part of the cone over
$S^1\times A$ recovers the fixed quotient coordinate and has no
continuous extension to the vertex. Neither''', 'D06/D14/D20', sid,
    'State the self-contained cone projection comparison without referring to later construction theorems. The same projection and its nonextension proof remain; the later concrete source maps are unchanged.')
replace('regular', r'''\(r_T:\mathbb R/\mathbb Z\to C_T\),
\([\theta]\mapsto[\ell_T\theta]\), be the arclength isometry.''', r'''\(\vartheta_T:\mathbb R/\mathbb Z\to C_T\),
\([\theta]\mapsto[\ell_T\theta]\), be the arclength isometry,
with inverse $[u]\mapsto[u/\ell_T]$. The domain metric is
$\ell_T^2d\theta^2$.''', 'D11/D20/D23', sid,
    'Use the later carrier arclength notation and display the inverse and domain metric; reserve r_T for the radial cusp parameter. This is the identity map of the old isometry under the renamed symbol.')
replace('regular', r'\xrightarrow{r_T^{\times4}\circ\chi_{\gamma,T}^{[4]}}',
    r'\xrightarrow{\vartheta_T^{\times4}\circ\chi_{\gamma,T}^{[4]}}',
    'D20/D23', sid, 'Apply the same renamed arclength isometry in the permanent target-smash display; the map and old equation owner remain.')
for old, new in [
    ('The literal quotient map and its', 'The specified quotient map and its'),
    (r'No continuous extension of the literal map \(\chi_\gamma\) exists.', r'No continuous extension of the specified map \(\chi_\gamma\) exists.'),
    ('literal map has no continuous extension. The metric', 'specified map has no continuous extension. The metric'),
    (r'Equation \cref{wb:cusp-spec-invariant-character-lattice} proves', r'Equation \eqref{wb:cusp-spec-invariant-character-lattice} proves'),
    (r'Equation \cref{wb:cusp-spec-invariant-character-lattice} gives', r'Equation \eqref{wb:cusp-spec-invariant-character-lattice} gives'),
    (r'\cref{wb:cusp-spec-radial-notation} and \cref{wb:cusp-spec-holomorphic-errors}', r'\cref{wb:cusp-spec-radial-notation,wb:cusp-spec-holomorphic-errors}'),
    (r'\cref{wb:cusp-spec-product-not-sphere} and \cref{wb:cusp-spec-four-product-not-sphere}', r'\cref{wb:cusp-spec-product-not-sphere,wb:cusp-spec-four-product-not-sphere}'),
]:
    replace('regular', old, new, 'D06/D08/D23', sid,
        'Use direct mathematical wording or the existing equation reference without changing the assertion, its proof or its permanent target.')

replace('regular', r'''diffeomorphism \(h:X\to S^6\); a rotation makes it based. For a fixed
fibre inclusion, choose its zero as the basepoint of \(X\).
The Cartesian powers of \(h\) and the integral K\"unneth theorem give''', r'''diffeomorphism $h_0:X\to S^6$. For a fixed fibre inclusion choose
its zero $x_0$ as basepoint, and let $p=h_0(x_0)$ and $b$ be the
north pole of $S^6\subset\mathbb R^7$. The following rotation sends
$p$ to $b$. If $p\ne\pm b$, put $c=\langle p,b\rangle$,
$s=\sqrt{1-c^2}$ and $w=(b-cp)/s$. On the orthonormal plane
$(p,w)$ use the matrix
\[
 R|_{\langle p,w\rangle}
   =\begin{pmatrix}c&-s\\s&c\end{pmatrix},
 \qquad R|_{\langle p,w\rangle^\perp}=I.
\]
For $p=b$ take $R=I$; for $p=-b$ take $R=-I$ on
$\langle p,w\rangle$ for any unit $w\perp p$, and $I$ on its
orthogonal complement. In every case $Rp=b$ and $R^{-1}=R^{\mathsf T}$.
Thus $h=Rh_0$ is based, with inverse $h_0^{-1}R^{\mathsf T}$.
In dimension $d$, let $b$ denote the north pole of $S^d$.
Stereographic projection identifies $(S^d,b)$ with
$(\mathbb R^d)^+$: writing $x=ab+v$ with $v\perp b$, its maps are
\[
 x\longmapsto\frac{v}{1-a},\qquad
 y\longmapsto\frac{2y+(\|y\|^2-1)b}{1+\|y\|^2},
 \qquad b\longleftrightarrow\infty.
\]
An orthonormal basis identifies $b^\perp$ with $\mathbb R^d$;
the two displayed substitutions are inverse.
The Cartesian powers of $h$, with coordinatewise inverse $h^{-1}$,
and the integral K\"unneth theorem give''', 'D20/D22', sid,
    'Supply the full based rotation, all antipodal cases, stereographic maps and inverses used by the original product/smash construction. These explicit maps justify the original based identification without selecting a different source.')
replace('regular', r'''by the identity on \((\mathbb R^6)^n\) and collapse of its complement.
The nonzero''', r'''by the identity on $(\mathbb R^6)^n$ and collapse of its complement.
The inverse splits a finite vector into its $n$ ordered six-dimensional
blocks and sends $\infty$ to the smash basepoint; the inverse of
$h^{\wedge n}$ applies $h^{-1}$ to every nonbasepoint factor.
The block identification and its inverse extend continuously across
infinity because they are proper linear maps. The maps $h^{\wedge n}$
and its inverse descend from the coordinatewise based diffeomorphisms.
The nonzero''', 'D20', sid,
    'State the exact inverse of the original ordered Cartesian-to-smash identification, with its continuity at infinity; the source collapse remains a quotient rather than an isomorphism.')
replace('regular', r'''\(\theta_i\mapsto\tan(\pi(\theta_i/\ell_T-1/2))\).
For the quotient length metric,
\[
 d_Q([x],[y])=\min\{d_{C_T^4}(x,y),
                   d_{C_T^4}(x,F)+d_{C_T^4}(y,F)\}.
\]
The infimum of the lengths of routes through the collapsed point is
the second term; routes avoiding it have length at least the first.
Both terms are attained or bounded above by the corresponding quotient
paths, which proves the formula.''', r'''$\theta_i\mapsto\tan(\pi(\theta_i/\ell_T-1/2))$,
with inverse $y_i\mapsto\ell_T(1/2+\arctan(y_i)/\pi)$, followed
by the stereographic inverse in dimension four. Infinity corresponds
to the collapsed fat wedge. For the quotient length metric,
\cref{mapsIII:lem:collapsed-subset-distance}, with $E=C_T^4$ and
$A=F$, gives
\[
 d_Q([x],[y])=\min\{d_{C_T^4}(x,y),
                   d_{C_T^4}(x,F)+d_{C_T^4}(y,F)\}.
\]
The comparison with that lemma's quotient sends $[x]$ to $[x]$;
its inverse is the same map, with $F$ representing the basepoint.''',
    'D12/D20', sid,
    'Apply the earlier complete Q311 proof to the identical circle-product quotient and retain its full specialized metric formula. Add the cube-chart inverse and the explicit sphere compactification map.')
replace('regular', r'''For the later cone constructions, projection on the open radial stratum
from \([r,\text{angle},\text{quotient}]\) to its torus or circle
coordinate recovers the fixed-target quotient. This projection cannot
extend to the cone vertex: fixed, distinct cross-section points approach
that vertex as \(r\to0\), while their projections remain distinct.
These are the codomain maps relating the cone constructions to the
fixed-target quotients.''', r'''For $A=(\mathbb R/\mathbb Z)^2$ or $\mathbb R/\mathbb Z$, form
the cone by collapsing $\{0\}\times S^1\times A$ in
$[0,\epsilon]\times S^1\times A$. Its positive part has projection
$p([r,z,a])=a$. For any $0<r_0\leq\epsilon$ and $z_0\in S^1$, the map
$a\mapsto[r_0,z_0,a]$ is a section: its composite with $p$ is
the identity. Thus $p$ recovers exactly the fixed quotient coordinate
from a radial quotient map. For distinct $a,a'\in A$, the paths
$[r,z_0,a]$ and $[r,z_0,a']$ approach the same vertex as $r\to0$,
while their projections are constantly $a$ and $a'$. Continuity at
that vertex is therefore impossible.''', 'D06/D14/D20/D27', sid,
    'Keep the full cone-comparison assertion and obstruction as explicit cone, projection, section and two-path maps, independent of the later construction statements.')

old_carrier = r'''We verify the metric of the first homeomorphism.  Collapsing a
nonempty closed subset $A$ of a compact length space $E$ gives
\[
 d_{E/A}([x],[y])
   =\min\{d_E(x,y),d_E(x,A)+d_E(y,A)\}.
\]
''' + generic
new_carrier = r'''For the metric comparison use
\cref{mapsIII:lem:collapsed-subset-distance} on
$Q_T/K_T^{(1)}$, on the smash of its twofold product, and on
$Q_T^2/W_{12,T}$ and $C_T^4/W_{24,T}$. In each case the map
to that lemma's quotient is $[x]\mapsto[x]$, with the same inverse;
off the collapsed point it takes the unique uncollapsed tuple, and
the collapsed subset represents the basepoint. The lemma supplies
the quotient distance, length and quotient-topology assertions.'''
replace('carriers', old_carrier, new_carrier, 'D12/D14/D20',
    'wb:cusp-cone-angle-forgotten-sphere-carriers',
    'Move the complete generic proof, unchanged, to earlier Q311; keep every 036J specialized successive-collapse identity and whole-ball proof. The identity on each displayed quotient and its inverse identify all four applications.')
replace('metrics', r'''\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}, applied here
to the same identity quotient''', r'''\cref{mapsIII:lem:collapsed-subset-distance}, applied here
to the same identity quotient''', 'D06/D12/D14', 'mapsIII:lem:fixed-conical-metrics',
    'Point the same explicit identity-quotient application to the sole earlier Q311 owner; all metric construction and topology conclusions are unchanged.')
replace('metrics', r'''closed-set distance formula and the period estimates proved in
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.''', r'''closed-set distance formula of
\cref{mapsIII:lem:collapsed-subset-distance} and the period estimates in
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.''', 'D06/D12', 'mapsIII:rem:source-and-moving-metrics',
    'Identify the distance and period proof owners separately; all maps, lower bounds and metric comparisons remain unchanged.')

identifier = re.compile(r'\\(?:label|hypertarget)\{([^}]+)\}')
for key, value in texts.items():
    old_ids = Counter(identifier.findall(before_all[key]))
    new_ids = Counter(identifier.findall(value))
    assert not (old_ids - new_ids), (key, old_ids - new_ids)
    additions = new_ids - old_ids
    if key == 'regular':
        assert additions == Counter({'tag-Q310': 1, 'mapsIII:def:regular-quotient-data': 1,
                                     'tag-Q311': 1, 'mapsIII:lem:collapsed-subset-distance': 1})
    else:
        assert not additions, (key, additions)
    assert not presentation.remove_manual_equation_tags(value)[2]
    assert '\r' not in value
    paths[key].write_text(value)
    print(key, len(value.splitlines()), hashlib.sha256(value.encode()).hexdigest())
out = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_regular_publication_defects.tsv'
fields = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with out.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Exact local edit rows', len(rows), 'new formal tags Q310,Q311; all prior identifiers preserved.')
print('All TSV rows use LF; no canonical, shared-ledger or criterion-count writes.')
