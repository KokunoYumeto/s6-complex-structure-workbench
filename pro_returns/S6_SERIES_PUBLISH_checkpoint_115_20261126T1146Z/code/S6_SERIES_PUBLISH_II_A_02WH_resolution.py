import sympy as s
t,x,u,k,y,v,l=s.symbols('t x u k y v l')
delta=4+27*t**12
assert s.gcd(delta,s.diff(delta,t))==1
print('discriminant degree',s.degree(delta,t),'gcd with derivative',s.gcd(delta,s.diff(delta,t)))
chart1={y:-k*u,v:-k*x}; chart2={u:-l*y,x:-l*v}
for j,c in enumerate([chart1,chart2],1):
 assert s.expand((x*y-u*v).subs(c,simultaneous=True))==0
 print('chart',j,'base',s.factor((x*y).subs(c,simultaneous=True)))
assert s.expand(((y-v)-k*(x-u)).subs(chart1,simultaneous=True))==0
assert s.expand(((x-u)-l*(y-v)).subs(chart2,simultaneous=True))==0
ss,X,Y=s.symbols('ss X Y',nonzero=True)
# dt wedge dx/(2y), using t=1/s, x=X/s², y=Y/s³.
J=s.Matrix([1/ss,X/ss**2]).jacobian([ss,X]).det()
assert s.simplify(J/(2*Y/ss**3)+1/(2*ss*Y))==0
print('canonical transition coefficient',s.factor(J/(2*Y/ss**3)))
print('resolved fibre Euler',1*1+(2-1),'total',12*(1*1+2-1))
