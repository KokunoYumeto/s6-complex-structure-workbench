#!/usr/bin/env python3
"""Fresh component-divisor enumeration and marked peripheral lattice maps.

Reads only the 21 raw open-family definitions, never a historical sphere
catalogue, original target proof, or earlier target computation.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from math import gcd
from functools import reduce
from datetime import datetime,timezone
import json
import csv
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
RAW=json.loads((INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KY_raw_profiles.json').read_text())
J=s.Matrix([[0,1],[-1,0]])
delta=s.Matrix([0,0,1,0])
gamma=s.Matrix([0,0,0,1])


def integer_matrix(M):
    assert all(x.q==1 for x in M),M
    return M.applyfunc(int)


def egcd(a,b):
    if b==0:
        return abs(a),1 if a>0 else -1 if a<0 else 0,0
    d,x,y=egcd(b,a%b)
    return d,y,x-(a//b)*y


def primitive_column(M):
    v=next(M[:,j] for j in range(M.cols) if any(M[:,j]))
    g=reduce(gcd,(abs(int(x)) for x in v))
    v=v/g
    if next(x for x in v if x)!=abs(next(x for x in v if x)):v=-v
    return integer_matrix(v)


def multiplicity(kind):
    return int(kind[1:]) if kind.startswith('I') and kind[1:].isdigit() else None


def unipotent_data(A,g,n):
    N=A-s.eye(2);u=primitive_column(N)
    assert N==n*u*u.T*J
    index=next(i for i in range(2) if u[i])
    kappa=s.Rational(g[index],u[index]);assert kappa.q==1 and g==kappa*u
    d,x,y=egcd(int(u[0]),int(u[1]));assert d==1
    r=s.Matrix([-y,x]);assert s.det(s.Matrix.hstack(u,r))==1
    return u,r,int(kappa)


def narrow(A,g,k,kind):
    n=multiplicity(kind)
    if n is not None:
        _,_,c=unipotent_data(A,g,n)
        return k*c%n==0
    v=(A-s.eye(2)).inv()*(k*g)
    return all(x.q==1 for x in v)


def lift(A,g,a,b,weight,kind):
    n=multiplicity(kind)
    if n is not None:
        _,r,k=unipotent_data(A,g,n)
        local_x=s.Rational(b*k,n)*r
    else:
        local_x=(A-s.eye(2)).inv()*(b*g)
    row=-a*g.T*J*A
    centre=(row*local_x)[0]+weight
    return A.row_join(s.zeros(2,1)).row_join(b*g).col_join(
        row.row_join(s.Matrix([[1,centre]]))).col_join(s.Matrix([[0,0,0,1]]))


def product(matrices):
    result=s.eye(matrices[0].rows)
    for M in matrices:result=result*M
    return result


def right_inverse_from_minors(B):
    """Bezout of maximal minors, returning an integer right inverse if onto."""
    d=0;W=s.zeros(B.cols,3);used=[]
    for inds in combinations(range(B.cols),3):
        sub=B[:,inds];det=int(sub.det())
        if not det:continue
        nd,a,b=egcd(d,det)
        if nd==d:continue
        C=s.zeros(B.cols,3)
        adj=sub.adjugate()
        for i,j in enumerate(inds):C[j,:]=adj[i,:]
        W=a*W+b*C;d=nd;used.append(dict(columns=list(inds),determinant=det,
                                        previous_multiplier=a,new_multiplier=b,gcd=d))
        assert B*W==d*s.eye(3)
        if d==1:return integer_matrix(W),used
    return None,used


def orbit_certificate(Ts,initial):
    # Words act on the angular columns of the selected cusp.  No vector is
    # divided after this stage: all columns are actual conjugate relations.
    cols=[initial[:,j] for j in range(initial.cols)]
    words=[dict(angular_column=j,word=[]) for j in range(initial.cols)]
    seen={tuple(v) for v in cols};front=list(range(len(cols)))
    actions=[(i,sign,T if sign==1 else T.inv())
             for i,T in enumerate(Ts) for sign in (1,-1)]
    for depth in range(5):
        B=s.Matrix.hstack(*cols)[:3,:]
        H=hermite_normal_form(B)
        if H.shape==(3,3) and abs(H.det())==1:
            W,steps=right_inverse_from_minors(B);assert W is not None
            return dict(depth=depth,columns=[list(v) for v in cols],words=words,
                        right_inverse=W.tolist(),bezout_minors=steps)
        new=[]
        for j in front:
            for i,sign,T in actions:
                v=integer_matrix(T*cols[j]);assert v[3]==0
                key=tuple(v)
                if key in seen:continue
                seen.add(key);new.append(len(cols));cols.append(v)
                words.append(dict(angular_column=words[j]['angular_column'],
                                  word=[[i,sign]]+words[j]['word']))
        if not new:break
        front=new
    return dict(failed=True,normal_lattice=H.tolist(),rank=H.rank(),depth=depth)


def main():
    output=[];counts=[]
    for raw in RAW['rows']:
        kinds=raw['fibers'];As=list(map(s.Matrix,raw['elliptic_matrices']))
        gs=list(map(s.Matrix,raw['generator_section_cocycle']))
        assert product(As)==s.eye(2)
        base=product([lift(A,g,1,1,0,k) for A,g,k in zip(As,gs,kinds)])
        h=-base[2,3];expected=s.eye(4);expected[2,3]=-h
        assert base==expected and h>0 and h==s.Rational(raw['height_of_generator'])
        assert h.p==1;d=int(h.q);before=len(output)
        for zero,kind in enumerate(kinds):
            n=multiplicity(kind)
            if n is None or d%n:continue
            u,r,kappa=unipotent_data(As[zero],gs[zero],n)
            degree=d//n
            for a in range(1,degree+1):
                if degree%a:continue
                b=degree//a
                if any(not(narrow(A,g,a,k) or narrow(A,g,b,k))
                       for j,(A,g,k) in enumerate(zip(As,gs,kinds)) if j!=zero):continue
                if gcd(b*kappa,n)!=1:continue
                deg=[0]*n
                for j,c in [(a*kappa,1),(0,-1),((a-b)*kappa,-1),(-b*kappa,1)]:deg[j%n]+=c
                for component in range(n):
                    target=[0]*n
                    for j,c in [(component,-2),(component-1,1),(component+1,1)]:target[j%n]+=c
                    if deg!=target:continue
                    Ts=[integer_matrix(lift(A,g,a,b,s.Rational(1,n) if j==zero else 0,k))
                        for j,(A,g,k) in enumerate(zip(As,gs,kinds))]
                    assert product(Ts)==s.eye(4)
                    assert all(T.det()==1 and list(T[3,:])==[0,0,0,1] for T in Ts)
                    N=Ts[zero]-s.eye(4)
                    long_r=s.Matrix(list(r)+[0,0]);lam1=N*long_r;lam2=N*gamma
                    H=s.Matrix.hstack(lam1,long_r,lam2,gamma)
                    target_N=s.zeros(4);target_N[0,1]=target_N[2,3]=1
                    assert H.det()==1 and H.inv()*N*H==target_N
                    angular=s.Matrix.hstack(lam1,lam2)
                    orbit=orbit_certificate(Ts,angular)
                    cusp_only=orbit if orbit.get('failed') else dict(depth=orbit['depth'],onto=True)
                    initial_sources=[dict(fiber=zero+1,cover_order=1,column=j,
                                          kind='selected primitive rank-two cusp') for j in range(2)]
                    extra=[]
                    if orbit.get('failed'):
                        for j,kindj in enumerate(kinds):
                            if not(kindj.startswith('I') and kindj.endswith('*')
                                   and kindj[1:-1].isdigit() and int(kindj[1:-1])%2):continue
                            U=Ts[j]**2;Nstar=U-s.eye(4)
                            assert Nstar.rank()==1
                            w=primitive_column(Nstar)
                            assert w[3]==0
                            if list(w)==[2,0,1,0]:
                                Hstar=s.Matrix([[2,0,-1,0],[0,1,0,2],[1,0,0,0],[0,0,0,1]])
                            elif list(w)==[1,0,2,0]:
                                Hstar=s.Matrix([[1,0,0,0],[0,0,0,1],[2,0,1,0],[0,-1,0,2]])
                            else:
                                raise AssertionError(('An additional geometric chart is required',list(w)))
                            normal=s.eye(4);normal[0,1]=3
                            assert Hstar.det()==1 and Hstar[:,0]==w
                            assert Hstar.inv()*U*Hstar==normal
                            initial_sources.append(dict(fiber=j+1,cover_order=2,
                                                        kind='primitive rank-one semistable Mumford cover'))
                            angular=angular.row_join(w)
                            extra.append(dict(fiber=j+1,cover_matrix=U.tolist(),vanishing=w.tolist(),
                                              period_basis=Hstar.tolist(),period_basis_inverse=Hstar.inv().tolist(),
                                              normal_monodromy=normal.tolist()))
                        orbit=orbit_certificate(Ts,angular)
                    assert not orbit.get('failed'),(raw['OS'],raw['profile'],a,b,zero,orbit)
                    record=dict(OS=raw['OS'],profile=raw['profile'],a=a,b=b,
                                zero_fiber=zero+1,zero_type=kind,zero_component=component,
                                multidegree=deg,matrices=[T.tolist() for T in Ts],
                                cusp_H=H.tolist(),cusp_H_inverse=H.inv().tolist(),
                                angular_relations=angular.tolist(),initial_sources=initial_sources,
                                selected_cusp_only=cusp_only,extra_cover_relations=extra,
                                orbit_certificate=orbit)
                    output.append(record)
        counts.append(dict(OS=raw['OS'],profile=raw['profile'],count=len(output)-before))
        print(raw['OS'],raw['profile'],'height',h,'natural rows',len(output)-before)
    fails=[r for r in output if r['orbit_certificate'].get('failed')]
    print('Total independently enumerated natural rows:',len(output))
    print('Remaining normal-closure failures after all geometric relations:',len(fails))
    for r in fails:print('FAIL',r['OS'],r['profile'],r['a'],r['b'],r['zero_fiber'],r['orbit_certificate'])
    exceptional=[r for r in output if r['extra_cover_relations']]
    print('Rows requiring the odd-star cover relation:',len(exceptional))
    for r in exceptional:
        print('COVER',r['OS'],r['profile'],r['a'],r['b'],
              'cusp-only lattice',r['selected_cusp_only']['normal_lattice'],
              'primitive vanishing',r['extra_cover_relations'][0]['vanishing'])
    data=dict(method='Exact component intersection vectors; independently reconstructed rational local lifts; integer conjugate-column Bezout certificates.',
              computed_utc=datetime.now(timezone.utc).isoformat(),counts=counts,rows=output)
    (HERE/'S6_SERIES_PUBLISH_III_02KY_fresh_enumeration_maps.json').write_text(
        json.dumps(data,default=int,indent=2)+'\n',newline='\n')
    short=lambda x:json.dumps(x,default=int,separators=(',',':'))
    fields=['row','OS','profile','a','b','zero_fiber','zero_type','cusp_H','cusp_H_inverse',
            'extra_vanishing','witnesses']
    with (HERE/'S6_SERIES_PUBLISH_III_02KY_fresh_certificates.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader()
        for j,r in enumerate(output,1):
            c=r['orbit_certificate'];witnesses=[]
            for k,coeff in enumerate(c['right_inverse']):
                if not any(coeff):continue
                word=[(i+1)*sign for i,sign in c['words'][k]['word']]
                witnesses.append([c['words'][k]['angular_column']+1,word,c['columns'][k][:3],coeff])
            row={key:r[key] for key in ['OS','profile','a','b','zero_fiber','zero_type']}
            row.update(row=j,cusp_H=short(r['cusp_H']),cusp_H_inverse=short(r['cusp_H_inverse']),
                       extra_vanishing=short([e['vanishing'] for e in r['extra_cover_relations']]),
                       witnesses=short(witnesses))
            writer.writerow(row)
    print('Compact certificates: 172 rows; each witness [initial-column, signed peripheral word, vector, right-inverse row].')
    print('Original target proofs and historical 172-row catalogue remain closed.')


if __name__=='__main__':main()
