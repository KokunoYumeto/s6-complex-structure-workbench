"""Exact neighborhood-jet checks for C.2.UN.38."""
import sympy as s
z, w, beta, c = s.symbols('z w beta c', nonzero=True)
count=0
for r in range(1,9):
    F=s.Matrix([beta**r*z+w**r,beta*w])
    assert s.simplify(F.jacobian([z,w]).det()-beta**(r+1))==0
    # The actual canonical form dz^dw / w^(r+1) is invariant.
    assert s.simplify(F.jacobian([z,w]).det()/(beta*w)**(r+1)
                      -1/w**(r+1))==0
    for k in range(1,10):
        j=r*k
        hj=c*z**(-k)
        assert s.simplify(beta**j*hj.subs(z,beta**r*z)-hj)==0
        # This is precisely the new coefficient at w^(j+r).
        derivative=beta**j*s.diff(hj,z).subs(z,beta**r*z)
        rhs=-derivative
        assert s.simplify(rhs-k*c*beta**(-r)*z**(-k-1))==0
        laurent_exponent=-k-1
        linear_eigenvalue=beta**(j+r+r*laurent_exponent)-1
        assert linear_eigenvalue==0
        assert rhs!=0
        count+=1
print('Invariant canonical form checked for r=1,...,8.')
print('Nonlinear resonant Laurent obstructions checked:',count)
print('For every r,k the obstructing coefficient is k*c*beta^(-r),')
print('while the coefficient of h_(r(k+1)) at z^(-k-1) is annihilated.')
print('The ordinary normal line has exact order r: beta^n=(beta^r)^j')
print('forces n=r*j by absolute values.  The neighborhood obstruction')
print('therefore uses strictly more than the torsion normal calculation.')
print('PASS: all exact canonical and resonant-jet identities')
