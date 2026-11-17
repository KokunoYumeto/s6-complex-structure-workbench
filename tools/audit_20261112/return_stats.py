"""Statement counts and status mix of returned answers (read only, from the answer zips)."""
import csv
import io
import os
import re
import sys
import zipfile
from collections import Counter

ANS = r'C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers'
for n in sys.argv[1:]:
    z = zipfile.ZipFile(os.path.join(ANS, n))
    names = [i.filename for i in z.infolist()]
    res = [x for x in names if re.search(r'_results\.csv$', x) and 'readings' not in x]
    rep = [x for x in names if re.search(r'_report\.md$', x)]
    print('==', n, '| results files:', res[:4], '| report:', rep[:2])
    for r in res[:1]:
        txt = z.read(r).decode('utf-8', 'replace')
        rows = list(csv.DictReader(io.StringIO(txt)))
        st = Counter((row.get('status') or '').strip().split(' ')[0].split('(')[0] for row in rows)
        print('   rows:', len(rows), dict(st))
    for r in rep[:1]:
        txt = z.read(r).decode('utf-8', 'replace')
        unf = len(re.findall(r'(?i)unfinished', txt))
        print('   report words:', len(txt.split()), '| "unfinished" mentions:', unf)
    tex = sum(len(z.read(x).decode('utf-8', 'replace').split()) for x in names if x.endswith('.tex'))
    code = len([x for x in names if x.startswith(tuple(p + 'code/' for p in ('', names[0].split('/')[0] + '/'))) and not x.endswith('/')])
    print('   tex words (all .tex):', tex, '| code files:', code)
