"""Stage or admit four exact current06/legacy05 layout diagnostics.

Default: inspect and write this packet's proposal TSV/diff only. Root must read
the packet, authored reviews and actual inspection output before explicitly
invoking --apply --root-reviewed. No CHECK_EVENTS, counts, progress or derived
records are written. Existing defect-ledger bytes are preserved as a prefix.
"""
from pathlib import Path
import argparse
import csv
import difflib
import hashlib
import io
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
DEFECTS = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
OUT = ROOT / 'agents/continuation9_candidate06_diagnostics'
PREFIX = 'S6_SERIES_PUBLISH_c9_candidate06_diagnostic_batch'
ANCHOR = ROOT / 'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate06_anchor_defects.tsv'
ANCHOR_JSON = ANCHOR.with_name('S6_SERIES_PUBLISH_c9_candidate06_anchor_proposals.json')
EXPECTED_SOURCE = '488e2b3ae308efeb3a1f6ef583930f8ae79af8379414ef8572fae8213e187aa5'
FIELDS = ['change_id', 'type', 'statement_id', 'old_location', 'old_page',
          'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status']
RUNS = {
    'current': ('candidate06', '30a3ba9654908429ff88e0fd5c5b131d651bab29590103abff7a6275b07198d2'),
    'legacy': ('candidate05', '2be6227137c37222d98ff546168eb91b20fd8c07cb5edaf32c9260b52c6f28db'),
}

OLD_MONODROMY = r'''\[
 \beta_i=-a g_i^tJ_{\rm ell}A_i,\qquad c_i^{\rm mon}=\beta_i b z_i+w_i,
 \qquad
 T_i=\begin{pmatrix}A_i&0&bg_i\\\beta_i&1&c_i^{\rm mon}\\0&0&1\end{pmatrix},
 \qquad
 w_i=\begin{cases}1/\nu_i&i\text{ selected},\\0&\text{otherwise}.
 \end{cases}
\]'''
OLD_PAIRING = r'''\begin{equation}
 K_N=(SC_S)^t\omega(LC_L)
       =\begin{pmatrix}n_{\rm per}&0\\M&r_{\rm per}\end{pmatrix},\qquad
 n_{\rm per}=\frac{a\nu}{d_0^2},\quad r_{\rm per}=-\frac{bd_0^2}{\nu},\qquad
 \delta=-\sigma_{\rm Bez} l+n_0p_0.
\hypertarget{tag-Q23B}{}\label{maps:eq:MT_local_38}
\end{equation}'''
OLD_BORDISM = r'''\begin{equation}
 \Omega_6^{\rm Spin}(K(\mathbb Z/2,2))
       =\mathbb Z\langle\epsilon_{2,\rm bord},\zeta_{2,\rm bord}\rangle/
                        \langle\epsilon_{2,\rm bord},2\zeta_{2,\rm bord}\rangle,\quad
 P(\zeta_{2,\rm bord})=1,\quad h_{\rm bord}(\zeta_{2,\rm bord})=\gamma_3(e_{2,\rm coef}).
\hypertarget{tag-Q24O}{}\label{maps:eq:MT_local_93}
\end{equation}'''


def sha(data):
    return hashlib.sha256(data).hexdigest()


def replace_once(text, old, new):
    assert text.count(old) == 1, ('fragment multiplicity', old, text.count(old))
    return text.replace(old, new, 1)


def make_reflow(old, opening, closing, gap_old, gap_new):
    steps = [(opening, opening + '\\begin{gathered}\n'),
             (gap_old, gap_new),
             (closing, '\\end{gathered}\n' + closing)]
    new = old
    for left, right in steps:
        new = replace_once(new, left, right)
    recovered = new
    for left, right in reversed(steps):
        recovered = replace_once(recovered, right, left)
    assert recovered == old
    return new


def exact_matrix_blocks(text):
    return [m.group(0) for m in re.finditer(
        r'\\begin\{(pmatrix|cases)\}.*?\\end\{\1\}', text, re.S)]


def ordered_formula_tokens(text):
    # Protect complete matrix/cases bodies first, including their row separators.
    counter = iter(range(100))
    text = re.sub(r'\\begin\{(pmatrix|cases)\}.*?\\end\{\1\}',
                  lambda _: r'\PreservedMatrix{' + str(next(counter)) + '}', text,
                  flags=re.S)
    text = re.sub(r'\\(?:begin|end)\{gathered\}', '', text)
    text = re.sub(r'\\(?:qquad|quad)\b|\\\\', '', text)
    return re.findall(r'\\[A-Za-z@]+|\\.|[^\s]', text)


def serialize(rows, header=False):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, FIELDS, delimiter='\t', lineterminator='\n')
    if header:
        writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode('utf-8')


def rows_for_reflows():
    new_monodromy = make_reflow(
        OLD_MONODROMY, '\\[\n', '\\]',
        ' \\qquad\n T_i=', ' \\\\\n T_i=')
    new_pairing = make_reflow(
        OLD_PAIRING, '\\begin{equation}\n', r'\hypertarget{tag-Q23B}',
        '\\end{pmatrix},\\qquad\n', '\\end{pmatrix},\\\\\n')
    new_bordism = make_reflow(
        OLD_BORDISM, '\\begin{equation}\n', r'\hypertarget{tag-Q24O}',
        '\\langle\\epsilon_{2,\\rm bord},2\\zeta_{2,\\rm bord}\\rangle,\\quad\n',
        '\\langle\\epsilon_{2,\\rm bord},2\\zeta_{2,\\rm bord}\\rangle,\\\\\n')
    data = [
        ('01', 'maps:src:D.2.39', '02LF unnumbered four-period monodromy display',
         '40963-40970', '476', '21.24054', OLD_MONODROMY, new_monodromy,
         'The first gathered row retains beta_i and c_i^{mon}; the second retains T_i and w_i. '
         'The complete displayed block matrix and two-case definition, with their row separators, are byte-identical. '
         'The following inverse matrix is outside the replacement and remains byte-identical.'),
        ('02', 'maps:src:D.2.42', '02LJ rank-one pairing, maps:eq:MT_local_38 / tag Q23B',
         '42291-42297', '493', '14.52957', OLD_PAIRING, new_pairing,
         'The first gathered row retains K_N=(SC_S)^t omega(LC_L) and its complete 2-by-2 matrix. '
         'The second retains n_per, r_per and delta in the original order. '
         'The defining basis matrices and literal inverses are outside the replacement and remain byte-identical.'),
        ('03', 'maps:src:D.2.42', '02LJ two-primary quotient, maps:eq:MT_local_93 / tag Q24O',
         '43196-43202', '503', '51.98416', OLD_BORDISM, new_bordism,
         'The first gathered row retains the complete bordism quotient. The second retains P(zeta_2,bord)=1 '
         'and h_bord(zeta_2,bord)=gamma_3(e_2,coef), in that order. '
         'The immediately following forward map and inverse are outside the replacement and remain byte-identical.'),
    ]
    rows = []
    for num, owner, location, lines, page, width, old, new, explanation in data:
        assert exact_matrix_blocks(old) == exact_matrix_blocks(new)
        assert ordered_formula_tokens(old) == ordered_formula_tokens(new)
        row = dict.fromkeys(FIELDS, '')
        row.update(change_id='III-C9-CURRENT06-REFLOW-' + num, type='D23', statement_id=owner,
                   old_location=f'{location}; frozen source lines {lines}',
                   old_page=f'current candidate06 / legacy candidate05; shipout context page {page}',
                   new_location=location + '; two gathered rows',
                   new_page='Pending current candidate07 / legacy candidate06 and actual image reading',
                   old_text=old, new_text=new,
                   reason=f'Both fully read final pass03 logs report {width}pt overflow at this exact display. '
                          + explanation + ' The identity on every displayed mathematical token gives the '
                          'same formulas; only a gathered wrapper and one outer line break replace one '
                          'horizontal gap. Reversing those three literal edits restores the complete old '
                          'fragment. All punctuation, labels and permanent tags remain in order. '
                          'No mathematical check event or count is added.',
                   review_status='Exact source, ordered-token and reverse comparisons completed; '
                                 'fresh two-kernel build and actual changed-page reading remain open.')
        rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--root-reviewed', action='store_true')
    args = parser.parse_args()
    assert not args.apply or args.root_reviewed, 'Root review is required before --apply.'
    csv.field_size_limit(100000000)
    before_bytes = SOURCE.read_bytes()
    before = before_bytes.decode('utf-8')
    prior_ledger = DEFECTS.read_bytes()
    assert sha(before_bytes) == EXPECTED_SOURCE
    assert b'\r' not in before_bytes and b'\r' not in prior_ledger
    assert prior_ledger.endswith(b'\n')
    reader = csv.DictReader(io.StringIO(prior_ledger.decode('utf-8'), newline=''), delimiter='\t')
    assert reader.fieldnames == FIELDS
    existing = list(reader)

    # Bind this packet to the actual completed drivers, final logs and PDFs.
    for kernel, (run, pdf_hash) in RUNS.items():
        driver = (ROOT / 'code' / f'S6_SERIES_PUBLISH_c9_build_III_{kernel}_{run}.out').read_text()
        assert f'Source SHA-256 {EXPECTED_SOURCE} kernel {kernel}' in driver
        assert re.findall(r'^Pass (\d+) exit (\d+)$', driver, re.M) == [('1', '0'), ('2', '0'), ('3', '0')]
        assert 'Pass 3 exit 0\nDiagnostics: overfull 5 >2pt 3 unresolved/rerun 0 fonts 0 anchors 0' in driver
        log = (ROOT / 'code' / f'S6_SERIES_PUBLISH_c9_III_{kernel}_{run}_pass03.log').read_bytes().decode('latin1')
        expected = [('0.83005', '21377'), ('21.24054', '40970'), ('14.52957', '42297'), ('51.98416', '43202')]
        assert re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\) detected at line (\d+)', log) == expected
        assert 'Overfull \\hbox (1.34203pt too wide) in paragraph at lines 45104--45115' in log
        pdf = ROOT / 'agents/continuation9_build_III' / kernel / 'S6_SERIES_PUBLISH_III.pdf'
        assert sha(pdf.read_bytes()) == pdf_hash
        print(f'Observed {kernel} {run}: completed pass03; three >2pt displays; PDF {pdf_hash}')

    rows = rows_for_reflows()
    with ANCHOR.open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        assert reader.fieldnames == FIELDS
        anchor_rows = list(reader)
    anchor_data = json.loads(ANCHOR_JSON.read_text())
    assert len(anchor_rows) == len(anchor_data) == 1
    anchor = anchor_rows[0]
    anchor_meta = anchor_data[0]
    assert anchor['change_id'] == 'C9-III-CANDIDATE06-ANCHOR-001'
    assert anchor['type'] == 'D23' and anchor['statement_id'] == 'wb:cusp-cone-S12-route'
    assert anchor_meta['source_sha256'] == EXPECTED_SOURCE
    assert (anchor['old_text'], anchor['new_text']) == (anchor_meta['old'], anchor_meta['new'])
    assert anchor['new_text'] == '\\Needspace{6\\baselineskip}\n' + anchor['old_text']
    rows.append(anchor)
    assert len(rows) == 4 and len({r['change_id'] for r in rows}) == 4
    assert not ({r['change_id'] for r in rows} & {r['change_id'] for r in existing})

    after = before
    for row in rows:
        assert before.count(row['old_text']) == 1
        assert before.count(row['new_text']) == 0
        after = replace_once(after, row['old_text'], row['new_text'])
        print(row['change_id'], 'unique old/new guard;', row['statement_id'])
    reverse = after
    for row in reversed(rows):
        assert after.count(row['new_text']) == 1
        reverse = replace_once(reverse, row['new_text'], row['old_text'])
    assert reverse == before

    patterns = {
        'labels': r'\\label\{[^{}]+\}',
        'permanent targets': r'\\hypertarget\{[^{}]+\}',
        'explicit tags': r'\\tag\*?\{[^{}]+\}',
        'references and citations': r'\\(?:[cC]ref|eqref|ref|pageref|cite[a-z]*)\*?(?:\[[^\]]*\])*\{[^{}]+\}',
    }
    for title, expression in patterns.items():
        assert re.findall(expression, before) == re.findall(expression, after)
        print('Ordered', title, 'preserved.')
    environment_pattern = r'\\(?:begin|end)\{(?!gathered\})[^{}]+\}'
    assert re.findall(environment_pattern, before) == re.findall(environment_pattern, after)
    numeric_after = replace_once(after, anchor['new_text'], anchor['old_text'])
    assert re.findall(r'\d+', before) == re.findall(r'\d+', numeric_after)
    print('All original environment boundaries and mathematical numeric literals preserved.')
    for row in rows[:3]:
        assert ordered_formula_tokens(row['old_text']) == ordered_formula_tokens(row['new_text'])
        assert exact_matrix_blocks(row['old_text']) == exact_matrix_blocks(row['new_text'])
        print(row['change_id'], 'ordered formula tokens and complete matrix/cases bodies identical.')
    print('Whole-source reverse SHA-256', sha(reverse.encode('utf-8')))
    print('Proposed source SHA-256', sha(after.encode('utf-8')))

    addition = serialize(rows)
    proposed_ledger = prior_ledger + addition
    assert proposed_ledger[:len(prior_ledger)] == prior_ledger
    parsed = list(csv.DictReader(io.StringIO(proposed_ledger.decode('utf-8'), newline=''), delimiter='\t'))
    assert parsed == existing + rows
    assert b'\r' not in addition
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / (PREFIX + '_defects.tsv')).write_bytes(serialize(rows, header=True))
    diff = ''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                     fromfile='S6_SERIES_PUBLISH_III.tex (current06 frozen source)',
                                     tofile='S6_SERIES_PUBLISH_III.tex (four layout proposals)'))
    (OUT / (PREFIX + '.diff')).write_bytes(diff.encode('utf-8'))
    assert SOURCE.read_bytes() == before_bytes and DEFECTS.read_bytes() == prior_ledger
    print('Defect-ledger prefix preserved:', len(prior_ledger), 'bytes;', len(existing), 'existing rows; four appended rows.')
    if args.apply:
        SOURCE.write_bytes(after.encode('utf-8'))
        with DEFECTS.open('ab') as stream:
            stream.write(addition)
        assert SOURCE.read_bytes() == after.encode('utf-8')
        assert DEFECTS.read_bytes() == proposed_ledger
        print('APPLIED after explicit root-review acknowledgment: four D23 rows and four exact source edits.')
    else:
        print('INSPECT ONLY: canonical source and defect ledger unchanged.')
    print('No CHECK_EVENT, count, progress/status, finding or derived record written.')
    print('Fresh builds, T1/formal inspections and actual changed-page reading remain open.')


if __name__ == '__main__':
    main()
