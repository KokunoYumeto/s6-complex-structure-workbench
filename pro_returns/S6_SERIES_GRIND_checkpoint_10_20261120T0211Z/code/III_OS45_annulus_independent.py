"""Literal Laurent annulus and all component/primitive mixed pairings.

Fresh after-reading implementation of D.OF12--17. No earlier program or
saved certificate is imported. Negative path powers are integral chains.
"""
from pathlib import Path
import datetime
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value):
    assert bool(value),name
    checks.append(name)

directions=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def psi(r,t):return 4*(r//8)+3*(r%8)*(t//2)
def walls(r,t):
    values=[]
    for j,(a,b) in enumerate(directions):
        c,d=directions[j-1];e,f=directions[(j+1)%6]
        values.append(psi(r,t)+psi(r+a,t+b)-psi(r+c,t+d)-psi(r+e,t+f))
    return values

# Literal Picard columns of OF13, in (x exponent,y exponent,E index,coefficient).
picard=[[( -1,-2,2,1),(0,-1,3,1)], [(-1,-1,2,-1)], [(-1,0,1,1),(-2,-1,2,1)]]
def geometric_series(n,axis,offset=(0,0)):
    out={}
    for k in (range(n) if n>=0 else range(n,0)):
        ex=list(offset);ex[axis]+=k
        out[tuple(ex)]=1 if n>=0 else -1
    return out
def add_poly(*terms):
    out={}
    for scale,p in terms:
        for k,v in p.items():out[k]=out.get(k,0)+scale*v
    return {k:v for k,v in out.items() if v}
def evaluate_column(poly,j):
    value=0
    for (a,b),coeff in poly.items():
        for dx,dy,E,c in picard[j]:
            # x translates the positive component labels by(-1,0), y by(0,1).
            r,t=-(a+dx),b+dy
            value+=coeff*c*walls(r,t)[2*(E-1)]
    return value
annulus=[];path_records=[]
for ar,at in [(1,0),(0,1)]:
    line=[]
    aa,bb=-ar,at
    for pr,pt in [(8,-6),(24,-16)]:
        p,q=-pr,pt
        sx=geometric_series(p,0)
        sy=geometric_series(q,1,offset=(p,0))
        polys=[add_poly((aa,sx)),add_poly((bb,sx),(aa,sy)),add_poly((bb,sy))]
        total=sum(evaluate_column(polys[j],j) for j in range(3))
        line.append(total)
        path_records.append(dict(angular=[ar,at],period=[pr,pt],laurent_coefficients=[[[a,b,v] for (a,b),v in sorted(poly.items())] for poly in polys],value=total))
    annulus.append(line)
check('literal full shifted Picard annulus matrix',annulus==[[9,24],[0,0]])
check('actual short-long reduction mod8',[[x%8 for x in row] for row in annulus]==[[1,0],[0,0]])

# The alternative y-first path is checked by the literal module relation.
alternate=[]
for ar,at in [(1,0),(0,1)]:
    line=[];aa,bb=-ar,at
    for pr,pt in [(8,-6),(24,-16)]:
        p,q=-pr,pt
        sx=geometric_series(p,0,offset=(0,q));sy=geometric_series(q,1)
        polys=[add_poly((aa,sx)),add_poly((bb,sx),(aa,sy)),add_poly((bb,sy))]
        line.append(sum(evaluate_column(polys[j],j) for j in range(3)))
    alternate.append(line)
check('opposite rectangular path same literal value',alternate==annulus)

components=[]
for r in range(8):
    for t in range(2):
        d=walls(r,t);eta=[d[0]+d[1]+d[2],-d[0],-d[2],-d[4]]
        components.append(dict(index=2*r+t,r=r,t=t,walls=d,eta=eta,square=eta[0]**2-sum(x*x for x in eta[1:]),mixed_y=(-1)**t*(eta[0]+eta[1])))
Q=s.zeros(16)
for row in components:
    i=row['index'];Q[i,i]=-sum(row['walls'])
    for j,(a,b) in enumerate(directions):
        k=2*((row['r']+a)%8)+(row['t']+b)%2
        if k!=i:Q[i,k]+=row['walls'][j]
check('component mixed matrix symmetric mod8',all(int(x)%8==0 for x in Q-Q.T))
check('total fibre divisor gives zero mixed pairings',all(int(x)%8==0 for x in Q*s.ones(16,1)))
P=s.zeros(15)
P[:14,:14]=Q[:14,:14]
for i in range(14):P[i,14]=P[14,i]=components[i]['mixed_y']
P[14,14]=0
T=s.zeros(15,16)
for i in range(14):T[i,i]=1
for i in range(0,14,2):T[i,14]=-1
for i in range(1,14,2):T[i,15]=-1
T[14,14]=-2;T[14,15]=2
recovered=T.T*P*T
for i in range(16):
    for j in range(16):check(f'primitive-to-component mixed pairing {i},{j}',int(recovered[i,j]-Q[i,j])%8==0)
for i,row in enumerate(components):
    check(f'component Pontryagin square{i}',row['square']%16==(7 if i<14 else 15))
    check(f'primitive y mixed entry{i}',row['mixed_y']%8==(4 if i in (0,1,14,15) else 0))
    check(f'half-component relation{i}',(sum(Q[i,j] for j in range(1,16,2))-2*row['mixed_y'])%8==0)

out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    author='GPT-6 Astra (OpenAI), ChatGPT Pro mode; no separate numeric effort setting exposed; same model family',
    exposure='After reading displayed OF12--17; literal Laurent/module reconstruction with no original code or saved certificate imported',
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    passed=len(checks),checks=checks,annulus_matrix=annulus,opposite_path_matrix=alternate,path_records=path_records,
    component_rows=components,component_mixed_mod8=[[int(x)%8 for x in row] for row in Q.tolist()],
    primitive_mixed_mod8=[[int(x)%8 for x in row] for row in P.tolist()],primitive_component_map=T.tolist(),
    qualification='Literal Picard/module annulus values and complete finite mixed table at the stated support; the separate full boundary/cochain geometric argument and odd-cycle framing retain their stated scopes.')
dest=ROOT/'code/outputs/III_OS45_annulus_independent.json'
dest.write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps({'passed':len(checks),'annulus':annulus,'opposite_path':alternate,'component_table':[16,16],'primitive_table':[15,15]}))
