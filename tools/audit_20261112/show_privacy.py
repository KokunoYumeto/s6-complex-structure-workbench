import collections
import json
import os
import sys

rep = json.load(open(sys.argv[1], encoding='utf-8'))
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 4
for r in rep:
    print('=====', os.path.basename(r['folder']))
    g = collections.defaultdict(list)
    for p in r['privacy']:
        base = p['where'].split(' [')[0]
        g[(base, p['kind'])].append(p)
    for (base, kind), lst in sorted(g.items()):
        uniq = collections.OrderedDict()
        for p in lst:
            uniq.setdefault(p['match'], (p['where'], p['context']))
        print('  %-70s %-14s n=%d' % (base, kind, len(lst)))
        for m, (w, c) in list(uniq.items())[:limit]:
            print('       %r @%s :: %s' % (m[:80], w.split(' [')[-1] if ' [' in w else '', c[:170]))
