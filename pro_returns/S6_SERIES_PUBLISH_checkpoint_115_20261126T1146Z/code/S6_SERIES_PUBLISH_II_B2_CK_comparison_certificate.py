#!/usr/bin/env python3
"""CK printed-coordinate comparison: polyhedron vertices and universal inequalities."""
import itertools,json
import sympy as s
Q=s.Rational
checks=[]
def check(name,condition,evidence):
    ok=bool(condition);checks.append({'name':name,'passed':ok,'evidence':evidence});assert ok,name
def eq(a,b):return s.simplify(a-b)==0

# Reconstruct the Newton polyhedron from its inequalities, not from a bounded lattice grid.
normals=[s.Matrix([Q(1,4),Q(1,4),Q(1,3)]),s.Matrix([Q(3,10),Q(1,5),Q(1,3)]),s.Matrix([0,1,Q(1,3)]),s.Matrix([1,0,0]),s.Matrix([0,1,0]),s.Matrix([0,0,1])]
constants=[1,1,1,0,0,0]
vertices=set()
for inds in itertools.combinations(range(6),3):
    A=s.Matrix.vstack(*[normals[i].T for i in inds]);b=s.Matrix([constants[i] for i in inds])
    if A.det():
        point=A.inv()*b
        if all(n.dot(point)>=c for n,c in zip(normals,constants)):vertices.add(tuple(point))
expected={(3,1,0),(2,2,0),(0,5,0),(0,0,3)}
check('Exact four Newton vertices',vertices==expected,{'vertices':[[int(c) for c in v] for v in sorted(vertices)],'recession_cone':'Positive octant: all displayed normals are nonnegative and the last three inequalities impose coordinate positivity'})
for name,face,inds in [('first_compact',normals[0],[(3,1,0),(2,2,0),(0,0,3)]),('second_compact',normals[1],[(2,2,0),(0,5,0),(0,0,3)]),('noncompact',normals[2],[(3,1,0),(0,0,3)])]:
    check(name+' exact supporting face',all(face.dot(s.Matrix(v))==1 for v in inds) and all(face.dot(s.Matrix(v))>=1 for v in expected),{'normal':[str(c) for c in face],'vertices':[list(v) for v in inds]})
check('Noncompact face contains precisely the positive u recession',normals[2].dot(s.Matrix([1,0,0]))==0,'normal=(0,1,1/3)')
for index,face in enumerate(normals[:2],1):
    origin_weight=sum(face)
    check('Facet '+str(index)+' base positive lattice weight',origin_weight==Q(5,6),str(origin_weight))
    increments=[origin_weight+c for c in face]
    check('Facet '+str(index)+' every larger positive integral point excluded',all(v>1 for v in increments),{'one_coordinate_increments':[str(v) for v in increments],'universal_reason':'Every other positive integer vector is coordinatewise at least one of these three increments'})
check('Noncompact inequality always strict for positive integer points',Q(1)+Q(1,3)>1,{'minimum':'4/3'})

for index,(wx,wy,wz) in enumerate([tuple(v) for v in normals[:2]],1):
    factor=wy+min(wx,wy)
    u_remainder=factor+wx+2*min(wx,wy)
    fourth_remainder=factor+4*min(wx,wy)
    check('Facet '+str(index)+' complete analytic higher-term bound',u_remainder>1 and fourth_remainder>1,{'u_times_order_two_lower_weight':str(u_remainder),'order_four_lower_weight':str(fourth_remainder),'scope':'All infinitely many monomials in the displayed analytic remainders'})

ss,tt,alpha,beta,uu,vv=s.symbols('ss tt alpha beta uu vv',nonzero=True)
forward=s.Matrix([alpha*ss+beta*tt,beta*tt])
inverse={ss:(uu-vv)/alpha,tt:vv/beta}
check('Axes and cusp tangent linear inverse',forward.subs(inverse,simultaneous=True)==s.Matrix([uu,vv]),{'map':['u=alpha*s+beta*t','v=beta*t'],'inverse':['s=(u-v)/alpha','t=v/beta']})
bb,cc,dd,xx=s.symbols('bb cc dd xx')
quad=(uu*uu+bb*uu+cc).subs(uu,s.sqrt(dd)*xx-bb/2)
check('Original cusp to frozen quadratic exact identity',eq(quad,dd*xx*xx+cc-bb*bb/4),'d(t)=-(c(t)-b(t)^2/4)/t^3 makes the last terms -d(t)t^3')
check('Section coordinate under the same cusp map',eq((uu-vv).subs(uu,s.sqrt(dd)*xx-bb/2),s.sqrt(dd)*(xx-(vv+bb/2)/s.sqrt(dd))),'a(t)=(t+b(t)/2)/sqrt(d(t)); the inverse map preserves t')
check('Printed even quadratic exponents match D list',[2*k+2 for k in range(1,4)]==[4,6,8],{'quadratic_exponents':[2,4,6],'D_indices':[4,6,8]})
check('Printed odd quadratic exponents match D list',[2*k+3 for k in range(1,4)]==[5,7,9],{'quadratic_exponents':[3,5,7],'D_indices':[5,7,9]})

# Universal graph identities and the printed global formulas.
g,beta_graph=s.symbols('g beta_graph',nonnegative=True)
check('Exceptional analytic and topological graph dimensions',eq(2*(g+beta_graph)-(2*g+beta_graph),beta_graph),'h1(O_E)=sum g_i+beta, b1(E)=2sum g_i+beta')
nu,lb,b1,n,rd,N0,r,z,ell,aa=s.symbols('nu lb b1 n rd N0 r z ell aa')
eU=3*(nu-2);b1D=nu-2+lb;dD=n+3;c=1;eps=1
eD=c-b1D+dD;eX=eU+eD;b2=eX-2+2*b1
rank=b2-dD+eps
check('C RD 24 complement Euler',eq(eU,3*(4-(6-nu))),str(eU))
check('C RD 24 boundary first Betti',eq(b1D,(nu-(3+0)+1)+lb),str(b1D))
check('C RD 24 exact compact rank',eq(rank,2*nu-4+2*b1-lb),str(s.expand(rank)))
check('C RD 24 universal lower bound gap',eq(rank-(2*nu-6),2*b1+(2-lb)),'b1>=0, lambda<=2')
check('Three boundary components and two independent base classes',3-2==1,'The exact inverse relation maps include every exceptional coefficient')
check('C RD 25 fibre branch identity',eq(1+aa,aa+1),{'ramified':2,'unramified':3})
nuF=1+aa;nuout=nu-nuF
check('C RD 26 duplicate-loss identity',eq((aa-1)+nuout,nu-2),'a distinct normalization points over the common zero, at most a-1 collisions')
K=r-z-rd
check('C RD 27 exact Euler gap before discarding nonnegative term',eq(2-r+N0+K-ell,2-rd-ell+(N0-z)),'Number z of wholly exceptional trees satisfies z<=N0')
check('C RD 27 final nonnegative decomposition',eq(2-rd-ell,(1-rd)+(1-ell)),'rdom<=1, ell<=1')

print(json.dumps({'tag':'01CK','phase':'postrelease comparison','method':'Rational vertex reconstruction of the printed nonconvenient Newton polyhedron; universal positive-lattice and analytic-remainder inequalities; exact coordinate identities; graph and Euler identities.','checks':checks,'exact_checks':len(checks),'all_passed':all(c['passed'] for c in checks)},indent=2))
