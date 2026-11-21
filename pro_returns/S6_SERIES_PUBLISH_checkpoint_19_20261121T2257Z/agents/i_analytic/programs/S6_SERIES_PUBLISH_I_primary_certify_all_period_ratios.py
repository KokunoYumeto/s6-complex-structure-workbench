"""Enclose all eleven real periods and the freshly replayed leading ratios.

The E4 formula and tail are the proved formulas in C.6.R5.  This extends
that calculation to the five other rows.  The L-value radii combine the
explicit coefficient tail with the rounding/Taylor bounds in C.6.R2;
the recorded decimals are comparison data, never an input L-value.
"""
from pathlib import Path
import csv, json, re
from flint import arb, ctx

P = Path(__file__).resolve().parents[2]
REC = P / 'code/I/records'
OUTPUTS = P / 'code/I/outputs'
ctx.prec = 768
models = {r['i']: r for r in json.loads((REC/'C_cm_exact_local_data.json').read_text())}
old = {int(r['index']): r for r in csv.DictReader(
    (P.parents[1]/'sources/returns/S6_05_ARITHMETIC/results_Crank.csv').open())}
heights = {r['index']: arb(r['height_O']) for r in json.loads(
    (REC/'C_cm_height_arb.json').read_text())}
cm_data = [(2, True), (3, True), (4, True), (7, True),
           (7, False), (11, False), (19, False), (27, False),
           (43, False), (67, False), (163, False)]


def period(a, cm_d, rectangular):
    a1, a2, a3, a4, a6 = a
    b2 = a1*a1 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3*a3 + 4*a6
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    disc = (c4**3-c6**2)//1728
    assert 1728*disc == c4**3-c6**2 and c4 > 0 and disc
    T = arb(cm_d).sqrt()/(1 if rectangular else 2)
    r = (-2*arb.pi()*T).exp()
    q = r if rectangular else -r
    assert r < arb('0.001')
    e6_margin = 1-1008*r/(1-32*r)
    assert e6_margin > 0
    M = 100
    sig = [0]*(M+1)
    for d in range(1, M+1):
        for n in range(d, M+1, d):
            sig[n] += d**3
    e4, qn = arb(1), arb(1)
    for n in range(1, M+1):
        qn *= q
        e4 += 240*sig[n]*qn
    A = M+1
    tail = 480*r**A*(A**3/(1-r)+3*A*A*r/(1-r)**2
                     +3*A*r*(1+r)/(1-r)**3
                     +r*(1+4*r+r*r)/(1-r)**4)
    e4 += arb(0, tail.upper())
    assert e4 > 0
    scale = 2*arb.pi()*(e4/c4).sqrt().sqrt()
    components = 2 if disc > 0 else 1
    direction = arb(1) if c6 > 0 else (T if disc > 0 else 2*T)
    omega = components*direction*scale
    return omega, dict(c4=str(c4), c6=str(c6), discriminant=str(disc),
                       components=components, E4=e4.str(100),
                       E4_tail=tail.str(30), E6_positive_margin=e6_margin.str(30),
                       full_real_period=omega.str(100))


out = []
for i, (cm_d, rectangular) in enumerate(cm_data, 1):
    omega, pd = period(models[i]['model'], cm_d, rectangular)
    f = OUTPUTS/(f'Crank_derivative_{i}.stdout.txt' if i < 11
                 else 'Crank_cm_stream_512.out')
    text = f.read_text()
    value = re.search(r'^(?:derivative|Lprime) (\S+)$', text, re.M)[1]
    tail = re.search(r'^tail_bound (\S+)$', text, re.M)[1]
    # The small extra factor strictly enlarges the printed tail bound.
    error = arb(tail)*arb('1.01') + arb('1e-100' if i < 11 else '1.1e-75')
    L = arb(value) + arb(0, error.upper())
    ratio = L/omega
    assert L > 0
    assert abs(ratio-arb(old[i]['Lleading_over_Omega'])) < arb('1e-55')
    assert abs(omega-arb(old[i]['full_real_period'])) < arb('1e-65')
    item = dict(index=i, period=pd, source_output=str(f.relative_to(P)),
                leading_derivative=L.str(100), error_radius=error.str(30),
                derivative_order=2 if i in [1, 8] else 1,
                leading_derivative_over_period=ratio.str(100),
                historical_55_digit_comparison=True)
    if i in [3, 5, 7]:
        sha = ratio/(4*heights[i])
        assert sha > arb('0.5') and sha < arb('1.5')
        item['Miller_positive_integer_enclosure'] = sha.str(90)
        item['Miller_unique_positive_integer'] = 1
    out.append(item)
    print('INDEX', i, 'period', omega.str(70), 'leading ratio', ratio.str(70))
(REC/'all_period_ratios_arb.json').write_text(json.dumps(out, indent=2)+'\n')
print('PASS: all eleven period/leading-ratio comparisons; three Miller integers isolated.')
