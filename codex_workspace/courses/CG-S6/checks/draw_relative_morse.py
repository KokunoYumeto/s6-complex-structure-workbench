from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1];O=W/'assets'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-RELATIVE-MORSE-20261010','font.size':12})
aa=3.;bb=5.;delta=4/5;x0=1.;y0=3/10
A=aa*x0*x0;B=bb*y0*y0;root=np.sqrt(delta*delta+4*A*B)
tm=.5*np.log(2*A/(delta+root));tp=.5*np.log((delta+root)/(2*B))
fig=plt.figure(figsize=(12,8))
fig.text(.5,.95,'The original Hessian coefficients and exact level-crossing times',ha='center',fontsize=17,fontweight='bold')
ax=fig.add_axes([.07,.35,.43,.49])
xx=np.linspace(0,1.3,1000)
for level,color,label in [(-delta,'#b56232',r'$f=c-\delta$'),(delta,'#26717c',r'$f=c+\delta$')]:
 mask=level+aa*xx*xx>=0;yy=np.sqrt(np.maximum(0,(level+aa*xx*xx)/bb))
 ax.plot(xx[mask],yy[mask],color=color,lw=2,label=label)
times=np.linspace(-.1,.8,500);ax.plot(x0*np.exp(-times),y0*np.exp(times),color='#192f47',lw=2.2)
for t,color,label in [(0,'#192f47','original point'),(tm,'#b56232',r'$\tau_-$'),(tp,'#26717c',r'$\tau_+$')]:
 qx=x0*np.exp(-t);qy=y0*np.exp(t);ax.scatter([qx],[qy],color=color,zorder=5,s=45);ax.annotate(label,(qx,qy),xytext=(8,-18 if t==tm else 9),textcoords='offset points',color=color)
ax.annotate('',xy=(x0*np.exp(-.49),y0*np.exp(.49)),xytext=(x0*np.exp(-.41),y0*np.exp(.41)),arrowprops=dict(arrowstyle='->',lw=1.8,color='#192f47'))
ax.set_xlim(0,1.25);ax.set_ylim(0,1.05);ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$y_1$',rotation=0,loc='top');ax.spines[['top','right']].set_visible(False);ax.legend(loc='upper left')
fig.text(.29,.245,r'$a_1=3,\quad b_1=5,\quad\delta=4/5,\quad(x_1,y_1)=(1,3/10)$',ha='center',fontsize=12)
fig.text(.29,.205,'A coordinate slice; every other coordinate is zero.',ha='center',fontsize=11)
fig.text(.755,.82,r'$A(u)=\int_0^1(1-t)D^2f(tu)\,dt$',ha='center',fontsize=18)
fig.text(.755,.72,r'$\dot M_s=-\frac{1}{2} A_s^{-1}(A(u)-A(0))M_s$',ha='center',fontsize=17)
fig.text(.755,.615,r'$M_1^{\mathsf{t}}A(u)M_1=H_0/2$',ha='center',fontsize=20)
fig.text(.755,.515,r'$f=c+\frac{1}{2}\sum_i\lambda_i\xi_i^2$',ha='center',fontsize=21)
fig.text(.755,.435,'All original eigenvalues and the factor 1/2 remain.',ha='center',fontsize=11.5)
fig.text(.755,.33,r'$\Phi_t(x,y)=(e^{-t}x,e^ty)$',ha='center',fontsize=19)
fig.text(.755,.265,r'$G_\xi=(Du)^{\mathsf{t}}G_u(Du)$',ha='center',fontsize=19)
fig.text(.755,.205,'The actual original metric is carried by its full derivative.',ha='center',fontsize=11)
fig.text(.5,.12,r'$e^{2\tau_-}=\frac{2A}{\delta+\sqrt{\delta^2+4AB}},\qquad e^{2\tau_+}=\frac{\delta+\sqrt{\delta^2+4AB}}{2B}$',ha='center',fontsize=21)
fig.text(.5,.054,'Equations (2.2)–(2.14), (3.2), (3.6)–(3.10). The lower formula needs A > 0; the upper needs B > 0.',ha='center',fontsize=11.5)
fig.savefig(O/'relative-morse-levels.svg',metadata={'Date':'2026-10-10'},bbox_inches='tight')
plt.close(fig)
