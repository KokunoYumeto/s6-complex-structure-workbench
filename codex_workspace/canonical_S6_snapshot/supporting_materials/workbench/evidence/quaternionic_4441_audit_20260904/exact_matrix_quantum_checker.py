#!/usr/bin/env python3
"""Exact bounded checks for the su(3)^3 bosonic quantum form estimate.

Requires only SymPy. No numerical tolerance, network, external data or files.
The complete analytic proof is in matrix_quantum_fragment.tex.
Each named scalar or matrix equality counts as one assertion.
"""
import sympy as sp

I = sp.I
assertions = []


def check(name, lhs, rhs):
    diff = lhs - rhs
    if isinstance(diff, sp.MatrixBase):
        diff = diff.applyfunc(lambda z: sp.simplify(sp.expand(z)))
        assert diff == sp.zeros(*diff.shape), (name, diff)
    else:
        diff = sp.simplify(sp.expand(diff))
        assert diff == 0, (name, diff)
    assertions.append(name)


def truth(name, condition):
    assert condition is True or condition == sp.true, (name, condition)
    assertions.append(name)


def unit(row, col):
    out = sp.zeros(3)
    out[row, col] = 1
    return out


def comm(x, y):
    return x*y-y*x


def inner(x, y):
    return -sp.trace(x*y)


pairs = [(0, 1), (0, 2), (1, 2)]
basis = []
for p, q in pairs:
    basis += [(unit(p, q)-unit(q, p))/sp.sqrt(2),
              I*(unit(p, q)+unit(q, p))/sp.sqrt(2)]
basis += [I*sp.diag(1, -1, 0)/sp.sqrt(2),
          I*sp.diag(1, 1, -2)/sp.sqrt(6)]
for j, e in enumerate(basis):
    check("basis anti-Hermitian " + str(j), e.H, -e)
    check("basis trace zero " + str(j), sp.trace(e), 0)
check("retained minus-trace orthonormal Gram",
      sp.Matrix(8, 8, lambda j,k: inner(basis[j], basis[k])), sp.eye(8))


def adjoint(x):
    return sp.Matrix(8, 8, lambda row,col: inner(basis[row], comm(x, basis[col])))


x = sp.Matrix(sp.symbols("x0:8", real=True))
y = sp.Matrix(sp.symbols("y0:8", real=True))
X = sum((x[j]*basis[j] for j in range(8)), sp.zeros(3))
Y = sum((y[j]*basis[j] for j in range(8)), sp.zeros(3))
DX = adjoint(X)
check("generic metric norm", inner(X, X), (x.T*x)[0])
check("generic adjoint skewness", DX.T, -DX)
check("generic commutator coordinates",
      sp.Matrix([inner(e, comm(X,Y)) for e in basis]), DX*y)
check("generic commutator quadratic form",
      inner(comm(X,Y), comm(X,Y)), (y.T*(-DX*DX)*y)[0])
check("generic adjoint Casimir trace with retained metric",
      sp.trace(-DX*DX), 6*(x.T*x)[0])

t1, t2 = sp.symbols("theta1 theta2", real=True)
eigenvalues = [t1, t2, -t1-t2]
Xd = I*sp.diag(*eigenvalues)
Dd = adjoint(Xd)
frequency_squares = []
for p,q in pairs:
    gap = eigenvalues[p]-eigenvalues[q]
    frequency_squares += [gap**2, gap**2]
frequency_squares += [sp.Integer(0), sp.Integer(0)]
check("all eight real adjoint squared frequencies",
      -Dd*Dd, sp.diag(*frequency_squares))
for j,(p,q) in enumerate(pairs):
    gap = eigenvalues[p]-eigenvalues[q]
    check("root U commutator " + str(j), comm(Xd,basis[2*j]), gap*basis[2*j+1])
    check("root V commutator " + str(j), comm(Xd,basis[2*j+1]), -gap*basis[2*j])

r, s = sp.symbols("r s", nonnegative=True)
roots = [-(2*r+s)/3, (r-s)/3, (r+2*s)/3]
norm2 = sum(v*v for v in roots)
freq_sum = 2*sum(sp.Abs(roots[p]-roots[q]) for p,q in pairs)
check("sorted eigenvalue trace", sum(roots), 0)
check("sorted lower gap", roots[1]-roots[0], r)
check("sorted upper gap", roots[2]-roots[1], s)
check("retained norm in both gaps", norm2, sp.Rational(2,3)*(r*r+r*s+s*s))
check("exact frequency sum", freq_sum, 4*(r+s))
check("sharp lower-bound remainder", freq_sum**2-24*norm2, 16*r*s)
check("sharp upper-bound remainder", 32*norm2-freq_sum**2, sp.Rational(16,3)*(r-s)**2)
check("once-per-positive-root factor", freq_sum/2, 2*(r+s))

fixtures = [
    ("regular", [-3,1,2], 6, 20),
    ("lower-wall", [-1,-1,2], 4, 12),
    ("upper-wall", [-2,1,1], 4, 12),
    ("equally-spaced", [-1,0,1], 6, 8),
    ("zero", [0,0,0], 0, 0),
]
for name, theta, rank, expected_sum in fixtures:
    mat = I*sp.diag(*theta)
    k = -adjoint(mat)**2
    truth(name + " adjoint rank", k.rank() == rank)
    check(name + " real-frequency sum",
          sum(sp.sqrt(k[j,j]) for j in range(8)), expected_sum)
    truth(name + " lower bound including degeneracy",
          expected_sum**2 >= 24*inner(mat,mat))
    truth(name + " upper bound", expected_sum**2 <= 32*inner(mat,mat))
check("lower constant attained on wall", sp.Integer(12)**2, 24*sp.Integer(6))
check("upper constant attained at equal spacing", sp.Integer(8)**2, 32*sp.Integer(2))

# Exact non-real SU(3) conjugacy; no change of metric.
rotation = sp.Matrix([[sp.Rational(3,5),0,-sp.Rational(4,5)],
                      [0,1,0],[sp.Rational(4,5),0,sp.Rational(3,5)]])
U = sp.diag(I,-I,1)*rotation
check("fixture SU3 unitary", U.H*U, sp.eye(3))
check("fixture SU3 determinant", U.det(), 1)
AdU = sp.Matrix(8, 8, lambda row,col: inner(basis[row],U*basis[col]*U.H))
check("AdU preserves the original real metric", AdU.T*AdU, sp.eye(8))
truth("AdU coefficients real", all(sp.simplify(sp.im(v))==0 for v in AdU))
wall = I*sp.diag(-1,-1,2)
wall_conjugate = U*wall*U.H
truth("wall fixture genuinely non-diagonal", wall_conjugate[0,2] != 0)
check("adjoint covariance at repeated eigenvalue",
      adjoint(wall_conjugate), AdU*adjoint(wall)*AdU.T)
check("frequency-square covariance",
      -adjoint(wall_conjugate)**2, AdU*(-adjoint(wall)**2)*AdU.T)
check("wall norm preserved", inner(wall_conjugate,wall_conjugate), inner(wall,wall))

# Exact integration-by-parts integrand identity for a complex test function.
z = sp.symbols("z", real=True)
alpha,beta,omega = sp.symbols("alpha beta omega", positive=True)
u = sp.Function("u", real=True)(z)
v = sp.Function("v", real=True)(z)
mass = u*u+v*v
square = (sp.sqrt(alpha)*sp.diff(u,z)+sp.sqrt(beta)*omega*z*u)**2
square += (sp.sqrt(alpha)*sp.diff(v,z)+sp.sqrt(beta)*omega*z*v)**2
kinetic = alpha*(sp.diff(u,z)**2+sp.diff(v,z)**2)
potential = beta*omega**2*z**2*mass
check("exact oscillator completion integrand",
      square-sp.sqrt(alpha*beta)*omega*sp.diff(z*mass,z),
      kinetic+potential-sp.sqrt(alpha*beta)*omega*mass)
width = sp.sqrt(beta/alpha)*omega
gaussian = sp.exp(-width*z*z/2)
check("oscillator ground coefficient without rescaling",
      (-alpha*sp.diff(gaussian,z,2)+beta*omega**2*z*z*gaussian)/gaussian,
      sp.sqrt(alpha*beta)*omega)

a,b = sp.symbols("a b", positive=True)
vartheta = sp.symbols("vartheta", real=True)
kin = sp.symbols("T1:4")
pots = {(0,1):sp.Symbol("V12"), (0,2):sp.Symbol("V13"), (1,2):sp.Symbol("V23")}
directed = sum((1-vartheta)*a*kin[j]/2 + b*pots[tuple(sorted((i,j)))]/2
               for i in range(3) for j in range(3) if i!=j)
check("six directed pairs count all coefficients exactly",
      vartheta*a*sum(kin)+directed, a*sum(kin)+b*sum(pots.values()))
remaining = sp.symbols("remaining", positive=True)
slice_factor = sp.sqrt((remaining*a/2)*(b/2))
check("one directed-pair ground coefficient",
      slice_factor, sp.sqrt(remaining*a*b)/2)
check("two partners and sharp root constant",
      2*slice_factor*2*sp.sqrt(6), 2*sp.sqrt(6*remaining*a*b))
check("half kinetic coercive coefficient",
      (2*sp.sqrt(6*remaining*a*b)).subs(remaining,sp.Rational(1,2)),
      2*sp.sqrt(3*a*b))

# Absolute energy-origin lower bound: derivative and exact minimizing constant.
gamma,M = sp.symbols("gamma M", positive=True)
energy = alpha/(64*M*M)+gamma*M
Mstar = (alpha/(32*gamma))**sp.Rational(1,3)
check("one-dimensional minimizing stationary equation",
      sp.diff(energy,M).subs(M,Mstar), 0)
truth("one-dimensional strict convexity", sp.diff(energy,M,2)>0)
check("one-dimensional exact minimum",
      energy.subs(M,Mstar), 3*(alpha*gamma**2)**sp.Rational(1,3)/2**sp.Rational(8,3))
bottom = 24*3*(sp.Rational(3,4)*a*a*b)**sp.Rational(1,3)/2**sp.Rational(8,3)
check("twenty-four-coordinate energy-origin constant",
      bottom, 9*sp.Rational(3,2)**sp.Rational(1,3)*a**sp.Rational(2,3)*b**sp.Rational(1,3))

# Exact coefficient bridge from the homogeneous density with volume retained.
hbar,g2,volume,velocity,momentum = sp.symbols(
    "hbar g2 volume velocity momentum", positive=True)
lag_kin = volume*velocity**2/g2
check("canonical momentum coefficient", sp.diff(lag_kin,velocity), 2*volume*velocity/g2)
legendre = (momentum*velocity-lag_kin).subs(velocity,g2*momentum/(2*volume))
check("Legendre kinetic coefficient", legendre, g2*momentum**2/(4*volume))
acoef = hbar**2*g2/(4*volume)
bcoef = volume/g2
check("exact coefficient product", acoef*bcoef, hbar**2/4)
check("native retained coercive coefficient",
      2*sp.sqrt(3*acoef*bcoef), sp.sqrt(3)*hbar)
check("native retained energy-origin constant",
      bottom.subs({a:acoef,b:bcoef}),
      9*(3*hbar**4*g2/(32*volume))**sp.Rational(1,3))

print("PASS:", len(assertions), "exact named assertions")
print("Scope: full minus-trace Gram, generic adjoint/potential identities,")
print("sharp root bounds and degenerate fixtures, oscillator coefficients,")
print("directed-pair allocation, lower-energy constant and canonical coefficients.")
print("The compactness, form closure, Fubini and approximation arguments")
print("are proved analytically in matrix_quantum_fragment.tex, not by this checker.")
