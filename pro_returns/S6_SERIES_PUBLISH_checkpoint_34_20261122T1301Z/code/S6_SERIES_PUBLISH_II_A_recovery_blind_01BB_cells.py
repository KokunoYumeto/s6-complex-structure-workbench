"""Independent prefreeze 01BB Euler and exceptional-form identities."""
from itertools import product

def tensor(a,b):
    result=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):result[i+j]+=u*v
    return result
def euler(a):return sum((-1)**i*v for i,v in enumerate(a))
circle=[1,1]
elliptic=tensor(circle,circle)
p1=[1,0,1]
ruled=tensor(p1,elliptic)
assert elliptic==[1,2,1] and ruled==[1,2,2,2,1]
assert euler(elliptic)==0 and euler(ruled)==0
assert euler(ruled)-euler(elliptic)+euler(elliptic)==0
print('elliptic cell counts',elliptic,'P1 bundle Euler cell sum',ruled,'Euler(S)=0')

# Formal coefficients of x_i*x_j for arbitrary symmetric matrix entries A_ij.
# Coefficients are dictionaries in independent names A_ij, no matrix diagonalization.
def add_term(poly,monomial,symbol,coefficient):
    row=poly.setdefault(monomial,{})
    row[symbol]=row.get(symbol,0)+coefficient
    if row[symbol]==0:del row[symbol]
    if not row:del poly[monomial]
for n in range(1,9):
    lhs={};rhs={}
    for i in range(n):
        for j in range(n):
            symbol=tuple(sorted((i,j)))
            add_term(lhs,tuple(sorted((i,j))),symbol,1)
            add_term(rhs,(i,i),symbol,1)
    for i in range(n):
        for j in range(i+1,n):
            symbol=(i,j)
            add_term(rhs,(i,i),symbol,-1)
            add_term(rhs,(j,j),symbol,-1)
            add_term(rhs,(i,j),symbol,2)
    assert lhs==rhs
print('weighted symmetric quadratic identity checked by formal coefficient construction for sizes 1 through 8')
print('the same coefficient rule proves it for arbitrary size, as written in the derivation')
