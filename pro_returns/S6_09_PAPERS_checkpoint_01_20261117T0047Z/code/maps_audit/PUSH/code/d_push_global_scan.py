"""Exploratory double-precision scan of both exact D.4 gradient factors.
Not an interval certificate. Every discovered candidate is retained.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import root
pi=np.pi
rho=.5+1j*np.sqrt(3)/2
seed=.5-1j*np.log(5+2*np.sqrt(6))/(2*pi)
n=np.arange(1,37,dtype=float)
def data(tau,z0=seed):
    q=np.exp(2j*pi*tau); a=q**n/(1-q**n)
    def f(z):
        ss=np.sin(pi*z);cc=np.cos(pi*z)
        cs=np.cos(2*pi*n*z);sn=np.sin(2*pi*n*z)
        w=pi*pi/(ss*ss)-pi*pi/3+8*pi*pi*np.sum(n*a*(1-cs))
        p=-2*pi**3*cc/(ss**3)+16*pi**3*np.sum(n*n*a*sn)
        return w,p
    z=z0
    for k in range(60):
        w,p=f(z)
        if abs(w)<3e-13:break
        if abs(p)<1e-14: z+=1e-5*(1+1j);continue
        step=w/p
        # Damping avoids excursions to poles and floating-point overflow.
        for j in range(16):
            zz=z-step*(.5**j)
            if abs(zz.imag)<2 and abs(f(zz)[0])<abs(w):break
        else: break
        z=zz
    w,p=f(z)
    if abs(w)>2e-10:raise ValueError((tau,z,w))
    L=pi/np.tan(pi*z)+4*pi*np.sum(a*np.sin(2*pi*n*z))
    Z=L+2j*pi*z.imag/tau.imag
    g2=4*pi**4/3*(1+240*np.sum(n**3*a))
    F=3*Z*p-2*g2
    return z,Z,F,p,g2,abs(w)
def inside(tau,tol=1e-7):
    return tau.imag>0 and -.000001<=tau.real<=.500001 and abs(tau)>=1-tol and tau.imag<=5
results=[];failed=[]
xs=np.linspace(0,.5,101)
ys=np.unique(np.r_[np.linspace(np.sqrt(3)/2,1.25,121),np.linspace(1.25,2,61),np.linspace(2,4,41)])
for x in xs:
    previous=seed
    for y in ys[::-1]:
        tau=x+1j*y
        if abs(tau)<1-1e-12 or abs(tau-1j)<1e-6 or abs(tau-rho)<1e-6:continue
        try:
            z,Z,F,P,g2,res=data(tau,previous);previous=z
            results.append((x,y,abs(Z),abs(F),res))
        except Exception as exc: failed.append(str(exc))
# Add both modular boundary arcs, in addition to the rectangular grid.
for x in np.linspace(0,.5,501)[1:-1]:
    tau=x+1j*np.sqrt(1-x*x)
    try:
        z,Z,F,P,g2,res=data(tau)
        results.append((tau.real,tau.imag,abs(Z),abs(F),res))
    except Exception as exc:failed.append(str(exc))
# Root solves from all grid-near local minima and a coarse seed grid.
arr=np.array(results)
starts=[complex(x,y) for x in np.linspace(0,.5,13) for y in np.linspace(.87,3,19) if abs(x+1j*y)>=1]
for index in [2,3]:
    # Include smallest values away from the known elliptic points.
    away=arr[(np.abs(arr[:,0]+1j*arr[:,1]-rho)>.04)&(np.abs(arr[:,0]+1j*arr[:,1]-1j)>.04)]
    starts += [complex(v[0],v[1]) for v in away[np.argsort(away[:,index])[:25]]]
roots={"Z":[],"3ZP-2g2":[]};solve_failures=0
for which in [1,2]:
    name='Z' if which==1 else '3ZP-2g2'
    for start in starts:
        def eq(v):
            tau=complex(v[0],v[1])
            if tau.imag<.65 or tau.imag>8 or abs(tau.real)>2:return [1e3+tau.real,1e3+tau.imag]
            try:
                out=data(tau)[which]
                scale=1 if which==1 else 100
                return [out.real/scale,out.imag/scale]
            except Exception:return [1e3+tau.real,1e3+tau.imag]
        sol=root(eq,[start.real,start.imag],tol=1e-10)
        if np.linalg.norm(eq(sol.x))<1e-7:
            tau=complex(*sol.x)
            if not any(abs(tau-complex(*old[:2]))<2e-5 for old in roots[name]):
                roots[name].append([tau.real,tau.imag,float(np.linalg.norm(eq(sol.x))),bool(inside(tau))])
        else:solve_failures+=1
out={'status':'exploratory only; no enclosure or nonvanishing theorem',
     'precision':'numpy complex128; 36 Fourier terms; checked wp residual',
     'grid_points':len(results),'grid_failures':failed,
     'worst_wp_residual':float(arr[:,4].max()),'root_solve_failures':solve_failures,'roots':roots}
for radius in [.02,.05,.1]:
    away=arr[(np.abs(arr[:,0]+1j*arr[:,1]-rho)>radius)&(np.abs(arr[:,0]+1j*arr[:,1]-1j)>radius)]
    out['min_away_'+str(radius)]={}
    for index,name in [(2,'Z'),(3,'3ZP-2g2')]:
        row=away[np.argmin(away[:,index])]
        out['min_away_'+str(radius)][name]={'tau':[float(row[0]),float(row[1])],'absolute_value':float(row[index])}
p=Path(__file__).with_name('d_push_global_scan.json');p.write_text(json.dumps(out,indent=2))
np.savetxt(Path(__file__).with_name('d_push_global_scan.csv'),arr,delimiter=',',header='real_tau,imag_tau,abs_Z,abs_3ZP_minus_2g2,wp_residual',comments='')
print(json.dumps(out,indent=2))
