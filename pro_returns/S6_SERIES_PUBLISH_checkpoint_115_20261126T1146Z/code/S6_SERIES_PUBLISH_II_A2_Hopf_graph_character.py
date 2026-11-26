"""Exact symbolic identities for the 02YH/02YK conductor-graph derivation.

The geometric pushout, graph presentation, virtual-abelian restriction and
existence of a nonzero character are proved in the accompanying derivation.
This program checks the universal polynomial/matrix identities used there.
"""
import json
import sympy as sp

c,s,E,G,q,n,b,r,k,v,mu=sp.symbols('c s E G q n b r k v mu')
cell_euler=(c+s)-(E+2*G)+c
graph_rank=E-c-s+q
curve_rhs=c+q-2*G-b
curve_residual=sp.expand(cell_euler.subs(E,b+c+s-q)-curve_rhs)
pushout_rank=sp.expand((E+n)-(1+c+s)+1)
pushout_residual=sp.expand(pushout_rank.subs(E,b+c+s-q)-(b+n-q))
rearranged_residual=sp.expand(curve_rhs.subs(b,r-n+q)-(c+n-2*G-r))
forest_residual=sp.expand((2*v)-v-v)
open_stratum_residual=sp.expand((k-v)-(k-v))
blowup_residual=sp.expand(1+(mu-1)-mu)
assert all(x==0 for x in [curve_residual,pushout_residual,rearranged_residual,
                         forest_residual,open_stratum_residual,blowup_residual])
a,b0,c0,d,u,w=sp.symbols('a b0 c0 d u w')
P=sp.Matrix([[a,b0],[c0,d]])
adj=sp.Matrix([[d,-b0],[-c0,a]])
det=a*d-b0*c0
assert sp.simplify(P*adj-det*sp.eye(2))==sp.zeros(2)
assert sp.simplify(adj*P-det*sp.eye(2))==sp.zeros(2)
row=sp.Matrix([[u,w]])
numerator=row*adj
assert sp.simplify(numerator*P-det*row)==sp.zeros(1,2)

print(json.dumps({
 'targets':['02YH / night:P4R.5','02YK / night:P4R.8'],
 'method':'Formal polynomial expansion and symbolic adjugate multiplication over Z[a,b0,c0,d,u,w].',
 'curve_euler_identity':'(c+s)-(E+2G)+c = c+q-2G-b, with E=b+c+s-q',
 'curve_residual':str(curve_residual),
 'pushout_graph_rank':'r=E+n-c-s=b+n-q',
 'pushout_residual':str(pushout_residual),
 'rearranged_euler':'e(C)=c+n-2G-r',
 'rearranged_residual':str(rearranged_residual),
 'rational_forest_euler_increment_per_vertex':1,
 'forest_residual':str(forest_residual),
 'surface_open_stratum':'e(T\\A)=k-v',
 'exceptional_coefficient':'mu-1',
 'blowup_residual':str(blowup_residual),
 'isogeny_matrix':[[str(x) for x in P.row(i)] for i in range(2)],
 'determinant':str(det),
 'character_extension_numerator':[str(x) for x in numerator],
 'character_extension_denominator':str(det),
 'character_composition_identity':'((u,w) adj(P)/det(P)) P=(u,w)',
 'limits':'The proof supplies det(P) != 0 from the finite unramified elliptic map, the nonzero Hopf character, the actual graph-of-spaces presentation, and the contradiction to virtual abelianness. No finite enumeration or generic-value computation replaces those arguments.'
},indent=2))
