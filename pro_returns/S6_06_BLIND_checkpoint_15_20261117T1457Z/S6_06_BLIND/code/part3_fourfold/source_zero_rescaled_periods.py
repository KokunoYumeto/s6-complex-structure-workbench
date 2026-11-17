#!/usr/bin/env python3
"""Exact rescaled two-node period lattices; no origin-count or index inference."""
from pathlib import Path
from datetime import datetime, timezone
import sympy as S
import json
ROOT=Path(__file__).resolve().parents[2]
N=S.symbols('N',integer=True)
swap=S.Matrix([[0,1],[1,0]])
rows=[]
for a,b in [(1,2),(2,1)]:
    H=S.Matrix([[2,b],[-a,N-1]])
    if a==1:
        U=S.Matrix([[1,0],[-2,1]])*S.diag(-1,1)*swap
        V=S.Matrix([[1,N-1],[0,1]])
    else:
        U=S.diag(1,-1)*S.Matrix([[1,0],[-(N-1),1]])
        V=swap*S.Matrix([[1,-2],[0,1]])
    assert U.det() in (-1,1)
    assert V.det() in (-1,1)
    assert U*H*V==S.diag(1,2*N)
    for n in range(1,257):
        assert U.subs(N,n)*H.subs(N,n)*V.subs(N,n)==S.diag(1,2*n)
    rows.append({
      'a':a,'b':b,
      'period_columns':[[str(e) for e in H.row(i)] for i in range(2)],
      'left_unimodular':[[str(e) for e in U.row(i)] for i in range(2)],
      'right_unimodular':[[str(e) for e in V.row(i)] for i in range(2)],
      'smith':'diag(1,2N)',
      'N_positive_quotient':'Z/(2N)',
      'N_zero_quotient':'Z',
    })
data={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS: symbolic unimodular certificates plus512 positive-N evaluations',
 'rescaling':'lambda=v^N*lambda0',
 'source_period':'h=(2,-a)',
 'suspension_period':'g=(b,N-1)',
 'sector_relation':'a*b=2',
 'rows':rows,
 'closed_parameter_requirement':'Use N divisible by M and the literal one-gamma parameter r=v^(N/M)r0; this adds N/M marked one-gamma scalar loops. The smaller M/b endpoint requires its rational root to be tracked around the varying-source puncture.',
 'scope':'Exact period-lattice arithmetic. A fundamental lattice index is not yet identified with a count of quotient origin links, and no return index is assigned.'
}
(ROOT/'code/part3_fourfold/source_zero_rescaled_periods.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+data['utc']+' — Executed own source_zero_rescaled_periods.py. Material: exact two-sector period matrices for lambda=v^N lambda0, unimodular Smith reductions and512 evaluations; no cell-count or return inference.\n')
print(json.dumps(data,indent=2))
