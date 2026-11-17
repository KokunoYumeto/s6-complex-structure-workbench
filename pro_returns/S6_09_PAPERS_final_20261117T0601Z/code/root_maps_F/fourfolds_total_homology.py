"""Complete integer Mayer--Vietoris algorithm for every marked F.2 gluing.

Input: finite homology matrices, integer affine numerators, actual cyclic
orders, primitive maximal cusp, and integral clutch vector.  Optional
unimodular local bases only improve runtime.  All maps are chain maps
from the explicit bar/groupoid models, not maps on homology alone.
The default executed example is the original (5,4) compact fourfold;
argument m adds its F2.32 identity-linear translation cap of order m.
"""
import sys,json,hashlib
from pathlib import Path
import sympy as S
from fourfolds_affine_cap_chains import AffineCap
from fourfolds_global_chains import (Complement,AffineGraphBoundary,CuspBoundaryToComplement,
                                    SuspensionBoundaryToCap)
from fourfolds_kuhn_cap_chains import KuhnCategory,TorusDiagram,Collapse,unit_reduce,homology_all
from fourfolds_survivor_test import snf,factors

CHAIN_CACHE_READ=True

def sparse(M):
    return {j:{i:int(M[i,j]) for i in range(M.rows) if M[i,j]} for j in range(M.cols)}

def sparse_apply(D,vector):
    out={}
    for c,a in vector.items():
        for r,b in D.get(c,{}).items():
            out[r]=out.get(r,0)+a*b
            if not out[r]:out.pop(r)
    return out

def check_chain_map(Dtarget,F,Fprevious,Dsource,source_rank):
    for c in range(source_rank):
        assert sparse_apply(Dtarget,F.get(c,{}))==sparse_apply(Fprevious,Dsource.get(c,{}))

def cached_maps(key,compute):
    folder=Path(__file__).with_name('fourfolds_chain_cache');folder.mkdir(exist_ok=True)
    names=['fourfolds_bar_koszul.py','fourfolds_affine_cap_chains.py',
           'fourfolds_global_chains.py','fourfolds_kuhn_cap_chains.py']
    source=b''.join(Path(__file__).with_name(n).read_bytes() for n in names)
    digest=hashlib.sha256(source+json.dumps(key,sort_keys=True,default=int).encode()).hexdigest()
    filename=folder/(digest+'.json')
    if CHAIN_CACHE_READ and filename.exists():
        raw=json.loads(filename.read_text())
        print('  restoring checked chain-map checkpoint',digest[:12],flush=True)
        return [{int(c):{int(r):int(v) for r,v in col.items()} for c,col in D.items()} for D in raw]
    answer=compute()
    filename.write_text(json.dumps(answer,separators=(',',':'),default=int)+'\n')
    return answer

def basis_map(key,source_basis,target_basis,method,clear=None,column_cache=False):
    if not target_basis:return {j:{} for j in range(len(source_basis))}
    target_index={b:i for i,b in enumerate(target_basis)};out={}
    for j,b in enumerate(source_basis):
        if key['degree']>=5 and (column_cache or j%128==0):
            print('   ',key['map'],'degree',key['degree'],'column',j+1,'of',len(source_basis),flush=True)
        def compute_column():
            return [{0:{target_index[t]:int(c) for t,c in method(*b).items()}}]
        if column_cache:
            out[j]=cached_maps(dict(key,column=j),compute_column)[0][0]
        else:out[j]=compute_column()[0][0]
        if clear is not None and (column_cache or j%64==63):clear()
    return out

def finite_cache_key(matrices,index,Q,v,m,n):
    # This boundary map uses only fibre translations and s_index.  All
    # bar, Alexander--Whitney and Fox terms stay in that subgroup.  Its
    # fibre rows and edge-index rows have the same indices for every k.
    # Consequently additional peripheral matrices do not change either
    # complete map; each cache load is still checked against both full
    # target differentials by check_chain_map below.
    return {'kind':'finite','matrix':matrices[index].tolist(),'index':index,
            'local_basis':Q.tolist(),'numerator':list(v),'order':m,'degree':n}

def adapted_cusp(matrices):
    P=S.eye(6)
    for M in matrices:P=P*M
    N=P.inv()-S.eye(6)
    assert N*N==S.zeros(6) and factors(N)==[1,1,1]
    D,U,V=snf(N);B=V[:,:3];A=N*B;Q=S.Matrix.hstack(A,B)
    assert abs(Q.det())==1 and N*Q==Q*S.Matrix.vstack(
        S.Matrix.hstack(S.zeros(3),S.eye(3)),S.zeros(3,6))
    return Q

def total_homology(matrices,numerators,orders,clutch=None,local_bases=None,
                   cusp_marking=None,output=None):
    assert len(matrices)==len(numerators)==len(orders) in (2,3)
    matrices=[S.Matrix(M) for M in matrices];k=len(matrices)
    assert all(M.shape==(6,6) for M in matrices)
    E=Complement(matrices)
    P=adapted_cusp(matrices) if cusp_marking is None else S.Matrix(cusp_marking)
    assert abs(P.det())==1
    clutch=S.zeros(6,1) if clutch is None else S.Matrix(clutch)
    local_bases=[S.eye(6) for _ in range(k)] if local_bases is None else [S.Matrix(Q) for Q in local_bases]
    main_sizes=[{n:len(E.bases(n)) for n in range(10)}]
    main_d=[{n:sparse(E.matrix_degree(n)) for n in range(10)}]
    boundary_sizes=[];boundary_d=[];mapE=[];mapCap=[]
    for i,(M,v,m,Q) in enumerate(zip(matrices,numerators,orders,local_bases)):
        print('FINITE CAP',i+1,'order',m,flush=True)
        assert abs(Q.det())==1
        localM=Q.inv()*M*Q;localv=Q.inv()*S.Matrix(v)
        assert all(S.denom(x)==1 for x in localv)
        cap=AffineCap(localM,list(localv),m)
        boundary=AffineGraphBoundary(cap,E,i,Q)
        suspension=(localM==S.diag(1,localM[1:,1:]) and
                    localv[1:,:]==S.zeros(5,1) and abs(localv[0])==1)
        if suspension:
            print('using exact geometric mapping-torus cap',flush=True)
            cap_target=Complement([localM[1:,1:]])
            cap_map=SuspensionBoundaryToCap(boundary,cap_target,int(localv[0]))
            cap_d={n:cap_target.matrix_degree(n) for n in range(10)}
        else:
            cap_target=cap;cap_map=None
            cap_d=cap.matrices(8,progress=True)
        main_sizes.append({n:len(cap_target.bases(n)) for n in range(10)})
        main_d.append({n:sparse(D) for n,D in cap_d.items()})
        boundary_sizes.append({n:len(boundary.bases(n)) for n in range(9)})
        boundary_d.append({n:sparse(boundary.matrix_degree(n)) for n in range(9)})
        FC={};FE={}
        for n in range(9):
            print('FINITE BOUNDARY MAPS',i+1,'degree',n,flush=True)
            key=finite_cache_key(matrices,i,Q,v,m,n)
            def clear_maps():
                cap.clear_intermediates();E.clear_intermediates()
                if suspension:cap_target.clear_intermediates()
            def compute_pair():
                print('  computing boundary-to-cap map',flush=True)
                C=basis_map(dict(key,map='cap'),boundary.bases(n),cap_target.bases(n),
                            cap_map.basis if suspension else boundary.cap_basis,clear_maps,True)
                print('  computing boundary-to-complement map',flush=True)
                F=basis_map(dict(key,map='complement'),boundary.bases(n),E.bases(n),
                            boundary.complement_basis,clear_maps,True)
                return [C,F]
            FC[n],FE[n]=cached_maps(key,compute_pair)
            DY=sparse(boundary.matrix_degree(n))
            check_chain_map(sparse(cap_d[n]),FC[n],FC.get(n-1,{}),DY,len(boundary.bases(n)))
            check_chain_map(sparse(E.matrix_degree(n)),FE[n],FE.get(n-1,{}),DY,len(boundary.bases(n)))
            cap.clear_intermediates();E.clear_intermediates()
            if suspension:cap_target.clear_intermediates()
        mapCap.append(FC);mapE.append(FE)
    print('KUHN CUSP PAIR',flush=True)
    C=KuhnCategory();W=TorusDiagram(C);Y=TorusDiagram(C,True)
    BW,DW=W.complex();BY,DY=Y.complex()
    main_sizes.append({n:len(BW.get(n,[])) for n in range(10)});main_d.append(DW)
    boundary_sizes.append({n:len(BY.get(n,[])) for n in range(9)});boundary_d.append(DY)
    collapse=Collapse(Y,W);FC=collapse.matrices(BY,BW);FE={}
    F=CuspBoundaryToComplement(Y,E,P,tuple(clutch))
    for n in range(8):
        print('CUSP BOUNDARY MAP degree',n,'generators',len(BY[n]),flush=True)
        key={'kind':'cusp','matrices':[T.tolist() for T in matrices],
             'marking':P.tolist(),'clutch':list(clutch),'degree':n}
        FE[n]=cached_maps(key,lambda:[basis_map(dict(key,map='cusp'),BY[n],E.bases(n),
                                              F.basis,E.clear_intermediates)])[0]
        check_chain_map(sparse(E.matrix_degree(n)),FE[n],FE.get(n-1,{}),DY[n],len(BY[n]))
        print('CUSP BOUNDARY MAP degree',n,'PASSED',flush=True)
        E.clear_intermediates()
    mapCap.append(FC);mapE.append(FE)
    main_offset={};boundary_offset={};dimensions={}
    for n in range(10):
        offset=0;main_offset[n]=[]
        for sizes in main_sizes:main_offset[n].append(offset);offset+=sizes.get(n,0)
        boundary_offset[n]=[]
        for sizes in boundary_sizes:boundary_offset[n].append(offset);offset+=sizes.get(n-1,0)
        dimensions[n]=offset
    assert max(dimensions.values())<=4003
    differential={}
    def put(n,column,row,value):
        if not value:return
        d=differential[n].setdefault(column,{})
        d[row]=d.get(row,0)+int(value)
        if not d[row]:d.pop(row)
    for n in range(10):
        differential[n]={}
        for j,D in enumerate(main_d):
            for c,col in D.get(n,{}).items():
                for r,v in col.items():put(n,main_offset[n][j]+c,main_offset[n-1][j]+r,v)
        if not n:continue
        for j,D in enumerate(boundary_d):
            shift=boundary_offset[n][j]
            for c,col in mapE[j].get(n-1,{}).items():
                for r,v in col.items():put(n,shift+c,r,v)
            for c,col in mapCap[j].get(n-1,{}).items():
                for r,v in col.items():put(n,shift+c,main_offset[n-1][j+1]+r,-v)
            if n>=2:
                for c,col in D.get(n-1,{}).items():
                    for r,v in col.items():put(n,shift+c,boundary_offset[n-1][j]+r,-v)
    print('MAYER--VIETORIS RAW RANKS',dimensions,flush=True)
    reduced,cancellations=unit_reduce(dimensions,differential)
    H=homology_all(reduced)
    H={n:h for n,h in H.items() if n<=8}
    print('FULL INTEGRAL HOMOLOGY',H,flush=True)
    print('UNIT CHAIN CANCELLATIONS',cancellations,flush=True)
    result={'matrices':[M.tolist() for M in matrices],'numerators':[list(v) for v in numerators],
            'orders':orders,'clutch':list(clutch),'local_bases':[Q.tolist() for Q in local_bases],
            'adapted_cusp':P.tolist(),'raw_chain_ranks':dimensions,'homology':H,
            'unit_cancellations':cancellations,
            'reduced_differentials':{n:D.tolist() for n,D in reduced.items()}}
    if output:Path(output).write_text(json.dumps(result,indent=2,default=int)+'\n')
    return H

def example(m=None):
    A=S.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],
                [0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
    B=S.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],
                [0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
    v1=S.Matrix([1,3,-2,-1,2,0]);v2=S.Matrix([-1,0,0,0,0,0])
    H5=S.Matrix([[-1,-1,0,-1,0],[0,1,0,1,1],[0,1,0,0,0],
                 [0,-1,-1,0,-1],[0,0,1,0,0]])
    H4=S.Matrix([[-1,0,-1,0,1],[-1,2,-1,1,3],[-1,1,-1,2,3],
                 [0,-1,0,-1,-1],[1,-1,2,-1,-3]])
    P5=S.Matrix.hstack(v1,S.eye(6)[:,1:]*H5)
    P4=S.diag(1,H4)
    matrices=[A.T,B.T];nums=[v1,v2];orders=[5,4];bases=[P5,P4]
    if m is not None:
        assert m>=2
        matrices.append(S.eye(6));nums.append(S.eye(6)[:,0]);orders.append(m);bases.append(S.eye(6))
    return matrices,nums,orders,bases

if __name__=='__main__':
    CHAIN_CACHE_READ='--fresh' not in sys.argv[1:]
    arguments=[a for a in sys.argv[1:] if a!='--fresh']
    m=int(arguments[0]) if arguments else None
    matrices,nums,orders,bases=example(m)
    tag='survivor' if m is None else 'k3_'+str(m)
    out=Path(__file__).with_name('fourfolds_total_homology_'+tag+'.json')
    H=total_homology(matrices,nums,orders,local_bases=bases,output=out)
    if m is None:
        assert H=={n:{'rank':1 if n in (0,8) else 4 if n==4 else 0,'torsion':[]} for n in range(9)}
    else:
        a=abs(20-m);eps=int(m==20)
        expected={0:{'rank':1,'torsion':[]},1:{'rank':eps,'torsion':([a] if a>1 else [])},
                  2:{'rank':eps,'torsion':[m]*5},3:{'rank':0,'torsion':[m]*10},
                  4:{'rank':4,'torsion':[m]*10},5:{'rank':0,'torsion':[m]*5},
                  6:{'rank':eps,'torsion':([a] if a>1 else [])},7:{'rank':eps,'torsion':[]},
                  8:{'rank':1,'torsion':[]}}
        assert H==expected,(H,expected)
    print('FULL MARKED GLUING MATCHES THE INDEPENDENT INTEGRAL HOMOLOGY THEOREM',flush=True)
