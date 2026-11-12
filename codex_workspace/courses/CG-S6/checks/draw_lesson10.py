"""Reproducible exact diagrams for the conormal and toric Cech arguments."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Polygon
import numpy as np
W=Path(__file__).resolve().parents[1]
OUT=W/'assets'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-10-20261009',
                     'mathtext.fontset':'dejavusans','savefig.facecolor':'white'})
ink='#1c2d43';blue='#2166a5';red='#a33730';green='#25765b'
def box(ax,x,y,w,h,title,lines,color=blue):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',
                            facecolor='#f5f8fb',edgecolor=color,linewidth=1.4))
 ax.text(x+w/2,y+h-.035,title,ha='center',va='top',weight='bold',color=color,fontsize=13)
 for j,line in enumerate(lines):
  ax.text(x+w/2,y+h-.09-.058*j,line,ha='center',va='top',color=ink,fontsize=13)
def arrow(ax,start,end,label=None):
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':ink,'lw':1.6})
 if label:ax.text((start[0]+end[0])/2+.012,(start[1]+end[1])/2,label,
                  ha='left',va='center',color=ink,fontsize=12)
fig,ax=plt.subplots(figsize=(11,10))
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.98,'A nonzero ambient form survives both endpoint vanishings',
        ha='center',va='top',weight='bold',fontsize=17,color=ink)
ax.text(.5,.93,r'$t=U_0V_0,\quad S=(U_0V_0=0),\quad \lambda=2$',
        ha='center',va='top',fontsize=16,color=ink)
box(ax,.05,.64,.4,.23,'Branch U₀ = 0',
    [r'$e=k_+(V_0)s_D$',r'$k_+(0)=2/3$',r'$e\,dt=k_+(V_0)V_0\,dU_0\otimes s_D$'])
box(ax,.55,.64,.4,.23,'Branch V₀ = 0',
    [r'$e=k_-(U_0)s_D$',r'$k_-(0)=4/3$',r'$e\,dt=k_-(U_0)U_0\,dV_0\otimes s_D$'])
arrow(ax,(.25,.625),(.40,.56))
arrow(ax,(.75,.625),(.60,.56))
box(ax,.05,.365,.90,.18,'Conormal-kernel map on the full fibre',
    [r'$s_e=(k_+(V_0)V_0\,dU_0+k_-(U_0)U_0\,dV_0)\otimes s_D$',
     r'$s_e\ne0,\qquad H^0(S,\Omega^1_{\mathcal{X}}|_S\otimes A)=\mathbb{C} s_e$'],green)
arrow(ax,(.5,.35),(.5,.285),r'$\rho$')
box(ax,.05,.105,.90,.165,'Intrinsic torsion on the double curve',
    [r'$\rho(s_e)=-\frac{2}{3}\,\tau\otimes s_D\ne0$',
     r'$\tau=[V_0\,dU_0]=-[U_0\,dV_0],\qquad U_0\tau=V_0\tau=0$'],red)
ax.text(.5,.05,r'Quotient by torsion: $\rho(s_e)\mapsto0$ in $\widetilde{\Omega}^1_S\otimes A$.',
        ha='center',va='center',fontsize=13,color=ink)
fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.98)
for ext in ('svg',):fig.savefig(OUT/('conormal-section-and-torsion.'+ext),dpi=150,metadata={'Date':'2026-10-09'})
plt.close(fig)

fig=plt.figure(figsize=(12,6.8))
ax=fig.add_axes([.06,.16,.44,.70])
tx=fig.add_axes([.54,.14,.44,.70]);tx.axis('off')
fig.suptitle('The hexagonal normalization: solving a Laurent coefficient',
             y=.96,fontsize=17,weight='bold',color=ink)
rays=np.array([(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)])
for i in range(6):
 points=np.array([[0,0],rays[i],rays[(i+1)%6]])
 bad=i in (1,2,3)
 ax.add_patch(Polygon(points,facecolor='#e9b6ab' if bad else '#dae8f4',edgecolor='none',alpha=.75))
 midpoint=(rays[i]+rays[(i+1)%6])*.37
 ax.text(*midpoint,r'$\sigma_'+str(i+1)+'$',ha='center',va='center',
         fontsize=13,color=red if bad else blue)
for i,r in enumerate(rays):
 ax.plot([0,r[0]],[0,r[1]],color=red if r[0]<0 else ink,lw=2)
 p=r*1.18
 ax.text(*p,r'$r_'+str(i+1)+'='+str(tuple(map(int,r)))+'$',ha='center',va='center',fontsize=12,color=ink)
ax.scatter([0],[0],color=ink,s=15)
ax.set(xlim=(-1.55,1.55),ylim=(-1.48,1.48),aspect='equal')
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
ax.grid(alpha=.16);ax.spines[['top','right']].set_visible(False)
ax.set_xlabel('first lattice coordinate');ax.set_ylabel('second lattice coordinate')
lines=[
 ('Original weight',r'$m=(1,0)$'),
 ('Pairings in the original ray order',r'$\langle m,r_i\rangle=(1,0,-1,-1,0,1)$'),
 ('Charts forbidding this monomial',r'$F_m=\{2,3,4\}$'),
 ('Their connecting intersections',r'$\sigma_2\ \overset{r_3}{\longleftrightarrow}\ \sigma_3'
                          r'\ \overset{r_4}{\longleftrightarrow}\ \sigma_4$'),
 ('Choose the coefficient potential',r'$b_i(m)=a_{2i}(m),\quad b_2=b_3=b_4=0$'),
 ('The cocycle is its difference',r'$a_{ij}(m)=b_j(m)-b_i(m)$')]
for k,(title,formula) in enumerate(lines):
 y=.98-k*.165
 tx.text(0,y,title,ha='left',va='top',color=ink,fontsize=12,weight='bold')
 tx.text(0,y-.068,formula,ha='left',va='top',color=red if k==2 else blue,fontsize=13)
fig.text(.06,.045,'Rays have their exact primitive coordinates; shaded cones are truncated for display.',
         color=ink,fontsize=11)
for ext in ('svg',):fig.savefig(OUT/('hexagon-laurent-cocycle.'+ext),dpi=150,metadata={'Date':'2026-10-09'})
plt.close(fig)
print(str(OUT))
