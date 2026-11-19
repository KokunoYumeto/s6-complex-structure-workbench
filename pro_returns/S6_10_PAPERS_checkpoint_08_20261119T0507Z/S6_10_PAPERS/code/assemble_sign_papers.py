"""Arrange II/VI draft fragments for reader order; no mathematical certification."""
from pathlib import Path
from fix_verified_legacy_locators import fix_legacy_locators
ROOT=Path(__file__).resolve().parents[1]
for paper in ('II','VI'):
    d=ROOT/'papers'/paper
    s=(d/'body_source.tex').read_text()
    if paper=='II':
        cut=s.index('\\section{Global CDP replacement')
        s=s[:cut]+(d/'body_night.tex').read_text()+s[cut:]
        cut=s.index('\\section{The remaining splitting problem}')
        s=s[:cut]+(d/'lr_cover.tex').read_text()+s[cut:]
    s=s.replace('% BEGIN GENERATED RESULT INDEX','')
    (d/'body.tex').write_text(fix_legacy_locators(s, 'assemble_sign_papers.'+paper)[0])
print('Assembled II and VI. Historical and current proof-review scopes remain separate.')
