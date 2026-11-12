from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'CG-S6-INTEGRAL-DUALITY-20261009'})
fig,ax=plt.subplots(figsize=(12,8))
ax.set_xlim(0,12);ax.set_ylim(0,8);ax.axis('off')
ax.text(6,7.65,'The covering degree remains in the integer pairing',ha='center',fontsize=18,fontweight='bold')
def box(x,y,label):
 ax.add_patch(FancyBboxPatch((x-2.2,y-.48),4.4,.96,boxstyle='round,pad=.08',fc='#f2f7fa',ec='#26717c'))
 ax.text(x,y,label,ha='center',va='center',fontsize=17)
box(2.55,6.5,r'$H^r(S;\mathbb{Z})$')
box(9.45,6.5,r'$L^r\subset H^r(F;\mathbb{Z})^G$')
ax.add_patch(FancyArrowPatch((4.88,6.5),(7.12,6.5),arrowstyle='-|>',mutation_scale=15,lw=1.6,color='#26717c'))
ax.text(6,6.88,r'$\pi^*$',ha='center',fontsize=18)
ax.text(6,5.23,r'$\langle\pi^*a\smile\pi^*b,[F]\rangle=m\langle a\smile b,[S]\rangle$',ha='center',fontsize=17)
ax.text(6,4.48,'The full integer dual tests every complementary descended class.',ha='center',fontsize=14)
ax.text(6,3.79,r'$x\in L^r\ \Longleftrightarrow\ x\in H^r(F;\mathbb{Z})^G,\quad \langle x\smile L^{n-r},[F]\rangle\subset m\mathbb{Z}$',ha='center',fontsize=16)
ax.plot([.5,11.5],[3.15,3.15],color='#b4c5cb')
ax.text(3.15,2.55,'Original order-three filling',ha='center',fontsize=15,fontweight='bold')
ax.text(8.85,2.55,'Original order-four filling',ha='center',fontsize=15,fontweight='bold')
ax.text(3.15,1.87,r'$L_1^3=\mathbb{Z}b\oplus\mathbb{Z}c_1$',ha='center',fontsize=19)
ax.text(8.85,1.87,r'$L_2^3=\mathbb{Z}(2b)\oplus\mathbb{Z}c_2$',ha='center',fontsize=19)
ax.text(3.15,1.22,r'$3s,\ -3r\ \in 3\mathbb{Z}$',ha='center',fontsize=16)
ax.text(8.85,1.22,r'$4s,\ -2r\ \in 4\mathbb{Z}\ \Longleftrightarrow\ r\in2\mathbb{Z}$',ha='center',fontsize=16)
ax.text(6,.45,'Equations (4.3)–(4.10).  The original b, c₁, c₂ and orientation are retained.',ha='center',fontsize=12)
fig.savefig(O/'integral-duality-lattices.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'integral-duality-lattices.svg'))
