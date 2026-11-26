from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix = 'S6_SERIES_PUBLISH_sec07_nodal_hessian'
path = OUT / (prefix + '_defects.tsv')
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
for row in rows:
    row['review_status'] = ('Complete old/current and receiving P4.41 proofs read and compared, '
                            'including all unchanged defect estimates and normalization matrices. '
                            'The normalization multiplier algebra, full-function coordinate maps '
                            'and rescaled critical-point inverse were followed directly. The one '
                            'bounded guard replays once and preserves all old labels/targets. '
                            'Numbered equations have no blank paragraphs. Root admission pending.')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
with (ROOT / 'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields = next(csv.reader(f, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
data = [
    ('conductor-factor-algebra',
     'Read the complete old/current and receiving P4.41 proofs. In q=1,A(0) unit,g_z(0)≠0, '
     'the exact ambient Hessian 2A(0)dg(0)⊗dg(0) meets R15 at the unchanged original full-fibre '
     'domain and contradicts the entire nodal critical curve. In g_z(0)=0, the displayed square '
     'completion gives G=√A g+B z²/(2√A), f=G²+D z⁴ and the same conductor I=(G,z²). '
     'Read the entire current P222 proof and applied its multiplier identification and Gorenstein '
     'biduality to this reduced hypersurface. With t=G/z², every conductor-dual multiplier '
     'theta satisfies theta z²=r,theta G=s; the lifted relation gives r−vG∈(z²), hence '
     'theta=v t+w. Therefore normalization is exactly R+Rt,t²=−D. Its fibre algebra proves '
     'local irreducibility when D(0)=0 and exactly two local irreducible factors G±z²√(−D) '
     'when D(0)≠0. Thus the full multiplicity split is established before any deformation.'),
    ('exact-root-and-weighted-families',
     'Read and followed every new coordinate map. In the proved locally irreducible case, '
     'the full root f0=V^(1/M)f has exact G0,D0 factors. The D0+delta deformation, fourth-root '
     'coordinate with implicit inverse, and parameter Morse map give the retained '
     '(XY+a(Z)−epsilon)²+Z⁴ model. Its critical value epsilon², XY entry−2epsilon and '
     'ZZ entry−2epsilon a″(0) are retained verbatim at their established full-root scope. '
     'In the two-factor case, Z=z(−D)^(1/4) and the same plane Morse maps give '
     'U[XY+A(Z)−Z²]^a[XY+A(Z)+Z²]^b with the original U,a,b. The deformation changes '
     'A to A+alpha Z² and shifts both factors by−epsilon, preserving their analytic factor '
     'families and full powers. At (X,Y,Z)=epsilon r, the logarithmic gradient extends '
     'holomorphically, has the stated unique zero at epsilon0 and derivative matrix '
     '[[0,−N,0],[−N,0,0],[0,0,−2T]], determinant2N²T≠0. The implicit r(epsilon) '
     'gives a full critical point with nonzero value, and the exact Hessian identity '
     'HessF=(F/epsilon)D_rL proves it is Morse while retaining the unit.'),
    ('boundary-and-remaining-proof',
     'Read the complete receiving boundary comparison and all remaining q=1/q=0/equality '
     'proof steps. The root construction uses nested balls with the first delta family, then '
     'the alpha/epsilon family, and ends in the original F=b^M. The unequal-power family '
     'uses v=XY+A_alpha(Z)−epsilon and Z at each intersection link; the P298 k=2 weighted '
     'unit map and inverse give fixed full transverse factors, while smooth component strata '
     'have normal-coordinate powers. Thus P295 applies with m=1 to the full function. '
     'The Morse sphere has its preserved square in the original torus. All subsequent '
     'branchwise d_i,b_i,q estimates, lower bounds5 or9/2, equality orders, exact generator '
     'coordinate change, Hilbert–Burch and extension matrices, six minors, membership '
     'conditions, retained x²/x⁴ factors, and finite birational map (x,u)→(x,−u²,x²u) '
     'are read and retained. The final equality normalization conclusion is unchanged.'),
    ('local-input-scope',
     'Read the complete present R10 statement and proof to compare its local inputs used '
     'by P4.41: conormal pullback K, ramification R, saturated Hessian line, zero orders d_p, '
     'projected conormal colength b_p and additional descent length q_p. P4.41 defines their '
     'two-branch local instances through its actual normalized nodal module; it does not '
     'invoke R10’s global irreducible/unibranch elliptic conclusion. Read the full P222 '
     'statement/proof at the same time; the only extra use is the exact conductor multiplier '
     'and biduality identification described above. R15/P298/P295 are their already proved '
     'full-function owners, with the explicitly matched functions and original component powers.')
]
events = []
for suffix, outcome in data:
    event = dict.fromkeys(event_fields, '')
    event.update(statement_id='night:P4.41', date=now[:10],
                 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                 type='used and rechecked in this run',
                 outcome=outcome + (' Exposed reading and direct rechecking only. No independent '
                                     'check credit, required-check increment, integrated compilation '
                                     'or final rendered-page reading is claimed. P4.45 remains OPEN '
                                     'pending its separate exact factor-lift comparison.'),
                 event_id='publish:c3:foundations:sec07:nodal-hessian:' + suffix,
                 phase='publication full-multiplicity nodal Hessian proof',
                 source_file=str(path.relative_to(ROOT)), source_event_type='used and rechecked in this run',
                 evidence_group='publish:c3:foundations:sec07:nodal-hessian', date_utc=now,
                 where='Complete P4.41 replacement; same statement, defect inequality and equality normalization')
    events.append(event)
with (OUT / (prefix + '_CHECK_EVENTS.tsv')).open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)

lines = ['# Bounded full-multiplicity nodal Hessian proof', '',
         'Complete original/current and receiving P4.41 proofs are read. Its broad statement, '
         'inequality and equality normalization remain, and the full-multiplicity deformation '
         'premise is established through its actual conductor algebra. P4.45 remains open. '
         'No subsection completion or movement credit is claimed.', '',
         '| Class | Bounded status | Reason |', '|---|---|---|']
for kind in [f'D{i:02}' for i in range(1, 26)] + ['restructuring']:
    state = 'done'
    reason = 'The complete bounded receiving text is read for this class; no additional instance in this owner.'
    if kind == 'D10':
        reason = 'The same numbered owner and statement persist; the actual conductor algebra and full-map data justify each case before its deformation.'
    if kind == 'D12':
        reason = 'R15, P222, A.5.17, P298 and P295 are used through exact local objects and maps; the original scalar Hessian formulas remain in their proved root specialization.'
    if kind == 'D14':
        reason = 'Every input owner precedes P4.41. The local definitions from R10 are explicitly distinguished from its global conclusion by their own exact module data.'
    if kind == 'D16':
        reason = 'The original broad domain, 9/2 bound, stronger casewise5 bounds, equality orders, all matrices and the full smooth-normalization conclusion remain.'
    if kind in ['D17', 'D18']:
        reason = 'The de Jong–van Straten exact source locator and matrix calculation are retained. New uses apply complete earlier internal proofs through the written multiplier and function maps.'
    if kind == 'D19':
        reason = '4.41a–e retain every formula under their prepared eq:II:manual:4.41a–e labels and section numbering; the old-tag map accompanies the package.'
    if kind == 'D23':
        state = 'open'
        reason = 'Complete source and inverse maps are read; the article and all converted math whitespace are corrected. Integrated compilation and final pages remain with root.'
    if kind == 'D25':
        reason = 'P4.41’s full-multiplicity premise is proved at its original domain. No closure is claimed for the separate P4.45 factor-lift problem.'
    if kind in ['D24', 'restructuring']:
        state = 'open'
        reason = 'The bounded proof and input order are complete; root admission and the enclosing subsection pass remain. No movement credit is claimed.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT / (prefix + '_status.md')).write_text('\n'.join(lines) + '\n', newline='\n')

comparison = r'''# P4.41 exact full-function comparison

| Original case | Established algebra or map | Full-function application |
|---|---|---|
| `A(0)≠0,g_z(0)≠0` | `Hess f=2A(0)dg(0)⊗dg(0)` is nonzero. | R15 applies to the original full fibre and contradicts the entire nodal critical curve. |
| `A(0)≠0,g_z(0)=0` | `G=√A g+Bz²/(2√A)`, `D=C−B²/(4A)`, `I=(G,z²)`, `f=G²+Dz⁴`. | The actual conductor is unchanged. |
| Exact normalization | `t=G/z²`; every dual multiplier is `v t+w` by the lifted syzygy. | `normalization=R+Rt`, `t²=−D`, as the same algebra in the total quotient ring. |
| `D(0)=0` | The fibre algebra has one maximal ideal; normalization is local normal and a domain. | The support is locally irreducible, so `F=Vf^M` has the exact root `f0=V^(1/M)f`. |
| `D(0)≠0` | The two coprime factors are `G±z²√(−D)`, and the fibre algebra bounds their number by two. | These are exactly the two local irreducible factors with their original positive powers `a,b`. |
| Root deformation | Fourth-root coordinate and parameter Morse maps give `(XY+a(Z)−epsilon)²+Z⁴`. | Original critical value and Hessian entries remain; nested P295 maps end in `F=b^M`. |
| Unequal-power deformation | Keep `U[XY+A_alpha(Z)−Z²−epsilon]^a[XY+A_alpha(Z)+Z²−epsilon]^b`. | Both factor families, their original powers and the unit are retained. |
| Full Morse point | `p_epsilon=epsilon r(epsilon)` is the implicit zero of the rescaled logarithmic gradient. Its limiting derivative has determinant `2N²T≠0`. | Exact Hessian `HessF=(F/epsilon)D_r L` is invertible at a nonzero full critical value. |
| Boundary comparison | `v=XY+A_alpha(Z)−epsilon`, `Z`, complementary tangent coordinate, then P298’s `k=2` weighted unit map and inverse. | P295 applies to the full family with `m=1`, including smooth component strata. |

All original matrices, branchwise defect computations, casewise bounds and the finite birational equality-normalization map remain. The complete old/current and receiving proofs, and the full current P222/R10 input proofs, were read. One bounded guard preserves all old labels and targets; five equations receive their prepared labels and no equation contains a blank paragraph. No new tag is allocated. P4.45 remains open with the provenance agent working on the precise factor lift.
'''
(OUT / (prefix + '_comparison.md')).write_text(comparison, newline='\n')
print(f'{len(rows)} defect rows; {len(events)} exposed-reading events; P4.41 full-multiplicity premise resolved; P4.45 remains OPEN.')
