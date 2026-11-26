#!/usr/bin/env python3
"""Fresh LF calculation from defining elliptic profiles only.

No target proof, historical target algorithm, or target-derived table is read.
Exact integer sections, inverse period maps, and all output are retained.
The geometric and primary-operation arguments are in the accompanying proof;
this program checks their finite arithmetic and literal matrix identities.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product, combinations
from math import gcd
from functools import reduce
from datetime import datetime, timezone
import csv
import hashlib
import json
import sympy as sp

W = Path(__file__).resolve().parents[1]
LANE = W / 'agents/continuation7_iii_three_primary'
RAW = W / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
PREFIX = 'S6_SERIES_PUBLISH_III_02LF'
J = sp.Matrix([[0, 1], [-1, 0]])
I2, I4, I6 = sp.eye(2), sp.eye(4), sp.eye(6)
PAIRS = list(combinations(range(4), 2))
FINITE = {'II': (6, 1), 'III': (4, 2), 'IV': (3, 3),
          'III*': (4, 2), 'IV*': (3, 3)}


def ints(M):
    assert all(sp.denom(x) == 1 for x in M)
    return [[int(x) for x in M.row(i)] for i in range(M.rows)]


def matstr(M):
    return json.dumps(ints(M), separators=(',', ':'))


def egcd(a, b):
    r0, r1, s0, s1, t0, t1 = abs(a), abs(b), 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q*r1
        s0, s1 = s1, s0 - q*s1
        t0, t1 = t1, t0 - q*t1
    return r0, s0 * (1 if a >= 0 else -1), t0 * (1 if b >= 0 else -1)


def smith(M0):
    """Tracked elementary integer operations: U*M0*V = D."""
    M = sp.Matrix(M0)
    U, V = sp.eye(M.rows), sp.eye(M.cols)

    def radd(i, j, q):
        M[i, :] = M[i, :] + q*M[j, :]
        U[i, :] = U[i, :] + q*U[j, :]

    def cadd(i, j, q):
        M[:, i] = M[:, i] + q*M[:, j]
        V[:, i] = V[:, i] + q*V[:, j]

    for k in range(min(M.rows, M.cols)):
        nz = [(abs(M[i, j]), i, j) for i in range(k, M.rows)
              for j in range(k, M.cols) if M[i, j]]
        if not nz:
            break
        _, i, j = min(nz)
        M.row_swap(k, i); U.row_swap(k, i)
        M.col_swap(k, j); V.col_swap(k, j)
        while True:
            reduced = False
            for i in range(k+1, M.rows):
                if M[i, k]:
                    q = M[i, k] // M[k, k]
                    radd(i, k, -q)
                    if M[i, k]:
                        M.row_swap(i, k); U.row_swap(i, k)
                    reduced = True
                    break
            if reduced:
                continue
            for j in range(k+1, M.cols):
                if M[k, j]:
                    q = M[k, j] // M[k, k]
                    cadd(j, k, -q)
                    if M[k, j]:
                        M.col_swap(j, k); V.col_swap(j, k)
                    reduced = True
                    break
            if reduced:
                continue
            bad = [(i, j) for i in range(k+1, M.rows)
                   for j in range(k+1, M.cols) if M[i, j] % M[k, k]]
            if not bad:
                break
            radd(k, bad[0][0], 1)
        if M[k, k] < 0:
            M[k, :] = -M[k, :]
            U[k, :] = -U[k, :]
    assert U*M0*V == M
    assert abs(U.det()) == abs(V.det()) == 1
    assert all(M[i, j] == 0 for i in range(M.rows)
               for j in range(M.cols) if i != j)
    diag = [int(M[i, i]) for i in range(min(M.rows, M.cols)) if M[i, i]]
    assert all(y % x == 0 for x, y in zip(diag, diag[1:]))
    return M, U, V


def section(M, B):
    """Return literal integer X with M*X=B, not only invariant factors."""
    D, U, V = smith(M)
    C = U*B
    Z = sp.zeros(M.cols, B.cols)
    rank = 0
    for i in range(M.rows):
        di = D[i, i] if i < M.cols else 0
        if di:
            rank += 1
            for j in range(B.cols):
                assert C[i, j] % di == 0
                Z[i, j] = C[i, j] // di
        else:
            assert all(x == 0 for x in C.row(i))
    X = V*Z
    assert M*X == B
    return X, [int(D[i, i]) for i in range(rank)]


def mult_type(t):
    return t.startswith('I') and t[1:].isdigit()


def primitive(A, g):
    N = A-I2
    nu = reduce(gcd, (abs(int(x)) for x in N), 0)
    col = next(N[:, j] for j in range(2) if N[:, j] != sp.zeros(2, 1))
    h = reduce(gcd, (abs(int(x)) for x in col), 0)
    u = col/h
    if next(x for x in u if x) < 0:
        u = -u
    assert N == nu*u*(u.T*J)
    den, xx, yy = egcd(int(u[0]), int(u[1]))
    assert den == 1
    v = sp.Matrix([-yy, xx])
    assert (u.row_join(v)).det() == 1
    kappa = next(sp.Rational(g[i], u[i]) for i in range(2) if u[i])
    assert sp.denom(kappa) == 1 and g == kappa*u
    return nu, u, v, int(kappa)


def narrow(comp, a):
    return all((a * int(row[0])) % int(d) == 0
               for d, row in zip(comp['moduli'], comp['rows']))


def wedge(T):
    return sp.Matrix([[T[i,k]*T[j,l]-T[i,l]*T[j,k]
                       for k,l in PAIRS] for i,j in PAIRS])


def lift2(v):
    return sp.Matrix([v[0], v[1], 0, 0])


def catalogue(raw):
    natural, counts = [], []
    for r in raw['rows']:
        As = [sp.Matrix(A) for A in r['elliptic_matrices']]
        gs = [sp.Matrix(g) for g in r['generator_section_cocycle']]
        height = Fraction(r['height_of_generator'])
        assert height.numerator == 1
        d = height.denominator
        local = []
        for zero, t in enumerate(r['fibers']):
            if not mult_type(t):
                continue
            nu,u,v,kappa = primitive(As[zero], gs[zero])
            assert nu == int(t[1:])
            if d % nu:
                continue
            ab = d//nu
            for a in range(1, ab+1):
                if ab % a:
                    continue
                b = ab//a
                if gcd(a,b) != 1 or gcd(b*kappa,nu) != 1:
                    continue
                lhs = [0]*nu
                rhs = [0]*nu
                for c, j in [(1,a*kappa),(-1,0),(-1,(a-b)*kappa),(1,-b*kappa)]:
                    lhs[j % nu] += c
                for c,j in [(-2,0),(1,1),(1,-1)]:
                    rhs[j % nu] += c
                if lhs != rhs:
                    continue
                if not all(i == zero or narrow(c,a) or narrow(c,b)
                           for i,c in enumerate(r['component_coordinates'])):
                    continue
                item = {'raw':r,'a':a,'b':b,'zero':zero}
                local.append(item); natural.append(item)
        counts.append((r['OS'],r['profile'],len(local)))
    return natural, counts


def expand(natural):
    answer = []
    for row in natural:
        r,a,b,z0 = row['raw'],row['a'],row['b'],row['zero']
        if any(t.endswith('*') and t.startswith('I') and t[1:-1].isdigit()
               for t in r['fibers']):
            continue
        choices=[]
        sites=[]
        for i,t in enumerate(r['fibers']):
            if mult_type(t):
                continue
            sites.append(i)
            opts=[]
            A=sp.Matrix(r['elliptic_matrices'][i]); g=sp.Matrix(r['generator_section_cocycle'][i])
            zi=(A-I2).inv()*g
            order,q=FINITE[t]
            if all(sp.denom(x)==1 for x in b*zi):
                opts.append(('F',order,q))
            if t in {'II','III','IV'} and narrow(r['component_coordinates'][i],a) and gcd(b,q)==1:
                opts.append(('O',1,1))
            choices.append(opts)
        for opts in product(*choices):
            fin=[x[1] for x in opts if x[0]=='F']
            if any(gcd(x,y)>1 for x,y in combinations(fin,2)):
                continue
            qtot=1
            for x in opts:
                qtot*=x[2]
            if b == 3*qtot:
                arow=dict(row)
                arow['options']={str(i):o[0] for i,o in zip(sites,opts)}
                arow['qtot']=qtot
                answer.append(arow)
    return sorted(answer,key=lambda x:(x['raw']['OS'],x['raw']['profile'],x['a'],x['b'],x['zero'],str(x['options'])))


def analyse(row, number):
    raw,a,b,z0 = row['raw'],row['a'],row['b'],row['zero']
    name=str(raw['OS'])+('' if raw['profile']=='default' else '/'+raw['profile'])
    As=[sp.Matrix(x) for x in raw['elliptic_matrices']]
    gs=[sp.Matrix(x) for x in raw['generator_section_cocycle']]
    Omega=sp.diag(1,1,1,1)*0
    Omega[0,1]=a;Omega[1,0]=-a;Omega[2,3]=-b;Omega[3,2]=b
    omega=sp.Matrix([[a,0,0,0,0,-b]])
    delta=sp.Matrix([0,0,1,0]); gamma=sp.Matrix([0,0,0,1])
    print(f'\nPATTERN {number}: {name} a={a} b={b} zero={z0} options={row["options"]}')
    print('fibres='+str(raw['fibers'])+' height='+raw['height_of_generator'])
    print('A='+json.dumps(raw['elliptic_matrices'],separators=(',',':')))
    print('g='+json.dumps(raw['generator_section_cocycle'],separators=(',',':')))
    Ts=[]; invs=[]; locals_data=[]; fixed_bases=[]; angular_columns=[]
    E_sites=[]
    for i,(typ,A,g) in enumerate(zip(raw['fibers'],As,gs)):
        beta=-a*g.T*J*A
        if mult_type(typ):
            nu,u,v,kappa=primitive(A,g)
            zi=sp.Rational(kappa,nu)*v
        else:
            zi=(A-I2).inv()*g
        c=(beta*(b*zi))[0]+(sp.Rational(1,nu) if i==z0 else 0)
        T=sp.eye(4)
        T[:2,:2]=A;T[:2,3]=b*g;T[2,:2]=beta;T[2,3]=c
        Ti=sp.eye(4)
        Ti[:2,:2]=A.inv();Ti[:2,3]=-b*A.inv()*g
        Ti[2,:2]=-beta*A.inv();Ti[2,3]=(b*beta*A.inv()*g)[0]-c
        ints(T);ints(Ti)
        assert T*Ti==I4==Ti*T and T.T*Omega*T==Omega
        assert T*delta==delta and T[3,:]==gamma.T
        Ts.append(T);invs.append(Ti)
        print(f'  site {i} {typ}: T={matstr(T)} inverse={matstr(Ti)}')
        loc={'site':i,'type':typ,'T':ints(T),'inverse':ints(Ti)}
        if i==z0:
            rho=sp.Rational(1-a*b*kappa*kappa,nu)
            C=sp.Matrix([[nu,b*kappa],[-a*kappa,rho]])
            Ci=sp.Matrix([[rho,-b*kappa],[a*kappa,nu]])
            S=lift2(u).row_join(delta);L=lift2(v).row_join(gamma)
            assert C*Ci==I2 and (T-I4)*L==S*C and (T-I4)*S==sp.zeros(4,2)
            K=C.T*sp.diag(a,-b)
            assert K==K.T and (S*C).T*Omega*L==K
            dshort=Ci*sp.Matrix([0,1])
            assert dshort==sp.Matrix([-b*kappa,nu])
            k=b*kappa
            Acurve=a*(nu-k)
            cD=b*(a*kappa*(k-nu)-1)
            eunit=nu*(k-nu)
            assert k%3==0 and nu%3!=0 and cD%3==0
            qC=(pow(Acurve,3,9)*pow(k,2,9)*pow(eunit,-1,9))%9
            assert qC==0
            weights=[[k-nu,nu,-k],[-nu,nu-k,k]]
            loc.update({'u':ints(u),'v':ints(v),'kappa':kappa,'nu':nu,
                        'C':ints(C),'C_inverse':ints(Ci),'K':ints(K),
                        'delta_short':ints(dshort),'north_south_weights':weights,
                        'doubled_character':int(cD),'alpha_C':Acurve,
                        'normal_Euler_unit_mod9':eunit%9,'Q3_C':qC})
            print(f'    cusp u={matstr(u)} v={matstr(v)} kappa={kappa} nu={nu}')
            print(f'    C={matstr(C)} C_inverse={matstr(Ci)} K={matstr(K)} delta_short={matstr(dshort)}')
            print(f'    north/south={weights}; doubled_character={cD}; alpha_C={Acurve}; Euler_unit9={eunit%9}; Q3_C={qC}')
            cusp=loc
            fixed_bases.append(delta.row_join(lift2(u)))
            angular_columns.extend([lift2(u),delta])
        elif mult_type(typ):
            d0=gcd(nu,a*kappa);n0=nu//d0;A0=a*kappa//d0
            B0=sp.Rational(b*kappa,n0);assert sp.denom(B0)==1;B0=int(B0)
            _,t,sigma=egcd(n0,A0)
            _,x,y=egcd(d0,B0)
            CS=sp.Matrix([[n0,sigma],[-A0,t]])
            CL=sp.Matrix([[x,-B0],[y,d0]])
            CSi=sp.Matrix([[t,-sigma],[A0,n0]])
            CLi=sp.Matrix([[d0,B0],[-y,x]])
            assert CS*CSi==I2 and CL*CLi==I2
            S=lift2(u).row_join(delta)*CS;L=lift2(v).row_join(gamma)*CL
            f=sp.Matrix([[*(d0*u.T*J),0,B0]])
            assert T-I4==S[:,0]*f
            assert (T-I4)*L==S*sp.Matrix([[1,0],[0,0]])
            K=S.T*Omega*L
            assert K[0,0]==sp.Rational(a*nu,d0*d0) and K[0,1]==0
            assert K[1,1]==sp.Rational(-b*d0*d0,nu)
            assert delta==-sigma*S[:,0]+n0*S[:,1]
            fixes=n0%3==0
            if fixes:
                E_sites.append(i)
                assert nu==3 and d0==1 and n0==3
                assert (-sigma*K[0,0])%3==0
                assert K[1,1]==-b//3
            loc.update({'u':ints(u),'v':ints(v),'kappa':kappa,'nu':nu,
                        'd0':d0,'n0':n0,'CS':ints(CS),'CS_inverse':ints(CSi),
                        'CL':ints(CL),'CL_inverse':ints(CLi),'K':ints(K),
                        'delta_coefficients':[-sigma,n0],'C3_fixed_core':fixes})
            print(f'    rank-one nu={nu} kappa={kappa} d0={d0} n0={n0}; CS={matstr(CS)} CSinv={matstr(CSi)}; CL={matstr(CL)} CLinv={matstr(CLi)}')
            print(f'    K={matstr(K)} delta_coefficients={[-sigma,n0]} C3_fixed_core={fixes}')
            fixed_bases.append(delta.row_join(lift2(u)).row_join(L[:,1]))
            angular_columns.append(S[:,0])
        else:
            order,q=FINITE[typ]
            ell=sp.Matrix([-b*zi[0],-b*zi[1],0,1])
            assert T*ell==ell
            power=I4
            norm=sp.zeros(4,4)
            for j in range(order):
                norm+=power;power=power*T
            assert power==I4
            if row['options'][str(i)]=='F':
                ints(ell)
                comb=(T-I4).row_join(q*I4)
                solve,diag=section(comb,delta)
                yy=solve[:4,:];bb=solve[4:,:]
                assert q*bb+(T-I4)*yy==delta
                assert norm*bb==(order//q)*delta and norm*ell==order*ell
                assert -(bb.T*Omega*ell)[0]==sp.Rational(b,q)
                gen=(T-I4).row_join(bb).row_join(ell)
                inv_section,diag_full=section(gen,I4)
                assert gen*inv_section==I4
                loc.update({'order':order,'q':q,'ell':ints(ell),'beta0':ints(bb),
                            'delta_preimage':ints(yy),'coinvariant_section':ints(inv_section),
                            'norm':ints(norm),'inverse_coinvariant_coordinates':ints(inv_section[-2:,:])})
                print(f'    finite order={order} q={q}; ell={matstr(ell)} beta0={matstr(bb)} y={matstr(yy)}')
                print(f'    norm={matstr(norm)}; (T-I,beta0,ell) section={matstr(inv_section)}')
                print(f'    inverse coinvariant coordinates={matstr(inv_section[-2:,:])}; -Omega(beta0,ell)={b//q}')
                fixed_bases.append(delta.row_join(ell))
            else:
                assert typ in {'II','III','IV'} and narrow(raw['component_coordinates'][i],a) and gcd(b,q)==1
                fixed_index=int(sp.ilcm(*[sp.denom(x) for x in ell]))
                ell_original=fixed_index*ell
                ints(ell_original)
                assert fixed_index==q and T*ell_original==ell_original
                print(f'    original: P narrow, Q single component orbit, primitive fixed return={matstr(ell_original)}, gamma index={fixed_index}; both fixed sweeps bound')
                loc.update({'order':order,'q':q,'fixed_return':ints(ell_original),
                            'fixed_gamma_index':fixed_index,'original_zero_Chern_single_orbit':True})
                fixed_bases.append(delta.row_join(ell_original))
        locals_data.append(loc)
    prod=I4
    for T in Ts:
        prod=prod*T
    assert prod==I4
    K1=sp.Matrix.hstack(*angular_columns)[:3,:]
    K1_inverse,diag_K1=section(K1,sp.eye(3))
    assert diag_K1==[1,1,1]
    # Include the removed ordinary disc as the last identity-monodromy site.
    graph_T=Ts+[I4]
    graph_F=fixed_bases+[delta.row_join(I4[:,0]).row_join(I4[:,1]).row_join(gamma)]
    D=sp.Matrix.hstack(*[T-I4 for T in graph_T[:-1]])
    graph_blocks=[]
    delta_columns=[]
    col_count=0
    for i,F in enumerate(graph_F):
        assert graph_T[i]*F==F and F[:,0]==delta
        delta_columns.append(col_count);col_count+=F.cols
        if i<len(graph_T)-1:
            Ji=sp.zeros(D.cols,4);Ji[4*i:4*i+4,:]=I4
        else:
            tails=[]
            for j in range(len(graph_T)-1):
                tail=I4
                for Tj in graph_T[j+1:-1]:
                    tail=tail*Tj
                tails.append(-tail)
            Ji=sp.Matrix.vstack(*tails)
            assert D*Ji==I4-graph_T[-1].inv()
        graph_blocks.append(Ji*F)
    B=sp.Matrix.hstack(*graph_blocks)
    assert D*B==sp.zeros(D.rows,B.cols)
    DD,UD,VD=smith(D)
    rank_D=sum(DD[i,i]!=0 for i in range(min(DD.rows,DD.cols)))
    assert rank_D==3
    kernel_D=VD[:,rank_D:]
    graph_section,diag_B=section(B,kernel_D)
    assert diag_B==[1]*(D.cols-3)
    graph_inverse=graph_section*VD.inv()[rank_D:,:]
    assert B*graph_inverse*kernel_D==kernel_D
    relation=sp.zeros(B.cols,1)
    for j in delta_columns:relation[j]=1
    assert B*relation==sp.zeros(B.rows,1)
    assert B.cols-len(diag_B)==1
    B1=sp.Matrix.hstack(*[(T-I4)[:3,:] for T in Ts])
    R1,diag1=section(B1,sp.eye(3))
    B2=sp.Matrix.hstack(*[wedge(T)-I6 for T in Ts])
    d,x,y=egcd(a,b);assert d==1
    s0=sp.Matrix([x,0,0,0,0,-y])
    assert omega*s0==sp.ones(1,1) and omega*B2==sp.zeros(1,B2.cols)
    P=s0.row_join(sp.Matrix([b,0,0,0,0,a]))
    for j in [1,2,3,4]:
        P=P.row_join(I6[:,j])
    assert abs(P.det())==1
    R2,diag2=section(B2,I6-s0*omega)
    assert diag1==[1,1,1] and diag2==[1,1,1,1,1]
    assert len(E_sites)==1
    alphaE=-b//3
    p1=(-2*(cusp['alpha_C']+alphaE))%3
    assert p1==0
    print('  ordered product=I4; B1 Smith='+str(diag1)+'; B1 right inverse='+matstr(R1))
    print('  Actual cap angular K1='+matstr(K1)+'; K1 integral right inverse='+matstr(K1_inverse))
    print('  Full exterior fixed bases, including ordinary disc='+json.dumps([ints(F) for F in graph_F],separators=(',',':')))
    print('  Graph D rank=3; B Smith='+str(diag_B)+'; sole primitive relation='+matstr(relation))
    print('  Graph inverse on ker(D)='+matstr(graph_inverse))
    print('  wedge omega='+matstr(omega)+'; s0='+matstr(s0)+'; primitive P='+matstr(P)+'; inverse='+matstr(P.inv()))
    print('  B2 Smith='+str(diag2)+'; B2*R2=I-s0*omega with R2='+matstr(R2))
    print(f'  C3 fixed components: C at {z0}, E at {E_sites[0]}; alpha_E={alphaE}; p1_pairing_mod3={p1}; refined_P={p1}; Q3_C=0')
    print('  Q3_E=0 by the proved suspension map to BC3 x S1 and Thomas 1956 (2.6)-(2.7), 1959 Theorem I(ii); this is a primary-input step, not a numeric test.')
    print('  Full mu in Z/9=0, with positive CP3 generator; H2 inverse [v] -> omega(v), 1 -> [s0].')
    return {'number':number,'OS':raw['OS'],'profile':raw['profile'],'a':a,'b':b,'zero':z0,
            'options':row['options'],'qtot':row['qtot'],'raw':raw,'locals':locals_data,
            'B1':ints(B1),'R1':ints(R1),'omega':ints(omega),'s0':ints(s0),
            'K1':ints(K1),'K1_right_inverse':ints(K1_inverse),
            'graph_D':ints(D),'graph_B':ints(B),'graph_inverse':ints(graph_inverse),
            'graph_relation':ints(relation),'graph_fixed_bases':[ints(F) for F in graph_F],
            'P':ints(P),'P_inverse':ints(P.inv()),'B2':ints(B2),'R2':ints(R2),
            'fixed_E':E_sites[0],'alpha_E':alphaE,'p1_pairing':p1,'refined_P':p1,'mu_Z9':0}


def symbolic_kernel():
    b,q,m,n,r,e,eps=sp.symbols('b q m n r e eps', integer=True)
    al=eps*e;eta=-eps
    C1=sp.Matrix([b*n/q,m/q,0]);C2=sp.Matrix([-b*r,0,m]);C3=sp.Matrix([0,r,n])
    K0=al*C2+eta*C3
    # The single relation n=m*e-eps and eps^2=1 is exact simple connectivity.
    def red(M):
        return M.applyfunc(lambda z:sp.rem(sp.expand(z.subs(n,m*e-eps)),eps**2-1,eps).simplify())
    assert red(K0-sp.Matrix([-al*b*r,eta*r,1]))==sp.zeros(3,1)
    assert red(C2-m*K0+eta*q*r*C1)==sp.zeros(3,1)
    assert red(C3-n*K0-al*q*r*C1)==sp.zeros(3,1)
    assert sp.expand(al+eta*e)==0
    print('\nUNBOUNDED FINITE-PARAMETER IDENTITIES')
    print('m=d*k, k>0; n=m*e-epsilon; epsilon=+/-1; r arbitrary; hence gcd(m,n)=1.')
    print('alpha=epsilon*e, eta=-epsilon, alpha*m+eta*n=1.')
    print('C1=(bn/q,m/q,0), C2=(-br,0,m), C3=(0,r,n).')
    print('K0=alpha*C2+eta*C3=(-alpha*b*r,eta*r,1).')
    print('C2-m*K0=-eta*q*r*C1; C3-n*K0=alpha*q*r*C1.')
    print('D=-b*e*s implies L=b*r*(alpha+eta*e)*s=0; remaining relation=-3*epsilon*s.')
    print('Affine power: t -> t+(I-T)h; norm map v -> v+N_m lambda; inverses use -h and -lambda.')


def main():
    raw_bytes=RAW.read_bytes()
    raw=json.loads(raw_bytes)
    print('Fresh LF exact arithmetic; UTC '+datetime.now(timezone.utc).isoformat())
    print('Raw fixture '+str(RAW.relative_to(W)))
    print('Raw SHA256 '+hashlib.sha256(raw_bytes).hexdigest())
    print('Source '+str(Path(__file__).relative_to(W)))
    print('Source SHA256 '+hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    natural,counts=catalogue(raw)
    print('Natural initial row counts by complete raw profile:')
    for os,profile,num in counts:
        print(f'  {os}/{profile}: {num}')
    print('Natural total='+str(len(natural)))
    assert len(natural)==172 and len(counts)==21
    rows=expand(natural)
    print('Expanded residual-order-three patterns='+str(len(rows)))
    assert len(rows)==8
    data=[analyse(row,i+1) for i,row in enumerate(rows)]
    symbolic_kernel()
    LANE.mkdir(parents=True,exist_ok=True)
    data_path=LANE/(PREFIX+'_fresh_data_v003.json')
    data_path.write_text(json.dumps({'scope':'fresh raw arithmetic; geometric operation inputs stated separately',
                                   'natural_counts':counts,'natural_total':len(natural),'patterns':data},
                                  indent=2)+'\n')
    tab=LANE/(PREFIX+'_fresh_patterns_v003.tsv')
    with tab.open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n')
        w.writerow(['No','OS','profile','a','b','zero','additive','kappa','nu','alpha_C','alpha_E','mu_Z9','refined_P'])
        for d in data:
            c=d['locals'][d['zero']]
            w.writerow([d['number'],d['OS'],d['profile'],d['a'],d['b'],d['zero'],d['options'],c['kappa'],c['nu'],c['alpha_C'],d['alpha_E'],d['mu_Z9'],d['refined_P']])
    for p in [data_path,tab]:
        print('Saved '+str(p.relative_to(W))+' SHA256 '+hashlib.sha256(p.read_bytes()).hexdigest())
    print('All eight patterns and every displayed exact inverse verified; no historical target program executed.')


if __name__=='__main__':
    main()
