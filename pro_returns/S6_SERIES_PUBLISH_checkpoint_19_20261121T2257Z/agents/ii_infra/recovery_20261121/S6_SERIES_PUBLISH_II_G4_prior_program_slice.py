import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
I=s.eye(4)

# Wang's matrices act on H^1, not on H_1.
WTstar=s.Matrix([[1,0,-6,-2],[0,-1,-1,1],[0,1,0,-1],[0,0,0,1]])
WT2=s.Matrix([[1,0,6,3],[0,1,2,1],[0,0,1,0],[0,0,0,1]])
WTplus=s.Matrix([[1,0,0,0],[0,2,1,0],[0,-1,0,0],[0,0,0,1]])
WTminus=s.Matrix([[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
WTs=[WTstar,WT2,WTplus,WTminus]
assert WTstar*WT2*WTplus*WTminus==I and WTstar**3==I
Winv=(WTstar-I).col_join(WT2-I).col_join(WTplus-I).col_join(WTminus-I).nullspace()
WR=s.Matrix.hstack(*[(T.inv().T-I) for T in WTs])
assert len(Winv)==1
print('Wang invariant H^1:',Winv)
print('Wang H_1 coinvariant Smith diagonal:',list(smith_normal_form(WR,domain=ZZ).diagonal()))
print('Corrected Wang count r=4-1+1=4; printed count 4-1+4=7.')

