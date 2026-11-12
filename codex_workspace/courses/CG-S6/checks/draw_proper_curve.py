from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-GRAPH-20261009'})
fig,ax=plt.subplots(figsize=(12,7.1));ax.set_xlim(0,12);ax.set_ylim(0,7.1);ax.axis('off')
ax.text(6,6.8,'The graph complex preserves the full singular fibre',ha='center',fontsize=17,fontweight='bold')
def box(x,y,label,note):
 ax.add_patch(FancyBboxPatch((x,y),2.9,.88,boxstyle='round,pad=.08',fc='#f2f7fa',ec='#346781',lw=1.3))
 ax.text(x+1.45,y+.61,label,ha='center',va='center',fontsize=14)
 ax.text(x+1.45,y+.23,note,ha='center',va='center',fontsize=9.8)
def arrow(a,b,label,dx=0,dy=0,style='-'):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.35,color='#247570',linestyle=style))
 ax.text((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy,label,ha='center',va='center',fontsize=11)
xs=[.3,4.55,8.8]
box(xs[0],4.95,r'$(\mathcal{K}^{\bullet},D)$','finite free over the base')
box(xs[1],4.95,r'$(\mathcal{B}^{\bullet},b_t)$','holomorphic parameter sections')
box(xs[2],4.95,r'$Rf_*E$','the actual direct image')
box(xs[0],2.45,r'$\mathcal{K}^{\bullet}\otimes\mathbb{C}(t)$','evaluate its finite matrices')
box(xs[1],2.45,r'$(\mathcal{B}^{\bullet},b_t)|_t$','the evaluated Cartier cone')
box(xs[2],2.45,r'$R\Gamma(X_t,E|_{X_t})$','cohomology of the full fibre')
for y in [5.39,2.89]:
 arrow((3.31,y),(4.43,y),r'$i_t$',dy=.31)
 arrow((7.56,y),(8.68,y),r'$\simeq$',dy=.29)
for x in [1.75,6.0]:arrow((x,4.79),(x,3.49),'evaluate',dx=.43)
arrow((10.25,4.79),(10.25,3.49),'canonical\ncomparison',dx=.66,style='--')
ax.text(6,1.77,r'$b_t(u,v)=(\bar\partial_Eu+\widetilde m_tv,\,-\bar\partial_{F,t}v)$',ha='center',fontsize=14)
ax.text(6,1.14,r'$\widetilde m_t$'+' keeps the full graph equation and its bundle comparison factor.',ha='center',fontsize=12)
ax.text(6,.52,r'$s^3-\tau,\qquad s^4-\tau,\qquad xy-\tau,\qquad xyz-\tau$',ha='center',fontsize=16)
fig.savefig(O/'graph-base-change.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'graph-base-change.svg'))
