"""Portable exact checks: Python + SymPy; no file/network side effects.

Run: python verify_homogeneous_quantization.py
The analytic domain, compactness and positivity proofs are in the TeX file.
One matrix identity counts once, but every entry is checked.
"""
import sympy as S

checks = 0
I = S.I
eye = S.eye(3)


def zero(name, value):
    global checks
    entries = list(value) if isinstance(value, S.MatrixBase) else [value]
    assert all(S.simplify(S.expand(v)) == 0 for v in entries), name
    checks += 1


def comm(a, b):
    return a*b-b*a


def tf(a):
    return a-S.trace(a)*eye/3


def unit(i, j):
    m = S.zeros(3)
    m[i,j] = 1
    return m


basis = []
for i in range(3):
    for j in range(i+1,3):
        basis += [(unit(i,j)-unit(j,i))/S.sqrt(2),
                  I*(unit(i,j)+unit(j,i))/S.sqrt(2)]
basis += [I*S.diag(1,-1,0)/S.sqrt(2),
          I*S.diag(1,1,-2)/S.sqrt(6)]
herm = [I*t for t in basis]
zero("gauge basis retained Gram",
     S.Matrix(8,8,lambda a,b:-S.trace(basis[a]*basis[b]))-S.eye(8))
zero("Hermitian basis retained Gram",
     S.Matrix(8,8,lambda a,b:S.trace(herm[a]*herm[b]))-S.eye(8))
zero("trace-free basis", S.Matrix([S.trace(t) for t in basis]))
for n,t in enumerate(basis):
    zero("anti-Hermitian generator "+str(n),t.H+t)

V3,g2,hbar,Gamma,K = S.symbols("V3 g2 hbar Gamma K", positive=True)
mass = S.diag(*([2*V3/g2]*24+[V3]*8+[2*V3]*6))
diffusion = S.diag(*([hbar**2*g2/(4*V3)]*24+
                    [hbar**2/(2*V3)]*8+[hbar**2/(4*V3)]*6))
zero("38 retained kinetic masses", mass.shape[0]-38)
zero("canonical quantum diffusion tensor",mass*diffusion-hbar**2*S.eye(38)/2)
zero("retained configuration volume",
     mass.det()-(2**15*V3**19/g2**12)**2)


def representation(t):
    ad = S.Matrix(8,8,lambda a,b:-S.trace(basis[a]*comm(t,basis[b])))
    # b-coordinate order is (x1,x2,x3,y1,y2,y3).
    rb = S.re(t).row_join(-S.im(t)).col_join(
        S.im(t).row_join(S.re(t)))
    return S.diag(ad,ad,ad,ad,rb)


rep = [representation(t) for t in basis]
for n,r in enumerate(rep):
    zero("mass-metric skew generator "+str(n),r.T*mass+mass*r)
    zero("zero generator divergence "+str(n),S.trace(r))
for i in range(8):
    for j in range(8):
        zero("Lie representation "+str((i,j)),
             comm(rep[i],rep[j])-representation(comm(basis[i],basis[j])))

q = S.Matrix(S.symbols("q0:38", real=True))
p = S.Matrix(S.symbols("p0:38", real=True))
vel = S.Matrix(S.symbols("v0:38", real=True))


def lincomb(coeffs, frame):
    return sum((c*t for c,t in zip(coeffs,frame)),S.zeros(3))


A = [lincomb(q[8*i:8*i+8],basis) for i in range(3)]
Pi = [lincomb(p[8*i:8*i+8],basis) for i in range(3)]
Phi = lincomb(q[24:32],herm)
PiPhi = lincomb(p[24:32],herm)
bv = S.Matrix([q[32+i]+I*q[35+i] for i in range(3)])
pib = S.Matrix([(p[32+i]+I*p[35+i])/2 for i in range(3)])
gauss = sum((comm(a,pi) for a,pi in zip(A,Pi)),S.zeros(3))-comm(Phi,PiPhi)-tf(bv*pib.H-pib*bv.H)
for n,t in enumerate(basis):
    zero("exact canonical Gauss pairing "+str(n),
         (p.T*rep[n]*q)[0]+S.trace(gauss*t))

E = [lincomb(vel[8*i:8*i+8],basis) for i in range(3)]
X = lincomb(vel[24:32],herm)
vb = S.Matrix([vel[32+i]+I*vel[35+i] for i in range(3)])
momentum_sub = dict(zip(p,mass*vel))
current = comm(Phi,X)+bv*vb.H-vb*bv.H
zero("Gauss equals volume times full field constraint",
     gauss.subs(momentum_sub)-V3*(2*sum((comm(a,e) for a,e in zip(A,E)),S.zeros(3))/g2-tf(current)))
zero("complex triplet momentum retains factor two in real duality",
     pib.subs(momentum_sub)-V3*vb)

lagkin = (vel.T*mass*vel)[0]/2
canonical_kin = (p.T*mass.inv()*p)[0]/2
zero("Legendre transform with all 38 masses",
     ((p.T*vel)[0]-lagkin-canonical_kin).subs(momentum_sub))
# Independently check the quadratic kinetic energy after the momentum map.
zero("canonical kinetic equals velocity kinetic",
     canonical_kin.subs(momentum_sub)-lagkin)

# Scalar cubic and the direct sharp bound's algebraic identities.
l1,l2,rr = S.symbols("l1 l2 rr",real=True)
lam = [l1,l2,-l1-l2]
ss = sum(x*x for x in lam)+2*rr
det = S.prod(lam)
for n,x in enumerate(lam):
    zero("extreme triplet cubic "+str(n),det-x*rr-x**3+ss*x/2)
t = S.symbols("t",real=True)
f = t**3-t/2
for pt in [S.sqrt(S.Rational(2,3)),1/S.sqrt(6)]:
    zero("sharp extremum magnitude "+str(pt),f.subs(t,pt)**2-S.Rational(1,54))
z = S.symbols("z",real=True)
young = Gamma*z**4/8-K*z**3/(3*S.sqrt(6))
critical = 2*K/(S.sqrt(6)*Gamma)
zero("retained Young critical point",S.diff(young,z).subs(z,critical))
zero("retained scalar lower constant",young.subs(z,critical)+K**4/(54*Gamma**3))

# Moving-sector oscillator allocation and constants.
eta = S.symbols("eta",positive=True)
aa = hbar**2*g2/(4*V3)
bb = V3/g2
zero("gauge kinetic-potential product",aa*bb-hbar**2/4)
for j in range(3):
    zero("kinetic allocation "+str(j),sum(S.Rational(1,2) for i in range(3) if i!=j)-1)
for j in range(3):
    for k in range(j+1,3):
        zero("magnetic allocation "+str((j,k)),
             sum(S.Rational(1,2) for i in range(3) if i in (j,k))-1)
d,mid = S.symbols("d mid",real=True)
eigen = [-(d+mid)/2,mid,(d-mid)/2]
zero("retained trace-zero eigenvalue norm",
     sum(x*x for x in eigen)-d*d/2-3*mid*mid/2)
zero("sharp adjoint trace range endpoint",
     sum(x*x for x in eigen).subs(mid,d/3)-2*d*d/3)

# Exact discarded-mode interaction, retaining original Fourier coefficients.
angle = S.symbols("angle",real=True)
q0,y0 = S.symbols("q0 y0",real=True)
quartic = S.integrate((q0+y0*S.cos(angle))**4,(angle,0,2*S.pi))/(2*S.pi)
zero("exact homogeneous/nonzero-mode quartic coupling",
     quartic-q0**4-3*q0**2*y0**2-S.Rational(3,8)*y0**4)
zero("nonzero Fourier kinetic mass",
     S.integrate(S.cos(angle)**2,(angle,0,2*S.pi))/(2*S.pi)-S.Rational(1,2))
print("PASS:",checks,"exact checks.")
