"""Post-release algebra for the nine retained 02WY proof steps.

This uses coefficient extraction and linear-system elimination.  It checks
the local normal-crossing calculation and the class-VII contradiction, not
the analytic classification or the topological pushout theorem.
"""
import json
import sympy as S

z,K,c2,normal=S.symbols('z K c2 normal')
total=S.Poly((1-K*z+c2*z**2)*(1+normal*z),z)
normal_value=S.solve(total.coeff_monomial(z),normal)[0]
c2_value=S.solve(total.coeff_monomial(z**2).subs(normal,normal_value),c2)[0]
assert normal_value==K and c2_value==K**2

chi,e,gamma,T=S.symbols('chi e gamma T')
# Noether plus the immersion identity, the branch-cover normalization
# identity, and the Cartier-divisor coherent Euler identity.
solution=S.solve([e-6*chi,gamma-3*T,chi-gamma/2+T],[e,gamma,T],dict=True)[0]
topological_e=S.expand(solution[e]-solution[gamma]+solution[T])
assert solution[T]==2*chi
assert topological_e==2*chi

n,k=S.symbols('n k',integer=True,nonnegative=True)
class_VII_e=n+k
class_VII_K2=-n-k
obstruction=S.expand(class_VII_e-class_VII_K2)
assert obstruction==2*(n+k)

r=S.symbols('r',integer=True)
local_inclusion_exclusion=[int(j-S.binomial(j,2)+S.binomial(j,3)) for j in (1,2,3)]
assert local_inclusion_exclusion==[1,1,1]

print(json.dumps({
 'scope':'Post-release exact algebra for retained original claims; no whole-proof certificate.',
 'normalization_immersion':{'first_chern_equation':str(total.coeff_monomial(z)),
     'second_chern_equation':str(total.coeff_monomial(z**2)),
     'normal_class':str(normal_value),'c2':str(c2_value)},
 'normal_crossing_single_support':{'sum_normalization_euler':str(solution[e]),
     'normalized_double_curve_euler':str(solution[gamma]),'triple_points':str(solution[T]),
     'support_euler':str(topological_e),'rational_single_component_chi_1_value':int(topological_e.subs(chi,1)),
     'local_branch_alternating_contributions':local_inclusion_exclusion},
 'class_VII_with_k_blowups':{'euler':str(class_VII_e),'canonical_square':str(class_VII_K2),
     'euler_minus_canonical_square':str(obstruction),
     'positive_for_n_positive_and_k_nonnegative':True},
 'event_scope':'Supporting computation in the comparative reread; no extra independent event.'
},indent=2))
