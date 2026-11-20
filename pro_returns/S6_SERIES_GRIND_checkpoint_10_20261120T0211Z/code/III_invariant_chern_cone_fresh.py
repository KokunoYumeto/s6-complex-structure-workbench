"""Fresh exact homology calculation for D2.51's displayed integral cone.

This program uses no historical executable, table, or coefficient array.
It independently constructs the matrices from permutations and invariant
Chern vectors, finds an integral cycle basis by Bezout column operations,
and applies SymPy Smith form to the actual boundary sublattice.
The mixed geometric boundary columns are not inputs or conclusions.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from math import gcd
from functools import reduce
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
checks = 0
counts = Counter()

def check(value, message):
    global checks
    checks += 1
    if not value:
        raise AssertionError(message)

def egcd(a, b):
    old_r, r = a, b
    old_s, s, old_t, t = 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r-q*r
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t

def row_reduction(c):
    """Return V unimodular with c V = (gcd(c),0,...,0)."""
    n = len(c)
    v = sp.eye(n)
    current = list(c)
    for j in range(1, n):
        a,b = current[0],current[j]
        if a == b == 0:
            continue
        g,x,y = egcd(a,b)
        a0,aj = v[:,0],v[:,j]
        v[:,0] = x*a0+y*aj
        v[:,j] = (-b//g)*a0+(a//g)*aj
        current[0],current[j] = g,0
    if current[0] < 0:
        v[:,0] = -v[:,0]
        current[0] = -current[0]
    check(abs(v.det()) == 1, "integral kernel basis determinant")
    check(sp.Matrix([c])*v == sp.Matrix([current]), "Bezout row map")
    return v,current[0]

def smith(m):
    d = smith_normal_form(m, domain=sp.ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]

def model(lengths, values):
    n = sum(lengths)
    p = sp.zeros(n)
    c = []
    at = 0
    for length,value in zip(lengths, values):
        for j in range(length):
            p[at+(j+1)%length,at+j] = 1
            c.append(value)
        at += length
    cmat = sp.Matrix([c])
    d2 = sp.zeros(2,n+1)
    d2[0,:n] = cmat
    d3 = sp.zeros(n+1,2*n)
    d3[:n,n:] = p-sp.eye(n)
    d3[n,n:] = cmat
    d4 = sp.zeros(2*n,n)
    d4[:n,:] = sp.eye(n)-p
    check(d2*d3 == sp.zeros(2,2*n), "d2d3")
    check(d3*d4 == sp.zeros(n+1,n), "d3d4")
    check(cmat*p == cmat, "actual invariant Chern row")
    v,g = row_reduction(c)
    transform = sp.diag(v,1)
    transformed = transform.inv()*d3
    rho = len(lengths)
    h = reduce(gcd,(abs(l*x) for l,x in zip(lengths,values)),0)
    if g:
        check(transformed[0,:] == sp.zeros(1,2*n), "boundaries are cycles")
        boundary = transformed[1:,:]
        expected_free = rho-1
    else:
        boundary = transformed
        expected_free = rho+1
    sd = smith(boundary)
    check(boundary.rows-len(sd) == expected_free, "H2 free rank")
    check([x for x in sd if x>1] == ([h] if h>1 else []), "full H2 torsion invariant")
    et = sp.zeros(boundary.rows,1)
    et[-1,0] = 1
    augmented = boundary.row_join(et)
    sa = smith(augmented)
    if g:
        check(augmented.rank() == boundary.rank(), "delta-gamma is torsion")
        check(all(x==1 for x in sa), "delta-gamma generates all torsion")
        check(sp.prod(sd)//sp.prod(sa) == h, "actual delta-gamma order")
    else:
        check(augmented.rank() == boundary.rank()+1, "delta-gamma is free")
        check(all(x==1 for x in sa), "delta-gamma is primitive")
    # Degree 3 splits into orbit coinvariants in its first block and
    # the kernel of the orbit Chern evaluation in its second block.
    invariant = sp.zeros(n,rho)
    at=0
    for j,length in enumerate(lengths):
        invariant[at:at+length,j]=sp.ones(length,1)
        at+=length
    check((p-sp.eye(n))*invariant == sp.zeros(n,rho), "actual invariant basis")
    check(cmat*invariant == sp.Matrix([[l*x for l,x in zip(lengths,values)]]), "invariant Chern functional")
    first = smith(sp.eye(n)-p)
    check(all(x==1 for x in first) and n-len(first)==rho, "free orbit coinvariants")
    check(2*n-d3.rank()-d4.rank() == (2*rho-1 if g else 2*rho), "H3 rank by chain matrices")
    check(n-d4.rank()==rho, "H4 rank")
    check(smith(d2) == ([g] if g else []), "H1 scalar relation")
    counts['models'] += 1
    counts['nonzero_Chern' if g else 'zero_Chern'] += 1
    counts['torsion_models'] += (h>1)
    return {'lengths':lengths,'degrees':values,'g':g,'h':h,'H2_free_rank':expected_free,'H2_torsion':[x for x in sd if x>1]}

def component_cases():
    """Construct the seven labelled affine intersection graphs explicitly.

    The cyclic component marking is j -> P^j(outer zero component).
    In the rank-two monodromy model it is j -> j e_2 (mod B-I).
    The output retains these maps, matrices, and orbit vectors.
    """
    cases=[]
    def graph(n,edges):
        c=2*sp.eye(n)
        for i,j,w in edges:c[i,j]=c[j,i]=-w
        return c
    data=[]
    data.append(('II',[1],sp.zeros(1),[0],1,sp.Matrix([[1,1],[-1,0]])))
    data.append(('III',[1,1],graph(2,[(0,1,2)]),[1,0],2,sp.Matrix([[0,1],[-1,0]])))
    data.append(('IV',[1,1,1],graph(3,[(0,1,1),(1,2,1),(2,0,1)]),[1,2,0],3,sp.Matrix([[0,1],[-1,-1]])))
    # E6 affine: central node and three arms of length two.
    edges=[(0,1,1),(1,2,1),(0,3,1),(3,4,1),(0,5,1),(5,6,1)]
    data.append(('IV*',[3,2,1,2,1,2,1],graph(7,edges),[0,3,4,5,6,1,2],3,sp.Matrix([[0,1],[-1,-1]]).inv()))
    # E7 affine: two length-three arms and one short arm.
    edges=[(0,1,1),(1,2,1),(2,3,1),(0,4,1),(4,5,1),(5,6,1),(0,7,1)]
    data.append(('III*',[4,3,2,1,3,2,1,2],graph(8,edges),[0,4,5,6,1,2,3,7],2,sp.Matrix([[0,1],[-1,0]]).inv()))
    for k in (1,3):
        n=k+5
        edges=[(0,2,1),(1,2,1)]+[(i,i+1,1) for i in range(2,k+2)]+[(k+2,k+3,1),(k+2,k+4,1)]
        perm=list(range(n));perm[0]=k+3;perm[k+3]=1;perm[1]=k+4;perm[k+4]=0
        for i in range(2,k+3):perm[i]=k+4-i
        data.append((f'I{k}*',[1,1]+[2]*(k+1)+[1,1],graph(n,edges),perm,4,sp.Matrix([[-1,-k],[0,-1]])))
    for kind,mu,cartan,perm,order,b in data:
        n=len(mu);p=sp.zeros(n)
        for i,j in enumerate(perm):p[j,i]=1
        check(cartan*sp.Matrix(mu)==sp.zeros(n,1),'primitive central multiplicity cycle '+kind)
        check(p.T*cartan*p==cartan,'actual component intersection map '+kind)
        check(p*sp.Matrix(mu)==sp.Matrix(mu),'multiplicity preserved '+kind)
        check(p**order==sp.eye(n),'component return order '+kind)
        check([x for x in smith(cartan) if x>1]==([order] if order>1 else []),'component discriminant group '+kind)
        check([x for x in smith(b-sp.eye(2)) if x>1]==([order] if order>1 else []),'rank-two component quotient '+kind)
        zero=next(i for i,x in enumerate(mu) if x==1)
        for j in range(order):
            pp=p**j;seen=set();orbits=[]
            for i in range(n):
                if i in seen:continue
                orb=[];cur=i
                while cur not in seen:
                    seen.add(cur);orb.append(cur)
                    cur=next(z for z in range(n) if pp[z,cur])
                orbits.append(orb)
            content=reduce(gcd,(len(o)*mu[o[0]] for o in orbits))
            expected=order//gcd(order,j)
            check(content==expected,'complete orbit-area content '+kind)
            q=sp.Matrix([0,j]);z=(b-sp.eye(2)).inv()*q
            denom=int(sp.ilcm(*(x.q for x in z)))
            check(denom==expected,'marked logarithm exact denominator '+kind)
            point=sp.eye(n)[:,zero];actual=point
            for power in range(1,order+1):
                actual=pp*actual
                if actual==point:break
            check(power==expected,'order of actual zero-component translate '+kind)
            cases.append({'type':kind,'component_class':j,'permutation_matrix':list(map(list,pp.tolist())),'multiplicities':mu,'orbits':orbits,'area_content':content,'monodromy':b.tolist(),'marked_cocycle':list(q),'marked_logarithm':[str(x) for x in z]})
    return cases

def main():
    cases=[]
    # Each tuple is generated here, not taken from an earlier certificate.
    for lengths in [(1,), (2,), (3,), (1,1), (1,2), (2,2), (1,3), (2,3), (1,1,2), (1,2,3)]:
        for values in product((-2,-1,0,1,2),repeat=len(lengths)):
            cases.append(model(lengths,values))
    # Actual multiplicity cycles with c.mu=0, and their orbit contents.
    area_cases=[]
    for lengths in [(1,1),(1,2),(2,2),(1,3),(2,3),(3,4)]:
        for mu1,mu2 in product(range(1,4),repeat=2):
            l1,l2=lengths
            divisor=gcd(l1*mu1,l2*mu2)
            cj=(l2*mu2//divisor,-l1*mu1//divisor)
            c=[cj[0]]*l1+[cj[1]]*l2
            mu=[mu1]*l1+[mu2]*l2
            check(sum(a*b for a,b in zip(c,mu))==0,"literal regular area is cycle")
            orbit=(l1*mu1,l2*mu2)
            check(gcd(orbit[0]//divisor,orbit[1]//divisor)==1,"primitive orbit area")
            area_cases.append({'lengths':lengths,'mu':mu,'degrees':c,'orbit_area':orbit,'content':divisor})
    components=component_cases()
    counts['actual_additive_component_classes']=len(components)
    out={'status':'PASS','assertions':checks,'counts':dict(counts),'sympy_version':sp.__version__,
         'scope':'Exact displayed cone and actual scalar-long torus order only. No mixed elliptic-long or fixed-normal marked torsion column is inferred.',
         'cases':cases,'multiplicity_cycles':area_cases,'component_class_models':components}
    path=ROOT/'code/outputs/III_invariant_chern_cone_fresh.json'
    path.write_text(json.dumps(out,indent=2,default=int)+'\n')
    print(json.dumps({k:out[k] for k in ['status','assertions','counts','scope']}))

if __name__=='__main__':main()
