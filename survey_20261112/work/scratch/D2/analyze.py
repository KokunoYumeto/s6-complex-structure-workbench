import numpy as np, math
from math import log, sqrt, pi
C0 = 9/(2*pi**2)*log(2+sqrt(3))*log(3/(2*sqrt(2)))
print("C0 =", repr(C0))
print("census R(1e8)/1e8 =", 3536002/1e8, " diff*1e8 =", 3536002-C0*1e8, " rel =", (3536002-C0*1e8)/(C0*1e8))
cnt = np.fromfile('cnt_1e7.bin', dtype=np.uint8).astype(np.int64)
X = len(cnt)-1
R = np.cumsum(cnt)
for x in (10**4,2*10**4,10**5,2*10**5,10**6,2*10**6,5*10**6,10**7):
    print(x, R[x], round(R[x]-C0*x,4))
z = np.arange(X+1)
E = R - C0*z
mask = z>=10000
r = np.abs(E)/np.sqrt(np.maximum(z,1))
i = np.argmax(np.where(mask, r, 0)); print("max |E|/sqrt on [1e4,1e7]:", r[i], "at", i, "R=", R[i])
print("max E", E.max(), int(E.argmax()), " min E", E.min(), int(E.argmin()))
# rms of E/sqrt(X) on dyadic blocks
for a in (10**4,10**5,10**6,5*10**6):
    b = min(2*a, X); seg = E[a:b+1]
    print(f"[{a},{b}] rms E = {np.sqrt((seg**2).mean()):.2f}  rms/sqrt(mid) = {np.sqrt((seg**2).mean())/sqrt(1.5*a):.4f}  mean E = {seg.mean():.2f}")
# --- full-period comparison: rho(18 z^2 - 2) = rho(3z-1) rho(3z+1), rho = 1 * chi_12
M = 3*X+2
rho = np.zeros(M+1, dtype=np.int32)
chi = {1:1, 11:1, 5:-1, 7:-1}
for d in range(1, M+1):
    c = chi.get(d % 12, 0)
    if c: rho[d::d] += c
zz = np.arange(1, X+1)
full = (rho[3*zz-1].astype(np.int64))*rho[3*zz+1]
F = np.concatenate([[0], np.cumsum(full)])
eps = 2+sqrt(3)
cfull = 9/(2*pi**2)*log(eps)**2
lam0 = log(3/(2*sqrt(2)))/log(eps)
print("lambda0 =", lam0, " predicted mean of rho(18z^2-2) =", cfull, " observed =", F[X]/X)
for x in (10**5,10**6,10**7):
    Efull = F[x]-cfull*x
    print(f"X={x}: sum rho = {F[x]}, radial disc = {Efull:.2f} (/sqrt = {Efull/sqrt(x):.4f}); lam0*radial = {lam0*Efull:.2f}; arc(angular) part = {R[x]-lam0*F[x]:.2f}; total E = {R[x]-C0*x:.2f}")
Efull = F - cfull*np.arange(X+1)
print("max |radial disc|/sqrt on [1e4,1e7] =", (np.abs(Efull)/np.sqrt(np.maximum(z,1)))[10000:].max())
ang = R - lam0*F
print("max |angular part|/sqrt on [1e4,1e7] =", (np.abs(ang)/np.sqrt(np.maximum(z,1)))[10000:].max(), " rms/sqrt at top dyadic:", np.sqrt((ang[5*10**6:]**2).mean())/sqrt(7.5e6))
print("rms radial/sqrt top dyadic:", np.sqrt((Efull[5*10**6:]**2).mean())/sqrt(7.5e6))
# consistency: cnt[z] <= rho(m_z)
print("cnt<=rho everywhere:", bool((cnt[1:]<=full).all()), " max rho =", full.max())
