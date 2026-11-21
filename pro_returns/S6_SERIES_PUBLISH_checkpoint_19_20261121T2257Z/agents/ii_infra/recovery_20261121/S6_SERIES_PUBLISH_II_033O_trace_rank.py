"""Postrelease centralizer dimension by exact Gram traces and Newton identities.

No elimination, linear solver, nullspace, or numerical spectral routine is used.
"""
from pathlib import Path
import json,hashlib,datetime

D=Path(__file__).parent
source=D/'S6_SERIES_PUBLISH_II_033O_fresh_exact_output.json'
data=json.loads(source.read_text())

def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def certificate(matrices,off_diagonal):
    # Row (i,j) of XH-HX, with unknown entry X_(p,q).
    A=[[int(i==p)*H[q][j]-H[i][p]*int(q==j)
        for p in range(4) for q in range(4)]
       for H in matrices for i in range(4) for j in range(4)]
    G=[[sum(row[p]*row[q] for row in A) for q in range(16)] for p in range(16)]
    assert all(G[i][j]==G[j][i] for i in range(16) for j in range(16))
    power=[[int(i==j) for j in range(16)]for i in range(16)]
    traces=[];elementary=[1]
    for k in range(1,17):
        power=multiply(power,G)
        traces.append(sum(power[i][i]for i in range(16)))
        numerator=sum((-1)**(i-1)*elementary[k-i]*traces[i-1]for i in range(1,k+1))
        assert numerator%k==0
        elementary.append(numerator//k)
    coefficients=[(-1)**k*elementary[k]for k in range(17)]
    assert elementary[14]>0 and elementary[15]==elementary[16]==0
    vI=[int(i==j)for i in range(4)for j in range(4)]
    vE=[int((i,j)==off_diagonal)for i in range(4)for j in range(4)]
    assert all(sum(a*b for a,b in zip(row,vI))==0 for row in A)
    assert all(sum(a*b for a,b in zip(row,vE))==0 for row in A)
    assert vI[0]==1 and vE[0]==0 and vE[off_diagonal[0]*4+off_diagonal[1]]==1
    return {'commutator_matrix_shape':[64,16],'gram_matrix':G,'traces_G_to_powers_1_through_16':traces,
            'characteristic_coefficients_descending':coefficients,
            'nonzero_degree_two_coefficient':coefficients[14],
            'degree_one_and_constant_coefficients':coefficients[15:],
            'exact_zero_eigenvalue_multiplicity':2,
            'gram_rank':14,'commutator_rank':14,'centralizer_dimension':2,
            'generators_checked_directly':['I',f'E{off_diagonal[0]+1}{off_diagonal[1]+1}']}

result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'timing':'Postrelease additional different-method certificate; no extra independent proof or check event is claimed.',
        'input_path':source.name,'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'method':'Integer Gram matrix, exact power traces and Newton identities. No elimination or nullspace call.',
        'homology':certificate(data['H'],(3,0)),
        'cohomology':certificate(data['T'],(0,3)),
        'rank_justification':'A^t A is real symmetric positive semidefinite; its exact characteristic polynomial has precisely a double zero. Real symmetric diagonalization gives rank14. v^t A^t A v=sum_j(Av)_j^2 identifies ker(A^t A)=ker(A), so the rational commutator map also has rank14. The two directly verified independent generators therefore form its entire kernel.',
        'events_added':0,'all_assertions_passed':True}
out=D/'S6_SERIES_PUBLISH_II_033O_trace_rank_output.json'
assert not out.exists()
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'homology_characteristic_coefficients':result['homology']['characteristic_coefficients_descending'],
                  'cohomology_characteristic_coefficients':result['cohomology']['characteristic_coefficients_descending'],
                  'rank_justification':result['rank_justification'],'all_assertions_passed':True},indent=2))
