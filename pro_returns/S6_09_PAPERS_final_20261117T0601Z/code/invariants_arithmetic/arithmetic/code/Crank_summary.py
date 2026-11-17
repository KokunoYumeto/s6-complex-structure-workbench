"""Collate independent L-derivatives, periods, heights and saturation results.

This script does not assume the Birch--Swinnerton-Dyer formula.  Its quotient
column records a numerical prediction, not an exact Tate--Shafarevich order.
"""
from pathlib import Path
import csv
import json
import re
import mpmath as mp

mp.mp.dps = 110
base = Path(__file__).resolve().parents[1]
model_text = (base / 'code/C_cm_models.out').read_text()
deriv_text = (base / 'code/Crank_derivatives.out').read_text()
stream_text = (base / 'code/Crank_cm_stream_163_check.out').read_text()
blocks = re.split(r'INDEX ', model_text)[1:]
derivatives = re.findall(r'derivative ([0-9.]+)\ntail_bound ([0-9.e+\-]+)', deriv_text)
last_derivative = re.search(r'Lprime ([0-9.]+)', stream_text).group(1)
last_tail = re.search(r'tail_bound ([0-9.e+\-]+)', stream_text).group(1)
derivatives.append((last_derivative, last_tail))
discriminants = [-8,-12,-16,-28,-7,-11,-19,-27,-43,-67,-163]
tam = [16,16,8,64,8,4,2,4,8,8,32]
tors = [2,2,2,2,2,1,1,1,1,1,1]
rows = []
for i, (block, (der, tail)) in enumerate(zip(blocks, derivatives)):
    j = int(re.search(r'j (-?\d+)', block).group(1))
    N = int(re.search(r'globalred \[(\d+)', block).group(1))
    h = mp.mpf(re.search(r'height_O ([0-9.]+)', block).group(1))
    omega1 = mp.mpf(re.search(r'periods \[([0-9.]+)', block).group(1))
    Omega = omega1 * (2 if j>1728 else 1)
    rank = 2 if i in (0,7) else 1
    val = mp.mpf(der)
    ratio = val/Omega
    quotient = ratio / (2*h*tam[i]/tors[i]**2) if rank==1 else None
    row = dict(index=i+1,j=j,CM_discriminant=discriminants[i],conductor=N,
               rank=rank,analytic_rank=rank,P_index='infinity' if rank==2 else 1,
               full_real_period=mp.nstr(Omega,75),height_O=mp.nstr(h,75),
               derivative_order=rank,leading_derivative=mp.nstr(val,75),
               derivative_tail_bound=tail,
               Lprime_over_Omega='0' if rank==2 else mp.nstr(ratio,70),
               Lleading_over_Omega=mp.nstr(ratio,70),
               Tamagawa_product=tam[i],torsion_order=tors[i],
               BSD_quotient_numerical='' if quotient is None else mp.nstr(quotient,70),
               expected_BSD_quotient='' if quotient is None else (9 if i==10 else 1))
    if quotient is not None:
        assert abs(quotient-(9 if i==10 else 1)) < mp.mpf('1e-69')
    rows.append(row)
    print('j',j,'rank',rank,'index',row['P_index'])
    print('Lprime/Omega',row['Lprime_over_Omega'])
    print('Lleading/Omega',row['Lleading_over_Omega'])
    print('BSD quotient (numerical)',row['BSD_quotient_numerical'])
with (base/'results_Crank.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(base/'records/Crank_summary.json').write_text(json.dumps(rows,indent=2)+'\n')
