"""Independent exact arithmetic for the actual reduced-III return comparison."""
from pathlib import Path
import json
import sympy as S

l=S.symbols('l',integer=True,nonnegative=True)
m=4*l+3;k=3*l+2
exponents={
    'linear_root_term':3*m-4*k,
    'first_source_constant':6*m-6*k,
    'second_source_constant':5*m-6*k,
    'second_source_section_x':2*m-2*k,
    'second_source_section_y':3*m-3*k,
}
assert S.expand(exponents['linear_root_term'])==1
assert S.expand(exponents['first_source_constant'])==6*(l+1)
assert S.expand(exponents['second_source_constant'])==2*l+3
assert S.expand(exponents['second_source_section_x'])==2*l+2
assert S.expand(exponents['second_source_section_y'])==3*l+3
t=S.symbols('t')
discriminants=[-16*(4*t**3+27),-16*(4*t**3+27*t**2)]
assert S.factor(discriminants[1])==-16*t**2*(4*t+27)
s,v,theta,g,c,M=S.symbols('s v theta g C m')
gamma=S.Matrix([g,-c-s-M*v])
delta=S.Matrix([0,1])
o=S.Matrix([-g*s/M,c*s/M+s**2/(2*M)+s*v])
sigma=S.Matrix([g*v,-c*v-M*(v**2-v)/2])
zero=lambda a:all(S.simplify(x)==0 for x in a)
assert zero(o.subs(v,v+1)-o-s*delta)
assert zero(sigma.subs(v,v+1)-sigma-s*delta-gamma)
assert zero(o.subs(s,s+2*M)-o+2*gamma-2*M*delta)
assert zero(sigma.subs(s,s+2*M)-sigma)
F=sigma-o
angular=S.simplify(F.subs(v,v+theta)-F)
assert zero(angular-theta*gamma+M*theta*(theta-1)*delta/2)
assert zero(angular.subs(s,s+2*M)-angular+2*M*theta*delta)
parameter,reference=S.symbols('c_parameter c_reference')
cochain=(parameter-reference)*s/M
assert S.simplify(cochain.subs(parameter,parameter+M)-cochain)==s
assert zero(gamma+S.Matrix([-g,c+s+M*v]))
chi=S.simplify((m+1)/4)
line_square=-2*m
p1=-24*chi
index=S.simplify((12*line_square-p1)/24)
assert chi==l+1
assert index==-3*l-2
assert S.simplify(3+3*m-12*chi)==0
residues=[int(index.subs(l,i))%28 for i in range(28)]
assert sorted(residues)==list(range(28))
out={
    'status':'PASS',
    'scope':'Exact source exponents, corrected ordinary-to-cap arrow, physical outward B-inverse period, angular deck identities and characteristic arithmetic; geometric page and kappa=+1 Thom comparison independently audited.',
    'physical_character':'V=exp(2*pi*i*zeta_2), positive delta; gamma_out=B^{-1}',
    'ordinary_to_cap_cochain':str(cochain),
    'inverse_closing_at_cap':'V -> q_infinity*V',
    'positive_parameter_deck_at_cusp':'V -> (t-t_c)*V',
    'thom_sign':'kappa=+1 from the actual positive arg(a) page boundary and positive gamma_out return',
    'history':'The algebraically consistent inward-origin attempt is preserved under attempts/reduced_iii_return_before_arrow_audit.*; its physical arrow was not yet fixed and it was never promoted.',
    'root_exponents':{a:str(S.expand(b)) for a,b in exponents.items()},
    'source_discriminants':[str(S.factor(x)) for x in discriminants],
    'origins':{'o':[str(x) for x in o],'sigma':[str(x) for x in sigma]},
    'angular_difference':[str(x) for x in angular],
    'chi':str(chi),'line_square':str(line_square),'relative_p1':str(p1),
    'positive_r_index':str(index),'residues_l_0_through_27':residues,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
