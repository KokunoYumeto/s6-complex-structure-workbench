#!/usr/bin/env python3
from pathlib import Path
import datetime,json
import sympy as S
root=Path(__file__).resolve().parents[2]
a,b,c,kappa,alpha,g,eta=S.symbols('a b c kappa alpha g eta',nonzero=True)
q=a*b*c
rows={
 'fixed':(kappa*alpha*b*c,a*b/alpha,1/(kappa*b)),
 'horizontal':(g*eta*b*c,1/(eta*c),a*c/g),
 'diagonal':(1/a,a*b,a*c)}
checks=[]
def z(name,expr):
    val=S.factor(expr)
    assert val==0,(name,val)
    checks.append({'name':name,'difference':str(val),'pass':True})
for name,row in rows.items():z(name+'_physical_height',S.prod(row)-q)
u,v,w=rows['horizontal']
for name,expr in [('horizontal_tangent',eta*v-1/c),
                  ('horizontal_normal_one',g*w-a*c),
                  ('horizontal_normal_two',u/(g*eta)-b*c)]:z(name,expr)
u,v,w=rows['diagonal']
for name,expr in [('diagonal_tangent',u-1/a),
                  ('diagonal_normal_one',v-a*b),
                  ('diagonal_normal_two',w-a*c)]:z(name,expr)
A,B,C=S.symbols('A B C',nonzero=True)
U,V,W=1/A,eta/C,kappa/B
Q=A*B*C
z('fixed_weight_minus_transition',V/(alpha*A*B)-eta/(alpha*Q))
z('fixed_weight_plus_transition',U*kappa*alpha/(B*C)-kappa*alpha/Q)
z('restricted_winding_difference',(-6+0)-(0-0)+6)
base_north=S.Matrix([-3,-3,6])
delta_north=S.Matrix([-3,3,0])
base_south=S.Matrix([3,-6,3])
delta_south=S.Matrix([3,0,-3])
for i in range(3):
    z('north_residual_weight_'+str(i),(base_north+delta_north-S.Matrix([-6,0,6]))[i])
    z('south_transferred_weight_'+str(i),(base_south+delta_south-S.Matrix([6,-6,0]))[i])
rr,phase=S.symbols('radius phase',positive=True)
first=rr**3*phase**3
second=S.sqrt(1-rr**6)
H=S.Matrix([[first,-second],[second,rr**3/phase**3]])
z('SU2_disc_determinant',H.det()-1)
z('SU2_disc_boundary_first',H[0,0].subs(rr,1)-phase**3)
z('SU2_disc_boundary_second',H[1,1].subs(rr,1)-phase**-3)
z('SU2_disc_central_off_diagonal',H[1,0].subs(rr,0)-1)
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'PASS for exact chart identities; common-exterior entries unresolved',
 'checks_count':len(checks),'checks':checks,
 'rho_windings':{'kappa':-6,'alpha':0,'g':0,'eta':0},
 'actual_edge_rows':{n:list(map(str,v)) for n,v in rows.items()},
 'restricted_diagonal_attempt_required_Q_windings':[0,-6],
 'residual_seam_weights':[-6,0,6],
 'transferred_other_vertex_weights':[6,-6,0],
 'SU2_filling_marked_point_degrees':[3,-3],
 'uncomputed':['simultaneous fixed/nonfixed product compatibility','common-exterior variation','nonfixed relative derivatives'],
 'proof':'notes/part3_source_cusp_other_edges_working.md'}
(root/'code/part3/source_cusp_other_edges.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS {len(checks)} exact chart identities. Restricted diagonal-gauge requirements are 0 and -6; no global obstruction or derivative value asserted.')
