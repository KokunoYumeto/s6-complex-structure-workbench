import re, sys, os
# usage: python -I outline.py file1 file2 ...   -> prints sections and statement heads with line numbers
pat = re.compile(r'^\\(?:sub)*section\*?\{|^\\begin\{(?:theorem|proposition|lemma|corollary|definition|conjecture|question|problem|remark|auditrecord)\}|^\\title|^\\begin\{abstract\}')
for f in sys.argv[1:]:
    print('=== ' + os.path.basename(f))
    with open(f, encoding='utf-8', errors='replace') as fh:
        lines = fh.readlines()
    for i, l in enumerate(lines, 1):
        if pat.match(l):
            s = l.rstrip('\n')
            if not s.rstrip().endswith('}') and i < len(lines):
                s += ' ' + lines[i].strip()
            print(f'{i}: {s[:170]}')
