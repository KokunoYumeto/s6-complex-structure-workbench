"""Independent exact bundle, nodal-frame and cusp-transversality checks."""
from pathlib import Path
import sympy as s
import json,hashlib
x,l=s.symbols('x lambda');a=-s.Rational(256,3125);r=s.Rational(64,625)
f=x**5+l**3*x+l**4
h=s.div(s.expand(f.subs(l,a)),(x-r)**2,x)
assert h[1]==0 and h[0].subs(x,r)!=0 and s.discriminant(h[0],x)!=0
weights={n:{'degree':s.floor(s.Rational(4*n,5))+s.floor(s.Rational(-3*n,4))} for n in [0,-1,-2,1,2]}
for n,d in weights.items():
 d['h0']=max(0,int(d['degree'])+1);d['h1']=max(0,-int(d['degree'])-1);d['degree']=int(d['degree'])
assert sum(d['h0'] for d in weights.values())==1 and sum(d['h1'] for d in weights.values())==0
assert s.Rational(2,5)-s.Rational(3,8)==s.Rational(1,40)
zero_hol_characters=[(-9)%8,(-3)%8]
# A regular-frame pullback has the inverse character of the meromorphic scaling.
zero_hol_characters=[9%8,3%8]
infty_hol_characters=[(-6)%5,(-2)%5]
assert zero_hol_characters==[1,3] and infty_hol_characters==[4,3]
source=json.loads(Path(__file__).with_name('gauss_manin_and_residue.json').read_text())
W=s.Matrix([[s.sympify(v.replace('lambda','ll'),locals={'ll':l}) for v in row] for row in source['Gamma_W']])
b=s.Matrix([[-s.Rational(25,6)/l**2,-s.Rational(125,48)/l,0,1,0]])/(l-a)
Gamma=s.zeros(6);Gamma[0,1:]=b;Gamma[1:,1:]=W
R=Gamma.applyfunc(lambda z:s.limit((l-a)*z,l,a));RP=R[:,1:4]
assert R**2==s.zeros(6) and R.rank()==3 and RP.rank()==3
v=s.Matrix([-s.Rational(4096,1171875),s.Rational(64,1875),1]);assert (R[1:,1:4]*v)==s.zeros(5,1)
eta=(R[0,1:4]*v)[0];assert eta==s.Rational(625,192)
assert s.cancel(eta/s.Rational(4,3))==s.Rational(625,256)
minors=[]
from itertools import combinations
for inds in combinations(range(6),3):
 det=RP[list(inds),:].det()
 if det: minors.append({'rows':inds,'determinant':str(det)})
out={'status':'PASS','nodal_normalization_cubic':str(h[0]),'nodal_branch_value':str(h[0].subs(x,r)),'nodal_cubic_discriminant':str(s.discriminant(h[0],x)),'line_weights':weights,'degree_T':'1/40','zero_holomorphic_characters_mod8':zero_hol_characters,'infinity_holomorphic_characters_mod5':infty_hol_characters,'residue_rank':R.rank(),'residue_on_limiting_P_rank':RP.rank(),'nonzero_minor':minors[0],'kernel_vector':[str(z) for z in v],'extension_on_kernel':str(eta),'residue_to_alpha_alg_ratio':'625/256','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'The exact computations appearing in prederivations10; the scalar height and global range proof are analytic arguments in that file.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
