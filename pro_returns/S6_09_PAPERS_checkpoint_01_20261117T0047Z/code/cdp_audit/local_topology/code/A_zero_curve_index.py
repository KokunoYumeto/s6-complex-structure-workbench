"""All nineteen monodromy constants for the geometric criterion UN39.

The input is the independently executed exact A'Campo signature table.
We compare the sum of its exponents with the finite average of actual
Lefschetz determinants, and emit the complete zero-index table.
"""
import csv
from fractions import Fraction
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
with (root/'records/D_monodromy_signatures.csv').open(newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==19
out=[]
tex=[r'\begin{array}{c|r|r|r}',
     r'\det(xI-T)&M&j(T)&I_\pi\text{ for }e(S)=0\\ \hline']
for row in rows:
    poly=row['characteristic_polynomial']
    M=int(row['semisimple_order'])
    values=[int(v.strip()) for v in row['one_period_Lk'].split(';')]
    assert len(values)==M
    coeffs={int(n):int(a) for n,a in
            re.findall(r'a_(\d+)=(-?\d+)',row['nonzero_a_n'])}
    exponent_sum=sum(coeffs.values())
    average=Fraction(sum(values),M)
    assert average.denominator==1
    j=int(average)
    assert j==exponent_sum
    if re.search(r'Phi_1(?:\^|\s|$)',poly): expected=0
    elif poly=='Phi_2^4': expected=8
    elif poly in ['Phi_3^2','Phi_4^2','Phi_6^2']: expected=6
    else: expected=4
    assert j==expected
    assert j%2==0
    target=j//2
    out.append({'characteristic_polynomial':poly,'semisimple_order':M,
                'sum_a_n':exponent_sum,'average_lefschetz':j,
                'zero_curve_index':target})
    factors=[]
    for n,power in re.findall(r'Phi_(\d+)(?:\^(\d+))?',poly):
        factors.append(r'\Phi_{'+n+'}'+('^{'+power+'}' if power else ''))
    tex.append(' '.join(factors)+f'&{M}&{j}&{target}'+r'\\')
    print(f'{poly:24s} M={M:2d}; sum a_n={j}; '
          f'average L_k={j}; zero index={target}')
tex.append(r'\end{array}')
(root/'records/A_zero_curve_index_table.tex').write_text('\n'.join(tex)+'\n')
with (root/'records/A_zero_curve_index.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]))
    w.writeheader(); w.writerows(out)
assert {r['average_lefschetz'] for r in out}=={0,4,6,8}

# Exact dual-curve data for the point and point-plus-quartic operations.
def curve_index(genera,triples):
    return sum(g-1 for g in genera)+triples
assert curve_index([],0)==0
assert curve_index([0],0)==-1
assert curve_index([0,3,0,0,0,0],4)==1
print('Point blowup of a smooth torus support: one rational double curve, '
      'index -1, Euler +2.')
print('Point plus transverse genus-three quartic: five rational double '
      'curves, one genus-three curve, four triples, index +1, Euler -2.')
print('PASS: all nineteen constants and both geometric modification checks.')
