"""Read-only snapshot of current A--C statements, outlines and body proof blocks.

This is an exposed global comparison intake, after the separately frozen
statement-directed record.  It does not assign independent-check credit.
"""
from pathlib import Path
import datetime, hashlib, json, re, sys

ROOT = Path('/workspace/scratch/653608133b22')
OUT = Path(__file__).parent
SOURCE = ROOT / 'work/S6_SERIES_PUBLISH_I.tex'
s = SOURCE.read_text()
freeze = json.loads((OUT / 'S6_SERIES_PUBLISH_I_global_ABC_preread_freeze.json').read_text())
for row in freeze['files']:
    p = Path(row['path'])
    assert hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256'], p

starts = list(re.finditer(r'\\begin\{(maintheorem|theorem|proposition|corollary|lemma|definition|remark|cited)\}', s))

def block(label):
    i = s.index(r'\label{' + label + '}')
    m = max((m for m in starts if m.start() < i), key=lambda m: m.start())
    end = r'\end{' + m.group(1) + '}'
    e = s.index(end, m.end()) + len(end)
    assert i < e, label
    nxt = re.search(r'\\begin\{(proof|maintheorem|theorem|proposition|corollary|lemma|definition|remark|cited|figure)\}', s[e:])
    if nxt and nxt.group(1) == 'proof':
        a = e + nxt.start()
        e = s.index(r'\end{proof}', a) + len(r'\end{proof}')
    return {'label':label, 'line_start':s.count('\n',0,m.start())+1,
            'line_end':s.count('\n',0,e)+1, 'text':s[m.start():e]}

labels = [
    'series:I:A','series:I:B','series:I:C','I:weierstrass-comparison',
    'fam:src:B.1.1','fam:src:B.1.3','fam:src:B.1.4',
    'fam:src:C.1.1','fam:src:C.2.3',
    'ari:C.4.2','ari:C.4.3','ari:C.4.4','ari:C.6.1','ari:C.6.3',
    'ari:C.8.1','ari:C.8.2','ari:C.8.3','ari:C.8.4','ari:C.8.15','push:src:D.4.8',
    'fam:src:A.1.1','fam:src:A.5.1','fam:src:B.2.1','fam:src:B.2.2',
    'fam:src:B.2.3','fam:src:B.3.1','push:src:E.1.2','ari:C.2.1',
    'fam:src:B.4.2','mapsI:src:A.3.1','mapsI:src:A.3.2','mapsI:src:A.3.3',
    'fam:src:F.1.1','I:monodromy-fundamental-set','fam:src:F.2.2',
    'fam:src:F.2.3','fam:src:F.3.1','fam:src:D.1.4','fam:src:D.1.6']
rows = {label:block(label) for label in labels}
a = s.index(r'\hypertarget{outline-I-A}{}')
b = s.index(r'\hypertarget{outline-I-D}{}', a)
ka = s.index(r'\subsection{Known and new}')
kb = s.index(r'\subsection{Methodology}',ka)
data = {'read_after_frozen_utc':freeze['frozen_utc'],
        'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'exposure':'Current global comparison; prior related proofs disclosed. No blind reproof claim.',
        'outlines_ABC':s[a:b], 'literature_status_table':s[ka:kb], 'blocks':rows}
target = OUT / 'S6_SERIES_PUBLISH_I_global_ABC_comparison_intake.json'
if target.exists():
    raise SystemExit('Snapshot already exists; preserve it and create a separate later binding.')
target.write_text(json.dumps(data,indent=2)+'\n')
for label in sys.argv[1:]:
    print('\nLABEL',label,'\n'+rows[label]['text'])
print('\nSNAPSHOT',target, data['source_sha256'])
