#!/usr/bin/env python3
"""Prepare ten metadata dispositions and nine unapplied exact bibliography guards.

Inputs are the frozen candidate17 source, infra's inventory, and our primary
metadata file. No source, log, ledger, shared provenance, or deposit file is written.
"""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'S6_SERIES_PUBLISH_I.tex'
INVENTORY = ROOT / 'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_inventory.json'
METADATA = OUT / 'S6_SERIES_PUBLISH_I_candidate17_bibliography_primary_metadata.json'
EXPECTED_SOURCE = '5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
KEYS = ['agboola2006', 'bertolin2022', 'bost2009', 'callSilverman1993',
        'Cartan1952B_AB', 'CrCremonaSiksek2006', 'demarco2017', 'Gauduchon1985',
        'Grauert1963ErratumD', 'CrJetchev2008']

def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()

def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def replace_once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new, 1)

def add_doi(text, doi):
    return replace_once(text, '\\newblock URL', '\\newblock \\doi{' + doi + '}.\n\n\\newblock URL')

source_bytes = SOURCE.read_bytes()
assert sha(source_bytes) == EXPECTED_SOURCE, 'Canonical source is no longer frozen candidate17.'
source = source_bytes.decode()
inventory = json.loads(INVENTORY.read_text())
assert inventory['source_sha256'] == EXPECTED_SOURCE
originals = {row['key']: row for row in inventory['entries']}
metadata = {row['key']: row for row in json.loads(METADATA.read_text())}
assert list(metadata) == KEYS
review = OUT / 'candidate17_bibliography_entries'
review.mkdir(exist_ok=True)
rows = []
guards = []
proposed_source = source
for index, key in enumerate(KEYS, 1):
    inv = originals[key]
    before = inv['original_entry']
    assert sha(before) == inv['entry_sha256'], key
    assert source.count(before) == 1, key
    after = before
    if metadata[key]['doi']:
        after = add_doi(after, metadata[key]['doi'])
    if key == 'bertolin2022':
        after += '\n\n\\newblock The cited version is arXiv:2010.15170v2, 15 November 2022; page and statement references use that version.'
    elif key == 'bost2009':
        after = replace_once(after,
            r"\newblock \emph{Ast{\'e}risque}, 327:\penalty0 361--424, 2009.",
            r"\newblock In \emph{From probability to geometry (I)---Volume in honor of the 60th birthday of Jean-Michel Bismut}, number 327 of \emph{Ast{\'e}risque}, pages 361--424. Soci{\'e}t{\'e} math{\'e}matique de France, 2009.")
    elif key == 'Cartan1952B_AB':
        after = replace_once(after,
            r"\newblock \emph{S{\'e}minaire Henri Cartan}, 4:\penalty0 1--15, 1952.",
            r"\newblock \emph{S{\'e}minaire Henri Cartan}, volume 4 (1951--1952), expos{\'e} 19, pages 1--15. Secr{\'e}tariat math{\'e}matique, Paris, 1952.")
    elif key == 'demarco2017':
        after = replace_once(after, 'https://arxiv.org/pdf/1701.07947', 'https://arxiv.org/pdf/1701.07947v2')
        after += '\n\n\\newblock The cited version is arXiv:1701.07947v2, 2 March 2017; page and statement references use that version.'
    elif key == 'Gauduchon1985':
        after = replace_once(after,
            r"\newblock \emph{Ast\'erisque}, 126:\penalty0 129--135, 1985.",
            r"\newblock In \emph{G{\'e}om{\'e}trie des surfaces K3: modules et p{\'e}riodes---S{\'e}minaire Palaiseau}, number 126 of \emph{Ast\'erisque}, pages 129--135. Soci{\'e}t{\'e} math{\'e}matique de France, 1985.")
    elif key == 'CrJetchev2008':
        after = replace_once(after, 'Jetchev et~al.(2008)', 'Jetchev et~al.(2009)')
        after = replace_once(after,
            r'\newblock \emph{Journal of Number Theory}, 128:\penalty0 3394--3410, 2008.',
            r'\newblock \emph{Journal of Number Theory}, 129\penalty0 (2):\penalty0 284--302, 2009.')

    # Exact bibliography keys, author/title text, and linked editions are retained.
    assert '\\bibitem' in before and '\\bibitem' in after
    key_pattern = re.compile(r'\\bibitem\[[\s\S]*?\]\{([^}]+)\}')
    assert key_pattern.search(before).group(1) == key_pattern.search(after).group(1) == key
    before_parts = before.split('\\newblock')
    after_parts = after.split('\\newblock')
    assert before_parts[1] == after_parts[1], (key, 'title changed')
    author_before = before_parts[0].split('\n', 1)[1]
    author_after = after_parts[0].split('\n', 1)[1]
    assert author_before == author_after, (key, 'author text changed')
    urls_before = re.findall(r'\\url\{([^}]+)\}', before)
    urls_after = re.findall(r'\\url\{([^}]+)\}', after)
    expected_urls = [url + 'v2' if key == 'demarco2017' and url == 'https://arxiv.org/pdf/1701.07947' else url for url in urls_before]
    assert urls_after == expected_urls, (key, 'unexpected URL change')
    assert [x for x in before_parts if 'The cited version is ' in x or 'The linked author version ' in x] == [x for x in after_parts if ('The cited version is ' in x or 'The linked author version ' in x) and x in before_parts]
    assert re.findall(r'\$[^$]+\$', before) == re.findall(r'\$[^$]+\$', after), (key, 'bibliography inline math changed')

    p_before = review / (key + '_before.tex')
    p_after = review / (key + '_proposed.tex')
    p_diff = review / (key + '.diff')
    p_before.write_text(before + '\n')
    p_after.write_text(after + '\n')
    p_diff.write_text(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile=key + '_before', tofile=key + '_proposed')))
    changed = before != after
    row = {
        'index': index, 'key': key, 'type': 'D18', 'source_line': inv['start_line'],
        'source_sha256': EXPECTED_SOURCE, 'original_entry_sha256': sha(before),
        'proposed_entry_sha256': sha(after), 'changed': changed,
        'status': 'proposed, not applied' if changed else 'verified current entry; no change proposed',
        'before': before, 'after': after, 'metadata_and_evidence': metadata[key],
        'review_files': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in (p_before, p_after, p_diff)},
        'citation_key_preserved': True, 'authors_and_title_preserved': True,
        'supplied_edition_notes_preserved': True,
        'mathematical_events_added': 0, 'full_page_reading_credit_added': 0,
        'proof_reading_credit_added': 0,
    }
    if changed:
        row['id'] = f'I17-prov-bib-{len(guards)+1:02d}'
        guards.append({
            'id': row['id'], 'key': key, 'type': 'D18', 'line': inv['start_line'],
            'before': before, 'after': after, 'reason': metadata[key]['change'],
            'source_sha256': EXPECTED_SOURCE, 'original_entry_sha256': sha(before),
            'proposed_entry_sha256': sha(after), 'status': 'proposed, not applied',
            'primary_evidence': metadata[key]['primary'],
            'mathematical_events_added': 0, 'full_page_reading_credit_added': 0,
        })
        proposed_source = replace_once(proposed_source, before, after)
    rows.append(row)

assert len(rows) == 10 and len(guards) == 9
assert sum(row['metadata_and_evidence']['doi'] is not None for row in rows) == 6
assert source.split('\\begin{thebibliography}', 1)[0] == proposed_source.split('\\begin{thebibliography}', 1)[0]
assert re.findall(r'\\bibitem\[[\s\S]*?\]\{([^}]+)\}', source) == re.findall(r'\\bibitem\[[\s\S]*?\]\{([^}]+)\}', proposed_source)
crossref = ROOT / 'agents/continuation_infra/candidate17_bibliography_audit/demarco2017_crossref.json'
assert sha(crossref.read_bytes()) == '9e08a832acd8a04bf40830effde3672ac42c6e04fb2827d1594371a127d350e7'
doi_record = json.loads(crossref.read_text())['message']
assert (doi_record['DOI'], doi_record['volume'], doi_record['issue'], doi_record['page']) == ('10.1353/ajm.2020.0012', '142', '2', '443-473')

entries_path = OUT / 'S6_SERIES_PUBLISH_I_candidate17_bibliography_entry_proposals.json'
guards_path = OUT / 'S6_SERIES_PUBLISH_I_candidate17_bibliography_guards.json'
dump(entries_path, rows)
dump(guards_path, guards)
receipt = {
    'prepared_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Ten assigned Paper I bibliography entries: primary-source metadata only.',
    'input_sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in (SOURCE, INVENTORY, METADATA, crossref)},
    'output_sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in (entries_path, guards_path)},
    'script_sha256': sha(Path(__file__).read_bytes()),
    'entries_checked': 10, 'changed_entry_proposals': 9, 'new_verified_dois': 6,
    'unchanged_verified_entry': 'callSilverman1993',
    'key_order_preserved': True, 'authors_and_titles_preserved': True,
    'all_nonbibliography_source_bytes_preserved_in_proposed_concatenation': True,
    'canonical_source_written': False, 'canonical_source_sha256_after': sha(SOURCE.read_bytes()),
    'mathematical_events_added': 0, 'full_page_reading_credit_added': 0,
    'proof_reading_credit_added': 0,
    'limits': [
        'This receipt covers metadata, exact original-entry matches, and proposed bibliography text; it does not certify the mathematical content of the cited works.',
        'Four entries have no DOI field in the opened primary archive record, and no exact DOI was found in the bounded title/author publisher/archive searches. This is not an assertion that no DOI exists.',
        'Publisher search receipts are identified as such. Failed direct publisher opens are not recorded as successful document opens.',
        'The proposed bibliography has not yet been applied or rendered; parent integration and final PDF reading remain required.'
    ]
}
assert receipt['canonical_source_sha256_after'] == EXPECTED_SOURCE
receipt_path = OUT / 'S6_SERIES_PUBLISH_I_candidate17_bibliography_receipt.json'
dump(receipt_path, receipt)
md = ['# Paper I candidate17: ten-entry primary metadata audit', '',
      'All ten assigned entries were checked against the primary records named in the metadata file. Nine exact entry proposals are unapplied; Call–Silverman is retained verbatim. This work adds no mathematical events, proof-reading credit, or full-page reading credit.', '',
      '| Key | Disposition | DOI |', '|---|---|---|']
for row in rows:
    m = row['metadata_and_evidence']
    md.append(f"| `{row['key']}` | {m['change']} | {m['doi'] or 'No exact DOI found in the bounded primary check'} |")
md += ['', 'The Jetchev–Lauter–Stein publisher record gives Journal of Number Theory **129(2) (2009), 284–302**. The existing citation key and arXiv:0707.0032v1 note are retained; the author-date label changes to 2009. Bertolin’s supplied v2 edition is dated 15 November 2022. DeMarco–Mavraki’s body citations identify v2, dated 2 March 2017; its URL is pinned accordingly.', '',
       'The four bounded DOI searches without an exact result are Bost–Künnemann, Call–Silverman, Cartan and Gauduchon. Their publication records are positively verified. No global DOI-absence or nonpublication claim is made.', '',
       f"Source SHA-256: `{EXPECTED_SOURCE}`", '',
       f"Guards SHA-256: `{sha(guards_path.read_bytes())}`", '',
       f"Entries SHA-256: `{sha(entries_path.read_bytes())}`", '',
       f"Receipt SHA-256: `{sha(receipt_path.read_bytes())}`", '']
(OUT / 'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit.md').write_text('\n'.join(md))
print(json.dumps({'entries': len(rows), 'guards': len(guards), 'new_dois': 6,
                  'sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in (METADATA, entries_path, guards_path, receipt_path)}}, indent=2))
