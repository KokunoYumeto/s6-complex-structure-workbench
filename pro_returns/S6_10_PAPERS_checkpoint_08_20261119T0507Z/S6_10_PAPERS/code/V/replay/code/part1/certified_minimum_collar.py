"""Certified interval cover of the collar between the two finite root disks.
The remaining cusp disk is handled separately. Each collar box is reached
from radius 0.95 by rigorously bounded local Taylor continuation of the
regular infinity-root connection. All accepted boxes and bounds are saved.
"""
from minimum_tools import *
from certified_minimum_root import h_data
D=root_data('infinity');m=D['m'];Bs=D['Bs'];w=D['weights'];Nbase=1280
rr=json.loads(Path(__file__).with_name('certified_minimum_root.json').read_text())
H=acb_mat([[ballparse(v) for v in row] for row in rr['charts']['infinity']['certified_root_frame']])
hstar=arb(rr['charts']['infinity']['center_h'])
ys=root_coeffs(D,Nbase);Cs=[H*Y for Y in ys]
polys={(i,j):acb_poly([center(C[i,j]) for C in Cs]) for i in range(6) for j in range(6)}
errs={(i,j):arb_poly([abs(C[i,j]-center(C[i,j])).upper() for C in Cs]) for i in range(6) for j in range(6)}
hr=[sum(abs(H[i,k])*w[k] for k in range(6)) for i in range(6)]
roots=[(acb(0,1)*acb.pi()*(2*j+1)/m).exp() for j in range(m)]
step_log=[]

def initial(z):
    Y=acb_mat(6,6);r=abs(z);ta=root_tail(D,Nbase,r)
    for i in range(6):
     for j in range(6):
        eps=errs[i,j](r)+ta*hr[i]/w[j]
        old=ctx.dps;ctx.dps=800;v=polys[i,j](z);ctx.dps=old
        Y[i,j]=v+acb(arb(0,eps),arb(0,eps))
    return Y

def local(c,v):
    distances=[abs(c-z) for z in roots]
    dist=min(float(d.lower()) for d in distances)
    R=arb(str(.449*dist));rho=abs(v)/R
    assert rho<arb('.8'),('step too wide',rho)
    denom=arb(1)
    for d in distances:denom*=d-R
    mx=abs(c)+R
    numerator=[sum(sum(abs(Bs[k][i,j])*mx**k for k in range(len(Bs)))*w[j]/w[i] for j in range(6)) for i in range(6)]
    M=max(numerator)/denom;MR=M*R
    N=max(60,math.ceil((float(MR.upper())+55)/(-math.log(float(rho.upper())))))
    ta=MR.exp()*rho**(N+1)/(1-rho)
    while not ta<arb('1e-20'):N+=20;ta=MR.exp()*rho**(N+1)/(1-rho)
    ds=[1+c**m]+[math.comb(m,j)*c**(m-j) for j in range(1,m+1)]
    bs=[sum((Bs[k]*math.comb(k,j)*c**(k-j) for k in range(j,len(Bs))),Z) for j in range(len(Bs))]
    us=[I]
    for n in range(1,N+1):
        q=Z
        for j in range(min(len(bs),n)):q+=us[n-j-1]*bs[j]
        for j in range(1,min(m,n)+1):q-=us[n-j]*ds[j]*(n-j)
        us.append(q/(ds[0]*n))
    U=matrix_series(us,v);U=add_tail(U,ta,w)
    step_log.append({'N':N,'rho':rho.str(20),'MR':MR.str(20),'tail':ta.str(20)})
    return U

def period_box(z):
    c=center(z);delta=abs(z-c)
    dist=min(abs(c-p) for p in roots)
    if not delta<dist*arb('.18'):return None
    zb=center(c*arb('.95')/abs(c));Y=initial(zb);point=zb
    while abs(point-c)>arb('1e-95'):
        dif=c-point;dd=min(float(abs(point-p).lower()) for p in roots)
        n=max(1,math.ceil(float(abs(dif).upper())/(.18*dd)))
        h=dif/n
        Y=Y*local(point,h);point=c if n==1 else point+h
    if delta>0:Y=Y*local(c,z-c)
    return h_data(Y)

print('collar initial frame ready',flush=True)
stack=[(0,1.03125,0,1.03125,0)];accepted=[];count=0;maxdepth=0
Rmax=arb('.98')**arb('-.8');slope=(arb.pi()*2/5).tan()
while stack:
    x0,x1,y0,y1,d=stack.pop();count+=1;maxdepth=max(d,maxdepth)
    rlo=(arb(x0)*x0+arb(y0)*y0).sqrt();rhi=(arb(x1)*x1+arb(y1)*y1).sqrt()
    if rhi<arb('.98') or rlo>Rmax:continue
    if arb(y0)>slope*arb(x1):continue
    z=acb(arb((x0+x1)/2,(x1-x0)/2),arb((y0+y1)/2,(y1-y0)/2))
    if abs(z)>0 and abs(-1/z**5-1)<arb('.25'):continue
    val=period_box(z) if rlo>arb('.9') and rhi<arb('1.1') else None
    if val and val['h']>hstar:
        accepted.append([x0,x1,y0,y1,d,val['h'].str(30)]);continue
    if d>=16:raise RuntimeError(('unresolved collar box',x0,x1,y0,y1,val))
    xm=(x0+x1)/2;ym=(y0+y1)/2
    stack.extend([(x0,xm,y0,ym,d+1),(xm,x1,y0,ym,d+1),(x0,xm,ym,y1,d+1),(xm,x1,ym,y1,d+1)])
    if count%100==0:print('collar',count,'accepted',len(accepted),'pending',len(stack),'steps',len(step_log),flush=True)
print('CERTIFIED collar',count,'accepted',len(accepted),'maxdepth',maxdepth,'steps',len(step_log),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'method':__doc__,'inner_root_radius':'.98','outer_root_radius':Rmax.str(90),'cusp_disk_radius':'.25','processed_boxes':count,'maxdepth':maxdepth,'accepted_boxes':accepted,'continuation_bounds':step_log},indent=2))
