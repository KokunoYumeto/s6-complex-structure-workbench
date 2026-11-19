from pathlib import Path
from itertools import combinations
import importlib.util
import sympy as s
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
inds=list(combinations(range(4),2))
def wedgemat(M):return s.Matrix([[M.extract(i,j).det() for j in inds] for i in inds])
def wedgevec(a,b):return s.Matrix([a[i]*b[j]-a[j]*b[i] for i,j in inds])
C=d.Cf*d.Cg.inv();D=C-s.eye(4)
Nv=(d.B*d.A).inv()-s.eye(6);Nw=Nv[1:,1:]
assert Nw==(d.Q.inv()*wedgemat(C)*d.Q-s.eye(6))[1:,1:]
c=s.Matrix([[1,-1,1,1,-1,1]])
print('N4',D);print('Nv',Nv);print('c',c)
for i in range(4):
 a=s.eye(4)[:,i];rfull=wedgevec(a,D*a);r=(d.Q.inv()*rfull)[1:,:];k=(c*rfull)[0];gamma=(Nv[:1,1:]*r)[0]
 print('a',i,'r1',r,'k',k,'gamma',gamma,'ratio',s.cancel(gamma/k) if k else 'zero')
# Verify the proportionality for arbitrary a,b subject only to r=a wedge N b.
a=s.Matrix(s.symbols('a:4'));b=s.Matrix(s.symbols('b:4'))
rfull=wedgevec(a,D*b);r=(d.Q.inv()*rfull)[1:,:];k=(c*rfull)[0];gamma=(Nv[:1,1:]*r)[0]
print('general_difference_gamma_minus_k',s.expand(gamma-k))
print('general_difference_gamma_plus_k',s.expand(gamma+k))
print('Nw_r',s.simplify(Nw*r))
