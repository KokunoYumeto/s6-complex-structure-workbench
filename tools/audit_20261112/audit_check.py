"""Mechanical checks of Pro-prompt upload folders (audit of 12 November 2026).

For each upload folder given on the command line:
  - the folder is flat, holds at most 20 files, PROMPT.md and one zip;
  - the zip opens and every member passes its CRC check;
  - MANIFEST.tsv lists exactly the members (name, size, SHA-256);
  - every file the prompt points to is a member; every LaTeX label it names is defined in a member;
  - arXiv numbers named in the prompt: attached or not;
  - neither the prompt nor any member contains the first name, a local path or an e-mail address
    (PDFs: page text, metadata, object dictionaries; other binaries: raw bytes).
Reads only; writes one JSON report next to this script.
Usage: python -I audit_check.py <report_name> <folder> [<folder> ...]
"""
import fnmatch
import hashlib
import io
import json
import os
import re
import sys
import zipfile

import fitz  # PyMuPDF

NAME_RE = re.compile(r'(?i)floris')
WINPATH_RE = re.compile(r'(?<![A-Za-z0-9])[A-Za-z]:(?:\\\\|\\|/)[A-Za-z0-9_.$~-]+(?:\\\\|\\|/)\S*')
PATHFRAG_RE = re.compile(r'(?i)(<DOCS>|<HOME>|\\Users\\|/Users/|/c/Users|AppData|OneDrive|\\Documents\\|Program Files)')
EMAIL_RE = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}')
TEXT_EXT = {'.md', '.tex', '.py', '.txt', '.tsv', '.csv', '.c', '.json', '.bib', '.sty', '.cls', '.log', '.sage',
            '.m', '.g', '.gap', '.sh', '.ps1', '.yaml', '.yml', '.html', '.xml', '.out', '.toml', '.ini', '.cfg'}
PATH_PREFIXES = None  # computed from zip top-level folders


def ctx(s, i, j, w=60):
    a = max(0, i - w)
    b = min(len(s), j + w)
    return s[a:b].replace('\n', ' ')


def scan_text(label, s, out):
    for rx, kind in ((NAME_RE, 'first_name'), (WINPATH_RE, 'windows_path'), (PATHFRAG_RE, 'path_fragment'),
                     (EMAIL_RE, 'email')):
        for m in rx.finditer(s):
            out.append({'where': label, 'kind': kind, 'match': m.group(0)[:120], 'context': ctx(s, m.start(), m.end())})


def scan_pdf(label, data, out):
    try:
        doc = fitz.open(stream=data, filetype='pdf')
    except Exception as e:  # noqa
        out.append({'where': label, 'kind': 'pdf_open_error', 'match': str(e)[:200], 'context': ''})
        return
    meta = doc.metadata or {}
    scan_text(label + ' [metadata]', json.dumps(meta, ensure_ascii=False), out)
    for xref in range(1, doc.xref_length()):
        try:
            obj = doc.xref_object(xref, compressed=False)
        except Exception:
            continue
        if obj:
            for rx, kind in ((NAME_RE, 'first_name'), (WINPATH_RE, 'windows_path'), (PATHFRAG_RE, 'path_fragment')):
                for m in rx.finditer(obj):
                    out.append({'where': label + ' [xref %d]' % xref, 'kind': kind, 'match': m.group(0)[:120],
                                'context': ctx(obj, m.start(), m.end())})
    for pno in range(doc.page_count):
        try:
            t = doc[pno].get_text()
        except Exception:
            continue
        scan_text(label + ' [p.%d]' % (pno + 1), t, out)
    # raw bytes (uncompressed parts)
    raw = data.decode('latin-1')
    for rx, kind in ((NAME_RE, 'first_name'),):
        for m in rx.finditer(raw):
            out.append({'where': label + ' [raw]', 'kind': kind, 'match': m.group(0), 'context': ctx(raw, m.start(), m.end(), 30)})


def check_folder(folder):
    rep = {'folder': folder, 'problems': [], 'notes': []}
    files = sorted(os.listdir(folder))
    subdirs = [f for f in files if os.path.isdir(os.path.join(folder, f))]
    rep['files'] = files
    if subdirs:
        rep['problems'].append('not flat: subfolders %s' % subdirs)
    if len(files) > 20:
        rep['problems'].append('more than 20 files: %d' % len(files))
    zips = [f for f in files if f.lower().endswith('.zip')]
    if 'PROMPT.md' not in files:
        rep['problems'].append('no PROMPT.md')
    if len(zips) != 1:
        rep['problems'].append('zips in folder: %s' % zips)
    others = [f for f in files if f not in ('PROMPT.md',) and f not in zips]
    if others:
        rep['notes'].append('other files in upload folder: %s' % others)
    prompt = io.open(os.path.join(folder, 'PROMPT.md'), encoding='utf-8').read()
    rep['prompt_bytes'] = len(prompt.encode('utf-8'))
    name = os.path.basename(folder.rstrip('\\/'))
    if zips and zips[0] != name + '_background.zip':
        rep['notes'].append('zip name %s differs from <folder>_background.zip' % zips[0])
    privacy = []
    scan_text('PROMPT.md', prompt, privacy)
    if not zips:
        rep['privacy'] = privacy
        return rep
    zpath = os.path.join(folder, zips[0])
    rep['zip_bytes'] = os.path.getsize(zpath)
    z = zipfile.ZipFile(zpath)
    bad = z.testzip()
    if bad:
        rep['problems'].append('CRC failure at %s' % bad)
    infos = z.infolist()
    names = [i.filename for i in infos]
    dirs = [n for n in names if n.endswith('/')]
    members = [n for n in names if not n.endswith('/')]
    if len(set(members)) != len(members):
        rep['problems'].append('duplicate member names')
    rep['n_members'] = len(members)
    data = {n: z.read(n) for n in members}
    # manifest
    if 'MANIFEST.tsv' not in data:
        rep['problems'].append('no MANIFEST.tsv at zip root')
        man_rows = []
    else:
        man_text = data['MANIFEST.tsv'].decode('utf-8')
        lines = [l for l in man_text.split('\n') if l.strip()]
        header = lines[0].split('\t')
        rep['manifest_header'] = header
        man_rows = [dict(zip(header, l.split('\t'))) for l in lines[1:]]
        pcol = header[0]
        bcol = next((h for h in header if h.lower() in ('bytes', 'size', 'size_bytes')), None)
        scol = next((h for h in header if 'sha' in h.lower()), None)
        listed = [r[pcol] for r in man_rows]
        actual = [n for n in members if n != 'MANIFEST.tsv']
        miss_in_zip = sorted(set(listed) - set(actual))
        miss_in_man = sorted(set(actual) - set(listed))
        if miss_in_zip:
            rep['problems'].append('listed in MANIFEST but not in zip: %s' % miss_in_zip)
        if miss_in_man:
            rep['problems'].append('in zip but not listed in MANIFEST: %s' % miss_in_man)
        if len(set(listed)) != len(listed):
            rep['problems'].append('duplicate rows in MANIFEST')
        mism = []
        for r in man_rows:
            p = r[pcol]
            if p not in data:
                continue
            if bcol and str(len(data[p])) != r[bcol].strip():
                mism.append('%s size %s vs %d' % (p, r[bcol], len(data[p])))
            if scol and hashlib.sha256(data[p]).hexdigest() != r[scol].strip().lower():
                mism.append('%s sha256 mismatch' % p)
        if mism:
            rep['problems'].append('manifest mismatches: %s' % mism)
        empty_why = [r[pcol] for r in man_rows if any('why' in h.lower() for h in header)
                     and not r.get(next(h for h in header if 'why' in h.lower()), '').strip()]
        if empty_why:
            rep['notes'].append('manifest rows without a reason: %s' % empty_why)
        rep['manifest_rows'] = len(man_rows)
    # pointers
    tops = sorted({n.split('/')[0] for n in members if '/' in n})
    rep['zip_top_folders'] = tops
    toks = set(re.findall(r'`([^`\n]+)`', prompt))
    path_re = re.compile(r'(?<![\w/.-])((?:%s)/[^\s`,;:)()\]]+)' % '|'.join(re.escape(t) for t in tops)) if tops else None
    bare = set(path_re.findall(prompt)) if path_re else set()
    cited_paths = set()
    for t in toks | bare:
        t2 = t.strip().rstrip('.')
        if '/' in t2 and t2.split('/')[0] in tops:
            cited_paths.add(t2)
        elif re.fullmatch(r'[\w.\-]+\.(md|tex|pdf|tsv|csv|py|txt|zip|bib|json)', t2):
            cited_paths.add(t2)
    resolved, unresolved = [], []
    for c in sorted(cited_paths):
        if c.startswith(name + '_') or c.startswith('<ID>_'):
            continue  # a deliverable of the run, not an attachment
        if c.endswith('/'):
            hits = [m for m in members if m.startswith(c)]
        elif '*' in c:
            hits = [m for m in members if fnmatch.fnmatch(m, c)]
        else:
            hits = [m for m in members if m == c]
            if not hits and '/' not in c:
                hits = [m for m in members if m.split('/')[-1] == c]
        (resolved if hits else unresolved).append(c)
    rep['cited_paths_resolved'] = resolved
    if unresolved:
        rep['problems'].append('prompt points to files not in zip: %s' % unresolved)
    # labels
    labels_def = {}
    for n in members:
        if os.path.splitext(n)[1].lower() == '.tex':
            s = data[n].decode('utf-8', errors='replace')
            for i, line in enumerate(s.split('\n'), 1):
                for m in re.finditer(r'\\label\{([^}]+)\}', line):
                    labels_def.setdefault(m.group(1), []).append((n, i))
    lab_toks = [t for t in toks if re.fullmatch(r'[A-Za-z0-9]+(?::[A-Za-z0-9\-_.]+)+', t) or
                (re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+){2,}', t) and '/' not in t)]
    lab_res = {}
    for t in sorted(set(lab_toks)):
        lab_res[t] = labels_def.get(t, [])
    rep['labels'] = {k: v for k, v in lab_res.items()}
    missing_labels = [k for k, v in lab_res.items() if not v]
    if missing_labels:
        rep['notes'].append('label-like tokens not defined by \\label in any .tex member: %s' % missing_labels)
    # arXiv numbers
    arx = set(re.findall(r'arXiv:\s?((?:\d{4}\.\d{4,5})|(?:math/\d{7}))', prompt))
    arx |= set(re.findall(r'arXiv\s+((?:\d{4}\.\d{4,5}))', prompt))
    arx |= set(re.findall(r'(?<![\d.])(\d{4}\.\d{5})(?:v\d)?(?![\d])', prompt))
    att, notatt = [], []
    for a in sorted(arx):
        key = a.replace('/', '_')
        (att if any(key in m for m in members) else notatt).append(a)
    rep['arxiv_attached'] = att
    rep['arxiv_named_not_attached'] = notatt
    # privacy scan of members
    for n in members:
        ext = os.path.splitext(n)[1].lower()
        b = data[n]
        if ext == '.pdf':
            scan_pdf(n, b, privacy)
        elif ext in TEXT_EXT or b[:4096].count(b'\x00') == 0:
            try:
                s = b.decode('utf-8')
            except UnicodeDecodeError:
                s = b.decode('latin-1')
            scan_text(n, s, privacy)
        else:
            raw = b.decode('latin-1')
            for m in NAME_RE.finditer(raw):
                privacy.append({'where': n + ' [raw]', 'kind': 'first_name', 'match': m.group(0),
                                'context': ctx(raw, m.start(), m.end(), 30)})
    rep['privacy'] = privacy
    rep['members'] = [(i.filename, i.file_size) for i in infos]
    return rep


def main():
    report_name = sys.argv[1]
    out = [check_folder(f) for f in sys.argv[2:]]
    here = os.path.dirname(os.path.abspath(__file__))
    with io.open(os.path.join(here, report_name), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for r in out:
        kinds = {}
        for p in r.get('privacy', []):
            kinds[p['kind']] = kinds.get(p['kind'], 0) + 1
        print('==', r['folder'])
        print('   files:', r['files'], ' members:', r.get('n_members'), ' manifest rows:', r.get('manifest_rows'),
              ' zip MB: %.2f' % (r.get('zip_bytes', 0) / 1e6))
        print('   problems:', r['problems'] or 'none')
        print('   notes:', r['notes'] or 'none')
        print('   arXiv named, not attached:', r.get('arxiv_named_not_attached'))
        print('   privacy hits by kind:', kinds or 'none')


if __name__ == '__main__':
    main()
