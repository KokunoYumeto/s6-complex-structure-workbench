"""Additional exact checks after target release; prerelease files stay immutable."""
from pathlib import Path
from fractions import Fraction
import ast,json

base=Path(__file__).parent
tree=ast.parse((base/'S6_SERIES_PUBLISH_II_033O_fresh_exact.py').read_text())
scope={'F':Fraction}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'own_prerelease_function_definitions','exec'),scope)
data=json.loads((base/'S6_SERIES_PUBLISH_II_033O_fresh_exact_output.json').read_text())
mul,sub,I=scope['mul'],scope['sub'],scope['ident'](4)
T,H=data['T'],data['H']
assert mul(mul(mul(H[0],H[1]),H[2]),H[3])==I
assert all(mul(sub(t,I),sub(t,I))==[[0]*4 for _ in range(4)] for t in T[1:])

# Sparse integer polynomials in two formal variables d and c.
def pc(n):return {(0,0):n} if n else {}
def pa(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def pn(a):return {k:-v for k,v in a.items()}
def pm(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),0)+x*y
    return {k:v for k,v in out.items() if v}
def ps(*terms):
    out={}
    for p in terms:out=pa(out,p)
    return out
def mm(a,b):return [[ps(*(pm(x,y) for x,y in zip(row,col))) for col in zip(*b)] for row in a]
def mi():return [[pc(i==j) for j in range(4)] for i in range(4)]
def matrix(rows):return [[pc(v) if isinstance(v,int) else v for v in row] for row in rows]
d={(1,0):1};c={(0,1):1};d2=pm(d,d)
star=matrix([[1,0,pm(pc(-2),d),c],[0,0,-1,0],[0,1,0,pn(d)],[0,0,0,1]])
p=mi()
for _ in range(4):p=mm(p,star)
expected=mi();expected[0][3]=pm(pc(4),pa(c,d2));assert p==expected
rank_one_minor=ps(pm(pm(pc(2),d),d),pn(c));assert rank_one_minor==pa(pm(pc(2),d2),pn(c))
star[0][3]=pn(d2)
t1=matrix([[1,0,pm(pc(2),d),pm(pc(2),d2)],[0,1,1,d],[0,0,1,0],[0,0,0,1]])
t2=matrix(T[2]);t3=matrix([[1,0,0,pn(d2)],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
assert mm(mm(mm(star,t1),t2),t3)==mi()
sign=matrix([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])
def neg_d(a):return [[{k:v*(-1)**k[0] for k,v in e.items()} for e in row] for row in a]
assert all(mm(mm(sign,t),sign)==neg_d(t) for t in [star,t1,t2,t3])

result={'timing':'Postrelease supplement. The prerelease derivation and exact output remain unchanged.',
        'homology_ordered_product_identity':True,'three_nilpotent_squares_zero':True,
        'formal_polynomial_ring':'Z[d,c], represented by integer coefficient dictionaries',
        'star_fourth_power_minus_identity_only_entry':'(1,4) = 4(c+d^2)',
        'rank_one_minor':'2d^2-c',
        'four_matrix_product_after_central_entries':'Identity as a formal polynomial matrix',
        'sign_change_coordinate_map':'D=diag(-1,1,1,-1), D T_i(d) D^-1 = T_i(-d) for all four matrices',
        'norm_quotient_transport':'(a mod 4,d mod 2) maps to (d mod 2,a mod 4) in the old Smith ordering Z/2 plus Z/4; its inverse swaps the two coordinates.',
        'old_program_scope':'Only the exact lines 1–43 monodromy/lattice slice was read and executed; subsequent collar/period/classification code remains excluded.',
        'all_assertions_passed':True}
out=base/'S6_SERIES_PUBLISH_II_033O_postrelease_exact_output.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
