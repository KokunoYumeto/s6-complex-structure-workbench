"""Build the source-settled Paper III with one isolated TeX kernel.

Every actual compiler stream and log is retained. Stable auxiliary data and
the final diagnostics are checked; this assigns no visual-reading credit.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def diagnostics(log):
    lines = log.splitlines()
    overflow = []
    for index, line in enumerate(lines):
        match = re.search(r'Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)', line)
        if match:
            overflow.append((float(match[1]), '\n'.join(lines[index:index + 5])))
    unresolved = [line for line in lines if re.search(
        r'(?:Reference|Citation).*undefined|There were undefined|Rerun to get|Rerun LaTeX|Label\(s\) may have changed', line)]
    missing = [line for line in lines if re.search(
        r'Missing character|LaTeX Font Warning|not loadable|Font .* not found|font .*not found', line)]
    anchors = [line for line in lines if re.search(
        r'destination with the same identifier|has been referenced but does not exist', line)]
    return overflow, unresolved, missing, anchors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kernel', choices=('current', 'legacy'), required=True)
    parser.add_argument('--run', required=True)
    args = parser.parse_args()
    assert re.fullmatch(r'[a-z0-9_]+', args.run)
    csv.field_size_limit(100000000)
    with (ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv').open(newline='') as stream:
        findings = list(csv.DictReader(stream, delimiter='\t'))
    assert all(row['status'] == 'done' for row in findings if row['id'] not in ('T1', 'P4')), 'Source findings must be settled before the manuscript build.'
    work = ROOT / 'agents/continuation9_build_III' / args.kernel
    work.mkdir(parents=True, exist_ok=True)
    wrapper = ROOT / 'code' / ('S6_SERIES_PUBLISH_c9_current_pdflatex.py' if args.kernel == 'current' else 'S6_SERIES_PUBLISH_c9_tex_runtime.py')
    identity = digest(SOURCE.read_bytes())
    print('UTC start', datetime.now(timezone.utc).isoformat(), flush=True)
    print('Source SHA-256', identity, 'kernel', args.kernel, flush=True)
    previous = None
    for number in range(1, 7):
        prefix = ROOT / 'code' / f'S6_SERIES_PUBLISH_c9_III_{args.kernel}_{args.run}_pass{number:02d}'
        assert not prefix.with_suffix('.log').exists(), 'Do not overwrite an earlier build log.'
        result = subprocess.run([sys.executable, str(wrapper), '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-synctex=1', '-output-directory=' + str(work), str(SOURCE)], cwd=ROOT, capture_output=True)
        prefix.with_suffix('.out').write_bytes(result.stdout)
        prefix.with_suffix('.err').write_bytes(result.stderr)
        actual_log = work / 'S6_SERIES_PUBLISH_III.log'
        log = actual_log.read_text(errors='replace') if actual_log.exists() else ''
        prefix.with_suffix('.log').write_bytes(actual_log.read_bytes() if actual_log.exists() else b'')
        assert digest(SOURCE.read_bytes()) == identity, 'Source changed during build.'
        print('Pass', number, 'exit', result.returncode, flush=True)
        overflow, unresolved, missing, anchors = diagnostics(log)
        print('Diagnostics:', 'overfull', len(overflow), '>2pt', sum(x[0] > 2 for x in overflow), 'unresolved/rerun', len(unresolved), 'fonts', len(missing), 'anchors', len(anchors), flush=True)
        if result.returncode:
            print(result.stdout[-7000:].decode(errors='replace'), result.stderr[-2000:].decode(errors='replace'), flush=True)
            return result.returncode
        state = tuple((work / ('S6_SERIES_PUBLISH_III' + suffix)).read_bytes() if (work / ('S6_SERIES_PUBLISH_III' + suffix)).exists() else b'' for suffix in ('.aux', '.toc', '.out'))
        if state == previous and not unresolved:
            break
        previous = state
    else:
        raise RuntimeError('Auxiliary data did not converge in six passes.')
    for width, context in overflow:
        print('OVERFULL', width, context, sep='\n', flush=True)
    for category, values in [('UNRESOLVED', unresolved), ('FONT', missing), ('ANCHOR', anchors)]:
        for value in values:
            print(category, value, flush=True)
    pdf = work / 'S6_SERIES_PUBLISH_III.pdf'
    info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True)
    fonts = subprocess.run(['pdffonts', str(pdf)], capture_output=True, text=True, check=True)
    print(info.stdout, fonts.stdout, sep='\n', flush=True)
    print('PDF', pdf, 'SHA-256', digest(pdf.read_bytes()), flush=True)
    print('UTC complete', datetime.now(timezone.utc).isoformat(), flush=True)
    print('No visual-page-reading credit follows from this build.', flush=True)
    return 2 if any(width > 2 for width, _ in overflow) or unresolved or missing or anchors else 0

if __name__ == '__main__':
    raise SystemExit(main())
