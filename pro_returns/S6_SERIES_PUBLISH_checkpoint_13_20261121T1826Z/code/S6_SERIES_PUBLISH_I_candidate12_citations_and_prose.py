"""Apply source-read citation guards and fully compared topology prose exactly once."""
import datetime, hashlib, json, re
from pathlib import Path
from S6_SERIES_PUBLISH_editing import Editor

ROOT = Path(__file__).resolve().parents[1]
sha = lambda b: hashlib.sha256(b).hexdigest()
ed = Editor('I')
source_before = sha(ed.before.encode())
applied = []
packages = [
    ('agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_locator_guards.json', 'changes'),
    ('agents/i_marking/S6_SERIES_PUBLISH_I_heegner_citation_guards.json', 'changes'),
    ('agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_bibliography_guards.json', 'changes'),
    ('agents/i_topology/editorial/S6_SERIES_PUBLISH_I_candidate11_prose_guards.json', 'patches'),
]
for name, key in packages:
    p = ROOT / name
    data = json.loads(p.read_text())
    for g in data[key]:
        kind = 'D18'
        ids = g.get('statement_ids', [])
        if key == 'patches':
            kind = ('D20' if g.get('proof_change') else 'D16' if g['old'].startswith('[')
                    else 'D06' if g['id'].endswith(('-59', '-60', '-61')) else 'D02')
        ed.replace(g['old'], g['new'], kind, g['reason'], ','.join(ids), count=g.get('count', 1))
    applied.append({'file': name, 'sha256': sha(p.read_bytes()), 'guards': len(data[key])})

# The added Drinfeld entry belongs between Douady and Du in the alphabetized list.
m = re.search(r'\\bibitem\[Drinfeld\(1973\)\]\{Drinfeld1973\}.*?(?=\\bibitem)', ed.text, re.S)
assert m
entry = m.group(0)
ed.replace(entry, '', 'D18', 'Move the newly cited Drinfeld entry to its alphabetical position.')
anchor = re.search(r'\\bibitem\[Du et~al\..*?\]\{DuEtAl2026v1\}', ed.text).group(0)
ed.replace(anchor, entry + anchor, 'D18', 'Place Drinfeld after Douady and before Du; entry content unchanged.')
ed.replace(r'\citet[Corollary~2]{reyssat1982weierstrass}',
           r'\citet[Corollary~2, p.~292]{reyssat1982weierstrass}',
           'D18', 'Exact published locator read in the cached primary PDF text; direct PDF fetch was blocked. Text-only source access is recorded without a page-image claim.',
           'I:Gaussian-comparison')

bibpath = ROOT / 'S6_SERIES_PUBLISH_references.bib'
bib_before = bibpath.read_text()
bib = bib_before
shared = []
for name in [
    'agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_shared_bib_guards.json',
    'agents/i_marking/S6_SERIES_PUBLISH_I_heegner_shared_bib_guards.json',
    'agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_shared_bibliography_tail_guards.json',
]:
    p = ROOT / name
    data = json.loads(p.read_text())
    for g in data['changes']:
        assert bib.count(g['old']) == g.get('count', 1), g['id']
        bib = bib.replace(g['old'], g['new'])
        shared.append({'id': g['id'], 'old': g['old'], 'new': g['new'], 'reason': g['reason']})
    applied.append({'file': name, 'sha256': sha(p.read_bytes()), 'guards': len(data['changes'])})
needle = '  current_run_locator = {Section 1, unnumbered theorem, p.83, original Russian edition; actual rendered statement and proof read on 21 November 2026; no English-page reading claimed}'
assert bib.count(needle) == 1
bib = bib.replace(needle, '  verification = {verified at listed scope},\n' + needle)
key = '@article{reyssat1982weierstrass,\n'
assert bib.count(key) == 1
bib = bib.replace(key, key + '  current_run_locator = {Corollary2, published p.292; its proof Section5.1, p.301. Root read cached primary-PDF text through the search service on21November2026. Direct downloads returned403; no actual PDF/page-image reading is claimed in this run.},\n')
ed.save()
bibpath.write_text(bib)
receipt = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_before_sha256': source_before,
    'source_after_sha256': sha(ed.text.encode()),
    'packages': applied,
    'shared_bibliography_before_sha256': sha(bib_before.encode()),
    'shared_bibliography_after_sha256': sha(bib.encode()),
    'shared_bibliography_changes': shared,
    'new_mathematical_events': 0,
    'scope': 'Citation and edition checks, root reading of every guarded new passage, and delegated complete topology proof comparisons. Existing exposed B4.26 event is reused; no independent or computational credit added.',
}
(ROOT / 'records/S6_SERIES_PUBLISH_I_candidate12_citations_and_prose_applied.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'source_after_sha256': receipt['source_after_sha256'], 'packages': len(applied), 'source_edits': len(ed.rows), 'shared_guards': len(shared)}))
