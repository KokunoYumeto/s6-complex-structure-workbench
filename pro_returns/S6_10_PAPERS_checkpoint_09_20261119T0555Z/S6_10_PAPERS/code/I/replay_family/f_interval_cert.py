"""Outward interval certificate on a rational compact modular rectangle.

The certified region is [0,1/2]+i[17/20,2], except the rational square
0<=Re(tau)<=1/10000, |Im(tau)-1|<=1/10000.  The square is covered by
the separate analytic local argument in cd_local_bound.py and the paper.

All proof comparisons use interval upper endpoints, never rounded floats.
Floating-point Newton iteration chooses a centre and preconditioner only;
the interval contraction check subsequently certifies a true wp zero for
every tau in the box.  Theta is summed in its even cos form.

Run python code/f_interval_cert.py sample or python code/f_interval_cert.py
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sys
import time
import mpmath as mp

mp.mp.dps=40
iv=mp.iv
iv.dps=30
PI=iv.pi
II=iv.mpc(0,1)
ONE=iv.mpf(1)
LOCAL=F(1,10000)

def rational(q):
    q=F(q)
    return iv.mpf(q.numerator)/iv.mpf(q.denominator)

def range_iv(lo,hi):
    return iv.mpf([rational(lo).a,rational(hi).b])

def exact_complex_decimal(z):
    # The decimal strings define the selected mathematical constants.
    return iv.mpc(str(mp.re(z)),str(mp.im(z)))

def upper(z):
    return abs(z).b

def max_upper(*zs):
    ans=upper(zs[0])
    for z in zs[1:]:
        b=upper(z)
        if b>ans:
            ans=b
    return ans

def disk_box(e):
    E=upper(e)
    return iv.mpc(iv.mpf([-E,E]),iv.mpf([-E,E]))

def tail1(r,N):
    return r**(N+1)*((N+1)/(1-r)+r/(1-r)**2)

def tail2(r,N):
    return r**(N+1)*((N+1)**2/(1-r)+2*(N+1)*r/(1-r)**2+r*(1+r)/(1-r)**3)

def wp_iv(z,t,N=24):
    q=iv.exp(2*PI*II*t)
    p=q*iv.exp(2*PI*II*z)
    m=q*iv.exp(-2*PI*II*z)
    qn,pn,mn=q,p,m
    sn,cs=iv.sin(PI*z),iv.cos(PI*z)
    f=PI**2/sn**2-PI**2/3
    d=-2*PI**3*cs/sn**3
    for n in range(1,N+1):
        f+=8*PI**2*n*(qn-(pn+mn)/2)/(1-qn)
        d+=8*PI**3/II*n*n*(pn-mn)/(1-qn)
        qn*=q;pn*=p;mn*=m
    r=upper(q)
    zrad=max_upper(p,m)
    if not zrad<1:
        raise ValueError('the Fourier tail strip was not certified')
    ef=8*PI**2/(1-r)*(tail1(r,N)+tail1(zrad,N))
    ed=16*PI**3/(1-r)*tail2(zrad,N)
    return f+disk_box(ef),d+disk_box(ed)

def wp_mp(z,t,N=35):
    q=mp.exp(2*mp.pi*1j*t)
    p=q*mp.exp(2*mp.pi*1j*z)
    m=q*mp.exp(-2*mp.pi*1j*z)
    qn,pn,mn=q,p,m
    f=mp.pi**2/mp.sin(mp.pi*z)**2-mp.pi**2/3
    d=-2*mp.pi**3*mp.cos(mp.pi*z)/mp.sin(mp.pi*z)**3
    for n in range(1,N+1):
        f+=8*mp.pi**2*n*(qn-(pn+mn)/2)/(1-qn)
        d+=8*mp.pi**3/1j*n*n*(pn-mn)/(1-qn)
        qn*=q;pn*=p;mn*=m
    return f,d

def centre_root(t):
    z=mp.mpf('.5')-mp.log(5+2*mp.sqrt(6))*1j/(2*mp.pi)
    for k in range(90):
        f,d=wp_mp(z,t)
        step=f/d
        if abs(step)>mp.mpf('.15'):
            step*=mp.mpf('.15')/abs(step)
        z-=step
        if abs(step)<mp.mpf('1e-36'):
            break
    return z,1/wp_mp(z,t)[1]

def N2_iv(z,t):
    h=z-(1-t)/2
    th=iv.mpc(1,0)
    for n in range(1,11):
        th+=2*iv.exp(PI*II*n*n*t)*iv.cos(2*PI*n*h)
    # Uniform bound on the n>=11 terms, using a decreasing ratio.
    Tmin=t.imag.a
    H=upper(h.imag)
    first=iv.exp(-PI*Tmin*121+2*PI*11*H)
    ratio=iv.exp(-PI*Tmin*23+2*PI*H)
    if not ratio.b<1:
        raise ValueError('the theta tail ratio was not certified')
    th+=disk_box(2*first/(1-ratio))
    q=iv.exp(2*PI*II*t)
    et=iv.exp(PI*II*t/12)
    qn=q
    for n in range(1,18):
        et*=1-qn
        qn*=q
    qr=upper(q)
    e=qr**18/((1-qr)*(1-qr**18))
    et*=iv.exp(disk_box(e))
    return abs(th/et)**2*iv.exp(-2*PI*h.imag**2/t.imag)

def mp_rat(q):
    return mp.mpf(q.numerator)/q.denominator

def certify(box):
    x0,x1,y0,y1=box
    tmid=mp.mpc(mp_rat((x0+x1)/2),mp_rat((y0+y1)/2))
    if tmid==1j:
        return False,{'reason':'central double zero'}
    z0,A=centre_root(tmid)
    tc=iv.mpc(range_iv(x0,x1),range_iv(y0,y1))
    zc=exact_complex_decimal(z0)
    Ac=exact_complex_decimal(A)
    f,_=wp_iv(zc,tc)
    off=-Ac*f
    rad=(iv.mpf(7)/5*max_upper(off.real,off.imag,iv.mpf('1e-28'))).b
    for attempt in range(5):
        Z=zc+disk_box(rad)
        _,d=wp_iv(Z,tc)
        op=1-Ac*d
        opnorm=(upper(op.real)+upper(op.imag)).b
        K=off+op*disk_box(rad)
        err=max_upper(K.real,K.imag)
        if err<rad and opnorm<1:
            val=N2_iv(Z,tc)
            return bool(val.b<2),{'reason':'norm bound','norm_squared_upper':str(val.b),'radius':str(rad),'operator_norm_upper':str(opnorm)}
        rad=(rad*iv.mpf(17)/10).b
    return False,{'reason':'interval contraction not certified','radius':str(rad),'operator_norm_upper':str(opnorm)}

def box_string(box):
    return [str(x) for x in box]

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='sample':
        samples=[('0.095','.105','.995','1.005'),('.245','.255','.995','1.005'),('0','.005','1.005','1.01'),('0','.00001','1.00001','1.00002'),('.49','.5','.866','.88')]
        records=[]
        for ss in samples:
            box=tuple(F(x) for x in ss)
            start=time.time()
            ok,why=certify(box)
            record={'box':box_string(box),'certified':ok,'certificate':why,'seconds':time.time()-start}
            records.append(record)
            print(json.dumps(record),flush=True)
        Path(__file__).with_name('f_interval_sample.out.txt').write_text(json.dumps(records,indent=2)+'\n')
    else:
        queue=[(F(0),F(1,2),F(17,20),F(2))]
        done=[];omitted=[];undecided=[]
        start=time.time()
        while queue:
            box=queue.pop()
            x0,x1,y0,y1=box
            if x1<=LOCAL and y0>=1-LOCAL and y1<=1+LOCAL:
                omitted.append(box_string(box))
                continue
            try:
                ok,why=certify(box)
            except Exception as e:
                ok=False;why={'reason':str(e)}
            if ok:
                done.append({'box':box_string(box),'certificate':why})
            elif max(x1-x0,y1-y0)<LOCAL/2048:
                undecided.append({'box':box_string(box),'certificate':why})
            elif x1-x0>=y1-y0:
                xm=(x0+x1)/2
                queue.extend([(x0,xm,y0,y1),(xm,x1,y0,y1)])
            else:
                ym=(y0+y1)/2
                queue.extend([(x0,x1,y0,ym),(x0,x1,ym,y1)])
            if len(done)>0 and len(done)%200==0:
                print('progress',len(done),'pending',len(queue),'undecided',len(undecided),'seconds',round(time.time()-start,2),flush=True)
            if len(undecided)>30:
                break
        summary={'result':'PASS' if not queue and not undecided else 'UNFINISHED','precision_decimal_digits':iv.dps,'rectangle':['0','1/2','17/20','2'],'omitted_square_radius':str(LOCAL),'certified_boxes':len(done),'omitted_boxes':len(omitted),'pending_boxes':len(queue),'undecided_boxes':undecided,'elapsed_seconds':time.time()-start}
        full={'summary':summary,'certified':done,'omitted':omitted,'pending':[box_string(b) for b in queue]}
        Path(__file__).with_name('f_interval_certificate.json').write_text(json.dumps(full,indent=2)+'\n')
        Path(__file__).with_name('f_interval_cert.out.txt').write_text(json.dumps(summary,indent=2)+'\n')
        print(json.dumps(summary,indent=2),flush=True)
