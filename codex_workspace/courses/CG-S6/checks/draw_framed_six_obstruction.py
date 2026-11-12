"""Reproducible exact-map diagram for the framed six-dimensional calculation."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
W=Path(__file__).resolve().parents[1]/'assets'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'CG-S6-framed-six-obstruction','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,9),facecolor='#faf9f5')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,14);ax.set_ylim(0,9);ax.axis('off')
navy='#15354a';teal='#087e82';orange='#a75a22'
def text(x,y,s,size=12,**kw):ax.text(x,y,s,fontsize=size,color=navy,va='top',**kw)
def box(x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',linewidth=1,edgecolor='#b8c9cf',facecolor='white'))
def arrow(x,y,X,Y):ax.annotate('',xy=(X,Y),xytext=(x,y),arrowprops=dict(arrowstyle='->',color=teal,lw=2))
text(.45,8.65,'The original rank-three framing map and its geometric values',20,fontweight='bold')
text(.45,8.18,'Exact maps and evaluated embeddings • Sections 1–3 • schematic diagram',11)
box(.5,5.1,13,2.6)
text(.78,7.5,'The factor two comes from both quaternion factors',15,fontweight='bold')
text(1.15,6.91,r'$\pi_3SO(3)=\mathbb{Z}$',16)
text(5.45,6.91,r'$\pi_3SO(4)=\mathbb{Z}\oplus\mathbb{Z}$',16)
text(10.5,6.91,r'$\pi_3SO(5)=\mathbb{Z}$',16)
arrow(3.6,6.65,5.05,6.65);arrow(9.35,6.65,10.15,6.65)
text(1.75,6.2,r'$r$',18);text(6.35,6.2,r'$(r,r)$',18);text(11.55,6.2,r'$r+r=2r$',18,ha='center')
text(.9,5.65,r'$v\mapsto av\bar a$',14)
text(5.2,5.65,r'$\rho_4(a,b)v=av\bar b$',14)
text(9.8,5.65,'right-appended coordinate',12)
box(.5,.75,6.1,3.9);box(6.95,.75,6.55,3.9)
text(.78,4.42,'The actual handle-framing obstruction',15,fontweight='bold')
text(.85,3.88,r'$z_T=z-q\,\mathrm{Re}(\bar qz)$',15)
text(.85,3.39,r'$A_{f,\phi}(q)(z,w,u)$',15)
text(1.08,2.98,r'$=(\tau(df(z_T)+\phi(w),u),-\mathrm{Re}(\bar qz))$',13)
text(.85,2.43,'The final minus sign is the attaching collar.',11)
text(.85,1.97,r'$\phi\mapsto\phi h:\quad k\mapsto k+2[h]$',15)
text(.85,1.42,r'$\varepsilon_\tau(f)=k\ \mathrm{mod}\ 2$',15)
text(.85,.99,'Value zero ⇔ an extending framed surgery exists.',11)
text(7.24,4.42,'Calculated values for the specified embeddings',15,fontweight='bold')
text(7.28,3.84,'Embedding',12,fontweight='bold');text(11.38,3.84,'integer k',12,fontweight='bold');text(12.6,3.84,'parity',12,fontweight='bold')
rows=[('Local coordinate sphere','0','0'),(r'$A:q\mapsto(q,1)$','−1','1'),(r'$B:q\mapsto(1,q)$','−1','1'),(r'$\mathrm{graph}(g):q\mapsto(q,g(q))$','−1','1')]
for j,(s,k,e) in enumerate(rows):
    y=3.39-j*.49;text(7.28,y,s,13);text(11.7,y,k,13,ha='center');text(12.9,y,e,13,ha='center')
text(7.28,1.32,r'$A\cdot B=+1,\qquad B\cdot A=-1$',13)
text(7.28,.94,'General homology invariance is not inferred from these examples.',10)
text(.52,.4,'Proof locators: (1.4)–(1.15), (2.3)–(2.9), (3.2)–(3.18). Original coordinate order and collar sign retained.',10)
fig.savefig(W/'framed-six-obstruction.svg',metadata={'Date':None})
plt.close(fig)
print('Rendered framed-six-obstruction.svg.')
