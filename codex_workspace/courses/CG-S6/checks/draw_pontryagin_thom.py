"""Reproducible original-frame collapse and its proved inverse comparisons."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

W=Path(__file__).resolve().parents[1]
O=W/"assets"
O.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.fonttype":"path",
                     "svg.hashsalt":"CG-S6-PONTRYAGIN-THOM-20261010"})
fig=plt.figure(figsize=(14,10))
fig.suptitle("The original framed tube and its smooth collapse",fontsize=20,y=.97)
gs=fig.add_gridspec(2,2,left=.07,right=.94,top=.84,bottom=.07,height_ratios=[3.5,2],hspace=.35,wspace=.42)
ax=fig.add_subplot(gs[0,0]); bx=fig.add_subplot(gs[0,1]); cx=fig.add_subplot(gs[1,:])
fig.text(.5,.915,r"Circle example: $a=3,\ b=2,\ c=1,\ d=3/2,\ \epsilon=1$; the given frame is not orthogonal.",ha="center",fontsize=13)
angle=np.linspace(0,2*np.pi,700)
# Exact inverse of (A1,A2) -> (2 A1+A2, 3 A2/2) on the physical unit circle.
A2=(2/3)*np.sin(angle); A1=(np.cos(angle)-A2)/2
ax.fill(A1,A2,color="#e1f0ea");ax.plot(A1,A2,color="#24634d",lw=2)
ax.axhline(0,color="#9caab1",lw=.8);ax.axvline(0,color="#9caab1",lw=.8)
ax.set(xlim=(-.9,.9),ylim=(-.83,.83),xlabel=r"Original frame coordinate $A_1$",ylabel=r"Original frame coordinate $A_2$",aspect="equal")
ax.set_title(r"$\rho=4A_1^2+4A_1A_2+\frac{13}{4}A_2^2<1$",pad=12,fontsize=14)
ax.plot([0,.5],[0,0],color="#84334f",lw=2)
colors=["#b35822","#713f9a","#166e99"]
fractions=[(7,20),(13,20),(9,10)]
for (num,den),col in zip(fractions,colors):
    t=num/den
    ax.scatter([t/2],[0],c=[col],s=48,zorder=4)
    ax.annotate(f"{num}/{den}",xy=(t/2,0),xytext=(t/2,.16+(.10 if num==13 else 0)),
                ha="center",fontsize=10,color=col,arrowprops={"arrowstyle":"-","color":col,"lw":.8})
ax.annotate("Entire boundary → q₊",xy=(-.12,.63),xytext=(-.83,.75),fontsize=11,
            arrowprops={"arrowstyle":"->","color":"#24634d"},color="#24634d")
ax.text(0,-1.20,r"Marked ray: $A=(t/2,0)$, hence $\rho=t^2$."+"\nThe numbers are the retained ray parameters t.",ha="center",fontsize=11,transform=ax.transData)
bx.plot(np.sin(angle),-np.cos(angle),color="#607a87",lw=1.5)
bx.axhline(0,color="#c2cbd0",lw=.8);bx.axvline(0,color="#c2cbd0",lw=.8)
bx.set(xlim=(-1.42,1.65),ylim=(-1.2,1.28),aspect="equal",xlabel=r"$Y_1$  (slice $Y_2=0$)",ylabel=r"Target last coordinate")
bx.set_title("Exact meridian in the original unit S²",fontsize=14,pad=12)
for (num,den),col in zip(fractions,colors):
    t=num/den
    zz=np.exp(t*t/(1-t*t))*t/2
    yy=2*zz/(1+zz*zz); hh=(zz*zz-1)/(1+zz*zz)
    bx.scatter([yy],[hh],c=[col],s=48,zorder=5)
    bx.annotate(f"t = {num}/{den}",xy=(yy,hh),xytext=(1.13,hh+(.06 if num==13 else 0)),
                va="center",color=col,fontsize=10,arrowprops={"arrowstyle":"-","color":col,"lw":.8})
bx.scatter([0,0],[-1,1],color="#233845",s=32,zorder=4)
bx.text(-.12,-1.13,"q₋",ha="right",fontsize=12);bx.text(-.12,1.08,"q₊",ha="right",fontsize=12)
bx.text(.1,-1.6,r"$Z=\exp\!\left(\frac{t^2}{1-t^2}\right)(t/2,0)$; target is $\sigma(Z)$.",ha="center",fontsize=11,transform=bx.transData)
cx.set(xlim=(0,14),ylim=(0,3));cx.axis("off")
cx.text(7,2.85,"The three explicit homotopies proving the inverse",ha="center",fontsize=15,fontweight="bold")
cards=[
    (.05,3.0,"Original F","Its actual inverse image\nand frame E are retained."),
    (3.7,3.0,"Collapse in T","Target latitude change\n(6.9)–(6.11)"),
    (7.35,3.0,"Collapse in Γ","Original ambient tube path\n(6.12)–(6.13)"),
    (11.0,2.95,"Original G, ε","Full positive-form path\n(6.15)–(6.17)")]
for x0,width,title,body in cards:
    cx.add_patch(FancyBboxPatch((x0,1.15),width,1.17,boxstyle="round,pad=.04,rounding_size=.08",
                               facecolor="#edf2f5",edgecolor="#536d79"))
    cx.text(x0+width/2,2.11,title,ha="center",fontsize=12,fontweight="bold")
    cx.text(x0+width/2,1.63,body,ha="center",va="center",fontsize=10,linespacing=1.5)
for x0 in (3.1,6.75,10.4):
    cx.annotate("",xy=(x0+.5,1.72),xytext=(x0,1.72),arrowprops={"arrowstyle":"-|>","color":"#84334f","lw":1.7})
cx.text(7,.66,r"At the original inverse image: $D(\kappa_-\mathcal{P})E_\ell=e_\ell$, while $D\mathcal{P}(E_\ell)=(2e_\ell,0)$.",ha="center",fontsize=12)
cx.text(7,.2,"Proof: Sections 3, 6 and Exercise 9.1. The plotted dots are numerical samples of the displayed exact formulas.\nHuman-source context: Michel–Weber, arXiv:1409.0704v1, §3.2. Full receiving proof is in this companion.",ha="center",fontsize=9.5,linespacing=1.5)
fig.savefig(O/"pontryagin-thom-original-frame.svg",metadata={"Date":None})
print(str(O/"pontryagin-thom-original-frame.svg"))
