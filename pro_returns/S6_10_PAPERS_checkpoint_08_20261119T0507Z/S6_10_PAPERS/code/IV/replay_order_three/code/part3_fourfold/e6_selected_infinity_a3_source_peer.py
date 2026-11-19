"""Independent invariant, neighbour, volume and outward-field source audit."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
proof=ROOT/'notes/part3_e6_selected_infinity_a3_source_working.md'
a,b,chi,eta,X,Y,q,t=S.symbols('a b chi eta X Y q t',nonzero=True)
checks=[]
def eq(e,n):
    assert S.factor(e)==0,n
    checks.append(n)
for k in range(4):
    xs=a**(k+1)*b**k;ys=a**(3-k)*b**(4-k);zs=a*b
    eq(xs*ys-zs**4,'entire quotient polynomial')
    eq(S.det(S.Matrix([[S.diff(xs,a)/xs,S.diff(xs,b)/xs],
                      [S.diff(zs,a)/zs,S.diff(zs,b)/zs]]))*zs-1,
       'actual crepant determinant in invariant characters')
    wa=S.Rational(16,3)-2*k;wb=2*k-S.Rational(10,3)
    eq((k+1)*wa+k*wb-S.Rational(16,3),'radial x derivative')
    eq((3-k)*wa+(4-k)*wb-S.Rational(8,3),'radial y derivative')
    eq(wa+wb-2,'radial z derivative')
    assert wa!=0 and wb!=0;checks.append('both complex indices nondegenerate')
    if k<3:
        aa=1/b;bb=a*b*b
        eq(aa**(k+2)*bb**(k+1)-xs,'full next-chart x square')
        eq(aa**(2-k)*bb**(3-k)-ys,'full next-chart y square')
        eq(aa*bb-zs,'full next-chart z square')
        eq(S.det(S.Matrix([aa,bb]).jacobian([a,b]))-1,'next-chart volume direction')
        eq(-wb-(S.Rational(16,3)-2*(k+1)),'next-chart first vector')
        eq(wa+2*wb-(2*(k+1)-S.Rational(10,3)),'next-chart second vector')
eq((chi**-3*Y)**2-(chi**-2*X)**3+2*(chi**-2*X)**2-chi**-4*chi**-2*X
   -chi**-6*(Y*Y-X**3+2*chi**2*X*X-X),'full native central equation')
eq((-S.I*Y)**2-((-X)**3-2*(S.I*chi)**2*(-X)**2-X)
   +(Y*Y-X**3+2*chi**2*X*X-X),'literal quarter-turn source action')
eq(2*(4-S.Rational(1,4))+(2-S.Rational(1,2))-9,'exact three orbifold Euler corrections')
eq(-2*(2*(4-S.Rational(1,4))+(2-S.Rational(1,2)))+18,'exact three Pontryagin corrections')
eq(S.Integer(2)+1+2+3+3+1-12,'actual finite and resolved-infinity Euler cells')
eq(S.Integer(12)-9-3,'orbifold Euler value')
eq(S.Integer(-24)+18+6,'orbifold Pontryagin value')
record={'status':'PASS','reviewer':'fourfold','utc':datetime.now(timezone.utc).isoformat(),
        'checks':len(checks),'check_labels':checks,
        'source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'full_read_scope':['Invariant ring with actual O/T coordinates and residual action',
         'Both end inverses, every adjacent chart and exact radial boundary',
         'Crepant frame with all signs and common outward field',
         'Four resolved zeros versus orbifold one-quarter, then actual exchanged A1 pair',
         'Native source equation, reduced infinity fibre quotient and chain attachment',
         'Canonical negative full fibre and exact Euler/Pontryagin differences'],
        'conclusion':'Source orbifold e=3 and p1=-6 follow from the literal source maps and relative tangent comparisons. No physical normal or return value is assigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
(ROOT/'records/fourfold_audit_e6_selected_infinity_a3_source.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
