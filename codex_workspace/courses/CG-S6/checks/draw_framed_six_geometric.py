"""Original local polynomial slice and the proved geometric comparison maps."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
W=Path(__file__).resolve().parents[1]/'assets'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'CG-S6-framed-six-geometric','mathtext.fontset':'dejavusans'})
navy='#15354a';teal='#087e82';orange='#a75a22'
fig=plt.figure(figsize=(15,11),facecolor='#faf9f5')
canvas=fig.add_axes([0,0,1,1]);canvas.set_xlim(0,15);canvas.set_ylim(0,11);canvas.axis('off')
def txt(x,y,s,size=12,**kw):canvas.text(x,y,s,fontsize=size,color=navy,va='top',**kw)
def box(x,y,w,h):canvas.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.1',linewidth=1,edgecolor='#b8c9cf',facecolor='white'))
def arrow(x,y,X,Y):canvas.annotate('',xy=(X,Y),xytext=(x,y),arrowprops={'arrowstyle':'->','color':teal,'lw':2})
txt(.45,10.7,'From the local derivative defect to the original framed nullbordism',20,fontweight='bold')
txt(.45,10.22,r'Exact slice $u=v=0$:  $F_t(0,0,w)=(0,0,w^2,0,0,w^3-tw)$',14)
ww=np.linspace(-1,1,801)
for i,(tt,label) in enumerate([(-.25,r'$t=-1/4$'),(0,r'$t=0$'),(.25,r'$t=1/4$')]):
    ax=fig.add_axes([.075+i*.31,.65,.235,.235],facecolor='white')
    ax.plot(ww*ww,ww**3-tt*ww,color=teal,lw=2)
    ax.set_xlim(-.04,1.04);ax.set_ylim(-1.3,1.3)
    ax.set_xlabel(r'$x_3=w^2$',fontsize=12)
    ax.set_ylabel(r'$x_6=w^3-tw$',fontsize=12)
    ax.set_title(label+'  '+['no double pair','rank loss at $w=0$','one unordered double pair'][i],fontsize=12,color=navy)
    ax.grid(alpha=.15);ax.spines[['top','right']].set_visible(False)
    if tt>=0:
        ax.scatter([tt],[0],s=45,color=orange,zorder=5)
        ax.annotate(['','$(0,0)$','$w=\\pm1/2$'][i],xy=(tt,0),xytext=(.38,.5),textcoords='data',fontsize=11,arrowprops={'arrowstyle':'->','color':orange},color=orange)
txt(.45,6.65,'Only the displayed two-coordinate slice is drawn. Curves sample the stated exact polynomial for −1 ≤ w ≤ 1.',10)
box(.5,3.8,14,2.35)
txt(.8,5.95,'Both changes are retained',16,fontweight='bold')
txt(.9,5.48,r'$r(u,v,w,t)=(2w,u,v,3w^2-t),\qquad \det Dr(0)=-2$',16)
txt(.9,4.94,r'local framing degree $=-1$;  framing parity changes by $1$',14)
txt(.9,4.46,r'one end of the unordered double curve;  double parity changes by $1$',14)
txt(10.25,5.1,r'$Q_\tau=\varepsilon_\tau+\mu$',18)
txt(10.25,4.55,r'$\Delta Q_\tau=1+1=0$',18)
arrow(8.95,4.98,9.9,4.98)
box(.5,.7,14,2.62)
txt(.8,3.1,'The actual quadratic-space and bordism comparisons',16,fontweight='bold')
txt(.9,2.6,r'$(L_2^\perp/L_2,\bar q_P)$',16)
txt(5.1,2.6,r'$(H_3(M;\mathbb{F}_2),q_M)$',16)
arrow(3.8,2.36,4.85,2.36)
txt(3.94,2.83,r'$\bar\Xi$',13)
txt(9.75,2.62,r'$G(q_P)=2^rG(q_M)$',16)
txt(.9,1.89,r'$\kappa:\ \Omega^{\mathrm{fr}}_6\ \longrightarrow\ \mathbb{F}_2$',17)
txt(6.6,1.88,'isomorphism',14)
txt(.9,1.34,r'$(S^3\times S^3,\tau_{\mathrm{Lie}})\mapsto1$',15)
txt(8.1,1.34,r'$(\Sigma,\tau_\Sigma)\mapsto0$',15)
txt(8.1,.95,'A framed nullbordism exists; bounding surgery remains.',11)
txt(.55,.39,'Proofs: (5.22)–(5.27), (6.22), (8.5)–(8.7), (8.13), (9.1)–(9.4). Human context: Michel–Weber and Snaith, cited in Section 11.',10)
fig.savefig(W/'framed-six-geometric.svg',metadata={'Date':None})
plt.close(fig)
print('Rendered framed-six-geometric.svg.')
