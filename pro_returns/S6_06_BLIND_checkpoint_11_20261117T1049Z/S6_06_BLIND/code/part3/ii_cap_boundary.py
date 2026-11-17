#!/usr/bin/env python3
"""Exact irreducible-II source and boundary mapping cones."""
from pathlib import Path
import json
import sympy as S
from integer_chain import cone,hom,ints
root=Path(__file__).resolve().parents[2]
data={x['row']:x for x in json.loads((root/'code/part3_fourfold/primitive_source_translation.json').read_text())['cases']}
out=[]
for row in [45,47,55]:
 a=data[row]; B=S.Matrix(a['gram']); T=S.Matrix(a['actual_suspension_translation'])
 F=S.eye(10)[:,1];L=F
 pdims={0:1,1:1,2:10,3:1,4:1}
 pd={1:S.zeros(1),2:L.T*B,3:S.zeros(10,1),4:S.ones(1),5:S.zeros(1,0)}
 pf={0:S.eye(1),1:S.eye(1),2:T,3:S.eye(1),4:S.eye(1)}
 wd,wdims=cone(pd,pf,pdims); WH={j:hom(wd[j],wd[j+1]) for j in range(1,5)}
 ndims={0:1,1:1,2:1,3:1}
 nd={1:S.zeros(1),2:S.zeros(1),3:S.zeros(1),4:S.zeros(1,0)}
 nf={j:S.eye(1) for j in range(4)}
 ed,edims=cone(nd,nf,ndims); EH={j:hom(ed[j],ed[j+1]) for j in range(1,5)}
 inc={0:S.eye(1),1:S.eye(1),2:L,3:S.eye(1),4:S.zeros(1,0)}
 iw={j:S.diag(inc.get(j,S.zeros(pdims.get(j,0),ndims.get(j,0))),inc.get(j-1,S.zeros(pdims.get(j-1,0),ndims.get(j-1,0)))) for j in range(1,5)}
 for j in range(2,5):assert wd[j]*iw[j]==iw[j-1]*ed[j]
 maps={j:WH[j][2]*iw[j]*EH[j][1] for j in range(1,5)}
 fibre=EH[2][2]*S.Matrix([1,0])
 assert WH[1][0]==WH[2][0]==WH[3][0]==[0] and WH[4][0]==[]
 assert maps[2]*fibre==S.zeros(1,1)
 assert abs(int(maps[2][0,1]))==1 and abs(int(fibre[0]))==1
 rec=dict(row=row,source_gram=ints(B),translation=ints(T),
          exterior_cone={str(j):ints(x) for j,x in wd.items()},
          boundary_cone={str(j):ints(x) for j,x in ed.items()},
          exterior_homology={str(j):WH[j][0] for j in WH},
          boundary_homology={str(j):EH[j][0] for j in EH},
          boundary_maps={str(j):ints(maps[j]) for j in maps},
          boundary_F=ints(fibre),
          boundary_L=ints(EH[3][2]*S.Matrix([1,0])),
          boundary_Fgamma=ints(EH[3][2]*S.Matrix([0,1])))
 out.append(rec)
 print('OS',row,'H(W)',rec['exterior_homology'],'H(E)',rec['boundary_homology'])
 print('all boundary maps',rec['boundary_maps'],'F',rec['boundary_F'])
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(status='PASS',cases=out),indent=2)+'\n')
print('PASS: all three actual II source/boundary cones and primitive fibre/Wang maps.')
