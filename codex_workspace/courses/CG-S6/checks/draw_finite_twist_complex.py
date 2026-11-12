from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-10-DUALITY-20261009'})
fig,ax=plt.subplots(figsize=(11,6.8));ax.set_xlim(0,11);ax.set_ylim(0,6.8);ax.axis('off')
ax.text(5.5,6.48,'The finite complex retains the actual twist family',ha='center',fontsize=16,fontweight='bold')
def box(x,y,w,h,label):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',fc='#f2f7fa',ec='#346781',lw=1.3))
 ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=14)
def arrow(a,b,label,offset=(0,0)):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.4,color='#247570'))
 ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',va='center',fontsize=12)
box(.8,4.9,2.8,.7,r'$\mathcal{H}^{q}$');box(7.4,4.9,2.8,.7,r'$\mathcal{H}^{q+1}$')
box(.8,2.9,2.8,.7,r'$\mathcal{A}^{0,q}(Y,V\otimes L(z))$');box(7.4,2.9,2.8,.7,r'$\mathcal{A}^{0,q+1}(Y,V\otimes L(z))$')
arrow((3.75,5.25),(7.25,5.25),r'$D(z)=p(1+\delta h)^{-1}\delta i$',(0,.42))
arrow((3.75,3.25),(7.25,3.25),r'$d_z=d_{z_0}+\delta(z-z_0)$',(0,-.44))
for x in [2.2,8.8]:
 arrow((x-.45,4.76),(x-.45,3.76),r"$i'=i-hTi$",(-.62,0))
 arrow((x+.45,3.76),(x+.45,4.76),r"$p'=p-pTh$",(.65,0))
ax.text(5.5,2.17,r'$\delta(z-z_0)=2\pi i\sum_j(z_j-z_{0j})b_j\wedge(-),\qquad T=(1+\delta h)^{-1}\delta$',ha='center',fontsize=13)
ax.text(5.5,1.55,r"$p'i'=1,\qquad i'p'=1-d_z h'-h'd_z,\qquad h'=h-hTh$",ha='center',fontsize=13)
ax.text(5.5,.92,'Both squares commute. The full maps and their domains are proved in (5.3)–(5.9).',ha='center',fontsize=11)
ax.text(5.5,.38,r'$2\pi\|h\|\sum_j|z_j-z_{0j}|\sup_Y|b_j|<1$'+'  makes the operator series converge.',ha='center',fontsize=11)
fig.savefig(O/'finite-twist-complex.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight');plt.close(fig)
print(str(O))
