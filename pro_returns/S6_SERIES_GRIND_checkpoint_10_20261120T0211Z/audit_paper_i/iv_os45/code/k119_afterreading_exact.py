#!/usr/bin/env python3
"""Fresh exact reconstruction after reading all four K119 supporting proofs.

This program imports no historical checker and no preceding audit program.
It checks rational source identities and the actual integral comparison maps;
the written review separately checks their analytic and geometric use.
"""
from pathlib import Path
from functools import reduce
import json, time, hashlib, platform
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from sympy.combinatorics.free_groups import free_group

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / 'output'
start = time.monotonic()
checks = []

def ck(name, condition):
    assert condition, name
    checks.append(name)

def zero(expr):
    return sp.cancel(expr) == 0

def mat(A):
    return [[str(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]

def smith(A):
    D = smith_normal_form(A, domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

def sum_mat(items, n=4, m=4):
    return sum(items, sp.zeros(n,m))

u,v,a,t,x,y,xi,q,h,S,c,p,Z,sg = sp.symbols('u v a t x y xi q h S c p Z sg')
R=t*t+a
f=R**2+t
g=R**3+sp.Rational(3,2)*t*R+sp.Rational(3,8)
D=sp.expand(64*(g*g-f**3))
cap_a=16*a**3+3
aa=-u/3-u**4/9
tc=1/(2*u)-u*u/3
cap=2187-16*u**3*(u**3+3)**3
unselected=8*u**9+84*u**6+342*u**3+729
ck('literal source finite discriminant', zero(D-48*a*(t*t+a)**2-8*t**3-72*a*t-9))
ck('cap locus pullback without scaling change', zero(729*cap_a.subs(a,aa)-cap))
ck('cap factorization', sp.expand(cap+(2*u**3-3)*unselected)==0)
ck('twelve distinct nonzero u values', sp.degree(cap,u)==12 and sp.gcd(cap,sp.diff(cap,u))==1 and cap.subs(u,0)!=0)
ck('six selected marked points', sp.degree(2*u**3-3,u)==3 and zero(tc+(2*u**3-3)/(6*u)))
ck('eighteen unselected marked points', sp.degree(unselected,u)==9 and sp.gcd(unselected,2*u**3-3)==1)
bezout={}
for name,other in [('u_zero',u),('a_zero',u**3+3),('ordered_branch',4*u**3+3),('unselected_II',16*u**6+120*u**3+243)]:
    A,B,C=sp.gcdex(cap,other,u)
    ck('exact boundary disjointness '+name, C==1 and sp.expand(A*cap+B*other)==1)
    bezout[name]={'A':str(A),'B':str(B),'other':str(other)}
ck('ordered cover unramified at all cap roots', sp.gcd(cap,4*u**3+3)==1)
ck('parameter a derivative', sp.diff(aa,u)==-(4*u**3+3)/9)
ck('node t derivative', sp.diff(D,t).subs(t,0)==72*a)
ck('node a derivative', sp.diff(D,a).subs(t,0)==144*a*a)
ck('implicit moving height derivative', zero(-sp.diff(D,a).subs(t,0)/sp.diff(D,t).subs(t,0)+2*a))
ck('cap cubic factorization', sp.rem(sp.expand(x**3-3*f.subs(t,0)*x+2*g.subs(t,0)-(x+a)**2*(x-2*a)),cap_a,a)==0)
ck('all remaining finite nodes simple', sp.factor(sp.discriminant(D,t))==331776*(256*a**3-3)**3 and sp.gcd(cap_a,256*a**3-3)==1)

# The actual q-dependent square-root chart, with its inverse.
# Write f=xi^2, g=xi^3+qh/2. This is exactly the defining relation for h.
source_y2=x**3-3*xi**2*x+2*xi**3+q*h
ck('full q-dependent node product', sp.expand(source_y2-(x-xi)**2*(x+2*xi)-q*h)==0)
X,Y,B=sp.symbols('X Y B')
Xp=y-(x-xi)*B
Yp=(y+(x-xi)*B)/h
ck('node XY=q after original source relation', zero(sp.expand(Xp*Yp).subs(B**2,x+2*xi).subs(y**2,source_y2)-q))
ck('node inverse y', zero((Xp+h*Yp)/2-y))
ck('node inverse x equation', zero(h*Yp-Xp-2*(x-xi)*B))
ck('node inverse tangent nonzero square', sp.diff(2*(x-xi)*sp.sqrt(x+2*xi),x).subs(x,xi)**2==12*xi)
xi_t=-1/(2*a)
h0=2*(sp.diff(g,t).subs(t,0)-3*a*a*xi_t)
ck('full node unit h at cap', sp.simplify(h0-6*a)==0)
kap_from_j=-sp.diff(D,t).subs(t,0)/(64*1728*f.subs(t,0)**3)
ck('original height inverse-j coefficient', sp.rem(sp.together(kap_from_j-1/(288*a*a)).as_numer_denom()[0],cap_a,a)==0)
ck('node unit and inverse-j coefficient agree', sp.rem(sp.together(-h0/(1728*(-a)**3)-1/(288*a*a)).as_numer_denom()[0],cap_a,a)==0)
ck('central normalization actual source', sp.rem(sp.expand((S*(S*S+3*a))**2-((S*S+2*a)**3-3*a*a*(S*S+2*a)+2*(a**3+sp.Rational(3,8)))),cap_a,a)==0)
sg0=sp.sqrt(3)/(4*a)
ck('original G normalization square', sp.rem(sp.together(sg0**2+a).as_numer_denom()[0],cap_a,a)==0)
ck('original G x coordinate', sp.rem(sp.together(sg0**2+2*a-a).as_numer_denom()[0],cap_a,a)==0)
ck('original G y coordinate', sp.rem(sp.together(sg0*(sg0**2+3*a)-sp.sqrt(3)/2).as_numer_denom()[0],cap_a,a)==0)
for eps in [-1,1]:
    pp=sp.simplify((1-eps*sp.sqrt(3))/(1+eps*sp.sqrt(3)))
    ck('ordered branch P '+str(eps), sp.simplify(pp-(-2+eps*sp.sqrt(3)))==0)
    ck('nonidentity real branch P '+str(eps), pp.is_real and pp!=0 and pp!=1 and sp.simplify(pp*pp-1)!=0)
ck('opposite branch reciprocal', sp.simplify((-2+sp.sqrt(3))*(-2-sp.sqrt(3)))==1)

# Reconstruct the original tangent recursion before using the point module.
xS=S*S-sp.Rational(2,3)*c*c
yS=S*(S*S-c*c)
sj=sp.symbols('sj', nonzero=True)
s2j=(sj*sj+c*c)/(2*sj)
slope=(3*sj*sj-c*c)/(2*sj)
tangent=sp.expand(yS-yS.subs(S,sj)-slope*(xS-xS.subs(S,sj)))
ck('actual tangent factorization', zero(tangent-(S-sj)**2*(S+s2j)))
ck('actual doubling vertical factorization', zero(xS-xS.subs(S,s2j)-(S-s2j)*(S+s2j)))
ck('exact tangent quotient', zero(tangent/(xS-xS.subs(S,s2j))-(S-sj)**2/(S-s2j)))
sgp=c*(1+p)/(1-p)
fm={}
prev=sp.Integer(1)
for j in [1,2,4]:
    sjp=c*(1+p**j)/(1-p**j)
    snext=c*(1+p**(2*j))/(1-p**(2*j))
    ck('source double uses literal P power '+str(j), zero((sjp*sjp+c*c)/(2*sjp)-snext))
    fm[2*j]=(S-sgp)**(2*j)/(S-snext)
    ck('chronological tangent recursion f'+str(2*j), zero(prev**2*(S-sjp)**2/(S-snext)-fm[2*j]))
    # Compare to the printed expression only after deriving the recursion.
    printed=(-2*c)**(2*j-1)*(1-p**(2*j))/(1-p)**(2*j)*(Z-p)**(2*j)/((Z-p**(2*j))*(Z-1)**(2*j-1))
    ck('full Z expression f'+str(2*j), zero(fm[2*j].subs(S,c*(1+Z)/(1-Z))-printed))
    ck('same values at both node branches f'+str(2*j), zero(fm[2*j].subs(S,c)-fm[2*j].subs(S,-c)))
    prev=fm[2*j]
T=(sg*S-c*c)/(sg-S)
ck('translation has literal Z/P direction', zero((T-c)/(T+c)-((S-c)/(S+c))/((sg-c)/(sg+c))))
f2=(S-sg)**2/(S-(sg*sg+c*c)/(2*sg))
kernel=sp.cancel(f2*(T-sg)/(S-sg))
ck('chronological cancellation kernel', kernel==-2*sg)
s8=c*(1+p**8)/(1-p**8)
BB=kernel**8*(S-s8)/(T-s8)
BBz=sp.factor(BB.subs(sg,sgp).subs(S,c*(1+Z)/(1-Z)))
BBprinted=(-2*sgp)**8*(Z-p)*(Z-p**8)/((Z-p**9)*(Z-1))
ck('complete chronological B8,1', zero(BBz-BBprinted))
fpoint=lambda zz:(1-zz/p**8)/(1-zz)
ck('point-module directed cancellation', zero(BBprinted*fpoint(Z/p)/fpoint(Z)-(-2*sgp)**8))
inverse_coeff=1/BBprinted.subs(Z,Z*p)
ck('actual inverse at inverse source point', zero(inverse_coeff.subs(Z,Z/p)*BBprinted-1))
ck('cap coefficient 9/a^2', sp.rem(sp.together((-2*sg0)**8-9/a**2).as_numer_denom()[0],cap_a,a)==0)
ck('infinity nonidentity point 16/27', sp.rem(sp.together(-1/(9*a**3)-sp.Rational(16,27)).as_numer_denom()[0],cap_a,a)==0)

# Full units stay present under the infinity frame change and translation.
Q,b,Aunit,Dunit=sp.symbols('Q b Aunit Dunit',nonzero=True)
theta_factor=sp.Integer(1)
for j in range(1,4):
    theta_factor*=-(Z/b)/Q**j
ck('three exact theta reindexes', zero(theta_factor-(-Z/b)**3*Q**-6))
ck('full infinity translation coefficient', zero(Dunit*theta_factor/theta_factor.subs(Z,Aunit*Z)-Dunit*Aunit**-3))
period_word=sp.Matrix([[-1,3],[-3,8]])
ck('infinity exact integer period inverse', period_word.inv()==sp.Matrix([[8,-3],[3,-1]]))
ck('infinity primitive source valuation', sp.Matrix([[8,-3]])*period_word==sp.Matrix([[1,0]]))
ck('point-module full forward inverse composition', zero((Dunit*fpoint(Z)/fpoint(Aunit*Z))*(Dunit**-1*fpoint(Aunit*Z)/fpoint(Z))-1))

# Literal source cohomology matrices, followed by independent inversion.
Ts=[
sp.Matrix([[1,0,3,9],[0,1,8,24],[0,0,1,0],[0,0,0,1]]),
sp.Matrix([[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]]),
sp.Matrix([[1,2,6,32],[0,4,9,48],[0,-1,-2,-16],[0,0,0,1]]),
sp.Matrix([[1,1,0,8],[0,1,0,0],[0,-1,1,-8],[0,0,0,1]]),
sp.Matrix([[1,0,0,-1],[0,-2,9,0],[0,-1,4,0],[0,0,0,1]])]
e=[sp.eye(4)[:,i] for i in range(4)]
local_generators=[e[2]+3*e[3],e[2],e[1]+3*e[2]+16*e[3],e[1]+8*e[3],e[1]-3*e[2]]
selected_preimages={1:e[0],2:e[0]+2*e[2],3:e[0]+e[2],4:e[0]}
Dprinted=sp.Matrix([[-3,-8,0,0],[0,-1,0,0],[-2,-3,1,0],[-1,0,1,0],[0,3,1,0],[1,0,0,0]])
Bprinted=sp.Matrix([[0,0,0,0,0,0],[0,0,1,-2,1,0],[1,1,-6,9,-3,0],[3,0,-8,8,0,1]])
L=sp.Matrix([[0,0,0,0,0,1],[0,-1,0,0,0,0],[0,0,0,1,0,1]])
J=sp.Matrix([[-24,-8,3],[0,0,0],[-9,-3,1],[0,0,0],[10,3,-1],[0,0,0]])
site_records={}
for selected in range(1,5):
    Tsite=[T.copy() for T in Ts]
    if selected!=4:
        Tsite[4][0,3]+=1
        Tsite[selected][0,3]-=1
    H=[T.inv().T for T in Tsite]
    N=[H0-sp.eye(4) for H0 in H]
    P=[sp.eye(4)]
    for H0 in H:P.append(P[-1]*H0)
    M=[P[i]*N[i] for i in range(5)]
    ck('homology product identity site '+str(selected), P[-1]==sp.eye(4))
    ck('twenty exact inverse transposes site '+str(selected), all(Tsite[i].T*H[i]==sp.eye(4) for i in range(5)))
    ck('telescoping based columns site '+str(selected), all(M[i]==P[i+1]-P[i] for i in range(5)))
    ck('full source/physical preimages site '+str(selected), N[selected]*selected_preimages[selected]==e[3] and N[1]*(-e[1])==e[2] and N[3]*e[2]==e[1]+8*e[3])
    Drows=[]
    for i in range(5):
        G=local_generators[i]
        if i==selected:G=G.row_join(e[3])
        coords=G.gauss_jordan_solve(N[i])[0]
        ck('integral local image coordinates '+str((selected,i)), all(x.q==1 for x in coords))
        ck('primitive entire local image '+str((selected,i)), smith(coords)==[1]*G.cols)
        Drows.append(coords[0,:])
        if i==selected:extra=coords[1,:]
    Dactual=sp.Matrix.vstack(*Drows,extra)
    Bactual=sp.Matrix.hstack(*[P[i]*local_generators[i] for i in range(5)],P[selected]*e[3])
    ck('literal D from full source matrices site '+str(selected), Dactual==Dprinted)
    ck('literal B from based generators site '+str(selected), Bactual==Bprinted)
    Dprime=Dactual[:,:3]
    Bprime=Bactual[1:,:]
    ck('full integral middle contraction site '+str(selected), Dprime*L+J*Bprime==sp.eye(6))
    ck('both integral splitting inverses site '+str(selected), L*Dprime==sp.eye(3) and Bprime*J==sp.eye(3))
    ck('differential square zero site '+str(selected), Bactual*Dactual==sp.zeros(4))
    ck('primitive degree-zero period kernel site '+str(selected), Dactual[:,3]==sp.zeros(6,1) and Dprime.rank()==3)
    ck('degree-two psi quotient with primitive section site '+str(selected), Bactual[0,:]==sp.zeros(1,6) and Bprime*J==sp.eye(3) and e[0][0]==1)
    # Twenty-dimensional upper-triangular raw-to-based coordinate map.
    U=sp.eye(20)
    for j in range(5):
        for i in range(j+1,5):U[4*j:4*j+4,4*i:4*i+4]=-N[i]
    Ui=sp.zeros(20)
    for j in reversed(range(5)):
        Ui[4*j:4*j+4,:]=sp.eye(20)[4*j:4*j+4,:]+sum_mat([N[i]*Ui[4*i:4*i+4,:] for i in range(j+1,5)],4,20)
    ck('complete twenty-dimensional inverse site '+str(selected), U*Ui==sp.eye(20) and Ui*U==sp.eye(20) and U.det()==1)
    raw=sp.Matrix.hstack(*N)
    based=sp.Matrix.hstack(*M)
    ck('complete raw to transported boundary map site '+str(selected), based*U==raw)
    Rmap=sp.zeros(20,3)
    Rmap[4:8,1]=-e[1]
    Rmap[12:16,0]=e[2]
    Rmap[4*selected:4*selected+4,0]+=-8*selected_preimages[selected]
    Rmap[4*selected:4*selected+4,2]+=selected_preimages[selected]
    target=sp.Matrix.hstack(e[1],e[2],e[3])
    ck('all retained source and physical differences site '+str(selected), raw*Rmap==target and based*U*Rmap==target)
    # Mapping-cone matrix in literal (four p blocks, five z blocks) order.
    cone=sp.zeros(20,36)
    for i in range(4):
        cone[4*i:4*i+4,4*i:4*i+4]=sp.eye(4)
        cone[16:20,4*i:4*i+4]=-H[4]*P[i]
    for i in range(5):cone[4*i:4*i+4,16+4*i:16+4*i+4]=-N[i]
    vstar=sp.Matrix.hstack(*P[:5])
    ck('complete exterior terms cancel in cone site '+str(selected), (vstar*cone)[:,:16]==sp.zeros(4,16))
    ck('complete local cone boundary sign site '+str(selected), (vstar*cone)[:,16:]==-based)
    zmap=-U*Rmap
    ck('positive cap-vector difference uses negative t site '+str(selected), (vstar*cone)[:,16:]*zmap==target)
    site_records[str(selected)]={'T':list(map(mat,Tsite)),'H':list(map(mat,H)),'P':list(map(mat,P)),'D':mat(Dactual),'B':mat(Bactual),'raw_to_based_U':mat(U),'inverse_U':mat(Ui),'raw_preimage_R':mat(Rmap),'based_preimage_UR':mat(U*Rmap),'cone_boundary':mat(cone),'vstar':mat(vstar)}

# Formal finite Laurent families check the full off-diagonal operator.
fc=sp.symbols('f_m5:6')  # 11 distinct symbolic coefficients
gc=sp.symbols('g_m7:8')  # 15 distinct symbolic coefficients
ac=sp.symbols('a_m3:4')  # 7 distinct symbolic coefficients
# Explicit indexed names avoid assumptions about symbol range syntax.
fc=sp.symbols(' '.join('f'+str(i+5) for i in range(-5,6)))
gc=sp.symbols(' '.join('g'+str(i+7) for i in range(-7,8)))
ac=sp.symbols(' '.join('a'+str(i+3) for i in range(-3,4)))
fv=sum(fc[i+5]*t**i for i in range(-5,6))
gv=sum(gc[i+7]*t**i for i in range(-7,8))
av=sum(ac[i+3]*t**i for i in range(-3,4))
u0=-sum(fc[i+5]*t**i for i in range(0,6))
uinf=sum(fc[i+5]*t**(i+1) for i in range(-5,0))
G=sp.expand(gv-av*uinf)
v0=-sum(G.coeff(t,i)*t**i for i in range(0,8))
vinf=sum(G.coeff(t,i)*t**i for i in range(-7,0))
ck('full Laurent source equation', sp.expand(t**-1*uinf-u0-fv)==0)
ck('full off-diagonal Laurent physical equation', sp.expand(av*uinf+vinf-v0-gv)==0)
ck('all infinity Laurent powers regular', all(term.as_powers_dict().get(t,0)<=0 for term in sp.Add.make_args(uinf)) and all(term.as_powers_dict().get(t,0)<0 for term in sp.Add.make_args(vinf)))

# Directed endpoint identities in a free, hence noncommutative, group.
FG,F0,F1,EX,EY,PY=free_group('F0 F1 EX EY PY')
C=F1*EX*F0**-1*EY**-1
ck('forward marked endpoint equality', F1*EX*F0**-1==C*EY)
ck('inverse marked endpoint equality without commutation', F0*EX**-1*F1**-1==EY**-1*C**-1)
ck('full inverse-endpoint return conjugacy', F0*(EX**-1*F1**-1*PY*F0)*F0**-1==EY**-1*C**-1*PY)

payload={'status':'PASS','checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family',
         'phase':'fresh execution after complete K119 OC45, OCP, OCGC and ORC proof reading',
         'check_count':len(checks),'checks':checks,'versions':{'python':platform.python_version(),'sympy':sp.__version__},
         'boundary_bezout_witnesses':bezout,'all_four_selected_sites':site_records,
         'scope':'Rational source and original-height node identities; three chronological Miller doublings; actual point coefficient and target-point inverse; complete infinity reindex; all four selected sites with full 20-by-20 raw/based map, integral image bases, splitting contraction, 20-by-36 mapping cone and sign; formal full-off-diagonal Laurent algebra; noncommutative endpoint composition. Analytic convergence, sheaf local extension, parameter regularity, properness and sphere transport are checked in the written review, not inferred from these symbolic tests.',
         'elapsed_seconds':time.monotonic()-start}
target=OUT/'k119_afterreading_exact.json'
target.write_text(json.dumps(payload,indent=2)+'\n')
summary={key:payload[key] for key in ['status','checker','phase','check_count','versions','elapsed_seconds']}
summary['output_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
print(json.dumps(summary,indent=2))
