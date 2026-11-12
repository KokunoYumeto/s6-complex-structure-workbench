"""Reproduce the original integral comparison diagram; CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
W=Path(__file__).resolve().parents[1]/'assets'
plt.rcParams.update({'svg.hashsalt':'CG-S6-integral-stable-comparison','font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(13.2,8.8));fig.patch.set_facecolor('#f8fafb');ax.set_facecolor('#f8fafb');ax.set_xlim(0,13.2);ax.set_ylim(0,8.8);ax.axis('off')
ink='#173042';teal='#146e77';muted='#526774'
def txt(x,y,s,size=14,color=ink,weight='normal'):ax.text(x,y,s,ha='center',va='center',fontsize=size,color=color,fontweight=weight)
def arrow(a,b):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.8,color=teal))
def panel(y,h):ax.add_patch(FancyBboxPatch((.3,y),12.6,h,boxstyle='round,pad=.12',facecolor='white',edgecolor='#cad6dd',lw=1))
txt(6.6,8.35,'The integral group and the original unit',21,weight='bold')
panel(5.75,2.05);txt(6.6,7.42,'1. Prove finite generation before taking completion',15,weight='bold')
txt(2.1,6.79,'Original integral chains',13);txt(2.1,6.32,'finite presentations\nand both homotopies',12,muted)
arrow((3.62,6.72),(4.15,6.72));txt(6.15,6.82,r'$L_q(A)$ and the actual path fibres',14);txt(6.15,6.31,'every integral homology group\nis finitely generated',12,muted)
arrow((8.3,6.72),(8.85,6.72));txt(10.7,6.84,r'$\pi_{m+r}S^m\;\longrightarrow\;\pi_r\mathbb{S}$',16);txt(10.7,6.29,r'isomorphism for $m\geq\max(3,r+2)$',11,muted)
panel(2.85,2.47);txt(6.6,4.98,'2. Retain the entire Moore sequence and its transitions',15,weight='bold')
xs=[.9,3.1,6.6,10.1,12.25]
labels=[r'$0$',r'$A_n/p^{a+1}A_n$',r'$\pi_nD_{a+1}$',r'$A_{n-1}[p^{a+1}]$',r'$0$']
labels2=[r'$0$',r'$A_n/p^aA_n$',r'$\pi_nD_a$',r'$A_{n-1}[p^a]$',r'$0$']
for x,t,b in zip(xs,labels,labels2):txt(x,4.36,t,16);txt(x,3.54,b,16)
for a,b in zip(xs[:-1],xs[1:]):
 arrow((a+.82 if a!=.9 else a+.24,4.36),(b-.9 if b!=12.25 else b-.22,4.36))
 arrow((a+.82 if a!=.9 else a+.24,3.54),(b-.9 if b!=12.25 else b-.22,3.54))
for x in xs[1:-1]:arrow((x,4.16),(x,3.76))
txt(3.98,3.95,'reduction',10,muted);txt(7.51,3.95,'original map',10,muted);txt(10.86,3.95,r'$\times p$',12,muted)
txt(6.6,3.05,'Finite stage groups kill lim¹; the full p-power transition kills the torsion limit.',11,muted)
panel(.35,2.05);txt(6.6,2.03,'3. Use every prime and the same original unit',15,weight='bold')
txt(3.15,1.4,r'$\pi_6(\mathbb{S}^{\wedge}_p)=0\quad(p\ \mathrm{odd})$',18)
txt(9.05,1.4,r'$\pi_6\mathbb{S}\;\longrightarrow\;\pi_6(\mathbb{S}^{\wedge}_2)\;\cong\;\mathbb{Z}/2$',19)
txt(8.25,1.77,r'$(v_2)_*$',12,teal)
txt(6.6,.76,'All primary subgroups and the free rank are accounted for. The framed value is the next calculation.',11,muted)
fig.tight_layout(pad=.6);fig.savefig(W/'integral-stable-comparison.svg',metadata={'Date':None});plt.close(fig)
