"""Exact marked LS historical/fresh presentation maps, after exposure.

This is a new bounded validator, not execution of the historical programs.
It reconstructs their used all-Mumford branches from the retained matrices,
then proves both relation-lattice inclusions through the actual Nielsen map.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import ast
import json
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

W=Path(__file__).resolve().parents[1]
LANE=W/'agents/continuation7_iii_vertical_correction_receiving'
fresh=json.loads((W/'agents/continuation7_iii_vertical_correction/S6_SERIES_PUBLISH_III_02LS_fresh_os45_data_v001.json').read_text())
old=json.loads((LANE/'S6_SERIES_PUBLISH_fourfolds_corrected_Mumford_examples.json').read_text())
source=W/'code/S6_SERIES_PUBLISH_c7_ls_os45_bar_v001.py'
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
I4,I6=S.eye(4),S.eye(6)
selected={'ints','sparse','bezout','smith','solve_from_factor','factor_record','wedge','exterior','p','multiply','inverse','power','f_word','f_poly'}
exec(compile(ast.Module(body=[n for n in ast.parse(source.read_text()).body if isinstance(n,ast.FunctionDef) and n.name in selected],type_ignores=[]),str(source),'exec'))

def mat(obj):
    A=S.zeros(*obj['shape'])
    for i,j,x in obj['entries']:A[i,j]=x
    return A

def old_smith(A):
    D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(S.ZZ))
    D,U,V=[x.to_Matrix() for x in (D,U,V)]
    assert U*A*V==D and abs(U.det())==abs(V.det())==1
    rank=sum(bool(D[i,i]) for i in range(min(D.shape)))
    return D,U,V,rank

def group(A):
    ds=smith(A)[-1]
    return dict(free=A.rows-len(ds),torsion=[d for d in ds if d>1])

def emit(label,obj):
    print(label+'='+json.dumps(obj,separators=(',',':')),flush=True)

print('START',datetime.now(timezone.utc).isoformat(),flush=True)
print('HISTORICAL_SHA256',sha256((LANE/'S6_SERIES_PUBLISH_fourfolds_corrected_Mumford_examples.json').read_bytes()).hexdigest(),flush=True)
results=[]
for history,new in zip(old,fresh):
    a,b,zero,e=new['a'],new['b'],new['zero'],new['e']
    assert (history['P'],history['Q'],history['weights'].index(1),history['e'])==(a,b,zero,e)
    Ts=[mat(x['T']) for x in new['local_maps']];As=[I4]+Ts;count=6
    R=mat(new['exterior']['R']);K=mat(new['exterior']['K']);Ki=mat(new['exterior']['K_inverse'])
    Bnew=mat(new['full']['B']);Jlast=mat(new['exterior']['J_last'])
    Dold=S.Matrix.hstack(*[T-I4 for T in As[:-1]])
    oldD,oldU,oldV,rank=old_smith(Dold);Ko=oldV[:,rank:];Koi=ints(oldV.inv())[rank:,:]
    assert Ko.cols==17 and Koi*Ko==S.eye(17)
    oldraw=[];suffix=[]
    for i in range(5):
        inj=S.zeros(20,4);inj[4*i:4*i+4,:]=I4;oldraw.append(inj)
        suf=I4.copy()
        for T in As[i+1:-1]:suf=suf*T
        suffix.append(suf)
    oldraw.append(-S.Matrix.vstack(*suffix))
    def old_c(i,u):
        if i<5:return f_poly(As[i],u)
        return -sum((f_poly(As[j],suffix[j]*As[i]*u) for j in range(5)),S.zeros(6,1))
    def old_graph(i,u):
        x=oldraw[i]*u;assert Dold*x==S.zeros(4,1)
        z=Koi*x;assert Ko*z==x
        return z
    suffix_new=[]
    for i in range(5):
        suf=I4.copy()
        for T in Ts[i+1:]:suf=suf*T
        suffix_new.append(suf)
    def last_c(u):
        return -sum((f_poly(Ts[i],suffix_new[i]*u) for i in range(5)),S.zeros(6,1))
    graph_change=Jlast.row_join(S.Matrix.vstack(I4.row_join(S.zeros(4,12)),S.zeros(16,16))) if False else S.zeros(20,20)
    graph_change[:,:4]=Jlast
    for i in range(4):graph_change[4*i:4*i+4,4*(i+1):4*(i+2)]=I4
    assert mat(new['exterior']['graph_D'])*graph_change==Dold
    Q=ints(Ki*graph_change*Ko);Qi=ints(Q.inv());assert abs(Q.det())==1
    linear_c=S.Matrix.hstack(*[last_c(I4[:,i]) for i in range(4)])
    shift=linear_c*Ko[:4,:]
    M=I6.row_join(shift).col_join(S.zeros(17,6).row_join(Q))
    Mi=I6.row_join(-shift*Qi).col_join(S.zeros(17,6).row_join(Qi))
    assert M*Mi==Mi*M==S.eye(23)
    # Reconstruct every old column, retaining its original ordering.
    fibre=S.Matrix.hstack(*[exterior(T)-I6 for T in As])
    columns=[fibre[:,j].col_join(S.zeros(17,1)) for j in range(fibre.cols)]
    labels=[['fibre',i,j] for i in range(6) for j in range(6)]
    v=-e*I4[:,3]
    for i in range(4):
        u=I4[:,i];columns.append((-wedge(u,v)).col_join(old_graph(0,u)));labels.append(['ordinary',i])
    columns.append(S.zeros(6,1).col_join(old_graph(0,v)));labels.append(['ordinary_root'])
    local_maps=[];vertical=[]
    h1=[(T-I4)[:,j].col_join(S.zeros(5,1)) for T in As for j in range(4)]
    def base(i):return S.eye(5)[:,i] if i<5 else -S.ones(5,1)
    h1.append((-v).col_join(base(0)))
    finite_h1=S.Matrix.hstack(*h1)
    assert group(finite_h1)==history['exterior_H1']==dict(free=5,torsion=[])
    for i,(lc,nc) in enumerate(zip(history['local'],new['local_maps'])):
        F2=S.Matrix(lc['fibre_kernel']);fixed=S.Matrix(lc['normal_vectors']);F1=S.Matrix(lc['pi1_kernel'])
        Nk=mat(nc['fibre_kernel']);Nf=mat(nc['fixed_basis']);nf=smith(Nk);of=smith(F2)
        into_new=solve_from_factor(Nk,F2,nf);into_old=solve_from_factor(F2,Nk,of)
        assert mat(nc['f2'])*F2==S.zeros(4,F2.cols)
        fixed_change=solve_from_factor(Nf,fixed,smith(Nf));assert abs(fixed_change.det())==1
        assert (Ts[i]-I4)*fixed==S.zeros(4,fixed.cols)
        assert mat(nc['f1'])*F1==S.zeros(mat(nc['f1']).rows,F1.cols)
        assert lc['site']==i and lc['type']==('I8' if i==0 else 'I1') and lc['components']==1
        assert (lc['P_component'],lc['Q_component'])==((3*a%8,3*b%8) if i==0 else (0,0))
        assert lc['kind']==('rank_two_mumford' if i==zero else 'rank_one_mumford')
        for j in range(fixed.cols):
            u=fixed[:,j];columns.append(old_c(i+1,u).col_join(old_graph(i+1,u)));labels.append(['normal',i,j])
        start=len(columns)
        for j in range(F2.cols):columns.append(F2[:,j].col_join(S.zeros(17,1)));labels.append(['cap_fibre',i,j])
        for j in range(F1.cols):h1.append(F1[:,j].col_join(S.zeros(5,1)))
        h1.append(S.zeros(4,1).col_join(base(i+1)))
        vertical.extend([F1[:,j] for j in range(F1.cols)])
        local_maps.append(dict(site=i,old_fibre_kernel=sparse(F2),new_from_old=sparse(into_new),old_from_new=sparse(into_old),fixed_basis_change=sparse(fixed_change),fixed_basis_change_inverse=sparse(ints(fixed_change.inv())),column_start=start,old_columns=F2.cols,new_columns=Nk.cols))
    Bold=S.Matrix.hstack(*columns)
    assert Bold==S.Matrix(history['H2_matrix']) and Bold.shape==(23,70)
    assert S.Matrix.hstack(*h1)==S.Matrix(history['H1_matrix'])
    assert group(S.Matrix.hstack(*h1))==dict(free=0,torsion=[])
    assert group(fibre)==history['regular_coinvariant_H2']==dict(free=1,torsion=[2])
    ff=smith(Bnew);hf=smith(Bold)
    new_from_old=solve_from_factor(Bnew,M*Bold,ff)
    old_from_new=solve_from_factor(Bold,Mi*Bnew,hf)
    assert Bnew*new_from_old==M*Bold and Bold*old_from_new==Mi*Bnew
    assert hf[-1]==ff[-1]==[1]*22+[b]
    assert history['entry']==45 and history['profile']=='default' and history['original_sites']==[]
    assert history['euler']==2 and history['relative_free_rank']==0
    expected=[dict(free=1,torsion=[]),dict(free=0,torsion=[]),dict(free=0,torsion=[b]),dict(free=0,torsion=[b]),dict(free=0,torsion=[]),dict(free=0,torsion=[]),dict(free=1,torsion=[])]
    assert history['homology']==expected
    fp=history['fundamental_group']
    assert fp['fibre_generators']==['e1','e2','delta','gamma'] and fp['fibre_abelian'] is True
    assert fp['base_generators']==['t'+str(i) for i in range(6)] and fp['conjugation_matrices']==[x.tolist() for x in As]
    assert fp['base_product']=='1' and fp['finite_power_relations']==[dict(site=0,m=1,v=list(map(int,v)))]
    assert fp['unchanged_caps']==[dict(site=i+1,killed_vectors=lc['pi1_kernel'],base_loop_killed=True) for i,lc in enumerate(history['local'])]
    assert fp['vertical_normal_closure']==S.eye(4)[:,:3].tolist() and fp['vertical_quotient']==dict(free=0,torsion=[])
    vf=smith(S.Matrix.hstack(*vertical)[:3,:]);assert vf[-1]==[1,1,1]
    assert history['boundary_marking']=='D.GI2 actual punctured marking; no extra affine boundary translations; ordinary gamma clutch e.'
    d0=history['chosen_I8_vertical_correction'];C8=S.zeros(8)
    for i in range(8):C8[i,i]-=2;C8[i,(i-1)%8]+=1;C8[i,(i+1)%8]+=1
    raw_d=S.Matrix(d0['vertical_coefficients']);physical_old=S.Matrix([raw_d[-i%8] for i in range(8)])
    physical_new=S.Matrix(new['vertical']['d']);difference=physical_old-physical_new
    sigma=mat(new['vertical']['S']);assert sigma*difference==difference
    assert d0['kind']=='I8' and (d0['p'],d0['q'])==(3*a%8,3*b%8) and d0['exists']
    mp=S.eye(8)[:,3*a%8]-S.eye(8)[:,0]
    assert d0['initial_multidegree']==list(map(int,mp)) and d0['corrected_multidegree']==list(map(int,mp+C8*raw_d))
    KK=S.Matrix.hstack(*map(S.Matrix,d0['all_correction_kernel_columns']));assert all(d==1 for d in smith(KK)[-1]) and KK.cols==(8 if b%8==0 else __import__('math').gcd(8,3*b))
    assert all(difference[i]==difference[(i-3*b)%8] for i in range(8)) and difference[0]==-1
    result=dict(a=a,b=b,zero=zero,e=e,old_shape=list(Bold.shape),new_shape=list(Bnew.shape),old_column_labels=labels,old_K=sparse(Ko),old_K_inverse=sparse(Koi),graph_change=sparse(graph_change),graph_basis_change=sparse(Q),graph_basis_inverse=sparse(Qi),central_shift=sparse(shift),marked_generator_map=sparse(M),marked_generator_inverse=sparse(Mi),new_relation_preimages=sparse(new_from_old),old_relation_preimages=sparse(old_from_new),local_maps=local_maps,old_smith=factor_record(hf),smith_diagonal=hf[-1],old_physical_D=list(map(int,physical_old)),fresh_physical_D=list(map(int,physical_new)),invariant_difference=list(map(int,difference)),meridian_shear=int(difference[0]),checked_historical_row=history)
    results.append(result)
    emit('EXACT_PRESENTATION_COMPARISON',result)
    print('PASS_ROW',a,b,zero,e,'70=59+6_zero+5_cusp_redundancies','M_and_inverse_integral','both_relation_preimages_verified',flush=True)
out=LANE/'S6_SERIES_PUBLISH_III_02LS_post_relation_data_v001.json'
out.write_text(json.dumps(results,indent=2)+'\n')
print('DATA',out.relative_to(W),'SHA256',sha256(out.read_bytes()).hexdigest(),flush=True)
print('PASS all16 historical matrices, all fields, exact marked generator maps and both integral relation-lattice inclusions.',flush=True)
print('COMPLETE',datetime.now(timezone.utc).isoformat(),flush=True)
