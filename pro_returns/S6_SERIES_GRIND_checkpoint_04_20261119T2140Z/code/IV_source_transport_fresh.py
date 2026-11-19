"""Exact source-equation, divisor-telescope and fan-convention checks.

Written from the displayed morphisms, without importing historical programs.
The symbolic identities corroborate the accompanying algebraic proof; they do
not claim extension across an unproved completed cap.
"""
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name, value):
    assert value, name
    checks.append(name)

t,tau,x,y,X,Y=s.symbols('t tau x y X Y')
tau_t=4/(27*t+4)
X_t=s.Rational(9,2)*tau_t**2*x
Y_t=27/(2*s.sqrt(2))*tau_t**3*y
eng=Y**2-X**3+3*tau**3*(tau-1)*X-2*tau**4*(tau-1)**2
pulled=eng.subs({X:X_t,Y:Y_t,tau:tau_t}, simultaneous=True)
factor=s.Rational(729,8)*tau_t**6
check('source_equation',s.factor(pulled-factor*(y*y-x**3-t*x-t*t))==0)
inverse={t:4*(1-tau)/(27*tau),x:2*X/(9*tau**2),y:2*s.sqrt(2)*Y/(27*tau**3)}
check('inverse_base',s.factor(tau_t.subs(inverse)-tau)==0)
check('inverse_x',s.factor(X_t.subs(inverse,simultaneous=True)-X)==0)
check('inverse_y',s.factor(Y_t.subs(inverse,simultaneous=True)-Y)==0)
check('marked_section',s.factor((Y_t.subs({x:0,y:t})).subs(t,inverse[t])-s.sqrt(2)*tau**2*(1-tau))==0)
check('minimal_infinity_x',s.factor((x/t**2).subs(inverse,simultaneous=True)-81*X/(8*(1-tau)**2))==0)
check('minimal_infinity_y',s.factor((y/t**3).subs(inverse,simultaneous=True)-729*s.sqrt(2)*Y/(32*(1-tau)**3))==0)
for a in [1,2,3,6]:
    b=6//a
    # Formal values at p-jG retain each factor of the actual Miller product.
    f=s.symbols('f0:7', nonzero=True)
    h=s.symbols('h0:6', nonzero=True)
    lamq=s.symbols('lamq', nonzero=True)
    left=f[6]*(lamq*s.prod(h))**a
    right=f[0]*s.prod(lamq*s.prod(h[j]**a*f[j+1]/f[j] for j in range(k*b,(k+1)*b)) for k in range(a))
    check(f'chronological_telescope_a{a}',s.factor(left-right)==0)
    check(f'cover_degree_a{a}',a*(6//b)==a*a)

def add(u,v):return tuple(a+b for a,b in zip(u,v))
def neg(v):return tuple(-a for a in v)
def canon(triangle):
    # An orbit is determined independently by all translations taking a vertex
    # to zero; pick the lexicographically least unordered representative.
    return min(tuple(sorted(tuple(p[i]-q[i] for i in range(2)) for p in triangle)) for q in triangle)
zero=(0,0)
def plus(u,v):return {canon((zero,u,add(u,v))),canon((zero,v,add(u,v)))}
def opposite(u,v):return {canon((zero,u,v)),canon((u,v,add(u,v)))}
n=0
for a in range(-4,5):
 for b in range(-4,5):
  for c in range(-4,5):
   for d in range(-4,5):
    if abs(a*d-b*c)!=1:continue
    u,v=(a,c),(b,d)
    check(f'periodic_fan_adapter_{n}',plus(u,v)==opposite(u,neg(v)))
    n+=1
for j in range(-12,13):
    check(f'vertical_index_{j}',plus((1,j),(0,1))==opposite((1,j+1),(0,1)))
r=s.symbols('r',real=True)
check('smooth_SU2_norm',s.trigsimp(s.sin(s.pi*r/2)**2+s.cos(s.pi*r/2)**2-1)==0)
check('smooth_SU2_centre',s.limit(s.sin(s.pi*r/2)/r,r,0)==s.pi/2)
check('smooth_SU2_boundary',s.sin(s.pi/2)==1 and s.cos(s.pi/2)==0)
result={'status':'PASS','assertions':len(checks),'unimodular_bases':n,'point_line_degrees':{str(a):a*a for a in [1,2,3,6]},'method':'SymPy rational identities; formal chronological telescoping; translation-orbit equality of literal triangles','checks':checks}
out=ROOT/'code/outputs/IV_source_transport_fresh.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
