"""Independent exact polynomial checks for the marked quaternionic audit.

No imported Pro verifier is used. Quaternionic multiplication is implemented
as pairs of complex matrices, retaining the displayed basis and all factors.
"""
from pathlib import Path
import json
import sympy as s

I = s.I
checks = []

def eq(name, a, b):
    d = a-b
    entries = list(d) if isinstance(d, s.MatrixBase) else [d]
    assert all(s.expand(e) == 0 for e in entries), name
    checks.append(name)

def mul(q, r):
    a,b=q; c,d=r
    return a*c-b*d.conjugate(), a*d+b*c.conjugate()

def star(q):
    a,b=q
    return a.conjugate().T, -b.T

def rep(q):
    a,b=q
    return a.row_join(b).col_join((-b.conjugate()).row_join(a.conjugate()))

def B(b):
    c=b.conjugate()
    return s.Matrix([[0,c[2],-c[1]],[-c[2],0,c[0]],[c[1],-c[0],0]])

def moore(q):
    a,b=q
    def entry(i,j):
        return s.Matrix([[a[i,j]]]),s.Matrix([[b[i,j]]])
    def norm(i,j):
        return a[i,j]*s.conjugate(a[i,j])+b[i,j]*s.conjugate(b[i,j])
    cyc=mul(mul(entry(0,1),entry(1,2)),entry(2,0))[0][0]
    return s.expand(a[0,0]*a[1,1]*a[2,2]-a[0,0]*norm(1,2)
                    -a[1,1]*norm(0,2)-a[2,2]*norm(0,1)+cyc+s.conjugate(cyc))

P=s.Matrix([[1,-1,0],[0,1,-1]])
u=s.ones(3,1); C=P*P.T; R=P.T*C.inv(); X=R.row_join(u)
eps=s.Matrix([[0,1],[-1,0]])
eq('marked inverse',X.inv(),P.col_join(u.T/3))
eq('marked determinant',X.det(),1)
D=X.T*X
eq('retained metric',D,s.diag(C.inv(),3))
z=s.Matrix([s.Symbol('z1r',real=True)+I*s.Symbol('z1i',real=True),
            s.Symbol('z2r',real=True)+I*s.Symbol('z2i',real=True)])
chi=s.Matrix([s.Symbol('c1r',real=True)+I*s.Symbol('c1i',real=True),
              s.Symbol('c2r',real=True)+I*s.Symbol('c2i',real=True)])
rr,ri,ga,gd,gr,gi,lam=s.symbols('rr ri ga gd gr gi lam',real=True)
rho=rr+I*ri
G=s.Matrix([[ga,gr+I*gi],[gr-I*gi,gd]])
Ac=G.row_join(z).col_join(z.conjugate().T.row_join(s.Matrix([[lam]])))
xi=chi.col_join(s.Matrix([rho])); b=X.T.inv()*xi; A=X*Ac*X.T
eq('marked complex compression',P*B(b)*P.T,s.conjugate(rho)*eps)
eq('full skew coordinate transport',X.inv()*B(b)*X.T.inv(),B(xi))
w=-eps*chi.conjugate()
eq('charge conjugation inverse',eps*w.conjugate(),chi)
eq('charge conjugation form',(w.conjugate().T*G.adjugate()*w)[0],
   (chi.conjugate().T*G*chi)[0])
N=lam*G.det()-(z.conjugate().T*G.adjugate()*z)[0]-(chi.conjugate().T*G*chi)[0]
cross=rho*(chi.conjugate().T*z)[0]
Nfull=N-cross-s.conjugate(cross)-lam*(rr**2+ri**2)
eq('pair determinant full 15-real-variable polynomial',moore((A,B(b))),
   A.det()-(b.conjugate().T*A*b)[0])
eq('full cubic with marked coordinates',moore((A,B(b))),Nfull)
Bs=B(xi).subs({rr:0,ri:0})
eq('same embedded thirteen-space upper-right',Bs[:2,2],w)
eq('restricted cubic',moore((Ac,Bs)),N)
t=s.Symbol('t',real=True)
point={ga:1,gd:1,gr:0,gi:0,z[0].as_real_imag()[0]:1,
       z[0].as_real_imag()[1]:0,z[1].as_real_imag()[0]:0,z[1].as_real_imag()[1]:0,
       chi[0].as_real_imag()[0]:1,chi[0].as_real_imag()[1]:0,
       chi[1].as_real_imag()[0]:0,chi[1].as_real_imag()[1]:0,lam:3,rr:t,ri:0}
eq('positive-cone transverse polynomial',Nfull.subs(point),1-2*t-3*t**2)
eq('nonzero normal derivative',s.diff(Nfull.subs(point),t).subs(t,0),-2)
Hp=rep((Ac,B(xi))) .subs(point).subs(t,0)
eq('positive witness complex determinant',Hp.det(),1)
assert all(Hp[:k,:k].det()>0 for k in range(1,7))
checks.append('positive witness all six leading minors')

# Jordan multiplication in the original nonunitary marking.
Z3=s.zeros(3)
MA=s.Matrix([[0,0,1],[0,0,0],[1,0,0]])
NB=s.Matrix([[0,0,0],[0,0,1],[0,-1,0]])
q=(X*MA*X.T,Z3); r=(Z3,X*NB*X.T)
qr=mul(q,r); rq=mul(r,q)
prod=tuple((a+b)/2 for a,b in zip(qr,rq))
pulled=(X.inv()*prod[0]*X.T.inv(),X.inv()*prod[1]*X.T.inv())
eq('Jordan nonunitary factor three',pulled[1][:2,:2],-3*eps/2)
r_k=(Z3,I*X*NB*X.T)
qr_k=mul(q,r_k); rq_k=mul(r_k,q)
prod_k=tuple((a+b)/2 for a,b in zip(qr_k,rq_k))
eq('Jordan independent k direction',
   (X.inv()*prod_k[1]*X.T.inv())[:2,:2],-3*I*eps/2)

# Correct direct-product left-action order, plus an explicit failure of gZk.
k1=eps; k2=s.diag(I,-I); Z=s.eye(2)
assert k2*k1 != k1*k2
checks.append('printed direct-product left-action law fails for noncommuting k')
eq('corrected left-action order',Z*k2.inv()*k1.inv(),Z*(k1*k2).inv())

# Exact scalar mechanics from the packet's kinetic terms, no gauge fields.
kap,m2,gam=s.symbols('kappa m2 Gamma',real=True)
bx=s.Matrix(s.symbols('b1 b2 b3',real=True))
Phi=s.diag(1,-1,0)
sv=s.trace(Phi**2)+2*(bx.T*bx)[0]
V=m2*sv/2+gam*sv**2/4-kap*(Phi.det()-(bx.T*Phi*bx)[0])
acc=s.Matrix([-s.diff(V,v)/2 for v in bx])
eq('full b acceleration',acc,-((m2+gam*sv)*s.eye(3)+kap*Phi)*bx)
eq('actual model omitted acceleration',(u.T*acc)[0].subs(dict(zip(bx,[1,-1,0]))),-2*kap)
eq('marked normal coupling',(u.T*A*b)[0],3*((z.conjugate().T*chi)[0]+lam*rho))
Qu=s.eye(3)-u*u.T/3
eq('projected reaction tangent',u.T*(-Qu*((m2+gam*sv)*s.eye(3)+kap*Phi)*Qu*bx),s.zeros(1,1))

# Anti-Hermitian gauge sign, with signature (+---).
E=s.diag(I,-I,0)
trFF=-2*s.trace(E*E)
eq('electric trace contraction',trFF,4)
eq('printed electric density coefficient',-trFF/2,-2)
eq('repaired electric density coefficient',trFF/2,2)

result={'status':'PASS','checks':checks,'check_count':len(checks),
        'sympy_version':s.__version__, 'normal_acceleration':'-2*kappa',
        'positive_witness_determinant':'1 - 2*t - 3*t**2',
        'jordan_block_j_coefficient':str(-3*eps/2),
        'scope':'Polynomial identities and explicit counterexamples; proofs are in quaternionic_4441_reconciliation.tex.'}
(Path(__file__).parent/'independent_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
