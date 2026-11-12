"""Exact center-cochain, native endpoint, and Pauli-action diagnostics."""
from itertools import combinations, product
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import sympy as s


def shift(n, i):
    out=list(n)
    out[i]+=1
    return tuple(out)


rows=[]
for L in (2,3,4):
    vertices=list(product(range(-L,L+1),repeat=3))
    edges=[(n,i) for n in vertices for i in range(3) if n[i]<L]
    native={e:(-1)**(e[0][1]%2) if e[1]==0 else 1 for e in edges}
    allface={e:(-1)**(sum(e[0][:e[1]])%2) for e in edges}
    faces=[]
    for n in vertices:
        for i,j in combinations(range(3),2):
            if n[i]>=L or n[j]>=L:
                continue
            boundary=((n,i),(shift(n,i),j),(shift(n,j),i),(n,j))
            faces.append((n,i,j,boundary))
            value=1
            parity=1
            for edge in boundary:
                value*=native[edge]
                parity*=allface[edge]
            assert value==(-1 if (i,j)==(0,1) else 1)
            assert parity==-1
    twisted=sum(1 for n,i,j,b in faces if (i,j)==(0,1))
    assert twisted==(2*L)**2*(2*L+1)
    # Test every 12 rectangle at a fixed retained third coordinate.
    rectangle_count=0
    for x0 in range(-L,L):
        for x1 in range(x0+1,L+1):
            for y0 in range(-L,L):
                for y1 in range(y0+1,L+1):
                    boundary=[((x,y0,0),0) for x in range(x0,x1)]
                    boundary += [((x1,y,0),1) for y in range(y0,y1)]
                    boundary += [((x,y1,0),0) for x in range(x0,x1)]
                    boundary += [((x0,y,0),1) for y in range(y0,y1)]
                    value=1
                    for edge in boundary:
                        value*=native[edge]
                    assert value==(-1)**(((x1-x0)*(y1-y0))%2)
                    rectangle_count+=1
    rows.append(dict(L=L,links=len(edges),faces=len(faces),
                     native_twisted_faces=twisted,rectangles=rectangle_count))

I=s.I
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
T=[-I*x/2 for x in sigma]
Hc=I*sigma[2]
assert Hc==-2*T[2]
assert Hc*T[0]-T[0]*Hc==-2*T[1]
assert Hc*T[1]-T[1]*Hc==2*T[0]
assert (s.pi*Hc).exp()==-s.eye(2)
assert (2*s.pi*Hc).exp()==s.eye(2)
z=s.symbols('z',nonzero=True)
g=s.diag(z,1/z)
cos2=(z**2+z**-2)/2
sin2=(z**2-z**-2)/(2*I)
assert s.simplify(g*T[0]*g.inv()-(cos2*T[0]-sin2*T[1]))==s.zeros(2)
assert s.simplify(g*T[1]*g.inv()-(sin2*T[0]+cos2*T[1]))==s.zeros(2)
assert F(4,3)/F(4,9)==3
assert F(4)/F(4,9)==9
assert 2*F(2,9)==F(4,9)

base=Path(__file__).resolve().parent
source=base/'native_center_disorder_bridge.md'
raw=source.read_bytes()
receipt=dict(status='PASS',source=source.name,source_bytes=len(raw),
             source_sha256=sha256(raw).hexdigest(),boxes=rows,
             checks='Exact integer cochains, rectangle pairing, Pauli rotations, center endpoints, and leading moment ratios.',
             scope='Diagnostics for explicit algebra; the all-coupling operator and vacuum statements are proved in the complete source.')
(base/'CENTER_DISORDER_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,indent=2))
