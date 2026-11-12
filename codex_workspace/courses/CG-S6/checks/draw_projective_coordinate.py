"""The full coordinate comparison and its actual three-factor receiving map. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parents[1]/'assets'
plt.rcParams.update({'svg.hashsalt':'CG-S6-projective-coordinate','font.family':'DejaVu Sans','font.size':12})
fig,ax=plt.subplots(figsize=(14,9));ax.set(xlim=(0,14),ylim=(0,9));ax.axis('off')
ink='#18323d';teal='#157b8b';purple='#75539a'
def tx(x,y,s,sz=13,c=ink,weight='normal'):ax.text(x,y,s,ha='center',va='center',fontsize=sz,color=c,weight=weight)
def ar(a,b,c=teal):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.8,'color':c})
tx(7,8.62,'The full formal coordinate and the actual projective comparison',19,weight='bold')
tx(7,8.16,r'$R=\mathbb{F}_2[u]/(u^3),\quad h(t)=t+ut^3,\quad h^{-1}(t)=t+ut^3+u^2t^5$',16)
tx(2.7,7.43,r'$F(x,y)$',18);tx(10.8,7.43,r'$h(x)+h(y)$',18)
ar((3.8,7.43),(9.05,7.43));tx(6.5,7.70,r'$h$',15,c=teal)
ar((9.05,7.09),(3.8,7.09),purple);tx(6.5,6.84,r'$h^{-1}$',15,c=purple)
tx(7,6.29,r'$F=x+y+u(x^2y+xy^2)+u^2(x^4y+x^3y^2+x^2y^3+xy^4)$',15)
tx(7,5.85,'This is the entire original law: all further contributions contain the actual zero factor u³.',11)
ax.plot([.35,13.65],[5.45,5.45],color='#ccd6dc')
tx(7,5.07,r'Actual spectrum $H_1\wedge H_2\wedge H_3$, with $H=H\mathbb{F}_2$',16,weight='bold')
tx(2,4.29,r'$x_1$',21);tx(7,4.29,r'$x_2$',21);tx(12,4.29,r'$x_3$',21)
ar((2.5,4.29),(6.5,4.29));ar((7.5,4.29),(11.5,4.29),purple)
tx(4.5,4.68,r'$f_{12}$',15,c=teal);tx(9.5,4.68,r'$f_{23}$',15,c=purple)
tx(7,3.63,r'$x_3=f_{23}(f_{12}(x_1))$',17)
tx(7,2.90,r'$\Delta\xi_n^{\rm act}=\sum_{i=0}^{n}(\xi_{n-i}^{\rm act})^{2^i}\otimes\xi_i^{\rm act}$',20)
tx(7,2.24,r'Both endpoints remain: $\xi_n^{\rm act}\otimes1$ and $1\otimes\xi_n^{\rm act}$.',12)
tx(7,1.70,r'$\beta(x)=x^2,\qquad b_0(\xi_1^{\rm act})=\overline{1}\otimes2$',17,c=teal)
tx(7,1.18,'The polynomial-to-cooperation morphism is constructed; its bijectivity is still to be proved.',11)
tx(7,.66,'Proofs: formal-coordinate text, (4.3)–(4.4); projective-cooperation text, (4.1)–(4.5), (5.1)–(5.6).',9)
tx(7,.26,'Human context: Luecke, arXiv:2109.00048v2; Peterson, FormalGeomNotes, mo.tex 32–241.',9)
fig.tight_layout(pad=.6)
fig.savefig(W/'projective-coordinate.svg',metadata={'Date':None})
plt.close(fig)
print('Rendered full coordinate comparison and actual projective coproduct.')
