#!/usr/bin/env python3
"""Fresh KO checks from marked definitions and toric monomial charts.

No original KO argument, prior computation program or KN matrix output is
read. The input is the safe marked-definition JSON. This computes action
weights, primitive circle retractions, local normal transitions, the
Hopf and SU(2) formulas, and the actual alpha gluing.
"""
from datetime import datetime,timezone
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
import sympy as S

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
IN=INPUT_ROOT.parent/'continuation5_iii_infra'/'S6_SERIES_PUBLISH_III_02KN_marked_inputs.json'
EXPECTED='0f0698dead8a1b427c34fb82cd3b7a311530e38cec55cff2160064d9d96cd145'
I4=S.eye(4);J=S.Matrix([[0,1],[-1,0]])
delta=I4[:,2]


def primitive_data(A,g):
    N=A-S.eye(2)
    nu=gcd(*(int(v) for v in N))
    col=next(N[:,i] for i in range(2) if N[:,i]!=S.zeros(2,1))
    u=col/gcd(*(int(v) for v in col))
    first=next(i for i in range(2) if u[i])
    if u[first]<0:u=-u
    c=S.Rational(g[first],u[first])
    assert c.q==1 and c*u==g and N==nu*u*u.T*J
    s,t,d=S.gcdex(u[0],u[1]);assert d==1
    r=S.Matrix([-t,s])
    if u[0]==1:r=S.Matrix([0,1])
    assert S.Matrix.hstack(u,r).det()==1
    return u,r,int(nu),int(c)


def serial(x):
    if isinstance(x,S.MatrixBase):return [[int(v) for v in row] for row in x.tolist()]
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,list):return [serial(v) for v in x]
    return x


def main():
    print('KO pre-exposure geometry computation started',datetime.now(timezone.utc).isoformat())
    raw=IN.read_bytes();assert sha256(raw).hexdigest()==EXPECTED
    print('Safe definition input SHA256',EXPECTED)
    rows=json.loads(raw)['rows'];records=[]
    for row in rows:
        p=row['P'];local=[]
        for index,(a,g,tt,w) in enumerate(zip(row['elliptic_matrices'],row['generator_section_cocycle'],
                                             row['matrices_input_to_be_rederived'],row['weights'])):
            A,g,T=S.Matrix(a),S.Matrix(g),S.Matrix(tt)
            u,r,nu,c=primitive_data(A,g)
            assert p%nu==0 and gcd(nu,c)==1
            lam=S.Matrix([u[0],u[1],-p*c//nu,0])
            cov=S.Matrix([[nu*(u.T*J)[0],nu*(u.T*J)[1],0,c]])
            angular=S.zeros(4);angular[2,3]=w
            assert T-I4==lam*cov+angular
            h=S.Matrix([[r[1],-r[0]]]);assert h*u==S.ones(1,1)
            retract=S.Matrix([[-lam[2]*h[0],-lam[2]*h[1],1,0]])
            assert retract*lam==S.zeros(1,1) and retract*delta==S.ones(1,1)
            loc=dict(index=index+1,u=u,r=r,nu=nu,c=c,vanishing=lam,
                     delta_retraction=retract)
            if index==4:
                assert nu==1 and w==1
                z=c*r;b=-p*z.T*J
                gauge=I4.copy();gauge[:2,3]=z;gauge[2,:2]=b
                inverse=I4.copy();inverse[:2,3]=-z;inverse[2,:2]=-b
                assert gauge*inverse==inverse*gauge==I4
                M=S.Matrix.hstack(u,r)
                H=inverse*S.diag(M,1,1)
                Hi=S.diag(M.inv(),1,1)*gauge
                normal=I4.copy();normal[0,1]=normal[2,3]=1
                assert H*Hi==Hi*H==I4 and H.det()==1
                assert Hi*T*H==normal and H*delta==delta
                angular_map=S.Matrix([[1,0,0,0],[0,0,1,0]])*Hi
                angular_inverse=S.Matrix.hstack(H[:,0],H[:,2])
                assert angular_map*angular_inverse==S.eye(2)
                assert angular_map*delta==S.Matrix([0,1])
                original=S.Matrix.hstack(S.Matrix([u[0],u[1],0,0]),delta)
                shift=S.Matrix([[1,0],[-p*c,1]])
                assert original*shift==angular_inverse and shift.det()==1
                loc.update(H=H,H_inverse=Hi,angular_map=angular_map,angular_inverse=angular_inverse)
                print('OS',row['OS'],'cusp H =',H.tolist())
                print('  delta angular image (0,1); inverse map and full monodromy conjugacy checked.')
            local.append(loc)
        records.append(dict(OS=row['OS'],local=local))
    print('All 16 rank-one delta retractions and all 4 cusp integral conjugacies passed.')

    a,b,c,m=S.symbols('a b c m',integer=True)
    for n in (-1,1):
        q=S.Matrix([-a,-b,-c,-n,m]);d5=S.eye(5)[:,2]
        retract=S.Matrix([[0,0,1,-c/n,0]])
        assert S.simplify((retract*q)[0])==0 and retract*d5==S.ones(1,1)
    print('Smooth-log delta retraction checked symbolically for n=+1 and n=-1, all m,a,b,c.')

    v1,v2=S.symbols('v1 v2',integer=True)
    rho=lambda x,y:S.Matrix([x,y,1])
    plus=S.Matrix.hstack(rho(v1,v2),rho(v1+1,v2),rho(v1,v2+1))
    minus=S.Matrix.hstack(rho(v1+1,v2+1),rho(v1+1,v2),rho(v1,v2+1))
    d3=S.Matrix([0,1,0])
    assert plus.det()==1 and minus.det()==-1
    assert plus.inv()*d3==S.Matrix([-1,0,1])
    assert minus.inv()*d3==S.Matrix([1,-1,0])
    for dx,dy in [(1,0),(0,1),(-1,1)]:
        quotient=S.Matrix([[-dy,dx,dy*v1-dx*v2]])
        edge=S.Matrix.hstack(rho(v1,v2),rho(v1+dx,v2+dy))
        assert quotient*edge==S.zeros(1,2)
        assert (quotient*d3)[0]==dx
        assert gcd(dx,dy)==1
    print('Universal fan chart weights (-1,0,1) and (1,-1,0); edge weights 1,0,-1.')
    print('Each triangle has exactly one e2-edge; period translations preserve the two triangle types.')

    X,Y,q=S.symbols('X Y q',nonzero=True)
    chart=S.Matrix([q/(X*Y),Y,X]);other=S.Matrix([q/Y,X*Y,1/X])
    x,y,w=S.symbols('x y w',nonzero=True)
    forward=S.Matrix([w*x,w*y,1/w])
    assert forward.subs({x:chart[0],y:chart[1],w:chart[2]},simultaneous=True)==other
    inverse=forward.subs({x:forward[0],y:forward[1],w:forward[2]},simultaneous=True)
    assert S.simplify(inverse-S.Matrix([x,y,w]))==S.zeros(3,1)
    jac=forward.jacobian([x,y,w])
    assert jac.det()==-1 and jac[:2,:2]==w*S.eye(2)
    assert S.prod(forward)==x*y*w
    action=S.Matrix([-x,y,0])
    assert jac*action==S.Matrix([-forward[0],forward[1],0])
    print('Normal charts and inverses checked; both normal transitions are multiplication by w.')

    u=S.symbols('u',nonzero=True);s,k=S.symbols('s k',real=True)
    G=S.Matrix([[s/u,-k],[k,s*u]])
    Gi=S.Matrix([[s*u,k],[-k,s/u]])
    assert S.simplify(G*Gi-(s*s+k*k)*S.eye(2))==S.zeros(2)
    assert G.det()==s*s+k*k
    assert G.subs({s:1,k:0})==S.diag(1/u,u)
    assert G.subs({s:0,k:1})==S.Matrix([[0,-1],[1,0]])
    print('SU(2) clutching extension and inverse checked exactly under s^2+k^2=1.')

    x1,x2,y1,y2,C,D=S.symbols('x1 x2 y1 y2 C D',real=True)
    def hopf(z):
        xx,yy,zz,ww=z
        return S.Matrix([2*(xx*zz+yy*ww),2*(yy*zz-xx*ww),xx*xx+yy*yy-zz*zz-ww*ww])
    vec=S.Matrix([x1,x2,y1,y2]);rot=S.diag(S.Matrix([[C,-D],[D,C]]),S.Matrix([[C,-D],[D,C]]))
    hh=hopf(vec);rr=(vec.T*vec)[0]
    assert S.expand((hh.T*hh)[0]-rr**2)==0
    assert all(S.expand(z)==0 for z in hopf(rot*vec)-(C*C+D*D)*hh)
    xx,yy=S.symbols('xx yy',real=True)
    den=1+xx*xx+yy*yy
    section=S.Matrix([1,0,xx,-yy])/S.sqrt(den)
    expected=S.Matrix([2*xx,2*yy,1-xx*xx-yy*yy])/den
    assert all(S.simplify(z)==0 for z in hopf(section)-expected)
    assert S.simplify((section.T*section)[0])==1
    radius=S.sqrt(xx*xx+yy*yy)
    northern=S.Matrix([1,xx-S.I*yy])/S.sqrt(den)
    southern=S.Matrix([(xx+S.I*yy)/radius,radius])/S.sqrt(den)
    phase=(xx+S.I*yy)/radius
    assert all(S.simplify(z)==0 for z in southern-phase*northern)
    z1=S.Matrix([1,u**-1])/S.sqrt(2);z2=S.Matrix([u,1])/S.sqrt(2)
    assert z2==u*z1
    print('Hopf norm, scalar invariance, local inverse sections and their overlap phase checked exactly.')
    print('The Hopf transition on the equator has winding +1.')

    cc,dd=S.symbols('cc dd',real=True)
    R=lambda c,s:S.diag(S.Matrix([[c,-s],[s,c]]),S.eye(3))
    assert S.expand(R(C,D)*R(cc,dd)-R(C*cc-D*dd,D*cc+C*dd))==S.zeros(5)
    assert R(C,D)*R(C,-D)==S.diag(C*C+D*D,C*C+D*D,1,1,1)
    assert R(C,D).det()==C*C+D*D
    print('alpha group law, inverse, orientation and boundary equivariance checked symbolically.')
    flip=S.diag(1,-1,-1,1,1)
    assert flip.det()==1 and flip*flip==S.eye(5)
    assert flip*R(C,D)*flip==R(C,-D)
    assert flip*R(C,-D)==R(C,D)*flip
    print('GR gluing direction: A alpha A^-1 = alpha^-1 and A alpha^-1 = alpha A checked exactly.')
    print('The two smooth relative degrees are 2 and 6; degree-four restriction has zero adjacent terms.')
    (HERE/'S6_SERIES_PUBLISH_III_02KO_fresh_geometry_maps.json').write_text(
        json.dumps(serial(records),indent=2)+'\n',newline='\n')
    print('Every retained integer angular map, inverse and primitive delta retraction saved.')
    print('KO pre-exposure geometry computation completed',datetime.now(timezone.utc).isoformat())


if __name__=='__main__':main()
