"""Exact full van Kampen presentation, invariant closure, and H1 for F.2.31.

Arbitrary integral affine numerators are allowed; the actual power vector
is computed from the rational affine lift, not assumed equal to that
numerator. Freeness is tested at the prime-order subgroups of the cyclic
action. No conjugacy classification or higher homology is claimed here.

The presentation uses left conjugation matrices. To convert a geometric
peripheral convention that gives the opposite action, reverse the ordered
list and invert each affine lift, and negate the clutch vector. This
replaces each peripheral generator by the inverse one in reverse order,
an explicit isomorphism of the presented group. The H1 and invariant-
closure calculations are unchanged by that simultaneous conversion.
"""
import sympy as S
import json
from pathlib import Path
from fourfolds_survivor_test import kernel, factors, fixed_split, Z
from fourfolds_family_survivors import family
from sympy.matrices.normalforms import hermite_normal_form

def integral(M):
    M=S.Matrix(M)
    assert all(S.denom(x)==1 for x in M), 'Nonintegral lattice input'
    return Z(M)

def affine_certificate(M,v,m):
    M=integral(M);v=integral(v);m=int(m)
    n=M.rows;I=S.eye(n)
    assert m>=1 and M.shape==(n,n) and v.shape==(n,1)
    assert abs(M.det())==1 and M**m==I
    affine=S.eye(n+1);affine[:n,:n]=M;affine[:n,n]=v/m
    power=(affine**m)[:n,n]
    assert all(S.denom(x)==1 for x in power), 'The claimed affine order is invalid'
    power=integral(power)
    assert M*power==power
    tests=[]
    for p in sorted(S.factorint(m)):
        j=m//int(p);lift=affine**j
        covectors=kernel((M**j).T-I).T
        pairings=covectors*lift[:n,n]
        fixed=all(S.denom(x)==1 for x in pairings)
        tests.append({'prime':int(p),'power':j,'fixed_point':fixed,
                      'invariant_pairings':[str(x) for x in pairings]})
    return {'free':not any(t['fixed_point'] for t in tests),
            'power_vector':power,'prime_subgroup_tests':tests}

def affine_free(M,v,m):
    return affine_certificate(M,v,m)['free']

def invariant_closure(generators,seed):
    """Exact normal closure inside an abelian lattice.

    Once the rational rank stops increasing, its saturation index D
    bounds the number of additional strict enlargements by floor(log2D).
    """
    seed=integral(seed);H=hermite_normal_form(seed);n=H.rows
    generators=[integral(M) for M in generators]
    invertible=generators+[Z(M.inv()) for M in generators]
    rounds=0;bound=None;rank_steps=0;old_rank=H.cols;trace=[]
    while True:
        L=hermite_normal_form(S.Matrix.hstack(H,*(M*H for M in invertible)))
        rounds+=1
        trace.append({'round':rounds,'rank':H.cols,
                      'saturation_index':int(S.prod(factors(H))),
                      'basis':H.tolist()})
        if L==H:return H,{'rounds':rounds,'rank_growth_steps':rank_steps,
                           'post_rank_stability_bound':bound,'trace':trace}
        if L.cols>old_rank:
            rank_steps+=1;assert rank_steps<=n-seed.rank();old_rank=L.cols
        elif bound is None:
            # Product of the nonzero Smith factors is the saturation index.
            index=S.prod(factors(H))
            bound=int(index).bit_length()-1
            remaining=bound
        if bound is not None:
            remaining-=1;assert remaining>=0
        H=L

def first_homology(matrices,numerators,orders,clutch=None):
    matrices=[integral(M) for M in matrices]
    numerators=[integral(v) for v in numerators]
    n=matrices[0].rows;k=len(matrices);I=S.eye(n)
    assert len(numerators)==len(orders)==k
    clutch=S.zeros(n,1) if clutch is None else integral(clutch)
    certificates=[affine_certificate(M,v,m) for M,v,m in zip(matrices,numerators,orders)]
    assert all(c['free'] for c in certificates), 'A finite cap is not free'
    powers=[c['power_vector'] for c in certificates]
    columns=[]
    for M in matrices:
        block=S.Matrix.vstack(M-I,S.zeros(k,n))
        columns.extend(block[:,j] for j in range(n))
    for i,(v,m) in enumerate(zip(powers,orders)):
        b=S.zeros(k,1);b[i]=m
        columns.append(S.Matrix.vstack(-v,b))
    columns.append(S.Matrix.vstack(clutch,S.ones(k,1)))
    relations=S.Matrix.hstack(*columns)
    fs=factors(relations)
    return {'rank':n+k-relations.rank(),'torsion':[d for d in fs if d>1],
            'smith':fs,'relations':relations,'affine_certificates':certificates}

def full_presentation(matrices,numerators,orders,clutch=None):
    """A finite presentation; the image of the fibre need not inject.

    For an aspherical orbifold with three genuine finite points, F.2.31
    additionally proves that the indicated fibre quotient does inject.
    """
    matrices=[integral(M) for M in matrices]
    n=matrices[0].rows;k=len(matrices);I=S.eye(n)
    assert n==6 and k in (2,3)
    clutch=S.zeros(n,1) if clutch is None else integral(clutch)
    product=I
    for M in matrices:product=product*M
    N=integral(product.inv()-I)
    assert N*N==S.zeros(n) and factors(N)==[1,1,1], 'Not a primitive maximal cusp'
    hom=first_homology(matrices,numerators,orders,clutch)
    L,certificate=invariant_closure(matrices,N)
    quotient=factors(L)
    relations={'fibre_generators':[f'x{j+1}' for j in range(n)],
               'peripheral_generators':[f's{i+1}' for i in range(k)],
               'all_fibre_generators_commute':True,
               'conjugation_matrices':[M.tolist() for M in matrices],
               'powers':[{'order':int(m),'fibre_vector':c['power_vector'].tolist()}
                         for m,c in zip(orders,hom['affine_certificates'])],
               'killed_cusp_lattice':hermite_normal_form(N).tolist(),
               'equivalent_normal_closure_lattice':L.tolist(),
               'ordered_product_times_fibre_clutch_equals_identity':clutch.tolist()}
    return {'presentation':relations,'fibre_quotient_free_rank':n-L.cols,
            'fibre_quotient_torsion':[d for d in quotient if d>1],
            'closure_certificate':certificate,
            'H1_free_rank':hom['rank'],'H1_torsion':hom['torsion'],
            'H1_relation_matrix':hom['relations'].tolist(),
            'affine_tests':[{**c,'power_vector':c['power_vector'].tolist()}
                            for c in hom['affine_certificates']]}

def contains_columns(lattice,columns):
    return hermite_normal_form(S.Matrix.hstack(lattice,columns))==hermite_normal_form(lattice)

def norm_matrix(M,m):
    n=M.rows;block=S.eye(2*n)
    block[:n,:n]=M;block[:n,n:]=S.eye(n)
    return integral((block**int(m))[:n,n:])

def two_point_structure(matrices,numerators,orders,clutch=None):
    """The full group as an injected abelian kernel extended by C_gcd.

    No assertion that a presentation's apparent fibre injects is used:
    the additional Euler relation is imposed first, and the resulting
    cyclic-extension construction proves precisely this injection.
    """
    assert len(matrices)==2
    base=full_presentation(matrices,numerators,orders,clutch)
    n=6;M=integral(matrices[0]);L=S.Matrix(base['presentation']['equivalent_normal_closure_lattice'])
    clutch=S.zeros(n,1) if clutch is None else integral(clutch)
    m1,m2=map(int,orders)
    w1,w2=[S.Matrix(p['fibre_vector']) for p in base['presentation']['powers']]
    u,v,d=map(int,S.gcdex(m1,m2))
    assert u*m1+v*m2==d and d>0
    w2prime=-w2-norm_matrix(M,m2)*clutch
    e=integral(S.Rational(m2,d)*w1-S.Rational(m1,d)*w2prime)
    c=u*w1+v*w2prime
    assert contains_columns(L,M**d-S.eye(n))
    assert contains_columns(L,(M-S.eye(n))*c)
    assert contains_columns(L,(M-S.eye(n))*e)
    K=hermite_normal_form(L.row_join(e));fs=factors(K)
    assert contains_columns(K,M*K) and contains_columns(K,M.inv()*K)
    # Independently abelianize the reduced cyclic-extension presentation.
    abelian=S.Matrix.vstack(S.Matrix.hstack(K,M-S.eye(n)),S.zeros(1,K.cols+n))
    abelian=abelian.row_join(S.Matrix.vstack(-c,S.Matrix([d])))
    assert n+1-abelian.rank()==base['H1_free_rank']
    assert [x for x in factors(abelian) if x>1]==base['H1_torsion']
    result={'cyclic_quotient_order':d,'abelian_kernel_relations':K.tolist(),
            'abelian_kernel_free_rank':n-K.cols,
            'abelian_kernel_torsion':[x for x in fs if x>1],
            'action_on_six_marked_fibre_generators':M.tolist(),
            'stable_letter_power_vector':c.tolist(),
            'additional_Euler_relation':e.tolist(),
            'group_order':d*int(S.prod(fs)) if K.cols==n else 'infinite',
            'H1_free_rank':base['H1_free_rank'],'H1_torsion':base['H1_torsion']}
    return result

def three_point_structure(matrices,numerators,orders,clutch=None):
    """Injected fibre kernel over a three-cone orbifold, including spheres.

    In the spherical case the finite triangle group is built explicitly,
    and its transfer Euler vector is computed before asserting injection.
    """
    assert len(matrices)==3 and all(int(m)>=1 for m in orders)
    base=full_presentation(matrices,numerators,orders,clutch)
    matrices=[integral(M) for M in matrices];orders=list(map(int,orders))
    L=S.Matrix(base['presentation']['equivalent_normal_closure_lattice'])
    clutch=S.zeros(6,1) if clutch is None else integral(clutch)
    if 1 in orders:
        i=orders.index(1);suffix=S.eye(6)
        for M in matrices[i+1:]:suffix=suffix*M
        power=S.Matrix(base['presentation']['powers'][i]['fibre_vector'])
        changed=integral(clutch+suffix.inv()*power)
        reduced=two_point_structure(matrices[:i]+matrices[i+1:],
                                   numerators[:i]+numerators[i+1:],
                                   orders[:i]+orders[i+1:],changed)
        assert reduced['H1_free_rank']==base['H1_free_rank']
        assert reduced['H1_torsion']==base['H1_torsion']
        return {'removed_order_one_site':i,'new_clutch':changed.tolist(),
                'two_point_structure':reduced}
    orb=sum(S.Rational(1,m) for m in orders)-1
    if orb<=0:
        return {'orbifold_euler':str(orb),
                'orbifold_geometry':'hyperbolic' if orb<0 else 'euclidean',
                'injected_fibre_relations':L.tolist(),
                'injected_fibre_free_rank':6-L.cols,
                'injected_fibre_torsion':base['fibre_quotient_torsion'],
                'group_order':'infinite',
                'H1_free_rank':base['H1_free_rank'],'H1_torsion':base['H1_torsion']}
    from sympy.combinatorics.named_groups import DihedralGroup, AlternatingGroup, SymmetricGroup
    from sympy.combinatorics.perm_groups import PermutationGroup
    sorted_orders=sorted(orders)
    if sorted_orders[:2]==[2,2]:
        finite=DihedralGroup(sorted_orders[2]);expected=2*sorted_orders[2]
    elif sorted_orders==[2,3,3]:finite=AlternatingGroup(4);expected=12
    elif sorted_orders==[2,3,4]:finite=SymmetricGroup(4);expected=24
    elif sorted_orders==[2,3,5]:finite=AlternatingGroup(5);expected=60
    else:raise AssertionError('Positive Euler triple outside the spherical list')
    elements=list(finite.generate_schreier_sims());identity=finite.identity
    assert len(elements)==expected
    peripheral=None
    for a in elements:
        if a.order()!=orders[0]:continue
        for b in elements:
            if b.order()!=orders[1]:continue
            c=(a*b)**-1
            if c.order()==orders[2] and PermutationGroup([a,b]).order()==expected:
                peripheral=[a,b,c];break
        if peripheral is not None:break
    assert peripheral is not None
    # Breadth-first representatives, with a simultaneous lattice marking.
    rho={identity:S.eye(6)};queue=[identity]
    for g in queue:
        for p,M in zip(peripheral,matrices):
            gp=g*p
            if gp not in rho:rho[gp]=rho[g]*M;queue.append(gp)
    assert len(rho)==expected
    for g in queue:
        for p,M in zip(peripheral,matrices):
            assert contains_columns(L,rho[g]*M-rho[g*p])
    e=sum((rho[g]*clutch for g in queue),S.zeros(6,1))
    transfer=[]
    for p,m,power in zip(peripheral,orders,base['presentation']['powers']):
        w=S.Matrix(power['fibre_vector']);seen=set();part=S.zeros(6,1);count=0
        for g in queue:
            if g in seen:continue
            count+=1;part+=rho[g]*w
            seen.update(g*(p**j) for j in range(m))
        assert count*m==expected and len(seen)==expected
        transfer.append({'cosets':count,'vector':part.tolist()});e+=part
    assert all(contains_columns(L,(M-S.eye(6))*e) for M in matrices)
    K=hermite_normal_form(L.row_join(e));fs=factors(K)
    return {'orbifold_euler':str(orb),'orbifold_geometry':'spherical',
            'orbifold_group_order':expected,
            'marked_finite_permutations':[p.array_form for p in peripheral],
            'local_transfer_vectors':transfer,'Euler_relation':e.tolist(),
            'injected_fibre_relations':K.tolist(),
            'injected_fibre_free_rank':6-K.cols,
            'injected_fibre_torsion':[d for d in fs if d>1],
            'group_order':expected*int(S.prod(fs)) if K.cols==6 else 'infinite',
            'H1_free_rank':base['H1_free_rank'],'H1_torsion':base['H1_torsion']}

if __name__=='__main__':
    A,B=family(0);M1=A.T;M2=B.T;I=S.eye(6)
    ell=kernel(S.Matrix.vstack(M1.T-I,M2.T-I))[:,0].T
    u1=fixed_split(M1,ell,5)['u'];u2=fixed_split(M2,ell,4)['u']
    u3=S.zeros(6,1);u3[0]=1
    assert ell*u3==S.ones(1,1)
    cusp=(M1*M2).inv()-I
    K,bound=invariant_closure([M1,M2,I],cusp)
    assert K==hermite_normal_form(kernel(ell))
    print('fixed numerator1',list(u1),'numerator2',list(-u2),
          'third numerator',list(u3),flush=True)
    print('normal fibre-kernel closure',K.tolist(),'bound',bound,flush=True)
    records=[]
    for m in (2,3,4,5,6,8,10,20,21):
        out=first_homology([M1,M2,I],[u1,-u2,u3],[5,4,m])
        p=abs(m-20)
        assert out['rank']==(m==20)
        assert out['torsion']==([p] if p>1 else [])
        print('m',m,'H1 rank',out['rank'],'torsion',out['torsion'],flush=True)
        records.append({'m':m,**full_presentation([M1,M2,I],[u1,-u2,u3],[5,4,m])})
    # A genuinely non-fixed numerator, and its nonfree comparison.
    R=S.diag(1,-1)
    good=affine_certificate(R,S.Matrix([1,1]),2)
    bad=affine_certificate(R,S.Matrix([0,1]),2)
    assert good['free'] and good['power_vector']==S.Matrix([1,0])
    assert not bad['free']
    # Check the finite-index stage of the closure certificate independently.
    swap=S.Matrix([[0,1],[1,0]])
    closure,index_certificate=invariant_closure([swap],S.diag(2,3))
    assert closure==S.eye(2) and index_certificate['post_rank_stability_bound']==2
    print('non-fixed affine numerator accepted with power vector [1,0]; reflection comparison rejected',flush=True)
    print('finite-index closure test',index_certificate,flush=True)
    two_point=[]
    for m1,m2,clutch_coefficient in [(5,4,0),(10,8,0),(15,8,1),(10,12,-1)]:
        cvec=clutch_coefficient*u3
        rec=two_point_structure([M1,M2],[u1,-u2],[m1,m2],cvec)
        print('two-point cyclic extension',m1,m2,'clutch',clutch_coefficient,
              'quotient',rec['cyclic_quotient_order'],
              'kernel rank',rec['abelian_kernel_free_rank'],
              'kernel torsion',rec['abelian_kernel_torsion'],
              'group order',rec['group_order'],flush=True)
        two_point.append({'orders':[m1,m2],'clutch_coefficient':clutch_coefficient,**rec})
    # A nonabelian two-point input in the full GL6 scope; the two caps
    # reverse orientation, so this is not asserted to be a complex example.
    C=S.diag(-1,1,1);J=S.zeros(6);J[:3,3:]=S.eye(3)
    R1=S.diag(-C,C);R2=R1*(S.eye(6)+J)
    v1=S.eye(6)[:,4];v2=S.eye(6)[:,0];v3=S.eye(6)[:,5]
    nonabelian=two_point_structure([R1,R2],[v1,v2],[2,4])
    assert nonabelian['abelian_kernel_free_rank']==2
    assert nonabelian['abelian_kernel_torsion']==[2]
    assert nonabelian['H1_free_rank']==1 and nonabelian['H1_torsion']==[2,4]
    print('nonabelian GL6 test: kernel Z^2+Z2, cyclic quotient2; H1=Z+Z2+Z4',flush=True)
    spherical=three_point_structure([R1,R2,I],[v1,v2,v3],[2,4,2])
    assert spherical['orbifold_group_order']==8
    assert spherical['injected_fibre_free_rank']==2
    assert spherical['injected_fibre_torsion']==[4]
    print('spherical triangle test: orbifold order8, injected kernel Z^2+Z4',flush=True)
    hyperbolic=three_point_structure([M1,M2,I],[u1,-u2,u3],[5,4,19])
    assert hyperbolic['injected_fibre_free_rank']==1
    assert hyperbolic['H1_free_rank']==0 and hyperbolic['H1_torsion']==[]
    print('hyperbolic triangle test: infinite perfect group with injected central Z',flush=True)
    padded=three_point_structure([M1,M2,I],[u1,-u2,u3],[5,4,1])
    assert padded['two_point_structure']['group_order']==19
    print('order-one elimination test: new clutch u3 and group Z19',flush=True)
    (Path(__file__).resolve().parents[1]/'records/fourfolds_vankampen.json').write_text(
        json.dumps({'three_point_family':records,'nonfixed_affine_test':{
          'power_vector':good['power_vector'].tolist(),
          'prime_subgroup_tests':good['prime_subgroup_tests']},
          'finite_index_closure':index_certificate,'two_point_extensions':two_point,
          'nonabelian_GL6_test':nonabelian,'spherical_test':spherical,
          'hyperbolic_test':hyperbolic,'order_one_test':padded},indent=2,default=int)+'\n')
    print('ALL NINE GENERAL-PRESENTATION H1 TESTS PASSED',flush=True)
