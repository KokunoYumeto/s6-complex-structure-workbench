"""Fresh integral sheaf and finite-norm certificates; staged during checkpoint freeze."""
from itertools import combinations
from pathlib import Path
import json
from flint import fmpz_mat

ROOT=Path(__file__).resolve().parents[2]
DATA=json.loads((ROOT/'code/continuation_V/F2_13_companion_explore_fresh.output.json').read_text())

def eye(n):
    return fmpz_mat([[int(i==j) for j in range(n)] for i in range(n)])

def zeros(m,n):return fmpz_mat(m,n)

def columns(*ms):
    n=ms[0].nrows()
    return fmpz_mat([[m[i,j] for m in ms for j in range(m.ncols())] for i in range(n)])

def rows(*ms):
    return fmpz_mat([[m[i,j] for j in range(m.ncols())] for m in ms for i in range(m.nrows())])

def sub(m,ri,cj):
    ri=list(ri);cj=list(cj)
    if not ri or not cj:return zeros(len(ri),len(cj))
    return fmpz_mat([[m[i,j] for j in cj] for i in ri])

def wedge(m,k):
    ix=list(combinations(range(m.nrows()),k))
    return fmpz_mat([[sub(m,i,j).det() for j in ix] for i in ix])

def integer_inverse(m):
    q=m.inv()
    out=fmpz_mat([[int(q[i,j]) for j in range(q.ncols())] for i in range(q.nrows())])
    assert out*m==eye(m.nrows())
    return out

def kernel(m):
    h,t=m.transpose().hnf(transform=True)
    assert t*m.transpose()==h and abs(t.det())==1
    rank=m.rank()
    assert all(h[i,j]==0 for i in range(rank,h.nrows()) for j in range(h.ncols()))
    u=t.transpose();ui=integer_inverse(u)
    k=sub(u,range(u.nrows()),range(rank,u.ncols()))
    assert m*k==zeros(m.nrows(),k.ncols())
    return k,ui,rank

def smith(m):
    d=m.snf()
    return [abs(int(d[i,i])) for i in range(min(d.nrows(),d.ncols())) if d[i,i]]

def serial(m):return [[int(m[i,j]) for j in range(m.ncols())] for i in range(m.nrows())]

def power(m,n):
    z=eye(m.nrows())
    for _ in range(n):z=z*m
    return z

def unit_minor(m):
    arr=serial(m);a=[[x%3 for x in row] for row in arr]
    order=list(range(m.nrows()));piv=[];r=0
    for j in range(m.ncols()):
        hit=next((i for i in range(r,m.nrows()) if a[i][j]),None)
        if hit is None:continue
        a[r],a[hit]=a[hit],a[r];order[r],order[hit]=order[hit],order[r]
        u=pow(a[r][j],-1,3);a[r]=[(u*x)%3 for x in a[r]]
        for i in range(r+1,m.nrows()):
            z=a[i][j]
            a[i]=[(x-z*y)%3 for x,y in zip(a[i],a[r])]
        piv.append(j);r+=1
        if r==m.nrows():break
    assert r==m.rank()
    chosen=order[:r];det=int(sub(m,chosen,piv).det())
    assert det%3
    return {'rows':chosen,'columns':piv,'determinant':det,'rank':r}

out={};checks=[]
for case,dat in DATA.items():
    a=fmpz_mat(dat['a6']);b=fmpz_mat(dat['b6']);d=fmpz_mat(dat['b5'])
    cc={'cohomology':{},'finite':{}}
    haug=columns(a.transpose()-eye(6),b.transpose()-eye(6))
    assert all(haug[0,j]==0 for j in range(haug.ncols()))
    hminor=unit_minor(sub(haug,range(1,6),range(haug.ncols())))
    assert hminor['rank']==5
    cc['homology_augmentation']={'matrix':serial(haug),'bottom_five_unit_minor':hminor}
    checks.append(case+'_actual_homology_coinvariant_character')
    for q in [1,2,3,4]:
        aq=wedge(a,q);bq=wedge(b,q);n=aq.nrows();ident=eye(n)
        j1,_,_=kernel(aq-ident);j2,_,_=kernel(bq-ident);j0,_,_=kernel(bq*aq-ident)
        delta=columns(aq-ident,bq-ident)
        d0=rows(columns(j1,zeros(n,j2.ncols()),-j0),columns(zeros(n,j1.ncols()),j2,-aq*j0))
        assert delta*d0==zeros(n,d0.ncols());checks.append(case+f'_q{q}_complex')
        k,ui,rank=kernel(delta);coords=ui*d0
        assert sub(coords,range(rank),range(coords.ncols()))==zeros(rank,coords.ncols())
        e=sub(coords,range(rank,coords.nrows()),range(coords.ncols()))
        assert k*e==d0;checks.append(case+f'_q{q}_actual_kernel_coordinates')
        h0=j1.ncols()+j2.ncols()+j0.ncols()-d0.rank()
        h1=k.ncols()-e.rank();h2=n-delta.rank()
        ss1=smith(e);ss2=smith(delta)
        assert h0==(1 if q==1 else 0)
        assert h2==0
        assert all(x%3 for x in ss1+ss2);checks.append(case+f'_q{q}_no_three_primary_sheaf_torsion')
        em=unit_minor(e);dm=unit_minor(delta)
        ai=power(aq,4);bi=power(bq,5)
        delta_inv=columns(ai-ident,bi-ident)
        d0_inv=rows(columns(j1,zeros(n,j2.ncols()),-aq*j0),columns(zeros(n,j1.ncols()),j2,-j0))
        x=rows(columns(-aq,zeros(n,n)),columns(zeros(n,n),-bq))
        assert delta_inv*x==delta and x*d0==-d0_inv
        checks.append(case+f'_q{q}_exact_inverse_generator_complex_map')
        cc['cohomology'][q]={'free_ranks':[h0,h1,h2],'d0_smith_nonzero':ss1,'delta_smith_nonzero':ss2,'d0_unit_minor':em,'delta_unit_minor':dm,'J1':serial(j1),'J2':serial(j2),'J0':serial(j0),'delta':serial(delta),'d0':serial(d0),'kernel':serial(k),'kernel_coordinates':serial(e),'kernel_coordinate_change':serial(ui),'inverse_generator_degree_one_map':serial(x)}
    for k in range(5):
        dk=wedge(d,k);ni=dk.nrows();norm=zeros(ni,ni)
        for j in range(6):norm=norm+power(dk,j)
        inv,ui,rank=kernel(dk-eye(ni));co=ui*norm
        assert sub(co,range(rank),range(co.ncols()))==zeros(rank,co.ncols())
        co=sub(co,range(rank,co.nrows()),range(co.ncols()))
        assert inv*co==norm;checks.append(case+f'_wedge{k}_norm_in_actual_invariants')
        ns=smith(co)
        assert len(ns)==inv.ncols();checks.append(case+f'_wedge{k}_norm_full_rank')
        local_smith=smith(dk-eye(ni));assert all(x%3 for x in local_smith)
        ch,ct=co.transpose().hnf(transform=True)
        assert ct*co.transpose()==ch and abs(ct.det())==1
        hcols=sub(ch,range(co.nrows()),range(ch.ncols())).transpose()
        assert co*sub(ct.transpose(),range(ct.ncols()),range(co.nrows()))==hcols
        cc['finite'][k]={'D':serial(dk),'D_minus_I_smith':local_smith,'invariants':serial(inv),'norm6':serial(norm),'norm_in_invariants':serial(co),'norm_smith_in_invariants':ns,'norm_image_HNF_basis':serial(hcols),'norm_image_HNF_transform':serial(ct)}
    out[case]=cc

assert out['A']['finite'][2]['norm_smith_in_invariants']==[1,6]
assert out['B']['finite'][1]['norm_smith_in_invariants']==[3]
assert out['A']['finite'][2]['norm_image_HNF_basis']==[[1,0],[4,6]]
assert fmpz_mat([[1,0],[-4,1]])*fmpz_mat(out['A']['finite'][2]['norm_image_HNF_basis'])==fmpz_mat([[1,0],[0,6]])
assert out['B']['finite'][1]['norm_image_HNF_basis']==[[3]]
checks.extend(['case_A_actual_degree_three_quotient_order','case_B_actual_degree_two_quotient_order'])
result={'checks_passed':len(checks),'checks':checks,'cases':out,'scope':'Integral j-star exterior complexes with primitive HNF kernel coordinates; actual finite norm images inside primitive invariant lattices. Parameter multiplicities and arbitrary affine translations are treated in the accompanying proof.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks_passed':len(checks),'ranks':{c:{q:d['free_ranks'] for q,d in z['cohomology'].items()} for c,z in out.items()},'norms':{c:{k:d['norm_smith_in_invariants'] for k,d in z['finite'].items()} for c,z in out.items()}},indent=2))
