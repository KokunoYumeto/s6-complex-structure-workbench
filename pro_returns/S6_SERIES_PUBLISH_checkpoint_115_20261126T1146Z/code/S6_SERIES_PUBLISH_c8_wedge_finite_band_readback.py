"""Record the exact based-cylinder and transfer-domain refinements."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
df, ds = r.table(r.DEFECTS)
specs = [
 ('carrier_wedge_recognition', 'BASED-CYLINDER', 'mapsIII:carrier-three-complex-wedge',
  'its homotopy inverse, form its mapping cylinder $N$ with\nbottom inclusion $j_W:W\\to N$, $W=S^2\\vee S^3$, top inclusion\n$j_C:C\\to N$ and retraction $p:N\\to C$. The pair $(N,W)$',
  r'''its homotopy inverse, let $W=S^2\vee S^3$ and form the reduced
based mapping cylinder
\[
 N=(W\times[0,1])\amalg C/\bigl((w,1)\sim F(w),\
                    (w_0,t)\sim c_0\bigr).
\]
Write $j_W,j_C$ for its bottom and top inclusions and let
$p([w,t])=F(w)$, $p(c)=c$. The pair $(N,W)$''',
  'Specify the actual based cylinder before its use; the basepoint arc is explicitly collapsed and the displayed inverse homotopies are defined on this same quotient.'),
 ('carrier_wedge_recognition', 'BASED-HOMOTOPIES', 'mapsIII:carrier-three-complex-wedge',
  'In a reduced based mapping cylinder these\nhomotopies fix the basepoint.',
  'The defining collapsed arc and the condition that $T_s$ fixes\n$W$ make both homotopies fix the basepoint.',
  'Verify basedness on the already defined quotient instead of changing cylinder models after the construction.'),
 ('finite_band_homology', 'TRANSFER-DOMAINS', 'mapsaudit:finite-degree-three',
  r''' D_F\pi_j^*=\operatorname{tr}_jD_{S_j},\qquad
 (\pi_j)_*\operatorname{tr}_j=m_j\operatorname{id},\qquad
 \operatorname{tr}_j(\pi_j)_*=\sum_{k=0}^{m_j-1}A_j^k
 \quad\hbox{on }H_1(F;\mathbb Z).''',
  r''' \begin{aligned}
 D_F\pi_j^*&=\operatorname{tr}_jD_{S_j}
       &&:H^3(S_j;\mathbb Z)\longrightarrow H_1(F;\mathbb Z),\\
 (\pi_j)_*\operatorname{tr}_j&=m_j\operatorname{id}
       &&\text{on }H_1(S_j;\mathbb Z),\\
 \operatorname{tr}_j(\pi_j)_*&=\sum_{k=0}^{m_j-1}A_j^k
       &&\text{on }H_1(F;\mathbb Z).
 \end{aligned}''',
  'Print the exact domain and target of each transfer relation, avoiding a shared trailing domain qualifier for three differently typed maps.')
]
for key, suffix, label, old, new, reason in specs:
    path = u.WORK / 'root' / (key + '.tex')
    before = path.read_text()
    assert before.count(old) == 1, suffix
    after = before.replace(old, new, 1)
    u.check_permanent_identifiers(before, after)
    ident = 'III-C8-ROOT-' + suffix
    assert not any(x['change_id'] == ident for x in ds)
    ds.append(dict(change_id=ident, type='D22', statement_id=label,
        old_location=key + ' complete first rewrite', old_page='pending page concordance',
        new_location=key + ' final readback', new_page='pending final PDF',
        old_text=old, new_text=new, reason=reason,
        review_status='exact staged refinement; final context reading and canonical application pending'))
    path.write_text(after, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
print('UTC', datetime.now(timezone.utc).isoformat())
print('EXACT_READBACK_EDITS', len(specs), 'ALL_IDENTITIES_PRESERVED')
