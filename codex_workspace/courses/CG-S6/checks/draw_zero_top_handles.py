from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-ZERO-TOP-20261010','font.size':12})
fig=plt.figure(figsize=(14,8.5))
fig.text(.5,.955,'Use the actual trajectory graph to remove the extreme indices',ha='center',fontsize=18,fontweight='bold')
ax=fig.add_axes([.06,.46,.49,.36]);ax.set_xlim(-.5,4.5);ax.set_ylim(-.7,2.1);ax.axis('off')
for x,txt in [(0,r'$*:\ M_-$'),(2,r'$q_1$'),(4,r'$q_2$')]:
 ax.scatter([x],[.8],s=260,color='#edf3f2',edgecolor='#173c4e',lw=1.6,zorder=4)
 ax.text(x,.43,txt,ha='center',fontsize=14)
def arrow(p,q,col,rad=0):
 ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=15,lw=2.2,color=col,connectionstyle='arc3,rad='+str(rad),shrinkA=11,shrinkB=11,zorder=2))
arrow((0,.8),(2,.8),'#176c7b');arrow((2,.8),(4,.8),'#777777')
arrow((4,.8),(0,.8),'#bd6634',.5)
arrow((1.90,.82),(2.10,.82),'#923e79',-3.3)
ax.text(1,1.03,r'$e_1$',ha='center',color='#176c7b',fontsize=15)
ax.text(3,1.03,r'$e_2$',ha='center',color='#777777',fontsize=15)
ax.text(1,1.83,r'$e_3$',ha='center',color='#bd6634',fontsize=15)
ax.text(2.35,1.30,r'$e_4$',ha='center',color='#923e79',fontsize=15)
ax.set_title('The original signed graph in Exercise 6.1',pad=12,fontweight='bold')
fig.text(.305,.385,'An edge from the incoming component to a minimum\nhas exactly the required single connecting trajectory.',ha='center',fontsize=12)
ax2=fig.add_axes([.60,.46,.35,.36]);ax2.axis('off')
ax2.set_title('Retain the full reversed function and index',pad=12,fontweight='bold')
ax2.text(.5,.82,r'$g=-f,\qquad Z^g=-Z$',ha='center',fontsize=18)
ax2.text(.5,.61,r'$k\longmapsto n-k,\qquad \det P=(-1)^{k(n-k)}$',ha='center',fontsize=16)
ax2.text(.5,.36,r'$n=6:\quad (0,1)\quad\hbox{and}\quad(6,5)$'.replace(r'\hbox{and}',r'\mathrm{and}'),ha='center',fontsize=16)
ax2.text(.5,.15,r'$n=7:\quad (0,1)\quad\mathrm{and}\quad(7,6)$',ha='center',fontsize=16)
fig.text(.77,.385,'The original collar endpoints and all Hessian\ncoefficients occur in equations (4.2)–(4.6).',ha='center',fontsize=12)
fig.text(.34,.285,r'$P_{j-1}$',ha='center',fontsize=23)
fig.text(.50,.285,r'$C$',ha='center',fontsize=23)
fig.text(.66,.285,r'$P_j$',ha='center',fontsize=23)
fig.text(.42,.325,r'$G_{j-1}$',ha='center',fontsize=15)
fig.text(.58,.325,r'$G_j$',ha='center',fontsize=15)
axd=fig.add_axes([0,0,1,1]);axd.axis('off')
for start,end in [(.37,.485),(.64,.515)]:
 axd.annotate('',xy=(end,.30),xytext=(start,.30),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',lw=1.5,color='#173c4e'))
fig.text(.5,.205,r'$\Psi_j=G_j^{-1}G_{j-1},\qquad D(\Psi_j\alpha)=D\Psi_j|_{\alpha}\,D\alpha$',ha='center',fontsize=20)
fig.text(.5,.135,'The whole thick attaching map and its normal frame travel through the actual cobordism comparison.',ha='center',fontsize=12)
fig.text(.5,.075,'Graph: equations (6.1)–(6.2), with loops retained. Cancellation: Section 3. Reversal: Section 4. Full presentation maps: Section 5.',ha='center',fontsize=11)
fig.text(.5,.035,'The graph records trajectory incidence; it is not a metric drawing of the original cobordism.',ha='center',fontsize=11)
fig.savefig(O/'zero-top-trajectory-graph.svg',metadata={'Date':'2026-10-10'},bbox_inches='tight')

plt.close(fig)

