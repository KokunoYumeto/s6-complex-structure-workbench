"""Re-run the shipped interval proof (certify) on every certified leaf of the saved
certificate and compare with the saved upper bounds.  Runner written by the reviewer;
the proof function is the return's f_interval_cert.certify."""
import sys, json, time
CODE = sys.argv[1]
sys.path.append(CODE)
from fractions import Fraction as F
from concurrent.futures import ProcessPoolExecutor

def work(rec):
    import f_interval_cert as C
    box = tuple(F(v) for v in rec['box'])
    try:
        ok, why = C.certify(box)
    except Exception as e:
        return (rec['box'], False, str(e), None)
    return (rec['box'], bool(ok), why.get('norm_squared_upper'), rec['certificate']['norm_squared_upper'])

if __name__ == '__main__':
    data = json.load(open(CODE + '/f_interval_parallel_certificate.json'))
    recs = data['certified']
    t0 = time.time()
    bad = []; mism = 0; n = 0; mx = '0'
    with ProcessPoolExecutor(max_workers=12) as pool:
        for box, ok, mine, saved in pool.map(work, recs, chunksize=50):
            n += 1
            if not ok:
                bad.append((box, mine))
            elif mine != saved:
                mism += 1
            if n % 2000 == 0:
                print('progress', n, 'bad', len(bad), 'mismatch', mism, round(time.time() - t0, 1), flush=True)
    print('TOTAL', n, 'NOT_RECERTIFIED', len(bad), 'BOUND_STRING_MISMATCH', mism, 'seconds', round(time.time() - t0, 1))
    for b in bad[:20]:
        print('BAD', b)
