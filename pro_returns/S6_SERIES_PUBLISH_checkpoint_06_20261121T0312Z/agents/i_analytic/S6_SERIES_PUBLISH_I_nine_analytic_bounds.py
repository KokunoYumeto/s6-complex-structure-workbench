"""Fresh interval majorants for ari:C.8.1, C.8.2 and C.8.3.

The local-maximum proof uses a theta3 polydisc, an ODE bootstrap at tau=i,
and Rouche's theorem. No attached proof code or old numerical certificate
is imported. All infinite tails are bounded explicitly below.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import mpmath as mp

iv=mp.iv
iv.dps=75
pi=iv.pi
ROOT=Path(__file__).parent

def positive_gaussian_tail(T,H,k,l,N):
    n=N+1
    degree=k+2*l
    first=2*(2*pi)**k*pi**l*n**degree*iv.exp(-pi*T*n*n+2*pi*H*n)
    ratio=iv.exp(-pi*T*(2*n+1)+2*pi*H)*((iv.mpf(n+1)/n)**degree)
    assert ratio.b<1
    return first/(1-ratio)

def theta_bound(k,l,T,H,N=12):
    """Bounds theta3-1 for k=l=0 and the indicated derivative otherwise."""
    total=iv.mpf(0)
    for n in range(1,N+1):
        z=2*pi*n*H
        hyp=(iv.exp(z)-iv.exp(-z))/2 if k%2 else (iv.exp(z)+iv.exp(-z))/2
        total += 2*(2*pi*n)**k*(pi*n*n)**l*iv.exp(-pi*T*n*n)*hyp
    return total+positive_gaussian_tail(T,H,k,l,N)

def norm_upper(T,N=12):
    theta=1+theta_bound(0,0,T,iv.mpf(0),N)
    r=iv.exp(-2*pi*T)
    product=iv.mpf(1)
    for n in range(1,N+1): product *= 1-r**n
    tail=r**(N+1)/((1-r)*(1-r**(N+1)))
    return iv.exp(pi*T/12)*theta/product*iv.exp(tail)

def divisor_sum(n,k):
    return sum(d**k for d in range(1,n+1) if n%d==0)

def power_series_tail(r,N,degree):
    n=N+1
    ratio=r*(iv.mpf(n+1)/n)**degree
    assert ratio.b<1
    return n**degree*r**n/(1-ratio)

def e4_i():
    r=iv.exp(-2*pi);N=20
    val=1+240*sum((divisor_sum(n,3)*r**n for n in range(1,N+1)),iv.mpf(0))
    tail=240*power_series_tail(r,N,4)
    return val+iv.mpf([0,1])*tail

def main():
    low=iv.sqrt(iv.mpf(3))/2
    ub={name:norm_upper(T) for name,T in [('sqrt3/2',low),('2',iv.mpf(2)),
                    ('7/5',iv.mpf(7)/5),('11/10',iv.mpf(11)/10)]}
    assert ub['sqrt3/2'].b<iv.mpf(143)/100
    assert ub['2'].b<iv.mpf(17)/10
    assert ub['7/5'].b<iv.mpf(3)/2
    assert ub['11/10'].b<iv.mpf(143)/100
    s=iv.exp(-2*pi);r=s*s
    wp_error=8/(1-r)*(r/(1-r)**2+s/(2*(1-s)**2)+s**3/(2*(1-s**3)**2))
    assert wp_error.b<iv.mpf(1)/100
    assert 1/(iv.mpf(1)/3+iv.mpf(1)/100)>((iv.exp(pi/3)+iv.exp(-pi/3))/2)**2
    assert 1/(iv.mpf(1)/3-iv.mpf(1)/100)<(iv.mpf(9)/5)**2
    cusp=iv.mpf(18)/5*iv.exp(-pi/3-pi/18+s/(1-s)+s**3/(1-s**3))
    assert cusp.b<iv.mpf(541)/500

    T=iv.mpf(49)/50;H=iv.mpf(1)/10;D=iv.mpf(1)/50
    b={(k,l):theta_bound(k,l,T,H) for k,l in [(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(0,2)]}
    den=1-b[0,0]
    assert den.a>0
    C4=b[4,0]/den+4*b[3,0]*b[1,0]/den**2+3*b[2,0]**2/den**2+12*b[2,0]*b[1,0]**2/den**3+6*b[1,0]**4/den**4
    C21=b[2,1]/den+b[2,0]*b[0,1]/den**2+2*b[1,0]*b[1,1]/den**2+2*b[1,0]**2*b[0,1]/den**3
    q=iv.exp(-2*pi*T)
    eta_log_second=4*pi*pi*q*(1+q)/(1-q)**5
    C02=b[0,2]/den+b[0,1]**2/den**2+eta_log_second
    eta1_prime=4*pi*eta_log_second
    assert C4.b<350 and C21.b<20 and C02.b<2 and eta1_prime.b<iv.mpf('1.1')
    wp_tau=C21+eta1_prime
    assert wp_tau.b<22
    zero={(k,l):theta_bound(k,l,T,iv.mpf(0)) for k,l in [(0,0),(2,0),(0,1),(2,1),(0,2),(2,2)]}
    dz=1-zero[0,0]
    eta1_second=32*pi**4*q*(1+4*q+q*q)*(1+q)/(1-q)**7
    e3_second=zero[2,2]/dz+2*zero[2,1]*zero[0,1]/dz**2+zero[2,0]*zero[0,2]/dz**2+2*zero[2,0]*zero[0,1]**2/dz**3+eta1_second
    assert e3_second.b<100
    E4=e4_i();G=4*pi**4*E4/3
    assert G.a>189 and G.b<190
    ode_upper=190*H*H/4+3*H*H*(iv.mpf(1)/2)**2
    assert ode_upper.b<iv.mpf(1)/2
    rouche_lower=189*H*H/4-3*H*H*(iv.mpf(1)/2)**2
    assert rouche_lower.a>22*D
    e3_lower=189/(6*pi)-100*D/2
    relation=350/(2*e3_lower)
    assert relation.b<20
    loss=350*H*H/24+20*D/2+2*20*D/2+pi*D/(1-D)
    assert loss.b<pi/2

    # Bound E6'' on the same tau disc, by exact initial divisor sums.
    N=20
    e6_second=504*(2*pi)**2*(sum((n*n*divisor_sum(n,5)*q**n for n in range(1,N+1)),iv.mpf(0))
                                     +power_series_tail(q,N,8))
    assert e6_second.b<60
    E6_boundary=(pi*(iv.mpf(7)/5)**2-60*D/2)*D
    delta_upper=q*iv.exp(24*q/(1-q))
    t_boundary=E6_boundary**2/(1728*delta_upper)
    assert E4.a>iv.mpf(7)/5
    assert t_boundary.a>iv.mpf(1)/500
    result=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
        program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        mpmath_version=mp.__version__,interval_dps=iv.dps,
        C8_1=dict(norm_endpoint_upper={k:str(v) for k,v in ub.items()},
                  cusp_wp_error=str(wp_error),cusp_norm_upper=str(cusp)),
        C8_2=dict(theta_denominator_lower=str(den),F_hhhh=str(C4),
                  F_hhtau=str(C21),F_tautau=str(C02),eta1_prime=str(eta1_prime),
                  wp_tau=str(wp_tau),e3_second=str(e3_second),G=str(G),
                  ode_bootstrap_upper=str(ode_upper),rouche_boundary_lower=str(rouche_lower),
                  tau_to_h2_ratio_upper=str(relation),quadratic_error_coefficient=str(loss),
                  strict_negative_margin=str(pi/2-loss)),
        C8_3=dict(E6_second_derivative=str(e6_second),E6_boundary_lower=str(E6_boundary),
                  Delta0_upper=str(delta_upper),t_minus_one_boundary_lower=str(t_boundary)),
        scope='Rigorous absolute majorants with explicit tails; no pointwise grid or old code imported.')
    (ROOT/'S6_SERIES_PUBLISH_I_nine_analytic_bounds.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
