from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-HIGHER-SLIDES-20261010'})
fig=plt.figure(figsize=(14,9.5))
fig.text(.5,.96,'One belt crossing, the full prism correction, both adjacent maps',ha='center',fontsize=17,fontweight='bold')
ax=fig.add_axes([.07,.56,.37,.29]);ax.set_xlim(-1.15,1.15);ax.set_ylim(-1.15,1.15)
ax.set_aspect('equal');ax.set_axis_off()
ax.add_patch(Rectangle((-1,-1),2,2,facecolor='#eef4f6',edgecolor='#bac9d0'))
ax.plot([-0.9,.9],[-.68,-.68],color='#1e5870',lw=3)
ax.plot([-0.9,.9],[.68,.68],color='#9a4269',lw=3)
ax.scatter([0],[0],s=60,color='#202d35')
ax.add_patch(FancyArrowPatch((0,-.63),(0,.63),arrowstyle='->',mutation_scale=18,lw=2,color='#37795b'))
ax.text(.14,.06,r'belt $x=0$',fontsize=11)
ax.text(-.98,-.96,r'$x_k=-\sigma\varepsilon$',fontsize=11,color='#1e5870')
ax.text(-.98,.82,r'$x_k=+\sigma\varepsilon$',fontsize=11,color='#9a4269')
ax.text(.23,-.47,r'$t$ increases',fontsize=10,color='#37795b')
fig.text(.255,.505,'Two-coordinate section of the inner patch, with σ = +1.\nThe full patch has k − 1 coordinates; other directions are retained.',ha='center',fontsize=10.5)
fig.text(.725,.815,r'$\det D_{(v,t)}x=2\sigma\varepsilon$',ha='center',fontsize=21)
fig.text(.725,.744,r'$\mathrm{prism\ orientation}=(t,v_1,\ldots,v_{k-1})$',ha='center',fontsize=17)
fig.text(.725,.67,r'$h=(-1)^{k-1}\sigma$',ha='center',fontsize=23,color='#9a4269')
fig.text(.725,.594,r'$\mathcal{T}=F_*-\partial\overline{P}-\overline{P}\partial$',ha='center',fontsize=21)
fig.text(.725,.525,r'$\mathcal{T}|_{S_*(B)}=\mathrm{id}$',ha='center',fontsize=20)
fig.text(.5,.429,r'$\mathcal{T}_k=U^{-1},\qquad U=I+hE_{ji},\qquad U^{-1}=I-hE_{ji}$',ha='center',fontsize=21)
canvas=fig.add_axes([0,0,1,1],frameon=False);canvas.set_axis_off()
xs=[.14,.5,.86]
for y,labels in [(.32,[r'$C_{k+1}$',r'$C_k$',r'$C_{k-1}$']),(.17,[r"$C'_{k+1}$",r"$C'_k$",r"$C'_{k-1}$"])]:
 for x,label in zip(xs,labels):fig.text(x,y,label,ha='center',fontsize=20)
for y,labels in [(.334,[r'$D_{k+1}$',r'$D_k$']),(.184,[r'$U^{-1}D_{k+1}$',r'$D_kU$'])]:
 for a,label in enumerate(labels):
  canvas.annotate('',(xs[a+1]-.065,y),(xs[a]+.065,y),arrowprops=dict(arrowstyle='->',lw=1.6,color='#1e5870'))
  fig.text((xs[a]+xs[a+1])/2,y+.022,label,ha='center',fontsize=16)
for x,label in zip(xs,[r'$\mathrm{id}$',r'$U^{-1}$',r'$\mathrm{id}$']):
 canvas.annotate('',(x,.216),(x,.304),arrowprops=dict(arrowstyle='->',lw=1.7,color='#9a4269'))
 fig.text(x+.038,.255,label,ha='left',fontsize=15,color='#9a4269')
fig.text(.5,.105,'Downward arrows are the actual corrected map from old to new. Both squares commute.',ha='center',fontsize=12)
fig.text(.5,.043,'Proof: Sections 2–5, especially (2.7), (4.5), (5.3) and (5.6).\nHuman source: Durst–Geiges–Kegel, arXiv:1811.09055v1, Section 4.1. This is a slide, before Whitney cancellation.',ha='center',fontsize=10)
fig.savefig(O/'higher-slide-prism-and-adjacent-maps.svg',metadata={'Date':None})
print(str(O/'higher-slide-prism-and-adjacent-maps.svg'))
