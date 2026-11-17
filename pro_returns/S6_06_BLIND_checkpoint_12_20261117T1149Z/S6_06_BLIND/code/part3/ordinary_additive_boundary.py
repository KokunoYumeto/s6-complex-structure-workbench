#!/usr/bin/env python3
"""Full source/boundary cones for the three ordinary III/IV cap sites."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S
from integer_chain import cone, hom, ints

root = Path(__file__).resolve().parents[2]
source = root / 'code/part3_fourfold/primitive_source_translation.json'
with (root / 'records/literature_control.md').open('a') as log:
    log.write('\n- ' + datetime.now(timezone.utc).isoformat() +
              ' — Read current-team primitive_source_translation.json and '
              'primitive/weighted_additive_complements programs/results; '
              'material: exact marked NS, translation and source-boundary '
              'lattices for ordinary III/IV caps. No external source or '
              'comparison paper was opened.\n')
data = {x['row']: x for x in json.loads(source.read_text())['cases']}
outputs = []
for row, p, block, kind in [(47, 2, 1, 'III'), (56, 2, 2, 'III'),
                            (56, 3, 1, 'IV')]:
    a = data[row]
    gram = S.Matrix(a['gram'])
    T0 = S.Matrix(a['actual_suspension_translation'])
    eye = S.eye(10)
    F = eye[:, 1]
    ri = [i for i, name in enumerate(a['basis'])
          if name.startswith(f'I{p}_{block}_C')]
    roots = eye[:, ri]
    L = S.Matrix.hstack(F-sum((roots[:, j] for j in range(p-1)),
                             S.zeros(10, 1)), roots)
    Lleft = (L.T*L).inv()*L.T
    for b in [1, p]:
        T = T0**b
        Pc = Lleft*T*L
        assert L*Pc == T*L
        assert Pc.T*Pc == S.eye(p)
        pdims = {0: 1, 1: p, 2: 10, 3: 1, 4: 1}
        pd = {1: S.zeros(1, p), 2: L.T*gram, 3: S.zeros(10, 1),
              4: S.ones(1, 1), 5: S.zeros(1, 0)}
        pf = {0: S.eye(1), 1: Pc.inv().T, 2: T,
              3: S.eye(1), 4: S.eye(1)}
        wd, wdims = cone(pd, pf, pdims)
        WH = {j: hom(wd[j], wd[j+1]) for j in range(1, 5)}
        ndims = {0: 1, 1: p, 2: p, 3: 1}
        nd = {1: S.zeros(1, p), 2: L.T*gram*L,
              3: S.zeros(p, 1), 4: S.zeros(1, 0)}
        nf = {0: S.eye(1), 1: Pc.inv().T, 2: Pc, 3: S.eye(1)}
        ed, edims = cone(nd, nf, ndims)
        EH = {j: hom(ed[j], ed[j+1]) for j in range(1, 5)}
        inc = {0: S.eye(1), 1: S.eye(p), 2: L,
               3: S.eye(1), 4: S.zeros(1, 0)}
        iw = {j: S.diag(inc.get(j, S.zeros(pdims.get(j, 0), ndims.get(j, 0))),
                        inc.get(j-1, S.zeros(pdims.get(j-1, 0), ndims.get(j-1, 0))))
              for j in range(1, 5)}
        for j in range(2, 5):
            assert wd[j]*iw[j] == iw[j-1]*ed[j]
        maps = {j: WH[j][2]*iw[j]*EH[j][1] for j in range(1, 5)}
        fibre = EH[2][2]*S.ones(p, 1).col_join(S.zeros(p, 1))
        Lcycle = EH[3][2]*S.Matrix([1]+[0]*p)
        # A source fibre traced in the actual suspension direction.
        Fgamma = EH[3][2]*S.Matrix([0]+[1]*p)
        record = dict(row=row, kind=kind, b=b, line_multiple=a['denominator']//b,
                      source_gram=ints(gram), component_columns=ints(L),
                      translation=ints(T), component_permutation=ints(Pc),
                      source_differentials={str(j): ints(x) for j, x in pd.items()},
                      boundary_differentials={str(j): ints(x) for j, x in nd.items()},
                      exterior_cone={str(j): ints(x) for j, x in wd.items()},
                      boundary_cone={str(j): ints(x) for j, x in ed.items()},
                      exterior_homology={str(j): WH[j][0] for j in WH},
                      boundary_homology={str(j): EH[j][0] for j in EH},
                      boundary_representatives={str(j): ints(EH[j][1]) for j in EH},
                      exterior_representatives={str(j): ints(WH[j][1]) for j in WH},
                      boundary_maps={str(j): ints(maps[j]) for j in maps},
                      boundary_F=ints(fibre), exterior_F=ints(maps[2]*fibre),
                      boundary_L=ints(Lcycle), boundary_Fgamma=ints(Fgamma))
        outputs.append(record)
        print(f'OS{row} {kind}: b={b}, a={a["denominator"]//b}')
        print(' H(W)=',record['exterior_homology'],'H(E)=',record['boundary_homology'])
        print(' H2 map=',record['boundary_maps']['2'],'F=',record['boundary_F'])
        print(' H3 map=',record['boundary_maps']['3'],
              'L=',record['boundary_L'],'Fgamma=',record['boundary_Fgamma'])

Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
    status='PASS', scope='Full integral source and boundary cone maps; actual cap maps retained in the working proof.',
    cases=outputs), indent=2)+'\n')
print('PASS: all six exact source-boundary chain maps, all homology degrees and marked fibre/source traces.')
