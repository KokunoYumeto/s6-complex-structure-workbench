from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path','svg.hashsalt':'CG-S6-RELATIVE-DISK-20261009'})
fig,ax=plt.subplots(figsize=(12,9));ax.set_xlim(0,12);ax.set_ylim(0,9);ax.axis('off')
ax.text(6,8.6,'A finite parameter family constructs the embedded disk',ha='center',fontsize=18,fontweight='bold')
ax.text(6,7.88,r'$F_v(p)=\mathfrak{r}\left(\iota u(p)+g(p)v_0+g(p)p_1v_1+g(p)p_2v_2\right)$',ha='center',fontsize=20)
ax.text(6,7.31,r'$p\in D_h^2,\quad v\in\mathbb{R}^{3m},\quad g=0\ \mathrm{on}\ r_0\leq\|p\|\leq h$',ha='center',fontsize=18)
xs=[3.15,4.68,6.42];ys=[6.64,6.12,5.6]
entries=[[r'$g$',r'$gp_1$',r'$gp_2$'],[r'$g_1$',r'$g_1p_1+g$',r'$g_1p_2$'],[r'$g_2$',r'$g_2p_1$',r'$g_2p_2+g$']]
for row,y in zip(entries,ys):
 for item,x in zip(row,xs):ax.text(x,y,item,ha='center',va='center',fontsize=18)
for x,sign in [(2.42,1),(7.25,-1)]:
 ax.plot([x+.15*sign,x,x,x+.15*sign],[6.99,6.99,5.23,5.23],color='#26717c',lw=1.8)
ax.text(1.6,6.12,r'$\mathcal{J}=$',ha='center',va='center',fontsize=22)
ax.text(9.44,6.12,r'$\det\mathcal{J}=g^3>0$',ha='center',va='center',fontsize=20)
ax.text(6,4.8,'The ambient value and both first derivatives can vary independently.',ha='center',fontsize=14)
ax.plot([.35,11.65],[4.48,4.48],color='#b4c5cb')
columns=[2.1,5.4,7.65,10.2]
for x,txt in zip(columns,['Defect','Domain dimension','Codimension','Solution dimension']):
 ax.text(x,4.04,txt,ha='center',fontsize=11.7,fontweight='bold')
rows=[('Derivative rank one','2','4',r'$3m-2$'),('Derivative rank zero','2','10',r'$3m-8$'),('Two equal disk values','4','5',r'$3m-1$'),('Meeting a surface interior','2','3',r'$3m-1$')]
for y,row in zip([3.49,2.96,2.43,1.90],rows):
 for x,txt in zip(columns,row):ax.text(x,y,txt,ha='center',fontsize=13.6)
ax.plot([.35,11.65],[1.55,1.55],color='#b4c5cb')
ax.text(6,1.13,r'Every bad-parameter projection has measure zero in $\mathbb{R}^{3m}$.',ha='center',fontsize=14)
ax.text(6,.69,'The original collar and all its derivatives remain fixed.',ha='center',fontsize=14)
ax.text(6,.19,'Equations (5.4), (5.7), (5.9)–(5.13). The curved-target derivative term is retained.',ha='center',fontsize=11.5)
fig.savefig(O/'relative-disk-parameters.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)
print(str(O/'relative-disk-parameters.svg'))

