"""Exact nine-direction spanning-tube algebra, written before target proof."""
from pathlib import Path
import json
import sympy as s
I=s.eye(3)
def E(i,j):
    v=s.zeros(3);v[i,j]=1;return v
directions=[];checks=[]
for i,j in [(0,1),(0,2),(1,2)]:
    N=E(i,j)-E(j,i)
    for kind,A in [('skew',I),('scaled',s.diag(*[2 if k==i else 1 for k in range(3)])),('complex_shear',I+s.I*E(i,j))]:
        M=s.simplify(s.conjugate(A)*N*A.inv())
        assert M.rank()==2
        assert s.simplify(s.conjugate(M)*M-A*(N*N)*A.inv())==s.zeros(3)
        if kind=='complex_shear':assert M==2*E(i,j)-E(j,i)+s.I*(E(i,i)+E(j,j))
        directions.append(M)
        # Infinite graph plane is (ker M in E) plus (im M in conjugate E).
        ker=M.nullspace()[0];im=M.columnspace()
        F=s.Matrix.hstack(ker.col_join(s.zeros(3,1)),s.zeros(3,1).col_join(im[0]),s.zeros(3,1).col_join(im[1]))
        swap=s.BlockMatrix([[s.zeros(3),I],[I,s.zeros(3)]]).as_explicit()
        full=F.row_join(swap*s.conjugate(F))
        assert full.det()!=0
        checks.append({'pair':[i+1,j+1],'kind':kind,'rank':2,'infinite_complement_determinant':str(full.det())})
B=s.Matrix.hstack(*(M.reshape(9,1) for M in directions))
assert B.det()!=0
# After the independent derivation was frozen, compare all exact numbers in
# the printed construction, without opening its producing program.
t=s.symbols('t',real=True)
vectors=[s.Matrix(v) for v in [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)]]
def cross(w):
    x,y,z=w;return s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
printed=[];bounds=[]
for w in vectors:
    q=(w.T*w)[0];K=cross(w);Proj=q*I-w*w.T;M=Proj+K
    assert s.expand((I+t*M).T*(I+t*M)-(I+(2*t+(q+1)*t*t)*Proj))==s.zeros(3)
    quadratic=(1+q*t)**2+q*t*t
    completed=q*(q+1)*(t+1/(q+1))**2+1/(q+1)
    assert s.expand(quadratic-completed)==0
    printed.append(M);bounds.append(str(1/(q+1)))
printed.extend(cross(w) for w in vectors[:3])
printed_det=s.Matrix.hstack(*(M.reshape(9,1) for M in printed)).det()
assert printed_det==-16
out={'nine_direction_determinant':str(B.det()),'rank':B.rank(),'individual_directions':checks,
 'printed_construction_determinant':str(printed_det),'printed_transverse_squared_singular_value_bounds':bounds,
 'scope':'Independent compact-projective-line construction plus subsequent exact comparison of every matrix and uniform bound in the printed construction. No producing code read or used.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
