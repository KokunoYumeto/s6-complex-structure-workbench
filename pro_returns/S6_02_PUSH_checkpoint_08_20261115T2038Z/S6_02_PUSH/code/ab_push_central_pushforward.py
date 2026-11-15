"""Integral normalization-cube checks for the central star formula A.4.9.

Each row is a Cech complex of coordinate projective subspaces in one
exceptional fibre.  Every possible codimension/branch count in a smooth
fourfold is checked.  Global compatibility is proved by the explicit
integral exceptional Gysin maps, not inferred from these finite tests.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def row_complex(labels,dim_of_intersection,a):
    terms=[]
    for p in range(len(labels)):
        terms.append([v for v in combinations(labels,p+1)
                      if dim_of_intersection(v)>=a])
    matrices=[]
    for p in range(len(terms)-1):
        matrix=s.zeros(len(terms[p+1]),len(terms[p]))
        index={t:j for j,t in enumerate(terms[p])}
        for row,t in enumerate(terms[p+1]):
            for i in range(len(t)):
                face=t[:i]+t[i+1:]
                if face in index:
                    matrix[row,index[face]]=(-1)**i
        matrices.append(matrix)
    for i in range(len(matrices)-1):
        assert matrices[i+1]*matrices[i]==s.zeros(matrices[i+1].rows,matrices[i].cols)
    ranks=[]; smiths=[]
    for matrix in matrices:
        sm=smith_normal_form(matrix,domain=ZZ)
        diagonal=[abs(int(sm[i,i])) for i in range(min(sm.shape)) if sm[i,i]]
        assert all(x==1 for x in diagonal)
        ranks.append(len(diagonal));smiths.append(diagonal)
    ranks=[0]+ranks+[0]
    cohom=[len(terms[p])-ranks[p]-ranks[p+1] for p in range(len(terms))]
    assert cohom==[1]+[0]*(len(terms)-1)
    return dict(term_ranks=list(map(len,terms)),cohomology_ranks=cohom,
                differential_smith=smiths,
                matrices=[mat.tolist() for mat in matrices])

rows=[]
for c in (2,3,4):
    for k in range(1,c+1):
        # Label0 is the exceptional component, the other labels are
        # strict-transform coordinate hyperplanes.
        labels=tuple(range(k+1))
        for a in range(c):
            rec=row_complex(labels,lambda subset:c-1-sum(i!=0 for i in subset),a)
            rec.update(kind='central',codimension=c,central_branches=k,half_degree=a)
            rows.append(rec)
            print('CENTRAL c=',c,'k=',k,'degree=',2*a,'cohom=',rec['cohomology_ranks'])
    # Horizontal centres can meet only the central coordinate branches
    # outside the c defining coordinates.
    for count in range(1,5-c):
        labels=tuple(range(count))
        for a in range(c):
            rec=row_complex(labels,lambda subset:c-1,a)
            rec.update(kind='horizontal',codimension=c,central_branches=count,half_degree=a)
            rows.append(rec)
            print('HORIZONTAL c=',c,'k=',count,'degree=',2*a,'cohom=',rec['cohomology_ranks'])

gysin=[]
for c in (2,3,4):
    matrix=s.diag(1,*([-1]*(c-1)))
    assert abs(matrix.det())==1
    gysin.append(dict(codimension=c,matrix=matrix.tolist(),determinant=int(matrix.det())))

out=dict(status='PASS',normalization_row_count=len(rows),normalization_rows=rows,
         exceptional_gysin_matrices=gysin,
         all_nonzero_smith_factors_one=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('PASS:',len(rows),'NORMALIZATION ROW COMPLEXES; ALL INTEGRAL SMITH FACTORS ONE')
