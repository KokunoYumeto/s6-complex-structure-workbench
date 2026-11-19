"""Receiving-only edits to the two independently reviewed CP29 exports.

Executed by revise_body.py after the original complete proofs are assembled.
Every replaced source sentence is retained in the reconciliation manifest.
"""
cp29_edits=[]

def exact_replace(t,label,old,new,reason):
    assert t.count(old)==1,(label,reason,t.count(old),old[:100])
    cp29_edits.append(dict(label=label,old=old,new=new,reason=reason))
    return t.replace(old,new,1)

root_new_replacements=W/'analysis/IV/root_F47_56_receiving_replacements.json'
if root_new_replacements.exists():
    for root_new in json.loads(root_new_replacements.read_text()):
        def apply_root_new(t,e=root_new):
            return exact_replace(t,e['label'],e['old'],e['new'],e['reason'])
        change(root_new['label'],apply_root_new,
               'Integrate the full independently rederived current source/cap proof scope and its exact physical, local-group or completed-dependency repair.')
root_later_replacements=W/'analysis/IV/root_K67_83_receiving_replacements.json'
if root_later_replacements.exists():
    for root_later in json.loads(root_later_replacements.read_text()):
        def apply_root_later(t,e=root_later):
            return exact_replace(t,e['label'],e['old'],e['new'],e['reason'])
        change(root_later['label'],apply_root_later,
               'Integrate the current typed integer-cover, exact cutoff inequality and named-review scope repairs from the complete independent proof review.')


peer_next_replacements=W/'analysis/IV_next_batch/receiving_replacements.json'
if peer_next_replacements.exists():
    for peer_next in json.loads(peer_next_replacements.read_text()):
        def apply_peer_next(t,e=peer_next):
            return exact_replace(t,e['label'],e['exact_old'],e['exact_new'],e['reason'])
        change(peer_next['label'],apply_peer_next,
               'Integrate the complete independently rederived cap and fan proof with its exact relation matrix, deck notation and corrected vertical normal coefficient.')

def receive_k106(t):
    label='night:P3K.106'
    edits=[
    (r'''specify their inverses. For a chosen Hermitian metric, the map
\(\overline{N_{-}}\) to \(N_{-}^{*}\) sending bar v to the functional w mapped to
\(<w,v\)\textgreater{} is complex-linear and invertible. Its local metric coefficient
is positive.''',r'''specify their inverses. Choose a Hermitian metric \(h\), conjugate-linear
in its first argument and linear in its second. The actual map
\[
 \overline{N_-}\longrightarrow N_-^*,\qquad
 \bar v\longmapsto\bigl[w\longmapsto h(v,w)\bigr]
\]
is complex-linear: multiplying \(\bar v\) by \(c\) replaces \(v\) by
\(\bar c v\), and \(h(\bar c v,w)=c h(v,w)\).
It is invertible because the metric is positive definite on every
one-dimensional fibre. In a local frame \(e\) its coefficient is
the positive function \(h(e,e)\).''',
     'Type the Hermitian duality with the same conjugate-linear-first convention as K68, and prove its complex linearity and inverse fibrewise.'),
    (r'''Use Cox coordinates \((a0,a1,c0,c_{1})\) with auxiliary weights
\((1,1,-1,-1), z=a1/a0\) and native \(c_{i}^{chart}=a0 c_{i}\). The height is
\(q=a0 a1 c0 c_{1}\). Any actual torus coefficient arrow \((Z,V)\longmapsto (AZ,DV)\)
has the complete lift''',r'''Use Cox coordinates \((a_0,a_1,c_0,c_1)\) with auxiliary weights
\((1,1,-1,-1)\), \(z=a_1/a_0\) and native
\(c_i^{\rm chart}=a_0c_i\). On the first vertex of (IF3.4)
the actual Tate-coordinate identification is
\[
 (z,c_0^{\rm chart},c_1^{\rm chart})=(a,b,c),\qquad
 Z=b,\quad V=c,\quad q=abc.
\]
On the second vertex it is \(Z'=uv\), \(V'=uw\).
Substituting all three rows of (IF3.4) gives respectively
\[
 (Z',V')=(\kappa q Z,\alpha V),\qquad
 (Z',V')=(gZ,q\eta V),\qquad (Z',V')=(Z,V).
\]
These equations identify the full torus arrows with the native
charts, including every unit and height factor. Since
\(q=a_0a_1c_0c_1\), an actual coefficient arrow
\((Z,V)\mapsto(AZ,DV)\) has the complete Cox lift''',
     'Exhibit the exact Tate-to-native chart morphisms before applying the Cox lift; direct substitution verifies all three overlap rows.'),
    ('''The earlier scoped paragraphs remain complete stage records: a
local normal sum is used only after the later full reference,
cap and outer maps have closed that scope. In particular MC3's
symbol \\(\\kappa\\) remains unassigned until IC2; IVP supplies every
vertical integer before AFI uses it. No earlier scope statement
is used to omit a required boundary or cap argument.''',r'''The local normal sums enter the full reference, cap and outer
maps in the order displayed below. IC2 evaluates the bundle
\(\kappa=-56\) defined by MC3; IVP computes both vertical
integers before AFI transports them. Thus each local calculation
is used with its constructed boundary and cap comparison.''',
     'Replace the historical stage-summary paragraph by the completed dependency order without changing any local construction.'),
    (r'''The remaining work is the actual common selected-fan/chronological
source-strip/point-line attachment for SI3.7, its reference-relative
cap cochain and compact exterior, followed by the oriented return.
The source, line, root and branch maps above assign no such return.''',r'''The common selected-fan, chronological source-strip and point-line
attachment is constructed in SI3.7--9 and I3P below. MC3 supplies
its reference-relative cap map; ASI3 constructs the compact exterior
and its oriented parameter transfer. The present source maps are
the inputs to those explicit constructions.''',
     'Resolve the obsolete initial attachment notice by the actual complete supporting proofs.'),
    (r'''point-line comparison through the blowups. This section records
the source graph only; its completed normal determinant and the
moving cap have not yet been evaluated.''',r'''point-line comparison through the blowups. The complete normal
determinant of this source graph is computed in MS3; MC3 constructs
its moving cap, and IC2 evaluates the two actual second Chern terms.''',
     'Point the retained source graph to its completed normal determinant and cap calculation.'),
    (r'''unit arrow. A console-only Fraction serialization failure is preserved
under \path{records/attempts/e6_selected_i3_common_output_fraction}: it occurred
after all geometric assertions and the full JSON export. The corrected
complete execution exits successfully with empty stderr. The remaining
stage is the four-dimensional corner extension relative to the selected
boundary and its full finite source, Cartier and cap attachment; this
section assigns no return.''',r'''unit arrow. The four-dimensional corner extensions relative to
this selected boundary are SI3.9 and I3P. Their full finite source,
Cartier and cap attachments are the maps used by I3C, FSI, MC3
and ASI3 below. Historical execution attempts and the current
unchanged replay have separate records.''',
     'Move historical execution-stage prose to this reconciliation record and identify the complete four-dimensional attachment.'),
    (r'''units. Its earlier formatted JSON is preserved losslessly under
\path{records/attempts/e6_selected_i3_corner_pre_volume_export.} A separate
initial parenthesis typo and its failed execution are retained under
\path{records/attempts/e6_selected_i3_corner_syntax.} These two exact toric
lifts do not replace the remaining finite source/Cartier attachment
and cap-reference proof.''',r'''units. The finite source and Cartier attachment through these
two lifts is completed by I3P and the fixed-stratum proofs below.
MC3 retains the cap reference, and ASI3 gives the full outer transfer.
The historical formatting and execution attempts remain in the
source apparatus and receiving reconciliation record.''',
     'Keep the corner-lift certificate and exact subsequent attachment maps, while archiving superseded execution commentary.'),
    (r'''product P1 times D is exactly \(34(-1-2)=-102\). This relative number
does not yet use a reference cap.''',r'''product P1 times D is exactly \(34(-1-2)=-102\).
Its reference cap is constructed by the directed maps of MC3
and evaluated with this same tangent comparison in IC2.''',
     'Relate the local tangent number to the complete reference cap without changing that number.'),
    (r'''completed Hopf-cap map, the resulting closed E bundle and its second
Chern number, the remaining fixed components and the outer physical
return are still being evaluated. MS3.10 and the relative tangent
number are local geometric inputs to that subsequent construction.''',r'''completed Hopf-cap map and its closed bundle are constructed in
MC3, and IC2 computes their second Chern numbers. I3C and FSI
evaluate the other compact fixed components; ASI3 supplies the
outer physical transfer. MS3.10 and the relative tangent number
are the local geometric inputs to those constructions.''',
     'Replace the obsolete moving-star work notice by the completed Hopf-cap, fixed-stratum and outer-transfer dependencies.'),
    (r'''their 34 ordinary blowups remain those of MS3. No value for the
second Chern number of the completed normal bundle is chosen.
The calculation here supplies the moving-face term with the
full ordinary/root closing, before the outer return comparison.''',r'''their 34 ordinary blowups remain those of MS3. This constructs
the completed normal bundle and the moving-face term with the
full ordinary/root closing. IC2 calculates its second Chern
number from this actual clutch, and ASI3 carries the term through
the outer return comparison.''',
     'State the constructed bundle and its later exact evaluation instead of a pending-value notice.'),
    (r'''map. The equality is independent of the unassigned \(\mu _{j}\).
For a subsequent arbitrary nonvertical flop, the complete
free seed still retains that actual left coordinate. \(At
j=0\) it is -57-kappa by IF3.20, with nu0\(=48\). The moving-cap
rank-two clutch defining \(\kappa\) remains exactly MC3\textquotesingle s
specified bundle; no value is selected here.''',r'''map. The complete integer comparison of IVP gives
\(\mu_j=-1\) for every signed vertical fan. At \(j=0\),
IF3.20 gives \(-57-\kappa=-1\), because IC2 evaluates the
specific MC3 bundle as \(\kappa=-56\); its right coordinate
is \(\nu_0=48\). AFI uses these two actual free coordinates
for every subsequent nonvertical flop.''',
     'Insert the independently derived full integer seed and exact cap evaluation, retaining their explicit source maps.'),
    (r'''The root full AFI read and all28 independent path replays are
complete; the independent IVP gate is retained in the audit record.
Central registration is left to the parent integration.''',r'''The complete IVP line, tangent, collar and cap comparisons
establish the integer seed. The full target-prism equations and
their explicit finite fan words below then give every displayed
path sum and each of the twenty-eight witnesses.''',
     'Replace source-process commentary with the exact mathematical dependencies; current proof and replay events remain separate.'),
    ]
    for old,new,reason in edits:t=exact_replace(t,label,old,new,reason)
    t=t.replace('This working proof retains the original source','This proof retains the original source',1)
    return t

if r'\label{night:P3K.106}' in s:
    change('night:P3K.106',receive_k106,
           'Integrate the complete K106 proof with typed Hermitian and Tate/Cox maps and reconcile completed supporting stages; preserve all exact original sentences separately.')

def receive_k107(t):
    rec=json.loads((W/'analysis/IV_K107/receiving_replacements.json').read_text())
    for e in rec['corrections']:
        t=exact_replace(t,e['label'],e['exact_old'],e['exact_new'],e['reason'])
    return t

if r'\label{night:P3K.107}' in s:
    change('night:P3K.107',receive_k107,
           'Apply the independently verified full theta-derivative coefficient and explicit M2 ordered-source interval to its (2,3) F41 sphere reference.')

if r'\label{night:P3K.106}' in s and r'\label{night:P3K.107}' in s:
    def narrow_k75(t):
        old=r'''all-fan formulas. The \(M_2\) order-three base return,
both selected-I3 generators and their remaining cap/norm/fan
scopes, and the additional singular-site/endpoint scopes
still require their full comparison maps. The working notes assign no
return to an unfinished attachment. Part 3.4 remains incomplete.'''
        new=r'''all-fan formulas.

\cref{night:P3K.106} completes the selected-I3 original source
loop for \(M_6\), translation by \(-G\), the quadratic cap
\((m,n)=(2,1)\), its retained finite character and full annular
reference. Its explicit marked-source reflection carries the
opposite selected branch with the corresponding reflected fan.
The initial physical pair is \((47,-4)\), and the signed vertical
pair is \((47-2j^3+18j^2-52j,-4)\). The full native coefficient
maps and target-prism systems compute every basis fan and realize
all twenty-eight classes through actual words of length at most
seven from the initial fan. The broader selected-I3 cap and norm
scopes are not established by this quadratic theorem.

\cref{night:P3K.107} completes the original \(M_2\) order-three
source loop with translation by \(-3G\), every good cap
\(m=3l\), \(l\geq1\), either primitive norm sign, and each
admitted finite character and complete annular reference.
For each selected cap the original scalar is chosen in its common
strict contraction range with the specified good reference cap.
The initial and all vertical physical pairs are \((-3,-12)\),
with native pair \((-3,0)\) and integer zero. Its full directed
fan maps give
\[
 A(P)=-\frac38(S-1)(S-3),\qquad
 S=x^2+xy+y^2,\quad (x,y)^t=P^{-1}(0,1)^t,
\]
and precisely the sixteen residues proved there.

The remaining marked source-moduli, selected-I3 cap/norm and
additional singular-site/endpoint scopes outside these stated
constructions still require their full comparison maps. This
remaining attachment problem is open; the two new complete
calculations do not assign a return to an unfinished attachment.'''
        t=exact_replace(t,'night:P3K.75',old,new,
                        'Narrow the open obligations only by the exact fully reviewed K106 and K107 domains, preserving the residual open scope.')
        t=t.replace('P3K.76--105 cited in the statement.','P3K.76--107 cited in the statement.',1)
        t=t.replace('P3K.92--105 are new complete proofs.','The receiving additions P3K.106--107 have separate current whole-proof records and complete supporting texts.',1)
        return t
    change('night:P3K.75',narrow_k75,
           'Record the precise quadratic selected-I3 and full good-cap M2 order-three closures; preserve Open status and all residual comparison obligations.')

if r'\label{iv:i3_all_reduced_caps}' in s:
    def narrow_icap(t):
        old=r'''The broader selected-I3 cap and norm
scopes are not established by this quadratic theorem.'''
        new=r'''\cref{iv:i3_all_reduced_caps} constructs the complete
selected-height ratio, invariant norm root, signed annular cochains
and proper cap products that carry these two integers separately
to every \(M_6\) reduced cap \(m=3l+2\), both primitive norm
signs and every admitted finite character and prescribed reference.
For each cap and its quadratic reference, the scalar lies in their
common strict contraction range. The unchanged selected tube retains
every native fan map, so the entire K106 integer algorithm and its
twenty-eight-class image apply throughout this full progression,
including the explicitly reflected second branch.'''
        t=exact_replace(t,'night:P3K.75',old,new,
             'Close the full M6 selected-I3 reduced-cap progression by the actual ICAP comparison, retaining each cap/reference scalar domain.')
        t=t.replace('The remaining marked source-moduli, selected-I3 cap/norm and',
                    'The remaining marked source-moduli, other selected-I3 point-line/cap data, and',1)
        return t
    change('night:P3K.75',narrow_icap,
           'Remove precisely the full M6 selected-I3 reduced-cap and signed-norm obligations established by the complete ICAP theorem; preserve all remaining Open scopes.')

for lab,uses in {
 'night:P3K.49':r'\cref{night:P3K.41}, only its retained CP.1--4 product, collar and source-cusp maps; no rejected global conclusion is used',
 'night:P3K.51':r'\cref{night:P3K.50}, only OR.2--3 and the actual ordinary-product \(V_{00}\) input; no rejected global conclusion is used',
 'night:P3K.106':r'\cref{night:P3F.35,night:P3F.41,night:P3K.62,night:P3K.68,night:P3K.89,night:P3K.94,night:P3K.95,night:P3K.96,night:P3K.97,night:P3K.98}; the retained local quaternion, prism and native-reset constructions of \cref{night:P3K.23,night:P3K.29,night:P3K.31}; IE.4--5 and local IE.7 of \cref{night:P3K.57}, transported through \cref{night:P3K.68}; BW.2 of \cref{night:P3K.76}; the complete SI3--AFI supporting proofs below',
 'night:P3K.107':r'\cref{night:P3F.41,night:P3K.68,night:P3K.95,night:P3K.96,night:P3K.103}; the retained local quaternion, prism and frame maps of \cref{night:P3K.23,night:P3K.29,night:P3K.31}; OR.2 of \cref{night:P3K.50}, CT.3 of \cref{night:P3K.51}, ST.1 of \cref{night:P3K.52}, GF.2--4 of \cref{night:P3K.55}; only IE.4--5 and local IE.7 of \cref{night:P3K.57} through the exact physical duality of \cref{night:P3K.68}; the complete E64--MFA proofs below',
 'night:P3K.75':r'\cref{night:P3K.106,night:P3K.107} in precisely the cap, norm, parameter and fan scopes stated here; the earlier completed reductions retained in the statement'
}.items():
    if r'\label{'+lab+'}' in s:
        change(lab,lambda t,u=uses:add_uses(t,u),
               'State the exact current operative dependencies, with retained local scopes separated from their historically refuted compound claims.')
if r'\label{iv:i3_all_reduced_caps}' in s:
    change('night:P3K.75',lambda t:add_uses(t,r'\cref{iv:i3_all_reduced_caps} with the complete original M6 source, signed meridian and proper relative cap maps'),
           'Add the fully proved all-reduced-cap ICAP theorem to the precise remaining-obligations dependency record.')

(W/'analysis/IV/checkpoint29_receiving_reconciliation.json').write_text(json.dumps(cp29_edits,indent=2)+'\n')
