#!/usr/bin/env python3
"""New exact simultaneous-kernel / coordinate-solving check, written before proof exposure.
No symbolic algebra library, no import of legacy verifier, no direct evaluation of T*P-P*A.
Primary inputs are the parent-supplied transcriptions; A,v,P,Q,S are transcribed statement data.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
PRIMARY=ROOT/'agents/i_provenance/S6_SERIES_PUBLISH_I_invB10_primary_inputs.json'
PREREQ=OUT/'S6_SERIES_PUBLISH_I_invB10_prerequisite_definitions.json'
STATEMENT=ROOT/'agents/i_provenance/S6_SERIES_PUBLISH_I_invB10_statement_intake.json'
data=json.loads(PRIMARY.read_text())
T=[data['T0'],data['T1']]
A=[[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]],[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]]
P=[[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]]
Q=[[2,-1,0,-2],[2,-1,0,-1],[0,2,1,3],[1,0,0,0]]
S=[[-1,0,0,0],[-6,0,-1,0],[6,-1,0,0],[2,1,1,1]]
v=[[1,2,-4,0],[-1,-3,3,0]]
delta=data['delta_E']
a=[[F(0),F(0),F(0),F(1,3)],[F(-3,4),F(-1,4),F(3,4),F(-1,4)]]

def encode(x):
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    if isinstance(x,F):return x.numerator if x.denominator==1 else str(x)
    return x

def rref(rows, coefficient_columns=None):
    a=[[F(x) for x in row] for row in rows]
    pivot=[]; operations=[]; r=0
    width=len(a[0]) if a else 0
    nc=width if coefficient_columns is None else coefficient_columns
    for c in range(nc):
        h=next((i for i in range(r,len(a)) if a[i][c]),None)
        if h is None:continue
        if h!=r:
            a[r],a[h]=a[h],a[r]; operations.append(['swap',r,h])
        d=a[r][c]
        if d!=1:
            a[r]=[x/d for x in a[r]]; operations.append(['scale',r,1/d])
        for i in range(len(a)):
            if i!=r and a[i][c]:
                multiplier=-a[i][c]
                a[i]=[x+multiplier*y for x,y in zip(a[i],a[r])]
                operations.append(['add',i,r,multiplier])
        pivot.append(c);r+=1
        if r==len(a):break
    # Replay only invertible elementary row operations as a certificate.
    replay=[[F(x) for x in row] for row in rows]
    for op in operations:
        if op[0]=='swap':replay[op[1]],replay[op[2]]=replay[op[2]],replay[op[1]]
        elif op[0]=='scale':
            assert op[2]!=0
            replay[op[1]]=[op[2]*x for x in replay[op[1]]]
        elif op[0]=='add':
            assert op[1]!=op[2]
            replay[op[1]]=[x+op[3]*y for x,y in zip(replay[op[1]],replay[op[2]])]
    assert replay==a
    return a,pivot,operations

def constraints(reverse=False):
    rows=[]
    for t,aa in zip(T,A):
        for i in range(4):
            for j in range(4):
                row=[0]*16
                if reverse:
                    # Coefficients of (T_i X A_i-X)_{ij}; no A inverse required.
                    for k in range(4):
                        for l in range(4):row[4*k+l]+=t[i][k]*aa[l][j]
                    row[4*i+j]-=1
                else:
                    # Coefficients of (T_i X-X A_i)_{ij}, before X is chosen.
                    for k in range(4):
                        row[4*k+j]+=t[i][k]
                        row[4*i+k]-=aa[k][j]
                rows.append(row)
    return rows

def reconstruct_kernel(rows,candidate):
    rr,piv,ops=rref(rows)
    n=len(rows[0]); free=[i for i in range(n) if i not in piv]
    target=[F(x) for x in candidate]
    recon=[F(0)]*n
    for i in free:recon[i]=target[i]
    for j,p in enumerate(piv):recon[p]=-sum(rr[j][i]*target[i] for i in free)
    basis=[]
    for f in free:
        b=[F(0)]*n;b[f]=F(1)
        for j,p in enumerate(piv):b[p]=-rr[j][f]
        basis.append(b)
    assert target==recon
    return {'coefficient_rows':rows,'rref':rr,'pivots':piv,'free_indices_zero_based':free,
            'free_values':[target[i] for i in free],'kernel_basis':basis,
            'candidate':candidate,'reconstruction':recon,'candidate_equal':target==recon,
            'elementary_row_operations':ops,'replay_pass':True}

def solve(rows,rhs):
    aug=[list(row)+[rhs[i]] for i,row in enumerate(rows)]
    rr,piv,ops=rref(aug,len(rows[0]))
    n=len(rows[0])
    assert len(piv)==n
    assert all(any(row[:n]) or row[n]==0 for row in rr)
    x=[F(0)]*n
    for j,p in enumerate(piv):x[p]=rr[j][n]
    return x,{'augmented_rows':aug,'rref':rr,'pivots':piv,'elementary_row_operations':ops,'replay_pass':True}

def inverse(m):
    cols=[]; cert=[]
    for j in range(len(m)):
        col,trace=solve(m,[int(i==j) for i in range(len(m))])
        cols.append(col);cert.append(trace)
    return [[cols[j][i] for j in range(len(m))] for i in range(len(m))],cert

def bareiss(m):
    a=[list(map(int,row)) for row in m]; n=len(a); prev=1; sign=1; trace=[]
    for k in range(n-1):
        h=next((i for i in range(k,n) if a[i][k]),None)
        if h is None:return 0,trace
        if h!=k:a[k],a[h]=a[h],a[k];sign=-sign;trace.append({'swap':[k,h]})
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        trace.append({'step':k,'pivot':pivot,'previous_pivot':prev,'matrix':[[x for x in row] for row in a]})
        prev=pivot
    return sign*a[-1][-1],trace

report={'checker':'/root/i_marking_fresh','target':'Paper I inv:B1.0',
        'computed_utc':datetime.now(timezone.utc).isoformat(),
        'before_target_proof_exposure':True,
        'method':'Exact Fraction RREF of simultaneous intertwiner coefficient systems; reconstruct candidates from free coordinates; solve coordinate systems for maps/vectors; fraction-free Bareiss for determinants. No legacy code or target proof read.',
        'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [PRIMARY,PREREQ,STATEMENT]},
        'transcribed_data':{'A1':A[0],'A2':A[1],'P':P,'Q':Q,'S':S,'v1':v[0],'v2':v[1],'derived_a0':a[0],'derived_a1':a[1]},
        'steps':{}}
report['steps']['positive_intertwiner_kernel']=reconstruct_kernel(constraints(False),sum(P,[]))
report['steps']['reversed_intertwiner_kernel']=reconstruct_kernel(constraints(True),sum(Q,[]))
for label,m in [('P',P),('Q',Q),('S',S),('A1',A[0]),('A2',A[1])]:
    inv,cert=inverse(m);det,dtrace=bareiss(m)
    assert all(x.denominator==1 for row in inv for x in row)
    report['steps'][label+'_integrality']={'inverse':inv,'determinant':det,'inverse_coordinate_certificates':cert,'bareiss_trace':dtrace}
assert report['steps']['P_integrality']['inverse']==[[0,0,0,-1],[-1,-1,-1,-2],[-1,2,0,4],[1,0,1,0]]
assert report['steps']['S_integrality']['inverse']==S
assert report['steps']['P_integrality']['determinant']==-1
assert report['steps']['Q_integrality']['determinant']==-1
assert report['steps']['S_integrality']['determinant']==1
solved_columns=[];cert=[]
for j in range(4):
    col,trace=solve(P,[Q[i][j] for i in range(4)])
    solved_columns.append(col);cert.append(trace)
solved_s=[[solved_columns[j][i] for j in range(4)] for i in range(4)]
assert solved_s==S
report['steps']['S_from_P_coordinates_of_Q']={'solved_S':solved_s,'certificates':cert,'equals_statement_S':True}
d,cert=solve(P,delta)
assert d==[0,0,0,1]
report['steps']['distinguished_circle']={'delta_E':delta,'P_coordinates':d,'certificate':cert,'equals_hatdelta':True}
for j in range(2):
    fixed=[[A[j][r][c]-int(r==c) for c in range(4)] for r in range(4)]
    report['steps']['v'+str(j+1)+'_fixed_lattice']=reconstruct_kernel(fixed,v[j])
    rhs=[-(j+3)*x for x in a[j]]
    recovered,cert=solve(P,rhs)
    assert recovered==v[j]
    report['steps']['affine_vector_'+str(j)]={'m':j+3,'a':a[j],'rhs_minus_m_a':rhs,'P_coordinates_of_minus_m_a':recovered,'equals_v':True,'certificate':cert}
report['summary']={'positive_kernel_rank':14,'reversed_kernel_rank':14,
'positive_integral_family':'X(r,k)=-k*P+r*delta_E*gamma, r,k in Z; chosen (r,k)=(0,-1)',
'reversed_integral_family':'Y(r,k)=k*Q+r*delta_E*gamma, r,k in Z; chosen (r,k)=(0,1)',
'circle_normalization':'X fixes stated delta exactly at k=-1; Y at k=1; the shear r remains free.',
'determinants':{label:report['steps'][label+'_integrality']['determinant'] for label in ['P','Q','S','A1','A2']},
'all_assertions_passed':True,
'limits':'Numerical reconstruction establishes the listed equations and integral maps. Attribution of actual affine conventions and identification of the named marked basis require the supplied geometric convention definitions; uniqueness is not asserted.'}
path=OUT/'S6_SERIES_PUBLISH_I_invB10_exact_reconstruction_output.json'
path.write_text(json.dumps(encode(report),indent=2)+'\n')
print(json.dumps(encode(report['summary']),indent=2))
print('output='+str(path))
print('output_sha256='+hashlib.sha256(path.read_bytes()).hexdigest())
