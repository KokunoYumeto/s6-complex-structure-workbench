from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix = 'S6_SERIES_PUBLISH_sec07_smooth_contact'
path = OUT / (prefix + '_defects.tsv')
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
for row in rows:
    row['review_status'] = ('Complete old/current and receiving R15/A.5.17 proofs and the complete P298 '
                            'proof read. Exact inverse compositions, full critical equations and Schur '
                            'complement followed directly. All three bounded guards replay once and '
                            'all old label/target multiplicities are preserved. Root admission pending.')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
with (ROOT / 'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields = next(csv.reader(f, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
data = [
    ('full-contact', 'prop:II:smooth-branch-contact',
     'Read all receiving P298. The full family is U(X−H_s)^a(X+H_s)^b with the original U,a,b. '
     'Boundary charts at smooth component strata give w^a or w^b; at an intersection link, '
     'y=nu_s^(1/k)h_s and the weighted unit-coordinate map give the fixed full transverse polynomial, '
     'with the displayed implicit inverse, a transverse tangent coordinate, and only critical value zero. '
     'P295 applies to g_s=F_s with m=1. For multiple factors the exact finite-degree shift and coordinate '
     'map give the P296 model. For a singular single factor, the equation for C has derivative N and '
     'c0=(b−a)/N; Lambda=qW^(1/N) and R have the stated two inverse identities. '
     'H_s=R(h_tilde_s^k,Y,Z) is the original H at s=0 and preserves its exponent k. '
     'The exact critical-centre identity is F_s(A_s,Y,Z)=h_tilde_s^(kN). The X Hessian entry has '
     'unit bracket −N^3/(4ab); the remaining Schur complement is kN v^(kN−1)Q. '
     'Thus the full Hessian is invertible at a nonzero critical value, giving the local Morse sphere '
     'and its full-function transport. The final weighted coordinate changes and their inverses '
     'prove both the full-function and reduced-generator normal forms, with all original exponents.'),
    ('r15', 'night:P4R.15',
     'Read the complete old/current and receiving R15 statement and proof. Its statement is unchanged. '
     'The locally irreducible case has exact F=H^M, H=U^(1/M)f, and unchanged nonzero Hessian; '
     'A.5.17 applies at precisely its uniform-multiple scope. The transverse exponent m is kept '
     'separate from M, and the weighted map plus implicit inverse gives the original reduced generator. '
     'The reducible monic quadratic has two monic linear factors, hence g=−H^2 and the exact smooth '
     'factors X±H; the full map with its original a,b is exactly P298. No common-multiplicity '
     'assumption is added. The old conclusion about a smooth entire critical curve and possibly '
     'different initial generic transverse types remains. The original explicit suspension Hessian '
     'and moving-node calculations are retained at A.5.17 with the exact sign map.'),
    ('suspension-owner', 'cdp:st:A.5.17',
     'Read the complete current and receiving A.5.17 proof, including its isolated-singularity argument, '
     'finite-gradient construction, corners and boundary transport, factor shifts, plane Morse '
     'construction and final uniform-multiple Hessian consequence. Its statement and all original '
     'proof steps remain. The added R15 formulas use x=iX and target negation to change '
     'x^2−h_s^b into X^2+h_s^b. The Hessian is diag(2,b v^(b−1)Q), with determinant '
     '2b^2 v^(2b−2) det Q. For h_s=YZ−epsilon, Q has off-diagonal entries1 and determinant−1; '
     'the full determinant is −2b^2 epsilon^(2b−2) for every positive b. '
     'The moved formulas have the same function, sign coordinate map and original scope.')
]
events = []
for suffix, owner, outcome in data:
    event = dict.fromkeys(event_fields, '')
    event.update(statement_id=owner, date=now[:10],
                 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                 type='used and rechecked in this run',
                 outcome=outcome + (' Exposed reading and direct rechecking only. No independent-check '
                                     'credit, required-check increment, integrated compilation or final '
                                     'rendered-page reading is claimed. P4R.14/P4.41/P4.45 remain open '
                                     'pending their separate complete full-function comparisons.'),
                 event_id='publish:c3:foundations:sec07:smooth-contact:' + suffix,
                 phase='publication full-function contact proof',
                 source_file=str(path.relative_to(ROOT)), source_event_type='used and rechecked in this run',
                 evidence_group='publish:c3:foundations:sec07:smooth-contact', date_utc=now,
                 where='P298 after P295; P4R.15 exact applications; A.5.17 plane-gradient step')
    events.append(event)
with (OUT / (prefix + '_CHECK_EVENTS.tsv')).open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)

lines = ['# Bounded full-function contact proof', '',
         'P298 and the complete R15 replacement are read, with the bounded A.5.17 formula transfer. '
         'The R15 full-multiplicity premise is resolved at its original broad domain. '
         'The contracted-boundary subsection and the other three broad consumers remain open. '
         'No subsection completion or movement credit is claimed.', '',
         '| Class | Bounded status | Reason |', '|---|---|---|']
for kind in [f'D{i:02}' for i in range(1, 26)] + ['restructuring']:
    state = 'done'
    reason = 'Complete bounded receiving text read for this class; no further instance in this package.'
    if kind == 'D10':
        reason = 'P298 is a numbered proved owner with complete local full-function data; R15 records both exact earlier inputs.'
    if kind == 'D12':
        reason = 'A.5.17 owns finite-degree/gradient and Morse-sphere constructions; P298 provides its new exact full-function maps. R15 is an exact application; its additional explicit Hessian formulas occur once at A.5.17.'
    if kind == 'D14':
        reason = 'P298 follows P295 and precedes all consumers. A.5.17 and P296 are already earlier; no forward premise is introduced.'
    if kind == 'D16':
        reason = 'R15 keeps every original conclusion and its broad standing domain; the exact full powers a,b remain. Its moving-node formulas and all A.5.17 conclusions are retained.'
    if kind in ['D17', 'D18']:
        reason = 'The proof applies complete earlier internal constructions through the specified functions, rather than deleting them in favour of a new unverified source.'
    if kind == 'D19':
        reason = 'No old tagged formula is moved or removed. All pre-existing stable labels and permanent targets retain their multiplicity.'
    if kind == 'D23':
        state = 'open'
        reason = 'The full source and equations are read; integrated compilation and final rendered pages remain with root.'
    if kind == 'D25':
        reason = 'The R15 gap is closed through the exact full factor-preserving family and unit-retaining critical-centre map. P4R.14/P4.41/P4.45 remain separate OPEN gates and receive no closure from this package.'
    if kind in ['D24', 'restructuring']:
        state = 'open'
        reason = 'The bounded owner/application order is complete; root admission and the whole subsection pass remain. No unit row closes by relocating these statements.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT / (prefix + '_status.md')).write_text('\n'.join(lines) + '\n', newline='\n')

comparison = r'''# Exact full-function contact map

| Input | Morphism and preserved data | Result used |
|---|---|---|
| Original two smooth branches | `F_s=U(X−H_s)^a(X+H_s)^b`; `U,a,b` are unchanged. | The transported levels belong to the original full map, using P295 with `m=1`. |
| Several plane factors | Shift each `h_i` by its own small constant; retain its exponent. At a selected transverse intersection, `H_s=mu v^k w^l`, and `v′=mu^(1/k)v` is invertible. | P296 applies to the full function and gives a compact sphere of nonzero square. |
| Single plane factor | `H=h^k`; solve `NC+(a−b)+q(C²−1)partial_X logU(qC)=0`. Set `W=U(qC)(C−1)^a(C+1)^b`, `Lambda=qW^(1/N)`, and use its unique inverse `R`. | These are exact holomorphic maps, with `Lambda(R(v))=v` and `R(Lambda(q))=q`. |
| Plane Morse deformation | `h_tilde=h W(H)^(1/(kN))`; `H_s=R(h_tilde_s^k,Y,Z)`. | `H_0=H`, multiplicity `k` remains, and the full critical value at `X=H_s C` is exactly `h_tilde_s^(kN)`. |
| Full Hessian | Its `XX` entry has unit bracket `−N³/(4ab)`; its Schur complement is `kN v^(kN−1)Q`. | A nonzero Morse critical value with a square `−2` local sphere, transported through the full family. |
| Locally irreducible R15 | `F=U f^M=H^M`, `H=U^(1/M)f`; the Hessian is scaled by the nonzero unit. | Exact A.5.17 application; the transverse exponent `m` is independent of `M`. |
| Reducible R15 | Monic quadratic factorization forces `g=−H²`; both factors `X±H` are smooth. | Exact P298 application with the original positive multiplicities. |
| Original reduced generator | The displayed weighted unit map and its implicit inverse. | Exact product germ, with no multiplication-by-a-unit ambiguity left. |

The complete old and receiving proofs are read. The R15 statement, all old identifiers and every original formula are preserved. Its explicit suspension Hessian and moving-node calculation now stand in A.5.17, with `x=iX` and target negation as the sign map. Three bounded guards replay once. New tag: P298.

P4R.14, P4.41 and P4.45 still require their own complete factor-preserving comparison. This package does not close those gates or alter their domains.
'''
(OUT / (prefix + '_comparison.md')).write_text(comparison, newline='\n')
print(f'{len(rows)} defect rows; {len(events)} exposed-reading events; R15 full-function premise resolved; three other consumer gates remain OPEN.')
