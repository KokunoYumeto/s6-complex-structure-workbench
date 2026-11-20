"""Fresh exact certificate for P1.4 from the literal isolated pencil.

No prior producer, receiving proof, or saved check is read or imported.
The expected target answer was exposed in the statement packet.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s

P=Path(__file__).parent
x,lam,X,Y,t,z,u=s.symbols('x lam X Y t z u')
f=x**5+lam**3*x+lam**4
checks=[]
def check(label,claim):
    assert claim,label
    checks.append(label)
disc=s.discriminant(f,x)
check('literal discriminant',s.expand(disc-lam**15*(256+3125*lam))==0)
star=-s.Rational(256,3125);root=s.Rational(64,625)
q=x**3+2*root*x**2+3*root**2*x+4*root**3
check('unique displayed double root factorization',s.expand(f.subs(lam,star)-(x-root)**2*q)==0)
check('double root equation',f.subs({lam:star,x:root})==0 and s.diff(f,x).subs({lam:star,x:root})==0)
check('exact multiplicity two',s.diff(f,x,2).subs({lam:star,x:root})!=0)
check('remaining cubic simple',s.discriminant(q,x)==-200*root**6 and s.discriminant(q,x)!=0)
check('node distinct from remaining roots',q.subs(x,root)==10*root**3 and q.subs(x,root)!=0)
check('transverse one-parameter smoothing',s.diff(f,lam).subs({lam:star,x:root})==star**3/4 and star**3/4!=0)

g0=Y**2-X**5-X-t**2
gi=Y**2-X**5-t*X-1
check('zero chart exact scaling',s.expand((t**15*Y)**2-f.subs({lam:t**8,x:t**6*X})-t**30*g0)==0)
check('infinity chart exact scaling',s.cancel((t**-10*Y)**2-f.subs({lam:t**-5,x:t**-4*X})-t**-20*gi)==0)
check('zero chart discriminant',s.discriminant(X**5+X+t**2,X)==256+3125*t**8)
check('infinity chart discriminant',s.discriminant(X**5+t*X+1,X)==256*t**5+3125)
for name,F in [('zero',u+u**5+t**2*u**6),('infinity',u+t*u**5+u**6)]:
    check(name+' odd-degree point at infinity smooth',s.diff(F,u).subs(u,0)==1)

phi8=s.cyclotomic_poly(8,z);phi5=s.cyclotomic_poly(5,z)
def rem(expr,mod):return s.rem(s.Poly(s.expand(expr),z),s.Poly(mod,z)).as_expr().expand()
check('zero deck equation',rem(g0.subs({X:z**2*X,Y:z*Y,t:z*t},simultaneous=True)-z**2*g0,phi8)==0)
check('infinity deck equation',rem(gi.subs({X:z**4*X,Y:Y,t:z*t},simultaneous=True)-gi,phi5)==0)
for name,power,mod in [('zero lambda',8,phi8),('zero x',8,phi8),('zero y',16,phi8),('infinity mu',5,phi5),('infinity y',10,phi5)]:
    check(name+' invariant',rem(z**power-1,mod)==0)
check('infinity x invariant',s.cancel(z**-4*z**4)==1)
for m in range(1,8):check('zero Hodge eigenvalue nontrivial power '+str(m),rem(z**m-1,phi8)!=0)
check('zero Hodge eigenvalue order eight',rem(z**8-1,phi8)==0)
for m in range(1,5):check('infinity Hodge eigenvalue nontrivial power '+str(m),rem(z**(4*m)-1,phi5)!=0)
check('infinity Hodge eigenvalue order five',rem(z**20-1,phi5)==0)
check('zero cubic line-character adapter',rem(z**9-z,phi8)==0)
check('infinity cubic line-character adapter',rem(z**9-z**4,phi5)==0)

val0=[6-15,12-15];vali=[-4+10,-8+10]
D1=[s.Rational(val0[0],8),s.Rational(vali[0],5)]
D2=[s.Rational(val0[1],8),s.Rational(vali[1],5)]
check('Hodge valuations',val0==[-9,-3] and vali==[6,2])
check('exact cubic divisor equality',D1==[3*a for a in D2])
check('T degree',sum(D2)==s.Rational(1,40))
check('first Hodge line degree',sum(D1)==s.Rational(3,40))
report={
 'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'checks':checks,
 'scope':'Exact polynomial, deck-character, and rational-divisor identities from the isolated literal pencil. Geometric minimality and the nodal relative-dualizing extension are proved in BEFORE_READING.md.',
 'expected_answer_exposure':'The isolated target statement supplied the expected nodal parameter, root orders, and Hodge splitting before this derivation.',
 'discriminant':str(s.factor(disc)),'nodal_parameter':str(star),'double_root':str(root),
 'nodal_cubic':str(q),'nodal_cubic_discriminant':str(s.discriminant(q,x)),
 'node_smoothing_derivative':str(star**3/4),
 'zero_model':str(g0),'infinity_model':str(gi),
 'zero_deck':{'base':'t -> zeta_8 t','X':'X -> zeta_8^2 X','Y':'Y -> zeta_8 Y'},
 'infinity_deck':{'base':'t -> zeta_5 t','X':'X -> zeta_5^4 X','Y':'Y -> Y'},
 'zero_Hodge_characters':['zeta_8','zeta_8^3'],
 'infinity_Hodge_characters':['zeta_5^4','zeta_5^3'],
 'form_valuations_at_zero':val0,'form_valuations_at_infinity':vali,
 'divisor_dx_over_y':[str(a) for a in D1],
 'divisor_x_dx_over_y':[str(a) for a in D2],
 'T_degree':str(sum(D2)),
 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(P/'p14_exact_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'assertions':len(checks),'discriminant':report['discriminant'],
                  'zero_deck':report['zero_deck'],'infinity_deck':report['infinity_deck'],
                  'T_degree':report['T_degree']},indent=2))
