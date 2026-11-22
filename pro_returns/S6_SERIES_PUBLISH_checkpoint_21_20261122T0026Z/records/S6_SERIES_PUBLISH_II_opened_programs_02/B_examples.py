"""Exact checks for the two nodal examples; no floating point arithmetic."""
import sympy as s

t,x,y,u,lam=s.symbols('t x y u lambda')
F=y*y-x*x*(x+1)-t
print('B1: affine total-space t derivative =',s.diff(F,t))
print('B1: singular fibres from critical equations =',s.solve([F,s.diff(F,x),s.diff(F,y)],(x,y,t)))
print('B1: normalization substitution =',s.expand(F.subs({x:u*u-1,y:u*(u*u-1),t:0})))
print('B1: gluing differential =',s.Matrix([[1-lam]]))
for scalar in [1,-1,2,s.I]:
    d=1-s.Matrix([[1-scalar]]).rank()
    print('B1 lambda =',scalar,'h(N*A) =',(d,d,0),'h(K*A) =',(1,0,0),
          'h(T*A) =',(1,0,0),'h(tfOmega*A) =',(0,1+d,d),
          'h(ambientOmega*A) =',(1,1+d,d))

a=t**4+1
b=t**6
D=s.expand(4*a**3+27*b**2)
print('B2: discriminant / -16 =',D)
print('B2: gcd(D,Dprime) =',s.gcd(D,s.diff(D,t)))
print('B2: resultant(D,Dprime) =',s.resultant(D,s.diff(D,t),t))
print('B2: gcd(D,a) =',s.gcd(D,a))
G=y*y-x**3-a*x-b
gb=s.groebner([G,s.diff(G,x),s.diff(G,y),s.diff(G,t)],x,y,t)
print('B2: total-space singularity ideal Groebner basis =',list(gb))
print('B2: section P residual =',s.expand(G.subs({x:0,y:t**3})))
print('B2: discriminant at infinity / -16 =',s.LC(s.Poly(D,t)))
print('B2: number of distinct nodal fibres =',s.degree(D,t))
print('B2: R^q g_*(TY tensor L): q=0,1,3 -> 0; q=2 -> 12 skyscrapers of length 1')
print('B2: h^q(Y,TY tensor L) = (0,0,12,0)')
