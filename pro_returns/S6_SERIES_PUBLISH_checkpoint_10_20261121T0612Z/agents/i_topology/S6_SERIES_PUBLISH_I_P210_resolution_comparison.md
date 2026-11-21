# P2.10: selected marked resolution

## Exposure and error scope

This is an exposed final receiving comparison. The complete current P2.10 statement and all eight proof steps were read, then its marked cusp comparison was compared with the corrected A1.2 chart maps. The original attached `S6_SERIES_GRIND_I.tex` contains the same `(b,x)` resolution and the same main-diagonal identification. Thus this step was inherited; it was not introduced by the publication move of P2.10. The error is the identification of that chosen resolution with the receiving marked cusp in Step 7. The node resolution itself is valid. The theorem statement is unchanged by choosing the required ruling.

## Exact receiving map

The node in the two-neck model is `zw=rxy`. For fixed nonzero r put `W=rw` and `u=r²`. Then `zW=u xy`. The exact map to A1.2's node `XY=uZV` is `(X,Y,Z,V)=(z,rw,x,y)`. No reflection of the Tate coordinate or change of marking is used.

The old ideal `(b,x)`, with `z=rb`, gives `(z,x)` on a nonzero fibre and the edge from `(0,0,1)` to `(1,1,1)` of the square. A1.2's fixed edge is from `(1,0,1)` to `(0,1,1)`. The required ideal is `(z,y)`, equivalently `(b,y)`, whose character `z/(ry)` has valuation `alpha+beta-gamma`.

The replacement charts are `b=yk,x=kw` and `y=bj,w=jx`. On their overlap `j=1/k` and `(b,x)=k(y,w)`. In A1.2 chart coordinates, the first has `(V,Y/u,A)=(y,w/r,rk)` and the second `(X,Z,B)=(rb,x,j/r)`. Direct substitution gives exactly the A1.2 node maps, with `AB=1`. The two q-pullbacks are `kyw` and `bxj`. The cone determinants are +1 and −1, so both are smooth unimodular charts with the selected edge.

## Finite quotient and unchanged construction

The involution on the old node variables is `(r,b,w,x,y)→(−r,−b,−w,x,y)`. It preserves `(b,y)`. On the replacement charts it is `(r,y,k,w)→(−r,y,−k,−w)` and `(r,b,j,x)→(−r,−b,−j,x)`. The transition intertwines these maps. The generic comparison uses the invariant coordinate `W=rw`, so it descends through `u=r²` with the same marked generic fibre. Properness, smoothness, reduced NC central divisor and parameter torsion-freeness follow by the same complete gluing and chart proof, now with the explicitly verified ruling.

The first five proof steps and the first blowup are unchanged. The correction replaces only Steps 6–8's small-resolution choice and its receiving/involution comparison. Parent's requested global propagation scan found the three selected-ideal occurrences and main-diagonal identification inside P2.10; the guarded replacement changes all of them together. A1.2 already carries the required corrected edge, and the headline F statement and outline assert the existence/construction without selecting a conflicting local ideal.

## Relation between the two small resolutions

Both resolutions contract properly to `bw=xy` and restrict to the same isomorphism off the node. Their common node blowup has exceptional Segre quadric `[b:x:y:w]=[u0v0:u0v1:u1v0:u1v1]`; projecting to the two projective factors contracts opposite rulings. This supplies the exact comparison morphisms. No claim that the resulting compact threefolds are nonisomorphic is required or made.

## Literature and computation

Engel Proposition 2.8 permits arbitrary periodic unimodular triangular tilings. Its figure does not prescribe Paper I's marked anti-diagonal. The corrected text therefore attributes the general construction to that proposition and fixes the selected edge through A1.2's exact map.

The actual fresh execution `code/S6_SERIES_PUBLISH_I_P210_resolution_exact.py` verifies both node equations, both chart maps, inverse overlap, the two A1.2 substitutions, both involution lifts, q-products, and cone determinants. Every residual is exactly zero. The output is `output/S6_SERIES_PUBLISH_I_P210_resolution_exact.json`. The event ledger has one exposed reread and one scoped computation, with no before-proof targeted credit. The error record is separate and creates no extra independent check.
