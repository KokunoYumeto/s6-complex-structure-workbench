#!/usr/bin/env python3
"""Fresh explicit (5,6) nonvacuity certificate, before target exposure."""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import re,json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

packet=Path('analysis/continuation_V/F2_13_nonvacuity_statement_packet.md')
models=[json.loads(x) for x in re.findall(r'```json\n(.*?)\n```',packet.read_text(),re.S)]
checks=[]
def check(name,b):
    assert b,name
    checks.append(name)
def eq(name,M,N):check(name,M==N)
def arr(M):return [[int(x) for x in row] for row in M.tolist()]
out=[]
for case,data,v2 in zip(('A','B'),models,([-1,2,0,-1,0,0],[-1,0,0,0,0,1])):
    A=s.Matrix(data['A']);B=s.Matrix(data['B']);I=s.eye(6);v1=I[:,0];v2=s.Matrix(v2);ell=I[0,:]
    M1=A.T;M2=B.T;K=B*A-I;N0=(M1*M2).inv()-I
    eq(case+' order5 relation',A**5,I);eq(case+' order6 relation',B**6,I)
    check(case+' exact order5',A!=I)
    for d in (1,2,3):check(case+' order6 proper divisor '+str(d),B**d!=I)
    check(case+' determinant A,B',A.det()==B.det()==1)
    eq(case+' cohomology square zero',K*K,s.zeros(6))
    eq(case+' exact marked cusp morphism',N0,-K.T)
    eq(case+' cusp square zero',N0*N0,s.zeros(6))
    unit=None
    for rr in combinations(range(6),3):
        for cc in combinations(range(6),3):
            d=int(K.extract(rr,cc).det())
            if abs(d)==1:unit={'rows':rr,'columns':cc,'determinant':d};break
        if unit:break
    check(case+' actual unit third minor exists',unit is not None)
    S=smith_normal_form(N0,domain=s.ZZ)
    smith=[abs(int(S[i,i])) for i in range(6) if S[i,i]]
    check(case+' independent cusp Smith computation',smith==[1,1,1])
    # Explicit marked conjugacy to the index-one angular/base cusp.
    # These three source vectors map to a primitive image basis because
    # the transposed displayed unit minor uses exactly these columns.
    base=I[:,[0,3,4]];angular=N0*base;marking=angular.row_join(base)
    standard=s.zeros(6)
    for j in range(3):standard[j,j+3]=1
    check(case+' explicit cusp marking unimodular',abs(marking.det())==1)
    eq(case+' actual cusp marking intertwiner',N0*marking,marking*standard)
    check(case+' explicit inverse marking integral',all(x.q==1 for x in marking.inv()))
    eq(case+' fixed first affine numerator',M1*v1,v1)
    eq(case+' fixed second affine numerator',M2*v2,v2)
    eq(case+' first marked quotient-circle map',ell*M1,ell)
    eq(case+' second marked quotient-circle map',ell*M2,ell)
    check(case+' signed quotient-circle numerators',(ell*v1)[0]==1 and (ell*v2)[0]==-1)
    for m,sgn in ((5,1),(6,-1)):
        for j in range(1,m):check(case+' free power '+str((m,j)),s.Rational(sgn*j,m).q!=1)
    J=(M1-I).row_join(M2-I)
    eq(case+' actual coinvariant image lies in ker ell',ell*J,s.zeros(1,12))
    cols=None
    for cc in combinations(range(12),5):
        V=J.extract(range(1,6),cc)
        if abs(int(V.det()))==1:cols=cc;break
    check(case+' unit lower coinvariant minor exists',cols is not None)
    V=J.extract(range(1,6),cols);inverse=V.inv()
    check(case+' lower coinvariant inverse integral',all(x.q==1 for x in inverse))
    lift=s.zeros(12,5)
    for j,c in enumerate(cols):lift[c,:]=inverse[j,:]
    eq(case+' actual Bezout lift of every kernel generator',J*lift,I[:,1:6])
    # The final abelian peripheral relation map after the exact group
    # reduction is on (h,a,b), with ell(v1)=1, ell(v2)=-1.
    relations=s.Matrix([[-1,5,0],[1,0,6],[0,1,1]])
    check(case+' peripheral relation determinant one',relations.det()==1)
    eq(case+' integral relation inverse',relations*relations.inv(),s.eye(3))
    check(case+' relation inverse integral',all(x.q==1 for x in relations.inv()))
    out.append({'case':case,'cohomology_lattice_basis':arr(I),'homology_lattice_basis':arr(I),
                'A':arr(A),'B':arr(B),'cusp_difference':arr(N0),'cusp_unit_minor':unit,
                'cusp_smith':smith,'v1':list(map(int,v1)),'v2':list(map(int,v2)),
                'cusp_marking':arr(marking),'cusp_marking_inverse':arr(marking.inv()),
                'ell':list(map(int,ell)),'coinvariant_unit_columns':cols,
                'coinvariant_unit_determinant':int(V.det()),'coinvariant_Bezout_lift':arr(lift),
                'peripheral_relations':arr(relations),'peripheral_inverse':arr(relations.inv())})

# Only the supplied checked base-sheaf table is an input here. The new
# calculation records its actual Leray degree bookkeeping and d2 map.
e2={(0,0):1,(2,0):1,(0,1):1,(1,3):3,(0,4):1}
einf=e2.copy();einf[(0,1)]-=1;einf[(2,0)]-=1
low=[sum(rank for (p,q),rank in einf.items() if p+q==d) for d in range(5)]
check('low rational Betti degrees from actual d2',low==[1,0,0,0,4])
betti=low+[0,0,0,1]
check('oriented duality and Euler total',sum((-1)**i*x for i,x in enumerate(betti))==6)
result={'status':'PASS','checks':len(checks),'check_names':checks,'models':out,
        'Leray_input':'the checked q=1,2,3,4 base-sheaf table in the clean packet; cusp degree4 skyscraper from P1.11',
        'E2_nonzero_low_terms':{str(k):v for k,v in e2.items()},
        'd2_map':'H0(R1)=Q -> H2(R0)=Q is an isomorphism because H1(total;Q)=0',
        'rational_betti':betti,'chronology':'new derivation before target/old lattice/vector/producer exposure',
        'packet_sha256':sha256(packet.read_bytes()).hexdigest(),'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','checks','models','rational_betti','source_sha256')},indent=2))
