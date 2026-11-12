from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'CG-S6-PATH-FIBRE-20261009'})
fig,ax=plt.subplots(figsize=(12,8.5))
ax.set_xlim(0,12);ax.set_ylim(0,8.5);ax.axis('off')
ax.text(6,8.08,'Two adjacent degrees eliminate the first fibre class',ha='center',fontsize=18,fontweight='bold')
ax.text(6,7.47,r'$H_i(K)=0\ (0<i<n),\qquad n\geq2$',ha='center',fontsize=18)
def box(x,y,w,label):
 ax.add_patch(FancyBboxPatch((x-w/2,y-.43),w,.86,boxstyle='round,pad=.08',fc='#f2f7fa',ec='#26717c'))
 ax.text(x,y,label,ha='center',va='center',fontsize=19)
box(2.8,6.38,4.3,r'$E_{n+1}^{n+1,0}=H_{n+1}(B)$')
box(9.1,6.38,4.2,r'$E_{n+1}^{0,n}=H_n(K)$')
ax.add_patch(FancyArrowPatch((5.1,6.38),(6.86,6.38),arrowstyle='-|>',mutation_scale=17,lw=1.8,color='#26717c'))
ax.text(6,6.8,r'$d_{n+1}$',ha='center',fontsize=18)
ax.text(6,5.4,r'$\mathrm{im}\left(H_{n+1}(E)\to H_{n+1}(B)\right)=\ker d_{n+1}$',ha='center',fontsize=19)
ax.text(6,4.72,'Surjectivity in degree n + 1 forces this incoming map to be zero.',ha='center',fontsize=14)
ax.plot([.45,11.55],[4.17,4.17],color='#b4c5cb')
ax.text(6,3.55,r'$H_n(K)=E_\infty^{0,n}=F_0H_n(E)$',ha='center',fontsize=22)
ax.text(6,2.79,r'$F_0H_n(E)\ \subset\ F_{n-1}H_n(E)=\ker\left(H_n(E)\to H_n(B)\right)$',ha='center',fontsize=18)
ax.text(6,2.05,'Injectivity in degree n forces the surviving subgroup to be zero.',ha='center',fontsize=14)
ax.text(6,1.25,r'$H_n(K)=0\qquad\text{contradicts}\qquad \pi_n(K)\cong H_n(K)\ne0$',ha='center',fontsize=20)
ax.text(6,.43,'Theorem 5.1, equations (5.2)–(5.5). Integer homology; the incoming differential is retained.',ha='center',fontsize=12)
fig.savefig(O/'path-fibre-edges.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'path-fibre-edges.svg'))
