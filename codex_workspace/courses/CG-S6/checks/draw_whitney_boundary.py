from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1];O=W/'assets'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-WHITNEY-BOUNDARY-20261010','font.size':13})
fig=plt.figure(figsize=(12,11))
fig.text(.5,.96,'The original corner collar, embedded filling and frame signs',ha='center',fontsize=18,fontweight='bold')
ax=fig.add_axes([.07,.55,.4,.32]);ax.set_aspect('equal');ax.axis('off')
x=np.linspace(-1,1,501);top=1-x*x
ax.fill(np.r_[x,x[::-1]],np.r_[top,-top[::-1]],color='#e5ebee')
ax.plot(x,top,color='#26717c',lw=2.5);ax.plot(x,-top,color='#b56232',lw=2.5)
ang=np.linspace(0,2*np.pi,501);ax.fill(.68*np.cos(ang),.59*np.sin(ang),color='#cce5ec')
ax.plot(.68*np.cos(ang),.59*np.sin(ang),color='#26717c',lw=1.5)
ax.scatter([-1,1],[0,0],color='#172e40',s=35)
ax.text(-1.12,0,r'$p$',ha='center',va='center',fontsize=17);ax.text(1.12,0,r'$q$',ha='center',va='center',fontsize=17)
ax.text(0,1.13,r'$\alpha\subset A:\ p\longrightarrow q$',ha='center',fontsize=15)
ax.text(0,-1.27,r'$\beta\subset B:\ p\longrightarrow q$',ha='center',fontsize=15)
ax.text(0,.77,r'$C$',ha='center',fontsize=18);ax.text(0,.02,r'$F(D_h^2)$',ha='center',fontsize=20)
ax.text(.53,.4,r'$\gamma$',ha='center',fontsize=17)
ax.set_xlim(-1.4,1.4);ax.set_ylim(-1.45,1.4)
fig.text(.27,.52,'Collar topology schematic; the two outer corners remain.',ha='center',fontsize=11.5)
ax=fig.add_axes([.6,.57,.3,.27]);ax.set_aspect('equal')
t=np.linspace(0,1,3001)
z=3*t-1
rho=lambda v: np.exp(-1/np.maximum(v,1e-300))*(v>0)
k=rho(z)/(rho(z)+rho(1-z))
integ=np.r_[0,np.cumsum((k[1:]+k[:-1])*(t[1:]-t[:-1])/2)]
eps=.4
xx=eps/2+2*eps*integ;yy=eps/2+2*eps*integ[::-1]
assert np.allclose([xx[0],yy[0],xx[-1],yy[-1]],[eps/2,3*eps/2,3*eps/2,eps/2])
ax.plot(xx,yy,color='#26717c',lw=2.5)
ax.plot([eps/2,eps/2],[3*eps/2,1.8*eps],color='#26717c',lw=2.5)
ax.plot([3*eps/2,1.8*eps],[eps/2,eps/2],color='#26717c',lw=2.5)
ax.scatter([eps/2,3*eps/2],[3*eps/2,eps/2],s=28,color='#26717c')
ax.set_xlim(0,1.9*eps);ax.set_ylim(0,1.9*eps)
ax.set_xticks([0,eps/2,eps,3*eps/2],['0',r'$\varepsilon/2$',r'$\varepsilon$',r'$3\varepsilon/2$'])
ax.set_yticks([0,eps/2,eps,3*eps/2],['0',r'$\varepsilon/2$',r'$\varepsilon$',r'$3\varepsilon/2$'])
ax.spines[['top','right']].set_visible(False);ax.set_xlabel(r'$x$',loc='right');ax.set_ylabel(r'$y$',loc='top',rotation=0)
ax.text(eps,.02*eps,r'$A\text{ edge}$' if False else 'A edge',ha='center',va='bottom',fontsize=10)
ax.text(.03*eps,eps,'B edge',rotation=90,va='center',fontsize=10)
fig.text(.75,.89,'Original corner coordinates: equation (7.6)',ha='center',fontsize=13)
fig.text(.75,.52,'Numerical sample of the exact curve; all widths retain ε.',ha='center',fontsize=11.5)
fig.text(.5,.459,r'$D=C\cup_\gamma F(D_h^2),\qquad \operatorname{int}D\cap\left(\bigcup_\ell A_\ell\cup\bigcup_kB_k\right)=\varnothing$',ha='center',fontsize=19)
fig.text(.5,.398,'Avoiding the retained collar uses its interior, boundary and corner strata.',ha='center',fontsize=13.5)
fig.text(.21,.336,'Endpoint',ha='center',fontweight='bold');fig.text(.48,.336,'Oriented disk tangent pair',ha='center',fontweight='bold');fig.text(.8,.336,'Full appended-frame sign',ha='center',fontweight='bold')
for yy,label,pa,sign in [(.291,r'$p$',r'$(a_p,b_p)$',r'$-\sigma_p$'),(.244,r'$q$',r'$-(a_q,b_q)$',r'$\sigma_q$')]:
 fig.text(.21,yy,label,ha='center',fontsize=18);fig.text(.48,yy,pa,ha='center',fontsize=18);fig.text(.8,yy,sign,ha='center',fontsize=18)
fig.text(.5,.18,r'$\sigma_q=-\sigma_p\quad\Longrightarrow\quad\text{the two normal-frame orientations agree}$',ha='center',fontsize=17)
fig.text(.5,.12,r'$W^\perp=W-V(V^{\mathsf{t}}GV)^{-1}V^{\mathsf{t}}GW$',ha='center',fontsize=21)
fig.text(.5,.067,'The full original metric G and all mixed terms remain. Equations (7.9)–(7.13).',ha='center',fontsize=12.5)
fig.savefig(O/'whitney-boundary-and-signs.svg',metadata={'Date':'2026-10-10'},bbox_inches='tight')
plt.close(fig)

