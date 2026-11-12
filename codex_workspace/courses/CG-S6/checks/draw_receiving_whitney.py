from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1]
O=W/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path','svg.hashsalt':'CG-S6-RECEIVING-WHITNEY-20261010'})
fig=plt.figure(figsize=(14,10))
fig.text(.5,.955,'The exact Whitney move in the receiving dimensions',ha='center',fontsize=19,fontweight='bold')
fig.text(.5,.912,r'Core section $z_A=z_B=0$, with $R=3$ and $d_0=2$. The fixed comparison sheet is $y=0$.',ha='center',fontsize=13)
xx=np.linspace(-3,3,501)
for col,t in enumerate([0,.5,1]):
 ax=fig.add_axes([.065+.318*col,.55,.275,.295])
 ax.axhline(0,color='#2e7659',lw=2,label=r'$B_0$')
 ax.plot(xx,(1-t)*(9-xx**2)-2*t,color='#925578',lw=3,label=r'$A_t$ core')
 ax.set_xlim(-3.3,3.3);ax.set_ylim(-3,10);ax.set_xlabel('$x$');ax.set_ylabel('$y$')
 ax.spines[['top','right']].set_visible(False);ax.set_title(['t = 0: two intersections','t = 1/2: two intersections','t = 1: no intersections'][col],pad=10,fontsize=13)
 ax.set_xticks([-3,0,3]);ax.set_yticks([-2,0,5,9])
 if t<9/11:
  a=np.sqrt(9-2*t/(1-t))
  ax.scatter([-a,a],[0,0],s=52,color='#202d35',zorder=5)
  for at,txt in [(-a,'−'),(a,'+')]:ax.annotate(txt,(at,0),(at,-2.0),ha='center',fontsize=17,color='#925578')
 ax.grid(alpha=.17)
fig.text(.5,.472,r'$f_t(x)=(1-t)(9-x^2)-2t,\qquad t_*=\frac{9}{11},\qquad\det(TA_t,TB_0)=(-1)^p[-2(1-t)x]$',ha='center',fontsize=20)
fig.text(.5,.425,'The signs shown are for p = 3. For p = 2 both signs reverse. Other normal directions remain in the full map.',ha='center',fontsize=12)
fig.text(.075,.335,'All three receiving cases',fontsize=16,fontweight='bold')
fig.text(.075,.282,'Level d     Sheet p     Belt q     Disk normal rank',fontsize=12)
fig.text(.095,.235,'5                 2               3                    3',fontsize=14)
fig.text(.095,.19,'6                 2               4                    4',fontsize=14)
fig.text(.095,.145,'6                 3               3                    4',fontsize=14)
fig.text(.65,.335,'Full rank-four frame extension',ha='center',fontsize=16,fontweight='bold')
fig.text(.65,.272,r'$e=nQT,\qquad\rho(a,b)x=axb^{-1}$',ha='center',fontsize=20)
fig.text(.65,.216,r'$\epsilon(Q)=+1\ \Longleftrightarrow\ e\ \mathrm{extends}$',ha='center',fontsize=20)
fig.text(.65,.16,'One supported full rotation in the free block changes ε.\nThe complete triangular matrix T and the original Gram terms remain.',ha='center',fontsize=12)
fig.text(.5,.059,'The plots show the exact core equation on −R ≤ x ≤ R, not the whole ambient manifold.\nProof: Sections 2–4, especially (2.3), (3.8)–(3.12), (4.16)–(4.25), and Exercise 2.\nHuman source: Benedetti, arXiv:1907.10297v1, original-author TeX 15077–15409 (bounded reading).',ha='center',fontsize=10)
fig.savefig(O/'receiving-whitney-flow-and-full-frame.svg',metadata={'Date':None})
print(str(O/'receiving-whitney-flow-and-full-frame.svg'))
