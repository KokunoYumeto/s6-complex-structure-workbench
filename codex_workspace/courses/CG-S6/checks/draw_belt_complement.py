from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'CG-S6-BELT-COMPLEMENT-20261009'})
fig,ax=plt.subplots(figsize=(12,9))
ax.set_xlim(0,12);ax.set_ylim(0,9);ax.axis('off')
ax.text(6,8.55,'The exact complement comparison through the original framing',ha='center',fontsize=17,fontweight='bold')
for x,label in [(2.8,'Outgoing boundary'),(9.2,'Original boundary')]:
 ax.add_patch(FancyBboxPatch((x-2.15,6.75),4.3,1.13,boxstyle='round,pad=.06',fc='#f2f7fa',ec='#26717c'))
 ax.text(x,7.54,label,ha='center',fontsize=15)
ax.text(2.8,7.12,r'$N^\prime\setminus\bigcup_j B_j$',ha='center',va='center',fontsize=19)
ax.text(9.2,7.12,r'$N\setminus\bigcup_j L_j$',ha='center',va='center',fontsize=19)
ax.add_patch(FancyArrowPatch((5.1,7.34),(6.91,7.34),arrowstyle='<->',mutation_scale=17,lw=1.8,color='#26717c'))
ax.text(6,7.72,r'$\Phi,\ \Psi$',ha='center',fontsize=18)
ax.text(6,6.08,r'$\Phi(x,y)=\varphi\left(\frac{a}{\|x\|}x,\frac{f(\|x\|)}{b}y\right)$',ha='center',fontsize=22)
ax.text(6,5.18,r'$\Psi(\varphi(\theta,z))=\left(\frac{f^{-1}(\|z\|)}{a}\theta,\frac{b}{\|z\|}z\right)$',ha='center',fontsize=21)
ax.text(6,4.61,'Both maps are the identity on the same tube exterior A.',ha='center',fontsize=15)
ax.plot([.45,11.55],[4.22,4.22],color='#b4c5cb')
ax.text(6,3.74,'The collar correction retains both radii',ha='center',fontsize=17,fontweight='bold')
ax.text(6,3.1,r'$f(0)=0,\quad f(a)=b,\quad f(r)=r+b-a\quad\mathrm{near}\ a$',ha='center',fontsize=20)
ax.text(6,2.51,r'$\|z\|-b=f(\|x\|)-b=\|x\|-a$',ha='center',fontsize=20)
ax.text(6,1.76,'For index-two handles in dimension six: normal dimension q = 4',ha='center',fontsize=15)
ax.text(6,1.12,r'$\pi_i\left(N^\prime\setminus\bigcup_jB_j\right)\cong\pi_i(N)\quad(i=1,2)$',ha='center',fontsize=20)
ax.text(6,.39,'Equations (1.11)–(1.14), (2.4)–(2.9), (3.4)–(3.5). The supported ambient move is a further construction.',ha='center',fontsize=11.8)
fig.savefig(O/'belt-complement-map.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')

plt.close(fig)
print(str(O/'belt-complement-map.svg'))
