"""Complete finite spectral evaluation for the universal suspension filter.

The input is exactly the eight spectral cases of F.2.14. No bound on matrix
entries or rational conjugacy classes is used.
"""
import sympy as s
x=s.symbols('x')
phi=lambda n:s.cyclotomic_poly(n,x)
cases=[(4,'Phi2^2 Phi4',phi(2)**2*phi(4)),
       (6,'Phi2^2 Phi3',phi(2)**2*phi(3)),
       (6,'Phi2^2 Phi6',phi(2)**2*phi(6)),
       (6,'Phi3 Phi6',phi(3)*phi(6)),
       (8,'Phi8',phi(8)),
       (12,'Phi12',phi(12)),
       (12,'Phi3 Phi4',phi(3)*phi(4)),
       (12,'Phi4 Phi6',phi(4)*phi(6))]
survivors=[]
for n,name,f in cases:
    value=int(f.subs(x,1));bound=s.gcd(n,value)
    forced_index=int(n//bound)
    survives=value%n==0
    if survives:survivors.append((n,name))
    print('linear order',n,'factor',name,'f(1)',value,
          'h divides',int(bound),'minimal possible cap cokernel order',forced_index,
          'passes',survives)
assert survivors==[(4,'Phi2^2 Phi4'),(6,'Phi2^2 Phi3')]
assert phi(5).subs(x,1)==5
print('COMPLETE EIGHT-CASE FILTER PASSED; only (5,4) and (5,6) Phi2^2 Phi3 remain')
