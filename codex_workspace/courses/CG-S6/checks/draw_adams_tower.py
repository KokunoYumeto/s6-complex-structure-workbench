"""Render the original indexed Adams fibre and cofibres sequences. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1]/'assets'
plt.rcParams.update({'svg.hashsalt':'CG-S6-original-adams-tower','font.family':'DejaVu Sans','font.size':13})
fig,ax=plt.subplots(figsize=(14,6.7));fig.patch.set_facecolor('white');ax.set(xlim=(0,14),ylim=(0,6.7));ax.axis('off')
ax.text(7,6.35,'Every stage of the original Adams tower',ha='center',weight='bold',fontsize=20,color='#18323d')
ax.text(7,5.82,r'$B=\mathrm{fib}(\mathbb{S}\longrightarrow H),\quad F_s=B^{\wedge s},\quad W_s=H\wedge B^{\wedge s}$',ha='center',fontsize=16)
xs=[1.3,5,8.7,12.3]
def arrow(a,b,y,label):
 ax.annotate('',xy=(b-.65,y),xytext=(a+.65,y),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#1b7581'})
 ax.text((a+b)/2,y+.23,label,ha='center',fontsize=12,color='#1b7581')
for x,label in zip(xs,[r'$F_{s+1}$',r'$F_s$',r'$W_s$',r'$\Sigma F_{s+1}$']):ax.text(x,4.66,label,ha='center',va='center',fontsize=20)
for a,b,label in zip(xs,xs[1:],[r'$a_s=\alpha\wedge1$',r'$\eta\wedge1$',r'$\partial\wedge1$']):arrow(a,b,4.66,label)
ax.text(7,3.88,r'$q_s=\alpha^{\wedge s},\qquad C_s=\mathrm{cofib}(q_{s+1}),\qquad C_{-1}=0,\quad C_0=H$',ha='center',fontsize=16)
for x,label in zip(xs,[r'$W_s$',r'$C_s$',r'$C_{s-1}$',r'$\Sigma W_s$']):ax.text(x,2.99,label,ha='center',va='center',fontsize=20)
for a,b,label in zip(xs,xs[1:],[r'$i_s$',r'$r_s$',r'$\delta_s$']):arrow(a,b,2.99,label)
ax.text(7,2.23,'The fibre is Wₛ. The cofibre is ΣWₛ. The connecting map has degree minus one on homotopy groups.',ha='center',fontsize=12)
ax.text(7,1.43,r'$\pi_{n+1}C_{s-1}\ \longrightarrow\ \pi_nW_s\ \longrightarrow\ \pi_nC_s\ \longrightarrow\ \pi_nC_{s-1}\ \longrightarrow\ \pi_{n-1}W_s$',ha='center',fontsize=16)
ax.text(7,.67,'Proof: The Adams tower and exact inverse limits, Section 1, equations (1.1)–(1.5).',ha='center',fontsize=11)
ax.text(7,.30,'Human-source context: Dugger–Isaksen, arXiv:0901.1632v1, original TeX 2218–2245. This diagram makes no convergence assertion.',ha='center',fontsize=10)
fig.tight_layout(pad=.6)
fig.savefig(W/'original-adams-tower.svg',metadata={'Date':None})
plt.close(fig)
print('Rendered exact original tower sequences.')
