"""Postrelease basis comparison and a cyclotomic-module certificate.
The fresh prerelease computation is preserved unchanged. This certificate
uses rational invariant-space splitting and polynomial remainders instead
of the historical direct matrix-power assertions.
"""
from pathlib import Path
import hashlib,json
import sympy as s
r=next(p for p in Path(__file__).resolve().parents if (p/'records/S6_SERIES_PUBLISH_II_opened_programs_01/D_exact_checks.py').is_file())
old=r/'records/S6_SERIES_PUBLISH_II_opened_programs_01/D_exact_checks.py';src=old.read_text();begin=src.index('I = s.eye(4)');end=src.index('M0=');scope=src[begin:end];ns={'s':s};exec(scope,ns)
A0=s.Matrix([[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]])
A1=s.Matrix([[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]])
Ai=s.Matrix([[1,0,0,1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
P=s.Matrix([[0,-1,0,-1],[6,0,1,0],[0,1,0,0],[1,0,0,0]])
assert P.det()==-1;assert P*ns['A1']==A0*P;assert P*ns['A2']==A1*P
E=s.zeros(4);E[0,3]=1;F=s.zeros(4);F[3,0]=1;assert P*F==-E*P
C=s.eye(4);C[2,1]=1;C[3,0]=-1;assert P*C==Ai*P
x=s.symbols('x');records=[]
for A,order,poly,comp in [(A0,3,x*x+x+1,s.Matrix([[0,-1],[1,-1]])),(A1,4,x*x+1,s.Matrix([[0,-1],[1,0]]))]:
 fixed=(A-s.eye(4)).nullspace();assert len(fixed)==2
 v=next((A-s.eye(4))[:,j] for j in range(4) if (A-s.eye(4))[:,j]!=s.zeros(4,1))
 Q=s.Matrix.hstack(*fixed,v,A*v);assert Q.det()!=0
 normal=s.diag(s.eye(2),comp);assert A*Q==Q*normal
 rem=s.rem(x**order-1,poly,x);assert rem==0
 records.append({'order':order,'invariant_space_basis_Q':[[str(v) for v in row] for row in Q.tolist()],'det_Q':str(Q.det()),'block_diagonal_form':normal.tolist(),'cyclotomic_relation':str(poly),'x_power_minus_one_remainder':str(rem)})
out={'primary_to_printed_basis_columns':P.tolist(),'det_P':int(P.det()),'exact_maps':{'printed_A1':'P A1_printed = A0_primary P','printed_A2':'P A2_printed = A1_primary P','printed_E':'P E_printed = -E14_primary P','printed_cusp':'P A0_cusp_printed = Ainf_primary P'},'finite_order_cyclotomic_certificates':records,'historical_program_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'historical_scope_sha256':hashlib.sha256(scope.encode()).hexdigest(),'historical_scope':'Only definitions of I,A1,A2 and direct third/fourth-power assertion; this scope executed.','method_difference':'Historical matrix powers; new rational invariant-subspace decomposition to I2 plus cyclotomic companion and polynomial divisibility.','timing':'postrelease supplement, same 033F evidence group','additional_events':0}
q=Path(__file__).with_suffix('.json');q.write_text(json.dumps(out,indent=2,default=str)+'\n');print(json.dumps({'det_P':int(P.det()),'orders':[3,4],'all_basis_identities':True,'method':'cyclotomic invariant-space decomposition','old_scope_executed':True}))
