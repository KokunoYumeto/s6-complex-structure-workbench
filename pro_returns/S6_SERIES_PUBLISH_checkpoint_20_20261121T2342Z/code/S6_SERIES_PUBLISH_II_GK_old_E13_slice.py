"""E13-only verbatim block from the pinned E_checks.py; import supplied."""
import sympy as s

mu,e1,e2,bb,x,y,r=s.symbols('mu e1 e2 b x y r')
residue_matrix=s.Matrix([[1,-bb/(e1+mu)],[1,-bb/(e2+mu)]])
assert s.simplify(residue_matrix.det()-bb*(e2-e1)/((e1+mu)*(e2+mu)))==0
print('E13 exact two-node residue determinant:',s.factor(residue_matrix.det()))
# Connection coefficient times the invariant differential transforms without
# a pole under the order-four good-reduction coordinate comparison.
transformed=s.factor(((r**-3*y+bb)/(r**-2*x+mu))*r)
assert s.simplify(transformed-(y+bb*r**3)/(x+mu*r**2))==0
print('E13 order-four connection comparison:',transformed)
