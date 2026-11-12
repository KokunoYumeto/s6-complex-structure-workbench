# check: R(X) = R_0(X) + sum_{z<=X} #{(s,t): s^2-3t^2=18z^2-2, t>=0, s>0, theta<=lambda_0}, and the exceptional point
from math import isqrt, log, sqrt
import numpy as np
cnt=np.fromfile('cnt_1e7.bin',dtype=np.uint8)
X=30000
viol=[]; arc=0; A=[0]*(X+1)
for z in range(1,X+1):
    m=18*z*z-2
    lo=isqrt(m); lo += (lo*lo<m)
    for s in range(lo,(17*z)//4+1):
        d=s*s-m
        if d%3: continue
        t=isqrt(d//3)
        if 3*t*t!=d: continue
        if not (s-4*z>t): viol.append((s,t,z))
        # theta<=lambda_0  <=>  s <= sqrt(m)*17/(12 sqrt2)  <=>  288 s^2 <= 289 m   (exact integers)
        if 288*s*s<=289*m: A[z]+=1
        else: assert 4*s==17*z, (s,t,z)   # points beyond the fixed arc are exactly the n=0 Pell face
pell=set(); a,q=1,1
while 4*a<=X:
    a,q=2*a+3*q,a+2*q
    if 4*a<=X: pell.add(4*a)
R0=len(pell)
print("violations of s-4z>t with t>=0, s<=17z/4, z<=%d:"%X, viol)
ok=all(int(cnt[z])==A[z]+(1 if z in pell else 0)-(1 if z==1 else 0) for z in range(1,X+1))
print("per-height identity cnt[z] = A_z + [z on Pell face] for all z<=X:", ok, " R0(X)=",R0, " sum A =",sum(A), " R(X)=",int(cnt[:X+1].sum()))
