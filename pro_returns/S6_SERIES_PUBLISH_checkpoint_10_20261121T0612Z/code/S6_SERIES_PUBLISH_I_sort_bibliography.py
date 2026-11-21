from pathlib import Path
import re, json, hashlib, datetime
from S6_SERIES_PUBLISH_editing import Editor

r = Path(__file__).resolve().parents[1]
ed = Editor('I')
a = ed.text.index(r'\begin{thebibliography}')
b = ed.text.index(r'\end{thebibliography}', a)
segment = ed.text[a:b]
matches = list(re.finditer(r'\\bibitem\[(.*?)\]\{([^}]+)\}', segment, re.S))
entries = {m[2]: segment[m.start():matches[i+1].start() if i+1 < len(matches) else len(segment)] for i,m in enumerate(matches)}
headers = {m[2]: m[1] for m in matches}
cited = set()
for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', ed.text[:a]):
    cited.update(x.strip() for x in m[1].split(','))
remove = ['BiliottiGhigi2021Root','Doi2009Root','Fujimoto1988Root','Johansson2016','KamenovaToriRoot','KatzarkovEtAl2025Root','Meersseman2011Root','Nakayama2002Root','PythonFlint2026']
assert not set(remove) & cited
assert len(entries) == 124
removed = {k: entries[k] for k in remove}
for key in remove:
    ed.replace(entries[key], '', 'D16', 'Remove an entry with no citation anywhere in the current paper, including hidden dependency records; retain the exact entry in the bibliography disposition and the shared references file.', key)

def key(k):
    h = headers[k]
    author = h.split('(')[0].split(',')[0]
    author = re.split(r'\s+and\s+|\s+et~al\.', author)[0]
    author = author.replace(r'\L{}', 'L').replace(r'\l', 'l')
    author = re.sub(r'\\[uc]\s*', '', author)
    author = re.sub(r'[^A-Za-z]', '', author).lower()
    year = re.search(r'(?:19|20)\d\d', h)
    return (author, int(year[0]) if year else 9999, h, k)

a = ed.text.index(r'\begin{thebibliography}')
b = ed.text.index(r'\end{thebibliography}', a)
current = ed.text[a:b]
prefix = segment[:matches[0].start()]
ordered = sorted((k for k in entries if k not in remove), key=key)
new = prefix + ''.join(entries[k] for k in ordered)
ed.replace(current, new, 'D16', 'Order the remaining bibliography by first author and year. The exact bytes of every retained entry are preserved; preprint and journal edition records remain distinct where no verified pagination map has been established.')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_bibliography_disposition.json').write_text(json.dumps({
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
    'old_order': [m[2] for m in matches], 'new_order': ordered,
    'sort_keys': {k: key(k) for k in ordered},
    'retained_entry_sha256': {k: hashlib.sha256(entries[k].encode()).hexdigest() for k in ordered},
    'removed_uncited_entries': removed,
    'exact_entry_bytes_preserved': True,
    'edition_scope': 'BM95AB and BM97 retain their separate preprint/journal records. Operative Chapter I locators identify the preprint explicitly; no edition equivalence is asserted.'
}, indent=2, ensure_ascii=False)+'\n')
