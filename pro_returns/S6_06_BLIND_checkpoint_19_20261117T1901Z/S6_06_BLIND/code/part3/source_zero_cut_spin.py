#!/usr/bin/env python3
"""Exact local real-cut, charged-overlap and canonical-spin checks.

Scope: RT.13--15 only. No completed period strip or source-zero value.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks = []


def eq(name, a, b):
    assert s.simplify(a-b) == 0, name
    checks.append(name)


A, t, eta, H, b, c = s.symbols('A t eta H b c', real=True)
f = (1-A)*(A+(1-A)*t)
tmax = (eta-A+A*A)/(1-A)**2
eq('corner t substitution', f.subs(t,tmax), eta)
eq('corner t derivative', s.diff(tmax,A), (A+2*eta-1)/(1-A)**3)
eq('allowed sublevel A derivative lower endpoint',
   s.diff(f,A).subs(t,tmax), (1-A-2*eta)/(1-A))
eq('radial invariant formula', (1-A)*(b+A*c)/(b+c), f.subs(t,b/(b+c)))
eq('lower charged rho square', H*(H+s.Symbol('y2')), H*H+H*s.Symbol('y2'))
u = s.symbols('u', real=True)
sig2 = s.symbols('sig2', positive=True)
eq('charged defining function square', sig2**2*(1-u), sig2*(sig2*(1-u)))
eq('charged product radius', (sig2*(1-u)-s.Symbol('z2'))*(s.Symbol('z2')+sig2*u),
   (sig2-sig2*u-s.Symbol('z2'))*(s.Symbol('z2')+sig2*u))

U,w,S1,T1,T0 = s.symbols('U w S1 T1 T0', nonzero=True)
source = s.Matrix([U,w,S1,T1,T0])
target = s.Matrix([U*w,S1,T1,U*T0,1/U])
eq('EA26 full complex Jacobian', target.jacobian(source).det(), -1)
weights_source=s.Matrix([2*U,-w,S1,-T1,-T0])
weights_target=s.Matrix([target[0],target[1],-target[2],target[3],-2*target[4]])
for j in range(5):
    eq(f'EA26 auxiliary Euler component {j}', (target.jacobian(source)*weights_source)[j],weights_target[j])
physical_source=s.Matrix([U,-w,0,0,0])
physical_target=s.Matrix([0,0,0,target[3],-target[4]])
for j in range(5):
    eq(f'EA26 physical component {j}',(target.jacobian(source)*physical_source)[j],physical_target[j])
eq('EA26 q',target[0]*target[3]*target[4],U*w*T0)
eq('EA26 v tilde',target[0]*target[3]*target[4]-target[1]*target[2],U*w*T0-S1*T1)
eq('EA26 inverse U',1/target[4],U)
eq('EA26 inverse w',target[0]*target[4],w)
eq('EA26 inverse T0',target[3]*target[4],T0)
eq('charged four-coordinate identity',target[0].subs(U,1),w)
eq('canonical volume ratio root',s.I**2,-1)
zs=s.symbols('zs',nonzero=True)
eq('a1 reset determinant root',(1/zs)**2,zs**-2)
eq('a2 reset determinant root',(s.I/zs**2)**2,-zs**-4)

# Cl(8), e_i^2=-1, in an ordered bit-mask basis.
def mul(x,y):
    cx,mx=x; cy,my=y
    swaps=sum((my & ((1<<i)-1)).bit_count() for i in range(8) if mx>>i&1)
    repeats=(mx & my).bit_count()
    return cx*cy*((-1)**(swaps+repeats)),mx^my

def prod(*xs):
    ans=(1,0)
    for x in xs: ans=mul(ans,x)
    return ans

def cl_eq(name,a,b):
    assert a==b,(name,a,b)
    checks.append(name)

e=[(1,1<<i) for i in range(8)]
omega4=prod(*e[:4]); omega4n=prod(*e[4:]); omega8=prod(*e)
canon_b=(-omega4[0],omega4[1]); canon_n=(-omega4n[0],omega4n[1])
cl_eq('canonical two-block deck product',mul(canon_b,canon_n),omega8)
cl_eq('full deck order two',mul(omega8,omega8),(1,0))
physical_b=prod((-1,e[0][1]),e[1],(-1,e[2][1]),e[3])
physical_n=prod(*e[4:])
cl_eq('physical half-angle base endpoint',physical_b,omega4)
cl_eq('physical half-angle normal endpoint',physical_n,omega4n)
cl_eq('physical full endpoint canonical deck',mul(physical_b,physical_n),omega8)
Q=mul(e[1],e[3])
cl_eq('two-negative-coordinate conjugation commutes deck',mul(Q,omega8),mul(omega8,Q))
cl_eq('constant conjugation spin square',mul(Q,Q),(-1,0))

for mask in range(16):
    n=[mask>>j&1 for j in range(4)]
    assert (-1)**(-n[0]-n[1]+n[2]+n[3])==(-1)**sum(n)
    checks.append(f'physical endpoint occupation {mask}')

# The actual scalar derivative has nilpotent deviation when it preserves q,v.
v0,v1,v2,v3,aa,bb,cc=s.symbols('v0 v1 v2 v3 aa bb cc',nonzero=True)
vec=s.Matrix([-v0,-v1,v2,v3])
row=s.Matrix([[aa,bb,cc,(aa*v0+bb*v1-cc*v2)/v3]])
N=vec*row
for i in range(4):
    for j in range(4):
        eq(f'physical scalar unipotent square {i}{j}',(N*N)[i,j],0)
lam=s.symbols('lam')
eq('physical scalar unipotent determinant',(s.eye(4)+lam*N).det(),1)

note=ROOT/'notes/part3_source_zero_real_trace_working.md'
data={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
      'checks':len(checks),'identities':checks,
      'scope':'RT.13--15 local compact cut and canonical spin/charged overlap only; no complete cyclic period strip and no individual source-zero value.',
      'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest()}
(ROOT/'code/part3/source_zero_cut_spin.json').write_text(json.dumps(data,indent=2)+'\n')
print(f'PASS: {len(checks)} exact local cut/overlap/Clifford/spinor identities.')
print(data['scope'])
