from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-HANDLE-REARRANGEMENT-20261010','font.size':11})
def chi(z):
 z=np.asarray(z,dtype=float);v=np.zeros_like(z);v[z>=1]=1
 mask=(z>0)&(z<1);p=np.exp(-1/z[mask]);q=np.exp(-1/(1-z[mask]));v[mask]=p/(p+q)
 return v
def integ(y,x):return np.r_[0,np.cumsum((y[1:]+y[:-1])*(x[1:]-x[:-1])/2)]
r=2.;s=3.;delta=5.;beta=7.;L=2.
t=np.linspace(0,1,4001);kap=chi(3*t-1);U=L*integ(kap,t);V=L*(.5-integ(1-kap,t))
V=np.maximum(V,0)
R=r*np.sqrt(1-U/(delta+beta+V));T=s*np.sqrt(1+V/beta)
fig=plt.figure(figsize=(14,9))
fig.text(.5,.965,'Retain the collars, move the full tube, then interchange the handles',ha='center',fontsize=17,fontweight='bold')
ax=fig.add_axes([.075,.49,.35,.36])
ax.plot([1.88,2],[3,3],color='#9b542b',ls=':',lw=2)
ax.plot([2,2],[3,3.26],color='#176c7b',ls=':',lw=2)
ax.plot(R,T,color='#923e79',lw=2.6)
ax.scatter([R[0],R[-1]],[T[0],T[-1]],s=35,color='#923e79')
for i in [1500,2300]:
 ax.annotate('',xy=(R[i+130],T[i+130]),xytext=(R[i],T[i]),arrowprops=dict(arrowstyle='->',color='#923e79',lw=2))
ax.annotate(r'$w=w_+$',(R[0],T[0]),xytext=(-55,9),textcoords='offset points',color='#923e79')
ax.annotate(r'$w=w_-$',(R[-1],T[-1]),xytext=(5,10),textcoords='offset points',color='#923e79')
ax.annotate('original corner',(2,3),xytext=(2.005,3.08),fontsize=10,ha='left',arrowprops=dict(arrowstyle='->',color='#666666'))
ax.set_xlim(1.875,2.045);ax.set_ylim(2.97,3.265);ax.set_xlabel(r'$R=\Vert u\Vert$');ax.set_ylabel(r'$T=\Vert v\Vert$')
ax.spines[['top','right']].set_visible(False);ax.set_title('The specified radial corner comparison',pad=14,fontweight='bold')
ax2=fig.add_axes([.565,.49,.35,.36])
m=1.;s0=2.;R1=5.;R2=6.;end=np.log(5);ts=np.linspace(0,end,2401)
def velocity(rr):
 vv=rr*rr
 zz=chi((vv-m*m/4)/(3*m*m/4))*(1-chi((vv-R1*R1)/(R2*R2-R1*R1)))
 return float(zz)*rr
final=[]
for start,color in [(1.,'#176c7b'),(2.,'#bd6634')]:
 vals=[start]
 for dt in np.diff(ts):
  v=vals[-1];k1=velocity(v);k2=velocity(v+dt*k1/2);k3=velocity(v+dt*k2/2);k4=velocity(v+dt*k3)
  vals.append(v+dt*(k1+2*k2+2*k3+k4)/6)
 ax2.plot(ts,vals,color=color,lw=2.4,label=r'$\rho='+str(int(start))+'$')
 ax2.scatter([end],[vals[-1]],s=30,color=color)
 final.append(vals[-1])
for y,color,label in [(2,'#999999','original tube radius 2'),(5,'#176c7b','target radius 5'),(6,'#777777','outer support radius 6')]:
 ax2.axhline(y,color=color,ls=':',lw=1.2)
 ax2.text(.90 if y==2 else .03,y+.075,label,fontsize=9,color=color)
ax2.axvline(end,color='#bbbbbb',ls=':',lw=1)
ax2.set_xlim(0,end+.15);ax2.set_ylim(.85,6.5);ax2.set_xlabel(r'$\tau$');ax2.set_ylabel(r'$R(\tau,\rho)$')
ax2.set_xticks([0,.5,1,end],[r'$0$',r'$1/2$',r'$1$',r'$\log 5$'])
ax2.spines[['top','right']].set_visible(False);ax2.legend(loc='lower right',fontsize=10)
ax2.set_title('The complete supported outward flow',pad=14,fontweight='bold')
fig.text(.25,.405,r'$r=2,\ s=3,\ \delta=5,\ \beta=7,\ L=2$',ha='center',fontsize=12)
fig.text(.25,.36,r'$R=r\sqrt{1-\frac{U}{\delta+\beta+V}},\quad T=s\sqrt{1+\frac{V}{\beta}}$',ha='center',fontsize=14)
fig.text(.75,.405,r'$m=1,\ R_1=5,\ R_2=6,\ \tau_*=\log 5$',ha='center',fontsize=12)
fig.text(.75,.36,r'$R(\log 5,1)=5,\qquad 5<R(\log 5,2)<6$',ha='center',fontsize=13)
boxes=[(.15,r'$W\cup_\varphi H_\mu\cup_\alpha H_\lambda$'),(.5,r'$W\cup_{\varphi,\alpha_1}(H_\mu\sqcup H_\lambda)$'),(.85,r'$W\cup_{\alpha_1}H_\lambda\cup_\varphi H_\mu$')]
for x,txt in boxes:
 fig.text(x,.24,txt,ha='center',va='center',fontsize=13,bbox=dict(boxstyle='round,pad=.65',facecolor='#eef3f2',edgecolor='#9aaca9'))
axd=fig.add_axes([0,0,1,1]);axd.axis('off')
for lo,hi in [(.285,.345),(.655,.715)]:
 axd.annotate('',xy=(hi,.24),xytext=(lo,.24),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',color='#19394e',lw=1.5))
fig.text(.312,.29,'full tube\nisotopy',ha='center',fontsize=10)
fig.text(.685,.29,'disjoint\nattachments',ha='center',fontsize=10)
fig.text(.5,.155,r'$\alpha_1=P_\mu^{-1}\mathcal{T}_{\tau_*}P_\mu\mathcal{C}_{t_c}\mathcal{I}_1\alpha$',ha='center',fontsize=18)
fig.text(.5,.10,'The same original parameter disks occur in both orders; their full framed embeddings are carried by these maps.',ha='center',fontsize=11)
fig.text(.5,.045,'Equations (1.5)–(1.19), (3.2)–(3.11), (4.4)–(4.13). Curves are numerical samples; Section 5.1 proves the exact flow bounds.',ha='center',fontsize=10.5)
fig.savefig(O/'original-handle-interchange.svg',metadata={'Date':'2026-10-10'},bbox_inches='tight')

plt.close(fig)
print({'flow_samples':final,'exact_bounds_check':abs(final[0]-5)<1e-9 and 5<final[1]<6})

