"""Exact degree-one geometric-root/bar-cell comparison for F.2.35.

The one-edge cell tau is g^{-1} x^{floor(v/m)}, not the geometric
positive root g.  Its complement column, the reconstructed geometric
root, and the cyclic degree-two power relation are checked separately.
"""
import sympy as S
from fourfolds_affine_cap_chains import AffineCap
from fourfolds_global_chains import Complement,AffineGraphBoundary
from fourfolds_total_homology import example

def check(M,v,m,Q=None,label=''):
    M=S.Matrix(M);r=M.rows;Q=S.eye(r) if Q is None else S.Matrix(Q)
    local=Q.inv()*M*Q;vv=Q.inv()*S.Matrix(v)
    cap=AffineCap(local,list(vv),m);E=Complement([M])
    B=AffineGraphBoundary(cap,E,0,Q)
    z=S.Matrix(cap.groupoid.z[1,0]);g=E.peripheral((1,))
    tau=E.mul(E.inv(g),E.translate(tuple(Q*z)))
    exact=E.from_group(E.group_term([tau]))
    assert B.complement_basis(0,())==exact
    expected={(0,()):-1}
    for j,a in enumerate(M.inv()*Q*z):
        if a:expected[-1,(j,)]=int(a)
    assert exact==expected
    geometric=E.mul(E.translate(tuple(Q*z)),E.inv(tau))
    assert geometric==g
    assert E.from_group(E.group_term([geometric]))=={(0,()):1}
    assert B.cap_basis(0,())=={(1,()):1}
    norm=sum((local**j for j in range(m)),S.zeros(r))
    power=S.Matrix(cap.groupoid.raw[m])
    relation={(1,()):m}
    for j,a in enumerate(power-norm*z):
        if a:relation[0,(j,)]=int(a)
    assert cap.d_basis(2,())==relation,(label,cap.d_basis(2,()),relation)
    print(label,'tau = -edge +',list(M.inv()*Q*z),
          '; geometric root = +edge; power relation passed',flush=True)

if __name__=='__main__':
    check([[1]],[1],2,label='positive circle')
    check([[1]],[3],2,label='integer-shifted circle')
    check([[1]],[-1],2,label='negative circle')
    check(S.diag(1,-1),[3,1],2,label='nonfixed Klein numerator')
    check(S.diag(1,-1,-1),[1,0,0],2,label='half-turn')
    M,v,n,Q=example()
    for i in range(2):check(M[i],v[i],n[i],Q[i],label='rank-six cap '+str(i+1))
    print('ALL SEVEN GEOMETRIC ROOT / CELL SIGNS AND EXACT POWER RELATIONS PASSED')
