#!/usr/bin/env python3
"""New exact Voronoi/Kuhn and marked integral dual-cell checks for P1.11.
The target proof has not been read. Standard-library arithmetic only.
"""
from fractions import Fraction as Q
from itertools import product,combinations,permutations
from pathlib import Path
import json

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def det(A):
    if not A:return 1
    return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))
def solve(A,b):
    d=det(A)
    if not d:return None
    out=[]
    for k in range(len(A)):
        B=[list(row) for row in A]
        for i in range(len(A)):B[i][k]=b[i]
        out.append(Q(det(B),d))
    return tuple(out)
def norm(v):return 4*dot(v,v)-sum(v)**2
def parity(order):return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
def canonical(vertices):return tuple(sub(v,vertices[0]) for v in vertices)
def cup(indices,simplex):
    assert len(indices)==len(simplex)-1
    out=1
    for j,i in enumerate(indices):out*=simplex[j+1][i]-simplex[j][i]
    return out

def main():
    o=(0,0,0);e=[(1,0,0),(0,1,0),(0,0,1)]
    positive=[v for v in product((0,1),repeat=3) if v!=o]
    facets=positive+[neg(v) for v in positive]
    rhs={v:Q(norm(v),2) for v in facets}
    vertices=set()
    for normals in combinations(facets,3):
        y=solve([list(v) for v in normals],[rhs[v] for v in normals])
        if y and all(dot(v,y)<=rhs[v] for v in facets):vertices.add(y)
    assert len(vertices)==24
    observed_tetrahedra=set();distance_checks=0
    for y in vertices:
        tight=[v for v in facets if dot(v,y)==rhs[v]]
        assert len(tight)==3
        tetra=frozenset([o]+tight);observed_tetrahedra.add(tetra)
        base=tuple(min(v[i] for v in tetra) for i in range(3))
        chain=sorted((sub(v,base) for v in tetra),key=sum)
        assert [sum(v) for v in chain]==[0,1,2,3]
        directions=[sub(chain[i+1],chain[i]) for i in range(3)]
        assert sorted(directions)==sorted(e)
        assert abs(det([list(x) for x in directions]))==1
        for nu in product(range(-2,3),repeat=3):
            diff=norm(nu)-2*dot(nu,y)
            assert diff>=0
            assert (diff==0)==(nu in tetra)
            distance_checks+=1
    expected=set()
    for base in product((-1,0),repeat=3):
        for order in permutations(range(3)):
            chain=[base]
            for i in order:chain.append(add(chain[-1],e[i]))
            if o in chain:expected.add(frozenset(chain))
    assert expected==observed_tetrahedra and len(expected)==24
    levelset_checks=0
    superbase=[(-1,-1,-1)]+e
    for nu in product(range(-3,4),repeat=3):
        coeff=[0]+list(nu);m=min(coeff);coeff=[x-m for x in coeff]
        subsets=[{i for i,c in enumerate(coeff) if c>=k} for k in range(1,max(coeff)+1)]
        pieces=[tuple(sum(superbase[i][j] for i in S) for j in range(3)) for S in subsets]
        total=tuple(sum(v[j] for v in pieces) for j in range(3))
        assert total==nu
        assert norm(nu)>=sum(norm(v) for v in pieces)
        if len(pieces)>1:assert norm(nu)>sum(norm(v) for v in pieces)
        levelset_checks+=1
    # Actual periodic Kuhn cochains; integral ordered cup products, not
    # divided alternating cochains.
    simplices={0:[(o,)],1:[(o,w) for w in positive]}
    simplices[2]=[(o,u,w) for w in positive for u in positive if u!=w and all(a<=b for a,b in zip(u,w))]
    simplices[3]=[];top=[]
    for order in permutations(range(3)):
        chain=[o]
        for i in order:chain.append(add(chain[-1],e[i]))
        simplices[3].append(tuple(chain));top.append((parity(order),tuple(chain)))
    cocycle_checks=0;pairing_checks=0;marked=[]
    for p in range(4):
        for J in combinations(range(3),p):
            L=tuple(i for i in range(3) if i not in J)
            eps=parity(L+J)
            coeff=[eps*cup(L,s) for s in simplices[3-p]]
            if 3-p<3:
                for s in simplices[4-p]:
                    value=sum((-1)**i*cup(L,canonical(s[:i]+s[i+1:])) for i in range(len(s)))
                    assert value==0;cocycle_checks+=1
            pairings=[]
            for K in combinations(range(3),p):
                # Cochain-first cap convention: <alpha_K,PD(alpha_L)>
                # equals <alpha_L cup alpha_K,[B]>.
                value=eps*sum(sign*cup(L+K,s) for sign,s in top)
                assert value==int(K==J);pairings.append(value);pairing_checks+=1
            for q in range(4):
                for I in combinations(range(3),q):
                    marked.append({'angular_I':list(I),'base_J':list(J),'dual_cochain_L':list(L),
                                   'PD_orientation_sign':eps,'angular_base_swap_sign':(-1)**(p*q),
                                   'dual_cell_coefficients_before_angular_quotient':coeff})
    E2={(0,0):1,(1,0):3,(2,0):3,(3,0):1,(1,1):6,(2,1):8,(3,1):3,(2,2):7,(3,2):3,(3,3):1}
    possible=[]
    for r in range(2,5):
        for (p,q),rank in E2.items():
            dest=(p-r,q+r-1)
            if dest in E2:possible.append([r,p,q,*dest])
    assert possible==[[2,3,0,1,1]]
    result={'status':'PASS','method':'New exact rational halfspace vertices, lattice-distance and nested-levelset identities; integral ordered Alexander-Whitney cochains and explicit PD orientation',
            'Voronoi_vertices':len(vertices),'Kuhn_tetrahedra_incident_to_origin':len(expected),
            'nearest_lattice_distance_checks':distance_checks,'nested_levelset_checks':levelset_checks,
            'cocycle_checks':cocycle_checks,'marked_PD_pairings':pairing_checks,'marked_tensor_cases':len(marked),
            'only_possible_angular_higher_differential':possible,
            'vertices':[[str(x) for x in y] for y in sorted(vertices)],
            'marked_dual_cell_chains':marked,
            'scope':'Universal Voronoi argument, actual PD map, section-induced vanishing and target-basis map are established in the frozen written note. Finite checks supplement them.'}
    Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['vertices','marked_dual_cell_chains']},indent=2))

if __name__=='__main__':main()
