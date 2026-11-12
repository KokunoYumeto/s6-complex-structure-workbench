from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1];O=W/'assets'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'CG-S6-NORMAL-FRAME-20261009','font.size':13})
fig=plt.figure(figsize=(12,8));ax=fig.add_axes([.06,.39,.46,.45]);ax.set_aspect('equal');ax.axis('off')
t=np.linspace(0,1,501);x=np.cos(np.pi*t);y=np.sin(np.pi*t)
ax.plot(x,y,color='#26717c',lw=3)
ax.annotate('',xy=(x[285],y[285]),xytext=(x[245],y[245]),arrowprops={'arrowstyle':'->','color':'#26717c','lw':3})
ax.scatter([1,-1],[0,0],s=65,color=['#26717c','#ab463d'])
ax.text(1,-.13,r'$+1$',ha='center',fontsize=17);ax.text(-1,-.13,r'$-1$',ha='center',fontsize=17)
ax.text(0,1.21,r'$\widetilde T(t)=\cos(\pi t)+\mathbf{i}\sin(\pi t)$',ha='center',fontsize=18)
ax.text(0,-.38,r'$(q_0,q_1,q_2,q_3)=(\cos\pi t,\sin\pi t,0,0)$',ha='center',fontsize=13.5)
ax.set_xlim(-1.3,1.3);ax.set_ylim(-.5,1.5)
fig.text(.5,.94,'A full rotation changes the normal-frame extension sign',ha='center',fontsize=18,fontweight='bold')
fig.text(.76,.77,'Downstairs: the frame returns',ha='center',fontsize=16)
fig.text(.76,.69,r'$T(0)=T(1)=I_3$',ha='center',fontsize=21)
fig.text(.76,.58,'Upstairs: the lift changes sheet',ha='center',fontsize=16)
fig.text(.76,.5,r'$\widetilde T(0)=1,\quad\widetilde T(1)=-1$',ha='center',fontsize=20)
fig.text(.5,.32,r'$e^\prime=eT,\qquad e^\prime_1=e_1,\qquad\epsilon(e^\prime)=-\epsilon(e)$',ha='center',fontsize=23)
fig.text(.5,.23,'The first normal vector is fixed; the last two rotate through their original plane.',ha='center',fontsize=14)
fig.text(.5,.16,'Exactly one frame extends. Section 7 proves the permitted directions on the Whitney boundary.',ha='center',fontsize=13)
fig.text(.5,.065,'Exact unit-quaternion slice, not a projection of an unspecified path. Equations (6.6)–(6.13).',ha='center',fontsize=12)
fig.savefig(O/'normal-frame-extension.svg',metadata={'Date':'2026-10-09'},bbox_inches='tight')
plt.close(fig)

