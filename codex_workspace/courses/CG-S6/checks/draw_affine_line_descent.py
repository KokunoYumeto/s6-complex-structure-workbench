from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'CG-S6-AFFINE-DESCENT-20261009'})
fig,ax=plt.subplots(figsize=(12,8));ax.set_xlim(0,12);ax.set_ylim(0,8);ax.axis('off')
ax.text(6,7.68,'The affine lift must satisfy the entire power relation',ha='center',fontsize=18,fontweight='bold')
def box(x,y,label):
 ax.add_patch(FancyBboxPatch((x-1.2,y-.35),2.4,.7,boxstyle='round,pad=.07',fc='#f2f7fa',ec='#26717c'))
 ax.text(x,y,label,ha='center',va='center',fontsize=18)
def arrow(a,b,label,offset=(0,.24)):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.4,color='#26717c'))
 ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',fontsize=12)
for x in [2.25,9.75]:
 box(x,6.65,r'$\mathbb{R}^4\times\mathbb{C}$');box(x,4.68,r'$L_{C_j}\longrightarrow F$')
 arrow((x,6.21),(x,5.12),'lattice quotient',(.78,0))
arrow((3.57,6.65),(8.43,6.65),r'$G_{j,\ell_j,\beta_j}$'+' from (2.6)')
arrow((3.57,4.68),(8.43,4.68),r'$\overline{G}_{j,\ell_j,\beta_j}$')
ax.text(6,5.65,r'$G^{m_j}=T_{v_j}$',ha='center',fontsize=17)
box(6,2.65,r'$L\longrightarrow S_j$')
arrow((2.5,4.23),(4.67,2.97),'finite quotient',(-.38,0))
arrow((9.5,4.23),(7.33,2.97),'finite quotient',(.38,0))
ax.text(6,1.75,r'$\pi_j^*L\simeq L_{C_j},\qquad c_1(\pi_j^*L)=a h_j+bq$',ha='center',fontsize=16)
ax.text(6,1.06,r'$j=2:\quad 2\ell_3=-(a+3b),\qquad a\equiv b\;(\mathrm{mod}\,2)$',ha='center',fontsize=15)
ax.text(6,.45,r'$\beta_1=8b/9,\qquad\beta_2=27b/32$'+'  cancel the retained constant defects (3.6).',ha='center',fontsize=12)
fig.savefig(O/'affine-line-descent.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'affine-line-descent.svg'))
