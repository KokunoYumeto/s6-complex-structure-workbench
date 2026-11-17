import sympy as s
x,l,u,X,Y=s.symbols('x l u X Y')
f=x**5+l**3*x+l**4
ls=-s.Rational(256,3125);xs=-5*ls/4
print('discriminant',s.factor(s.discriminant(f,x)))
for name,expr in [('f',f),('fx',s.diff(f,x)),('fxx',s.diff(f,x,2)),('flambda',s.diff(f,l))]: print(name,s.factor(expr.subs({x:xs,l:ls})))
print('lambda_star',ls,'x_star',xs)
print('zero_chart',s.expand(f.subs({l:u**8,x:u**6*X})/u**30))
print('infinity_chart',s.expand(f.subs({l:u**-5,x:u**-4*X})*u**20))
print('zero_central_discriminant',s.discriminant(X**5+X,X))
print('infinity_central_discriminant',s.discriminant(X**5+1,X))
print('Hodge_degrees',s.Rational(6,5)-s.Rational(9,8),s.Rational(2,5)-s.Rational(3,8))
