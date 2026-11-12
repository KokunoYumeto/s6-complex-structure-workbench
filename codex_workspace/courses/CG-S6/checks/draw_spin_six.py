from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'CG-S6-SPIN6-20261009'})
fig,ax=plt.subplots(figsize=(12,7));ax.set_xlim(0,12);ax.set_ylim(0,7);ax.axis('off')
ax.text(6,6.65,'Keep the tangent bundle; add the specified real line',ha='center',fontsize=18,fontweight='bold')
xs=[1.6,6,10.4]
for x,t in zip(xs,[r'$SU(4)$',r'$SO(6)$',r'$SO(7)$']):ax.text(x,5.8,t,ha='center',fontsize=19)
def arrow(a,b,label,dy=.22):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',lw=1.4,mutation_scale=14,color='#246e79'))
 ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha='center',fontsize=12)
arrow((2.4,5.92),(5.2,5.92),r'$V=(\Lambda^2E)^\tau$')
arrow((6.8,5.92),(9.6,5.92),'add one real coordinate')
for x,t in zip(xs,[r'$\pi_5=\mathbb{Z}$',r'$\pi_5=\mathbb{Z}$',r'$\pi_5=0$']):ax.text(x,4.58,t,ha='center',fontsize=18)
arrow((2.4,4.72),(5.2,4.72),r'$\rho_*$'+' is an isomorphism')
arrow((6.8,4.72),(9.6,4.72),'tangent generator maps to zero')
for x in xs:
 ax.plot([x,x],[5.55,5.03],linestyle=':',color='#246e79',lw=1.4)
 ax.text(x+.13,5.24,r'$\pi_5(-)$',ha='left',fontsize=10)
ax.text(6,4.03,'Positive tangent clutching class:',ha='center',fontsize=11)
ax.text(6,3.68,r'$\langle c_3(E),[S^6]\rangle=\langle e(V),[S^6]\rangle=2$',ha='center',fontsize=17)
ax.plot([.4,11.6],[3.16,3.16],color='#c2d3d9',lw=1)
ax.text(2.8,2.52,r'$g^*T\Sigma$',ha='center',fontsize=20)
ax.text(9.2,2.52,r'$TS^6$',ha='center',fontsize=20)
arrow((4.2,2.65),(7.8,2.65),r'$B$'+' : oriented bundle isomorphism')
ax.text(6,1.7,r'$(p;v,a)\longmapsto(p;B_pv+ap)$',ha='center',fontsize=19)
ax.text(6,1.0,r'$g^*T\Sigma\oplus\mathbf{1}_{\mathbb{R}}\ \simeq\ S^6\times\mathbb{R}^7$',ha='center',fontsize=19)
ax.text(6,.35,'Exact maps: (3.4), (4.7), (5.2)–(5.4), and (6.3)–(6.4).',ha='center',fontsize=11)
fig.savefig(O/'spin-six-framing.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'spin-six-framing.svg'))
