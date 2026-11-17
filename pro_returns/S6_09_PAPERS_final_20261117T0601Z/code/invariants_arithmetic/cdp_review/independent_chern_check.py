"""Independent symbolic intersection calculation for CDP A.5.10.

All analytic inputs are proved in the audit; this checks the two polynomial
identities, without using the printed answers as an implementation template.
"""
import json
import sympy as s

k,v,r,w2,wb,b2=s.symbols('k v r W2 WB B2')
matrix=s.Matrix([[-k-v,v,r,1],[v,w2,wb,0],[r,wb,b2,0],[1,0,0,0]])
records=[]
for epsilon in [0,1]:
    L=s.Matrix([2+epsilon,1,0,k])
    M=s.Matrix([1-epsilon,0,1,-k])
    expression=s.expand((L.T*matrix*L+L.T*matrix*M+M.T*matrix*M)[0])
    expected=(-6*k-2*v+4*r if epsilon==0 else -6*k-3*v+3*r)+w2+wb+b2
    assert s.expand(expression-expected)==0
    records.append({'epsilon':epsilon,'intersection_polynomial':str(expression),'matches':True})
print(json.dumps({'basis':['C','W=V+D_p','B_v=R-D_p','F'],
                  'intersection_matrix':str(matrix),'records':records},indent=2))
