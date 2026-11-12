"""Exploratory interval cover. Only a PASS with zero undecided boxes certifies
its stated compact region; this program never infers a bound from samples.
"""
import mpmath as mp, math,time,json,sys
mp.mp.dps=35;iv=mp.iv;iv.dps=25
PI=iv.pi;II=iv.mpc(0,1)
def C(z):return iv.mpc(str(mp.re(z)),str(mp.im(z)))
def bound(z):return max(float(abs(z).b),0)
def tail1(r,N):return r**(N+1)*((N+1)/(1-r)+r/(1-r)**2)
def tail2(r,N):return r**(N+1)*((N+1)**2/(1-r)+2*(N+1)*r/(1-r)**2+r*(1+r)/(1-r)**3)
def errorbox(e):return iv.mpc([-e,e],[-e,e])
def wp_iv(z,t,N=24):
 q=iv.exp(2*PI*II*t);p=q*iv.exp(2*PI*II*z);m=q*iv.exp(-2*PI*II*z)
 qn=q;pn=p;mn=m
 sn=iv.sin(PI*z);cs=iv.cos(PI*z)
 f=PI**2/sn**2-PI**2/3;d=-2*PI**3*cs/sn**3
 for n in range(1,N+1):
  f+=8*PI**2*n*(qn-(pn+mn)/2)/(1-qn)
  d+=8*PI**3/II*n*n*(pn-mn)/(1-qn)
  qn*=q;pn*=p;mn*=m
 r=abs(q);s=max(float(abs(p).b),float(abs(m).b));s=iv.mpf(str(s))*iv.mpf('1.000000000000001')
 if float(s.b)>=1:raise ValueError('bad strip')
 ef=8*PI**2/(1-r)*(tail1(r,N)+tail1(s,N))
 ed=16*PI**3/(1-r)*tail2(s,N)
 return f+errorbox(float(ef.b)*1.000000000000001),d+errorbox(float(ed.b)*1.000000000000001)
def wp_mp(z,t,N=35):
 q=mp.exp(2*mp.pi*1j*t);p=q*mp.exp(2*mp.pi*1j*z);m=q*mp.exp(-2*mp.pi*1j*z)
 qn=q;pn=p;mn=m
 f=mp.pi**2/mp.sin(mp.pi*z)**2-mp.pi**2/3
 d=-2*mp.pi**3*mp.cos(mp.pi*z)/mp.sin(mp.pi*z)**3
 for n in range(1,N+1):
  f+=8*mp.pi**2*n*(qn-(pn+mn)/2)/(1-qn)
  d+=8*mp.pi**3/1j*n*n*(pn-mn)/(1-qn)
  qn*=q;pn*=p;mn*=m
 return f,d
def center_root(t):
 z=mp.mpf('.5')-mp.log(5+2*mp.sqrt(6))*1j/(2*mp.pi)
 for k in range(80):
  f,d=wp_mp(z,t);step=f/d
  if abs(step)>.15:step*=mp.mpf('.15')/abs(step)
  z-=step
  if abs(step)<mp.mpf('1e-32'):break
 return z,1/wp_mp(z,t)[1]
def N2_iv(z,t):
 h=z-(1-t)/2
 qt=iv.exp(PI*II*t);qh=iv.exp(2*PI*II*h)
 th=iv.mpc(1,0)
 for n in range(1,11):th+=iv.exp(PI*II*(n*n*t+2*n*h))+iv.exp(PI*II*(n*n*t-2*n*h))
 # tail bound from |Im h| and Tmin; ratio majorant of consecutive terms.
 T=float(t.imag.a);H=max(abs(float(h.imag.a)),abs(float(h.imag.b)))
 first=mp.exp(-mp.pi*T*121+2*mp.pi*11*H)
 ratio=mp.exp(-mp.pi*T*23+2*mp.pi*H)
 err=2*first/(1-ratio)
 th+=errorbox(float(err)*1.000000000001)
 q=qt*qt;et=iv.exp(PI*II*t/12)
 qn=q
 for n in range(1,18):et*=1-qn;qn*=q
 # eta tail multiplicative error in exp(log product).
 r=abs(q);e=r**18/((1-r)*(1-r**18))
 et*=iv.exp(errorbox(float(e.b)*1.000000000001))
 return abs(th/et)**2*iv.exp(-2*PI*h.imag**2/t.imag)
def certify(box):
 x0,x1,y0,y1=box
 tmid=mp.mpc((x0+x1)/2,(y0+y1)/2)
 if abs(tmid-1j)<mp.mpf('1e-30'):return False,'center i'
 z0,A=center_root(tmid);tc=iv.mpc([x0,x1],[y0,y1]);zc=C(z0);Ac=C(A)
 f,_=wp_iv(zc,tc);off=-Ac*f
 rad=1.4*max(bound(off.real),bound(off.imag),1e-26)
 for attempt in range(4):
  Z=zc+iv.mpc([-rad,rad],[-rad,rad]);_,d=wp_iv(Z,tc)
  op=1-Ac*d;opnorm=bound(op.real)+bound(op.imag)
  K=off+op*iv.mpc([-rad,rad],[-rad,rad])
  err=max(bound(K.real),bound(K.imag))
  if err<rad and opnorm<1:
   v=N2_iv(Z,tc)
   return float(v.b)<2,('bound',float(v.b),rad,opnorm)
  rad*=1.7
 return False,('root',rad,opnorm)
if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='sample':
  for b in [(0.095,.105,.995,1.005),(.245,.255,.995,1.005),(0,.005,1.005,1.01),(0,.00001,1.00001,1.00002),(.49,.5,.866,.88)]:
   st=time.time();print(b,certify(b),'seconds',time.time()-st,flush=True)
 else:
  local=float(sys.argv[1]) if len(sys.argv)>1 else 1e-4
  queue=[(0,.5,.85,2)];done=0;undecided=[];start=time.time();worst=0
  while queue:
   b=queue.pop();x0,x1,y0,y1=b
   # Omit only boxes entirely inside the stated local square around i.
   if x1<=local and y0>=1-local and y1<=1+local:continue
   try:ok,why=certify(b)
   except Exception as e:ok=False;why=str(e)
   if ok:
    done+=1;worst=max(worst,why[1])
   elif max(x1-x0,y1-y0)<local/32:
    undecided.append((b,why))
   elif x1-x0>=y1-y0:
    xm=(x0+x1)/2;queue.extend([(x0,xm,y0,y1),(xm,x1,y0,y1)])
   else:
    ym=(y0+y1)/2;queue.extend([(x0,x1,y0,ym),(x0,x1,ym,y1)])
   if (done+len(undecided))%200==0 and done+len(undecided)>0:
    print('progress',done,len(queue),len(undecided),'seconds',time.time()-start,flush=True)
   if len(undecided)>30:break
  print(json.dumps({'local_square_radius':local,'certified_boxes':done,'pending_boxes':len(queue),'undecided':undecided,'worst_squared_norm_bound':worst,'seconds':time.time()-start},indent=2))
