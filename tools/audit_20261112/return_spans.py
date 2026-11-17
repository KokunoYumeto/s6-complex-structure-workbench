"""Working-time spans of returned Pro answers, from the entry timestamps of their zips (read only)."""
import datetime as dt
import os
import sys
import zipfile

ANS = r'C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers'
NAMES = sys.argv[1:] or ['CATHOT.zip', 'TOTASPH.zip', 'POLES.zip', 'GALOIS.zip', 'STRATA.zip', 'PATHS.zip',
                         'BISITE.zip', 'RESIDUE.zip', 'LM3_TEICHMULLER_TOWER_2026-11-11.zip',
                         'LM3b_TEICHMULLER_PUSH.zip', 'LM2_LOOP_EQUATIONS.zip']
for n in NAMES:
    p = os.path.join(ANS, n)
    if not os.path.isfile(p):
        print('%-40s missing' % n)
        continue
    z = zipfile.ZipFile(p)
    infos = [i for i in z.infolist() if not i.filename.endswith('/')]
    times = sorted(dt.datetime(*i.date_time) for i in infos)
    # drop the 1980 default stamp if present
    real = [t for t in times if t.year > 2000]
    span = (real[-1] - real[0]).total_seconds() / 60 if real else float('nan')
    # largest gap, to see whether early files are leftovers
    gaps = sorted(((real[k + 1] - real[k]).total_seconds() / 60, real[k], real[k + 1]) for k in range(len(real) - 1))[-2:]
    tex_words = 0
    for i in infos:
        if i.filename.endswith('.tex') and 'paper' in i.filename.lower():
            try:
                tex_words += len(z.read(i).decode('utf-8', 'replace').split())
            except Exception:
                pass
    print('%-40s entries=%4d  first=%s  last=%s  span=%6.0f min  dl=%s  paper.tex words=%d  largest gaps=%s' % (
        n, len(infos), real[0].strftime('%m-%d %H:%M') if real else '-', real[-1].strftime('%m-%d %H:%M') if real else '-',
        span, dt.datetime.fromtimestamp(os.path.getmtime(p)).strftime('%m-%d %H:%M'), tex_words,
        ['%.0f' % g[0] for g in gaps]))
