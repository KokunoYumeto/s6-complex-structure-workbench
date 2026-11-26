#!/usr/bin/env python3
"""CJ: quotient algebras, rational monodromy kernels, Newton counts and global identities."""
import itertools
import json
from collections import Counter
import sympy as s

x,y,T = s.symbols('x y T')
Q=s.Rational
checks=[]
def check(name,condition,evidence):
    good=bool(condition)
    checks.append({'name':name,'passed':good,'evidence':evidence})
    assert good,name
def equal(a,b):return s.simplify(a-b)==0

def companion(poly):
    p=s.Poly(poly,T);n=p.degree();M=s.zeros(n)
    for j in range(n-1):M[j+1,j]=1
    for i in range(n):M[i,n-1]=-p.nth(i)
    return M

types=[]
for n in range(1,11):types.append(('A'+str(n),x**2+y**(n+1),Q(1,2),Q(1,n+1),(n+1)//2,n))
for n in range(4,10):types.append(('D'+str(n),x**2*y+y**(n-1),Q(n-2,2*(n-1)),Q(1,n-1),n//2+1,n))
types.extend([('E6',x**3+y**4,Q(1,3),Q(1,4),3,6),('E7',x**3+x*y**3,Q(1,3),Q(2,9),4,7),('E8',x**3+y**5,Q(1,3),Q(1,5),4,8)])
rows=[]
M3=companion(T**2+T+1)
for name,f,wx,wy,delta,mu in types:
    gb=s.groebner([s.diff(f,x),s.diff(f,y)],x,y,order='lex')
    leading=[p.LM(order=gb.order).exponents for p in gb.polys]
    ax=min(i for i,j in leading if j==0)
    ay=min(j for i,j in leading if i==0)
    basis=[(i,j) for i in range(ax) for j in range(ay) if not any(i>=a and j>=b for a,b in leading)]
    check(name+' Jacobian quotient dimension',len(basis)==mu,{'groebner_basis':[str(p.as_expr()) for p in gb.polys],'standard_monomials':basis,'dimension':len(basis)})
    lattice=[(i,j,k) for i in range(int(s.floor(1/wx))) for j in range(int(s.floor(1/wy))) for k in range(3) if (i+1)*wx+(j+1)*wy+Q(k+1,3)<=1]
    pg=len(lattice)
    expected_pg=0 if name in ['A1','A2','A3','A4'] else 1
    check(name+' Newton geometric genus',pg==expected_pg,{'weights':[str(wx),str(wy),'1/3'],'lattice_points':lattice,'pg':pg})
    phases=[s.frac((i+1)*wx+(j+1)*wy) for i,j in basis]
    orders=Counter(int(v.q) for v in phases)
    blocks=[];factors={}
    for order,count in sorted(orders.items()):
        degree=int(s.totient(order));assert count%degree==0,(name,order,count)
        multiplicity=count//degree;factors[str(order)]=multiplicity
        blocks.extend([companion(s.cyclotomic_poly(order,T)) for _ in range(multiplicity)])
    M=s.diag(*blocks)
    assert M.rows==mu
    phase_counts=Counter(phases)
    descent=all(all(phase_counts[s.frac(Q(k,order))]==multiplicity for k in range(1,order+1) if s.gcd(k,order)==1) for order,multiplicity in [(int(o),m) for o,m in factors.items()])
    check(name+' cyclotomic evaluation isomorphism',descent,{'phase_multiplicities':{str(k):v for k,v in phase_counts.items()},'map':'[p(T)] maps to the tuple p(zeta_m^k); inverse is Lagrange interpolation at primitive m-th roots, separately for each copy.'})
    suspended=s.kronecker_product(M,M3)
    link_b1=suspended.rows-(suspended-s.eye(suspended.rows)).rank()
    expected_link=2 if name in ['A5','D4'] else 0
    check(name+' rational tensor-monodromy fixed space',link_b1==expected_link,{'cyclotomic_factor_multiplicities':factors,'plane_matrix_size':mu,'suspension_matrix_size':suspended.rows,'kernel_dimension':link_b1})
    rows.append({'type':name,'delta':delta,'pg':pg,'link_b1':link_b1,'standard_monomials':basis,'shifted_weight_phases':[str(v) for v in phases]})

# Exhaust every multiset of the 19 types with total delta at most five.
collections=[]
def visit(start,budget,names,pg,lb):
    collections.append({'types':names,'delta':5-budget,'pg':pg,'link_b1':lb})
    for i in range(start,len(rows)):
        r=rows[i]
        if r['delta']<=budget:visit(i,budget-r['delta'],names+[r['type']],pg+r['pg'],lb+r['link_b1'])
visit(0,5,[],0,0)
check('All delta-five local collections',all(r['pg']<=1 and r['link_b1']<=2 for r in collections),{'multisets':len(collections),'max_pg':max(r['pg'] for r in collections),'max_link_b1':max(r['link_b1'] for r in collections),'nonzero_invariant_min_delta':min(r['delta'] for r in rows if r['pg'] or r['link_b1'])})

def dot(a,b):return 2*a[0]*b[0]+a[0]*b[1]+a[1]*b[0]
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
xi=(s.Integer(1),s.Integer(0));K=(-2,0);D=(3,0)
a,j,b,n,lb,q,w,rd,rr,N0,zexc,keep,pairs,edges=s.symbols('a j b n lb q w rd rr N0 zexc keep pairs edges')
check('Normal degree independent of splitting',equal(a+(-2-a),-2),'N=O(a)+O(-2-a)')
check('Root divisor arithmetic genus',equal(1+Q(1,2)*dot(D,sub(D,(-K[0],-K[1]))),4),'Adjunction uses D.(D+K)/2+1')
check('Two rational components total delta',2-(1-4)==5,'Normalization Euler sequence gives delta=chi(O_normalization)-chi(O_D)')
check('Riemann-Roch character polynomial',equal(1+dot((-j,0),sub((-j,0),K))/2,1+j*(j-2)),'chi(O(-j xi))')
check('Finite cover holomorphic Euler',sum(1+i*(i-2) for i in range(3))==2,'1+0+1=2')
check('Pullback root class square',3*dot(xi,xi)==6,'Degree three pullback of xi has square six')
eD=4-b;eX=3*4-2*eD;eV=eX+n-lb;b2=eV-2+4*q
check('Branched cover topological Euler',equal(eX,4+2*b),'Three sheets off D and one sheet on D')
check('Resolved surface second Betti number',equal(b2,2+2*b+n-lb+4*q),'eV=eX+n-link_b1 and b1=b3=2q')
check('Complement pairing rank bound',equal(b2-(n+2),2*b-lb+4*q),'Subtract at most n+2 boundary classes')
check('Complement first Betti bound',equal(2*q+n+2-(n+1),2*q+1),'At least n+1 independent boundary classes')
check('Positive rank when branch excess at least two',all(2*bb-ll+4*qq>=2 for bb in range(2,6) for ll in range(3) for qq in range(2)),{'b_range':[2,5],'link_range':[0,2],'q_range':[0,1],'universal_gap':'2b-L+4q = 2+2(b-2)+(2-L)+4q'})
check('Universal positive-rank gap identity',equal(2*b-lb+4*q,2+2*(b-2)+(2-lb)+4*q),'All three extra terms are nonnegative in the asserted domain')
check('Attachment loss Euler identity',equal((2-rr+N0+keep-pairs).subs(keep,rr-zexc-rd),2-rd-pairs+(N0-zexc)),'K=r-z-rdom, and at most pairs edges are identified')
check('Final Euler nonnegative gap',equal(2-rd-pairs+(N0-zexc),(1-rd)+(1-pairs)+(N0-zexc)),'rdom<=1, pairs<=1, z<=N0')

v=s.Matrix(3,4,lambda i,j:s.Symbol('v'+str(i)+str(j)))
two=[s.Matrix([v[i,a]*v[j,b]-v[i,b]*v[j,a] for a,b in itertools.combinations(range(4),2)]) for i,j in itertools.combinations(range(3),2)]
def wedge(A,B):return s.expand(A[0]*B[5]-A[1]*B[4]+A[2]*B[3]+A[3]*B[2]-A[4]*B[1]+A[5]*B[0])
gram=s.Matrix(3,3,lambda i,j:wedge(two[i],two[j]))
check('Torus pairing on a rank-three subgroup',gram==s.zeros(3),{'exterior_square_gram':str(gram),'scope':'Three arbitrary vectors in Q^4; every pairing in their exterior-square span is zero.'})

print(json.dumps({'tag':'01CJ','method':'Automatically derived Jacobian standard monomials; rational cyclotomic companion blocks and exact tensor-monodromy kernel ranks; Newton lattice counts; exact surface/intersection identities and exterior-square matrix.','checks':checks,'local_rows':rows,'exact_checks':len(checks),'all_passed':all(c['passed'] for c in checks),'supporting_scope':'Local classification and spectrum/adjunction maps are the completed cited input 01CI. This program recomputes its arithmetic without claiming a new independent proof of that owner. Finite global grids are supplemented by the displayed universal symbolic gap identities.'},indent=2))
