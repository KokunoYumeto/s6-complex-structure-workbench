from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1];O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-MORSE-20261009'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(12,6),gridspec_kw={'width_ratios':[1.1,1]})
u=np.linspace(-2,2,1801);bump=np.zeros_like(u);mask=np.abs(u)<1
bump[mask]=4*np.exp(-1/(1-u[mask]**2))
ax.plot(u,u+bump,color='#24637d',lw=2.5,label=r'$h(u)=u+\delta(u)$')
ax.plot(u,u,color='#c36435',lw=2.2,label=r'$h_1(u)=u$')
ax.fill_between(u,u,u+bump,color='#d9e8ed',alpha=.85)
ax.set_xlabel(r'$u$');ax.set_ylabel('function value');ax.set_xlim(-2,2);ax.set_ylim(-2.2,2.4)
ax.grid(alpha=.2);ax.legend(loc='upper left');ax.set_title('Lower the arc; keep its endpoints',fontsize=14)
ax.annotate(r'$\delta=h-h_1$',xy=(.15,.7),xytext=(-1.45,.3),arrowprops={'arrowstyle':'->','color':'#555'},fontsize=12)
bx.axis('off');bx.set_xlim(0,1);bx.set_ylim(0,1)
bx.set_title('Why no transverse critical points appear',fontsize=13)
lines=[(.86,r'$R(u)^2=h(u)-a$'),(.73,r'$0\leq\delta/R^2\leq\rho<1$'),(.60,r'$-K<\beta^{\prime}\leq0,\quad\eta^{\prime}\leq0$'),(.44,r'$1+s(\delta/R^2)\beta^{\prime}\eta\geq1-\rho K>0$'),(.28,r'$1-s\delta\beta\eta^{\prime}\geq1$'),(.10,r'$\rho=3/5,\quad K=3/2:\quad 1-\rho K=1/10$')]
for yy,txt in lines:bx.text(.5,yy,txt,ha='center',va='center',fontsize=13 if yy!=.44 else 12)
fig.text(.5,.02,r'Sample: $a=-2$; $\delta(u)=4e^{-1/(1-u^2)}$ for $|u|<1$, and $0$ otherwise.  Proof: (3.6), (4.5), (5.4).',ha='center',fontsize=10)
fig.subplots_adjust(bottom=.17,wspace=.26,top=.88)
fig.savefig(O/'morse-supported-cutoff.svg',metadata={'Date':'2026-10-09'})
plt.close(fig)
print(str(O/'morse-supported-cutoff.svg'))
