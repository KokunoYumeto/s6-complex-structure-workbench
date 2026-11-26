"""Post-release exact cyclic quotient maps in the retained WZ proof.

For primitive lambda=(a,b), K=Z(-b,a).  Under an integral full-rank
matrix P the saturation of P(K) has primitive generator P(-b,a)/e,
where e is the gcd of its coordinates.  The annihilating primitive row
then induces a nonzero integer multiplier on the edge quotient.
"""
import json,math
import sympy as S

a,b,p,q,r,s=S.symbols('a b p q r s',integer=True)
P=S.Matrix([[p,q],[r,s]])
k=S.Matrix([-b,a])
image=P*k
annihilator=S.Matrix([[-image[1],image[0]]])
identity=annihilator*P+P.det()*S.Matrix([[a,b]])
assert identity.applyfunc(S.expand)==S.zeros(1,2)

examples=[
 ([[2,0],[0,3]],[2,2]),
 ([[1,1],[0,2]],[3,0]),
 ([[2,4],[0,2]],[0,5]),
 ([[0,2],[3,1]],[3,-3]),
 ([[1,0],[0,1]],[2,3]),
 ([[-2,1],[1,2]],[-4,6]),
]
out=[]
for matrix,row in examples:
    Q=S.Matrix(matrix);assert Q.det()!=0
    d=math.gcd(*row);assert d>0
    lam=[x//d for x in row];aa,bb=lam
    assert math.gcd(aa,bb)==1
    ker=S.Matrix([-bb,aa]);qker=Q*ker
    e=math.gcd(int(qker[0]),int(qker[1]));assert e>0
    sat=qker/e
    target_row=S.Matrix([[-sat[1],sat[0]]])
    mult=-int(Q.det())//e
    assert int(Q.det())%e==0 and mult!=0
    assert target_row*Q==mult*S.Matrix([lam])
    assert target_row*sat==S.zeros(1,1)
    assert math.gcd(int(target_row[0]),int(target_row[1]))==1
    out.append({'P':matrix,'h_a':row,'primitive_source_quotient_row':lam,
        'source_kernel_generator':[int(x) for x in ker],
        'image_kernel_generator':[int(x) for x in qker],
        'saturation_index':e,'saturated_generator':[int(x) for x in sat],
        'primitive_target_quotient_row':[int(x) for x in target_row],
        'edge_to_T_multiplier':d,'edge_to_elliptic_multiplier':mult,
        'both_maps_injective':True})

print(json.dumps({
 'scope':'Universal polynomial identity for the saturated cyclic quotient, with six exact integral diagnostics. Bezout and the normal-form argument are supplied in the comparison.',
 'symbolic_source_kernel_generator':[str(x) for x in k],
 'symbolic_image_kernel_generator':[str(x) for x in image],
 'unsaturated_annihilator_row':[str(x) for x in annihilator],
 'universal_identity':'(-v2,v1)*P = -det(P)*(a,b), where v=P*(-b,a)',
 'identity_residual':['0','0'],
 'saturated_target_multiplier':'-det(P)/gcd(v1,v2)',
 'integrality_reason':'The target quotient row is integral. Compose it with an integral Bezout section of the primitive source row (a,b).',
 'integer_diagnostics':out,
 'whole_group_certificate_claim':False,
 'additional_check_event_claim':False
},indent=2))
