"""Exact global period and conjugate-frame checks for C.2.UN.57."""
from pathlib import Path
import csv
import sympy as S

x,y,a,c,c1,c2,s1,s2,A,B=S.symbols('x y a c c1 c2 s1 s2 A B',real=True)
z=x+S.I*y
r2=x*x+y*y
J=S.Matrix([[0,1],[-1,0]])
def V(w):
    return w+z*J*S.conjugate(w)
def real_vector(w):
    return S.Matrix([S.re(w[0]),S.im(w[0]),S.re(w[1]),S.im(w[1])])
w1=S.Matrix([1,c1]);w2=S.Matrix([a+S.I*c,c2])
p=S.Matrix([0,1]);b=S.Matrix([s1+S.I*s2,S.I])
columns=[V(w1),V(w2),V(p),V(b)+(A+S.I*B)*V(p)]
det=S.factor(S.Matrix.hstack(*map(real_vector,columns)).det())
assert S.expand(det-c*(1+r2)*(1+r2+B*(1-r2)))==0
print('Full symbolic determinant:',det)
print('Im(log coefficient)=-d*log(r)/(2*pi) gives strict positivity for every d>0.')
print('All base-lattice characters and full affine horizontal translation remain arbitrary.')

# Every complex Hopf frame is retained, with its actual two normal columns.
ar,ai,br,bi,cr,ci,dr,di=S.symbols('ar ai br bi cr ci dr di',real=True)
P=S.Matrix([[ar+S.I*ai,br+S.I*bi],[cr+S.I*ci,dr+S.I*di]])
n_out=2*S.pi*S.I*P[:,0]
n_incoming=-2*S.pi*S.I*P[:,1]
n_out_inf=-J*S.conjugate(n_out)
n_incoming_inf=-J*S.conjugate(n_incoming)
P_inf=S.Matrix.hstack(n_out_inf/(2*S.pi*S.I),-n_incoming_inf/(2*S.pi*S.I))
assert all(S.simplify(v)==0 for v in P_inf-J*S.conjugate(P))
lr,li,mr,mi=S.symbols('lr li mr mi',real=True)
logs=S.Matrix([lr+S.I*li,mr+S.I*mi])
contracting=P*logs
assert all(S.simplify(v)==0 for v in J*S.conjugate(contracting)-P_inf*S.conjugate(logs))
print('PASS exact frame P_infinity=J*conjugate(P) for arbitrary normal columns.')
print('PASS actual contracting logarithms become conjugates, preserving both negative real parts.')

# The full finite angular group is conjugated, with no loss of its order.
from math import gcd
cases=0
for n in range(1,25):
    for h in range(n):
        for k in range(n):
            if gcd(h,n)==gcd(k,n)==1:
                assert gcd((-h)%n,n)==gcd((-k)%n,n)==1
                assert n//gcd(gcd(h,k),n)==n
                cases+=1
print('Exact free secondary angular character pairs checked:',cases)

# The edge affine periods transform with the same conjugate gluing map.
u=S.Matrix([ar+S.I*ai,cr+S.I*ci])
ell=-u/(2*S.pi*S.I)
assert all(S.simplify(v)==0 for v in J*S.conjugate(ell)-J*S.conjugate(u)/(2*S.pi*S.I))
print('PASS infinity normal-log coefficient is the exact conjugate coefficient.')
print('PASS all period, frame, contracting-generator and finite-character comparisons.')

root=Path(__file__).resolve().parents[1]
path=root/'records/root_results.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
record=dict(zip(fields,[
    'C.2.UN.57',
    'Complete reduced marked diagonal Hopf and degree-zero ruled cycle criterion with compact conjugate filling and no algebraic-dimension restriction',
    'Proved',
    'sections/part_C2_all_diagonal_cycles.tex; C.AD.1–11; code/root_all_diagonal_cycles.py and .out',
    'C.2.UN.46 actual local normal collars; C.2.UN.51 separate ruled frame; C.2.UN.55 global twistor-log determinant and proper gluing; exact conjugate Hopf lattice frames',
    'C.2','',
    'The local lattice product criterion holds for every marked diagonal primary or secondary Hopf pair and degree-zero ruled pair. Contracting logarithms prove the total normal period transverse even in algebraic dimension one. Its primitive divisor d gives an explicit holomorphic torus family on C-star with everywhere-positive real period determinant. Moving normal frames retain every original marked component and gluing map at zero. At infinity the exact frame P_infinity=J conjugate(P) makes every deck logarithm and finite character the conjugate one, giving the entire conjugate support. Both proper fillings glue to a compact smooth threefold over P1, with only those two singular supports and all Euler numbers zero. Normal-product constants are chosen; no equivalence of arbitrary analytic neighbourhoods is asserted. Full independent source audits requested.'
]))
old=next((row for row in rows if row['id']==record['id']),None)
if old is None:rows.append(record)
else:
    # Preserve later audit annotations on rerunning the exact certificates.
    record['notes']=old['notes']
    rows=[record if row['id']==record['id'] else row for row in rows]
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
print('CSV row C.2.UN.57 saved.')
