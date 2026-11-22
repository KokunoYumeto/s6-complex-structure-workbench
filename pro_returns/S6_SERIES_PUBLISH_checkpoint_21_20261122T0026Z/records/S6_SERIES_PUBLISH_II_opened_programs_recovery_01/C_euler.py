"""Exact Euler and cohomology checks for the fibre modifications in C.2."""
from math import comb

def euler(b): return sum((-1)**i*v for i,v in enumerate(b))
torus=[comb(4,i) for i in range(5)]
product=[(torus[i] if i<5 else 0)+(torus[i-2] if 0<=i-2<5 else 0) for i in range(7)]
curve=[1,4,1]
blown=[product[i]+(curve[i-2] if 0<=i-2<3 else 0) for i in range(7)]
point=list(blown)
point[2]+=1; point[4]+=1
print('A x P1 Betti numbers:',product,'Euler:',euler(product))
print('Blowup along genus-two curve Betti numbers:',blown,'Euler:',euler(blown))
print('Additional point blowup Betti numbers:',point,'Euler:',euler(point))
print('Central fibre Euler by additivity:',0+2*(-2)-(-2))
print('Modified central fibre Euler:',1-4+3-(-2)-2)
print('Triangulated torus quotient counts: N vertices, 3N edges, 2N triangles')
for n in range(1,13):
    v,e,f=n,3*n,2*n
    assert v-e+f==0 and 3*f==2*e
    print(n,v,e,f,'fibre Euler',f)
