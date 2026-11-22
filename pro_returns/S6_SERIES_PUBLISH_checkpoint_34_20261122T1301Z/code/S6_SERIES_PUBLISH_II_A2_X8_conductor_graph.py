#!/usr/bin/env python3
"""Exact graph/Euler calculations for the statement-first 02X8 argument.

Color-family enumeration is complete (three possible nonempty subsets of
two colors). The finite graph examples diagnose the general source/sink
algorithm; the all-graph proof is written in the frozen derivation.
"""
import itertools
import json
import sympy as s


def forest_source_sink(component_vertices, point_vertices, edges):
    vertices=set(component_vertices)|set(point_vertices)
    parent={v:v for v in vertices}
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    incoming={v:0 for v in vertices};outgoing={v:0 for v in vertices}
    colors={v:set() for v in vertices}
    for comp,point,color in edges:
        assert comp in component_vertices and point in point_vertices
        assert color in ('a','b')
        left,right=find(comp),find(point)
        assert left!=right,'underlying graph has a cycle, including parallel edges'
        parent[left]=right
        start,end=(comp,point) if color=='a' else (point,comp)
        outgoing[start]+=1;incoming[end]+=1
        colors[comp].add(color);colors[point].add(color)
    assert edges and all(colors[v]=={'a','b'} for v in component_vertices)
    assert all(colors[v] for v in vertices)
    sources=sorted(v for v in vertices if incoming[v]==0)
    sinks=sorted(v for v in vertices if outgoing[v]==0)
    assert sources and sinks
    assert all(v in point_vertices and colors[v]=={'b'} for v in sources)
    assert all(v in point_vertices and colors[v]=={'a'} for v in sinks)
    assert set(sources).isdisjoint(sinks)
    return {'sources':sources,'sinks':sinks,'source_color':'b','sink_color':'a',
            'local_intersection_condition_fails':True}


def main():
    types=[frozenset('a'),frozenset('b'),frozenset('ab')]
    families=[]
    for r in range(1,4):
        for chosen in itertools.combinations(types,r):
            pairwise=all(x&y for x,y in itertools.combinations(chosen,2))
            has_both_pure=frozenset('a') in chosen and frozenset('b') in chosen
            assert pairwise == (not has_both_pure)
            families.append({'types':[''.join(sorted(x)) for x in chosen],
                             'pairwise_intersect':pairwise,'both_pure_types':has_both_pure})
    examples=[]
    for n in (1,2,5):
        comps={f'c{i}' for i in range(n)};points={f'p{i}' for i in range(n+1)}
        edges=[(f'c{i}',f'p{i}','b') for i in range(n)]+[(f'c{i}',f'p{i+1}','a') for i in range(n)]
        examples.append({'kind':f'chain_{n}','vertices':n+n+1,'edges':len(edges),
                         'result':forest_source_sink(comps,points,edges)})
    branch_edges=[('c0','p0','b'),('c0','p1','a'),('c0','p2','a'),
                  ('c1','p1','b'),('c1','p3','a'),('c2','p2','b'),('c2','p4','a')]
    examples.append({'kind':'branching_tree','vertices':8,'edges':7,
                     'result':forest_source_sink({'c0','c1','c2'},{f'p{i}' for i in range(5)},branch_edges)})
    e,v,k,c=s.symbols('e v k c',integer=True)
    beta=e-v+c
    contracted=(e-k)-(v-k)+c
    added_leaf=(e+1)-(v+1)+c
    suppressed=(e-1)-(v-1)+c
    assert s.expand(contracted-beta)==s.expand(added_leaf-beta)==s.expand(suppressed-beta)==0
    u,q,b=s.symbols('u q b',integer=True,nonnegative=True)
    # c=1+q, e(S_reg)=u; 1=u+c+1-b is exactly u+q+1=b.
    e_support=u+(1+q)+1-b
    residual=s.expand(e_support-1)
    assert residual==u+q+1-b
    assert residual.subs(b,0)==u+q+1
    assert residual.subs(b,1)==u+q
    print(json.dumps({
        'tag':'02X8','phase':'before target-proof release',
        'complete_nonempty_color_type_families':families,
        'forest_algorithm_examples_only':examples,
        'all_graph_proof':'An orientation of a finite forest has no directed cycle. Following predecessors or successors terminates at a source or sink. Component vertices have both directions, so these extrema are point vertices of pure opposite colors.',
        'cycle_rank':str(beta),
        'contract_connected_tree_rank_difference':str(s.expand(contracted-beta)),
        'add_smooth_point_leaf_rank_difference':str(s.expand(added_leaf-beta)),
        'suppress_valence_two_vertex_rank_difference':str(s.expand(suppressed-beta)),
        'euler_one_residual_c_equals_one_plus_q':str(residual),
        'b_zero_residual':str(residual.subs(b,0)),
        'b_one_residual':str(residual.subs(b,1)),
        'nonnegative_euler_solution':{'b':1,'c':1,'e_Sreg':0},
        'limitations':'No analytic finiteness, hypersurface intersection theorem or actual conductor graph is inferred from these examples. The exact morphisms and all-size argument are in the derivation.',
        'all_assertions_passed':True,
    },indent=2))


if __name__=='__main__':
    main()
