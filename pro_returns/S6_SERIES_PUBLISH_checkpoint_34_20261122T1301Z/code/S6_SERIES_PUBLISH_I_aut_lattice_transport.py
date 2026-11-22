from pathlib import Path
import json
import sympy as s
r=Path(__file__).resolve().parents[1]
Q=s.Matrix([[0,-1,0],[0,0,1],[-2,-1,0],[1,0,0]])
K=s.Matrix([[0,1,2],[1,0,0],[0,1,0],[0,0,1]])
T=s.Matrix([[0,0,1],[-2,-1,0],[1,0,0]])
L=s.Matrix([[3,0,1],[-6,1,-1],[-2,1,0]])
C=s.Matrix([[-6,1,-1],[2,-1,0],[0,1,1],[-3,0,-1]])
assert K*T==Q
assert Q*L==-C
assert abs(T.det())==abs(L.det())==1
native=lambda M:[[int(x) for x in row] for row in M.tolist()]
out={'Q':native(Q),'K':native(K),'T':native(T),'L':native(L),'C':native(C),
     'identities':['K*T=Q','Q*L=-C'],'det_T':int(T.det()),'det_L':int(L.det()),
     'interpretation':'Night parameters (A,B,C) map to body pair coefficients (-B,C,-2A-B,A). The minus sign is the exact conversion from (A_j-I) to (I-A_j) coboundaries. Both integral quotients vanish via unimodular parameter maps.',
     'scope':'Post-reading exact comparison of the two supplied integral proofs; no preread derivation claim.'}
(r/'records/S6_SERIES_PUBLISH_I_aut_lattice_transport.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
