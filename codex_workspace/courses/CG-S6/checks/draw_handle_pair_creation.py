from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-HANDLE-PAIR-20261010','font.size':12})
def delta(u):
 v=np.zeros_like(np.asarray(u,dtype=float));mask=np.abs(u)<1
 v[mask]=4*np.exp(-1/(1-np.asarray(u)[mask]**2));return v
def g(u):return 8*u/(1-u*u)**2*np.exp(-1/(1-u*u))
ustar=3**(-.25);umax=brentq(lambda u:g(u)-1,.0001,ustar);umin=brentq(lambda u:g(u)-1,ustar,.999)
sstar=1/g(ustar)
fig=plt.figure(figsize=(14,9))
fig.text(.5,.955,'Insert the pair through the exact original height product',ha='center',fontsize=18,fontweight='bold')
ax=fig.add_axes([.075,.48,.39,.36])
u=np.linspace(-1.1,1.1,1600)
for s,col,label in [(0,'#879399',r'$s=0$'),(sstar,'#a46f2b',r'$s=s_*$'),(1,'#176c7b',r'$s=1$')]:
 ax.plot(u,u+s*delta(u),color=col,label=label,lw=2)
ax.scatter([umax,umin],[umax+delta(np.array([umax]))[0],umin+delta(np.array([umin]))[0]],color='#933b67',zorder=5)
ax.annotate(r'$p:\ k+1$',(umax,umax+delta(np.array([umax]))[0]),xytext=(-.82,1.35),arrowprops=dict(arrowstyle='->',color='#933b67'),color='#933b67')
ax.annotate(r'$q:\ k$',(umin,umin+delta(np.array([umin]))[0]),xytext=(.1,.63),arrowprops=dict(arrowstyle='->',color='#933b67'),color='#933b67')
ax.set_xlabel(r'$u$');ax.set_ylabel(r'$F_s(u,0,0)=u+s\delta(u)$')
ax.set_title('One supported birth: equations (3.7)–(3.8)',fontsize=12,fontweight='bold');ax.legend(loc='lower right');ax.grid(alpha=.2)
ax2=fig.add_axes([.565,.48,.375,.36])
theta=np.linspace(0,2*np.pi,400);r1=np.sqrt((umin+2)/2);r2=np.sqrt((umin+2)/7)
x=r1*np.cos(theta);y=r2*np.sin(theta)
ax2.fill(x,y,color='#dcebed');ax2.plot(x,y,color='#176c7b',lw=2)
for t in [.4,2,3.7,5.2]:
 p=np.array([r1*np.cos(t),r2*np.sin(t)]);v=.32*p
 ax2.annotate('',p+v,p,arrowprops=dict(arrowstyle='->',lw=1.5,color='#933b67'))
ax2.text(0,0,r'$D_{\rm in}$'+'\n'+r'$2y_{0,1}^2+7y_{0,2}^2\leq u_m+2$',ha='center',va='center',fontsize=12)
ax2.set_xlim(-1.65,1.65);ax2.set_ylim(-1.05,1.05);ax2.set_aspect('equal')
ax2.set_xlabel(r'$y_{0,1}$');ax2.set_ylabel(r'$y_{0,2}$');ax2.grid(alpha=.2)
ax2.set_title('Actual attaching ellipse in the level t = −2',fontsize=12,fontweight='bold')
fig.text(.755,.375,'Outward frame direction shown; the three constant z directions\nare perpendicular to this coordinate slice. Equation (6.7).',ha='center',fontsize=11)
fig.text(.26,.40,r'$u_*=3^{-1/4},\quad s_*=1/g(u_*)$',ha='center',fontsize=14)
fig.text(.18,.28,r'$(q_0,t)$',ha='center',fontsize=20)
fig.text(.48,.28,r'$(u,y,z)$',ha='center',fontsize=20)
fig.text(.81,.28,r'$C$',ha='center',fontsize=20)
ax3=fig.add_axes([0,0,1,1],frameon=False);ax3.set_axis_off()
ax3.annotate('',(.405,.29),(.245,.29),arrowprops=dict(arrowstyle='->',lw=1.6,color='#173c4e'))
ax3.annotate('',(.775,.29),(.565,.29),arrowprops=dict(arrowstyle='->',lw=1.6,color='#173c4e'))
fig.text(.325,.32,r'$H$',ha='center',fontsize=16)
fig.text(.67,.32,r'$E=\Gamma L_0H^{-1}$',ha='center',fontsize=15)
fig.text(.5,.205,r'$F_cH=t,\qquad \mathcal{B}=F_bH,\qquad f_{\rm new}E=t_0+\lambda F_b$',ha='center',fontsize=17)
fig.text(.5,.135,'The full maps, inverse, derivatives, metric and support are proved in Sections 2–5.\nThe compact set (4.5) keeps every upper unstable trajectory down to the retained lower level.',ha='center',fontsize=12)
fig.text(.5,.065,'Numerical samples illustrate the exact formulas. No metric identification is asserted.\nCutoff mechanism: Laudenbach, arXiv:1307.2545v1; complete receiving proof and disk frame: this chapter.',ha='center',fontsize=10)
fig.savefig(O/'original-handle-pair.svg',metadata={'Date':None})

print(str(O/'original-handle-pair.svg'))

