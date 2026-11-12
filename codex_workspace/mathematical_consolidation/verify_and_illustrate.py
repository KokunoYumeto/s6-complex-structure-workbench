import hashlib
import json
import pathlib
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent
FIG = ROOT/'figures'
FIG.mkdir(exist_ok=True)
P = sp.Matrix([[1,-1,0],[0,1,-1]])
u = sp.ones(3,1)
C = P*P.T
R = P.T*C.inv()
X = R.row_join(u)
D = X.T*X
checks = {}
def check(name, assertion):
    if not assertion:
        raise AssertionError(name)
    checks[name] = True
check('original determinant X equals one',X.det()==1)
check('original inverse marking',X.inv()==P.col_join(u.T/3))
check('D retains C inverse and factor three',D==sp.diag(C.inv(),3))
check('D determinant equals one',D.det()==1)
check('PR is I and Pu is zero',P*R==sp.eye(2) and P*u==sp.zeros(2,1))
rs = sp.symbols('r',positive=True)
Hr = P.T*C.inv()*P+(rs/3)*u*u.T
check('full precision witness',X.T*Hr*X==sp.diag(C.inv(),3*rs))
check('hidden original covariance factor',sp.simplify((u.T*Hr.inv()*u)[0]-3/rs)==0)
check('example full cubic and beta squared',(sp.Rational(104,59)*sp.Rational(59,4)-20)==6 and (2*sp.sqrt(5))**2==20)
check('exact averaged Gaussian mass at repaired example',sp.simplify(6/(sp.Integer(36)-20)**sp.Rational(3,2)-sp.Rational(3,32))==0)
check('exact mean-substitution ratio',sp.Rational(3,32)/(sp.Rational(1,36))==sp.Rational(27,8))

def left(q):
    a,b,c,d=q
    return np.array([[a,-b,-c,-d],[b,a,-d,c],[c,d,a,-b],[d,-c,b,a]],float)
def qmul(a,b):
    return left(a)@b
def qbar(a):
    return a*np.array([1,-1,-1,-1])
def realify(H):
    return np.block([[left(H[i,j]) for j in range(len(H))] for i in range(len(H))])
def cubic(H):
    a,b,lam=H[0,0,0],H[1,1,0],H[2,2,0]
    v,p,q=H[0,1],H[0,2],H[1,2]
    return a*b*lam-lam*np.dot(v,v)-b*np.dot(p,p)-a*np.dot(q,q)+2*qmul(qmul(qbar(p),v),q)[0]
rng=np.random.default_rng(20260929)
max_cubic_error=0.
for k in range(12):
    H=np.zeros((3,3,4))
    for i in range(3):
        H[i,i,0]=8+i
        for j in range(i+1,3):
            H[i,j]=rng.normal(size=4)/3
            H[j,i]=qbar(H[i,j])
    A=realify(H)
    check('positive full real example '+str(k),np.linalg.eigvalsh(A)[0]>0)
    max_cubic_error=max(max_cubic_error,abs(np.linalg.det(A)**.25/cubic(H)-1))
    x=rng.normal(size=12)
    Psi=np.linalg.inv(np.kron(np.array(X,float),np.eye(4)))@A@np.linalg.inv(np.kron(np.array(X.T,float),np.eye(4)))
    B=np.kron(np.array(X.T,float),np.eye(4))@A@np.kron(np.array(X,float),np.eye(4))
    Dr=np.kron(np.array(D,float),np.eye(4))
    check('two complete real markings '+str(k),np.allclose(B,Dr@Psi@Dr,rtol=1e-12,atol=1e-12))
check('full quaternionic cubic agrees with real determinant',max_cubic_error<1e-11)

angles=np.linspace(0,2*np.pi,65536,endpoint=False)
mass_quadrature=np.mean(np.pi**6/(6-2*np.sqrt(5)*np.cos(angles))**2)
check('independent circle quadrature for full pi factor',abs(mass_quadrature/(3*np.pi**6/32)-1)<1e-12)
A=np.diag(np.repeat([2.,3.,5.],4))
Sigma=.5*np.linalg.inv(A)
B=rng.normal(size=(6,12))
diff=B[:,None,:]-B[None,:,:]
distance=np.einsum('abi,ij,abj->ab',diff,np.linalg.inv(A),diff)
phase=np.exp(-.7**2*distance/4)
check('coherence Gram matrix is positive',np.linalg.eigvalsh(phase)[0]>-1e-12)
tau,s=.7,.4
check('static semigroup fails at nonzero noise',not np.allclose(np.exp(-(tau+s)**2*distance/4),np.exp(-tau**2*distance/4)*np.exp(-s**2*distance/4)))
check('static propagator reproduces later channel',np.allclose(np.exp(-(tau**2-s**2)*distance/4)*np.exp(-s**2*distance/4),np.exp(-tau**2*distance/4)))
clock=3.
check('clocked Brownian semigroup composition',np.allclose(np.exp(-clock*(tau+s)*distance/4),np.exp(-clock*tau*distance/4)*np.exp(-clock*s*distance/4)))
Sroot=np.diag(np.sqrt(np.diag(Sigma)))
L=np.sqrt(clock)*B@Sroot
check('all GKLS factor constants',np.allclose(.5*np.sum((L[:,None,:]-L[None,:,:])**2,axis=-1),clock*distance/4))
recovered=np.zeros((12,12))
for i in range(12):
    recovered[i,i]=Sigma[i,i]
    for j in range(i):
        e=np.eye(12)[i]+np.eye(12)[j]
        recovered[i,j]=recovered[j,i]=(e@Sigma@e-Sigma[i,i]-Sigma[j,j])/2
check('tomographic polarization recovers full covariance',np.allclose(recovered,Sigma))

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12,4.6))
m=np.linspace(2*np.sqrt(5)+.05,12,700)
axes[0].plot(m,np.pi**6*m/(m*m-20)**1.5,label=r'Exact average $\pi^6m/(m^2-20)^{3/2}$',lw=2.4)
axes[0].plot(m,np.pi**6/m**2,label=r'Mean substitution $\pi^6/m^2$',lw=2,ls='--')
axes[0].axvspan(0,2*np.sqrt(5),color='#f0c3bd',alpha=.45)
axes[0].axvline(2*np.sqrt(5),color='#98443a',lw=1.4)
axes[0].set_yscale('log');axes[0].set_xlim(0,12);axes[0].set_ylim(6,5000)
axes[0].set_xlabel(r'Original $m=\lambda(59/4)-20$')
axes[0].set_ylabel(r'Gaussian mass $Z$ with the full $\pi^6$ factor')
axes[0].set_title('R3: positive fibres and finite mass')
axes[0].text(.3,800,'Positive part exists;\naverage is infinite',fontsize=10)
axes[0].scatter([6],[3*np.pi**6/32],c='#174d70',zorder=4)
axes[0].annotate(r'$m=6:\ 3\pi^6/32$',(6,3*np.pi**6/32),(7,180),arrowprops={'arrowstyle':'->'},fontsize=10)
axes[0].legend(loc='lower left',fontsize=8)
t=np.linspace(0,8,500)
axes[1].plot(t,np.exp(-t*t/8),label=r'Static $e^{-\tau^2/8}$',lw=2.4)
axes[1].plot(t,np.exp(-3*t/8),label=r'Brownian, $\tau_c=3$: $e^{-3\tau/8}$',lw=2,ls='--')
axes[1].set_xlabel(r'Original time $\tau$');axes[1].set_ylabel('Coherence magnitude')
axes[1].set_title(r'R5–R6: $H=\mathrm{diag}(2,3,5)$')
axes[1].text(3.1,.83,r'$b_0=0,\ b_1=e_1,\ E_0=E_1$',fontsize=10)
axes[1].legend(fontsize=9)
fig.tight_layout()
for ext in ['png','svg','pdf']:fig.savefig(FIG/('mass_and_time_laws.'+ext),dpi=190)
plt.close(fig)

fig,ax=plt.subplots(figsize=(12,6));ax.axis('off')
boxes=[
(.01,.68,.27,.22,r'Original parameter $H>0$'+'\n'+r'$N(H),\ Z(H)=\pi^6/N(H)^2$'),
(.39,.68,.27,.22,r'Jordan marking $\Psi$'+'\n'+r'$\Psi=X^{-1}HX^{-*}$'),
(.75,.68,.24,.22,r'Sample precision $B$'+'\n'+r'$B=X^*HX=D\Psi D$'),
(.01,.28,.27,.22,r'Original sample $q\in\mathbb{H}^3$'+'\n'+r'$d^{12}q;\ \xi=X^*q$'),
(.39,.28,.27,.22,r'Observation $y=Pq\in\mathbb{H}^2$'+'\n'+r'Affine sample fibre: real dimension 4'),
(.75,.28,.24,.22,r'Parameters $(S,c,\ell)$'+'\n'+r'$H\mapsto S$: real dimension 9 fibres'),
]
for x,y,w,h,label in boxes:
    ax.add_patch(plt.Rectangle((x,y),w,h,fc='#edf3f7',ec='#274b67',lw=1.4,transform=ax.transAxes))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=11,transform=ax.transAxes)
for start,end in [((.28,.79),(.39,.79)),((.66,.79),(.75,.79)),((.28,.39),(.39,.39)),((.87,.68),(.87,.50))]:
    ax.annotate('',xy=end,xytext=start,xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.7})
ax.text(.33,.84,'R2',ha='center',transform=ax.transAxes)
ax.text(.705,.84,r'$D=X^*X$',ha='center',fontsize=10,transform=ax.transAxes)
ax.text(.50,.12,'Fixed c and ell, varying S: six-dimensional KL equality family.\nFixed S, varying c and ell: nine-dimensional parameter fibre.\nThe metric-map residual fibre is a separate four-circle object (R3).',ha='center',fontsize=12,transform=ax.transAxes)
fig.tight_layout()
for ext in ['png','svg','pdf']:fig.savefig(FIG/('exact_maps.'+ext),dpi=190)
plt.close(fig)
receipt={'checks':checks,'exact_arithmetic':'SymPy rational matrices and original factors','numerical_checks':'deterministic full quaternionic coordinates, direct circle quadrature and finite channel matrices; evidence only, not proof substitutes','max_relative_cubic_error':max_cubic_error,'mass_circle_quadrature':mass_quadrature,'figures':[{'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(FIG.iterdir()) if p.is_file()]}
(ROOT/'MATHEMATICAL_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'figures':len(receipt['figures']),'max_relative_cubic_error':max_cubic_error}))
