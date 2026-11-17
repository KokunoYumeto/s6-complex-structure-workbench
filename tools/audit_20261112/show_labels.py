import io
import json
import os
import re
import sys

rep = json.load(open(sys.argv[1], encoding='utf-8'))
for r in rep:
    name = os.path.basename(r['folder'])
    prompt = io.open(os.path.join(r['folder'], 'PROMPT.md'), encoding='utf-8').read()
    print('=====', name)
    for lab, locs in sorted(r.get('labels', {}).items()):
        # line number the prompt gives right after the label, if any
        m = re.search(re.escape('`' + lab + '`') + r'[^`\n]{0,40}?l\. ?(\d+)', prompt)
        given = m.group(1) if m else ''
        print('  %-45s defined at %s   prompt says l. %s' % (lab, '; '.join('%s:%d' % (f, n) for f, n in locs) or 'NOT DEFINED', given or '-'))
