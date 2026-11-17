"""List every line of the text members of the given zips that holds a sanitized local path (read only)."""
import re
import sys
import zipfile

PAT = re.compile(r'<DOCS>|<HOME>|work\\\\scratch|work\\\\[A-Za-z0-9]+_notes|repo\\\\s6')
seen = {}
for zp in sys.argv[1:]:
    z = zipfile.ZipFile(zp)
    for i in z.infolist():
        if not i.filename.endswith(('.md', '.tex', '.py', '.txt', '.c', '.tsv')):
            continue
        s = z.read(i).decode('utf-8', 'replace')
        for ln, line in enumerate(s.split('\n'), 1):
            if PAT.search(line):
                key = (i.filename, ln)
                if key not in seen:
                    seen[key] = line.strip()
for (f, ln), line in sorted(seen.items()):
    print('%s:%d: %s' % (f, ln, line[:260]))
