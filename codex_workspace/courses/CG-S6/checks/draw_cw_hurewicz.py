from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'CG-S6-CW-HUREWICZ-20261009'})
fig,ax=plt.subplots(figsize=(12,8))
ax.set_xlim(0,12);ax.set_ylim(0,8);ax.axis('off')
ax.text(6,7.65,'Actual maps from the original manifold to a CW model',ha='center',fontsize=18,fontweight='bold')
def box(x,y,label):
 ax.add_patch(FancyBboxPatch((x-.8,y-.45),1.6,.9,boxstyle='round,pad=.08',fc='#f2f7fa',ec='#26717c'))
 ax.text(x,y,label,ha='center',va='center',fontsize=23)
def arrow(a,b,label,dy):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.5,color='#26717c'))
 ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha='center',fontsize=15)
for x,label in [(1.5,r'$T$'),(6,r'$U$'),(10.5,r'$M$')]:box(x,6.35,label)
arrow((2.42,6.5),(5.05,6.5),r'$q(x,t)=x$',.3)
arrow((5.05,6.18),(2.42,6.18),r'$s(x)=(x,\rho(x))$',-.48)
arrow((6.95,6.5),(9.58,6.5),r'$r$',.3)
arrow((9.58,6.18),(6.95,6.18),r'$\iota$',-.48)
ax.text(6,4.76,r'$\alpha=rq,\quad\beta=s\iota,\quad\alpha\beta=1_M,\quad\beta\alpha\simeq1_T$',ha='center',fontsize=18)
ax.text(6,4.05,r'$H_\tau(x,t)=(x,(1-\tau)t+\tau\rho(x))$',ha='center',fontsize=18)
ax.text(6,3.47,'The height stays above the first cubical stage containing the same point x.',ha='center',fontsize=13)
ax.plot([.5,11.5],[2.93,2.93],color='#b4c5cb')
ax.text(6,2.38,'The first Hurewicz map chooses the original sphere class',ha='center',fontsize=16,fontweight='bold')
ax.text(6,1.63,r'$h:\pi_6(X)\longrightarrow H_6(X;\mathbb{Z}),\qquad[g]\longmapsto g_*[S^6]$',ha='center',fontsize=18)
ax.text(6,.94,r'$[g]=h^{-1}([X]),\qquad g_*[S^6]=[X]$',ha='center',fontsize=19)
ax.text(6,.33,'Equations (1.6)–(1.7), (2.3)–(2.4), and (5.1).  Smooth recognition is a later step.',ha='center',fontsize=12)
fig.savefig(O/'cw-hurewicz-maps.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'cw-hurewicz-maps.svg'))
