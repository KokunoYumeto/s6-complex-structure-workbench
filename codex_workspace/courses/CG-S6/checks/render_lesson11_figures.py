from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','svg.hashsalt':'CG-S6-11-20261009','axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(10,5.2),layout='constrained')
gs=fig.add_gridspec(1,2,width_ratios=[1.5,1])
ax=fig.add_subplot(gs[0,0]);info=fig.add_subplot(gs[0,1]);info.axis('off')
t=np.linspace(-np.pi,np.pi,801)
ax.plot(t,4*np.abs(np.sin(t)),color='#137c79',lw=2.7,label=r'$|N_J(U,V_\theta)|=4|\sin\theta|$')
ax.plot(t,2*np.abs(np.sin(t)),color='#a55220',lw=2,ls='--',label=r'$|[p,U,V_\theta]|=2|\sin\theta|$')
ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['−π','−π/2','0','π/2','π'])
ax.set_yticks([0,1,2,3,4]);ax.set_ylim(-.12,4.3);ax.set_xlim(-np.pi,np.pi)
ax.grid(alpha=.2);ax.set_xlabel('θ (radians)');ax.set_ylabel('Euclidean norm');ax.legend(loc='upper center',bbox_to_anchor=(.5,-.17),fontsize=10,frameon=False)
fig.suptitle('The exact obstruction along a specified circle of tangent vectors',fontsize=14,fontweight='bold')
lines=[r'$p=e_7,\quad U=e_1,\quad JU=-e_6$',r'$V_\theta=\cos\theta\,(-e_6)+\sin\theta\,e_2$',r'$N_J(U,V_\theta)=-4\sin\theta\,e_4$',r'$[p,U,V_\theta]=-2\sin\theta\,e_4$','',r'$\ker N_J(U,\cdot)=\mathrm{span}_{\mathbb{R}}(e_1,e_6)$','The zero values at θ = 0, ±π lie','in that complex line.','',r'$\operatorname{im}N_J(U,\cdot)=\{e_1,e_6\}^{\perp}\cap T_pS^6$','The image has real dimension four.']
y=.94
for s in lines:
 info.text(0,y,s,transform=info.transAxes,fontsize=10.5,va='top');y-=.082
fig.savefig(O/'octonion-obstruction-circle.svg',metadata={'Date':'2026-10-09'});plt.close(fig)
fig,ax=plt.subplots(figsize=(10,6.2));ax.set_xlim(0,10);ax.set_ylim(0,6.2);ax.axis('off')
ax.text(5,5.95,'How the proved local coordinates return to the original field',ha='center',fontsize=14,fontweight='bold')
def box(x,y,w,h,title,body):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',fc='#f2f7fa',ec='#346781',lw=1.2))
 ax.text(x+w/2,y+h-.21,title,ha='center',va='top',fontsize=10,fontweight='bold')
 ax.text(x+w/2,y+h-.57,body,ha='center',va='top',fontsize=10,linespacing=1.35)
def arrow(a,b,label=''):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,lw=1.3,color='#356f70'))
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.15,label,ha='center',fontsize=9)
box(.25,3.65,2.7,1.55,'Original real chart',r'$y,\quad J_y$'+'\n'+r'$z=C(y-y_p),\quad J_z=CJ_yC^{-1}$')
box(3.7,3.65,2.65,1.55,'Exact rescaling',r'$x=z/\epsilon$'+'\n'+r'$\widetilde A_\epsilon(x)=\chi(x)A(\epsilon x)$'+'\n'+r'$\chi=1\ \mathrm{on}\ |x|\leq1$')
box(7.08,3.65,2.65,1.55,'Periodic coordinates',r'$\zeta=H(x)=x+h(x)$'+'\n'+r'$\sum_j\partial_{\zeta_j}B_j=0$'+'\n'+r'$D_h\mathcal{F}(0,0)=-\Delta/4$')
arrow((3.05,4.42),(3.59,4.42));arrow((6.45,4.42),(6.98,4.42))
box(7.08,1.2,2.65,1.65,'Analytic flows',r'$a=G(\zeta-H(0))$'+'\n'+r'$\bar\partial G=\widehat B\partial G$'+'\n'+r'$\widehat B(w)=B(w+H(0))$')
box(.25,1.2,6.1,1.65,'Return every coordinate and scale',r'$F_y(y)=\epsilon\,G\!\left(H\!\left(C(y-y_p)/\epsilon\right)-H(0)\right)$'+'\n'+r'$dF_y\circ J_y=i\,dF_y,\qquad \det_{\mathbb{R}}dF_y\ne0$')
arrow((8.4,3.55),(8.4,2.95));arrow((6.98,2.02),(6.45,2.02))
ax.text(5,.58,'Local construction: restrict to the original ball where χ = 1 and all inverse maps exist.',ha='center',fontsize=11)
ax.text(5,.2,'Exact formulas and convergence proof: Sections 6–9. The torus is an auxiliary domain for solving the gauge equation.',ha='center',fontsize=10)
fig.savefig(O/'integrability-coordinate-maps.svg',bbox_inches='tight',metadata={'Date':'2026-10-09'});plt.close(fig)
print(str(O))
