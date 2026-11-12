"""The exact all-length module calculation, with both source gradings."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-DEGREE-SIX-COBAR-20261010'})
fig,ax=plt.subplots(figsize=(14,10));fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.set(xlim=(0,14),ylim=(0,10));ax.axis('off')
ax.text(7,9.55,'Every length in the degree-six cobar calculation',ha='center',fontsize=19,fontweight='bold')
ax.text(7,9.09,r'$R=\mathbb{F}_2[x],\qquad d_3:(s,t,W)\mapsto(s+1,t,W-3)$',ha='center',fontsize=16)
def card(x,y,w,h,title,body,color='#edf2f5'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06,rounding_size=0.12',facecolor=color,edgecolor='#344a58',lw=1.2))
 ax.text(x+w/2,y+h-.28,title,ha='center',va='top',fontsize=14,fontweight='bold')
 ax.text(x+w/2,y+h/2-.13,body,ha='center',va='center',fontsize=12,linespacing=1.7)
def arrow(a,b,label,offset=(0,0)):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'-|>','lw':1.8,'color':'#993d55'})
 mid=((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1])
 ax.text(*mid,label,ha='center',va='center',fontsize=12,color='#852d46',bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(2.0,8.45,'Incoming: t − s = 7',ha='center',fontsize=13)
ax.text(7.0,8.45,'Receiving: t − s = 6',ha='center',fontsize=13)
ax.text(12.0,8.45,'Outgoing: t − s = 5',ha='center',fontsize=13)
card(.45,6.6,3.1,1.45,r'$v=ab+yc$',r'$(s,t,W)=(2,9,6)$'+'\nFull cochain: equation (4.7)')
card(5.05,6.4,3.9,1.8,r'$R\{z^2\}$',r'$x^r z^2:\ (s,t,W)=(2+r,8+r,2+r)$'+'\nEvery integer r ≥ 0 is retained.','#e6f3ee')
arrow((3.65,7.25),(4.95,7.25),r'$d_3v=xz^2$',(0,.35))
card(5.05,4.3,3.9,1.45,r'$(R/(x))\{y^2B\}$',r'$(s,t,W)=(4,10,8)$')
card(10.45,4.3,3.1,1.45,r'$(R/(x))\{y^5\}$',r'$(s,t,W)=(5,10,5)$')
arrow((9.05,5.02),(10.35,5.02),r'$d_3(y^2B)=y^5$',(0,.37))
card(.45,2.3,3.1,1.45,r'$y^3B$',r'$(s,t,W)=(5,12,9)$')
card(5.05,2.3,3.9,1.45,r'$(R/(x))\{y^6\}$',r'$(s,t,W)=(6,12,6)$')
arrow((3.65,3.02),(4.95,3.02),r'$d_3(y^3B)=y^6$',(0,.38))
ax.text(11.92,2.92,'Odd primes:\nevery degree-six\nclass is a boundary.\nExact signs: Section 6.',ha='center',va='center',fontsize=12,linespacing=1.7)
ax.text(7,1.59,r'Survivor: $\mathbb{F}_2\{[\zeta_1^4\mid\zeta_1^4]\}$ at $(s,t,W)=(2,8,2)$',ha='center',fontsize=17,color='#175c43')
ax.text(7,1.11,'No incoming higher differential: its length-one, degree-eight source would need weight greater than two;\nthe only first-page class there is h₁₃, with weight one. The representative has zero original differential.',ha='center',fontsize=11,linespacing=1.6)
ax.text(7,.38,'Proof: Sections 3–6, especially (3.7)–(3.8), (4.3)–(4.10), and (5.1)–(5.3).\nSource comparison: Isaksen, arXiv:1407.8418v2; its May d₂ is this weight-drop-three d₃, with W = 2m − s.\nThese are cobar groups. The stable-homotopy and framed-manifold comparisons are subsequent arguments.',ha='center',fontsize=9.5,linespacing=1.5)
fig.savefig(O/'degree-six-cobar-all-lengths.svg',metadata={'Date':None})
print(str(O/'degree-six-cobar-all-lengths.svg'))
