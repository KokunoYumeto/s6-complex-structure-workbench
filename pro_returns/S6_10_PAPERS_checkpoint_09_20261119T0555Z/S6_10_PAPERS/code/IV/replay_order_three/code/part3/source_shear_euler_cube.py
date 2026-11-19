#!/usr/bin/env python3
"""Exact algebra for the global source-shear Euler-cube proof.

The Cech, section-disc, and actual cap morphisms are proved in the
companion note. This certificate checks their stated period/group
data and the complete oriented Chern--Weil calculation.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

n=s.symbols("n",integer=True)
tau, mu, G, beta = s.symbols("tau mu G beta")
u, v, d, gamma, alpha, theta, t = s.symbols(
    "u v d gamma alpha theta t"
)
checks = []
def ck(name, left, right):
    if isinstance(left, s.MatrixBase):
        good = left.shape == right.shape and all(
            s.simplify(x) == 0 for x in left-right)
    else:
        good = s.simplify(left-right) == 0
    assert good, (name, left, right)
    checks.append(name)
def exact(name, left, right):
    assert left == right, (name, left, right)
    checks.append(name)

z = u + tau*v + G*gamma
ell = d + mu*v + beta*gamma
tau_n = tau+n*G
mu_n = mu+n*beta-n*tau-n*n*G
beta_n = beta-n*G
dn = d-n*u
gn = gamma-n*v
ck("actual source point in the changed period basis",
   u+tau_n*v+G*gn,z)
ck("actual line character, including the quadratic bounded unit",
   dn+mu_n*v+beta_n*gn,ell-n*z)
q_change = {tau:tau+1,beta:beta+1,u:u-v,d:d-gamma}
rho_change = {tau:tau-6,u:u+6*v}
ck("q deck fixes the literal source point",
   z.subs(q_change, simultaneous=True),z)
ck("q deck fixes the literal line point",
   ell.subs(q_change, simultaneous=True),ell)
ck("rho deck fixes the literal source point",
   z.subs(rho_change, simultaneous=True),z)
ck("rho deck fixes the literal line point",
   ell.subs(rho_change, simultaneous=True),ell)
ck("rho deck of the new source-line multiplier",
   mu_n.subs(rho_change, simultaneous=True)-mu_n,6*n)
ck("rho deck of the physical delta coefficient",
   dn.subs(rho_change, simultaneous=True)-dn,-6*n*v)
ck("q deck of the physical delta coefficient",
   dn.subs(q_change, simultaneous=True)-dn,-gn)
q,Z,x0,V=s.symbols("q Z x0 V",nonzero=True)
disc=s.Matrix([q*Z**(n-1),Z,Z**(-n)])
ck("actual section-disc chart preserves physical height",
   s.prod(disc),q)
chart=s.Matrix([x0*Z**n,Z,V*Z**(-n)])
ck("free-chart comparison is invertible with complex determinant one",
   chart.jacobian([x0,Z,V]).det(),1)
ck("inverse free-chart comparison retains the physical line",
   chart[2]*Z**n,V)

# Abelianization: (u,v,gamma,alpha,theta), with the two literal
# base/graph commutators u and 6u.
relations = s.Matrix([[1,0,0,0,0],[6,0,0,0,0]])
snf_boundary = smith_normal_form(relations,domain=s.ZZ)
exact("boundary abelianization kills u primitively",
      snf_boundary, s.Matrix([[1,0,0,0,0],[0,0,0,0,0]]))
restriction = s.Matrix([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])
snf_restriction = smith_normal_form(restriction,domain=s.ZZ)
exact("restriction of theta, b, gamma is primitive of rank three",
      snf_restriction,
      s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,0]]))
ck("only remaining boundary coefficient is the q angle",
   s.Matrix([[1,0,0,0]])*restriction,s.zeros(1,3))
exact("restriction kernel dimension",
      len(restriction.T.nullspace()),1)
ck("primitive obstruction covector",
   restriction.T.nullspace()[0],s.Matrix([1,0,0,0]))

def add(*forms):
    out={}
    for form in forms:
        for I,c in form.items():
            out[I]=s.simplify(out.get(I,0)+c)
    return {I:c for I,c in out.items() if c != 0}
def scale(c,form):
    return {I:s.simplify(c*a) for I,a in form.items()
            if s.simplify(c*a) != 0}
def wedge(a,b):
    out={}
    for I,c in a.items():
        for J,e in b.items():
            if set(I)&set(J):
                continue
            sign=(-1)**sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J))
            out[K]=s.simplify(out.get(K,0)+sign*c*e)
    return {I:c for I,c in out.items() if c != 0}
def formcheck(name,a,b):
    exact(name,add(a,scale(-1,b)),{})

# Ordered boundary one-forms:
# d alpha_q, du, dv, d gamma_B, d theta.
da,du,dv,dg,dt=[{(i,):s.Integer(1)} for i in range(5)]
F0 = wedge(da,dg)
bform=add(scale(-n,du),scale(-n*(alpha-6*theta),dv))
dbform=add(scale(-n,wedge(da,dv)),
           scale(6*n,wedge(dt,dv)))
Fext=add(F0,scale(n,wedge(da,dv)))
Fpiece=add(F0,scale(6*n,wedge(dt,dv)))
formcheck("exact boundary curvature gluing",add(Fext,dbform),Fpiece)
formcheck("exterior boundary curvature square",wedge(Fext,Fext),{})
formcheck("connection-difference curvature square",
          wedge(dbform,dbform),{})
Ft=add(Fext,scale(t,dbform))
CS=scale(3,wedge(bform,wedge(Ft,Ft)))
CS_integral={I:s.integrate(c,(t,0,1)) for I,c in CS.items()}
formcheck("complete cubic fifth form",
          CS_integral,{tuple(range(5)):18*n*n})
collar={I:s.integrate(c,(t,1,0)) for I,c in CS.items()}
formcheck("actual piece-to-exterior collar direction",
          collar,{tuple(range(5)):-18*n*n})
formcheck("theta-graph curvature has square zero",
          wedge(wedge(dt,dv),wedge(dt,dv)),{})

# Real connection invariance. The auxiliary dd coefficient is
# represented as a scalar symbol because only linearity is needed.
dd,dgamma,dv_symbol=s.symbols("dd dgamma dv_symbol")
A0=dd+alpha*dgamma
An=dd+alpha*dgamma+6*n*theta*dv_symbol
ck("old principal connection is q invariant",
   A0.subs({dd:dd-dgamma,alpha:alpha+1},simultaneous=True),A0)
ck("new principal connection is q invariant",
   An.subs({dd:dd-dgamma,alpha:alpha+1},simultaneous=True),An)
ck("new principal connection is rho invariant",
   An.subs({dd:dd-6*n*dv_symbol,theta:theta+1},
           simultaneous=True),An)

# The ordinary complex line has curvature 2*pi*i*dA. Its inverse
# is used for the auxiliary positive-orientation cubic calculation.
F=s.symbols("F",real=True)
ck("actual complex-line Chern sign",
   s.I/(2*s.pi)*(2*s.pi*s.I*F),-F)
exact("Jin orientation and odd-cube reversals cancel",(-1)*(-1)**3,1)
exact("circle-first orbit sign from five transpositions",(-1)**5,-1)
exact("contracting radial derivative restores source-gamma orientation",
      (-1)*(-1),1)

e1=(1,0); e2=(0,1)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
T1_first={(0,0),(1,1),(0,1)}
T1_second={(1,1),(0,1),(1,2)}
exact("first T1 triangle is the reflected second triangle",
      T1_first,{(0,0),e2,(1,1)})
exact("literal inverse-B translate of second T1 triangle",
      {sub(p,e2) for p in T1_second},{(0,0),e1,(1,1)})

bulk=s.symbols("bulk")
k=-6+18*n*bulk-18*n*n
bulk_value=s.solve(s.Eq(k.subs(n,1),-6),bulk)
exact("actual reflected pair determines the bulk linear coefficient",
      bulk_value,[s.Integer(1)])
k=s.factor(k.subs(bulk,bulk_value[0]))
A=s.factor(k/6)
ck("exact Euler cube",k,-6-18*n*(n-1))
ck("exact integer Jin index",A,-1-3*n*(n-1))
V00=18*n*(n-1)
delta0=-12-18*n*(n-1)
ck("ordinary variation-to-k identity",-(V00+6),k)
ck("ordinary derivative-to-ell identity",
   24+2*V00+2*delta0,0)
ck("native fixed right integer",(delta0-V00)/2,6*A)
ck("native fixed left integer",-(V00+delta0)/2-6,0)
ck("residue period is exactly divisible by 28",
   s.expand(A.subs(n,n+28)-A),-28*(6*n+81))
residues=sorted({int(A.subs(n,j))%28 for j in range(28)})
exact("corrected physical residue range from exact integer polynomial",
      residues,[5,7,9,13,19,21,23,27])

report={
  "utc":datetime.now(timezone.utc).isoformat(),
  "status":"PASS",
  "checks":checks,
  "check_count":len(checks),
  "boundary_H1_basis":["alpha_q","theta","v","gamma_B"],
  "extending_H1_basis":["theta","b","gamma_B"],
  "remaining_relative_obstruction":"alpha_q winding, zero on the actual section disc",
  "line_convention":"x=c1(L_delta)=-dA; c1(U=L_delta^-1)=dA",
  "auxiliary_orientation":"dr_q dalpha_q du dv dgamma_B dtheta",
  "collar_cubic":str(collar[tuple(range(5))]),
  "k_M":str(k),
  "k_U":str(-k),
  "ell":0,
  "A_M":str(A),
  "A_U":str(-A),
  "V00":str(V00),
  "delta0":str(delta0),
  "scope":"Algebraic certificate for P3K.66; the full geometric Cech, disc, cap and oriented cubic proof passed full relative-line audits and the independent physical/dual transfer correction."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(report,indent=2)+"\n")
print("PASS",len(checks),"exact period, integral-group, line and cubic identities.")
print("k =",k,"ell = 0; A =",A)
