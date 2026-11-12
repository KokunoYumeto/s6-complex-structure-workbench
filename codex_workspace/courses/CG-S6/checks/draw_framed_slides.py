from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-FRAMED-SLIDE-20261010','font.size':12})
def step(x):
    z=np.asarray(x,dtype=float)
    out=np.zeros_like(z);out[z>=1]=1
    mask=(z>0)&(z<1);a=np.exp(-1/z[mask]);b=np.exp(-1/(1-z[mask]));out[mask]=a/(a+b)
    return out
fig=plt.figure(figsize=(14,10))
fig.text(.5,.96,'The belt crossing, its exact flow map, and the cancellation',ha='center',fontsize=18,fontweight='bold')
ax=fig.add_axes([.075,.515,.39,.34])
v=np.linspace(-1,1,1000);eps=.25
chi=1-step(3*np.abs(v)-1)
colors=['#355e75','#738da1','#a5afb9','#b8758a','#933b67']
for t,col in zip([0,.25,.5,.75,1],colors):
    ax.plot(v,-eps+2*eps*t*chi,color=col,lw=2,label=fr'$t={t:g}$')
ax.scatter([0],[0],s=55,color='#1d2429',zorder=6)
ax.annotate('belt in this slice',(0,0),xytext=(.33,.34),fontsize=10,arrowprops=dict(arrowstyle='->',color='#1d2429'))
ax.annotate('',(.48,-.25),(.2,-.25),arrowprops=dict(arrowstyle='->',lw=2,color=colors[0]))
ax.annotate('',(.23,.25),(-.05,.25),arrowprops=dict(arrowstyle='->',lw=2,color=colors[-1]))
ax.set_xlim(-1.05,1.05);ax.set_ylim(-.39,.39)
ax.set_xlabel(r'$x_1=v$');ax.set_ylabel(r'$x_2=-\varepsilon+2\varepsilon t\chi_0(v)$')
ax.set_title('Actual normal slice: '+r'$\ell=1,\ \varepsilon=1/4,\ \zeta=0$',fontsize=12,fontweight='bold')
ax.grid(alpha=.2);ax.legend(loc='lower left',fontsize=9,ncol=3)
fig.text(.27,.407,r'$\det D_{(v,t)}(x_1,x_2)=2\varepsilon=1/2$'+'\nAfter arc + reverse before arc: clockwise, relator exponent −1.',ha='center',fontsize=11)
ax2=fig.add_axes([.585,.515,.36,.34])
r=np.linspace(0,5,600)
rq=7*np.sqrt((2*r*r/5)/(3+np.sqrt(9+8*r*r/5)))
epsf=.2;c=67/47
eta=lambda q:float(step((q-5+2*epsf)/epsf))
integ=np.array([0 if q<=4.6 else quad(eta,4.6,q,epsabs=1e-11)[0] for q in r])
rf=c*r+(1-c)*integ
ax2.plot(r,rf,color='#6c8391',lw=2,label=r'$P:\ F(\rho)$')
ax2.plot(r,rq,color='#933b67',lw=2,label=r'$Q:\ 7\Lambda(\rho)^{-1/2}$')
ax2.scatter([0,5],[0,7],s=30,color='#1d2429')
ax2.set_xlim(0,5.1);ax2.set_ylim(0,7.3);ax2.grid(alpha=.2);ax2.legend(loc='upper left',fontsize=10)
ax2.set_xlabel(r'original positive-face radius $\rho$')
ax2.set_ylabel('original target normal radius')
ax2.set_title('Before rounding: '+r'$\delta=3,\ \beta=2,\ r=5,\ s=7$',fontsize=12,fontweight='bold')
fig.text(.765,.407,'Different inside the handle; equal on the common exterior.\nFull local derivatives: (6.15)–(6.19).',ha='center',fontsize=11)
fig.text(.12,.32,r'$E\subset N$',ha='center',fontsize=20)
fig.text(.42,.32,r'$e(E)\subset S$',ha='center',fontsize=20)
fig.text(.80,.32,r'$H(e(E))\subset f^{-1}(b)$',ha='center',fontsize=18)
canvas=fig.add_axes([0,0,1,1],frameon=False);canvas.set_axis_off()
for start,end,label in [((.2,.33),(.33,.33),r'$e=J|_E$'),((.53,.33),(.66,.33),r'$H$')]:
    canvas.annotate('',end,start,arrowprops=dict(arrowstyle='->',lw=1.7,color='#173c4e'))
    fig.text((start[0]+end[0])/2,.36,label,ha='center',fontsize=15)
canvas.annotate('',(.12,.275),(.8,.275),arrowprops=dict(arrowstyle='->',lw=1.7,color='#933b67'))
fig.text(.46,.242,'actual descending flow: '+r'$(\mathrm{flow}_{b\to a})\,H e=1_E$',ha='center',fontsize=15,color='#933b67')
fig.text(.5,.175,r'$c_1<b_-<c_p^\prime<a<c_2<f(p)<f(r)$',ha='center',fontsize=16)
fig.text(.5,.125,'Lower p along its complete escaping disk; its circle at b− crosses the stable section of q once.\nCancel p and q. The inserted index-three handle r remains with its full transported attachment.',ha='center',fontsize=12)
fig.text(.5,.055,'Sections 3–4 prove the crossing and sign; Sections 6–7 prove the actual maps and cancellation.\nCurves are numerical samples of the retained formulas. Laudenbach, arXiv:1307.2545v1, supplies the cited cancellation source.',ha='center',fontsize=10)
fig.savefig(O/'framed-slide-and-original-flow.svg',metadata={'Date':None})
print(str(O/'framed-slide-and-original-flow.svg'))

