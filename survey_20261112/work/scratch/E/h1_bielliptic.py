from sympy import Matrix, eye, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ
A1 = Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
MF = Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
print("A1^3", A1**3==eye(4), "A2^4", A2**4==eye(4), "A1A2MF", A1*A2*MF==eye(4))
v1 = Matrix([1,2,-4,0]); v2 = Matrix([-1,-3,3,0])
print("A1 v1 = v1", A1*v1==v1, "A2 v2 = v2", A2*v2==v2)
# H_1 of T^4/<g>, g = (A, v/m): generators e1..e4, g ; relations (A-I)e_i = 0, m g - v = 0
for A,v,m in ((A1,v1,3),(A2,v2,4)):
    R = zeros(5,5)
    R[:4,:4] = (A-eye(4))   # columns = relations (A-I)e_i
    rel = Matrix(list(-v)+[m])
    R[:,4] = rel
    print(m, smith_normal_form(R, domain=ZZ))
    print(" coinv", smith_normal_form(A-eye(4), domain=ZZ))
