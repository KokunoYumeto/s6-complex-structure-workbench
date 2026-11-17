"""Independent Arb certificate for all real periods and printed derivative ratios.

The source E4 Fourier expansion is enclosed with its explicit geometric tail.
All eleven minimal models have c4>0,c6<0.  At the reduced CM parameter
tau=iT (four positive j) or tau=1/2+iT (seven negative j), E4,E6>0.
If a=2*pi*(E4/c4)^(1/4), rotating the standard lattice by i gives the
model's sign of c6.  Its full real period is 2*T*a in both cases:
two components each of period T*a in the rectangular case, and the
primitive real cycle of length 2*T*a in the rhombic case.

The finite derivative sums have the independently audited C.6.R2 errors:
rows1–10 tail plus 1e-200 (1024-bit cancellation bound); row11 tail plus
1e-74 (Taylor <1e-75, operation rounding <1e-90, continuation <1e-90).
These radii are intentionally conservative.  No BSD hypothesis is used.
"""
from pathlib import Path
from decimal import Decimal, localcontext
import csv
import hashlib
import json
import re
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
D = Path(__file__).resolve().parent / 'arithmetic'
ctx.prec = 1152
rows = list(csv.DictReader((D / 'results_Crank.csv').open()))
models = json.loads((D / 'records/C_cm_exact_local_data.json').read_text())
out = []
pi = arb.pi()
M = 350
ds = [2, 3, 4, 7, 7, 11, 19, 27, 43, 67, 163]

for r, model, d in zip(rows, models, ds):
    i = int(r['index'])
    T = arb(d).sqrt() / (1 if i <= 4 else 2)
    Q = (-2 * pi * T).exp()
    q = Q if i <= 4 else -Q
    qn = arb(1)
    E4 = arb(1)
    E6 = arb(1)
    for n in range(1, M + 1):
        qn *= q
        E4 += 240 * n**3 * qn / (1 - qn)
        E6 -= 504 * n**5 * qn / (1 - qn)
    # (M+1+k)^s <= (M+1)^s (1+k)^s and the exact geometric power sums.
    tail4 = 240 * (M+1)**3 * Q**(M+1) * (1+4*Q+Q**2) / (1-Q)**5
    tail6 = 504 * (M+1)**5 * Q**(M+1) * (1+26*Q+66*Q**2+26*Q**3+Q**4) / (1-Q)**7
    E4 += arb(0, tail4)
    E6 += arb(0, tail6)
    a1, a2, a3, a4, a6 = model['model']
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    assert c4 > 0 and c6 < 0 and E4 > 0 and E6 > 0
    real_period = 4 * pi * T * (E4 / c4).sqrt().sqrt()
    assert real_period.rad() < arb('1e-330')
    source = D / 'outputs' / (f'writing_Crank_derivatives_{i}.txt' if i <= 10
                              else 'writing_Crank_cm_stream_163_512_190.txt')
    text = source.read_text()
    value = re.search(r'^(?:derivative|Lprime) ([^\n]+)', text, re.M)[1]
    tail = re.search(r'^tail_bound ([^\n]+)', text, re.M)[1]
    guard = '1e-200' if i <= 10 else '1e-74'
    derivative = arb(value) + arb(0, arb(tail) + arb(guard))
    ratio = derivative / real_period
    diff = abs(ratio - arb(r['Lleading_over_Omega']))
    assert derivative > 0
    assert diff < arb('1e-65')
    assert abs(real_period-arb(r['full_real_period'])) < arb('1e-70')
    out.append(dict(index=i, j=int(r['j']), c4=c4, c6=c6,
                    period=real_period.str(110), derivative=derivative.str(110),
                    ratio=ratio.str(110), difference_from_source_decimal=diff.str(30),
                    derivative_tail=tail, arithmetic_guard=guard,
                    derivative_source=str(source.relative_to(ROOT)),
                    derivative_source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                    E4_tail=tail4.str(20), E6_tail=tail6.str(20),
                    fifty_decimal_digit_check='PASS'))
    print(i, 'period', real_period.str(70), 'ratio', ratio.str(70), 'PASS')

stream1 = D / 'outputs/writing_Crank_cm_stream_163_170.txt'
stream2 = D / 'outputs/writing_Crank_cm_stream_163_512_190.txt'
with localcontext() as context:
    context.prec = 120
    a, b = [Decimal(re.search(r'^Lprime (.+)', p.read_text(), re.M)[1])
            for p in (stream1, stream2)]
    stream_difference = str(abs(a-b))
    assert abs(a-b) < Decimal('1e-75')

result = dict(checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro',
              date='2026-11-17', precision_bits=ctx.prec, terms=M,
              proof=__doc__, original_table='results_Crank.csv',
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              independent_stream_difference=stream_difference, rows=out)
(D / 'records/writing_period_derivative_certificate.json').write_text(
    json.dumps(result, indent=2) + '\n')
print('PASS all eleven periods and leading-derivative ratios; stream difference', stream_difference)
