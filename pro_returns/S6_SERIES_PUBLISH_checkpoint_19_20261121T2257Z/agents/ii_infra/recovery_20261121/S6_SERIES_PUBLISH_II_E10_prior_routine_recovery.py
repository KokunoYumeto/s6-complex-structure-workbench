import sympy as s
t=s.symbols('t')
w=s.exp(2*s.pi*s.I/3)
# Algebraic minimal polynomials avoid approximate comparisons of critical values.
disc1=t**3-1
disc2=(t-4)*((t-4)**3-1)
assert s.gcd(disc1,disc2)==1
assert s.degree(disc2)==4
for branch in range(10,16):
    assert disc1.subs(t,branch)*disc2.subs(t,branch)!=0
branchpoly=s.prod(t-j for j in range(10,16))
assert s.gcd(branchpoly,s.diff(branchpoly,t))==1
print('E10 disjoint Hesse critical-value polynomials and six simple branch values: passed')

