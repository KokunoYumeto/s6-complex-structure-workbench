"""Stage exact radial-coefficient imports; canonical files remain unchanged."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import difflib
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_root_image_repairs'
TMP = ROOT.parents[1] / 'tmp/c9_root_radial_imports'
TMP.mkdir(parents=True, exist_ok=True)
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
blocks = {}
history = []
for tag in ['039U', '0374', '0375']:
    mark = source.index(r'\hypertarget{tag-' + tag + '}')
    begin = source.rfind(r'\begin{theorem}', 0, mark)
    end = source.index(r'\end{proof}', mark) + len(r'\end{proof}')
    old = source[begin:end]
    assert source.count(old) == 1
    blocks[tag] = [old, old]

def change(tag, key, begin, end, transform, reason):
    scope = blocks[tag][1]
    a = scope.index(begin)
    b = scope.index(end, a) + len(end)
    old = scope[a:b]
    new = transform(old)
    assert old != new and scope.count(old) == 1
    blocks[tag][1] = scope[:a] + new + scope[b:]
    history.append(dict(tag=tag, key=key, old=old, new=new, reason=reason))

old_constant = r'Here \(B_{\rm rad}=B\) denotes the bounded radial coefficient.'
change('039U', 'limiting-coefficient', old_constant, old_constant,
       lambda s: s.replace(r'B_{\rm rad}=B', r'B_{\rm rad}=\operatorname{Im}b(0)'),
       'The radial-data definition identifies the limiting coefficient as Im b(0). Bind B_rad directly to that same real number, preserving the circumference and determinant expansions. The base B retains its original space; no unqualified coefficient B is introduced in this theorem.')

matrix_old = r''' P_T=\begin{pmatrix}
 6\alpha&\eta&1&0\\
 6m&L&0&0\\
 c&\alpha&0&1\\
 -q&m&0&0
 \end{pmatrix},\qquad
 Y_T=\begin{pmatrix}6m&L\\-q&m\end{pmatrix},'''
matrix_new = r''' P_T=\begin{pmatrix}
 6\alpha_T&\eta_T&1&0\\
 6m_T&L_T&0&0\\
 c_T&\alpha_T&0&1\\
 -q_T&m_T&0&0
 \end{pmatrix},\qquad
 Y_T=\begin{pmatrix}6m_T&L_T\\-q_T&m_T\end{pmatrix},'''
def physical_obstruction(s):
    assert s.count(matrix_old) == 1
    old = r''' \quad D_T=Lq+6m^2>0,
\]
where \(L=T+H\), \(B_{\rm rad}=B\), \(q=L-B_{\rm rad}\), and the remaining coefficients are bounded.'''
    new = r''' \quad D_T=L_Tq_T+6m_T^2>0,
\]
where \(L_T=T+H_T\) and \(q_T=L_T-B_T\). The radial coefficients
\(\alpha_T,\eta_T,m_T,c_T,H_T,B_T\) are bounded.'''
    assert s.count(old) == 1
    return s.replace(matrix_old, matrix_new, 1).replace(old, new, 1)
change('0374', 'pointwise-native-matrix', matrix_old, 'and the remaining coefficients are bounded.', physical_obstruction,
       'The displayed P_T is the already defined native real period matrix. Read its entries: alpha=P_11/6=P_32=alpha_T, eta=P_12=eta_T, m=P_21/6=P_42=m_T, L=P_22=L_T, c=P_31=c_T and q=-P_41=q_T. Hence H=L-T=H_T and the pointwise radial B=L-q=B_T. Identity on these actual entries and its inverse preserve P_T,Y_T,D_T and every quotient map. Keeping their established T indices also leaves the later local cover integer m as its single named object.')

statement_old = r''' =T+H-B+O(T^{-1}).
\]
The associated compact source'''
statement_new = r''' =T+H-B_{\rm rad}+O(T^{-1}).
\]
Here \(B_{\rm rad}=\operatorname{Im}b(0)\) is the limiting radial coefficient.
The associated compact source'''
change('0375', 'limiting-coefficient', statement_old, statement_old,
       lambda s: s.replace(statement_old, statement_new, 1),
       'The statement uses the constant B=Im b(0) from the radial-data definition. B_rad is that exact same number, with explicit binding; the asymptotic coefficients and error term are unchanged. The regular base B retains its original meaning.')

def physical_optimality(s):
    assert s.count(matrix_old) == 1
    old = r'''where \(L=T+H\), \(q=L-B\),
\(D_T=\det Y_T=Lq+6m^2>0\), and the residual coefficients are bounded'''
    new = r'''where \(L_T=T+H_T\), \(q_T=L_T-B_T\),
\(D_T=\det Y_T=L_Tq_T+6m_T^2>0\), and the residual coefficients are bounded'''
    assert s.count(old) == 1
    return s.replace(matrix_old, matrix_new, 1).replace(old, new, 1)
change('0375', 'pointwise-native-matrix', matrix_old, 'on a sufficiently small radial tail.', physical_optimality,
       'Use the actual time-indexed entries of the same native P_T and Y_T. The entrywise identity and inverse specified for0374 identify each formerly unindexed coefficient with its established T-indexed value. The statement retains limiting H and B_rad; the proof now names the exact pointwise coefficients throughout its matrix and determinant.')

def pointwise_metric(s):
    for letter in ['L', 'B', 'm', 'H']:
        s, n = re.subn(r'(?<![A-Za-z\\])' + letter + r'(?![A-Za-z_])', letter + '_T', s)
        assert n, letter
    return s
change('0375', 'pointwise-metric-remainder', 'for $G=Y_T^{\\mathsf T}Y_T$', 'This is the stated unscaled quotient metric.', pointwise_metric,
       'Propagate L_T,B_T,m_T,H_T through the Schur-complement equality, radius, exact remainder, boundedness and zero-value case. With R_T^2=L_T^2+m_T^2 and q_T=L_T-B_T, subtracting q_T from (L_Tq_T+6m_T^2)/R_T gives m_T^2/R_T times (6-q_T/(R_T+L_T)), exactly the displayed remainder. All actual quotient maps and their arclength/least-norm inverses stay fixed. The earlier holomorphic-error comparison identifies its limiting coefficients with H and B_rad in the statement.')

def slice_map(s):
    assert s.count(r'\alpha_T') == 2
    return s.replace(r'\alpha_T', r'\alpha_{T,\rm sl}')
change('0375', 'slice-map', 'For a radial slice put', 'c_{\\mathcal C}i_T=\\zeta_T\\pi_{\\gamma,T}.', slice_map,
       'alpha_(T,sl) is the exact same slice embedding y↦[r_T,1,iota_T^-1(y)]. It retains that pointwise formula and its occurrence in c_A i_T=alpha_(T,sl) pi_T. This qualification preserves the native period coefficient alpha_T as a distinct full symbol; the inverse on the embedded slice remains recovery of y via iota_T.')

now = datetime.now(timezone.utc).isoformat()
rows, events = [], []
whole = source
for tag, (old, new) in blocks.items():
    inverse = new
    local = [h for h in history if h['tag'] == tag]
    for h in reversed(local):
        assert inverse.count(h['new']) == 1
        inverse = inverse.replace(h['new'], h['old'], 1)
    assert inverse == old
    for pattern in [r'\\(?:label|hypertarget)\{[^{}]+\}', r'\\(?:[Cc]ref|[Ee]qref|ref|cite)(?:\[[^]]*\])?\{[^{}]+\}', r'\\mathbb\s*(?:\{[^{}]+\}|[A-Za-z])']:
        assert re.findall(pattern, old) == re.findall(pattern, new)
    expected = Counter(re.findall(r'\d+', old))
    expected['0'] += 1 if tag in ['039U', '0375'] else 0
    assert expected == Counter(re.findall(r'\d+', new)), tag
    owner = re.search(r'\\label\{([^}]+)\}', old).group(1)
    for h in local:
        assert whole.count(h['old']) == 1
        whole = whole.replace(h['old'], h['new'], 1)
        rows.append(dict(change_id='III-C9-ROOT-RADIAL-' + tag + '-' + h['key'], type='D20', statement_id=owner, old_location=tag + ' current source; ' + h['key'], old_page='candidate02; prior actual root image reading', new_location=tag + ' source; ' + h['key'], new_page='pending changed-page reading', old_text=h['old'], new_text=h['new'], reason='CLAUDE-III-P15. ' + h['reason'], review_status='Root read the actual radial definitions/proposition, complete current0374/0375 scopes, and affected039U statement/proof passages against its earlier complete reading. Every exact difference read; admission and rendering pending.'))
    event_id = 'publish:c9:III:' + tag + ':radial-import-readback'
    events.append(dict(statement_id=owner, date='2026-11-26', who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; root', type='used and rechecked in this run', outcome='Compared the actual time-indexed radial-data entries, pointwise period matrix and limiting imaginary coefficients with every affected current source use. ' + str(len(local)) + ' exact fragments retain the same physical matrices, quotient maps and inverse formulas. Full-source reversal, permanent identifiers and blackboard fields checked. Only the two explicit limiting-value bindings add their written zero arguments. Exposed source rechecking; no independent-proof or new-image credit.', event_id=event_id, phase='publication continuation9', source_file='agents/continuation9_root_image_repairs/S6_SERIES_PUBLISH_c9_root_radial_imports_review.md', source_row=tag + ' radial imports and every affected use', source_event_type='used and rechecked in this run', evidence_group=event_id, publish_input_file='S6_SERIES_PUBLISH_III.tex', publish_input_row=owner, date_utc=now, where='Original/proposed bounded source comparison; retained prior actual root image evidence.'))
    (TMP / (tag + '_original.tex')).write_text(old, newline='\n')
    (TMP / (tag + '_proposed.tex')).write_text(new, newline='\n')
    (OUT / ('S6_SERIES_PUBLISH_c9_root_radial_' + tag + '.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=tag+'-current', tofile=tag+'-proposed')), newline='\n')
inverse = whole
for h in reversed(history):
    assert inverse.count(h['new']) == 1
    inverse = inverse.replace(h['new'], h['old'], 1)
assert inverse == source
assert len(rows) == 6 and len(events) == 3
for canonical, suffix, contents in [('S6_SERIES_PUBLISH_defects_III.tsv','defects',rows), ('CHECK_EVENTS.tsv','CHECK_EVENTS',events)]:
    with (ROOT / canonical).open(newline='') as f:
        fields = next(csv.reader(f, delimiter='\t'))
    with (OUT / ('S6_SERIES_PUBLISH_c9_root_radial_imports_' + suffix + '.tsv')).open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader(); writer.writerows(contents)
print('Six exact fragments, three scoped used events; complete source reverses byte for byte.')
print('Original numbers preserved; exactly two written zero arguments added to bind the existing limiting coefficients.')
print('All source identifiers, references, citations and blackboard tokens preserved. Canonical source/records untouched.')
