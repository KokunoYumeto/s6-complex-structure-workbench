"""Fresh local algebra witnesses for the companion-derived family models."""
from pathlib import Path
import json
import sympy as S

data=json.loads(Path(__file__).with_name('F2_13_companion_explore_fresh.output.json').read_text())
out={}
for case,d in data.items():
    a=S.Matrix(d['a6']);b=S.Matrix(d['b6'])
    positions=[(0,j) for j in range(6)]+[(i,j) for i in range(1,6) for j in range(1,6)]
    echelon={};words=[];matrices=[]
    def add(word,m):
        r=[int(m[i,j])%3 for i,j in positions]
        for k in sorted(echelon):
            c=r[k]
            if c:r=[(x-c*y)%3 for x,y in zip(r,echelon[k])]
        if not any(r):return False
        k=next(i for i,x in enumerate(r) if x)
        inv=pow(r[k],-1,3);r=[x*inv%3 for x in r]
        echelon[k]=r;words.append(word);matrices.append(m)
        return True
    add('',S.eye(6));j=0
    while j<len(words):
        word=words[j];m=matrices[j]
        for symbol,g in [('A',a),('B',b)]:add(word+symbol,m*g)
        j+=1
    c=S.Matrix([[m[i,j] for m in matrices] for i,j in positions])
    det=int(c.det()) if c.rows==c.cols else None
    out[case]={'dimension_mod3':len(words),'words':words,'determinant':det,'coordinates':c.tolist()}
    print(case,len(words),det,words)
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
