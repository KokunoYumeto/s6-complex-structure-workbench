import json, collections, os, sys
base = r"C:\Users\user\Documents\math\research\s6_recent_results_main\related_sources"
BS = chr(92)
for sid in sorted(os.listdir(base)):
    d = json.load(open(os.path.join(base, sid, 'UNIQUE_TEXT_SOURCES.json'), encoding='utf-8'))
    print('=====', sid, len(d))
    c = collections.Counter()
    ext = collections.Counter()
    for it in d:
        m = it['members'][0].replace(BS, '/')
        parts = m.split('/')
        key = '/'.join(parts[:int(sys.argv[1]) if len(sys.argv) > 1 else 9])
        c[key] += 1
        ext[os.path.splitext(it['corpus_file'])[1]] += 1
    for k, v in c.most_common(40):
        print(v, k)
    print(dict(ext))
