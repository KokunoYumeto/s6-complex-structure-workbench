# G2 sanity check: bielliptic types of S_1, S_2 and the degree-two specialization lattice at p_2.
from sympy import Matrix, eye, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ
from itertools import combinations
A1 = Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
v1 = Matrix([1,2,-4,0]); v2 = Matrix([-1,-3,3,0])
print("A1^3=I", A1**3==eye(4), " A2^4=I", A2**4==eye(4), " A1 v1=v1", A1*v1==v1, " A2 v2=v2", A2*v2==v2)
for name,A in (("A1",A1),("A2",A2)):
    print(name, "Smith form of A-I:", smith_normal_form(A-eye(4), domain=ZZ).diagonal())
    # invariant sublattice and 'rotation' sublattice
    inv = (A-eye(4)).nullspace()
    print(name, "Lambda^A basis:", [list(x.T) for x in inv])
# rotation sublattice Lambda_E = ker(A^2+1) for A2, ker(A^2+A+1) for A1
for name,A,P in (("A1",A1,A1**2+A1+eye(4)),("A2",A2,A2**2+eye(4))):
    ker = P.nullspace()
    inv = (A-eye(4)).nullspace()
    def prim(v):
        from sympy import ilcm, igcd
        d = ilcm(*[x.q for x in v]); w = [int(x*d) for x in v]
        g = 0
        for x in w: g = igcd(g,x)
        return Matrix([x//g for x in w])
    K = [prim(x) for x in ker]; I = [prim(x) for x in inv]
    # saturate rank-2 lattices: use the given primitive vectors and check index via gcd of 2x2 minors
    def sat_index(vecs):
        M = Matrix.hstack(*vecs)
        from sympy import igcd
        g = 0
        for r in combinations(range(4),2):
            g = igcd(g, int(M.extract(list(r),[0,1]).det()))
        return g
    M = Matrix.hstack(*(K+I))
    print(name, "rot sublattice gens", [list(x.T) for x in K], "minor-gcd", sat_index(K),
          "| inv gens", [list(x.T) for x in I], "minor-gcd", sat_index(I),
          "| index of (Lambda_E + Lambda^A) in Lambda:", abs(M.det()))
# two-forms: coordinates (gu, gw, gd, uw, ud, wd) on basis indices (0,1,2,3)=(gamma,u,w,delta)
pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def wedge2(a,b):
    return Matrix([a[i]*b[j]-a[j]*b[i] for (i,j) in pairs])
def ext2(T):
    return Matrix(6,6,lambda r,c: T[pairs[r][0],pairs[c][0]]*T[pairs[r][1],pairs[c][1]]-T[pairs[r][0],pairs[c][1]]*T[pairs[r][1],pairs[c][0]])
def pair22(x,y):
    # x^y = coefficient of vol = g u w d
    # complementary pairs with signs: (01)(23)+, (02)(13)-, (03)(12)+
    return x[0]*y[5]+x[5]*y[0]-x[1]*y[4]-x[4]*y[1]+x[2]*y[3]+x[3]*y[2]
g=[1,0,0,0];u=[0,1,0,0];w=[0,0,1,0];d=[0,0,0,1]
eta1=[0,2,1,3]; eta2=[0,1,1,2]
q = wedge2(u,w)+6*wedge2(g,d)
for name,A,eta in (("p1",A1,eta1),("p2",A2,eta2)):
    T = (A.inv()).T          # action on covectors
    h = wedge2(g,eta)
    L2T = ext2(T)
    print(name, "eta invariant:", (T*Matrix(eta))==Matrix(eta), " h inv:", L2T*h==h, " q inv:", L2T*q==q,
          " Gram(h,q)=", [[pair22(h,h),pair22(h,q)],[pair22(h,q),pair22(q,q)]])
# p2: isotropic classes h and q-3h; candidate lattices
h2 = wedge2(g,eta2)
print("p2: (q-3h)^2 =", pair22(q-3*h2,q-3*h2), " h.(q-3h) =", pair22(h2,q-3*h2))
for nm,B in (("<2h,h+q> (course)",[2*h2,h2+q]),("<h,2q>",[h2,2*q]),("<2h,q>",[2*h2,q])):
    G = Matrix(2,2,lambda i,j: pair22(B[i],B[j]))/4
    print(nm, "downstairs Gram", G.tolist(), "det", G.det())
