from pathlib import Path
from fractions import Fraction as F
import json,hashlib,shutil,sys,datetime
import sympy as s
W=Path(__file__).resolve().parents[2];SRC=W.parents[1]/'sources/newer_night/checkpoint29';O=W/'code/IV/replay_cp29_retained_batch';out=[]
for rel in ['code/part3_root/scalar_all_fans.py','code/part3_root/source_all_fans.py']:
 p=O/rel;p.parent.mkdir(exist_ok=True,parents=True);shutil.copyfile(SRC/rel,p);assert p.read_bytes()==(SRC/rel).read_bytes();out.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
sys.path.insert(0,str(O/'code/part3_root'))
from scalar_all_fans import calculate
rows=[]
for basis,want in [((3,-1,1,0),15),((1,-2,0,1),3),((1,0,2,1),26)]:
 row=calculate(basis,2,F(1,3),F(1,6),True);assert row['physical_class_mod28']==want;rows.append(row)
assert [x['actual_single_native_right'] for x in rows[0]['steps']]==[0,3,12]
# The displayed input pairs are read directly from the actual predecessor native invariants.
from scalar_all_fans import vertical_seed,child
P,V,D,S=vertical_seed(1,2,F(1,3),F(1,6));pairs=[]
for i in [0,1,1]:pairs.append([V[i][i],D[i]]);P,V,D,S=child(P,V,D,S,i,2)
assert pairs==[[2,2],[-4,8],[-14,34]] and S==15
# Complete local Cox and charged-end matrices, without executing the old script's audit-log side effect.
U=s.Matrix([[0,1,1,0],[0,1,0,1],[1,1,1,1]]);aux=s.Matrix([1,1,-1,-1]);delta=s.Matrix([-1,0,0,1]);assert U*aux==s.zeros(3,1) and U*delta==s.Matrix([0,1,0])
rows2=s.Matrix.vstack(aux.T,delta.T);minors={(i,j):int(rows2[:,[i,j]].det()) for i in range(4) for j in range(i+1,4)};assert all(abs(x)<=1 for x in minors.values())
x=s.Matrix([1,-1]);E1=s.diag(1,-1);E2=s.Matrix([[0,-1],[1,0]]);G=s.Matrix([[0,-1],[-1,0]]);pair=s.Matrix([[0,1],[1,0]])
assert E1*x==E2*x==s.Matrix([1,1]) and G*x==x and G**2==s.eye(2) and G.T*pair*G==pair
# Literal current physical transfer. Earlier programs keep their old central signs.
AU=F(4*6-0,24);AM=-AU;n=-6*AU;assert AU==1 and AM==-1 and n==-6 and AM+n==-7
r={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','role':'Current exact scope reconciliation, separate from unchanged historical-program executions and geometric proof events.','source_function_hashes':out,'original_shorter_examples':rows,'exact_predecessor_pairs':pairs,'cox_two_torus_minors':{str(k):v for k,v in minors.items()},'current_source_loop':{'dual_pair':[6,0],'physical_pair':[-6,0],'physical_reference_index':int(AM),'first_fixed_edge_increment':int(n),'first_fixed_edge_class':int(AM+n)%28,'reflected_class':int(AM)%28},'historical_program_corrections':{'source_cusp_fixed_edge.py':'Its central=1 and class23 are the rejected physical sign. Current central=-1 with the same native right exponent-6 gives21. Exact coordinate and quaternion assertions remain supported.','source_cusp_reflection.py':'Its printed specific class1 is the rejected physical sign; actual oriented reflected class is27. The source, line and fan involution assertions are unchanged.','source_cusp_reflected_pair.py':'Its relative central coordinate+1 is rejected; actual relative tuple is(0,-6,-1). The complete cap-map identities and displayed U pair remain supported.','canonical_scalar_catalogue.py':'Its all_fan fields are the withdrawn norm polynomial. The30 branch, source, cap, height, chi, determinant and complete norm-solution identities remain supported.'}}
(O/'current_scope_reconciliation.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
