"""Fresh integral identities for the actual F2.5 cusp normal closure."""
from pathlib import Path
import json
import sympy as S

M1=S.Matrix([
 [1,0,0,0,0,0],
 [0,1,1,2,2,1],
 [0,-1,0,-1,0,1],
 [1,-1,-1,-1,-1,-1],
 [-1,1,0,0,0,0],
 [1,0,0,1,0,0]])
M2=S.Matrix([
 [1,0,0,0,0,0],
 [0,0,0,0,1,0],
 [0,-1,-1,-1,-1,-1],
 [0,0,0,0,0,1],
 [0,1,0,0,0,0],
 [0,0,1,0,0,0]])
I=S.eye(6)
Z=S.zeros(6)
M0=(M1*M2).inv()
N=M0-I
D=M1*M2-I
checks={}
checks['order_five']=M1**5==I
checks['order_four']=M2**4==I
checks['D_to_N']=D==-(M1*M2)*N
tel=sum((M1**(3-j)*D*M2**(-(j+1)) for j in range(4)),Z)
checks['noncommutative_telescoping']=tel==M1**4-I
first=sum((M1**(4-j)*(M1*M2)*N*M2**(-(j+1)) for j in range(4)),Z)
checks['first_augmentation_in_cusp_closure']=first==M1-I
checks['second_augmentation_in_cusp_closure']=M2-I==-M2*N-M1.inv()*(M1-I)
checks['cusp_in_augmentation']=N==-M0*((M1-I)*M2+(M2-I))
checks['all_identity_coefficients_integral']=all(x.q==1 for j in range(4) for x in M1**(4-j)*(M1*M2)) and all(x.q==1 for j in range(4) for x in M2**(-(j+1)))
ell=S.Matrix([[1,0,0,0,0,0]])
checks['actual_character_preserved']=ell*M1==ell and ell*M2==ell
assert all(checks.values()),checks
out={'checks':checks,'passed':len(checks),'scope':'Exact matrix maps for the isolated normal-closure equality. The primitive cusp and full coinvariant identification remain the already checked P1.1 inputs.','matrices':{'M1':M1.tolist(),'M2':M2.tolist(),'N':N.tolist(),'D':D.tolist()}}
path=Path(__file__).with_suffix('.output.json')
path.write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps({'passed':len(checks),'all_pass':all(checks.values())}))
