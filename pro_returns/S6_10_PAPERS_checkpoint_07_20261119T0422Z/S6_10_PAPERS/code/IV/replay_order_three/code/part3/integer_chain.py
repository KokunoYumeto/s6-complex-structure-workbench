"""Integral chain helpers with full Smith transformations retained."""
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ

def dec(M):
    D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
    D,U,V=[x.to_Matrix() for x in (D,U,V)]
    assert D==U*M*V
    return D,U,V

def ints(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def hom(d,up):
    assert d*up==S.zeros(d.rows,up.cols)
    D,U,V=dec(d);r=d.rank();K=V[:,r:]
    relation=(V.inv()*up)[r:,:]
    assert K*relation==up
    E,L,R=dec(relation);rr=relation.rank()
    inds=[i for i in range(K.cols) if i>=rr or abs(E[i,i])!=1]
    orders=[0 if i>=rr else abs(int(E[i,i])) for i in inds]
    reps=K*L.inv()[:,inds]
    project=(L*V.inv()[r:,:])[inds,:]
    assert project*reps==S.eye(len(inds))
    return orders,reps,project

def cone(ds,fs,dimensions):
    dims={j:dimensions.get(j,0)+dimensions.get(j-1,0) for j in range(7)}
    out={}
    for j in range(1,7):
        top=ds.get(j,S.zeros(dimensions.get(j-1,0),dimensions.get(j,0))).row_join(
            fs.get(j-1,S.zeros(0))-S.eye(dimensions.get(j-1,0)))
        bottom=S.zeros(dimensions.get(j-2,0),dimensions.get(j,0)).row_join(
            -ds.get(j-1,S.zeros(dimensions.get(j-2,0),dimensions.get(j-1,0))))
        out[j]=top.col_join(bottom)
        assert out[j].shape==(dims[j-1],dims[j])
    for j in range(2,7):
        assert out[j-1]*out[j]==S.zeros(dims[j-2],dims[j])
    return out,dims
