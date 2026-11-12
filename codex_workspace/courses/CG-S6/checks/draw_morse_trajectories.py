from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-MORSE-TRAJECTORIES-20261010','font.size':11})
def chi(v):
 v=np.asarray(v,dtype=float);a=np.zeros_like(v);a[v>=1]=1
 m=(v>0)&(v<1);p=np.exp(-1/v[m]);q=np.exp(-1/(1-v[m]));a[m]=p/(p+q)
 return a
fig=plt.figure(figsize=(14,8))
fig.text(.5,.96,'Move the attaching trajectories, then lower the original critical value',ha='center',fontsize=17,fontweight='bold')
ax=fig.add_axes([.075,.32,.35,.5])
t=np.linspace(2,6,1801);eta=1-chi((t-3)/2)
for q1,col in [(-1,'#923e79'),(0,'#176c7b'),(1,'#bd6634')]:
 xx=q1+eta
 ax.plot(xx,t,color=col,lw=2.5)
 ax.scatter([q1,q1+1],[6,2],color=col,s=30)
 for i in [1350,900,450]:
  ax.annotate('',xy=(xx[i-65],t[i-65]),xytext=(xx[i],t[i]),arrowprops=dict(arrowstyle='->',color=col,lw=2))
 ax.text(q1,6.13,str(q1),ha='center',color=col)
 ax.text(q1+1,1.75,str(q1+1),ha='center',color=col)
ax.axhspan(2,3,color='#edf3f2',zorder=-1);ax.axhspan(5,6,color='#edf3f2',zorder=-1)
ax.axhline(2,color='#999999',lw=.8);ax.axhline(6,color='#999999',lw=.8)
ax.set_ylim(1.55,6.5);ax.set_xlim(-1.45,2.45)
ax.set_xlabel(r'$q_1+\eta(t)q_2^2\quad(q_2=1)$');ax.set_ylabel(r'original level $t$')
ax.spines[['top','right']].set_visible(False)
ax.set_title('The exact descending shear',pad=14,fontweight='bold')
ax2=fig.add_axes([.565,.32,.35,.5])
v=np.linspace(0,1,12001)
b=4/3*chi(12*v-1)*chi(11-12*v)
cum=np.r_[0,np.cumsum((b[1:]+b[:-1])*np.diff(v)/2)]
beta=1-cum
A=9*v;old=11-A;new=11-A-6*beta
ax2.plot(A,old,color='#b46c42',lw=2,label=r'original $11-A$')
ax2.plot(A,new,color='#176c7b',lw=2.5,label=r'changed $11-A-6\beta(A/9)$')
ax2.scatter([0,0,9],[11,5,2],color=['#b46c42','#176c7b','#176c7b'],s=30)
ax2.annotate('',xy=(0,5),xytext=(0,11),arrowprops=dict(arrowstyle='->',color='#923e79',lw=1.8))
ax2.text(.3,8.0,r'$\delta=6$',color='#923e79')
ax2.text(7.3,2.45,r'$a=2$',fontsize=11)
ax2.axvline(.75,color='#aaaaaa',ls=':',lw=1)
ax2.axvline(8.25,color='#aaaaaa',ls=':',lw=1)
ax2.set_xlim(-.35,9.4);ax2.set_ylim(1.2,11.8)
ax2.set_xlabel(r'original $A=2x_1^2+7x_2^2$');ax2.set_ylabel(r'$f$ on the disk $B=0$')
ax2.spines[['top','right']].set_visible(False);ax2.legend(loc='upper right',fontsize=10)
ax2.set_title('A supported change with no new critical point',pad=14,fontweight='bold')
fig.text(.25,.21,r'$\eta(t)=1-\chi((t-3)/2),\quad b_0=2,\quad b_1=6$',ha='center',fontsize=13)
fig.text(.25,.155,r'$\widetilde Z=(-\eta^{\prime}(t)q_2^2,0,-1)$',ha='center',fontsize=14)
fig.text(.75,.21,r'$T=9,\quad \delta=6,\quad b(v)=\frac{4}{3}\chi(12v-1)\chi(11-12v)$',ha='center',fontsize=13)
fig.text(.75,.145,r'$1+\frac{\delta}{T}\beta^{\prime}(A/T)\geq\frac{1}{9}>0$',ha='center',fontsize=16)
fig.text(.5,.065,'Equations (1.2)–(1.9), (4.4)–(4.9) and (6.1)–(6.11). Numerical samples of the exact formulas; all six derivatives are proved in the text.',ha='center',fontsize=10.5)
fig.savefig(O/'morse-holonomy-and-lowering.svg',metadata={'Date':'2026-10-10'},bbox_inches='tight')

plt.close(fig)
print({'bump_integral_sample':float(cum[-1]),'new_value_at_A0':float(new[0]),'new_value_at_A9':float(new[-1]),'sampled_negative_derivative_gap':float(np.min(1-2*b/3))})

