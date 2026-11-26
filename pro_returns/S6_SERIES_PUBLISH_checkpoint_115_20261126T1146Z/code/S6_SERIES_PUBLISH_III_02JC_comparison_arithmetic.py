#!/usr/bin/env python3
"""Post-release comparison of every printed 02JC integral matrix.

This program was written after the authorized proof was read. It is
comparison evidence, not a pre-release independent derivation. The
pre-release method and program remain in their separate frozen files.
"""
from itertools import combinations
from functools import reduce
from math import gcd
from sympy import Matrix, eye, zeros


def exterior(a, degree):
    choices = list(combinations(range(a.rows), degree))
    return Matrix([[a.extract(i, j).det() for j in choices] for i in choices])


def smith_from_minors(a):
    """Determine nonzero Smith factors by gcds of all minors."""
    previous = 1
    factors = []
    for size in range(1, min(a.shape)+1):
        divisor = 0
        for rows in combinations(range(a.rows), size):
            for cols in combinations(range(a.cols), size):
                divisor = gcd(divisor, abs(int(a.extract(rows, cols).det())))
        if not divisor:
            break
        assert divisor % previous == 0
        factors.append(divisor//previous)
        previous = divisor
    return factors


def check(name, assertion):
    assert assertion, name
    print('PASS '+name)


def show(name, a):
    print(name+':')
    for i in range(a.rows):
        print('  '+' '.join(str(a[i,j]) for j in range(a.cols)))


A1=Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=(A1*A2).inv()
v1=Matrix([1,2,-4,0]);v2=Matrix([-1,-3,3,0])
g,u,w,d=[eye(4)[:,j] for j in range(4)]
B1=A1[1:,1:];B2=A2[1:,1:]
for j,(Aj,Bj,vj,mj) in enumerate([(A1,B1,v1,3),(A2,B2,v2,4)],1):
    base_change=Matrix.hstack(vj,u,w,d)
    block=Matrix.diag(1,Bj)
    check('finite mapping-torus coordinate map '+str(j),
          abs(base_change.det())==1 and Aj*base_change==base_change*block)
    for r in range(4):
        e=exterior(Bj,r)
        factors=smith_from_minors(e-eye(e.rows))
        check('finite exterior Smith factors j='+str(j)+' r='+str(r),all(k==1 for k in factors))
        print('  factors',factors,'kernel rank',e.rows-len(factors))

alpha1=Matrix([[3,0,0,0],[0,2,1,3],[4,0,0,0],[0,-1,-1,-2]])
nu=Matrix([0,-1,-1,1]);left1=Matrix([[4,0,-3,0]])
check('alpha1 nonzero Smith factors',smith_from_minors(alpha1)==[1,1,1])
check('alpha1 primitive right and left kernels',alpha1*nu==zeros(4,1)
      and left1*alpha1==zeros(1,4) and reduce(gcd,map(abs,list(nu)))==1
      and reduce(gcd,map(abs,list(left1)))==1)
check('H1 quotient coefficients',left1*Matrix([3,0,0,0])==Matrix([12])
      and 4+(-3)==1)

pairs=list(combinations(range(4),2))
def wedge_vector(x,y):
    return Matrix([x[i]*y[j]-x[j]*y[i] for i,j in pairs])

def product2(x,y):
    total=0
    for a,(i,j) in enumerate(pairs):
        for b,(k,l) in enumerate(pairs):
            perm=(i,j,k,l)
            if len(set(perm))<4:
                continue
            sign=(-1)**sum(perm[r]>perm[s] for r in range(4) for s in range(r+1,4))
            total+=sign*x[a]*y[b]
    return total

eta1=Matrix([0,2,1,3]);eta2=Matrix([0,1,1,2])
ge1=wedge_vector(g,eta1);ge2=wedge_vector(g,eta2)
q2=Matrix([0,0,6,1,0,0])
for j,(Aj,ge,degree) in enumerate([(A1,ge1,3),(A2,ge2,4)],1):
    fixed=Matrix.hstack(ge,q2)
    op=exterior(Aj.T,2)-eye(6)
    check('primitive integral H2 invariant lattice '+str(j),
          op*fixed==zeros(6,2) and op.rank()==4 and smith_from_minors(fixed)==[1,1])
    pairing=Matrix([[product2(x,y) for y in (ge,q2)] for x in (ge,q2)])
    show('invariant intersection form '+str(j),pairing)
    check('invariant intersection determinant '+str(j),abs(pairing.det())==[9,4][j-1])
    print('  covering pullback index', [1,2][j-1], 'degree',degree)
check('order-four invariant torus evaluations',
      (ge2.T*wedge_vector(v2,d))[0]==-2 and (q2.T*wedge_vector(v2,d))[0]==-6)

pullback1=Matrix.hstack(ge1,q2-2*ge1)
pullback2=Matrix.hstack(2*ge2,q2-3*ge2)
alpha2=Matrix.vstack(pullback1.T,-pullback2.T)
check('alpha2 exactly evaluates the stated pullback bases',
      alpha2==Matrix([[2,1,3,0,0,0],[-4,-2,0,1,0,0],[-2,-2,-4,0,0,0],[3,3,0,-1,0,0]]))
Phi=Matrix([[4,2,3,2]])
check('alpha2 nonzero Smith factors',smith_from_minors(alpha2)==[1,1,1])
check('alpha2 primitive left kernel',Phi*alpha2==zeros(1,6)
      and reduce(gcd,map(abs,list(Phi)))==1)
check('cohomology restriction of A is 2q2',pullback1*Matrix([4,2])==2*q2
      and pullback2*Matrix([3,2])==2*q2)

c2=Matrix([[1,0,0,0,0,0],[0,0,-1,0,0,0],
           [0,-1,-1,1,1,0],[0,0,0,1,0,0]])
fresh_c2=Matrix([[1,0,0,0,0,0],[0,0,1,0,0,0],
                 [0,0,0,-1,0,0],[0,-1,-1,1,1,0]])
target_change=Matrix([[1,0,0,0],[0,-1,0,0],[0,0,0,1],[0,0,-1,0]])
check('exact cusp target-basis morphism',c2==target_change*fresh_c2
      and abs(target_change.det())==1)
show('fresh cusp target coordinates to printed target coordinates',target_change)
qmaps={1:Matrix([[1,0,0,0],[0,1,0,0]]),2:c2,
       3:Matrix([[1,0,0,0],[0,1,0,0]]),4:eye(1)}
for r,qmap in qmaps.items():
    op=exterior(M0,r)-eye(qmap.cols)
    check('cusp kernel equals primitive monodromy image degree '+str(r),
          qmap*op==zeros(qmap.rows,op.cols)
          and op.rank()+qmap.rank()==qmap.cols
          and all(x==1 for x in smith_from_minors(op))
          and smith_from_minors(qmap)==[1]*qmap.rows)

check('connecting maps on both phase generators',
      (eye(4)-A2)*w==-nu and (eye(4)-A2)*d==zeros(4,1)
      and (eye(4)-A2)*Matrix.hstack(w,d)==(eye(4)-A1.inv())*Matrix.hstack(w,d))
contraction=Matrix([0,0,0,0])
for coefficient,(i,j) in zip(2*q2,pairs):
    contraction[j]+=coefficient*d[i]
    contraction[i]-=coefficient*d[j]
check('circle-sweep restriction i_d(2q2)=-12 gamma',contraction==-12*g)
D1=Matrix([[1,0,0],[0,1,0],[-12,0,1]])
check('full H1 cusp map unimodular',D1.det()==1)

counts=[5,20,45,56,42,17,3]
homology_ranks=[1,0,0,0,0,0,1]
boundary_ranks=[0]
for n in range(6):
    boundary_ranks.append(counts[n]-homology_ranks[n]-boundary_ranks[-1])
check('boundary ranks derived from proved homology and granted cell counts',
      boundary_ranks[1:]==[4,16,29,27,15,2]
      and counts[6]-boundary_ranks[-1]==1)
print('Boundary ranks',boundary_ranks[1:])
print('These ranks use the proved homology; no original cellular differential was executed.')
print('Unit Smith factors follow from primitivity of images, proved in the comparison note.')
print('ALL POST-RELEASE COMPARISON CHECKS PASSED')
