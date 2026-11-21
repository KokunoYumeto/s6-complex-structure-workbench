"""Post-preread comparison of every displayed scalar bound in nine target proofs.

New method: outward interval transcendental evaluation plus explicitly bounded
positive Fourier tails, and exact rational/symbolic algebra. This file was
written after opening the target proofs; it has no preread-independence claim.
No attached verification program is imported.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib, json
import mpmath as mp
import sympy as sy

iv=mp.iv
iv.dps=90
pi=iv.pi
out={}
def v(a,b=1): return iv.mpf(a)/b
def check(name,value,lo=None,hi=None):
    if lo is not None: assert value.a>lo,(name,value,lo)
    if hi is not None: assert value.b<hi,(name,value,hi)
    out[name]=str(value)
    return value
def cosh(x): return (iv.exp(x)+iv.exp(-x))/2
def sinh(x): return (iv.exp(x)-iv.exp(-x))/2

# C8.1: original endpoint and eta bounds, separately from the preread proof.
def F(T): return iv.exp(pi*T/12)*(1+2*iv.exp(-pi*T)/(1-iv.exp(-3*pi*T)))
for a,b,c in [(6,7,14211),(1,1,14116),(11,10,14180),(7,5,14782),(2,1,16944)]:
    check(f"C8.1 F({a}/{b})",F(v(a,b)),hi=v(c,10000))
for a,b,c in [(6,7,10047),(1,1,10019)]:
    r=iv.exp(-2*pi*v(a,b))
    check(f"C8.1 eta({a}/{b})",iv.exp(r/(1-r)**2),hi=v(c,10000))
assert Q(14211*10047,10**8)<Q(17,10)
assert Q(16944*10019,10**8)<Q(17,10)
assert Q(14782*10047,10**8)<Q(3,2)
assert Q(14211*10047,10**8)<Q(143,100)
b0=v(43,100);r0=iv.exp(-4*pi)
cusp_error=1/sinh(pi*b0)**2+8*(r0/(1-r0)**3+
    (iv.exp(-2*pi)/(1-iv.exp(-2*pi))**2+
     iv.exp(-6*pi)/(1-iv.exp(-6*pi))**2)/(2*(1-r0)))
check("C8.1 cusp exclusion",cusp_error,hi=v(1,3))
cusp_norm=2*cosh(pi*b0)*iv.exp(-pi/3-pi*b0*b0/2)*iv.exp(
    2*cosh(2*pi*b0)*r0/(1-r0)+r0*r0/(1-r0*r0))
check("C8.1 cusp norm",cusp_norm,hi=v(541,500))
check("C8.1 monotonicity endpoint",sinh(pi*b0)/cosh(pi*b0)-b0,lo=0)

# Infinite Gaussian sums, with twelve initial terms and an explicit tail.
# The degree-adjusted successive-term quotient decreases beyond N.
def gaussian_sum(T,H,k,shift=0,N=12):
    total=iv.mpf(0)
    for n in range(N):
        m=n+shift
        total+=m**k*iv.exp(-pi*T*m*m)*cosh(2*pi*H*m)
    m=N+shift
    # Replace cosh by exp for the tail, preserving a strict majorant.
    first=m**k*iv.exp(-pi*T*m*m+2*pi*H*m)
    ratio=((iv.mpf(m)+1)/iv.mpf(m))**k*iv.exp(-pi*T*(2*m+1)+2*pi*H)
    assert ratio.b<1
    return total+first/(1-ratio)

# C8.2: full polydisc majorants and all printed rational margins.
A=[gaussian_sum(v(9,10),v(1,4),k,shift=1) for k in range(3)]
a0=2*A[0];a1=4*pi*A[1];a2=8*pi*pi*A[2]
check("C8.2 a0",a0,hi=v(3,10))
check("C8.2 a1",a1,hi=v(19,10))
check("C8.2 a2",a2,hi=12)
r=iv.exp(-9*pi/5)
G=a2/(1-a0)+a1*a1/(1-a0)**2+pi*pi/3*(1+24*r/(1-r)**3)
H=-iv.ln(1-a0)+11*pi/120+r/(1-r)**2
check("C8.2 G polydisc",G,hi=30)
check("C8.2 H polydisc",H,hi=v(2,3))

theta2=[];theta4=[]
for k in range(3):
    q2=2*pi**k*gaussian_sum(v(49,50),v(0),2*k,shift=v(1,2))
    q4=2*pi**k*gaussian_sum(v(49,50),v(0),2*k,shift=1)+(1 if k==0 else 0)
    theta2.append(q2);theta4.append(q4)
    check(f"C8.2 theta2 derivative {k}",q2,hi=v([929,742,670][k],1000))
    check(f"C8.2 theta4 derivative {k}",q4,hi=v([1093,290,911][k],1000))
T2=list(map(lambda x:v(x,1000),[929,742,670]))
T4=list(map(lambda x:v(x,1000),[1093,290,911]))
ep=4*pi*pi/3*(T2[0]**3*T2[1]+T4[0]**3*T4[1])
epp=pi*pi/3*(12*T2[0]**2*T2[1]**2+4*T2[0]**3*T2[2]+
              12*T4[0]**2*T4[1]**2+4*T4[0]**3*T4[2])
check("C8.2 e prime from rational table",ep,hi=14)
check("C8.2 e second from rational table",epp,hi=60)
r=v(1,470)
check("C8.2 q bound",iv.exp(-2*pi*v(49,50)),hi=r)
gp=640*pi**5*r*(1+11*r+11*r*r+r**3)/(1-r)**7
Ep=16*pi**3*r*(1+r)/(1-r)**5
E6pp=2016*pi*pi*r*(1+r)*(1+120*r+1191*r*r+2416*r**3+
                              1191*r**4+120*r**5+r**6)/(1-r)**11
check("C8.2 g2 prime",gp,hi=500)
check("C8.2 E prime",Ep,hi=2)
check("C8.2 E6 second",E6pp,hi=100)

q=iv.exp(-2*pi);N=20
E4=1+240*sum((n**3*q**n/(1-q**n) for n in range(1,N+1)),iv.mpf(0))
m=N+1
tail=240*m**3*q**m/(1-q)/(1-q*(v(m+1,m))**3)
E4+=iv.mpf([0,1])*tail
g=pi**4*E4/3
check("C8.2 g",g,lo=47,hi=v(95,2))
check("C8.2 d",2*g/(3*pi),lo=v(99,10))
assert Q(5,2)+3*Q(7,25)**2==Q(3419,1250)
assert Q(95,2)+Q(3419,1250)==Q(62794,1250)
assert (47-Q(3419,1250))/100==Q(55331,125000)>Q(4426,10000)
rouche=Q(7,25)+Q(7,25)*Q(62794,1250)/10000+30*Q(4,25)**3/(1-Q(4,25))
assert rouche<Q(4277,10000)
Qbound=Q(3419,1250)+Q(7,25)*Q(62794,1250)/100+30*Q(4,25)**3/((1-Q(4,25))/100)
assert Qbound<Q(88,5)
assert (Q(95,2)+Q(88,5))/Q(93,10)==7
check("C8.2 H0 second",v(14)/(4*pi),hi=v(6,5))
assert Q(62794,1250)/12<Q(21,5)
assert Q(2,3)*4**6*Q(1,100)/(1-Q(16,100))==Q(2048,63)
check("C8.2 Gaussian coefficient",7*pi/(1-v(1,50)),hi=v(1100,49))
C=Q(147,5)+56+Q(21,5)+Q(2048,63)+Q(1100,49)
assert C<150
out["C8.2 exact rational margins"]={
 "Rouche remainder":str(rouche),"Q+g bound":str(Qbound),"quartic C":str(C)}

# C8.3: covering-disc constants.
check("C8.3 E4(i)",E4,lo=v(29,20))
check("C8.3 E6 prime lower",pi*v(29,20)**2,lo=v(13,2))
check("C8.3 Delta upper at q=1/470",r*iv.exp(24*r/(1-r)),hi=v(1,400))
assert Q(121,43200)>Q(1,500)

# C8.4: every coarse coefficient and its stated one-disc inequality.
coeffs=[Q(217,27),Q(20486,729),Q(10910,19683),Q(161383,177147),Q(245,14348907)]
assert all(c<z for c,z in zip(coeffs,[Q(81,10),29,1,1,1]))
M=Q(81,10)+Q(29,28)+Q(1,28**2)+Q(1,28**3)+Q(1,28**4)
assert M<10
out["C8.4 coarse M"]=str(M)

# C8.12: independently expose and settle the omitted E4 factor.
A,B,ppi=sy.symbols('E4 E6 pi',nonzero=True)
t=A**3/(A**3-B**2);tp=-2*ppi*sy.I*t*B/A
ratio=sy.factor((t-1)/tp)
correct=-B/(2*ppi*sy.I*A*A)
assert sy.simplify(ratio-correct)==0
wrong=-B/(2*ppi*sy.I*A)
out["C8.12 correct ratio"]=str(ratio)
out["C8.12 printed-minus-correct"]=str(sy.factor(wrong-correct))
assert sy.simplify(wrong-correct)!=0

out.update(timestamp_utc=datetime.now(timezone.utc).isoformat(),
    program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    mpmath_version=mp.__version__,sympy_version=sy.__version__,interval_dps=iv.dps,
    scope="Post-reading recomputation; no target-proof independence claimed for newly read constants.")
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
