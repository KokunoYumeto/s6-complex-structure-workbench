"""Finite algebra diagnostics for the proved original-weighted trace theorem.

Exact identities and numerical finite-matrix checks are reported separately.
Neither class certifies an infinite-volume or weak-coupling limit.
"""
from pathlib import Path
import hashlib,json,math
import sympy as s
import numpy as np
root=Path(__file__).resolve().parent
exact=[];numeric=[]
def eq(name,left,right=0):
    residual=s.simplify(left-right)
    assert residual==0,(name,residual)
    exact.append({'name':name,'residual':str(residual)})
u,r,t,a,N,ell,g,theta,I,Omega=s.symbols('u r t a N ell g theta I Omega',positive=True)
eq('full transverse directional angular factor',2*s.pi*s.integrate((1-u**2)**2,(u,-1,1)),32*s.pi/15)
eq('positive octant angular factor',(32*s.pi/15)/8,4*s.pi/15)
eq('radial positive time integral',s.integrate(r**4*s.exp(-2*t*r),(r,0,s.oo)),3/(4*t**5))
eq('physical mode trace coefficient',(4*s.pi/15)*(3/(4*t**5))/s.pi**3,1/(5*s.pi**2*t**5))
eq('fourth spatial moment',s.integrate(u**4,(u,-s.Rational(1,2),s.Rational(1,2))),s.Rational(1,80))
L=s.symbols('L',integer=True,positive=True)
n=s.symbols('n',integer=True)
eq('exact symmetric fourth-power sum',s.summation(n**4,(n,-L,L)),L*(L+1)*(2*L+1)*(3*L**2+3*L-1)/15)
eq('discrete weight mean limit',s.limit(L*(L+1)*(3*L**2+3*L-1)/(15*(2*L+1)**4),L,s.oo),s.Rational(1,80))
eq('weighted heat prefactor',s.Rational(3,32)*s.Rational(1,80)/(5*s.pi**2*t**5),3/(12800*s.pi**2*t**5))
eq('original physical factor',(N**4*a**2*ell**3).subs(N,ell/a),ell**7/a**2)
eq('entire raw mass prefactor',s.Rational(3,32)*s.Rational(1,80)*I,3*I/2560)
eq('energy density Laplace coefficient',s.factorial(4)/(102400*s.pi**2*t**5),3/(12800*s.pi**2*t**5))
eq('bounded energy mass',s.integrate(r**4/(102400*s.pi**2),(r,0,Omega)),Omega**5/(512000*s.pi**2))
eq('probability density coefficient',(1/(102400*s.pi**2))/(3*I/2560),1/(120*s.pi**2*I))
eq('probability interval coefficient',(Omega**5/(512000*s.pi**2))/(3*I/2560),Omega**5/(600*s.pi**2*I))
eq('native total raw coefficient',s.Rational(4,9)*3*I/2560,I/1920)
eq('native finite energy raw coefficient',s.Rational(4,9)*Omega**5/(512000*s.pi**2),Omega**5/(1152000*s.pi**2))
eq('native filtered raw coefficient',s.Rational(4,9)*3/(12800*s.pi**2*t**5),1/(9600*s.pi**2*t**5))
eq('native energy quotient',-s.diff(t**-5,t)/(t**-5),5/t)
for k in range(7):
    eq('positive-time moment '+str(k),s.integrate(r**(k+4)*s.exp(-t*r),(r,0,s.oo)),s.factorial(k+4)/t**(k+5))
z=s.Matrix([[s.Rational(1,9),s.Rational(1,20),s.Rational(-1,30)],[s.Rational(1,20),s.Rational(1,8),s.Rational(1,60)],[s.Rational(-1,30),s.Rational(1,60),s.Rational(1,7)]])
d=s.diag(s.Rational(1,3),s.Rational(2,7),s.Rational(5,9))
comm=z*d-d*z
eq('finite trace commutator identity',s.trace(z*z*d*d)-s.trace(z*d*z*d),s.trace(comm.T*comm)/2)
for nv in (3,5,9,17):
    lv=(nv-1)//2
    pos=np.arange(-lv,lv+1,dtype=float)
    indices=np.arange(nv,dtype=float)
    v=np.cos(np.pi*(pos[:,None]+lv+.5)*indices[None,:]/nv)*np.sqrt((2-(indices==0))/nv)
    zmat=v.T@np.diag((pos/nv)**2)@v
    weights=(pos/nv)**4
    diagmean=weights.mean()
    A=np.diag(v.T@np.diag(weights)@v)
    target=np.array([diagmean if k==0 else diagmean+np.mean(weights*np.cos(2*np.pi*k*(pos+lv+.5)/nv)) for k in range(nv)])
    ortherr=float(np.max(np.abs(v.T@v-np.eye(nv))))
    diagerr=float(np.max(np.abs(A-target)))
    assert ortherr<1e-12 and diagerr<1e-12
    for av,tv in ((.17,.7),(.071,1.3)):
        freq=2*np.sin(np.pi*indices/(2*nv))
        exacttrace=0.;approxtrace=0.;commnorm=0.
        for r1 in range(1,nv):
            for r3 in range(nv):
                sigma=np.sqrt(freq[r1]**2+freq**2+freq[r3]**2)
                ds=(freq**2+freq[r3]**2)/sigma*np.exp(-tv*sigma/av)/av
                exacttrace+=float(np.sum(zmat**2*ds[:,None]*ds[None,:]))
                approxtrace+=float(np.sum(A*ds**2))
                commnorm+=float(np.sum(zmat**2*(ds[:,None]-ds[None,:])**2))
        residual=abs(approxtrace-exacttrace-commnorm/2)
        assert residual<1e-10
        numeric.append({'N':nv,'a':av,'t':tv,'orthogonality_residual':ortherr,'weight_diagonal_residual':diagerr,'trace_commutator_residual':residual})
report={'scope':'Finite exact constants and finite DCT matrix consistency only; analytic limits are proved in retained source.',
 'exact_checks':len(exact),'exact_results':exact,'numerical_matrix_checks':len(numeric),'numerical_results':numeric,
 'sources':{p:{'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest()} for p in ['sources/original_weighted_heat_trace.md','check_original_weighted_trace.py']}}
(root/'ORIGINAL_WEIGHTED_TRACE_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks':len(exact),'numerical_matrix_checks':len(numeric),'all_passed':True}))
