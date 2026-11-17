"""Compact-domain Arb nonvanishing check for the two D.4 gradient factors.
Depends explicitly on the already-certified E.4 root enclosures. It does not
assert a global theorem until local i/rho and cusp comparisons are certified.
"""
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from pathlib import Path
import argparse, hashlib, json, time
from flint import arb, acb, ctx
from e4_arb_certificate import rat, interval, square_error, tail_moment
ctx.prec=192
PI=arb.pi(); I=acb(0,1)
BASE=Path(__file__).resolve().parent
INPUT=BASE/'e4_arb_certificate.json'
RHO=acb(rat('1/2'),arb(3).sqrt()/2)
RHO_RADIUS=rat('1/50')
I_RADIUS=rat('3/20000')
def components(z,tau,cut=36):
    q=(2*PI*I*tau).exp()
    sn,co=(PI*z).sin(),(PI*z).cos()
    L=PI*co/sn
    P=-2*PI**3*co/sn**3
    e4=acb(1);e2=acb(1);qn=q
    for n in range(1,cut+1):
        a=qn/(1-qn)
        si=(2*PI*n*z).sin()
        L+=4*PI*a*si
        P+=16*PI**3*n*n*a*si
        e4+=240*n**3*a
        e2-=24*n*a
        qn*=q
    r=q.abs_upper()
    R=(r*(2*PI*z.imag.abs_upper()).exp()).upper()
    if not (r<1 and R<1):raise ArithmeticError('Fourier strip tail bound fails')
    L+=square_error(4*PI*R**(cut+1)/((1-r)*(1-R)))
    P+=square_error(16*PI**3*tail_moment(R,cut,2)/(1-r))
    e4+=square_error(240*(cut+1)**3*r**(cut+1)*(1+4*r+r*r)/(1-r)**5)
    e2+=square_error(24*tail_moment(r,cut,1)/(1-r))
    E=PI**2*e2/3;g2=4*PI**4*e4/3
    b=z.imag/tau.imag
    Z=L+2*PI*I*b
    F=3*Z*P-2*g2
    return {'Z':Z,'F':F,'L':L,'P':P,'g2':g2,'E':E,'b':b}
def certify(record):
    x0,x1,y0,y1=record['box']
    tau=acb(interval(x0,x1),interval(y0,y1))
    out={'index':record['index'],'box':record['box']}
    if (tau-acb(0,1)).abs_upper()<I_RADIUS:
        return dict(out,status='local_i',distance_upper=(tau-acb(0,1)).abs_upper().str(35,more=True))
    if (tau-RHO).abs_upper()<RHO_RADIUS:
        return dict(out,status='local_rho',distance_upper=(tau-RHO).abs_upper().str(35,more=True))
    z0=acb(arb(record['centre_real']),arb(record['centre_imag']))
    radius=arb(record['radius']).upper()
    z=z0+square_error(radius)
    values=components(z,tau)
    zl=values['Z'].abs_lower();fl=values['F'].abs_lower()
    ok=bool(zl>0 and fl>0)
    return dict(out,status='PASS' if ok else 'UNDECIDED',
                Z_abs_lower=zl.str(40,more=True),F_abs_lower=fl.str(40,more=True),
                Z=values['Z'].str(40,more=True),F=values['F'].str(40,more=True))
def safe(record):
    try:return certify(record)
    except Exception as exc:return {'index':record['index'],'box':record['box'],'status':'ERROR','reason':repr(exc)}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=4);parser.add_argument('--sample',action='store_true')
    args=parser.parse_args()
    raw=INPUT.read_bytes();payload=json.loads(raw)
    assert payload['summary']['result']=='PASS'
    records=payload['boxes'];assert all(r['proved'] for r in records)
    if args.sample:
        ids=sorted(set([0,1,2,37,510,2000,5000,10000,15000,len(records)-1]))
        records=[records[i] for i in ids]
    started=time.time();out=[];failures=0
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for r in pool.map(safe,records,chunksize=24):
            out.append(r)
            if r['status'] in ['UNDECIDED','ERROR']:
                failures+=1
                if failures<=25:print('FAIL',json.dumps(r),flush=True)
            if len(out)%1000==0:print('progress',len(out),'/',len(records),'failures',failures,'seconds',round(time.time()-started,2),flush=True)
    counts={k:sum(r['status']==k for r in out) for k in ['PASS','local_i','local_rho','UNDECIDED','ERROR']}
    passed=[r for r in out if r['status']=='PASS']
    summary={'scope':'compact domain only; depends on E.4 roots; local and cusp proof separate',
             'result':'COMPACT_PASS' if not failures else 'UNFINISHED','counts':counts,
             'input_sha256':hashlib.sha256(raw).hexdigest(),'precision_bits':ctx.prec,
             'rho_radius':'1/50','i_radius':'3/20000','seconds':time.time()-started,
             'minimum_Z_lower':min((arb(r['Z_abs_lower']).lower() for r in passed),default=arb(0)).str(40,more=True),
             'minimum_F_lower':min((arb(r['F_abs_lower']).lower() for r in passed),default=arb(0)).str(40,more=True)}
    name='d_push_global_arb_sample' if args.sample else 'd_push_global_arb'
    (BASE/(name+'.json')).write_text(json.dumps({'summary':summary,'boxes':out},indent=2)+'\n')
    (BASE/(name+'_summary.json')).write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':main()
