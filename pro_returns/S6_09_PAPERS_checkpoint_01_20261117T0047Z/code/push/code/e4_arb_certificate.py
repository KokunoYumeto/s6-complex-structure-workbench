"""Independent Arb recertification of the supplied rational box cover.

No mpmath or code from the earlier certificate is imported. The input supplies
only a finite list of exact rational rectangles. Every elliptic, theta and eta
series and every tail bound used for acceptance is implemented here.

Run: python code/e4_arb_certificate.py --sample
     python code/e4_arb_certificate.py --workers 4
The latter stores every box's new enclosure and a summary next to this file.
"""
from __future__ import annotations
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import time
import flint
from flint import arb, acb, fmpq, ctx

ctx.prec = 192
PI = arb.pi()
I = acb(0, 1)
BASE = Path(__file__).resolve().parent
INPUT = BASE.parents[1] / 'background/s6_02_return/code/f_interval_parallel_certificate.json'

def rat(x):
    q = Fraction(x)
    return arb(fmpq(q.numerator, q.denominator))

def interval(a, b):
    a, b = Fraction(a), Fraction(b)
    return rat((a+b)/2) + arb(0, rat((b-a)/2).upper())

def square_error(e):
    r = e.abs_upper()
    return acb(arb(0, r), arb(0, r))

def tail_moment(r, cut, power):
    """Bound sum_{n>cut} n^power r^n for power 1 or 2.
    For n=cut+k, n <= (cut+1)k, k>=1. Sum k r^(k-1) or
    k^2 r^(k-1) exactly; this differs from the old tail implementation.
    """
    assert r >= 0 and r < 1
    lead = (cut+1)**power * r**(cut+1)
    return lead/(1-r)**2 if power == 1 else lead*(1+r)/(1-r)**3

def wp_series(z, tau, cut=32, certified=True):
    """Weierstrass p and its z derivative, via the cosine Fourier series."""
    q = (2*PI*I*tau).exp()
    s, co = (PI*z).sin(), (PI*z).cos()
    value = PI**2/s**2 - PI**2/3
    deriv = -2*PI**3*co/s**3
    qn = q
    for n in range(1, cut+1):
        angle = 2*PI*n*z
        a = qn/(1-qn)
        value += 8*PI**2*n*a*(1-angle.cos())
        deriv += 16*PI**3*n*n*a*angle.sin()
        qn *= q
    if certified:
        r = q.abs_upper()
        height = z.imag.abs_upper()
        R = (r*(2*PI*height).exp()).upper()
        if not (r < 1 and R < 1):
            raise ArithmeticError('Fourier strip bound fails')
        ev = 8*PI**2*(tail_moment(r,cut,1)+tail_moment(R,cut,1))/(1-r)
        ed = 16*PI**3*tail_moment(R,cut,2)/(1-r)
        value += square_error(ev)
        deriv += square_error(ed)
    return value, deriv

def seed(tau):
    """Only chooses exact dyadic centre and preconditioner, not a proof."""
    z = acb(rat('1/2'), -(5+2*arb(6).sqrt()).log()/(2*PI)).mid()
    for _ in range(100):
        f, d = wp_series(z,tau,cut=40,certified=False)
        dz = (f/d).mid()
        length = dz.abs_upper()
        if not length.is_finite():
            raise ArithmeticError('seed Newton division failed')
        if length > rat('1/8'):
            dz = (dz/(8*length)).mid()
        z = (z-dz).mid()
        if dz.abs_upper() < arb(2)**(-150):
            break
    _, d = wp_series(z,tau,cut=40,certified=False)
    return z, (1/d).mid()

def norm_squared(z, tau):
    h = z-(1-tau)/2
    theta = acb(1)
    cut = 12
    for n in range(1,cut+1):
        theta += 2*(PI*I*n*n*tau).exp()*(2*PI*n*h).cos()
    ymin = tau.imag.lower()
    H = h.imag.abs_upper()
    first = (-PI*ymin*(cut+1)**2 + 2*PI*H*(cut+1)).exp()
    ratio = (-PI*ymin*(2*cut+3) + 2*PI*H).exp()
    assert ratio < 1
    theta += square_error(2*first/(1-ratio))
    # Independently sum log eta, rather than multiply truncated factors.
    q = (2*PI*I*tau).exp()
    logeta = PI*I*tau/12
    qn = q
    eta_cut = 24
    for n in range(1,eta_cut+1):
        logeta += (1-qn).log()
        qn *= q
    r = q.abs_upper()
    eta_tail = r**(eta_cut+1)/((1-r)*(1-r**(eta_cut+1)))
    logeta += square_error(eta_tail)
    theta_abs_squared = theta.real**2 + theta.imag**2
    return theta_abs_squared * (-2*logeta.real-2*PI*h.imag**2/tau.imag).exp()

def certify_box(task):
    idx, box = task
    x0,x1,y0,y1 = map(Fraction,box)
    tmid = acb(rat((x0+x1)/2),rat((y0+y1)/2)).mid()
    tau = acb(interval(x0,x1),interval(y0,y1))
    z0, A = seed(tmid)
    f,_ = wp_series(z0,tau)
    shift = -A*f
    b = max(shift.real.abs_upper(),shift.imag.abs_upper(),arb(2)**(-140))
    best = None
    for multiplier in [Fraction(6,5),Fraction(7,5),Fraction(8,5),Fraction(2),Fraction(3)]:
        r = (rat(multiplier)*b).upper()
        ball = square_error(r)
        Z = z0+ball
        _,d = wp_series(Z,tau)
        L = 1-A*d
        lip = (L.real.abs_upper()+L.imag.abs_upper()).upper()
        image = shift+L*ball
        displacement = max(image.real.abs_upper(),image.imag.abs_upper())
        if not (lip < 1 and displacement < r):
            continue
        n2 = norm_squared(Z,tau)
        bound = n2.upper()
        entry = {'index':idx, 'box':box, 'proved':bool(bound < 2),
                 'norm_squared_upper':bound.str(55,more=True),
                 'radius':r.str(55,more=True),
                 'lipschitz_upper':lip.str(55,more=True),
                 'image_radius_upper':displacement.str(55,more=True),
                 'centre_real':z0.real.str(55,more=True),
                 'centre_imag':z0.imag.str(55,more=True)}
        if best is None or arb(entry['norm_squared_upper']).upper() < arb(best['norm_squared_upper']).upper():
            best = entry
        if entry['proved']:
            return entry
    return best or {'index':idx,'box':box,'proved':False,'reason':'no strict contraction'}

def safe_certify(task):
    try:
        return certify_box(task)
    except Exception as e:
        return {'index':task[0],'box':task[1],'proved':False,'reason':repr(e)}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--sample',action='store_true')
    parser.add_argument('--workers',type=int,default=4)
    parser.add_argument('--limit',type=int)
    args=parser.parse_args()
    source=INPUT.read_bytes()
    payload=json.loads(source)
    tasks=[(i,r['box']) for i,r in enumerate(payload['certified'])]
    if args.sample:
        ids=sorted(set([0,1,2,37,510,2000,5000,10000,15000,len(tasks)-1]))
        tasks=[tasks[i] for i in ids]
    if args.limit:
        tasks=tasks[:args.limit]
    started=time.time()
    completed=[]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for record in pool.map(safe_certify,tasks,chunksize=16):
            completed.append(record)
            if not record['proved']:
                print('FAIL',json.dumps(record),flush=True)
            if len(completed)%500==0:
                print('progress',len(completed),'/',len(tasks),'seconds',round(time.time()-started,2),flush=True)
    good=[r for r in completed if r['proved']]
    worst=max(good,key=lambda r:float(arb(r['norm_squared_upper']).upper())) if good else None
    upper=max((arb(r['norm_squared_upper']).upper() for r in good),default=arb(0))
    summary={'result':'PASS' if len(good)==len(tasks) else 'UNFINISHED',
             'input_sha256':hashlib.sha256(source).hexdigest(),
             'engine':'python-flint '+flint.__version__+'; Arb/acb',
             'precision_bits':ctx.prec,'boxes':len(tasks),'proved':len(good),
             'failures':len(tasks)-len(good),
             'largest_upper_bound':upper.str(55,more=True),
             'worst_index':worst['index'] if worst else None,
             'seconds':time.time()-started,
             'input_use':'rational rectangle endpoints only; no original radii, values, roots or code'}
    name='e4_arb_sample' if args.sample else 'e4_arb_certificate'
    (BASE/(name+'.json')).write_text(json.dumps({'summary':summary,'boxes':completed},indent=2)+'\n')
    (BASE/(name+'_summary.json')).write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
    main()
