"""Fresh exact original cusp-hexagon calculation, after proof reading.

The finite calculation derives each effective gluing action by transporting
both its oriented side and its annihilating character. It does not assume
that reversing the side preserves the character sign. No historical checker
is imported. The geometric normalization argument remains the printed proof.
"""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as s

checks=[]
def check(name,condition,scope):
    assert condition,name
    checks.append(dict(name=name,result="PASS",scope=scope))

directions=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,-1])]
characters=[s.Matrix([[0,1]]),s.Matrix([[1,0]]),s.Matrix([[1,1]])]
rays=[sgn*v for v in directions for sgn in [1,-1]]
ray_tuples={tuple(v) for v in rays}
actions=[]
for u,v in product(rays,repeat=2):
    A=s.Matrix.hstack(u,v)
    if abs(A.det())!=1:continue
    if {tuple(A*w) for w in rays}!=ray_tuples:continue
    action=[];transports=[]
    for j,(w,r) in enumerate(zip(directions,characters)):
        matches=[(k,alpha) for k,z in enumerate(directions) for alpha in [1,-1] if A*w==alpha*z]
        assert len(matches)==1
        k,alpha=matches[0]
        beta=next(beta for beta in [1,-1] if characters[k]*A==beta*r)
        epsilon=alpha*beta
        action.append((k+1,epsilon))
        transports.append(dict(source_pair=j+1,target_pair=k+1,side_sign=alpha,character_sign=beta,effective_sign=epsilon))
        check(f"side and character map {len(actions)+1}:{j+1}", A*w==alpha*directions[k] and characters[k]*A==beta*r,"exact actual cocharacter pushforward and character pullback")
    actions.append(dict(matrix=A.tolist(),determinant=int(A.det()),effective_action=action,transports=transports))
check("complete integral fan automorphism enumeration",len(actions)==12,"images of the two integral basis vectors must be rays; all36 ordered image pairs examined")
effective={tuple(tuple(z) for z in row['effective_action']) for row in actions}
expected={((1,1),(2,1),(3,1)),((1,-1),(3,1),(2,1)),((2,-1),(3,-1),(1,1)),((2,1),(1,1),(3,-1)),((3,-1),(2,-1),(1,-1)),((3,1),(1,-1),(2,-1))}
check("six original effective actions",effective==expected,"comparison after independently transporting each oriented side and character")
for row in actions:
    neg=(-s.Matrix(row['matrix'])).tolist()
    mate=next(q for q in actions if q['matrix']==neg)
    check("central negative has same effective action",row['effective_action']==mate['effective_action'],"both side and character signs reverse under minus identity")

mu,h,c=s.symbols("mu h c")
C=s.Matrix([[6*mu,h],[c-h,mu]])
B0=s.Matrix([[0,1],[-1,0]])
exponents=[]
for j,(v,r) in enumerate(zip(directions,characters)):
    e=s.expand((r*C*B0*v)[0]);exponents.append(e)
    check(f"cusp exponent {j+1}",s.expand(e-[-mu,6*mu,-7*mu-c][j])==0,"actual r C(0) B0 v; full h cancellation")
    check(f"cusp q power {j+1}",(r*B0**2*v)[0]==0,"remaining power is minus r v")
a,q=s.symbols("a q",nonzero=True)
formal=[q**-1,q**6,q**-7]
target=[-a**-1,a**6,-a**-7]
for j in range(3):check(f"original sign and a power {j+1}",s.cancel(formal[j].subs(q,-a)-target[j])==0,"q=exp(2pi i mu0)=-a; third entry retains exp(-2pi i c)")

constant_data={1:(-1,-1),2:(1,6)}
obstructions=[]
for act in sorted(effective):
    if act==((1,1),(2,1),(3,1)):continue
    witnesses=[]
    for j in [1,2]:
        k,eps=act[j-1]
        if k not in constant_data:continue
        target_sign,target_exp=constant_data[k]
        source_sign,source_exp=constant_data[j]
        # A negative sign is unchanged under inverse; exponents multiply.
        target_exp*=eps
        if target_sign!=source_sign:
            witnesses.append(dict(equation=j,type="opposite real signs",target_sign=target_sign,source_sign=source_sign))
        elif target_exp!=source_exp:
            witnesses.append(dict(equation=j,type="distinct real powers",difference=target_exp-source_exp,reason="a>1 makes a^d unequal to1 for every nonzero integer d"))
    check("nonidentity action has a constant obstruction",bool(witnesses),"exact symbolic sign/power obstruction for every real a>1; no c-value sampling")
    obstructions.append(dict(action=act,witnesses=witnesses))

fixed=[tuple(v) for v in rays if s.Matrix.hstack(v,directions[1]).det()==0]
check("vertical fixed pair",set(fixed)=={(0,1),(0,-1)},"e2 lies exactly in the two rays for the stated opposite-side pair")
out=dict(author="GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family",exposure="after reading the receiving proof; no before-reading independence claimed",method="complete36-basis-image enumeration; integral side pushforward and character pullback; exact symbolic cusp factors",sympy_version=s.__version__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),passed=len(checks),checks=checks,automorphisms=actions,effective_actions=sorted(effective),cusp_exponents=[str(e) for e in exponents],obstructions=obstructions,vertical_fixed_rays=fixed)
print(json.dumps(out,indent=2,default=str))
