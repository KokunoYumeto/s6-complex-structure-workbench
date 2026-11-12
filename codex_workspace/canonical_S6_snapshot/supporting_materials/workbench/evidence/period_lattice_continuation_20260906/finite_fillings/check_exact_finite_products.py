"""Read-only exact arithmetic companion to AUDIT.md; no source or output writes."""
import json
import sympy as s

I = s.I
rho = (1 + I*s.sqrt(3))/2
B = s.Symbol('B')
delta = s.Matrix([0, 0, 0, 1])
uhat = s.Matrix([0, 1, 0, 0])
gamma = s.Matrix([[1, 0, 0, 0]])
data = [
    dict(j=1, m=3, tau=rho, mu=(2-rho)/3,
         A=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),
         eps=s.Matrix([1,2,-4,0]), v=s.Matrix([1,2,-4,0]),
         e=s.Matrix([0,1,-2,0]), f=s.Matrix([0,0,-3,1]),
         h=3, c=s.Rational(2,3), r=rho-1, d=3,
         psi=s.Matrix([[0,2,1,3]])),
    dict(j=2, m=4, tau=I, mu=(1-I)/2,
         A=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]),
         eps=s.Matrix([1,3,-3,0]), v=s.Matrix([-1,-3,3,0]),
         e=s.Matrix([0,1,-1,0]), f=s.Matrix([0,0,-2,1]),
         h=2, c=s.Rational(1,2), r=-I, d=2,
         psi=s.Matrix([[0,1,1,2]])),
]
results = []
for a in data:
    A, tau, mu = a['A'], a['tau'], a['mu']
    eps, e, f, v = a['eps'], a['e'], a['f'], a['v']
    Pi = s.Matrix([[6*mu,tau,1,0],[B,mu,0,1]])
    kappa = B + (2 if a['j']==1 else 3)*mu
    R = (s.Matrix([[-1/tau,0],[(1-mu)/tau,1]]) if a['j']==1
         else s.Matrix([[1/tau,0],[-mu/tau,1]]))
    Z = lambda M: M.applyfunc(s.simplify) == s.zeros(*M.shape)
    assert A**a['m'] == s.eye(4)
    assert A*eps == eps and A*v == v and A*delta == delta
    assert Z(R*Pi - Pi*A)
    assert Z(Pi*eps - s.Matrix([0,kappa]))
    assert Z(Pi*delta - s.Matrix([0,1]))
    assert Z(Pi*e - s.Matrix([tau-(2 if a['j']==1 else 1),
                              -(tau-(2 if a['j']==1 else 1))/a['h']]))
    assert Z(Pi*f - s.Matrix([-a['h'],1]))
    assert abs(s.Matrix.hstack(eps,delta,e,f).det()) == a['d']
    assert uhat == a['c']*delta + e - a['c']*f
    assert Z(Pi*uhat - s.Matrix([tau,a['c']-tau/a['h']]))
    assert Z(R*s.Matrix([1,-s.Rational(1,a['h'])])
             -a['r']*s.Matrix([1,-s.Rational(1,a['h'])]))
    assert s.simplify(a['r']**a['m']-1) == 0
    # FF20: verify every retained moving-period image, including unimodularity.
    moving_periods = s.Matrix([[tau-(2 if a['j']==1 else 1), -a['h']]])
    moving_rotation = (s.Matrix([[-2,-3],[1,1]]) if a['j']==1
                       else s.Matrix([[1,2],[-1,-1]]))
    assert Z(a['r']*moving_periods - moving_periods*moving_rotation)
    assert moving_rotation.det() == 1
    assert moving_rotation**a['m'] == s.eye(2)
    assert s.simplify(a['r']*tau-tau
                     + (tau-(2 if a['j']==1 else 1))
                     + (3 if a['j']==1 else 0)) == 0
    assert gamma*A == gamma and a['psi']*A == a['psi']
    for power in range(1,a['m']):
        assert (A**power-s.eye(4)).rank() == 2
        assert gamma*A**power == gamma and a['psi']*A**power == a['psi']
        assert s.Rational(power,a['m'])*(gamma*v)[0] not in s.ZZ
    for col in (A-s.eye(4)).columnspace():
        assert (gamma*col)[0] == 0 and (a['psi']*col)[0] == 0
    results.append({'j':a['j'], 'm':a['m'], 'product_cover_degree':a['d'],
                    'surface_product_cover_degree':a['d']*a['m'],
                    'gamma_v':int((gamma*v)[0]),
                    'moving_rotation_matrix':[[int(x) for x in row]
                                               for row in moving_rotation.tolist()],
                    'moving_rotation_det':int(moving_rotation.det()),
                    'all_exact_assertions_passed':True})
print(json.dumps(results,indent=2))
