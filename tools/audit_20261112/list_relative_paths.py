"""Count relative local paths (work\\..., LW\\..., repo\\...) in the text members of the given zips (read only)."""
import collections
import re
import sys
import zipfile

PAT = re.compile(r'(?<![A-Za-z0-9_])(work|repo|LW)\\[A-Za-z0-9_.*<>\\-]+')
for zp in sys.argv[1:]:
    z = zipfile.ZipFile(zp)
    c = collections.Counter()
    ex = {}
    for i in z.infolist():
        if not i.filename.endswith(('.md', '.tex', '.py', '.txt', '.c')):
            continue
        s = z.read(i).decode('utf-8', 'replace')
        for m in PAT.finditer(s):
            c[(i.filename, m.group(1))] += 1
            ex.setdefault((i.filename, m.group(1)), m.group(0))
    print('==', zp.split('\\')[-1])
    for k, v in sorted(c.items()):
        print('   %-32s %-5s %3d   e.g. %s' % (k[0], k[1], v, ex[k][:90]))
