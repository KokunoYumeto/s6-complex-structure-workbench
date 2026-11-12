"""Independent exact scalar-vacuum replay; reads no canonical file."""
import sympy as sp

def qmul(p, q):
    a, b, c, d = p
    e, f, g, h = q
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)

def qconj(q):
    return (q[0], -q[1], -q[2], -q[3])

def qnorm(q):
    return sum(t*t for t in q)

def check(name, expression):
    assert sp.expand(expression) == 0, name
    print("PASS:", name)

l1, l2 = sp.symbols("lambda1 lambda2", real=True)
l3 = -l1-l2
s_eig = l1*l1+l2*l2+l3*l3
n_eig = l1*l2*l3
check("exact discriminant and sharp factor 54",
      s_eig**3-54*n_eig**2
      -2*(l1-l2)**2*(l1-l3)**2*(l2-l3)**2)

eps, x, y, beta = sp.symbols("eps x y beta", real=True)
m2, Gamma, kappa = sp.symbols("m2 Gamma kappa", real=True)
omega = sp.symbols("o0:4", real=True)
v1 = sp.symbols("v0:4", real=True)
v2 = sp.symbols("w0:4", real=True)
h = x+eps*y
a1, a2, a3 = 2*h, -h+eps*beta, -h-eps*beta
q1 = tuple(eps*c for c in omega)
q2 = tuple(eps*c for c in v2)
q3 = tuple(eps*c for c in qconj(v1))
n_direct = (a1*a2*a3-a1*qnorm(q1)-a2*qnorm(q2)-a3*qnorm(q3)
            +2*qmul(qmul(q1,q2),q3)[0])
vnorm = qnorm(v1)+qnorm(v2)
Bnorm = 2*(beta**2+qnorm(omega))
vBv = beta*(qnorm(v1)-qnorm(v2))+2*qmul(qmul(qconj(v1),omega),v2)[0]
n_block = 2*h**3+eps**2*h*(vnorm-Bnorm)+eps**3*vBv
check("full exact cubic block expansion with all quaternionic directions",
      n_direct-n_block)
s_direct = a1*a1+a2*a2+a3*a3+2*(qnorm(q1)+qnorm(q2)+qnorm(q3))
metric = 6*y*y+2*vnorm+Bnorm
check("retained trace metric", s_direct-(6*x*x+12*eps*x*y+eps*eps*metric))

potential = m2*s_direct/2+Gamma*s_direct**2/4-kappa*n_direct
Hquad = sp.expand(potential).coeff(eps,2)*2
Hquad_expected = ((m2+6*Gamma*x*x)*metric+72*Gamma*x*x*y*y
                  -kappa*(12*x*y*y+2*x*vnorm-2*x*Bnorm))
check("entire unrestricted Hessian quadratic form", Hquad-Hquad_expected)
Mrad = x*(12*Gamma*x-kappa)
Mfive = 3*kappa*x
Hstationary = Hquad.subs(m2,kappa*x-6*Gamma*x*x)
check("entire stationary Hessian and eight zero directions",
      Hstationary-(6*Mrad*y*y+Mfive*Bnorm))
coords = [y,beta,*omega,*v1,*v2]
Hmatrix = sp.hessian(Hstationary,coords)/2
metric_matrix = sp.diag(6,*([2]*13))
expected_operator = sp.diag(Mrad,*([Mfive]*5),*([0]*8))
assert sp.simplify(metric_matrix.inv()*Hmatrix-expected_operator) == sp.zeros(14)
print("PASS: generalized Hessian eigenvalues, multiplicities 1+5+8")

r, K = sp.symbols("r K", nonnegative=True)
Gamma_pos = sp.symbols("Gamma_pos", positive=True)
f = m2*r*r/2+Gamma_pos*r**4/4-K*r**3/(3*sp.sqrt(6))
mc2 = K*K/(27*Gamma_pos)
rc = 2*K/(3*sp.sqrt(6)*Gamma_pos)
check("global-minimum threshold factorization",
      f-Gamma_pos*r*r*(r-rc)**2/4-(m2-mc2)*r*r/2)
check("radial derivative exact",
      sp.diff(f,r)-r*(Gamma_pos*r*r-K*r/sp.sqrt(6)+m2))
check("coexistence radial Hessian",
      Mrad.subs(x,kappa/(9*Gamma))-kappa**2/(27*Gamma))
check("coexistence fivefold Hessian",
      Mfive.subs(x,kappa/(9*Gamma))-kappa**2/(3*Gamma))
check("zero-m2 broken radial Hessian",
      Mrad.subs(x,kappa/(6*Gamma))-kappa**2/(6*Gamma))
check("zero-m2 broken fivefold Hessian",
      Mfive.subs(x,kappa/(6*Gamma))-kappa**2/(2*Gamma))
print("All independent exact checks passed. No gauge quotient claim checked.")
