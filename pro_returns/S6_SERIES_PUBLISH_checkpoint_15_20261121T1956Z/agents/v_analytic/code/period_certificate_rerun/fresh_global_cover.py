#!/usr/bin/env python3
"""Independent closed-box cover for Paper V P1.18; no inherited leaves read.
Each output JSONL is a complete dyadic quadtree, including geometric leaves.
A leaf asserts the height inequality on its entire closed rectangle; domains
are covered by the rectangles, with their overlaps retained.
"""
import os,sys,json,math,time,itertools
from fractions import Fraction as Q
from pathlib import Path
import fresh_local_domains as L
F=L.F
from flint import arb,acb,arb_mat,acb_mat,ctx
import sympy as sp
ctx.dps=80
L.RI.raw_goal=40
L.R0.raw_goal=40
rb=F.rb;I=F.ident;Z=F.zero
OUT=F.OUT;START=time.monotonic()
U=arb('-1.0945402503114027801162682630549457037')
assert U>F.hinf
# Exact conjugation matrix, and the exact deck reductions used for coverage.
K=sp.Matrix([[1,2,-1,-1,2,-1],[0,0,0,0,-1,1],[0,0,-1,0,0,1],[0,0,0,-1,0,1],[0,-1,0,0,0,1],[0,0,0,0,0,1]])
A=sp.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=sp.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
assert K*A==A.inv()*K and K*B==B.inv()*K and K*K==sp.eye(6) and K[:,0]==sp.eye(6)[:,0]
assert Q(49,50)**4>=Q(100,103)**5

class Refine(Exception):pass

def boxdata(box):
    x0,x1,y0,y1=box;xc=(x0+x1)/2;yc=(y0+y1)/2
    zc=acb(rb(xc),rb(yc))
    zb=acb(arb(rb(xc),rb((x1-x0)/2)),arb(rb(yc),rb((y1-y0)/2)))
    rho=(rb((x1-x0)/2)**2+rb((y1-y0)/2)**2).sqrt().upper()
    return zc,zb,rho

def r2range(box):
    x0,x1,y0,y1=box
    def near(lo,hi):return 0 if lo<=0<=hi else min(abs(lo),abs(hi))
    return near(x0,x1)**2+near(y0,y1)**2,max(x0*x0,x1*x1)+max(y0*y0,y1*y1)

def allfinite(M):return all(M[i,j].is_finite()for i in range(M.nrows())for j in range(M.ncols()))

def height_bound(Y):
    # Four row equations determine the actual normalized real intersection.
    # Geometric existence is P1.8; this computes the same unique intersection.
    rows=[[Y[i,1].imag,Y[i,1].real,Y[i,2].imag,Y[i,2].real]for i in range(1,6)]
    approx=F.np.array([[float(z.mid())for z in row]for row in rows])
    _,_,piv=F.qr(approx.T,pivoting=True,mode='economic')
    sel=[int(i)for i in piv[:4]]
    M=arb_mat([rows[i]for i in sel]);b=arb_mat([[Y[i+1,3].real]for i in sel])
    v=M.solve(b)
    c=[Y[0,1].imag,Y[0,1].real,Y[0,2].imag,Y[0,2].real]
    h=F.c0*(sum((c[j]*v[j,0]for j in range(4)),arb(0))-Y[0,3].real)
    return h,sel

def enclosure(Yc,Gbox,rho):
    if not allfinite(Gbox):raise Refine('connection pole in box')
    # A new real constant left map at each centre. Its exact formula fixes e0
    # and the height as explained in P1.18 step1; no arbitrary gauge shift.
    Y=L.precondition(Yc)*Yc
    AA=L.absmat(Gbox)
    if not F.norm(Gbox)*rho<50:raise Refine('wide ODE box')
    E=L.absmat(Y)*((AA*rho).exp()-arb_mat([[int(i==j)for j in range(6)]for i in range(6)]))
    return L.inflate(Y,E)

TRANSITIONS=0

def transition(c,h):
    global TRANSITIONS
    pp=[sum((L.RI.P[k]*(math.comb(k,j)*c**(k-j))for k in range(j,len(L.RI.P))),Z())for j in range(len(L.RI.P))]
    qq=[sum((L.RI.Q[k]*(math.comb(k,j)*c**(k-j))for k in range(j,len(L.RI.Q))),acb(0))for j in range(len(L.RI.Q))]
    RA=arb('0.125')
    while True:
        dl=qq[0].abs_lower()-sum((qq[j].abs_upper()*RA**j for j in range(1,len(qq))),arb(0))
        if dl>0:break
        RA/=2
        if RA<arb('1e-6'):raise Refine('continuation close to pole')
    remaining=h.abs_upper()
    fac=arb(1) if remaining<RA/2 else (RA/(2*remaining)).lower()
    delta=h*fac;r=delta.abs_upper();ratio=r/RA
    upper=sum((F.norm(pp[j])*RA**j for j in range(len(pp))),arb(0))/dl
    kk=(upper*RA).exp();nmax=32
    while not kk*ratio**(nmax+1)/(1-ratio)<arb('1e-45'):nmax+=16
    if nmax>1000:raise Refine('long Taylor transition')
    coeff=[I()]
    for n in range(nmax):
        rhs=sum((coeff[n-j]*pp[j]for j in range(min(len(pp)-1,n)+1)),Z())
        rhs-=sum((coeff[n-j+1]*(qq[j]*(n-j+1))for j in range(1,min(len(qq)-1,n)+1)),Z())
        coeff.append(rhs/(qq[0]*(n+1)))
    val=coeff[-1]
    for v in reversed(coeff[:-1]):val=val*delta+v
    val=F.add_tail(val,kk*ratio**(nmax+1)/(1-ratio))
    TRANSITIONS+=1
    return delta,val,fac==1

def collar_value(z):
    r=z.abs_upper()
    if r<arb('0.99'):return L.RI.eval(z)
    c=z*(rb(Q(49,50))/r)
    Y=L.RI.eval(c)
    for _ in range(60):
        delta,T,done=transition(c,z-c);Y=Y*T;c+=delta
        if done:return Y
    raise Refine('continuation step limit')

def evaluate(kind,box):
    zc,zb,rho=boxdata(box)
    if kind=='infinity' or kind=='zero':
        root=L.RI if kind=='infinity' else L.R0
        if not zc.abs_upper()<arb('0.99'):raise Refine('root centre beyond series radius')
        Yc=root.eval(zc);Gbox,_=root.conn(zb)
    elif kind=='collar':
        if not (box[1]-box[0]<=Q(1,32) and box[3]-box[2]<=Q(1,32)):raise Refine('initial collar subdivision')
        qb=-zb**(-5)-1
        if not qb.is_finite()or not qb.abs_lower()>arb('0.1'):raise Refine('collar box too close to cusp')
        Yc=collar_value(zc);Gbox,_=L.RI.conn(zb)
    else:
        if not zc.abs_upper()<arb('0.4'):raise Refine('cusp series centre beyond radius')
        Yc=L.Hc*(I()+L.Rc*zc.log())*L.cusp_P(zc)
        Gbox=L.Rc/zb+L.Ac/(1+zb)
    Y=enclosure(Yc,Gbox,rho)
    return height_bound(Y)

def geom(kind,box):
    low,high=r2range(box)
    if kind in ('infinity','zero'):
        if low>Q(49,50)**2:return 'outside_root_disc'
        if kind=='infinity' and max(abs(box[0]),abs(box[1]),abs(box[2]),abs(box[3]))<=Q(1,10):return 'central_hessian_square'
    elif kind=='collar':
        if low>Q(103,100)**2:return 'outside_collar_outer_disc'
        if high<Q(49,50)**2:return 'inside_collar_inner_disc'
        _,zb,_=boxdata(box)
        qb=-zb**(-5)-1
        if qb.is_finite()and qb.abs_upper()<=rb(Q(1,4)):return 'covered_by_cusp_disc'
    else:
        if low>Q(1,4)**2:return 'outside_cusp_disc'
        if high<=Q(1,100)**2:return 'inner_cusp_certificate'
    return None

def subdivide(box):
    x0,x1,y0,y1=box;xm=(x0+x1)/2;ym=(y0+y1)/2
    return [(x0,xm,y0,ym),(xm,x1,y0,ym),(x0,xm,ym,y1),(xm,x1,ym,y1)]

def run(kind):
    init=(Q(-1,4),Q(1,4),Q(0),Q(1,4)) if kind=='cusp' else (Q(0),Q(103,100) if kind=='collar' else Q(49,50),Q(0),Q(103,100) if kind=='collar' else Q(49,50))
    stack=[('',init)];counts={'positive':0,'geometric':0,'split':0};worst=None;maxdepth=0;processed=0;start=time.monotonic()
    path=OUT/f'fresh_cover_{kind}.jsonl'
    with path.open('w')as f:
        while stack:
            key,box=stack.pop();processed+=1;maxdepth=max(maxdepth,len(key))
            reason=geom(kind,box);h=None
            if reason:counts['geometric']+=1
            else:
                try:
                    h,sel=evaluate(kind,box)
                    if h>U:reason='strict_height_bound';counts['positive']+=1
                except (Refine,ZeroDivisionError,ValueError,OverflowError):pass
            if reason:
                rec={'path':key,'box':[str(x)for x in box],'reason':reason}
                if h is not None:
                    rec['height_lower']=str(h.lower());rec['height_upper']=str(h.upper());rec['selected_rows']=sel
                    if worst is None or h.lower()<worst:worst=h.lower()
                f.write(json.dumps(rec,separators=(',',':'))+'\n')
            else:
                if len(key)>=22:
                    report={'domain':kind,'failed_box':[str(x)for x in box],'path':key,'height':str(h),'pending':len(stack),'counts':counts}
                    (OUT/f'fresh_cover_{kind}_failure.json').write_text(json.dumps(report,indent=2)+'\n')
                    raise RuntimeError(report)
                counts['split']+=1
                children=subdivide(box)
                stack.extend((key+str(i),children[i])for i in range(4))
            if processed%500==0:
                f.flush();print(kind,'processed',processed,'counts',counts,'pending',len(stack),'depth',maxdepth,'elapsed',round(time.monotonic()-start,1),flush=True)
    # Independently close the quadtree using only the written path strings.
    keys={json.loads(line)['path']for line in path.read_text().splitlines()}
    for depth in range(maxdepth,0,-1):
        for parent in {s[:-1]for s in keys if len(s)==depth}:
            children={parent+str(i)for i in range(4)}
            if children<=keys:keys.difference_update(children);keys.add(parent)
    assert keys=={''},('partition does not close',keys)
    result={'domain':kind,'initial_closed_rectangle':[str(x)for x in init],'counts':counts,'processed':processed,'maximum_depth':maxdepth,'strict_threshold':str(U),'lowest_accepted_height_lower':str(worst),'partition_closes':True,'leaf_file':path.name,'fresh_complex_taylor_transitions':TRANSITIONS,'elapsed_seconds':time.monotonic()-start}
    (OUT/f'fresh_cover_{kind}.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS DOMAIN',json.dumps(result),flush=True)
    return result

selected=os.environ.get('CERT_DOMAINS','infinity,zero,cusp,collar').split(',')
results=[run(kind)for kind in selected]
(OUT/'fresh_cover_run.json').write_text(json.dumps({'checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family','method':'new adaptive exact-rational closed-box partitions with fresh Arb period enclosures','domains':results,'elapsed_seconds':time.monotonic()-START},indent=2)+'\n')
