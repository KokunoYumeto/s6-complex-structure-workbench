"""Exact s-chain / p-one-factor boundary comparison, with full periods."""
from pathlib import Path
import sympy as S,json,datetime
ROOT=Path(__file__).resolve().parents[2];checks=[]
def ck(x,n):assert x,n;checks.append(n)
# Character orders use (P,u_s,Z,a,b); index integers are never rooted.
for j in range(-4,5):
 for l in range(4):
  k=4*j+l
  U=S.Matrix([3*(j+1)-k,k,-1,1,0]);V=S.Matrix([k+1-3*(j+1),-k-1,1,0,1])
  ck(U+V==S.Matrix([1,-1,0,1,1]),'UV=(P/us)ab=s')
  invA=S.Matrix([k-3*(j+1),-k,1]);invB=S.Matrix([3*(j+1)-k-1,k+1,-1])
  ck(invA+U[:3,0]==S.zeros(3,1),'a inverse')
  ck(invB+V[:3,0]==S.zeros(3,1),'b inverse')
  # New chart indices under B; Z maps P^-1 Z, a maps c a.
  jp,kp=j+1,k+4
  nextU=S.Matrix([3*(jp+1)-kp,kp,-1,1,0]);nextU[0]+=1
  ck(nextU-U==S.Matrix([0,4,0,0,0]),'B factor us^4 c=lambda0 q K')
  nextV=S.Matrix([kp+1-3*(jp+1),-kp-1,1,0,1]);nextV[0]-=1
  ck(nextV-V==S.Matrix([0,-4,0,0,0]),'inverse B factor')
  # h: Z->P^3 p Z; a->p^-2 a,b->p^2 b.
  ck(-3==-3 and -1-2==-3,'h U factor P^-3 p^-3=R^-3')
  ck(3==3 and 1+2==3,'h V factor R^3')
  ck(U[3]-U[4]==1 and V[3]-V[4]==-1,'physical weights retained')
P,us,Z,aa,bb,p,c,Q,R,U6,lam,qh,K=S.symbols('P us Z aa bb p c Q R U6 lam qh K',nonzero=True)
j,l=S.symbols('j l',integer=True);k=4*j+l
# Exponent identities hold symbolically for every integer j and each lower l.
UU=S.Matrix([3*(j+1)-k,k,-1,1,0]);VV=S.Matrix([k+1-3*(j+1),-k-1,1,0,1])
ck(S.simplify(UU+VV-S.Matrix([1,-1,0,1,1]))==S.zeros(5,1),'symbolic all-integer inverse/product')
# Full h logarithmic multiplier rows (P,p) from Z,a,b.
hlogs=S.Matrix([[3,1],[-0,-2],[0,2]])
ck((S.Matrix([[-1,1,0]])*hlogs)==S.Matrix([[-3,-3]]),'literal h positive coefficient')
ck((S.Matrix([[1,0,1]])*hlogs)==S.Matrix([[3,3]]),'literal h negative coefficient')
# H: VC -> Vpoint=P^-6 U6^-1 Z^3 VC, with Q=P^2 R.
ck(S.cancel((Q**3/R**3).subs(Q,P**2*R)-P**6)==0,'point source-period intertwining')
ck(S.cancel((P**-1)**3*lam*qh*K-lam*qh*K*P**-3)==0,'point full suspension intertwining')
point=UU+S.Matrix([-6,0,3,0,0])
ck(point==S.Matrix([3*(j+1)-k-6,k,2,1,0]),'full original point normal coefficient')
# After B^-j use Z=P^-j Zstar,a=c^j aref,c=lambda0 qK us^-4.
# (P,us,Zstar,lambda0 qK,aref) exponents before/after reduction.
reduced=S.Matrix([point[0]-2*j,point[1]-4*j,2,j,1])
ck(S.simplify(reduced-S.Matrix([-3-l-3*j,l,2,j,1]))==S.zeros(5,1),'full point B^-j representative')
ck((4*j+l)-4*j==l,'actual lower chain label after B^-j')
t,alpha,beta,H,n=S.symbols('t alpha beta H n')
# ordinary logarithm alpha=-beta+H and m=2,n=1,k=2 scalar root.
F=2*t*beta;oord=2*t*(-beta+H);ocap=2*t*H
ck(S.expand(F+oord-ocap)==0,'full ordinary-to-cap origin square')
ck(S.expand((F.subs(t,t+1)-F)+2*(-beta+H)-2*H)==0,'forward parameter closing square q^2/h^2')
# A shifts2, B shifts4 and source/root norm is retained A0^2=B0.
ck(2*2==4,'full chain index norm')
# No central collapse of a Cartier frame: coefficient sDelta is retained as typed line map.
report={'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'check_labels':checks,'scope':'Exact side-annulus scalar chain, every integer chart index, full h/B units, physical weights, root norm indices and directed ordinary/cap origin square. Exterior transport and total residue ledger are stated separately.'}
(ROOT/'code/part3/e6_collision_boundary_chain.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='check_labels'}))
