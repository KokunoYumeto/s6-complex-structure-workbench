#!/usr/bin/env python3
"""Exact counts in the retained 02X8 argument, after target release.

The symbolic identities apply to all indicated integer parameters.  The
two-component diagnostic refutes applying the connected-curve formula
without its connectedness hypothesis; it does not refute that formula
on its stated domain or the proposition being checked.
"""
import json
import sympy as s


def main():
    k,c,n,u,v,w=s.symbols('k c n u v w',integer=True,nonnegative=True)
    rp=n+u
    rm=c+v
    over_p=s.expand(rp+rm-n)
    beta=s.expand(k-c+over_p+w)
    assert over_p==c+u+v
    assert beta==k+u+v+w
    assert s.expand(beta-k)==u+v+w
    # Normalization exact sequence for a connected reduced compact curve.
    G,R,delta=s.symbols('G R delta',integer=True,nonnegative=True)
    h1=G+delta-c+1
    graph_rank=1-c+R
    delta_excess=delta-R
    assert s.expand(h1-(G+graph_rank+delta_excess))==0
    # D=P1 disjoint union P1, with no identified points.
    diagnostic={'components_k':2,'normalized_components_c':2,
                'sum_branch_excess':0,'true_cycle_rank':2-2+0,
                'connected_formula_outside_its_domain':1-2+0}
    assert diagnostic['true_cycle_rank']==0
    assert diagnostic['connected_formula_outside_its_domain']==-1
    print(json.dumps({
        'tag':'02X8',
        'timing':'after target-proof release',
        'hypotheses':{'k':'b0(D)>=1','c':'number of normalized components>=1',
                      'n':'number of points over the unique two-branch image point>=1',
                      'u':'r_plus-n>=0','v':'r_minus-c>=0',
                      'w':'sum of r_q-1 over all other singular or marked points>=0'},
        'contribution_over_p':str(over_p),
        'full_graph_cycle_rank':str(beta),
        'cycle_rank_minus_k':str(s.expand(beta-k)),
        'forest_contradiction':'The full cycle rank is at least k>=1, whereas a forest has rank zero.',
        'disconnected_domain_diagnostic':diagnostic,
        'normalization_exact_sequence_identity':{
            'h1':str(h1),'sum_normalized_genera':'G',
            'graph_cycle_rank':str(graph_rank),
            'delta_minus_branch_excess':str(delta_excess),
            'identity_difference':str(s.expand(h1-(G+graph_rank+delta_excess)))},
        'limitations':'No coherent direct-image vanishing or analytic normalization theorem is certified by this code. Those steps are justified in the full proof comparison with Grauert formal functions and finite-thickening cohomology. The disconnected example only diagnoses the missing case in the original proof.',
        'all_assertions_passed':True,
    },indent=2))


if __name__=='__main__':
    main()
