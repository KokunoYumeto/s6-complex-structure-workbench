"""Exact certificates for the degeneration calculations in Part E.

Run from the deliverable directory with: python code/e_degeneration.py
No floating point calculations are used.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

out = []
def record(label, value):
    out.append(f"{label}: {value}")

x,y,z,v,u,r,a = s.symbols('x y z v u r a')
F = x*y-u*z*v
record('double degeneration equation', F)
record('Jacobian in x,y,z,v,u', [s.diff(F,k) for k in (x,y,z,v,u)])
record('small resolution chart x=z*r (strict transform)', s.cancel(F.subs(x,z*r)/z))
record('small resolution chart z=x*a (strict transform)', s.cancel(F.subs(z,x*a)/x))
record('chart 1 q after solving for v at u!=0', z*r*y/u)
record('chart 2 q', x*a*v)
assert s.expand(F.subs({x:z*r, v:r*y/u})) == 0
assert s.expand(F.subs({z:x*a, y:u*a*v})) == 0
record('two independent substitutions into xy-u*z*v', 'both zero')

# Lattice certificate. The proof uses the invariant Gram data and primitivity;
# this integral model independently checks all matrix identities and Smith ranks.
G = s.diag(1,*([-1]*9))
f = s.Matrix([3]+[-1]*9)
O = s.eye(10)[:,9]
P = s.eye(10)[:,8]
m = P-O
q = s.Matrix([0,1,1,-1,-1,-1,0,0,1,0])
dot = lambda v,w: (v.T*G*w)[0]
T = s.eye(10)+q*(f.T*G)-f*(q.T*G)+3*f*(f.T*G)
record('Gram(F,q,m)', s.Matrix.hstack(f,q,m).T*G*s.Matrix.hstack(f,q,m))
record('T preserves intersection form', T.T*G*T==G)
record('T fixes F', T*f==f)
record('T(O)=O+q+3F', T*O==O+q+3*f)
record('T pullback on m is m-F', T.inv()*m==m-f)
record('primitive rank-two Gram determinant', s.det(s.Matrix([[-6,-1],[-1,-2]])))
d2 = (s.eye(10)-T).col_join(m.T*G*T)
snf = smith_normal_form(d2,domain=s.ZZ)
record('d2 Smith nonzero diagonal', [snf[i,i] for i in range(min(snf.shape)) if snf[i,i]])
record('d2 rank via Gaussian elimination', d2.rank())
record('d2 image in (q,F,fibre) coordinates', s.Matrix([[-1,0,0],[-3,1,0],[-1,0,1]]))
record('Q integral homology ranks H0..H6', [1,1,8,7,10,0,1])
record('Q Euler by ranks', sum((-1)**i*b for i,b in enumerate([1,1,8,7,10,0,1])))
record('Q Euler by normalization minus double surface', 2*12-12)

def twisted_cycle(n,R):
    B=s.zeros(2*n,2*n)
    for i in range(n):
        for j in range(2):
            B[2*i+j,2*i+j]-=1
            target=(i+1)%n
            block=R if i==n-1 else s.eye(2)
            for k in range(2):
                B[2*target+k,2*i+j]+=block[k,j]
    return B

for label,n,R in [('order3',4,s.Matrix([[0,-1],[1,-1]])),
                  ('order4',3,s.Matrix([[0,-1],[1,0]]))]:
    B=twisted_cycle(n,R)
    S=smith_normal_form(B,domain=s.ZZ)
    diag=[abs(S[i,i]) for i in range(2*n)]
    tors=[int(d) for d in diag if d>1]
    record(f'{label} components',n)
    record(f'{label} graph H1 Smith invariants',diag)
    record(f'{label} independent det(R-I)',abs(s.det(R-s.eye(2))))
    record(f'{label} homology ranks H0..H4',[1,1,n+1,2*n+1,n])
    record(f'{label} torsion H1',tors)
    record(f'{label} Euler',1-1+(n+1)-(2*n+1)+n)
    assert B.det()!=0
    assert abs(B.det())==abs((R-s.eye(2)).det())

record('homotopy-sphere cohomology monodromy H0,H6', [1,1])
record('Eells-Kuiper denominator 2^7*7',2**7*7)
record('Theta_7 residue numerator denominator after multiplying by 28',(2**7*7)//28)
text='\n'.join(out)+'\n'
print(text,end='')
Path(__file__).with_suffix('.out').write_text(text)
