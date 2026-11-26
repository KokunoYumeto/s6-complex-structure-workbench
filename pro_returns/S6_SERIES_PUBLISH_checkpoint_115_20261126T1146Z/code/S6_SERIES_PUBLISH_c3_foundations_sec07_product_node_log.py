from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix = 'S6_SERIES_PUBLISH_sec07_product_node'
path = OUT / (prefix + '_defects.tsv')
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
for row in rows:
    row['review_status'] = ('Complete original/current and receiving UN9/P299 and the complete current '
                            'and receiving R14 proof read and compared. Four bounded guards replay '
                            'once; all old labels/targets remain. The only R14 proof transfer is '
                            'its exact finite-free intersection argument; its full weighted polar '
                            'proof and repaired equation whitespace are retained. Root admission pending.')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
with (ROOT / 'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields = next(csv.reader(f, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
data = [
    ('intersection', 'lem:II:smooth-curve-intersection',
     'Read the complete receiving P299 and the complete old/current R14 intersection proof. '
     'The identical local quotient C{x,y,z}/(phi,psi) is finite over C{z}, a one-dimensional '
     'complete intersection, and torsionfree over the discrete valuation ring, hence free '
     'with generic transverse rank r. For r1, the special plane ideal has length1 and equals '
     '(x,y), giving the invertible map (phi,psi,z) and its stated implicit inverse. For r2, '
     'length2 forces one smooth factor; its restricted other factor is a unit times y², '
     'and the exact parameter Morse map gives phi=X,psi=Y²+XH while keeping z. '
     'All rank-two conclusions formerly proved in R14 remain at this earlier single owner.'),
    ('node', 'cdp:st:C.2.UN.9',
     'Read the full original/current and receiving UN9 statement and proof. The printed broad '
     'scope is retained. Two local factors share the entire smooth axis and have generic '
     'intersection multiplicity1; P299 gives their independent coordinates, and X=V phi '
     'with its implicit inverse gives the exact original reduced generator XY for arbitrary '
     'original positive component powers. In the locally irreducible case, the full root '
     'f0=U^(1/M)f is established before perturbation. The original constant symmetric '
     'matrix construction, nonzero trace condition, E=R−Q(z0), simple determinant zero, '
     'parameter Morse coordinate and Z=h(y,z) are all retained. Z→−Z is the explicit '
     'map to the (2,2,1) binomial, whose spherical square is−4. The fixed product-node '
     'boundary charts and original F=f0^M meet P295 exactly; its target path, parameter '
     'transport and final inclusion reach F=b^M. The original common-power conclusion '
     'and original reduced-generator unit map are retained.'),
    ('r14-application', 'night:P4R.14',
     'Read the entire current and receiving R14 proof. Its rank-two application uses the '
     'same phi,psi and z as P299. The complete subsequent determinant identity '
     'Delta=−(alpha delta−beta gamma)², the root-only discriminant perturbation, exact '
     'reduced factorization, full unit absorption, positive-coefficient weighted polar '
     'argument, full Hessian, all old unweighted formulas, weighted boundary inverse '
     'and positive-genus six-root example remain unchanged. The earlier root correction '
     'of whitespace inside the final two equations is preserved. Its dependency record '
     'adds P299 without removing an existing input or changing the statement.')
]
events = []
for suffix, owner, outcome in data:
    event = dict.fromkeys(event_fields, '')
    event.update(statement_id=owner, date=now[:10],
                 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                 type='used and rechecked in this run',
                 outcome=outcome + (' Exposed reading and direct rechecking only; no independent '
                                     'check credit, required-check increment, integrated compilation '
                                     'or final rendered-page reading is claimed.'),
                 event_id='publish:c3:foundations:sec07:product-node:' + suffix,
                 phase='publication full-multiplicity product-node proof',
                 source_file=str(path.relative_to(ROOT)), source_event_type='used and rechecked in this run',
                 evidence_group='publish:c3:foundations:sec07:product-node', date_utc=now,
                 where='P299 before P298; R14 exact rank-two application; complete UN9 replacement')
    events.append(event)
with (OUT / (prefix + '_CHECK_EVENTS.tsv')).open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)

lines = ['# Bounded product-node proof and common intersection owner', '',
         'The full original/current and receiving proofs have been read. UN9 is proved at its '
         'original broad scope with the original full multiplicities. P299 owns the exact '
         'intersection algebra used by UN9 and R14. This is prerequisite work for the '
         'contracted-boundary subsection; no whole-unit or movement credit is claimed.', '',
         '| Class | Bounded status | Reason |', '|---|---|---|']
for kind in [f'D{i:02}' for i in range(1, 26)] + ['restructuring']:
    state = 'done'
    reason = 'Complete bounded receiving text read for this class; no further instance in this package.'
    if kind == 'D10': reason = 'P299 is a numbered proved owner, and both exact consumers record it as an earlier input.'
    if kind == 'D12': reason = 'One finite-free intersection proof serves r1 and r2; P295 owns the complete boundary transport, and the node proof gives its exact charts and full root.'
    if kind == 'D14': reason = 'P299 follows P295 and precedes P298, R14 and UN9; every construction used by UN9 is earlier.'
    if kind == 'D16': reason = 'The original broad node conclusion, all matrix formulas and square−4 class persist. Every R14 full-multiplicity conclusion and formula remains.'
    if kind in ['D17', 'D18']: reason = 'Complete internal proofs are transferred or applied through explicit maps; no new unverified external citation replaces a proof.'
    if kind == 'D19': reason = 'C.UNNODE.1–3 retain their exact formula payloads, labels and permanent targets with section numbering. R14 equation aliases and corrected whitespace are untouched.'
    if kind == 'D23':
        state = 'open'; reason = 'Complete source read and math whitespace checks are done; integrated compilation and final rendered pages remain with root.'
    if kind == 'D25': reason = 'The full-fibre scope gap in UN9 is resolved through the rank-one two-factor map and the established full root in the irreducible case, without narrowing the statement.'
    if kind in ['D24', 'restructuring']:
        state = 'open'; reason = 'This bounded owner/application order is complete; root admission and the contracted-boundary subsection pass remain. No unit closes through relocation.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT / (prefix + '_status.md')).write_text('\n'.join(lines)+'\n', newline='\n')

comparison = r'''# Product-node and intersection comparison

| Input | Exact common owner or map | Preserved output |
|---|---|---|
| R14 two factors | P299 on the same `(phi,psi,z)`, with generic rank2. | One smooth factor, same special-fibre length2 and full quartic determinant comparison. |
| UN9 two factors | P299 with rank1; inverse of `(phi,psi,z)`, then inverse of `X=V(phi,psi,z)phi`. | Exact original reduced generator `XY`, allowing the original unequal positive component powers. |
| UN9 locally irreducible | `f0=U^(1/M)f`, exact `F=f0^M`; same critical axis. | The full root is established before the retained symmetric-matrix perturbation. |
| Node matrix degeneration | `E=R−Q(z0)`, nonzero trace of `adj(R)Q′(z0)`, then the parameter Morse map and `Z=h(y,z)`. | Same simple determinant zero and exact binomial `X²+y²Z`. |
| Binomial and transport | `Z→−Z` identifies `(2,2,1)`; fixed product charts and P295 with `F=f0^M`. | Same compact spherical square−4 class in the original full fibre `F=b^M`. |

Four guards replay once and preserve every existing label and target. The complete receiving R14 proof has been read after the bounded transfer, including its full polar argument and root’s repaired equation whitespace. New tag P299; P300 remains unused by this agent. No shared manuscript or central table is written.
'''
(OUT / (prefix + '_comparison.md')).write_text(comparison, newline='\n')
print(f'{len(rows)} defect rows; {len(events)} exposed-reading events; P299 allocated; UN9 original full-multiplicity scope resolved.')
