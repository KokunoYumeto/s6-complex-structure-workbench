"""The actual cocycle bundle and its homology support, with exact indices. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
W=Path(__file__).resolve().parents[1]/'assets'
plt.rcParams.update({'svg.hashsalt':'CG-S6-finite-cocycle-tower','font.family':'DejaVu Sans','font.size':12})
fig=plt.figure(figsize=(14,9.2),facecolor='white')
head=fig.add_axes([.035,.70,.93,.27]);head.set(xlim=(0,14),ylim=(0,3));head.axis('off')
head.text(7,2.70,'Finite cocycles give the actual Adams-stage finiteness',ha='center',fontsize=20,weight='bold',color='#18323d')
head.text(7,2.15,r'$K^n_q=Z^n(\Delta^q;\mathbb{F}_p),\quad U^n_q=C^n(\Delta^q;\mathbb{F}_p),\quad |K^n_q|=p^{\binom{q}{n}}\ (n\geq1)$',ha='center',fontsize=15)
for x,label in [(2.1,r'$L_n=|K^n|$'),(7,r'$E_n=|U^n|$'),(11.9,r'$L_{n+1}=|K^{n+1}|$')]:head.text(x,1.25,label,ha='center',fontsize=19)
for a,b,label in [(3.4,5.8,r'$|j_n|$'),(8.2,10.6,r'$p_n=|\delta|$')]:
 head.annotate('',xy=(b,1.34),xytext=(a,1.34),arrowprops={'arrowstyle':'->','lw':2,'color':'#197787'})
 head.text((a+b)/2,1.61,label,ha='center',fontsize=14,color='#197787')
head.text(7,.59,r'$\Gamma_n:\ E_n\times[0,1]\longrightarrow E_n,\qquad \lambda_n(z)(t)=p_n\Gamma_n(j_nz,1-t)$',ha='center',fontsize=14)
head.text(7,.13,'The lifted loop starts at zero and ends at the original z. Its connecting value is +z.',ha='center',fontsize=12)
ax=fig.add_axes([.07,.17,.47,.47]);ax.set(xlim=(-.6,8.5),ylim=(-.6,7.5),xlabel='Base degree u',ylabel='Fibre degree v',xticks=range(9),yticks=range(8));ax.grid(alpha=.16)
ax.add_patch(Rectangle((3.7,2.7),4.8,4.8,facecolor='#e7eff0',edgecolor='#c5d7da'))
ax.text(6.1,6.6,'Possible mixed terms',ha='center',fontsize=11,color='#284d56')
ax.text(6.1,6.05,r'$u\geq4,\ v\geq3$',ha='center',fontsize=13,color='#284d56')
for u in range(9):
 for v in range(8):
  if (u==0 and (v==0 or v>=3)) or (v==0 and u>=4) or (u>=4 and v>=3):ax.plot(u,v,'o',ms=4,color='#335f69',alpha=.65)
colors=['#116a82','#b75c24','#6a4c9c']
for q,color in zip([3,4,5],colors):
 ax.annotate('',xy=(0,q),xytext=(q+1,0),arrowprops={'arrowstyle':'->','lw':2.2,'color':color})
 ax.text((q+1)*.52,q*.46,rf'$d_{{{q+1}}}$',color=color,fontsize=14,bbox=dict(facecolor='white',edgecolor='none',pad=1))
ax.set_title('Exact support example: n = 3',fontsize=14,pad=12)
right=fig.add_axes([.60,.19,.36,.45]);right.axis('off')
lines=[(1.00,r'General range: $n\leq q<2n$',15,'#18323d'),(.85,r'$d_{q+1}:H_{q+1}(L_{n+1};k)$',15,'#18323d'),(.74,r'$\hspace{1}\longrightarrow H_q(L_n;k)$',15,'#18323d'),(.61,'Only these two axis terms can interact.',12,'#18323d'),(.51,'The total space is contractible.',12,'#18323d'),(.41,'The displayed transgression is an isomorphism.',12,'#18323d'),(.28,r'Its inverse is $(\sigma_n)_*\,\mathrm{susp}$.',14,'#18323d'),(.12,r'Fixed $a\geq0$: take $q=n+a$ and $n>a$.',13,'#18323d'),(.01,'Stable homology is then a finite vector space.',12,'#18323d')]
for y,s,fs,c in lines:right.text(0,y,s,fontsize=fs,color=c,va='top')
fig.text(.5,.092,'Dots indicate allowed support, not a claim that every group at a dot is nonzero. Mixed support starts at total degree 2n + 1.',ha='center',fontsize=10)
fig.text(.5,.059,'Proof: The Adams tower and exact inverse limits, Sections 8–11; bundle (9.4), actual suspension (9.6), range (10.3)–(10.6).',ha='center',fontsize=10)
fig.text(.5,.028,'Source context: Friedman, arXiv:0809.4221v8, original TeX 756–898. The full receiving construction is proved in the chapter.',ha='center',fontsize=10)
fig.savefig(W/'finite-cocycle-tower.svg',metadata={'Date':None})
plt.close(fig)
print('Rendered the original cocycle bundle and exact transgression range.')
