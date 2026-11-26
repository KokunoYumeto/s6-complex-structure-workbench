#!/usr/bin/env python3
"""State the displayed table's one-based position convention explicitly."""
from hashlib import sha256
from pathlib import Path
import difflib

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_star_logs_receiving'
P='S6_SERIES_PUBLISH_III_02LQ_'
old='These are four $I_3^*$ and eight $I_1^*$ marked positions.'
new='Selected positions in the table are numbered from one.\n'+old
guards={
 'receiving.tex':'577fa535a072e797228d14943c98f871136d5b616f8858f29295723c6526526f',
 'receiving_proof.tex':'bab080e77764812af37031dbc7750099ed7c3d7465a90fb1f0178371687b8fbf'}
for name,expected in guards.items():
    path=LANE/(P+name)
    before=path.read_text()
    assert sha256(path.read_bytes()).hexdigest()==expected
    assert before.count(old)==1
    after=before.replace(old,new)
    path.write_text(after)
    print(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),
          fromfile=name+' before v3',tofile=name+' after v3')),end='')
    print('SHA256',name,sha256(path.read_bytes()).hexdigest(),'LINES',len(after.splitlines()))
assert sha256((LANE/(P+'receiving_statement.tex')).read_bytes()).hexdigest()=='7a2a2f635f67f165cbfac82c0d41885ce7c4dc82cd2f322625c07a58b45a0976'
print('PASS only the one-based position sentence added; theorem and all mathematical maps unchanged')
