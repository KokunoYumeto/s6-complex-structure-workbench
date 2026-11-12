"""Finite exact checks for the higher-index slide and prism formulas."""
from pathlib import Path
from collections import defaultdict
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,ok):
    assert bool(ok),name
    checks.append(name)
def boundary(chain):
    out=defaultdict(int)
    for simplex,c in chain.items():
        for a in range(len(simplex)):
            out[simplex[:a]+simplex[a+1:]]+=c*(-1)**a
    return {v:c for v,c in out.items() if c}
def add(*chains):
    out=defaultdict(int)
    for chain in chains:
        for v,c in chain.items():out[v]+=c
    return {v:c for v,c in out.items() if c}
def prism(simplex):
    return {tuple((v,0) for v in simplex[:a+1])+tuple((v,1) for v in simplex[a:]):(-1)**a for a in range(len(simplex))}
def chain_prism(chain):
    out={}
    for simplex,c in chain.items():out=add(out,{v:c*b for v,b in prism(simplex).items()})
    return out
for m in range(0,7):
    simplex=tuple(range(m+1))
    side=chain_prism(boundary({simplex:1})) if m else {}
    top={tuple((v,1) for v in simplex):1}
    bottom={tuple((v,0) for v in simplex):-1}
    ck(f'Exact alternating prism boundary in degree {m}',
       add(boundary(prism(simplex)),side)==add(top,bottom))
    for a,(_,c) in enumerate(prism(simplex).items()):
        vertices=[(v,0) for v in simplex[:a+1]]+[(v,1) for v in simplex[a:]]
        def point(vt):
            v,t=vt
            return S.Matrix([t]+[int(v==q) for q in range(1,m+1)])
        M=S.Matrix.hstack(*[point(v)-point(vertices[0]) for v in vertices[1:]])
        ck(f'Time-first prism orientation m={m} a={a}',M.det()==c)
eps,t,chi=S.symbols('eps t chi',real=True)
for k in range(2,6):
    for sig in [-1,1]:
        crossing=S.diag(*([1]*(k-1)),2*sig*eps)
        timefirst=crossing[:,[k-1]+list(range(k-1))]
        ck(f'Full crossing permutation k={k} sigma={sig}',
           S.expand(timefirst.det()-(-1)**(k-1)*2*sig*eps)==0)
        gradient=S.symbols('c0:'+str(k-1))
        flow=S.eye(k+2)
        for q in range(k-1):flow[k-1,q]=2*sig*eps*t*gradient[q]
        inv=flow.subs(t,-t)
        ck(f'Inner full framing derivative inverse k={k} sigma={sig}',flow*inv==S.eye(k+2))
        ck(f'Inner full framing derivative determinant k={k} sigma={sig}',flow.det()==1)
A=S.Matrix([[2,3,5]]);B=S.Matrix([[-3,-4],[2,1],[0,1]])
U=S.Matrix([[1,0,0],[1,1,0],[0,0,1]])
Ap=S.Matrix([[5,3,5]]);Bp=S.Matrix([[-3,-4],[5,5],[0,1]])
ck('Exercise one original adjacent product',A*B==S.zeros(1,2))
ck('Exercise one first differential',A*U==Ap)
ck('Exercise one second differential',U.inv()*B==Bp)
ck('Exercise one filtered lower square',Ap*U.inv()==A)
ck('Exercise one filtered upper square',Bp==U.inv()*B)
ck('Exercise one new adjacent product',Ap*Bp==S.zeros(1,2))
section=S.Matrix([-1,1,0]);newsection=S.Matrix([-1,2,0])
ck('Exercise one exact section transport',U.inv()*section==newsection)
ck('Exercise one section identity',Ap*newsection==S.eye(1))
E21=S.zeros(3);E21[1,0]=1
E32=S.zeros(3);E32[2,1]=1
E31=S.zeros(3);E31[2,0]=1
U1=S.eye(3)-E21;U2=S.eye(3)+E32
V=S.Matrix([[1,0,0],[-1,1,0],[0,1,1]])
Vi=S.Matrix([[1,0,0],[1,1,0],[-1,-1,1]])
ck('Exercise two ordered geometric basis',U1*U2==V)
ck('Exercise two reverse ordered map',U2.inv()*U1.inv()==Vi)
ck('Exercise two complete cross term',Vi==S.eye(3)+E21-E32-E31)
ck('Exercise two both inverse identities',V*Vi==Vi*V==S.eye(3))
ck('Exercise two order genuinely matters',U1*U2!=U2*U1)
for a in [-7,-2,0,3,11]:
    Va=S.eye(3)+a*E21
    ck(f'Integer slide multiplicity {a}',Va.inv()==S.eye(3)-a*E21)
    ck(f'Both adjacent maps for multiplicity {a}',(A*Va)*(Va.inv()*B)==S.zeros(1,2))
# Chain-homotopy correction on a nontrivial graded free complex.
# Acyclic example, degrees 2,3,4; arbitrary P2 and P3 produce T=F-dP-Pd.
P2=S.Matrix([2,-1,3]);P3=S.Matrix([[1,-2,4],[-3,5,2]])
T2=S.eye(1)-A*P2
T3=S.eye(3)-B*P3-P2*A
T4=S.eye(2)-P3*B
ck('Prism correction lower chain equation',A*T3==T2*A)
ck('Prism correction upper chain equation',B*T4==T3*B)
src=W/'src/higher-index-framed-slides-and-chain-maps.md'
result=dict(source=src.name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),passed=len(checks),checks=checks,scope='Finite exact prism-boundary, orientation, derivative and matrix checks. The geometric existence and singular-homology statements rely on the complete written arguments.',independent_review=False)
(W/'checks/HIGHER_SLIDE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(checks=len(checks),source_sha256=result['source_sha256'])))
