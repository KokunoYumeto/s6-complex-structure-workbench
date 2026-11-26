from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix = 'S6_SERIES_PUBLISH_sec07_weighted_sphere'
path = OUT / (prefix + '_defects.tsv')
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    row['review_status'] = ('Complete old/current A.5.15 and P247 proofs, all named conic consumers, '
                            'and all receiving P297/P296/A.5.15 proofs read and compared. '
                            'All five bounded guards replay once; every old label and target '
                            'has unchanged multiplicity. Root admission pending.')
    if row['type'] == 'D25':
        row['review_status'] += (' The exact P296 weighted model is proved. The factor-preserving '
                                 'deformation premise for the unchanged broad P4R.14/P4R.15/'
                                 'P4.41/P4.45 consumers remains OPEN; their domains are preserved.')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

with (ROOT / 'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields = next(csv.reader(f, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
data = [
    ('curve', 'lem:II:monomial-curve-matching-sphere',
     'Read the complete original/current A.5.15 arc and intersection construction and the complete P247 proof, '
     'then the whole receiving P297 statement and proof. The coordinate chart at a simple zero is '
     '(y,z)→(chi(y^bprime z^cprime),y,z), with projection inverse. The continuous collapsed-circle map, '
     'coprime primitive slope, parallel-arc homotopy and compact supports remain. The endpoint links have '
     'slope (cprime,−bprime), linking −bprime cprime, and both orientation reversals at the second endpoint '
     'preserve that sign. P247 is the bprime=cprime=1 clause, retaining its X_B notation, both explicit '
     'maps over v≠0, smooth endpoint disk, projection inverse and determinant −((a−1)^2+b^2). '
     'The original A.J.33a/A.J.33b/A.BP.3 labels and permanent targets occur once at this owner.'),
    ('binomial', 'cdp:st:A.5.15',
     'Read the complete old/current and receiving A.5.15 proof. Its exact curve B={x^a−v^d=1}, '
     'd=gcd(b,c), remains smooth and connected with a≥2 simple zeros of v. The identity on (x,y,z) '
     'identifies H with X_(B;b/d,c/d), since (y^(b/d)z^(c/d))^d=y^b z^c. Only the common arc/framing '
     'proof is replaced by P297. The weighted homothety, the full original map u h^m, its explicit '
     'unit-coordinate change and implicit inverse, the global torus inclusion, the compact intersection '
     'argument and the complete mixed-normalization/conductor/differential calculation all remain. '
     'The dependency record now names P297; the binomial proposition and its P4.18 alias retain every conclusion.'),
    ('conic-consumers', 'lem:II:conic-bundle-matching-sphere',
     'Read the full current A.5.21, P230 and P4.25 statements and proofs, including their later deformation '
     'and normalization arguments. Each P247 application uses precisely its bprime=cprime=1 clause. '
     'A.5.21 uses B={P(x,v)=1} and the coordinate identity to P(x,yz)=1; its connected cyclic-cover '
     'and simple-zero hypotheses remain. P230 uses v=x−y and '
     'Z=y(y+v)z+y^2(2y+v), with the displayed inverse on xy≠0, to obtain vZ+y^4=1; '
     'its chosen arc avoids y=0 and its circle support obeys |v|<|y|/2. '
     'P4.25 uses U1=x−iyz=t^bprime and U2=x+iyz=t^(−aprime), with its Bezout inverse, '
     'and the corresponding curve B in (x,v). Thus every consumer retains the same curve, same X_B '
     'and smoothly embedded square −2 sphere; no consumer domain or later proof step changes.'),
    ('weighted-model', 'prop:II:weighted-two-branch-sphere',
     'Read the complete new P296 statement and proof and directly followed both inverse compositions. '
     'For G=(X−Y^k Z^l)^a(X+Y^k Z^l)^b, primitive a0,b0 and Bezout integers b0 r−a0 t=1 '
     'give s=(X−Y^k Z^l)^r(X+Y^k Z^l)^t and the inverse Theta; the identities hold also at Y=Z=0. '
     'The root curve v^e=(s^(−a0)−s^b0)/2 is smooth, connected by full-cycle monodromy around a '
     'simple zero, and has N=a0+b0≥2 simple zeros of v. The identity surface map and P297 give '
     'square −2(k/e)(l/e). Weighted homothety and the displayed implicit inverse for the unit '
     'coordinate change embed the compact supports in the original uG-level with the original a,b. '
     'Asphericity of the torus contradicts the preserved nonzero intersection. This proves that exact '
     'model; no factor-preserving deformation of another full function is asserted. The original '
     'P4R.14/P4R.15/P4.41/P4.45 domains and their OPEN transport premise are retained.')
]
events = []
for suffix, owner, outcome in data:
    event = dict.fromkeys(event_fields, '')
    event.update(
        statement_id=owner, date=now[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
        type='used and rechecked in this run',
        outcome=outcome + (' This is exposed reading and rechecking of the retained internal proofs; '
                           'no independent-check credit, required-check increment, integrated compilation '
                           'or final rendered-page reading is claimed.'),
        event_id='publish:c3:foundations:sec07:weighted-sphere:' + suffix,
        phase='publication weighted full-fibre sphere consolidation',
        source_file=str(path.relative_to(ROOT)), source_event_type='used and rechecked in this run',
        evidence_group='publish:c3:foundations:sec07:weighted-sphere', date_utc=now,
        where='P297 before A.5.15; P247 specialization alias there; P296 after A.5.15; bounded A.5.15 application')
    events.append(event)
with (OUT / (prefix + '_CHECK_EVENTS.tsv')).open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)

lines = [
    '# Bounded weighted full-fibre sphere package', '',
    'Scope: one common curve-input owner P297 before A.5.15, retaining P247 as its embedded conic clause; '
    'the exact binomial application; and the proved weighted two-branch model P296 after A.5.15. '
    'The complete old/current and receiving proofs and all named conic consumer proofs were read. '
    'These are bounded statement transfers inside existing units, with no subsection or movement credit.', '',
    '| Class | Bounded status | Reason |', '|---|---|---|'
]
for kind in [f'D{i:02}' for i in range(1, 26)] + ['restructuring']:
    state = 'done'
    reason = ('Complete bounded receiving text read for this class; no additional instance in this package. '
              'The enclosing contracted-boundary subsection remains open.')
    if kind == 'D10':
        reason = 'P297 and P296 are numbered proved owners with complete inputs; P247 remains an explicit specialization alias; A.5.15 records its exact earlier input.'
    if kind == 'D12':
        reason = 'The shared arc, collapsed-circle, compact-homotopy and framing proof occurs once. A.5.15 applies it through the identity map; the P247 smooth endpoint argument remains as its precise specialization.'
    if kind == 'D14':
        reason = 'Bounded dependency order is P297, A.5.15, P296, before all their named consumers. All earlier labels and targets survive once; integrated whole-paper placement remains with root.'
    if kind == 'D16':
        reason = 'All old hypotheses, stronger embedded-sphere conclusion, two explicit endpoint comparisons, formula targets and consumer maps remain. The original full multiplicities in P296 are never replaced by a common power.'
    if kind in ['D17', 'D18']:
        reason = 'No known proof is replaced by an unverified external citation. The complete internal construction and the exact consumer maps are retained at their single owner.'
    if kind == 'D19':
        reason = 'A.J.33a, A.J.33b and A.BP.3 keep their exact labels, permanent targets and section equation numbering at P297; the map records every transferred formula.'
    if kind == 'D23':
        state = 'open'
        reason = 'Source equations, inverse maps and alias positions are read. Integrated compilation and final rendered-page reading remain with root.'
    if kind == 'D25':
        state = 'open'
        reason = 'P297/P296 and the exact binomial/conic applications are proved. The four broad-domain rigidity consumers still require factor-preserving deformation of their original full functions; no conditional replacement, narrowing or refutation is claimed.'
    if kind in ['D24', 'restructuring']:
        state = 'open'
        reason = 'This bounded single-owner order is complete; root admission and the whole contracted-boundary subsection pass remain. No unit row is closed by relocating statements.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT / (prefix + '_status.md')).write_text('\n'.join(lines) + '\n', newline='\n')

comparison = r'''# Exact sphere-owner and consumer comparison

| Old owner or consumer | Receiving data and exact map | Preserved conclusion |
|---|---|---|
| A.5.15, general arc construction | `B={x^a−v^d=1}`, `d=gcd(b,c)`, exponents `(b/d,c/d)`; identity on `(x,y,z)` because `(y^(b/d)z^(c/d))^d=y^b z^c`. | Same continuous spherical cycle, compact parallel homotopy and square `−2(b/d)(c/d)`; A.J.33a/b retained at P297. |
| P247 | `X_B=X_(B;1,1)`; same coordinates, with `(b,y)↦(x(b),y,v(b)/y)` and inverse `(x,y,z)↦((x,yz),y)`. | Same smoothly embedded sphere, endpoint disks and determinant `−((a−1)^2+b^2)`; P247 and A.BP.3 retained at P297. |
| A.5.21 | Its curve `P(x,v)=1` and coordinate identity to `P(x,yz)=1`. | Embedded square `−2` sphere; complete variable-coefficient remainder retained unchanged. |
| P230 | Its displayed invertible chart gives `vZ+y^4=1`; the matching arc and support remain within `xy≠0`. | Embedded square `−2` sphere, full homothety and unit comparison unchanged. |
| P4.25 | The existing primitive-exponent parametrization of `U1^a U2^b=1`, with its Bezout inverse, gives the same curve in `(x,v)` and same `X_B`. | Embedded square `−2` sphere; the later conductor, deformation and normalization steps remain unchanged. |
| New P296 | `s↦(s^b0,s^(−a0))`, inverse `s=U1^r U2^t`, `b0r−a0t=1`; then `v^e=ψ(s)` and the identity on `(s,Y,Z)`. | Compact spherical square `−2(k/e)(l/e)` in the full weighted fibre, including the endpoints where `Y=Z=0`. |

## Full-function comparison in P296

For `G=(X−Y^kZ^l)^a(X+Y^kZ^l)^b`, let `D=(k+l)(a+b)`. The homothety is

`δλ(X,Y,Z)=(λ^(k+l)X,λY,λZ)`, with `G∘δλ=λ^D G` and inverse `δ_(1/λ)`.

For a unit `u`, the coordinate change is

`Φ=(u^(1/(a+b))X,u^(1/D)Y,u^(1/D)Z)`, so `G∘Φ=uG`.

Writing `v=u^(1/D)`, the displayed implicit equation defines `τ` with `τ(0)=v(0)` and nonzero derivative `D v(0)^(D−1)`. The inverse is `Ψ=(τ^(−k−l)X′,τ^(−1)Y′,τ^(−1)Z′)`. Both inverse identities follow from uniqueness of the selected root. Thus `Ψ∘δλ∘Θ` places the entire compact cycle and its intersection comparison in the original full map, with its original `a,b`.

## Remaining consumer gate

P4R.14, P4R.15, P4.41 and P4.45 retain their original broad standing hypotheses. P296 settles the exact two-branch monomial model for every pair of positive component multiplicities. A deformation of their original full functions into that model must preserve each analytic factor and its multiplicity and satisfy the earlier P295 boundary comparison. That further premise remains open; this package neither changes those statements nor substitutes a common-power hypothesis.

The full old/current and receiving proofs have been read. Five bounded guards replay once and preserve every old label and permanent target. The two new tags are P296 and P297; P247 is an alias, not a new tag. No shared manuscript or central table is written by this package.
'''
(OUT / (prefix + '_comparison.md')).write_text(comparison, newline='\n')
print(f'{len(rows)} defect rows; {len(events)} exposed-reading events; P296/P297 allocated; four consumer transport gates remain OPEN.')
