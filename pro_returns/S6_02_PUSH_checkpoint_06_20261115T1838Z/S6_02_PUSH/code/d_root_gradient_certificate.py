"""Rigorous local/cusp nonvanishing for D.4, independently of compact scan.

Arb enclosures implement Fourier series and all tails directly.  The cusp
uses a complex q rectangle covering the closed disc |q|<=exp(-4*pi), plus
the independent interval 0<=1/Im(tau)<=1/2.  The rho calculation uses a
uniform contraction and the exact derivatives on wp(mu)=0.  The i proof
uses only the analytic constants already established in E.4.2.
"""
from pathlib import Path
from fractions import Fraction
import json
from flint import arb, acb, fmpq, ctx

ctx.prec=256
P=arb.pi(); I=acb(0,1)
BASE=Path(__file__).resolve().parent

def rat(x):
    f=Fraction(x); return arb(fmpq(f.numerator,f.denominator))

def square(r):
    r=abs(r).upper(); return acb(arb(0,r),arb(0,r))

def enclose(a,b):
    return (a+b)/2+arb(0,((b-a)/2).upper())

def bound(x):
    return x.str(65,more=True)

def series(z,q,nterms=40):
    """wp, wp', L=theta1'/theta1, E=pi² E2/3 and g2.
    For tails use (N+k)^j <= (N+1)^j k^j and exact moments
    sum k^j r^(k-1), j=0,1,2,3.
    """
    s=(P*z).sin(); c=(P*z).cos()
    w=P*P/s**2-P*P/3
    pp=-2*P**3*c/s**3
    L=P*c/s
    E=P*P/3
    g2=4*P**4/3
    qn=q
    for n in range(1,nterms+1):
        f=qn/(1-qn); angle=2*P*n*z
        w+=8*P*P*n*f*(1-angle.cos())
        pp+=16*P**3*n*n*f*angle.sin()
        L+=4*P*f*angle.sin()
        E-=8*P*P*n*f
        g2+=320*P**4*n**3*f
        qn*=q
    r=q.abs_upper(); R=(r*(2*P*z.imag.abs_upper()).exp()).upper()
    assert r<1 and R<1
    def tail(a,j):
        moment=[1/(1-a),1/(1-a)**2,(1+a)/(1-a)**3,
                (1+4*a+a*a)/(1-a)**4][j]
        return (nterms+1)**j*a**(nterms+1)*moment
    w+=square(8*P*P*(tail(r,1)+tail(R,1))/(1-r))
    pp+=square(16*P**3*tail(R,2)/(1-r))
    L+=square(4*P*tail(R,0)/(1-r))
    E+=square(8*P*P*tail(r,1)/(1-r))
    g2+=square(320*P**4*tail(r,3)/(1-r))
    return w,pp,L,E,g2

def contraction(z0,q,preconditioner,radius):
    radius=rat(radius) if isinstance(radius,str) else radius
    disk=square(radius); zz=z0+disk
    f=series(z0,q)[0]; pp=series(zz,q)[1]
    shift=-preconditioner*f; lip=1-preconditioner*pp
    lipnorm=(lip.real.abs_upper()+lip.imag.abs_upper()).upper()
    image=shift+lip*disk
    image_norm=max(image.real.abs_upper(),image.imag.abs_upper()).upper()
    return zz,{'radius':bound(radius),'lipschitz_upper':bound(lipnorm),
               'image_radius_upper':bound(image_norm),
               'strict_contraction':bool(lipnorm<1 and image_norm<radius)}

def cusp():
    z0=acb(rat('1/2'),-(5+2*arb(6).sqrt()).log()/(2*P)).mid()
    q=square((-4*P).exp())
    A=(1/series(z0,acb(0))[1]).mid()
    z,record=contraction(z0,q,A,'1/1000')
    assert record['strict_contraction']
    w,pp,L,E,g2=series(z,q)
    invT=enclose(arb(0),rat('1/2'))
    Z=L+2*P*I*z.imag*invT
    F=3*Z*pp-2*g2
    record.update({'q_abs_cover_upper':bound(q.abs_upper()),
                   'Im_Z':bound(Z.imag),'Re_F':bound(F.real),
                   'Z_abs_lower':bound(Z.abs_lower()),
                   'F_abs_lower':bound(F.abs_lower()),
                   'root_centre':str(z0)})
    assert Z.abs_lower()>0 and F.abs_lower()>0
    return record

def rho_local():
    rho=acb(rat('1/2'),arb(3).sqrt()/2)
    zc=(2-rho)/3
    z0=zc.mid(); qc=(2*P*I*rho).exp()
    pp0=series(zc,qc)[1]
    za=I*pp0/(4*P); fa=-21*I*pp0**2/(4*P)
    tau=rho+square(rat('1/50'))
    q=(2*P*I*tau).exp(); A=(1/pp0).mid()
    z,record=contraction(z0,q,A,'1/80')
    uniform_trial=record
    # A single square loses too much dependence.  Partition its exact rational
    # translate of rho; the union still contains the full radius-1/50 disc.
    records=[]
    count=20
    for j in range(count):
        for k in range(count):
            dx0=rat(Fraction(-1,50)+Fraction(j,25*count))
            dx1=rat(Fraction(-1,50)+Fraction(j+1,25*count))
            dy0=rat(Fraction(-1,50)+Fraction(k,25*count))
            dy1=rat(Fraction(-1,50)+Fraction(k+1,25*count))
            tt=rho+acb(enclose(dx0,dx1),enclose(dy0,dy1))
            tm=tt.mid(); zz=(zc-(tm-rho)/3).mid()
            qm=(2*P*I*tm).exp()
            for _ in range(8):
                ww,pp,*_=series(zz,qm)
                zz=(zz-ww/pp).mid()
            aa=(1/series(zz,qm)[1]).mid()
            qq=(2*P*I*tt).exp()
            enclosure,rec=contraction(zz,qq,aa,'1/1000')
            assert rec['strict_contraction'],(j,k,rec)
            branch_distance=(enclosure-zc).abs_upper()
            assert branch_distance<rat('1/50')
            common_square=max((enclosure-z0).real.abs_upper(),(enclosure-z0).imag.abs_upper())
            assert common_square<rat('1/80')
            rec.update(rho_derivatives(enclosure,tt,qq,za,fa))
            rec['distance_from_equianharmonic_root_upper']=bound(branch_distance)
            rec['common_square_sup_radius_upper']=bound(common_square)
            rec['index']=[j,k]
            rec['offset_box']=[str(Fraction(-1,50)+Fraction(j,25*count)),
                               str(Fraction(-1,50)+Fraction(j+1,25*count)),
                               str(Fraction(-1,50)+Fraction(k,25*count)),
                               str(Fraction(-1,50)+Fraction(k+1,25*count))]
            rec['centre_real']=bound(zz.real);rec['centre_imag']=bound(zz.imag)
            records.append(rec)
    (BASE/'d_root_rho_boxes.json').write_text(json.dumps(records,indent=2)+'\n')
    return {'boxes':len(records),'uniform_trial':uniform_trial,
            'common_square_sup_radius_upper':max((arb(r['common_square_sup_radius_upper']).upper() for r in records)).str(65,more=True),
            'Z_dominance':all(r['Z_dominance'] for r in records),
            'F_dominance':all(r['F_dominance'] for r in records),
            'worst_Z_error_upper':max((arb(r['Z_derivative_error_upper']).upper() for r in records)).str(65,more=True),
            'Z_centre_derivative_lower':bound(za.abs_lower()),
            'worst_F_error_upper':max((arb(r['F_derivative_error_upper']).upper() for r in records)).str(65,more=True),
            'F_centre_derivative_lower':bound(fa.abs_lower())}

def rho_derivatives(z,tau,q,za,fa):
    record={}
    w,pp,L,E,g2=series(z,q)
    T=tau.imag; b=z.imag/T
    Z=L+2*P*I*b
    mup=I*L/(2*P)-I*g2/(6*P*pp)
    Zt=(-pp-2*E*L)/(4*P*I)-E*mup+(P/T)*(mup-b)
    Zbt=(P/T)*(b-mup.conjugate())
    Pt=(-3*E*pp-L*g2/2)/(2*P*I)-(g2/2)*mup
    g2t=(2*I*E*g2+3*I*pp**2)/P
    Ft=3*Zt*pp+3*Z*Pt-2*g2t
    Fbt=3*Zbt*pp
    ze=((Zt-za).abs_upper()+Zbt.abs_upper()).upper()
    fe=((Ft-fa).abs_upper()+Fbt.abs_upper()).upper()
    record.update({'Z_derivative_error_upper':bound(ze),
                   'Z_centre_derivative_lower':bound(za.abs_lower()),
                   'F_derivative_error_upper':bound(fe),
                   'F_centre_derivative_lower':bound(fa.abs_lower()),
                   'Z_dominance':bool(ze<za.abs_lower()),
                   'F_dominance':bool(fe<fa.abs_lower()),
                   'P_abs_lower':bound(pp.abs_lower())})
    return record

def i_local():
    a=rat('3/2000'); b=rat('1/800'); eps=rat('3/20000')
    ex=1/(1-a)**2/(1-b)-1
    eh=1/(1-a)/(1-b)**2-1
    gx_error=200*ex
    gh_coefficient=2*(rat('47.30')+500*eh)
    xp=gh_coefficient/(rat('10.03')-gx_error)
    assert xp<11
    rh=30*eh; rx=6*ex
    derivative_error=(rh+rx*xp)/2+P*eps/(1-eps)+P*xp/(2*20000*(1-eps)**2)
    assert derivative_error<rat('.203') and derivative_error<P/2
    return {'a':str(a),'b':str(b),'Gx_error_upper':bound(gx_error.upper()),
            'Gh_coefficient_upper':bound(gh_coefficient.upper()),
            'x_prime_over_h_upper':bound(xp.upper()),
            'Wirtinger_gradient_error_over_h_upper':bound(derivative_error.upper()),
            'leading_coefficient_lower':bound((P/2).lower()),'result':'PASS'}

if __name__=='__main__':
    result={'engine':'python-flint Arb/acb','precision_bits':ctx.prec,
            'i_local':i_local(),'cusp':cusp(),'rho_local':rho_local()}
    result['status']='PASS' if result['rho_local'].get('Z_dominance') and result['rho_local'].get('F_dominance') else 'UNFINISHED'
    (BASE/'d_root_gradient_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
