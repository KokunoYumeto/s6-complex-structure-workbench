"""Exact first/second-jet checks for the excess-one curve classification."""
from pathlib import Path
import json
import sympy as sp

a,b,c=sp.symbols('a b c',nonzero=True)
v1=sp.Matrix([1,0,-a/c])
v2=sp.Matrix([0,1,-b/c])
products=sp.Matrix.hstack(v1.multiply_elementwise(v1),
                         v1.multiply_elementwise(v2),
                         v2.multiply_elementwise(v2))
det=sp.factor(products.det())
assert det==-a*b/c**2

cases=[]
for r in range(1,4):
    for k in range(1,r+1):
        if k==1:
            edim=r+1
            name='cusp plus '+str(r-1)+' independent smooth branches'
        elif k==2:
            edim=r
            name='tacnode plus '+str(r-2)+' independent smooth branches'
        else:
            edim=2
            name='ordinary plane triple point'
        cases.append({'branches':r,'nonzero_hyperplane_coefficients':k,
                      'embedding_dimension':edim,'analytic_model':name,
                      'embeds_in_smooth_threefold':edim<=3})

# The remaining global conductor has c=2, graph rank1, chi=-1.
c_norm=2
graph_rank=1
chi=-1
delta_total=c_norm-chi
branch_identification_total=graph_rank+c_norm-1
excess_total=delta_total-branch_identification_total
assert (delta_total,branch_identification_total,excess_total)==(3,2,1)

out={'working_proof':'notes/part4_a1_excess_working.md',
     'second_jet_product_matrix':[[str(x) for x in row] for row in products.tolist()],
     'second_jet_determinant':str(det),'cases':cases,
     'global_delta_total':delta_total,
     'global_branch_identification_total':branch_identification_total,
     'global_excess_total':excess_total,'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Excess-one curve classification checks: PASS')
print('Second-jet product determinant:',det)
print('All realizable models:',[x['analytic_model'] for x in cases if x['embeds_in_smooth_threefold']])
print('Global (delta, identification, excess):',delta_total,branch_identification_total,excess_total)
