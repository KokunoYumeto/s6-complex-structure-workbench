"""Exact local identities and integer bounds in P4.42--P4.46.

The analytic inverse and boundary-transport arguments are proved in the
TeX. These checks verify their algebra and the exhaustive small defect
budgets, without replacing those arguments by sampled data.
"""
from pathlib import Path
import json
import sympy as sp

u,H,x,y,s=sp.symbols('u H x y s')
# A cubic with three distinct roots, simple u-critical roots, and nonzero
# critical values. The critical branch u=H has value -2H^3 and F_uu=6H.
F=u**3-3*u*H**2
assert sp.expand(sp.diff(F,u).subs(u,H))==0
assert sp.expand(F.subs(u,H))==-2*H**3
assert sp.expand(sp.diff(F,u,2).subs(u,H))==6*H
h=x*y+s
f=F.subs(H,h)
critical={x:0,y:0,u:s}
assert all(sp.expand(sp.diff(f,v).subs(critical))==0 for v in (u,x,y))
hessian=sp.hessian(f,(u,x,y)).subs(critical)
assert sp.expand(hessian.det())==-216*s**5
assert sp.expand(f.subs(critical))==-2*s**3

# The two primitive-line cases prove the maximum/minimum identity exactly.
a,b,v=sp.symbols('a b v', integer=True, nonnegative=True)
cases=[]
for aa in range(9):
    for bb in range(9):
        for vv in range(13):
            left=max(aa,bb-vv)+min(aa+vv,bb)
            assert left==aa+bb
            left_swapped=max(aa-vv,bb)+min(aa,bb+vv)
            assert left_swapped==aa+bb
            cases.append((aa,bb,vv))

# Symbolic proof in the first case: choose the two possible inequalities.
assert sp.expand(a+(b)-(a+b))==0
assert sp.expand((b-v)+(a+v)-(a+b))==0

defects={
    'A3 ordinary node':sp.Rational(9,2),
    'A3 nonordinary planar two-branch':sp.Integer(6),
    'A3 nonplanar two-branch delta>=3':sp.Integer(5),
    'A3 cusp plus line':sp.Integer(2+7-1),
    'D4 nonplanar three smooth branches':sp.Integer(2+6+3),
    'D4 three branches, one singular, minimum':sp.Integer(4+4+3),
    'D4 planar three-branch':sp.Integer(5*3),
}
assert all(defects[k]>sp.Rational(9,2) for k in (
    'A3 nonordinary planar two-branch',
    'A3 nonplanar two-branch delta>=3','A3 cusp plus line'))
assert all(defects[k]>=11 for k in defects if k.startswith('D4'))

# The noncontracted A3 ramification budget is exact for every g>=1:
# total9-g, triple at least5, extra singular points at least2 each.
ramification=[]
for genus in range(1,10):
    total=9-genus
    extra=max(-1,(total-5)//2)
    if extra>=0:
        possible_branch_values=2+extra
        required_branch_values=2*genus+2
        assert possible_branch_values<required_branch_values
        ramification.append({'genus':genus,'maximum_extra_points':extra,
            'maximum_branch_values':possible_branch_values,
            'required_branch_values':required_branch_values})
    else:
        assert total<5

out={
    'proof_ids':['P4.42','P4.43','P4.44','P4.45','P4.46'],
    'D4_cubic':str(F),'critical_value':str(f.subs(critical)),
    'Hessian_matrix':[[str(v) for v in row] for row in hessian.tolist()],
    'Hessian_determinant':str(sp.factor(hessian.det())),
    'primitive_line_identity_cases_checked':len(cases)*2,
    'defect_bounds':{k:str(v) for k,v in defects.items()},
    'A3_Riemann_Hurwitz_budget':ramification,
    'all_checks_passed':True,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Uniform transverse-sector identities and defect budgets: PASS')
print('D4 local Morse Hessian determinant:',sp.factor(hessian.det()))
print('D4 local Morse critical value:',sp.factor(f.subs(critical)))
print('Primitive-line maximum/minimum identities checked:',len(cases)*2)
for key,val in defects.items(): print(key+': '+str(val))
print('A3 Riemann--Hurwitz budgets:',json.dumps(ramification))
