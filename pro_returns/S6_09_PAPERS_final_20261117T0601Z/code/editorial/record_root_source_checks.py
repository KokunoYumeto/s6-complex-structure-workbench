"""Persist scoped original-source checks actually performed in the writing.

This script records human-readable audit evidence; it does not verify a theorem.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'deliverables/work/root/references_verified.json'
rows=json.loads(p.read_text())
extra=[
('AtiyahSinger1968IIIE','sources/external/root/retrieved/AtiyahSinger1968IIIE.pdf',
 'Atiyah–Singer (1968), III, printed pp.565–566, formula (4.4), Theorem (4.6)',
 'Original scanned pages visually opened. Compact complex manifold, holomorphic vector bundle and finite group; no Kähler hypothesis. B.4.14 applies to nontrivial roots of unity and then determines the finite Laurent-polynomial C* character.'),
('Pinkham1974Root','sources/external/root/retrieved/Pinkham1974Root.pdf',
 'Pinkham (1974), Remark 7.6(iii), printed pp.45–46; Section 9, pp.63–65',
 'Original text opened. Normal projective cone swept by hyperplanes gives the flat family; degree-eight quadric smoothing component distinguished from the cubic-blowup component. Used as context for the independently written affine construction, not as a global analytic gluing theorem.')]
for key,source,locator,verification in extra:
    rows=[r for r in rows if key not in r.get('keys',[])]
    rows.append({'keys':[key],'locator':locator,'source':source,
                 'source_sha256':hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),
                 'verification':verification,'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026',
                 'status':'verified in the specified scope'})
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Scoped original-source groups:',len(rows))
