"""Size of Pro prompts: Parts words, demanding verbs, parts, numbered items, prompt words, background zip.

Same Parts boundary and verb list as push_rewrite_20261111.py (Longue Marche work tree), extended to the
layouts of the Derivateurs, S6 and CATHOT-expert prompts. Read only; prints a TSV.
"""
import io
import os
import re
import sys
import zipfile

VERBS = r"\b(prove|proves|proved|refute|decide|construct|compute|classify|determine|derive|exhibit|enumerate|tabulate|attack|carry out|write a program|by program|find)\b"
END_MARKERS = ['\n---\n', '\nCONVENTIONS', '\nTHE TEXT YOU ARE GIVEN', '\nTHE MATERIAL YOU ARE GIVEN', '\n## Conventions',
               '\nWHAT IS ATTACHED', '\nRULES OF PROOF', '\n## What is attached', '\n## Rules of proof']


def parts_of(text):
    a = text.index('\n## Parts')
    ends = [text.find(m, a + 5) for m in END_MARKERS]
    ends = [e for e in ends if e > 0]
    b = min(ends) if ends else len(text)
    return text[a + 1:b]


def measure(path):
    t = io.open(path, encoding='utf-8').read()
    p = parts_of(t)
    words = len(re.findall(r'\S+', p))
    verbs = len(re.findall(VERBS, p, flags=re.I))
    parts = len(re.findall(r'^\*\*(?:Part )?[A-H][.)]', p, flags=re.M))
    numbered = len(re.findall(r'(?:^|\s)[A-H]\.?\d+[a-z]?\.(?=\s)', p))  # A.1. or A1.
    lettered = len(re.findall(r'(?:^|\s)\((?:[a-k]|i{1,3}|iv|v|vi{0,3}|ix|x)\)\s', p))
    items = numbered if numbered else lettered
    total_words = len(re.findall(r'\S+', t))
    return dict(parts_words=words, verbs=verbs, parts=parts, numbered=numbered, lettered=lettered, items=items,
                prompt_words=total_words, prompt_bytes=len(t.encode('utf-8')))


def zip_info(folder):
    zs = [f for f in os.listdir(folder) if f.lower().endswith('.zip')] if os.path.isdir(folder) else []
    if not zs:
        return '', '', ''
    z = os.path.join(folder, zs[0])
    with zipfile.ZipFile(z) as zz:
        n = len([i for i in zz.infolist() if not i.filename.endswith('/')])
        unc = sum(i.file_size for i in zz.infolist())
    return '%.1f' % (os.path.getsize(z) / 1e6), str(n), '%.1f' % (unc / 1e6)


def main():
    print('\t'.join(['label', 'parts_words', 'verbs', 'parts', 'items(numbered|lettered)', 'prompt_words',
                     'zip_MB', 'zip_files', 'unzipped_MB']))
    for arg in sys.argv[1:]:
        label, path = arg.split('=', 1)
        m = measure(path)
        zmb, zn, zu = zip_info(os.path.dirname(path))
        print('\t'.join(str(x) for x in [label, m['parts_words'], m['verbs'], m['parts'],
                                          '%d (%d|%d)' % (m['items'], m['numbered'], m['lettered']),
                                          m['prompt_words'], zmb, zn, zu]))


if __name__ == '__main__':
    main()
