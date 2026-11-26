import sympy as s

X, z, a, b, q, qx, qxx, qxz, qzz = s.symbols('X z a b q qx qxx qxz qzz')
N = a + b
Lxx = -a / X**2 + b * ((2*qx + X*qxx)/(X*q) - (q + X*qx)**2/(X*q)**2)
J = ((N+b)*qx + b*X*qxx)*qzz - b*X*qxz**2
det_log = 2*b/(X*q) * (Lxx*b*qzz/q - (b*qxz/q)**2)
claimed = 2*b**2*J/(X**2*q**3)
assert s.factor((det_log-claimed).subs(q, -b*X*qx/N)) == 0
assert s.factor(claimed.subs({a:1, b:1})*(X**2*q)**3 - 2*X**4*J.subs({a:1,b:1})) == 0

H = z*(X-z)*(X-2*z)
G = 2*H+X*s.diff(H,X)
Hz = s.diff(H,z)
J_example = s.det(s.Matrix([[s.diff(G,X),s.diff(G,z)],[s.diff(Hz,X),s.diff(Hz,z)]]))
gb = s.groebner([G-2,Hz], X,z, order='lex')
expected = [3*X-5*z**4-14*z,25*z**6+50*z**3-2]
assert all(gb.reduce(e)[1] == 0 for e in expected)
egb = s.groebner(expected,X,z,order='lex')
assert all(egb.reduce(e)[1] == 0 for e in [G-2,Hz])
eliminant = expected[1]
assert s.gcd(eliminant,s.diff(eliminant,z)) == 1
for extra in [X,s.diff(H,X),J_example]:
    assert list(s.groebner([G-2,Hz,extra],X,z,order='lex')) == [1]
print('Weighted logarithmic Hessian identity verified symbolically; its a=b=1 specialization is 2 X^4 J.')
print('The retained six-root example has the stated two-generator ideal, square-free eliminant, and unit ideals after adjoining X, H_X or J.')
