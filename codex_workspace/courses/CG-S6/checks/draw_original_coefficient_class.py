"""Reproducible exact degree-six coefficient and weight diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1]/'assets'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'original-coefficient-h28','font.size':12})
fig,ax=plt.subplots(figsize=(12.8,7.3));ax.set_xlim(0,12.8);ax.set_ylim(0,7.3);ax.axis('off')
ax.text(6.4,7.05,'The full original degree-six coefficient class',ha='center',fontsize=19,weight='bold')
ax.text(6.4,6.62,r'$\mathcal{H}_0^{2,8}=\mathbb{F}_2[t_{\mathrm{h}}]\{e\},\qquad e=[\xi_1^2|\xi_1^2],\qquad |e|_w=4,\quad |t_{\mathrm{h}}|_w=-1$',ha='center',fontsize=15)
ax.text(.35,5.97,'Original coefficient module',weight='bold')
ax.text(7.7,5.97,'Exact localized comparison',weight='bold')
labels=[r'$e=[\xi_1^2|\xi_1^2]$',r'$t_{\mathrm{h}}e$',r'$t_{\mathrm{h}}^2e$',r'$t_{\mathrm{h}}^3e$',r'$t_{\mathrm{h}}^4e=[\tau_0^4|\tau_0^4]$']
for k,label in enumerate(labels):
    y=5.48-.86*k
    ax.scatter([1.15],[y],s=65,color='#15645c',zorder=3)
    ax.text(.65,y,f'w={4-k}',ha='right',va='center',fontsize=11)
    ax.text(1.47,y,label,va='center',fontsize=14)
    if k<4:
        ax.annotate('',xy=(1.15,y-.69),xytext=(1.15,y-.17),arrowprops={'arrowstyle':'->','color':'#15645c','lw':1.8})
        ax.text(.93,y-.43,r'$t_{\mathrm{h}}$',ha='right',va='center',fontsize=11)
    if k in [0,4]:
        start=5.05 if k==0 else 6.05
        ax.annotate('',xy=(7.25,y),xytext=(start,y),arrowprops={'arrowstyle':'->','color':'#9c4b23','lw':1.8})
        ax.text((start+7.25)/2,y+.18,r'$\Psi^{\otimes2}$',ha='center',fontsize=12)
        dest=(r'$t_{\mathrm{h}}^{-4}[z_1^4|z_1^4]$' if k==0 else r'$[z_1^4|z_1^4]$')
        ax.text(7.5,y,dest,va='center',fontsize=16)
ax.annotate('',xy=(1.15,1.37),xytext=(1.15,1.87),arrowprops={'arrowstyle':'->','color':'#15645c','lw':1.8})
ax.text(1.47,1.42,'continues in every lower weight',va='center',fontsize=11)
ax.text(7.5,4.35,'The coefficient is inverted here.\nThe map retains its complete power.\nThe original polynomial module\nremains identified on the left.',fontsize=12,va='top',linespacing=1.5)
ax.text(6.4,.84,'All five displayed classes are nonzero. There is no coefficient torsion in this bidegree.',ha='center',fontsize=12)
ax.text(6.4,.42,'Proof: coefficient-ring chapter, (5.7), (5.9) and (6.5); complete original matrices in the attached certificate.',ha='center',fontsize=10)
ax.text(6.4,.13,'Human-source context: Dugger–Isaksen, arXiv:0901.1632v1, Section 2. This diagram asserts an algebraic result.',ha='center',fontsize=9)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
for ext in ['svg']:fig.savefig(W/f'original-coefficient-degree-six-class.{ext}',dpi=140,metadata={'Date':None} if ext=='svg' else None)
plt.close(fig)
