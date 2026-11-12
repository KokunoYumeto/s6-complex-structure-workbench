from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1];O=W/'assets'
O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-WHITNEY-MOVE-20261010','font.size':12})
R=2.;d=3/5;b=2/5;star=R*R/(R*R+d)
x=np.linspace(-2.23,2.23,6001);phi=R*R-x*x
def rho(q):
 out=np.zeros_like(q);mask=q>0;out[mask]=np.exp(-1/q[mask]);return out
def chi(q):return rho(q)/(rho(q)+rho(1-q))
delta=chi(4*phi/d+2)*(phi+d)
fig=plt.figure(figsize=(12,12))
fig.text(.5,.965,'A supported move of the original two-sheet model',ha='center',fontsize=19,fontweight='bold')
fig.text(.5,.93,r'$R=2,\quad d=3/5,\quad b=2/5;\qquad z_1=z_2=z_3=0$',ha='center',fontsize=16)
for i,(t,title) in enumerate([(0,'Before the move'),(.5,'Two transverse intersections'),(star,'The unique tangency'),(1,'Both intersections removed')]):
 ax=fig.add_axes([.08+.48*(i%2),.615-.315*(i//2),.37,.235])
 inside=np.abs(x)<=R
 ax.fill_between(x[inside],0,phi[inside],color='#e1ebee',alpha=.7,label=r'Original $D_R$')
 ax.axhline(0,color='#b56232',lw=2,label=r'$B_0$ in this slice')
 ax.plot(x,phi-t*delta,color='#226e84',lw=2.3,label=r'$\mathcal{H}_t(A_0)$ in this slice')
 if t<star:
  xp=np.sqrt(R*R-t*d/(1-t))
  ax.scatter([-xp,xp],[0,0],s=38,color='#173446',zorder=5)
  ax.text(-xp,.26,'+',ha='center',fontsize=20,color='#173446');ax.text(xp,.26,'−',ha='center',fontsize=20,color='#173446')
 elif t==star:ax.scatter([0],[0],s=45,color='#173446',zorder=5)
 ax.set_xlim(-2.24,2.24);ax.set_ylim(-1.25,4.4);ax.set_xticks([-2,0,2]);ax.set_yticks([-.6,0,2,4],['−3/5','0','2','4'])
 ax.set_xlabel(r'$x$',loc='right');ax.set_ylabel(r'$y$',loc='top',rotation=0)
 ax.spines[['top','right']].set_visible(False)
 tt=['0','1/2','20/23','1'][i]
 ax.set_title(title+'\n'+r'$t='+tt+'$',fontsize=13,pad=10)
 if i==0:ax.legend(fontsize=9,loc='upper right')
fig.text(.5,.218,r'$x_\pm(t)=\pm\sqrt{R^2-td/(1-t)},\qquad t_*=\frac{R^2}{R^2+d}$',ha='center',fontsize=20)
fig.text(.5,.166,r'$\det(TA_t,TB_0)=-2(1-t)x,\qquad\det D\mathcal{H}_t=J_t>0$',ha='center',fontsize=18)
fig.text(.5,.111,r'$\varphi_{\ell,t}=H_t\circ\varphi_\ell,\qquad D\varphi_{\ell,t}=DH_t\,D\varphi_\ell$',ha='center',fontsize=20)
fig.text(.5,.067,'The fixed comparison belt is used to count intersections. All original attaching tubes are transported.',ha='center',fontsize=11.5)
fig.text(.5,.038,'Exact formulas (1.3), (1.8)–(1.11), (2.4), (6.2), (6.5). The plots sample the full cutoff expression.',ha='center',fontsize=11)
fig.savefig(O/'supported-whitney-move.svg',metadata={'Date':'2026-10-10'},bbox_inches='tight')
plt.close(fig)
