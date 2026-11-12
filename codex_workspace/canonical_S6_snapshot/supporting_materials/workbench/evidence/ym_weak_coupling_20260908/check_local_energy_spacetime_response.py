"""Finite exact identities only; no continuum or interacting-theory certificate."""
import argparse
import json
from pathlib import Path
import sympy as s

checks = []


def exact(name, expr):
    value = s.simplify(expr)
    ok = value == 0
    checks.append({"name": name, "kind": "exact_symbolic_identity", "pass": ok,
                   "residual": str(value)})
    if not ok:
        raise AssertionError((name, value))


r, t, b = s.symbols("r t b", positive=True)
pi = s.pi


def lap(f):
    return s.diff(f, r, 2) + 2 * s.diff(f, r) / r


u = t*t+r*r
kernel = (9*t**4-30*t*t*r*r+9*r**4)/(pi**4*u**6)
exact("first_spatial_laplacian", lap(u**-2)-12*(r*r-t*t)/u**4)
exact("second_spatial_laplacian", lap(lap(u**-2))/(40*pi**4)-kernel)
exact("fourier_prefactor", 8*pi*t/(320*pi**5*t)-1/(40*pi**4))
exact("point_kernel", kernel.subs(r, 0)-9/(pi**4*t**8))
exact("retained_spacetime_dilation",
      kernel.subs({r:b*r, t:b*t}, simultaneous=True)-b**-8*kernel)
I00 = 1-2*t*t/u
exact("stress_tensor_0000", 12/(pi**4*u**4)*(I00**2-s.Rational(1,4))-kernel)
exact("three_vector_CT", 3*16/(2*pi**2)**2-12/pi**4)
exact("phase_space_prefactor",
      s.Rational(3,4)/(2*pi)**6*4*pi/s.Integer(15)-1/(320*pi**5))
v = s.symbols("v")
exact("ellipsoid_integral",
      pi/(4*r)*s.integrate((r*r-v*v)**2, (v,-r,r))-4*pi*r**4/15)
exact("local_tail_to_time_power",
      s.factorial(7)/(560*pi**4)-9/pi**4)
exact("local_energy_first_moment",
      s.factorial(8)/(560*pi**4)-72/pi**4)

# Two-dimensional noncommuting positive K,W analogue of the retained
# g^2 electric plus g^-2 magnetic family. This checks the response
# algebra and vacuum terms, not SU(2) continuum convergence.
g = s.symbols("g", positive=True)
ident = s.eye(2)
K = s.diag(1, 3)
W = s.Matrix([[2,1],[1,2]])
Kh = s.diag(1, 2)
Wh = s.Matrix([[3,s.Rational(1,2)],[s.Rational(1,2),1]])
Hg = g*g*K+W/(4*g*g)  # exact original coefficients with a=2
Dg = g*g*Kh+Wh/(4*g*g)
disc = s.sqrt((Hg[0,0]-Hg[1,1])**2+4*Hg[0,1]**2)
e0g = (s.trace(Hg)-disc)/2
e1g = (s.trace(Hg)+disc)/2
P0g = (e1g*ident-Hg)/disc
P1g = ident-P0g
at = lambda z: z.subs(g,1).applyfunc(s.simplify) if isinstance(z,s.MatrixBase) else s.simplify(z.subs(g,1))
H,D,V,Z,P0,P1 = map(at,(Hg,Dg,s.diff(Hg,g),s.diff(Dg,g),P0g,P1g))
delta,e0 = at(disc),at(e0g)
vv = s.simplify(s.trace(P0*V))
Pprime = -(P1*V*P0+P0*V*P1)/delta
for i in range(2):
    for j in range(2):
        exact(f"vacuum_projector_derivative_{i}{j}",
              at(s.diff(P0g,g))[i,j]-Pprime[i,j])
exact("vacuum_energy_derivative", at(s.diff(e0g,g))-vv)
exact("excitation_derivative", at(s.diff(disc,g))-s.trace(P1*V)+vv)

raw = s.Matrix([1,4-s.sqrt(17)])
psi = raw/s.sqrt((raw.T*raw)[0])
eta = P1*V*psi/delta
m = (psi.T*D*psi)[0]
mp = (psi.T*Z*psi)[0]-2*(eta.T*D*psi)[0]
xi = (D-m*ident)*psi
xip = (Z-mp*ident)*psi-(D-m*ident)*eta
qprime = s.trace(Pprime*D*P1*D+P0*Z*P1*D-P0*D*Pprime*D+P0*D*P1*Z)
exact("raw_centered_norm_derivative", qprime-2*(xip.T*xi)[0])
exact("vacuum_subtraction_derivative",
      mp-s.trace(Pprime*D+P0*Z))
exact("duhamel_excited_block",
      (xi.T*(V-vv*ident)*xi)[0]-
      (s.trace(P1*V)-vv)*(xi.T*xi)[0])
constant_xip = (V-vv*ident)*psi-(H-e0*ident)*eta
for i in range(2):
    exact(f"constant_profile_vacuum_response_{i}", constant_xip[i])

parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True)
args = parser.parse_args()
result = {"scope": __doc__, "all_pass": all(c["pass"] for c in checks),
          "exact_identity_count": len(checks), "checks": checks}
Path(args.output).write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k != "checks"}))
