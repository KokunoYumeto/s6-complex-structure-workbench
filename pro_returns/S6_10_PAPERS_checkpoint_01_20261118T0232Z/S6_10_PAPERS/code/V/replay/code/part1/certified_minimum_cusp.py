"""Uniform transversality at c=-h(infinity) on an explicitly bounded cusp disk.

The regular-singular factorization Y=H exp(log(q) R) P(q) uses R^2=0.
The analytic right factor satisfies (n-ad_R)P_n=sum P_{n-1-j}A_j.
The finite inverse 1/n+ad_R/n^2+ad_R^2/n^3 and a scalar majorant
provide a rigorous Cauchy tail. In an integral Jordan marking the period
matrix is log(q)/(2*pi*i) I+C(q). A positive-coefficient shifted cubic
certifies det(Im Z)>0 throughout the punctured disk.
"""
from minimum_tools import *
import itertools
R=Ra
assert norm(R*R)<1e-90
cc=[parts[-1],parts[-2]/aa,parts[-3]/(aa*aa),parts[0]*aa,parts[1]*aa*aa]
abs0=np.array([[float(abs(R[i,j]))+sum(float(abs(V[i,j])) for V in cc) for j in range(6)] for i in range(6)])
eval,evec=np.linalg.eig(abs0+np.ones((6,6))*1e-15)
v=np.abs(evec[:,np.argmax(eval.real)].real);v/=max(v)
w=[arb(2)**round(math.log2(max(float(c),2**-40))) for c in v]
def wnorm(V):return max(sum(abs(V[i,j])*w[j]/w[i] for j in range(6)) for i in range(6))
rnorm=wnorm(R);factor=1+2*rnorm+4*rnorm*rnorm
bigR=arb('.4')
MA=wnorm(cc[0])/(1-bigR)+wnorm(cc[1])/(1-bigR)**2+wnorm(cc[2])/(1-bigR)**3+wnorm(cc[3])+wnorm(cc[4])*(1+bigR)
growth=(factor*MA*bigR).exp()
N=max(300,math.ceil((float(factor*MA*bigR)+150)/(-math.log(.36/.4))))
print('majorant','Rnorm',rnorm,'factor',factor,'M',MA,'N',N,flush=True)
As=[];Ps=[I]
for n in range(N):
    An=(cc[0]+cc[1]*(n+1)+cc[2]*((n+1)*(n+2)/2))*(-1)**n
    if n==0:An+=cc[3]+cc[4]
    if n==1:An+=cc[4]
    As.append(An)
    Q=Z
    for j in range(n+1):Q+=Ps[n-j]*As[j]
    ad=Q*R-R*Q;ad2=ad*R-R*ad
    Ps.append(Q/(n+1)+ad/(n+1)**2+ad2/(n+1)**3)

def tail(r):return growth*(r/bigR)**(N+1)/(1-r/bigR)
def P_at(q):
    U=matrix_series(Ps,q)
    return add_tail(U,tail(abs(q)),w)

q0=acb('.01');lam0=aa*(1+q0)
tr=certified_transport([acb(1),acb(1,1),lam0+acb(0,1),lam0])
H=X*tr*P_at(q0).inv()*(I-R*q0.log())
Nc=H*R*H.inv()*acb(0,2)*acb.pi()
Ni=s.Matrix([[round(float(Nc[i,j].real.mid())) for j in range(6)] for i in range(6)])
for i in range(6):
 for j in range(6):
    assert Nc[i,j].real.contains(int(Ni[i,j])) and Nc[i,j].imag.contains(0)
    assert abs(Nc[i,j]-int(Ni[i,j]))<arb('.01')
assert Ni*Ni==s.zeros(6) and Ni.rank()==3
J=None
for indices in itertools.combinations(range(6),3):
    test=s.Matrix.hstack(*[Ni[:,j] for j in indices],*[s.eye(6)[:,j] for j in indices])
    if abs(test.det())==1:J=test;break
assert J is not None
assert Ni*J==J*s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),s.eye(3)),s.zeros(3,6))
print('integral cusp N',Ni.tolist(),'Jordan marking',J.tolist(),flush=True)
HH=cm(J.inv())*H
hstar=arb('-1.0945402503114027801162682630549457037255332694053308978 +/- 5e-56')
cstar=-hstar
F=acb_mat(6,3);F[1,0]=1;F[2,1]=1;F[3,2]=1;F[0,2]=-acb.pi()*625/96*cstar
out={'method':__doc__,'N':N,'Rnorm':rnorm.str(90),'majorant_factor':factor.str(90),'M':MA.str(90),'majorant_radius':bigR.str(),
     'nilpotent_matrix':[[int(x) for x in row] for row in Ni.tolist()],'Jordan_marking':[[int(x) for x in row] for row in J.tolist()],
     'regular_factor_H':[[H[i,j].str(95) for j in range(6)] for i in range(6)],'tests':[]}
for dd in ['.2','.1','.05','.02','.01','.001','.0001','.000001']:
    delta=arb(dd);q=acb(arb(0,delta),arb(0,delta))
    G=HH*P_at(q)*F
    T=acb_mat([[G[i,j] for j in range(3)] for i in range(3)])
    D=acb_mat([[G[i+3,j] for j in range(3)] for i in range(3)])
    try:C=T*D.inv()
    except (ZeroDivisionError,ValueError):
        print('disk',dd,'bottom block not certified invertible',flush=True);continue
    B=arb_mat([[C[i,j].imag for j in range(3)] for i in range(3)])
    c2=sum(B[i,i] for i in range(3))
    c1=sum(B[i,i]*B[j,j]-B[i,j]*B[j,i] for i in range(3) for j in range(i+1,3))
    c0=B.det();yy=-delta.log()/(2*arb.pi())
    ss=[yy*yy*yy+c2*yy*yy+c1*yy+c0,3*yy*yy+2*c2*yy+c1,3*yy+c2,arb(1)]
    good=all(v>0 for v in ss)
    print('disk',dd,'shifted determinant coefficients',[v.str(12) for v in ss],good,flush=True)
    out['tests'].append({'disk_radius':dd,'shifted_cubic_coefficients':[v.str(90) for v in ss],'certified':good})
    if good:
        out['certified_disk_radius']=dd;break
assert 'certified_disk_radius' in out
out['step_bounds']=stats
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
