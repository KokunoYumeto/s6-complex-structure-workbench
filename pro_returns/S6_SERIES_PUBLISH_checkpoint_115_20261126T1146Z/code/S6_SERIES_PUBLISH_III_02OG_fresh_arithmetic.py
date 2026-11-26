#!/usr/bin/env python3
"""Independent exact model, coset, peripheral and cocycle calculations for 02OG.

Inputs: the safe 02OG statement, Herfurtner Table III printed p.23,
and the general Poincare pairing proved in the admitted KM receiver.
No target original or root KP files are read.
"""
import json
from pathlib import Path
import sympy as S
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'agents/continuation6_iii_carriers/S6_SERIES_PUBLISH_III_02OG_fresh_maps.json'
I = S.eye(2)
J = S.Matrix([[0,1],[-1,0]])
A = S.Matrix([[0,1],[-1,1]])
B = S.Matrix([[0,1],[-1,0]])
T = S.Matrix([[1,1],[0,1]])
L = S.Matrix([[1,0],[-1,1]])
t = S.symbols('t')

def word_reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return tuple(out)

def inverse(w): return tuple(-x for x in w[::-1])

def substitute(w,images):
    return word_reduce(tuple(y for x in w for y in
                             (images[abs(x)-1] if x>0 else inverse(images[abs(x)-1]))))

def wpow(w,n): return word_reduce((w if n>=0 else inverse(w))*abs(n))

def word_matrix(w):
    m=I
    for x in w: m=m*({1:A,-1:A.inv(),2:B,-2:B.inv()}[x])
    return m

def psl_equal(m,n): return m==n or m==-n

def matrix_word(m):
    """Euclidean row reduction, with every inverse retained."""
    z=m.copy(); left=()
    while z[1,0]:
        q=int(z[0,0]//z[1,0])
        op=word_reduce((2,)+wpow((-1,2),-q))
        z=B*T**(-q)*z
        left=word_reduce(op+left)
    assert abs(z[0,0])==1 and z[0,0]==z[1,1]
    k=int(z[0,1]/z[0,0])
    out=word_reduce(inverse(left)+wpow((-1,2),k))
    assert psl_equal(word_matrix(out),m)
    return out

def cycles(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i not in seen:
            c=[]; j=i
            while j not in seen:
                seen.add(j);c.append(j);j=p[j]
            out.append(c)
    return out

def pairings(xs):
    if not xs:
        yield ();return
    i=xs[0]
    for j in xs[1:]:
        rest=tuple(k for k in xs if k not in (i,j))
        for p in pairings(rest): yield ((i,j),)+p

def orbit_relabel(pa,pb,root):
    """Canonical pointed transition table by BFS; both inverse labels explicit."""
    order=[root]; labels={root:0}
    for i in order:
        for j in (pa[i],pb[i]):
            if j not in labels:
                labels[j]=len(order);order.append(j)
    if len(order)!=len(pa): return None
    return tuple((labels[pa[i]],labels[pb[i]]) for i in order)

def passports(n,widths):
    pa=list(range(n))
    for i in range(0,n-1,3): pa[i:i+3]=[i+1,i+2,i]
    reps={}; count=0
    for pairs in pairings(tuple(range(n))):
        pb=list(range(n))
        for i,j in pairs: pb[i]=j;pb[j]=i
        pc=[pb[pa[i]] for i in range(n)]
        if sorted(map(len,cycles(pc)))!=sorted(widths):continue
        codes=[orbit_relabel(pa,pb,r) for r in range(n)]
        if codes[0] is None:continue
        count+=1;code=min(codes)
        reps.setdefault(code,(pa,pb))
    return count,len(reps)

def coset_surface(mats,peripherals):
    F,a,b=free_group('a,b')
    G=FpGroup(F,[a**3,b**2])
    def fw(w):
        out=F.identity
        for x in w:out=out*({1:a,-1:a,2:b,-2:b}[x]**(1 if x>0 else -1))
        return out
    ct=coset_enumeration_r(G,[fw(matrix_word(m)) for m in mats],max_cosets=500)
    ct.compress();ct.standardize()
    table=ct.table;n=len(table)
    pa=[row[0] for row in table];pb=[row[2] for row in table]
    assert all(pa[pa[pa[i]]]==i and pb[pb[i]]==i for i in range(n))
    assert all(pb[i]!=i for i in range(n))
    # Fill all smooth a-triangles and b-digons. Leave the a-fixed loop unfilled.
    removed={max(c) for c in cycles(pa) if len(c)==3}
    edges=[('a',i,i,pa[i]) for i in range(n) if i not in removed]
    edges += [('b',i,i,pb[i]) for i in range(n) if i<pb[i]]
    parent=list(range(n))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    ew={};chords=[];tree=[]
    for kind,i,u,v in edges:
        if find(u)!=find(v):
            parent[find(u)]=find(v);ew[kind,i]=();tree.append((kind,i,u,v))
        else:
            chords.append((kind,i,u,v));ew[kind,i]=(len(chords),)
    assert len({find(i) for i in range(n)})==1
    adjacency=[[] for _ in range(n)]
    for kind,i,u,v in tree:
        letter=1 if kind=='a' else 2
        adjacency[u].append((v,letter));adjacency[v].append((u,-letter))
    tree_paths={0:()};queue=[0]
    for u in queue:
        for v,letter in adjacency[u]:
            if v not in tree_paths:
                tree_paths[v]=tree_paths[u]+(letter,);queue.append(v)
    chord_words=[];chord_matrices=[]
    for kind,i,u,v in chords:
        w=word_reduce(tree_paths[u]+(1 if kind=='a' else 2,)+inverse(tree_paths[v]))
        chord_words.append(w);chord_matrices.append(word_matrix(w).tolist())
    aw={i:ew['a',i] for i in range(n) if i not in removed}
    for i in removed:
        aw[i]=word_reduce(inverse(aw[pa[pa[i]]])+inverse(aw[pa[i]]))
    bw={i:(ew['b',i] if i<pb[i] else inverse(ew['b',pb[i]])) for i in range(n)}
    def lift(w):
        i=0;out=()
        for x in w:
            if x==1: part=aw[i];j=pa[i]
            elif x==-1:j=pa[pa[i]];part=inverse(aw[j])
            elif x==2:part=bw[i];j=pb[i]
            else:j=pb[i];part=inverse(bw[j])
            out=word_reduce(out+part);i=j
        return i,out
    lifted=[]
    for w in peripherals:
        end,word=lift(w);assert end==0
        lifted.append(word)
    prod=word_reduce(tuple(x for w in lifted for x in w))
    pc=[pb[pa[i]] for i in range(n)]
    return dict(n=n,a=pa,b=pb,cusp_cycles=cycles(pc),tree=tree,chords=chords,
                tree_paths=tree_paths,chord_modular_words=chord_words,
                chord_projective_matrices=chord_matrices,
                a_edges=aw,b_edges=bw,peripheral_words=lifted,product_word=prod)

data={
 '50':dict(g2=3*t*(t+8),g3=t*(t*t-20*t-8),
           matrices=[S.Matrix([[3,7],[-1,-2]]),S.Matrix([[7,12],[-3,-5]]),S.Matrix([[-2,-1],[1,0]])],
           q=[S.Matrix([-5,2]),S.Matrix([-8,4]),S.Matrix([0,1])],
           bases=[I,S.Matrix([2,-1]),I],widths=[1,3]),
 '56':dict(g2=3*(t-3)*(81*t**3-9*t**2-53*t-27),
           g3=(t-3)*(729*t**5-1215*t**4-1350*t**3-350*t**2-675*t-243),
           matrices=[S.Matrix([[5,8],[-2,-3]]),S.Matrix([[27,37],[-19,-26]]),S.Matrix([[61,80],[-45,-59]]),S.Matrix([[4,3],[-3,-2]])],
           q=[S.Matrix([-2,1]),S.Matrix([0,0]),S.Matrix([4,-3]),S.Matrix([1,-1])],
           bases=[S.Matrix([2,-1]),I,S.Matrix([4,-3]),S.Matrix([1,-1])],widths=[2,5,3])}

saved={}
for key,d in data.items():
    print('\nPROFILE',key)
    g2,g3=d['g2'],d['g3'];delta=S.factor(g2**3-27*g3**2)
    expected_delta=1728*t**2*(t-1)**3 if key=='50' else -2**14*3**4*t**3*(t-3)**2*(9*t+5)**2
    assert S.expand(delta-expected_delta)==0
    jj=S.cancel(g2**3/delta);num,den=S.fraction(jj)
    print('g2 =',S.factor(g2));print('g3 =',S.factor(g3));print('Delta =',delta)
    print('J numerator/denominator =',S.factor(num),S.factor(den))
    print('J-1 numerator =',S.factor(num-den))
    print('J derivative numerator =',S.factor(S.diff(num,t)*den-num*S.diff(den,t)))
    factors=[S.Poly(f,t) for polynomial in [num,num-den,den]
             for f,e in S.factor_list(polynomial,t)[1]]
    assert all(S.gcd(f,f.diff()).degree()==0 for f in factors)
    assert all(S.gcd(factors[i],factors[j]).degree()==0
               for i in range(len(factors)) for j in range(i))
    singular_points=[0,1,S.oo] if key=='50' else [S.Rational(-5,9),3,S.oo,0]
    def valuation(f,p,weight):
        if p==S.oo:return weight-S.degree(f,t)
        z=S.Poly(f,t)
        order=0
        while z.eval(p)==0:z=z.exquo(S.Poly(t-p,t));order+=1
        return order
    orders=[tuple(valuation(f,p,w) for f,w in [(g2,4),(g3,6),(delta,12)])
            for p in singular_points]
    expected_orders=[(1,1,2),(0,0,3),(2,3,7)] if key=='50' else [(0,0,2),(1,1,2),(0,0,5),(0,0,3)]
    assert orders==expected_orders
    print('ordered places and valuation triples =',list(zip(singular_points,orders)))
    mats=d['matrices'];q=d['q'];bs=d['bases'];prefix=I
    relation=S.zeros(2,1);blocks=[];cblocks=[];qloc=[]
    for m,z,bb in zip(mats,q,bs):
        assert m.det()==1
        blocks.append(prefix*bb)
        cb=bb.gauss_jordan_solve(m-I)[0]
        qq=bb.gauss_jordan_solve(z)[0]
        assert all(x.q==1 for x in cb) and all(x.q==1 for x in qq)
        cblocks.append(cb);qloc.extend(qq)
        relation+=prefix*z;prefix=prefix*m
    assert prefix==I and relation==S.zeros(2,1)
    R=S.Matrix.hstack(*blocks);C=S.Matrix.vstack(*cblocks);g=S.Matrix(qloc)
    # Since the II block of A-I is unimodular, torsion is immediately zero.
    ii_index=0 if key=='50' else 1
    assert abs((mats[ii_index]-I).det())==1
    print('R =',R);print('C =',C);print('g =',g.T)
    # The II block has determinant one: its actual inverse supplies E.
    offset=sum(bb.cols for bb in bs[:ii_index])
    E=S.zeros(R.cols,2)
    E[offset:offset+2,:]=R[:,offset:offset+2].inv()
    M=S.Matrix.hstack(C,g,E)
    assert abs(M.det())==1 and R*M==S.Matrix.hstack(S.zeros(2,3),I)
    print('M =',M);print('M inverse =',M.inv())
    print('det M =',M.det())
    k,h1,h2,l,j1,j2=S.symbols('k h1 h2 l j1 j2')
    cc=[k*z+(m-I)*S.Matrix([h1,h2]) for m,z in zip(mats,q)]
    dd=[l*z+(m-I)*S.Matrix([j1,j2]) for m,z in zip(mats,q)]
    zz=[]
    for m,z in zip(mats,dd):
        sol,pars=(m-I).gauss_jordan_solve(z)
        zz.append(sol.subs({p:0 for p in pars}))
    beta=[-z.T*J*m for m,z in zip(mats,cc)]
    height=S.Integer(0)
    for i in range(len(mats)):
        height-=(beta[i]*zz[i])[0]
        walk=I
        for j in range(i+1,len(mats)):
            height-=(beta[i]*walk*dd[j])[0]
            walk=walk*mats[j]
    height=S.factor(height)
    assert height==k*l/S.Integer(12 if key=='50' else 30)
    print('B(kq+dh,lq+dj) =',height)
    zq=[];betaq=[]
    for m,z in zip(mats,q):
        sol,pars=(m-I).gauss_jordan_solve(z)
        zq.append(sol.subs({p:0 for p in pars}));betaq.append(-z.T*J*m)
    local_terms=[-(bb*zz)[0] for bb,zz in zip(betaq,zq)]
    cross_terms=[]
    for i in range(len(mats)):
        walk=I
        for j in range(i+1,len(mats)):
            cross_terms.append((i,j,-(betaq[i]*walk*q[j])[0]));walk=walk*mats[j]
    print('fixed-point vectors z_i =',[list(z) for z in zq])
    print('beta_i =',[list(z) for z in betaq])
    print('local and cross pairing terms =',local_terms,cross_terms)
    if key=='50':
        conj=I
        loops=[matrix_word(T**-3)+(1,)+inverse(matrix_word(T**-3)),
               matrix_word(T**-2)+wpow((-2,-1),3)+inverse(matrix_word(T**-2)),
               matrix_word(B*T)+(-2,-1)+inverse(matrix_word(B*T))]
    else:
        conj=S.Matrix([[4,-1],[-3,1]])
        W=S.Matrix([[1,1],[1,2]])
        loops=[matrix_word(W)+wpow((-2,-1),2)+inverse(matrix_word(W)),
               matrix_word(T)+(1,)+inverse(matrix_word(T)),
               (2,)+wpow((-2,-1),5)+(-2,),wpow((-2,-1),3)]
    norm=[conj.inv()*m*conj for m in mats]
    for w,m in zip(loops,norm):assert psl_equal(word_matrix(w),m)
    surf=coset_surface(norm,loops)
    assert surf['n']==(4 if key=='50' else 10) and not surf['product_word']
    if key=='50':
        # u,v generate; x=uv u v^-1 u^-1 and y=v^-1u^-1.
        inv_basis=[(1,2,1,-2,-1),(-2,-1)]
        actual_chords=[mats[2].inv()*mats[0]*mats[2],mats[2]]
    else:
        inv_basis=[(2,),(-3,-2),(-3,-2,-1)]
        actual_chords=[norm[1],norm[3]*norm[0],norm[3]]
    generators=surf['peripheral_words'][:-1]
    for i,w in enumerate(inv_basis):assert substitute(w,generators)==(i+1,)
    for i,w in enumerate(generators):assert substitute(w,inv_basis)==(i+1,)
    def chord_eval(w):
        m=I
        for x in w:m=m*actual_chords[abs(x)-1]**(1 if x>0 else -1)
        return m
    for w,m in zip(surf['peripheral_words'],norm):assert chord_eval(w)==m
    for m,literal in zip(actual_chords,surf['chord_projective_matrices']):
        assert psl_equal(m,S.Matrix(literal))
    surf['inverse_free_basis']=inv_basis
    surf['actual_SL_chord_matrices']=[m.tolist() for m in actual_chords]
    print('global conjugator/inverse =',conj,conj.inv())
    print('peripheral modular words =',loops)
    print('coset surface =',surf)
    passport=passports(surf['n'],d['widths'])
    print('connected matching count, unpointed isomorphism classes =',passport)
    assert passport==(3,1) if key=='50' else passport==(162,1)
    saved[key]=dict(g2=str(g2),g3=str(g3),delta=str(delta),J=str(jj),
        R=R.tolist(),C=C.tolist(),q_local=list(g),M=M.tolist(),Minv=M.inv().tolist(),
        pairing=str(height),fixed_point_vectors=[list(z) for z in zq],
        beta=[list(z) for z in betaq],pairing_local_terms=local_terms,
        pairing_cross_terms=cross_terms,conjugator=conj.tolist(),inverse_conjugator=conj.inv().tolist(),
        modular_words=loops,surface=surf,passport=passport)
OUT.write_text(json.dumps(saved,indent=2,default=str)+'\n')
print('\nAll completed exact checks passed; saved',OUT.relative_to(ROOT))
