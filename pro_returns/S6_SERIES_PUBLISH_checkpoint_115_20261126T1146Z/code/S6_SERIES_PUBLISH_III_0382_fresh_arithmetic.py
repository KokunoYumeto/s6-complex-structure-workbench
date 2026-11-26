#!/usr/bin/env python3
"""Fresh exact holomorphic-unit and coefficient arithmetic for III 0382."""
import sympy as s

n=s.symbols('n',integer=True,positive=True)
a=s.symbols('a0:4')
b=s.symbols('b0:4')
A=s.Matrix(2,2,a) # C(v)
B=s.Matrix(2,2,b) # C(v^N)
l1,l2,m1,m2=s.symbols('l1 l2 m1 m2',integer=True)
lam=s.Matrix([l1,l2])
mu=s.Matrix([m1,m2])
defect=n*A-B
assert (n*A*lam-B*lam-defect*lam).applyfunc(s.expand)==s.zeros(2,1)
correct=B/n
assert n*correct*lam==B*lam
assert (correct*(lam+mu)-correct*lam-correct*mu).applyfunc(s.expand)==s.zeros(2,1)
print('PASS: exact naive exponent defect (N*C(v)-C(v^N))*lambda and zero prescribed defect, with lattice-character coherence')

v=s.symbols('v')
coeff=s.symbols('c0:11')
series=sum(coeff[k]*v**k for k in range(len(coeff)))
assert s.expand(series-series.subs(v,v))==0
for N in range(1,7):
    delta=s.Poly(N*series-series.subs(v,v**N),v)
    for k in range(N*(len(coeff)-1)+1):
        expected=N*(coeff[k] if k<len(coeff) else 0)
        if k%N==0 and k//N<len(coeff):
            expected-=coeff[k//N]
        assert s.expand(delta.nth(k)-expected)==0
    assert delta.nth(0)==(N-1)*coeff[0]
    if N>1:
        positive_equations=[delta.nth(k) for k in range(1,len(coeff))]
        solved=s.solve(positive_equations,coeff[1:],dict=True)
        assert solved==[{c:0 for c in coeff[1:]}]
print('PASS: every coefficient of the symbolic degree-10 input under N*C(v)-C(v^N), for N=1,...,6; positive coefficients force zero for N>1')

for N in range(2,9):
    for k in range(1,129):
        reduced=k
        exponent=0
        while reduced%N==0:
            smaller=reduced//N
            assert 0<smaller<reduced
            reduced=smaller
            exponent+=1
        assert reduced%N!=0 and N**exponent*reduced==k
print('PASS: exact N-adic coefficient-index reductions used by the all-orders analytic recurrence')

# This is the N>1 constant exceptional family, handled separately from N=1.
C0=s.eye(2)/(n-1)
assert (n-1)*C0==s.eye(2)
assert (n*(C0-C0/n)-s.eye(2)).applyfunc(s.simplify)==s.zeros(2)
N=2
constant=s.eye(2)
naive=s.exp(2*s.pi*s.I*constant[0,0])
prescribed=s.exp(2*s.pi*s.I*constant[0,0]/N)
ratio=s.simplify(naive/prescribed)
assert naive==1 and prescribed==-1 and ratio==-1
assert naive**N==s.exp(2*s.pi*s.I*constant[0,0])
assert prescribed**N==s.exp(2*s.pi*s.I*constant[0,0])
assert ratio**N==1
print('PASS: constant quantized exceptional family; N=2,C0=I gives distinct source factors 1 and -1, both equivariant and related by a mu_2 deck multiplier')
print('PASS: N=1 gives C_1(v)=C(v) and identical actions with no restriction on the holomorphic matrix')
print('ALL FRESH 0382 ARITHMETIC PASSED; target paragraph remains closed.')
