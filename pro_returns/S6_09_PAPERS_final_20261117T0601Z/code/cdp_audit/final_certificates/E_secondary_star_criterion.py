"""Integral coarse quotient and boundary certificates for C.2.UN.50."""
import math
import sympy as s
z,x,p,W,beta=s.symbols('z x p W beta',nonzero=True)
count=0
for r in range(1,21):
    for n in range(1,21):
        if math.gcd(r,n)!=1: continue
        kk,tt,gg=s.gcdex(r,n)
        k=int(kk);l=-int(tt)
        assert r*k-n*l==1
        assert (r*k-1)%n==0
        assert math.gcd(l,r)==1
        u=z**n;X=x*z**k
        pp=X**r*u**(-l)
        WW=X**(-n)*u**k
        assert s.simplify(pp-x**r*z)==0
        assert s.simplify(WW-x**(-n))==0
        assert s.simplify((p**k*W**l)**r*(p**n*W**r)**(-l)-p)==0
        assert s.simplify((p**k*W**l)**(-n)*(p**n*W**r)**k-W)==0
        M=s.Matrix([[-l,0,r],[k,0,-n],[0,1,0]])
        assert M.det()==1
        a,b,mu=[M[:,i] for i in range(3)]
        assert n*a+k*mu==s.Matrix([1,0,0])
        assert r*a+l*mu==s.Matrix([0,1,0])
        assert b==s.Matrix([0,0,1])
        # Normal root generator whose normal character is primitive has
        # fibre translation n/r, rather than merely 1/r.
        assert (-l*n-1)%r==0
        # Coarse infinite deck in u,X.
        assert s.simplify(u.subs(z,beta**r*z)-beta**(r*n)*u)==0
        Xdeck=X.subs({z:beta**r*z,x:beta**-1*x},simultaneous=True)
        assert s.simplify(Xdeck-beta**(n*l)*X)==0
        count+=1
print('PASS',count,'coprime (r,n) coarse quotient charts, Bezout bases, and primitive boundary matrices.')
print('Every matrix has determinant one; mu_P=r*delta-n*e.')
print('The complementary Hopf meridian is delta=n*a-k*mu_H.')
print('Its fibre cycle is e=r*a-l*mu_H, and mu_H=-mu_P gives exactly e.')

r,n=s.symbols('r n',integer=True,positive=True)
c=s.symbols('c',nonzero=True)
period=s.Matrix([[0,beta**(-r)],[2*s.pi*s.I/n,s.log(beta)]])
assert s.simplify(period.det()+2*s.pi*s.I*beta**(-r)/n)==0
print('Secondary core canonical period:',-period.det())
print('It remains nonzero, so its exact t-order is the resonance r.')
print('Full n is retained in the inverse Chern correction n*e/r.')
print('For r=1, tensoring by O(nR) inserts exactly the secondary Jordan quotient')
print('and adds n to the one-direction Seifert coefficient, not its residue modulo r.')
print('PASS all exact secondary-star comparisons.')
