from pathlib import Path
import json
import sympy as S

v=S.symbols('v', integer=True)
q=v*v-v+1
I=S.eye(5)
A=S.zeros(5)
for j in range(5): A[(j+1)%5,j]=1
X=I[:,0].row_join(I[:,2]+v*I[:,4])
Y=S.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
N=X*Y
P=S.eye(5)
P[:,0]=S.ones(5,1)/q
Ap=P.inv()*A*P
B=A.inv()*(I-N)
Bp=P.inv()*B*P
s=v*v+v-1
r=-(v+1)*(v*v-2)/2
beta=S.Matrix([[s,s-v*r,v*v*s+v*r,r,-v*s-r]])
z=S.Matrix([-v**3+v-1,0,0,2,2*(1-v*v)])
Ah=S.diag(1,Ap)
Bh=S.zeros(6)
Bh[0,0]=1
Bh[0,1:6]=beta
Bh[1:6,1:6]=Bp
zz=S.Matrix([0]+list(z))
checks=[]
def zero(name,m):
    ok=all(S.cancel(a)==0 for a in m)
    checks.append({'name':name,'pass':ok})
    assert ok,name
zero('YX zero',Y*X)
zero('N squared zero',N*N)
zero('actual inverse of I+N',(I+N)*(I-N)-I)
zero('C inverse B',((I+N)*A)*B-I)
zero('YP exact',Y*P-S.Matrix([[-2,-q,-v*v,-1,v],[2*(1-v),1-v*q,-v*q,v*v-v,q]]))
zero('YPz zero',Y*P*z)
zero('beta z unit',beta*z-S.ones(1,1))
zero('actual hatted unit',(Ah*Bh-S.eye(6))*zz-S.eye(6)[:,0])
zero('A order five',A**5-I)
for n in range(-32,33):
    matrices=[Ap.subs(v,n),Bp.subs(v,n),Ah.subs(v,n),Bh.subs(v,n)]
    ok=all(a.is_Integer for m in matrices for a in m) and r.subs(v,n).is_Integer
    ok=bool(ok and all(abs(m.det())==1 for m in matrices))
    checks.append({'name':f'actual integer lattice at v={n}','pass':ok})
    assert ok,n
out={'status':'PASS','check_count':len(checks),'scope':'Exact hatted lattice, YPz, beta z, and six-dimensional cusp unit only','checks':checks}
dest=Path('analysis/continuation_root/F2_16_hatted_unit_fresh.output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'check_count':len(checks)}))
