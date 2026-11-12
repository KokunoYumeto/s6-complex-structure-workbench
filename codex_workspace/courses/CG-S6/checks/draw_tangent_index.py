from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-INDEX-20261009'})
fig,ax=plt.subplots(figsize=(11,6.5));ax.set_xlim(0,11);ax.set_ylim(0,6.5);ax.axis('off')
ax.text(5.5,6.17,'A higher transferred differential changes the cohomology',ha='center',fontsize=16,fontweight='bold')
ax.text(5.5,5.59,r'$D=P\partial I-P\partial h\partial I\qquad$'+'(higher terms vanish in these bidegrees)',ha='center',fontsize=13)
def box(x,y,label,degree,color):
 ax.add_patch(FancyBboxPatch((x,y),2.1,.85,boxstyle='round,pad=.06',fc=color,ec='#346781',lw=1.3))
 ax.text(x+1.05,y+.60,label,ha='center',va='center',fontsize=16)
 ax.text(x+1.05,y+.22,degree,ha='center',va='center',fontsize=11)
def arrow(a,b,label,off=(0,0),color='#247570'):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.5,color=color))
 ax.text((a[0]+b[0])/2+off[0],(a[1]+b[1])/2+off[1],label,ha='center',va='center',fontsize=14)
box(.65,3.85,r'$a$','bidegree (0,1)','#fff2d8')
box(4.45,3.85,r'$v$','bidegree (1,1)','#f2f7fa')
box(4.45,1.75,r'$u$','bidegree (1,0)','#f2f7fa')
box(8.25,1.75,r'$w$','bidegree (2,0)','#fff2d8')
arrow((2.88,4.275),(4.32,4.275),r'$\partial$',(0,.32))
arrow((5.18,3.72),(5.18,2.75),r'$h$',(-.28,0))
arrow((5.83,2.75),(5.83,3.72),r'$\bar\partial$',(.32,0))
arrow((6.68,2.175),(8.12,2.175),r'$\partial$',(0,.32))
ax.text(1.7,2.6,'The retained\nharmonic classes\nare a and w.',ha='center',fontsize=12)
ax.text(5.5,1.07,r'$P\partial I(a)=0,\qquad -P\partial h\partial I(a)=-w$',ha='center',fontsize=15)
ax.text(5.5,.47,'The complete map sends a to minus w and has zero cohomology.',ha='center',fontsize=12)
fig.savefig(O/'higher-transfer-term.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'higher-transfer-term.svg'))
