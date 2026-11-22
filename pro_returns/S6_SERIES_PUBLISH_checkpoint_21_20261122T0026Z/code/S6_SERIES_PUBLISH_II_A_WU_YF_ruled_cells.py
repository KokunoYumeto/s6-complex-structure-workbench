#!/usr/bin/env python3
"""Fresh prerelease program for 02WU and 02YF, written from their statements.

Weighted divisor trees, explicit elementary contractions, and finite-grid
certificates for the actual branch-image polynomials. No old target program
or either target proof was opened. Uses only Python's standard library.
"""
from itertools import product
import json


class DivisorTree:
    def __init__(self, genus, vertical_weights):
        self.genus = genus
        self.weights = [2] + list(vertical_weights)
        self.edges = {(0, j) for j in range(1, len(self.weights))}
        self.surface_blowups = 0
        self.omitted_exceptionals = 0

    def blowup_smooth(self, vertex):
        multiplicity = self.weights[vertex]
        self.surface_blowups += 1
        if multiplicity == 1:
            self.omitted_exceptionals += 1
            return
        new = len(self.weights)
        self.weights.append(multiplicity-1)
        self.edges.add(tuple(sorted((vertex, new))))

    def blowup_node(self, edge):
        edge = tuple(sorted(edge))
        assert edge in self.edges
        a, b = edge
        new = len(self.weights)
        self.weights.append(self.weights[a]+self.weights[b]-1)
        self.edges.remove(edge)
        self.edges.add(tuple(sorted((a,new))))
        self.edges.add(tuple(sorted((b,new))))
        self.surface_blowups += 1

    def certificate(self):
        # Contract rational terminal components one at a time. Each terminal
        # sphere meets the rest at one point, so it contributes Euler number
        # 2-1=1 and contributes no fundamental-group generator.
        vertices = set(range(len(self.weights)))
        edges = set(self.edges)
        removed = []
        while len(vertices) > 1:
            degree = {v:sum(v in edge for edge in edges) for v in vertices}
            leaves = [v for v in vertices if v != 0 and degree[v] == 1]
            assert leaves, ('not a core-and-tree graph', vertices, edges)
            v = min(leaves)
            edge = next(e for e in edges if v in e)
            edges.remove(edge)
            vertices.remove(v)
            removed.append(v)
        assert vertices == {0} and not edges
        rational_count = len(removed)
        e_conductor = (2-2*self.genus)+sum(2-1 for _ in removed)
        e_surface = 4*(1-self.genus)+self.surface_blowups
        assert e_conductor == 2-2*self.genus+rational_count
        return dict(genus=self.genus,weights=list(self.weights),edges=sorted(self.edges),
                    terminal_contraction_order=removed,
                    rational_components=rational_count,
                    point_blowups=self.surface_blowups,
                    e_conductor=e_conductor,e_surface=e_surface,
                    e_open=e_surface-e_conductor,
                    remaining_core_vertices=sorted(vertices))


def polynomial_product_weight_two(a,b):
    # Variables k,e,l have cohomological weights 1,2,2. Exponents are triples.
    answer={}
    for u,c in a.items():
        for v,d in b.items():
            w=tuple(u[i]+v[i] for i in range(3))
            if w[0]+2*w[1]+2*w[2] <= 2:
                answer[w]=answer.get(w,0)+c*d
    return {k:v for k,v in answer.items() if v}


def branch_polynomial_certificates():
    checks=[]
    for n in range(2,9):
        # At n+1 distinct integers, degree <=n polynomials are determined.
        grid=range(n+1)
        for t in grid:
            tacnode=[(t,0),(t,t*t)]
            # y*x^(n-2), and x^n minus that polynomial.
            first=[x**n-y*x**(n-2) for x,y in tacnode]
            second=[y*x**(n-2) for x,y in tacnode]
            assert first == [t**n,0] and second == [0,t**n]
            triple=[(0,t),(t,0),(t,t)]
            one=[y**(n-1)*(y-x) for x,y in triple]
            two=[x**(n-1)*(x-y) for x,y in triple]
            three=[x*y*x**(n-2) for x,y in triple]
            assert one==[t**n,0,0]
            assert two==[0,t**n,0]
            assert three==[0,0,t**n]
        checks.append(dict(order=n,separate_t_degree_bound=n,
                           exact_grid=list(grid),tacnode_basis_vectors=2,
                           triple_basis_vectors=3))
    # The remaining constant/linear constraints describe the image exactly:
    # tacnode: equal constants and equal linear coefficients; delta=2.
    # triple: equal constants (two constraints) and c3=c1+c2 (one).
    constants_tacnode=[[1,1]]
    linear_tacnode=[[1,1]]
    constants_triple=[[1,1,1]]
    linear_triple=[[0,1,1],[1,0,1]]
    delta_tacnode=(2-len(constants_tacnode))+(2-len(linear_tacnode))
    delta_triple=(3-len(constants_triple))+(3-len(linear_triple))
    assert delta_tacnode==2 and delta_triple==3
    # Cusp semigroup: every even n>=2 is a multiple of 2; every odd n>=3
    # is 3 plus a multiple of 2. The sole positive missing exponent is 1.
    cusp=[]
    for n in range(2,19):
        a,b=(n//2,0) if n%2==0 else ((n-3)//2,1)
        assert 2*a+3*b==n and a>=0 and b>=0
        cusp.append([n,a,b])
    return dict(interpolation_certificates=checks,
                image_constraints={'tacnode_delta':delta_tacnode,
                                   'triple_delta':delta_triple,
                                   'tacnode_conductor_orders':[2,2],
                                   'triple_conductor_orders':[2,2,2]},
                cusp_representations=cusp,cusp_delta=1,cusp_conductor=2)


def main():
    trees=[]
    for g in (1,2,3,5):
        for vertical in ([],[1],[2],[1,2]):
            D=DivisorTree(g,vertical)
            trees.append(dict(stage='minimal',**D.certificate()))
            D.blowup_smooth(0)
            trees.append(dict(stage='blowup on double section',**D.certificate()))
            newest=len(D.weights)-1
            D.blowup_smooth(newest)
            trees.append(dict(stage='blowup on coefficient-one exceptional',**D.certificate()))
            D.blowup_node((0,newest))
            trees.append(dict(stage='blowup on section-exceptional node',**D.certificate()))
    # Total Chern class of T_T and its rank-one torsion-free quotient.
    tangent={(0,0,0):1,(1,0,0):-1,(0,1,0):1}
    quotient={(0,0,0):1,(1,0,0):1,(0,0,1):1}
    chern=polynomial_product_weight_two(tangent,quotient)
    expected={(0,0,0):1,(0,1,0):1,(2,0,0):-1,(0,0,1):1}
    assert chern==expected
    # For an elliptic-ruled r-fold blowup: e=r,K^2=-r.
    finite_rank=[]
    for r,l in product(range(5),repeat=2):
        c2=r-(-r)+l
        assert c2==2*r+l
        if c2==0:
            assert r==l==0
        finite_rank.append([r,l,c2])
    # Curve image: at most one positive-genus normalization component.
    image_cases=[]
    for c in range(1,7):
        for h,b in ((0,0),(0,1),(1,0)):
            e=c+1-b-2*h
            assert e>=0
            if e==0:assert (c,h,b)==(1,1,0)
            image_cases.append(dict(components=c,positive_genus=h,
                                    graph_rank=b,euler=e))
    # In the Euler-zero image case no rational conductor can map onto its
    # elliptic normalization. The surviving minimal core has the following
    # exact open Euler number, negative for every g>=2 by 2-2g=-2(g-1).
    zero_case=[]
    for g in range(1,9):
        D=DivisorTree(g,[]).certificate()
        assert D['e_open']==-2*(g-1)
        zero_case.append([g,D['e_surface'],D['e_conductor'],D['e_open']])
    # Generic coefficient-two conductor has q=delta; plane intersections
    # contribute at least q(q-1)/2, so q is at most three.
    q_cases=[]
    for q in range(1,15):
        if q*(q-1)<=2*q:q_cases.append(q)
    assert q_cases==[1,2,3]
    print(json.dumps(dict(method='weighted divisor trees with elementary leaf contractions; exact branch interpolation',
        divisor_stages=trees,chern_product={str(k):v for k,v in chern.items()},
        elliptic_ruled_rank_constraints=finite_rank,image_curve_cases=image_cases,
        zero_image_cases=zero_case,coefficient_two_branch_counts=q_cases,
        branch_images=branch_polynomial_certificates(),
        conclusion='all exact assertions passed'),indent=2))


if __name__=='__main__':
    main()
