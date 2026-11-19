#!/usr/bin/env python3
"""Fresh whole-domain local certificates supplementing fresh_frobenius.py."""
import json, math, time
from fractions import Fraction
from pathlib import Path
import fresh_frobenius as F
from flint import arb, acb, acb_mat, arb_mat, acb_poly
import sympy as sp

started=time.monotonic();OUT=F.OUT
I=F.ident;Z=F.zero;rb=F.rb;norm=F.norm
aA=rb(Fraction(256,3125))
alphaI=(1/aA).root(5);alpha0=aA.root(4)

def absmat(M):return arb_mat([[M[i,j].abs_upper()for j in range(M.ncols())]for i in range(M.nrows())])
def inflate(M,E):return acb_mat([[M[i,j]+acb(arb(0,E[i,j].upper()),arb(0,E[i,j].upper()))for j in range(M.ncols())]for i in range(M.nrows())])
def precondition(C):
    B=arb_mat([[C[i,1].imag,C[i,1].real,C[i,2].imag,C[i,2].real,C[i,3].imag]for i in range(1,6)])
    Binv=B.inv()
    row=arb_mat([[C[0,1].imag,C[0,1].real,C[0,2].imag,C[0,2].real,0]])*Binv
    T=acb_mat([[1]+[-row[0,j]for j in range(5)]]+[[0]+[Binv[i,j]for j in range(5)]for i in range(5)])
    return T

class Root:
    def __init__(self,P,scale,q0,m,C,N=3000):
        self.P=[p*(scale**(j+1)/q0)for j,p in enumerate(P)]
        self.Q=[acb(1)]+[acb(0)]*(m-1)+[acb(1)]
        self.m=m;self.N=N;self.raw_goal=85;self.C=C;self.T=precondition(C);self.Cp=self.T*C
        self.b=F.exact_upper_max([sum((self.P[k][i,j].abs_upper()*F.WEIGHTS[j]/F.WEIGHTS[i]for k in range(len(self.P))for j in range(6)),arb(0))for i in range(6)])
        self.R=rb(Fraction(999,1000))
        self.K=(self.b*(-(1-self.R).log()/m+rb(Fraction(m-1,m))*self.R)).exp()
        coeff=[I()]
        for n in range(N):
            rhs=sum((coeff[n-j]*self.P[j]for j in range(min(m-1,n)+1)),Z())
            if n>=m:rhs-=coeff[n-m+1]*(n-m+1)
            coeff.append(rhs/(n+1))
        self.coeff=coeff
        self.block_size=32
        self.polys=[[[acb_poly([c[i,j]for c in coeff[k:k+self.block_size]])for k in range(0,N+1,self.block_size)]for j in range(6)]for i in range(6)]
    def tail(self,r):
        assert r<self.R,str(r)
        return self.K*(r/self.R)**(self.N+1)/(1-r/self.R)
    def raw(self,z,r=None):
        if r is None:r=z.abs_upper()
        ratio=r/self.R
        rr_float=float(ratio.upper())
        if rr_float<=0:blocks_used=1
        else:
            estimate=math.ceil((-self.raw_goal*math.log(10)+math.log(1-rr_float)-float(self.K.log().upper()))/math.log(rr_float)/self.block_size)
            blocks_used=max(1,min(len(self.polys[0][0]),estimate))
        used_degree=min(self.N,blocks_used*self.block_size-1)
        actual_tail=self.K*ratio**(used_degree+1)/(1-ratio)
        zk=z**self.block_size
        def ev(blocks):
            v=acb(0)
            for poly in reversed(blocks[:blocks_used]):v=v*zk+poly(z)
            return v
        U=acb_mat([[ev(self.polys[i][j])for j in range(6)]for i in range(6)])
        return F.add_tail(U,actual_tail)
    def eval(self,z,conditioned=True,r=None):return (self.Cp if conditioned else self.C)*self.raw(z,r)
    def conn(self,z):
        num=sum((self.P[j]*z**j for j in range(self.m)),Z())
        den=1+z**self.m
        G=num/den
        dnum=sum((self.P[j]*(j*z**(j-1))for j in range(1,self.m)),Z())
        Gp=(dnum*den-num*(self.m*z**(self.m-1)))/(den**2)
        return G,Gp
    def envelope(self,x0,x1,y0,y1):
        xc=(x0+x1)/2;yc=(y0+y1)/2
        zc=acb(rb(xc),rb(yc))
        box=acb(arb(rb(xc),rb((x1-x0)/2)),arb(rb(yc),rb((y1-y0)/2)))
        r=(max(abs(rb(x0)),abs(rb(x1)))**2+max(abs(rb(y0)),abs(rb(y1)))**2).sqrt().upper()
        rho=(rb((x1-x0)/2)**2+rb((y1-y0)/2)**2).sqrt().upper()
        Y=self.eval(zc,r=r)
        G,_=self.conn(box)
        E=absmat(Y)*((absmat(G)*rho).exp()-arb_mat([[int(i==j)for j in range(6)]for i in range(6)]))
        return inflate(Y,E),box

print('Building new regular-root series',flush=True)
RI=Root(F.PI,alphaI,3125,5,F.FI)
R0=Root(F.P0,alpha0,256,4,F.F0)
print('Root weighted majorants',RI.b,R0.b,flush=True)

def components(Y):
    M=arb_mat([[Y[i,j].imag if k%2==0 else Y[i,j].real for k,j in enumerate([1,1,2,2])]for i in range(1,5)])
    b=arb_mat([[Y[i,3].real]for i in range(1,5)])
    c=arb_mat([[Y[0,1].imag,Y[0,1].real,Y[0,2].imag,Y[0,2].real]])
    d=Y[0,3].real
    return M,b,c,d

def hessian(Y,G,Gp):
    Yx=Y*G;Yy=Yx*acb(0,1)
    Yxx=Y*(G*G+Gp);Yxy=Yxx*acb(0,1);Yyy=-Yxx
    M,b,c,d=components(Y);inv=M.inv();v=inv*b
    der=[]
    for YY in [Yx,Yy]:
        Ma,ba,ca,da=components(YY);va=inv*(ba-Ma*v)
        der.append((Ma,ba,ca,da,va))
    values=[]
    for ai,bi,YY in [(0,0,Yxx),(0,1,Yxy),(1,1,Yyy)]:
        Mab,bab,cab,dab=components(YY)
        Ma,ba,ca,da,va=der[ai];Mb,bb,cb,db,vb=der[bi]
        vab=inv*(bab-Mab*v-Ma*vb-Mb*va)
        values.append(F.c0*((cab*v+ca*vb+cb*va+c*vab)[0,0]-dab))
    return values,M.det()

local=[]
def certify_square(x0,x1,y0,y1,depth=0):
    xc=(x0+x1)/2;yc=(y0+y1)/2
    z=acb(arb(rb(xc),rb((x1-x0)/2)),arb(rb(yc),rb((y1-y0)/2)))
    Y=RI.eval(z);G,Gp=RI.conn(z)
    try:
        (xx,xy,yy),det=hessian(Y,G,Gp)
        lower=min(xx.lower(),yy.lower())-xy.abs_upper()
        good=lower>rb(Fraction(1,4))
    except (ZeroDivisionError,ValueError):good=False
    if good:
        local.append({'box':[str(t)for t in (x0,x1,y0,y1)],'hxx':xx.str(80,more=True),'hxy':xy.str(80,more=True),'hyy':yy.str(80,more=True),'hessian_lower':str(lower),'system_determinant':str(det)})
    else:
        assert depth<10,('central subdivision limit',str(z))
        xm=(x0+x1)/2;ym=(y0+y1)/2
        for box in [(x0,xm,y0,ym),(xm,x1,y0,ym),(x0,xm,ym,y1),(xm,x1,ym,y1)]:certify_square(*box,depth+1)

certify_square(Fraction(-1,10),Fraction(1,10),Fraction(-1,10),Fraction(1,10))
print('Central Hessian certified on',len(local),'closed squares',flush=True)

# New cusp holomorphic-series computation, derived symbolically from Gamma6.
q=sp.symbols('q');ls=-sp.Rational(256,3125)
dl=sp.diag(1,F.lam**2,F.lam,1,F.lam**-1,F.lam**-2)
gc=(dl.inv()*F.G*dl+dl.inv()*dl.diff(F.lam)).applyfunc(sp.cancel)
gq=(ls*gc.subs(F.lam,ls*(1+q))).applyfunc(sp.cancel)
R=gq.applyfunc(lambda z:sp.limit(q*z,q,0))
A0=((gq-R/q)*(1+q)).applyfunc(sp.cancel)
assert all(not z.has(q)for z in A0)
assert R*R==sp.zeros(6)
Rc=F.toball(R);Ac=F.toball(A0)
def ad(M):return M*Rc-Rc*M
pc=[I()]
for n in range(1,601):
    rhs=ad(pc[n-1])+pc[n-1]*Ac-pc[n-1]*(n-1)
    pc.append((rhs+ad(rhs)/n+ad(ad(rhs))/(n*n))/n)
cuspweights=[rb(100)]+[rb(1)]*5
def cusp_norm(M):return F.exact_upper_max([sum((M[i,j].abs_upper()*cuspweights[j]/cuspweights[i]for j in range(6)),arb(0))for i in range(6)])
rr=cusp_norm(Rc);aa=cusp_norm(Ac);gamma=(1+2*rr+4*rr*rr)*aa
cpolys=[[acb_poly([c[i,j]for c in pc])for j in range(6)]for i in range(6)]
def cusp_P(z,r=None):
    if r is None:r=z.abs_upper()
    s=rb(Fraction(2,5));tail=(1-s)**(-gamma)*(r/s)**601/(1-r/s)
    val=acb_mat([[cpolys[i][j](z)for j in range(6)]for i in range(6)])
    err=arb_mat([[tail*cuspweights[i]/cuspweights[j]for j in range(6)]for i in range(6)])
    return inflate(val,err)

qa=rb(Fraction(1,4));la=ls*sp.Rational(5,4)
wa=acb((rb(Fraction(4,5))).root(5))*((acb(0,1)*arb.pi()/5).exp())
ua=wa*alphaI
Dinf=acb_mat([[ua**[0,-8,-4,0,4,8][i]if i==j else 0 for j in range(6)]for i in range(6)])
Dla=acb_mat([[F.ball(la)**[0,2,1,0,-1,-2][i]if i==j else 0 for j in range(6)]for i in range(6)])
Ya=RI.eval(wa,conditioned=False)*Dinf.inv()*Dla
Hc=Ya*cusp_P(acb(qa)).inv()*(I()-Rc*qa.log())
print('Cusp debug norms',rr,aa,gamma,'Ya determinant',Ya.det(),'P determinant',cusp_P(acb(qa)).det(),'Hc radius',F.maxrad(Hc),'Hc determinant',Hc.det(),flush=True)
Nb=Hc*Rc*Hc.inv()*(acb(0,2)*arb.pi())
Ni=sp.Matrix([[round(float(Nb[i,j].real.mid()))for j in range(6)]for i in range(6)])
assert all(Nb[i,j].contains(int(Ni[i,j]))and Nb[i,j].complex_rad().abs_upper()<rb(Fraction(1,100))for i in range(6)for j in range(6))
assert Ni*Ni==sp.zeros(6)
import itertools
J=None
for inds in itertools.combinations(range(6),3):
    bs=sp.eye(6)[:,list(inds)];candidate=(Ni*bs).row_join(bs)
    if abs(candidate.det())==1:J=candidate;break
assert J is not None
Jb=F.toball(J);Ji=Jb.inv()
assert J.inv()*Ni*J==sp.zeros(3).row_join(sp.eye(3)).col_join(sp.zeros(3,6))
eJ=Ji*acb_mat([[1],[0],[0],[0],[0],[0]])
Aint=sp.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
Bint=sp.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
Nold=Aint.inv()*Bint.inv()-sp.eye(6)
Jold=sp.Matrix([[-1,0,0,0,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],[0,1,0,1,0,0],[0,0,1,0,0,0],[0,-1,1,0,0,0]])
assert Ni==Bint.inv()*Aint.inv()-sp.eye(6)
assert Ni==Aint*Nold*Aint.inv() and Aint[:,0]==sp.eye(6)[:,0]
Smark=J.inv()*Aint*Jold
assert Smark[:3,:3]==Smark[3:,3:] and Smark[3:,:3]==sp.zeros(3)
assert abs(Smark.det())==1


def inner_graph(radius):
    # A disk is enclosed entrywise from actual coefficient absolute sums;
    # there is no independent-box approximation to q^n in this enclosure.
    r=rb(radius);s=rb(Fraction(2,5))
    tail=(1-s)**(-gamma)*(r/s)**601/(1-r/s)
    E=arb_mat([[sum((pc[n][i,j].abs_upper()*r**n for n in range(1,601)),arb(0))+tail*cuspweights[i]/cuspweights[j]for j in range(6)]for i in range(6)])
    Pdisc=inflate(I(),E)
    V=Ji*Hc*Pdisc
    cols=acb_mat([[V[i,1],V[i,2],V[i,3]-F.c0**(-1)*(-F.hinf)*eJ[i,0]]for i in range(6)])
    upper=acb_mat([[cols[i,j]for j in range(3)]for i in range(3)])
    lower=acb_mat([[cols[i+3,j]for j in range(3)]for i in range(3)])
    C=upper*lower.inv();B=arb_mat([[C[i,j].imag for j in range(3)]for i in range(3)])
    y0=-r.log()/(2*arb.pi());BB=B+arb_mat([[y0 if i==j else 0 for j in range(3)]for i in range(3)])
    trace=sum((BB[i,i]for i in range(3)),arb(0))
    middle=sum((BB[i,i]*BB[j,j]-BB[i,j]*BB[j,i]for i in range(3)for j in range(i+1,3)),arb(0))
    coeff=[BB.det(),middle,trace,arb(1)]
    return coeff,lower.det()

inner,lowerdet=inner_graph(Fraction(1,100))
assert all(v>0 for v in inner),[str(v)for v in inner]
print('Inner cusp determinant lower bounds:',*[str(x.lower())for x in inner],flush=True)
qsign=rb(Fraction(1,100))
Ysign=Hc*(I()+Rc*qsign.log())*cusp_P(acb(qsign))
hsign,signrows=F.height(Ysign)
assert hsign>F.hinf
vs=(rb(Fraction(1,2))).root(4)*(acb(0,1)*arb.pi()/4).exp()
asplit=R0.eval(vs,conditioned=False)[0,3]*acb(0,-1)*F.c0
print('Fresh split constant',asplit,flush=True)
print('Cusp anchor height',hsign,flush=True)
result={'checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family',
 'method':'new root recurrences, interval implicit Hessian, exact cusp gauge and coefficient absolute sums',
 'central_square':['-1/10','1/10','-1/10','1/10'],'central_hessian_lower':'1/4','central_closed_leaves':local,
 'central_consequence':'deck invariance gives gradient zero; integration gives h(w)-h(0)>=|w|^2/8 on the entire square',
 'cusp_radius':'1/100','cusp_monodromy':[[int(Ni[i,j])for j in range(6)]for i in range(6)],
 'cusp_marking':[[int(J[i,j])for j in range(6)]for i in range(6)],'cusp_marking_det':int(J.det()),
 'exact_prior_marking_transport':{'N_old':[[int(Nold[i,j])for j in range(6)]for i in range(6)],'left_transport':'A','N_new_equals_A_N_old_A_inverse':True,'J_new_inverse_A_J_old':[[int(Smark[i,j])for j in range(6)]for i in range(6)],'height_transport':'A fixes e0 and its top entry adds z3-z4+z5, real on the normalized intersection vector'},
 'cusp_lower_block_det':str(lowerdet),'cusp_shifted_det_coefficients':[{'ball':str(x),'lower':str(x.lower()),'upper':str(x.upper())}for x in inner],
 'cusp_anchor':{'q':'1/100','height':str(hsign),'above_infinity':True,'selected_rows':signrows},
 'splitting_constant':{'real':str(asplit.real),'imag':str(asplit.imag),'path_comparison':'zero root v=2^(-1/4) exp(pi i/4), upper-half-plane continuation from lambda=1 to lambda_star/2','h_original_min_candidate':str(F.hinf-asplit.imag)},
 'cusp_coefficients_exact':{'R':[[str(R[i,j])for j in range(6)]for i in range(6)],'A0':[[str(A0[i,j])for j in range(6)]for i in range(6)]},
 'cusp_constant_frame':F.matjson(Hc),'cusp_majorant':str(gamma),
 'scope':'local whole-domain certificates; fresh_global_cover.py separately certifies the complementary root sectors, cusp annulus and collar',
 'elapsed_seconds':time.monotonic()-started}
(OUT/'fresh_local_domains.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS local whole-domain certificates',flush=True)
