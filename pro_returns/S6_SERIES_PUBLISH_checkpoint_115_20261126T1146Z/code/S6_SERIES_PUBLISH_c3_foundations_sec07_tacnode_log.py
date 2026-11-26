from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix = 'S6_SERIES_PUBLISH_sec07_tacnode'
path = OUT / (prefix + '_defects.tsv')
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
for row in rows:
    row['review_status'] = ('Complete old/current and receiving P4R.14 proofs read and compared. '
                            'The exact full-unit coordinate map, rank-two intersection argument, '
                            'weighted polar calculation and boundary inverse were followed. '
                            'The full Hessian identity and retained six-root example were also '
                            'verified symbolically. The single bounded guard replays once and all '
                            'old label/target multiplicities remain. Root admission pending.')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
with (ROOT / 'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields = next(csv.reader(f, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
data = [
    ('factor-domain',
     'Read the whole original/current and receiving R14 proof. The common-root discriminant deformation '
     'is now used only for a locally irreducible reduced equation, with the exact F=f0^M and unchanged '
     'critical germ; the root multiplies Delta by a unit square. For two local factors, their intersection '
     'is the full smooth axis. The one-dimensional complete-intersection quotient is finite free of '
     'rank2 over C{z}; its special fibre has length2, forcing one factor smooth. The restriction '
     'of the other is a unit times y^2, giving Delta=−(alpha delta−beta gamma)^2 with unit determinant. '
     'Thus the reducible case changes no factor or full multiplicity. The original exact graph '
     'factorization and parameter Morse map remain, and both normalization conclusions remain.'),
    ('weighted-polar',
     'Read and directly followed all receiving full-function steps. The bth root of U and parameter '
     'Morse coordinate in Y change U X^a(Y^2+XH)^b exactly into X^a(Y^2+XK)^b, fixing X,z. '
     'The critical-value derivative gives K(0,z)=U(0,0,z)^(1/b)H(0,z), so their z derivatives '
     'vanish together at the origin. On every branch of K_z=0, X=t^r gives X K_X=(t/r)dK/dt; '
     'the positive coefficients a+b+bj/r force isolation of (K_z,(a+b)K+bXK_X). '
     'The displayed finite map and exclusion of X=0,K_X=0 give nonzero critical values of the '
     'original full weighted family. Its determinant is 2b^2 F_s^3 J/(X^2 K_s^3). '
     'The exact boundary maps T=XK_s, X=chi_s=T kappa_s, and the weighted unit map with its '
     'implicit inverse give fixed full transverse charts, including smooth component strata. '
     'P295 applies with g_s=F_s,m=1. Its sphere therefore reaches the original full fibre. '
     'All old a=b=1 polar equations, Psi, critical value, Hessian block and determinant remain '
     'as their exact specialization. The R14 broad statement is unchanged.'),
    ('algebra-and-example',
     'Ran code/S6_SERIES_PUBLISH_c3_foundations_sec07_tacnode_algebra.py after directly deriving the '
     'weighted logarithmic Hessian. Symbolic substitution K_s=−bXK_X/(a+b) proves the displayed '
     'determinant identity and its a=b=1 specialization 2X^4J. For the retained H=z(x−z)(x−2z) '
     'example, both ideal containments were checked for the printed two-polynomial Groebner basis; '
     'the degree-six eliminant is square-free; adjoining x, H_x or J gives the unit ideal in '
     'each case. The full old and receiving positive-genus example was read, including its '
     'double-cover normalization, elliptic exceptional curve, discrepancy/pole coefficient and '
     'epsilon^(1/3) scaling. No example or stronger original conclusion is deleted.')
]
events = []
for suffix, outcome in data:
    event = dict.fromkeys(event_fields, '')
    event.update(statement_id='night:P4R.14', date=now[:10],
                 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                 type='used and rechecked in this run',
                 outcome=outcome + (' Exposed reading and direct rechecking only; no independent '
                                     'credit, required-check increment, integrated compilation or '
                                     'final rendered-page reading. P4.41 and P4.45 remain OPEN '
                                     'pending their separate full-function comparisons.'),
                 event_id='publish:c3:foundations:sec07:tacnode:' + suffix,
                 phase='publication full-multiplicity tacnode proof',
                 source_file=str(path.relative_to(ROOT)), source_event_type='used and rechecked in this run',
                 evidence_group='publish:c3:foundations:sec07:tacnode', date_utc=now,
                 where='Complete P4R.14 replacement, retaining its original domain and P4R.14.1–5 formulas')
    events.append(event)
with (OUT / (prefix + '_CHECK_EVENTS.tsv')).open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)

lines = ['# Bounded full-multiplicity tacnode proof', '',
         'The complete original/current and receiving R14 proofs are read. The broad R14 statement '
         'and every original formula are retained, and its unequal-multiplicity premise is proved '
         'through the full polar family. P4.41 and P4.45 remain separate open tasks. '
         'No subsection completion or movement credit is claimed.', '',
         '| Class | Bounded status | Reason |', '|---|---|---|']
for kind in [f'D{i:02}' for i in range(1, 26)] + ['restructuring']:
    state = 'done'
    reason = 'The complete bounded receiving text is read for this class; no further instance in this owner.'
    if kind == 'D10':
        reason = 'The original numbered owner and statement persist, with its exact earlier inputs and full-function data stated in the proof.'
    if kind == 'D12':
        reason = 'The earlier coordinate, sphere and boundary owners are applied at exact scopes. The weighted polar proof retains the old unweighted formulas only as its specialization.'
    if kind == 'D14':
        reason = 'All used construction and boundary owners precede R14; the proof introduces no forward premise. Whole-paper placement remains with root.'
    if kind == 'D16':
        reason = 'The original domain, both exact normal forms, all normalization conclusions, pole example and P4R.14.1–5 payloads remain.'
    if kind in ['D17', 'D18']:
        reason = 'The complete earlier internal proofs are used through explicit maps. No proof is deleted in favour of a new unverified external source.'
    if kind == 'D19':
        reason = 'All five original manual tags now have the exact prepared eq:II:manual:P4R.14.1–5 labels and section equation numbering; their old-tag map accompanies the package.'
    if kind == 'D23':
        state = 'open'
        reason = 'Complete source read and symbolic formula checks are done; integrated compilation and rendered pages remain with root.'
    if kind == 'D25':
        reason = 'R14 is proved at its original domain, with original full multiplicities. P4.41 and P4.45 receive no closure from this bounded package.'
    if kind in ['D24', 'restructuring']:
        state = 'open'
        reason = 'The bounded proof and input order are complete; root admission and the enclosing subsection pass remain. No movement credit is claimed.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT / (prefix + '_status.md')).write_text('\n'.join(lines) + '\n', newline='\n')

comparison = r'''# R14 exact factor and full-function comparison

| Stage | Exact map or algebra | Consequence |
|---|---|---|
| Locally irreducible support | `f0=U^(1/M)f`, `F=f0^M`; the quartic discriminant is multiplied by a unit square. | The original simple-discriminant-zero deformation and P295 are valid for this precise full-map root. |
| Two local factors | `A=C{x,y,z}/(phi,psi)` is finite free of rank2 over `C{z}`. Its special fibre has length2. | One factor is smooth; the restricted other factor is a unit times `y²`, and `Delta=−(alpha delta−beta gamma)²` is a unit without moving either factor. |
| Reduced second model | Graph root `X=x−y²v(y,z)` and the parameter Morse coordinate give `f=X(Y²+XH)`. | The original exact reduced normal form and all original hypotheses remain. |
| Full unit | Multiply the second factor by `V=U^(1/b)` and complete the square in `Y`, fixing `X,z`. | `F=X^a(Y²+XK)^b` exactly, with `K(0,z)=V(0,0,z)H(0,z)`. |
| Weighted polar family | `K_s=K−eta z−epsilon`; retain `F_s=X^a(Y²+XK_s)^b`. | Original component multiplicities `a,b` remain. |
| Isolated finite map | `G_(a,b)=(a+b)K+bXK_X`, `Psi=(K_z,(G_(a,b)−(a+b)zK_z)/(a+b))`. Along `K_z=0`, `X=t^r` gives positive coefficients `a+b+bj/r`. | Finite positive local degree; a regular value avoiding the two exceptional curves gives full nonzero Morse critical values. |
| Full Hessian | `det Hess F_s=2b² F_s³ J/(X²K_s³)`. | Nonzero at every selected point; its `a=b=1` specialization is the retained `2X⁴J`. |
| Boundary | `T=XK_s`, inverse `X=chi_s=T kappa_s`, followed by the displayed weighted unit map and implicit inverse. | Fixed full transverse function `T^a(Y²+T)^b`; P295 applies with `m=1`, including smooth component strata. |
| Original conclusion | `K_z(0)≠0` iff `H_z(0)≠0`; invert `Z=H(X,z)`. | The original exact second reduced normal form and plane/quadric normalization. |

The single bounded guard preserves every old stable label and permanent target. P4R.14.1–5 use their prepared section-equation labels. The original full positive-genus example and its explicit six-root calculation remain; the Hessian and example ideals have been symbolically rechecked. No new tag is allocated. P4.41/P4.45 remain open.
'''
(OUT / (prefix + '_comparison.md')).write_text(comparison, newline='\n')
print(f'{len(rows)} defect rows; {len(events)} exposed-reading events; R14 full-multiplicity premise resolved; P4.41/P4.45 remain OPEN.')
