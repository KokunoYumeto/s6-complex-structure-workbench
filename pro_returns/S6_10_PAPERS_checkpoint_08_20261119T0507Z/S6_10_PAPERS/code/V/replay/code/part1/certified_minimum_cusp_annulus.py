"""Finite interval cover between the certified logarithmic cusp disk and radius 1/4."""
from minimum_tools import *
from certified_minimum_root import h_data
j=json.loads(Path(__file__).with_name('certified_minimum_cusp.json').read_text())
H=acb_mat([[ballparse(v) for v in row] for row in j['regular_factor_H']])
J=s.Matrix(j['Jordan_marking']);HH=cm(J.inv())*H
R=Ra;cc=[parts[-1],parts[-2]/aa,parts[-3]/(aa*aa),parts[0]*aa,parts[1]*aa*aa]
abs0=np.array([[float(abs(R[i,k]))+sum(float(abs(V[i,k])) for V in cc) for k in range(6)] for i in range(6)])
eva,eve=np.linalg.eig(abs0+np.ones((6,6))*1e-15);v=np.abs(eve[:,np.argmax(eva.real)].real);v/=max(v)
w=[arb(2)**round(math.log2(max(float(c),2**-40))) for c in v]
growth=(arb(j['majorant_factor'])*arb(j['M'])*arb(j['majorant_radius'])).exp();bigR=arb(j['majorant_radius'])
N=512;As=[];Ps=[I]
for n in range(N):
    An=(cc[0]+cc[1]*(n+1)+cc[2]*((n+1)*(n+2)//2))*(-1)**n
    if n==0:An+=cc[3]+cc[4]
    if n==1:An+=cc[4]
    As.append(An);Q=Z
    for k in range(n+1):Q+=Ps[n-k]*As[k]
    ad=Q*R-R*Q;ad2=ad*R-R*ad
    Ps.append(Q/(n+1)+ad/(n+1)**2+ad2/(n+1)**3)
hstar=arb('-1.0945402503114027801162682630549457037255332694053308978 +/- 5e-56')
F=acb_mat(6,3);F[1,0]=1;F[2,1]=1;F[3,2]=1;F[0,2]=acb.pi()*625/96*hstar
Cs=[HH*P*F for P in Ps];polys={}
hr=[sum(abs(HH[i,k])*w[k] for k in range(6)) for i in range(6)]
fc=[sum(abs(F[k,j])/w[k] for k in range(6)) for j in range(3)]
def tail(n,r):return growth*(r/bigR)**(n+1)/(1-r/bigR)
def det_at(q):
    r=abs(q)
    if not r>0 or not r<bigR:return None
    n=next((n for n in [40,80,160,320,512] if tail(n,r)<arb('1e-18')),512)
    if n not in polys:polys[n]={(i,j):acb_poly([Cs[k][i,j] for k in range(n+1)]) for i in range(6) for j in range(3)}
    G=acb_mat(6,3);tt=tail(n,r)
    for i in range(6):
     for j in range(3):
        eps=tt*hr[i]*fc[j];G[i,j]=polys[n][i,j](q)+acb(arb(0,eps),arb(0,eps))
    T=acb_mat([[G[i,j] for j in range(3)] for i in range(3)])
    D=acb_mat([[G[i+3,j] for j in range(3)] for i in range(3)])
    try:C=T*D.inv()
    except (ZeroDivisionError,ValueError):return None
    yy=-r.log()/(2*arb.pi())
    BB=arb_mat([[C[i,j].imag+(yy if i==j else 0) for j in range(3)] for i in range(3)])
    return BB.det()

stack=[(-.25,.25,-.25,.25,0)];accepted=[];count=0;maxdepth=0
while stack:
    x0,x1,y0,y1,d=stack.pop();count+=1;maxdepth=max(d,maxdepth)
    minx=max(0,x0,-x1);miny=max(0,y0,-y1)
    if arb(minx)**2+arb(miny)**2>arb('.25')**2:continue
    q=acb(arb((x0+x1)/2,(x1-x0)/2),arb((y0+y1)/2,(y1-y0)/2))
    if abs(q)<arb(j['certified_disk_radius']):continue
    det=det_at(q)
    if det is not None and det>0:
        accepted.append([x0,x1,y0,y1,d,det.str(30)]);continue
    if d>=16:raise RuntimeError(('unresolved cusp-annulus box',x0,x1,y0,y1,det))
    xm=(x0+x1)/2;ym=(y0+y1)/2
    stack.extend([(x0,xm,y0,ym,d+1),(xm,x1,y0,ym,d+1),(x0,xm,ym,y1,d+1),(xm,x1,ym,y1,d+1)])
    if count%500==0:print('cusp-annulus',count,'accepted',len(accepted),'pending',len(stack),flush=True)
print('CERTIFIED cusp annulus',count,'accepted',len(accepted),'maxdepth',maxdepth,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'method':__doc__,'inner_radius':j['certified_disk_radius'],'outer_radius':'.25','processed_boxes':count,'maxdepth':maxdepth,'accepted_boxes':accepted},indent=2))
