"""Migrate the completed survivor finite maps to their exact local keys.

The finite boundary subgroup contains only fibre translations and its
single marked peripheral generator.  The bar/AW/Fox projections therefore
use only that peripheral matrix.  Appending another peripheral generator
changes neither the columns nor their target row indices.  This reuses
identical already computed maps, not a homology-level substitute.  Every
subsequent assembly rechecks the full chain identities against its own
target differential.  --fresh always bypasses these checkpoints.
"""
import fourfolds_total_homology as C

if __name__=='__main__':
    matrices,numerators,orders,bases=C.example()
    count=0
    def missing():raise RuntimeError('The complete original finite-map checkpoint is absent')
    for i,(v,m,Q) in enumerate(zip(numerators,orders,bases)):
        for n in range(9):
            old={'kind':'finite','matrices':[T.tolist() for T in matrices],
                 'index':i,'local_basis':Q.tolist(),'numerator':list(v),'order':m,'degree':n}
            data=C.cached_maps(old,missing)
            new=C.finite_cache_key(matrices,i,Q,v,m,n)
            assert C.cached_maps(new,lambda:data)==data
            count+=1
    print('EXACT COMMON FINITE MAP PAIRS MIGRATED:',count)
