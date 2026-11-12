from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-HANDLE-CHAINS-20261010'})
fig=plt.figure(figsize=(14,9))
fig.text(.5,.956,'The original incidences and the complete chain comparison',ha='center',fontsize=18,fontweight='bold')
ax=fig.add_axes([.055,.52,.40,.32]);ax.set_axis_off()
ax.set_xlim(-1.1,1.1);ax.set_ylim(-.8,.8)
ax.add_patch(Rectangle((-.95,-.65),1.9,1.3,facecolor='#eef4f6',edgecolor='#bac9d0'))
ax.plot([0,0],[-.63,.63],color='#933b67',lw=3)
ax.plot([-.85,.85],[-.42,.42],color='#173c4e',lw=3)
ax.add_patch(FancyArrowPatch((-.34,-.168),(.25,.124),arrowstyle='->',mutation_scale=16,lw=2,color='#173c4e'))
ax.add_patch(FancyArrowPatch((0,-.32),(0,.32),arrowstyle='->',mutation_scale=16,lw=2,color='#933b67'))
ax.scatter([0],[0],color='#17242a',s=36,zorder=5)
ax.text(.1,.52,r'belt: $u=0$',color='#933b67',fontsize=12)
ax.text(.48,-.34,r'attaching $T A$',color='#173c4e',ha='center')
ax.text(-.86,-.57,r'$u$ increases $\longrightarrow$',fontsize=11)
ax.set_title('Local schematic: one normal direction and one belt direction',fontsize=11,pad=12)
fig.text(.255,.465,r'$c(z)=\operatorname{sgn}\det D(u\circ\alpha)_\theta,\quad z=\alpha(\theta)$',ha='center',fontsize=14)
fig.text(.255,.422,'The full normal block has p coordinates.\\nThe drawing shows a two-direction schematic only.'.replace('\\n','\n'),ha='center',fontsize=11)
fig.text(.725,.80,r'$I(z)=\varepsilon_{p,i}(-1)^p c(z)$',ha='center',fontsize=22)
fig.text(.725,.735,r'$a_{ij}=\sum_{z\in A_j\cap B_i}c(z)$',ha='center',fontsize=21)
fig.text(.725,.653,'The chart sign, outward-normal permutation,\\nand each intersection sign are all retained.'.replace('\\n','\n'),ha='center',fontsize=13)
fig.text(.725,.566,'Integral coefficients use the belt normal frame.\\nAn ambient orientation is not required.'.replace('\\n','\n'),ha='center',fontsize=13)
fig.text(.725,.477,'Proof: Section 3, equations (3.3)–(3.9).',ha='center',fontsize=11)
canvas=fig.add_axes([0,0,1,1],frameon=False);canvas.set_axis_off()
xs=[.14,.50,.86]
for x,label in zip(xs,[r'$C_{p+1}$',r'$C_p$',r'$C_{p-1}$']):
 fig.text(x,.313,label,ha='center',fontsize=21)
for x,label in zip(xs,[r'$C^\prime_{p+1}$',r'$C^\prime_p$',r'$C^\prime_{p-1}$']):
 fig.text(x,.165,label,ha='center',fontsize=21)
for y,labels in [(.325,[r'$D_{p+1}$',r'$D_p$']),(.177,[r'$U_p^{-1}D_{p+1}U_{p+1}$',r'$U_{p-1}^{-1}D_pU_p$'])]:
 for j,label in enumerate(labels):
  canvas.annotate('',(xs[j+1]-.075,y),(xs[j]+.075,y),arrowprops=dict(arrowstyle='->',lw=1.6,color='#173c4e'))
  fig.text((xs[j]+xs[j+1])/2,y+.023,label,ha='center',fontsize=15)
for x,label in zip(xs,[r'$U_{p+1}$',r'$U_p$',r'$U_{p-1}$']):
 canvas.annotate('',(x,.296),(x,.205),arrowprops=dict(arrowstyle='->',lw=1.6,color='#933b67'))
 fig.text(x+.038,.245,label,ha='left',fontsize=14,color='#933b67')
fig.text(.5,.096,'Both squares commute: the upward maps give original coordinates. Section 4, equation (4.2).',ha='center',fontsize=12)
fig.text(.5,.043,'Human source: Durst–Geiges–Kegel, arXiv:1811.09055v1, Sections 3.1 and 4.1.\\nThis figure shows the proved chain maps; it does not depict a completed geometric handle cancellation.'.replace('\\n','\n'),ha='center',fontsize=10)
fig.savefig(O/'handle-incidences-and-chain-comparison.svg',metadata={'Date':None})
print(str(O/'handle-incidences-and-chain-comparison.svg'))
