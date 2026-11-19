#!/usr/bin/env python3
"""Post-target exact comparison of the printed primitive basis with the frozen one."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
p=Path('code/continuation_VI/primitive_exterior_bridge_fresh.output.json');data=json.loads(p.read_text())
N=[[F(x) for x in r] for r in data['transvection_image_minus_identity']]
Q=[[F(x) for x in r] for r in data['primitive_basis_gram']]
S=[[1,0,0,0,0],[0,1,0,0,0],[0,0,0,-1,0],[0,0,-1,0,0],[0,0,0,0,1]]
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tr(a):return list(map(list,zip(*a)))
I=[[int(i==j) for j in range(5)] for i in range(5)]
assert mm(S,S)==I
Nt=mm(mm(S,N),S)
expected=[[0]*5 for _ in range(5)];expected[0][2]=-1;expected[1][3]=1
assert Nt==expected
assert mm(N,S)==mm(S,Nt)
Qt=mm(mm(tr(S),Q),S)
expectedQ=[[0]*5 for _ in range(5)]
for i,j in [(0,3),(3,0),(1,2),(2,1)]:expectedQ[i][j]=-1
expectedQ[4][4]=-2
assert Qt==expectedQ
out={'status':'PASS','checks':4,'basis_conversion_columns':S,'printed_transvection_minus_identity':[[str(x) for x in r] for r in Nt],'printed_gram':[[str(x) for x in r] for r in Qt],'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Actual post-comparison coordinate map only; prereading general bridge remains the frozen note.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','checks':4,'target_arrows':['third to minus first','fourth to second']},indent=2))
