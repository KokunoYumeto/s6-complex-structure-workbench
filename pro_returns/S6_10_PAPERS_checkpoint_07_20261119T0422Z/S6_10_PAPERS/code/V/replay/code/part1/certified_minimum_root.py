"""Certified lower bounds for h on finite root disks and at the infinity minimum.

Every ODE tail is enclosed by the explicit weighted Cauchy bound in
minimum_tools.py. No numerical grid is used as a proof. A recursive cover
certifies h>h(infinity) off a local square. On that square the Hessian is
certified positive definite; root rotation forces its gradient at zero to
vanish exactly.
"""
from minimum_tools import *
import time
Aconst=arb.pi()*625/96

def serial(V):return [[V[i,j].str(95) for j in range(V.ncols())] for i in range(V.nrows())]

def h_data(Y,Yp=None,Ypp=None):
    # Unknowns are Re(v2),Im(v2),Re(v1),Im(v1); coefficient of w0 is -i.
    rows=[[Y[r,1].imag,Y[r,1].real,Y[r,2].imag,Y[r,2].real] for r in range(1,6)]
    vals=[[Y[r,3].real] for r in range(1,6)]
    arr=np.array([[float(a.mid()) for a in row] for row in rows])
    _,_,pivot=qr(arr.T,pivoting=True,mode='economic');chosen=list(pivot[:4])
    M=arb_mat([rows[i] for i in chosen]);b=arb_mat([vals[i] for i in chosen])
    try:sol=M.solve(b)
    except (ZeroDivisionError,ValueError):return None
    t=arb_mat([[Y[0,1].imag,Y[0,1].real,Y[0,2].imag,Y[0,2].real]])
    f=(t*sol)[0,0]-Y[0,3].real
    ans={'h':f/Aconst,'minor_rows':chosen}
    if Yp is None:return ans
    def ingredients(V):
        mm=arb_mat([[V[r+1,1].imag,V[r+1,1].real,V[r+1,2].imag,V[r+1,2].real] for r in chosen])
        bb=arb_mat([[V[r+1,3].real] for r in chosen])
        tt=arb_mat([[V[0,1].imag,V[0,1].real,V[0,2].imag,V[0,2].real]])
        return mm,bb,tt,V[0,3].real
    Mx,bx,tx,cx=ingredients(Yp);My,by,ty,cy=ingredients(Yp*acb(0,1))
    sx=M.solve(bx-Mx*sol);sy=M.solve(by-My*sol)
    hx=((tx*sol+t*sx)[0,0]-cx)/Aconst
    hy=((ty*sol+t*sy)[0,0]-cy)/Aconst
    ans.update(hx=hx,hy=hy)
    if Ypp is None:return ans
    H=[]
    for tag,der,a1,a2 in [('xx',Ypp,(Mx,tx,sx),(Mx,tx,sx)),('xy',Ypp*acb(0,1),(Mx,tx,sx),(My,ty,sy)),('yy',-Ypp,(My,ty,sy),(My,ty,sy))]:
        Mab,bab,tab,cab=ingredients(der);Ma,ta,sa=a1;Mb,tb,sb=a2
        sab=M.solve(bab-Mab*sol-Ma*sb-Mb*sa)
        hab=((tab*sol+ta*sb+tb*sa+t*sab)[0,0]-cab)/Aconst
        ans[tag]=hab
    return ans

class RootEvaluator:
    def __init__(self,kind,N=4000):
        self.data=root_data(kind);self.N=N;self.ys=root_coeffs(self.data,N)
        self.H=root_frame(self.data,self.ys[:401]);self.weight=self.data['weights']
        self.original_H=acb_mat(self.H)
        # Explicit real change of flat coordinates, fixing e. It does not
        # alter h: on the real intersection line the added top row is real.
        B=arb_mat([[self.H[r,j].imag if k%2==0 else self.H[r,j].real
                    for k,j in enumerate([1,1,2,2,3])] for r in range(1,6)])
        Binv=B.inv()
        tt=arb_mat([[self.H[0,1].imag,self.H[0,1].real,self.H[0,2].imag,self.H[0,2].real,self.H[0,3].imag]])*Binv
        change=acb_mat(6,6);change[0,0]=1
        for j in range(5):change[0,j+1]=-tt[0,j]
        for i in range(5):
         for j in range(5):change[i+1,j+1]=Binv[i,j]
        self.change=change;self.H=change*self.H
        self.Cs=[self.H*Y for Y in self.ys]
        self.polys={};self.errorpolys={};self.derivbounds={}
        self.Hrow=[sum(abs(self.H[i,j])*self.weight[j] for j in range(6)) for i in range(6)]
        self.hcenter=h_data(self.H)['h']
        print(kind,'frame ready','center',self.hcenter.str(80),flush=True)
    def evaluate(self,z,derivs=False):
        r=abs(z)
        assert r<arb('.999')
        n=next((n for n in [40,80,160,320,640,1280,2560,self.N] if root_tail(self.data,n,r)<arb('1e-15')),self.N)
        if n not in self.polys:
            self.polys[n]={(i,j):acb_poly([center(self.Cs[k][i,j]) for k in range(n+1)]) for i in range(6) for j in range(6)}
            self.errorpolys[n]={(i,j):arb_poly([abs(self.Cs[k][i,j]-center(self.Cs[k][i,j])).upper() for k in range(n+1)]) for i in range(6) for j in range(6)}
            self.derivbounds[n]={(i,j):arb_poly([abs(self.Cs[k][i,j]).upper()*k for k in range(1,n+1)]) for i in range(6) for j in range(6)}
        Y=acb_mat(6,6);Y[0,0]=1
        zmid=center(z);rho=abs(z-zmid).upper();rmid=abs(zmid)
        tail=root_tail(self.data,n,r)
        # H times the entrywise weighted tail enclosure.
        for i in range(6):
         for j in range(1,4):
            eps=tail*self.Hrow[i]/self.weight[j]+self.errorpolys[n][i,j](rmid)+rho*self.derivbounds[n][i,j](r)
            oldprec=ctx.dps;ctx.dps=800
            midval=self.polys[n][i,j](zmid)
            ctx.dps=oldprec
            Y[i,j]=midval+acb(arb(0,eps),arb(0,eps))
        if not derivs:return h_data(Y)
        # The rational root connection gives exact derivatives, avoiding
        # independently truncated derivative series.
        B=Z
        for coef in self.data['Bs'][::-1]:B=B*z+coef
        D=1+z**self.data['m'];G=B/D
        Bp=Z
        for k in range(len(self.data['Bs'])-1,0,-1):Bp=Bp*z+self.data['Bs'][k]*k
        Gp=Bp/D-B*(self.data['m']*z**(self.data['m']-1))/(D*D)
        # Need all columns to form YG. Build them only for derivative queries.
        for i in range(6):
         for j in [0,4,5]:
            eps=tail*self.Hrow[i]/self.weight[j]+self.errorpolys[n][i,j](rmid)+rho*self.derivbounds[n][i,j](r)
            oldprec=ctx.dps;ctx.dps=800
            midval=self.polys[n][i,j](zmid)
            ctx.dps=oldprec
            Y[i,j]=midval+acb(arb(0,eps),arb(0,eps))
        Yp=Y*G;Ypp=Y*(G*G+Gp)
        return h_data(Y,Yp,Ypp)

if __name__=='__main__':
    out={'method':__doc__,'charts':{}}
    evs={kind:RootEvaluator(kind) for kind in ['infinity','zero']}
    ref=evs['infinity'].hcenter
    for radius in ['.3','.2','.1','.05','.025','.01','.005']:
        z=acb(arb(0,radius),arb(0,radius))
        val=evs['infinity'].evaluate(z,True)
        print('hessian square',radius,{k:v.str(20) if isinstance(v,arb) else v for k,v in val.items()} if val else None,flush=True)
        if val and val['xx']>0 and val['yy']>0 and val['xx']*val['yy']-val['xy']*val['xy']>0:
            local=arb(radius);out['local_hessian']={'radius':radius,**{k:v.str(80) for k,v in val.items() if isinstance(v,arb)}};break
    else:raise RuntimeError('no positive local Hessian certified')
    for kind,ev in evs.items():
        count=0;accepted=[];maxdepth=0;stack=[(0,1,0,1,0)]
        slope=(arb.pi()*2/5).tan() if kind=='infinity' else None
        while stack:
            x0,x1,y0,y1,depth=stack.pop();count+=1;maxdepth=max(depth,maxdepth)
            if arb(x0)**2+arb(y0)**2>arb('.98')**2:continue
            if slope is not None and arb(y0)>slope*arb(x1):continue
            if kind=='infinity' and arb(x1)<=local and arb(y1)<=local:continue
            z=acb(arb((x0+x1)/2,(x1-x0)/2),arb((y0+y1)/2,(y1-y0)/2))
            val=ev.evaluate(z) if abs(z)<arb('.99') else None
            if val and val['h']>ref:
                accepted.append([x0,x1,y0,y1,depth,val['h'].str(30)]);continue
            if depth>=18:
                raise RuntimeError(('unresolved box',kind,x0,x1,y0,y1,val))
            xm=(x0+x1)/2;ym=(y0+y1)/2
            stack.extend([(x0,xm,y0,ym,depth+1),(xm,x1,y0,ym,depth+1),(x0,xm,ym,y1,depth+1),(xm,x1,ym,y1,depth+1)])
            if count%500==0:print(kind,'processed',count,'accepted',len(accepted),'pending',len(stack),'depth',maxdepth,flush=True)
        out['charts'][kind]={'center_h':ev.hcenter.str(90),'certified_root_radius':'.98','processed_boxes':count,'maxdepth':maxdepth,'accepted_boxes':accepted,'certified_root_frame':serial(ev.H)}
        print(kind,'CERTIFIED',count,'boxes',len(accepted),'maxdepth',maxdepth,flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
