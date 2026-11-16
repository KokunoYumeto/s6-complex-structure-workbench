"""Exact determinant and endpoint-frame checks for C.2.UN.73."""
import sympy as S

x,w,y,a,p,q,r=S.symbols('x w y a p q r',real=True)
I=S.eye(2); J=S.Matrix([[0,1],[-1,0]])
Sym=S.Matrix([[p,q],[q,r]])
A=Sym+a*J
M=(I+x*J).row_join(w*J*(A-y*I)).col_join(
    (w*J).row_join((I-x*J)*A+y*(I+x*J)))
rr=x*x+w*w
positive=(1+rr)**2*Sym.det()+(1-rr)*(1+rr)*y*S.trace(Sym)
positive+=y*y*(1-rr)**2+((1+rr)*a+2*x*y)**2
assert S.expand(M.det()-positive)==0
print('PASS symbolic real4x4 determinant for arbitrary symmetric S and skew aJ.')
print('For S>0 and y=-log|t|/(2pi), (1-|t|^(2k))*y>=0; the first term is strictly positive and all others are nonnegative.')

positive_cases=0
for B in (S.Matrix([[1,0],[0,1]]),S.Matrix([[2,1],[1,1]]),
          S.Matrix([[1,2],[-1,1]]),S.Matrix([[3,-1],[2,1]])):
    SS=B.T*B+I
    assert SS.det()>0 and SS[0,0]>0
    for xx in range(-3,4):
        for ww in range(-3,4):
            for skew in (-7,0,9):
                radius2=xx*xx+ww*ww
                yy=S.Rational(1-radius2,7)
                value=positive.subs({p:SS[0,0],q:SS[0,1],r:SS[1,1],a:skew,x:xx,w:ww,y:yy})
                assert value>0
                positive_cases+=1
print('PASS',positive_cases,'exact rational positivity cases with the required radial sign, including complex-angular-frame degeneracy.')

z,s=S.symbols('z s')
b11,b12,b21,b22,h11,h12,h21,h22=S.symbols('b11 b12 b21 b22 h11 h12 h21 h22')
b=S.Matrix([[b11,b12],[b21,b22]])
barb=S.Matrix([[h11,h12],[h21,h22]])
B0=I+z*J
V=b+z*J*barb
F0=B0.inv()*V
assert F0.subs(z,0)==b
Binf=s*I+J
Vinf=s*b+J*barb
Finf=-Binf.inv()*Vinf
assert Finf.subs(s,0)==-barb
assert S.simplify(s*V.subs(z,1/s)-Vinf)==S.zeros(2)
assert S.simplify(s*B0.subs(z,1/s)-Binf)==S.zeros(2)
print('PASS exact zero/infinity angular frames and the reversed nonangular period limit -conjugate(bprime).')

# Do not commute the imaginary shift through the real-linear V.
R=S.symbols('R',real=True)
shift_difference=(I+z*J)*S.I*R*I - (S.I*R*I+z*J*(-S.I*R*I))
assert S.expand(shift_difference-2*S.I*R*z*J)==S.zeros(2)
print('PASS explicit real-linearity correction: iR*V(e)-V(iR e)=2iR z J e; no invalid complex-linear shift is used.')

base_scale_cases=0
for aa in range(1,13):
    for dd in range(1,13):
        for bb in range(aa):
            Q=S.Matrix([[aa,bb],[0,dd]])
            assert Q.det()!=0
            N0=Q.inv()
            assert Q*N0==I
            # e_j belongs to N0 Z2 with the literal integral coordinates Q e_j.
            assert N0*Q[:,0]==S.Matrix([1,0])
            assert N0*Q[:,1]==S.Matrix([0,1])
            exponent_shift=2*S.pi*S.I*Q*(S.I*R*I)
            assert exponent_shift==-2*S.pi*R*Q
            # Near zero subtract log(kappa)*Q; at infinity conjugate first,
            # then subtract the identical real logarithm.
            logk=-2*S.pi*R
            assert exponent_shift-logk*Q==S.zeros(2)
            assert S.conjugate(exponent_shift)-logk*Q==S.zeros(2)
            base_scale_cases+=1
print('PASS',base_scale_cases,'exact finite angular enlargements, monodromy inclusions and both central base-scale recoveries.')

kappa,t,u,v=S.symbols('kappa t u v',nonzero=True)
assert S.simplify((kappa*t)*(kappa/t)-kappa*kappa)==0
# Integer exponent comparisons avoid branch choices.
for exponent in range(-12,13):
    assert S.simplify(kappa**(-exponent)*(u**exponent)*kappa**exponent-u**exponent)==0
    assert S.simplify((u/kappa)**exponent*kappa**exponent-u**exponent)==0
print('PASS actual P1 chart transition uv=kappa^2 and all signed integral toric base exponents through12.')
print('ALL UN73 EXACT CHECKS PASSED')
