from pathlib import Path
import numpy as np
def cumulative_trapezoid(y,x,initial=0):
 return np.r_[initial,initial+np.cumsum((y[1:]+y[:-1])*(x[1:]-x[:-1])/2)]
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
W=Path(__file__).resolve().parents[1]
O=W/'assets'
O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-ORIGINAL-HANDLE-20261010','font.size':11})
def chi(z):
 z=np.asarray(z,dtype=float);result=np.zeros_like(z)
 result[z>=1]=1
 mask=(z>0)&(z<1)
 p=np.exp(-1/z[mask]);q=np.exp(-1/(1-z[mask]))
 result[mask]=p/(p+q)
 return result
aa=3.;bb=5.;delta=4/5;beta=5/4;L=2/5
t=np.linspace(0,1,4001);kap=chi(3*t-1)
U=L*cumulative_trapezoid(kap,t,initial=0)
V=L*(.5-cumulative_trapezoid(1-kap,t,initial=0))
V=np.maximum(V,0)
fig=plt.figure(figsize=(15.2,8.2))
fig.text(.5,.955,'An actual handle, its specified corner, and the exact collar map',ha='center',fontsize=18,fontweight='bold')
ax=fig.add_axes([.055,.37,.38,.48])
ys=np.linspace(-.75,.75,1000)
xb=np.sqrt((delta+bb*ys**2)/aa)
ax.fill_betweenx(ys,-1.25,-xb,color='#edd6c2',alpha=.75)
ax.fill_betweenx(ys,xb,1.25,color='#edd6c2',alpha=.75)
yh=np.linspace(-np.sqrt(beta/bb),np.sqrt(beta/bb),600)
xh=np.sqrt((delta+bb*yh*yh)/aa)
ax.fill_betweenx(yh,-xh,xh,color='#a9d9dc',alpha=.85)
ax.plot(xb,ys,color='#9b542b',lw=1.8)
ax.plot(-xb,ys,color='#9b542b',lw=1.8)
for sign in [-1,1]:
 ax.plot([-xh[-1],xh[-1]],[sign*.5,sign*.5],color='#176c7b',lw=2.3)
 for sx in [-1,1]:
  xr=sx*np.sqrt((delta+beta+V-U)/aa)
  yr=sign*np.sqrt((beta+V)/bb)
  ax.plot(xr,yr,color='#ad3858',lw=2.6)
# Chosen arrows are exact positive multiples of (-x,y).
for xx,yy in [(-.9,.3),(.9,.3),(-.9,-.3),(.9,-.3),(.25,.43),(-.25,-.43)]:
 ax.annotate('',xy=(xx-.12*xx,yy+.12*yy),xytext=(xx,yy),arrowprops=dict(arrowstyle='->',color='#19394e',lw=1.2))
ax.text(0,0,r'$H:\ B\leq\beta,\ A\leq\delta+B$',ha='center',fontsize=13)
ax.text(0,.23,r'$f=c-A+B$',ha='center',fontsize=13)
ax.text(1.06,-.04,r'$C_a$',ha='center',color='#9b542b')
ax.text(-1.06,-.04,r'$C_a$',ha='center',color='#9b542b')
ax.text(0,.56,r'$H^+:\ B=\beta$',ha='center',color='#176c7b')
ax.annotate(r'$H^-:\ A=\delta+B$',xy=(.64,-.29),xytext=(-.1,-.66),ha='center',arrowprops=dict(arrowstyle='->',color='#9b542b'),color='#9b542b')
ax.set_xlim(-1.25,1.25);ax.set_ylim(-.76,.76)
ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$y_1$',rotation=0,loc='top')
ax.spines[['top','right']].set_visible(False)
ax.set_title('Original coordinate slice',pad=14,fontweight='bold')
ax2=fig.add_axes([.52,.39,.22,.44])
R=.28
ax2.fill([-0.05,0,0,R,R,-.05],[-.05,-.05,0,0,-.05,-.05],color='#edd6c2')
ax2.axvspan(-.055,0,color='#edd6c2',alpha=.7)
ax2.fill_between([0,R],[-.055,-.055],[0,0],color='#a9d9dc',alpha=.9)
ax2.add_patch(Polygon(np.c_[np.r_[0,U,0],np.r_[0,V,0]],closed=True,color='#efc7d3'))
ax2.plot([0,0],[L/2,R],color='#9b542b',lw=2)
ax2.plot([L/2,R],[0,0],color='#176c7b',lw=2)
ax2.plot(U,V,color='#ad3858',lw=2.7)
for idx in [1450,2000,2550]:
 ax2.annotate('',xy=(U[idx]+.045*(1-kap[idx]),V[idx]+.045*kap[idx]),xytext=(U[idx],V[idx]),arrowprops=dict(arrowstyle='->',color='#ad3858',lw=1.4))
ax2.scatter([0,L/2],[L/2,0],s=18,color='#ad3858')
ax2.set_xlim(-.055,R);ax2.set_ylim(-.055,R);ax2.set_aspect('equal')
ax2.set_xlabel(r'$U=f-a$');ax2.set_ylabel(r'$V=B-\beta$',rotation=90)
ax2.spines[['top','right']].set_visible(False)
ax2.set_title('Outward corner rounding',pad=14,fontweight='bold',fontsize=12)
ax2.text(.15,.245,r'$XU>0,\ XV>0$',ha='center',fontsize=11)
ax3=fig.add_axes([.8,.39,.175,.44])
ell=2/5;T=3/5;ts=np.linspace(-ell,0,700)
eta=chi((ts+3*ell/4)/(ell/2));hs=ts+T*eta
ax3.plot(ts,ts,color='#888888',ls=':',lw=1.5,label=r'$t$')
ax3.plot(ts,hs,color='#176c7b',lw=2.5,label=r'$h_q(t)$')
ax3.scatter([-ell,0],[-ell,T],color='#176c7b',s=25)
ax3.axhline(0,color='#cccccc',lw=.7)
ax3.set_xlabel(r'$t$');ax3.set_ylabel(r'$h_q(t)$')
ax3.set_title('Absorb the outer collar',pad=14,fontweight='bold',fontsize=12)
ax3.spines[['top','right']].set_visible(False)
ax3.legend(loc='upper left',fontsize=10)
fig.text(.245,.255,r'$A=3x_1^2,\ B=5y_1^2,\ \delta=4/5,\ \beta=5/4$',ha='center',fontsize=13)
fig.text(.245,.21,'All other coordinates are zero; arrows follow (-x,y).',ha='center',fontsize=10.5)
fig.text(.625,.265,r'$U^\prime=L\kappa,\quad V^\prime=-L(1-\kappa)$',ha='center',fontsize=12)
fig.text(.625,.215,r'$L=2/5,\quad \kappa=\chi(3t-1)$',ha='center',fontsize=12)
fig.text(.88,.275,r'$h_q=t+T(q)\eta(t)$',ha='center',fontsize=12)
fig.text(.88,.225,r'$\partial_t h_q=1+T(q)\eta^\prime>0$',ha='center',fontsize=11)
fig.text(.88,.175,r'$\ell=2/5,\quad T(q)=3/5$',ha='center',fontsize=11)
fig.text(.5,.115,r'$x_i=\frac{u_i}{r}\sqrt{\frac{\delta+\beta\Vert v\Vert^2/s^2}{a_i}},\qquad y_j=\frac{v_j}{s}\sqrt{\frac{\beta}{b_j}}$',ha='center',fontsize=20)
fig.text(.5,.045,'Equations (4.3)–(4.13), (4.17)–(4.20), (4.26)–(4.30). Pink curves show the retained outward smoothing.',ha='center',fontsize=11)
fig.savefig(O/'original-handle-attachment.svg',metadata={'Date':'2026-10-10'},bbox_inches='tight')

plt.close(fig)

