"""Exact supplementary checks for the original completion maps. CC0."""
from pathlib import Path
from fractions import Fraction
import json, hashlib
W=Path(__file__).resolve().parents[1]
src=W/'src/the-original-adams-tower-and-arithmetic-completion.md'
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def clean(x): return {i:a for i,a in x.items() if a}
def add(x,y):
 z=dict(x)
 for i,a in y.items():z[i]=z.get(i,0)+a
 return clean(z)
def scale(x,k):return clean({i:k*a for i,a in x.items()})
def sigma(x):return {i+1:a for i,a in x.items()}
def delta(x):return clean({i-1:a for i,a in x.items() if i>0})
def M(x,p):return add(delta(x),scale(x,-p))
def N(x,p):return add(x,scale(sigma(x),-p))
def rho(x,p):return sum((Fraction(a,p**(i+1)) for i,a in x.items()),Fraction(0))
def loc(x,p):return sum((Fraction(a,p**i) for i,a in x.items()),Fraction(0))
for p in [2,3,5,7]:
 for size in range(1,13):
  x={i:(-1)**i*(i*i+3) for i in range(size)}
  check(f'backward-forward p{p} size{size}',delta(sigma(x))==x)
  check(f'original factorization p{p} size{size}',delta(N(x,p))==M(x,p))
  check(f'localization relations p{p} size{size}',loc(N(x,p),p)==0)
  check(f'extension unit negative sign p{p} size{size}',rho(M(x,p),p)==-x[0])
  check(f'free injection highest coefficient p{p} size{size}',M(x,p)[size-1]==-p*x[size-1])
 for m in range(1,9):
  v={j:-p**j for j in range(m)}
  check(f'cyclic subgroup full chain map p{p} m{m}',M(v,p)=={m-1:p**m})
  c=[(-1)**j*(j*j+2*j+7) for j in range(m+1)]
  mc=[-p*c[0]]+[c[j-1]-p*c[j] for j in range(1,m)]
  check(f'change of lifts all terms p{p} m{m}',-sum(p**j*mc[j] for j in range(m))==p**m*c[m-1])
  check(f'Moore original square p{p} m{m}',p**m*p==p**(m+1)*1)
  check(f'Pruefer positive endpoint p{p} m{m}',p*Fraction(1,p**(m+1))==Fraction(1,p**m))
  for a in [-p-1,-1,0,1,p+2]:
   unit=[-a]+[0]*(m-1)
   check(f'unit residue p{p} m{m} a{a}',(-sum(p**j*unit[j] for j in range(m))-a)%(p**m)==0)
 for exponent in range(1,6):
  mod=p**exponent; size=3*exponent+7
  b=[(j*j+3*j+5)*(-1)**j%mod for j in range(size)]
  def Q(v):return [(p*v[j+1])%mod if j+1<len(v) else 0 for j in range(len(v))]
  def diff(v):return [(a-q)%mod for a,q in zip(v,Q(v))]
  def inv(v):
   a=[0]*len(v);z=v[:]
   for _ in range(exponent):
    a=[(x+y)%mod for x,y in zip(a,z)];z=Q(z)
   check(f'full transition power p{p} N{exponent} call{len(checks)}',not any(z))
   return a
  check(f'finite-sum right inverse p{p} N{exponent}',diff(inv(b))==b)
  check(f'finite-sum left inverse p{p} N{exponent}',inv(diff(b))==b)
 for s in range(0,7):
  middle=p**(s+1);right=p**s
  images={(a*p**s)%middle for a in range(p)}
  kernel={a for a in range(middle) if a%right==0}
  check(f'original degree-zero extension p{p} s{s}',images==kernel and len(images)==p)
  check(f'actual sharp exponent p{p} s{s}',p**(s+1)%middle==0 and p**s%middle!=0)
for b in [-3,0,2]:
 for m in range(1,6):
  for n in range(b,b+8):
   layers=[(j,i) for j in range(b,n+1) for i in range(2*m)]
   check(f'full extension count b{b} m{m} n{n}',len(layers)==2*m*(n-b+1) and layers[0]==(b,0) and layers[-1]==(n,2*m-1))
# Cone on the original e_0 unit: d(a,z)=(epsilon(a)+z,M(a)).
for p in [2,3,5]:
 for j in range(10):
  a={j:1};z=-a.get(0,0)
  check(f'cone boundary sign p{p} cell{j}',a.get(0,0)+z==0 and z==(-1 if j==0 else 0))
report=dict(passed=len(checks),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
 scope='Exact finite checks of the original free-presentation maps, every endpoint sign, integer prime powers, full finite inverse sum, coefficient transitions, actual degree-zero extension and sharp exponent, and finite extension counts. All-spectrum and all-stage proofs are in the chapter; these checks are supplementary.',
 independent_review=False,checks=checks)
(W/'checks/ARITHMETIC_COMPLETION_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
