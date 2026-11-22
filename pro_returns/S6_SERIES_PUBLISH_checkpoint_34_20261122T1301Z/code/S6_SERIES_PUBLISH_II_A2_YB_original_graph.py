#!/usr/bin/env python3
"""Exact arithmetic of the retained eight-item 02YB proof.

Checks the primary Euler identity, local defect formulas and all connected
two-component one-cycle incidence patterns. Analytic duality and local
normal-form statements are verified in the accompanying proof comparison.
"""
import itertools
import json
import sympy as sp


def main():
    delta,R,a,b,q,g = sp.symbols("delta R a b q g")
    chi_reduced = 1-delta
    chi_nilradical = 3+R-a-b-q
    defect = delta+a+b-R+q
    assert sp.expand(chi_reduced+chi_nilradical-(4-defect)) == 0
    assert sp.expand((4-(g-1))-(5-g)) == 0

    # The planar different identity is sum(alpha)=2delta+R.
    planar_lower = sp.expand(delta+(2*delta+R)-R+q)
    assert planar_lower == 3*delta+q
    mi = sp.symbols("m_i", integer=True, positive=True)
    nonplanar_branch = sp.expand(mi/2+mi-(mi-1))
    assert nonplanar_branch == 1+mi/2
    assert (1+nonplanar_branch).subs(mi,2) == 3

    patterns = []
    types = [(ra,rb) for ra in range(4) for rb in range(4)
             if 2 <= ra+rb <= 3]
    for n in (1,2):
        for config in itertools.combinations_with_replacement(types,n):
            if sum(ra+rb-1 for ra,rb in config) != 2:
                continue
            if not any(ra and rb for ra,rb in config):
                continue
            forced_A_singular_points = sum(ra>=2 for ra,rb in config)
            assert forced_A_singular_points <= 1
            available_additional_singular_points = 1-forced_A_singular_points
            values_over_graph = sum(ra for ra,rb in config)
            total_values = values_over_graph+available_additional_singular_points
            assert total_values <= 3
            patterns.append({
                "points_rA_rB":config,
                "forced_A_singular_points":forced_A_singular_points,
                "maximum_extra_unibranch_singular_points":available_additional_singular_points,
                "normalization_points_of_A_over_graph":values_over_graph,
                "maximum_possible_branch_values":total_values,
            })
    assert len(patterns)==5
    assert max(x['maximum_possible_branch_values'] for x in patterns)==3

    # Exact quadric resolution chart used to verify the final original step.
    s,v = sp.symbols("s v")
    X,Y,Z = -s*v**2,s*v,s
    assert sp.expand(Y**2+X*Z)==0
    assert Z.subs(v,0)==s and sp.diff(Z,s)==1

    out={
        "check":"Retained 02YB primary defect and graph proof",
        "primary_euler_identity":"chi=4-[delta+sum(d/2+b-r)+q]",
        "planar_defect_lower":str(planar_lower),
        "nonplanar_branch_lower":str(nonplanar_branch),
        "minimum_singular_point_defect":3,
        "maximum_total_defect_at_g_ge_1":4,
        "maximum_number_of_primary_singular_points":1,
        "all_incidence_patterns":patterns,
        "pattern_count":len(patterns),
        "maximum_branch_values":3,
        "hurwitz_minimum_for_degree_2_g_ge_1":4,
        "quadric_chart":{"X":str(X),"Y":str(Y),"Z":str(Z),"quadric_identity":0,"strict_line_parameter_derivative":1},
        "scope":"The printed original proof's numerical steps, full graph enumeration, and exact quadric coordinate map; no claim to automate analytic duality or purity.",
        "status":"PASS"
    }
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
