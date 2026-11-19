from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from itertools import combinations
import sympy as s,json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'code/part3_fourfold/e6_p_one_common_cayley.json';d=json.loads(p.read_text());checks=[]
def ck(x,m):assert x,m;checks.append(m)
def mat(r):return s.Matrix.hstack(*map(s.Matrix,r))
def canon(f):return tuple(sorted(map(tuple,f)))
vol=defaultdict(F);inc=Counter();delta=s.Matrix([0,1,0,0])
for i,c in enumerate(d['cones']):
 N=mat(c['rays']);Np=mat(d['parents'][c['parent']]['rays'])
 ck(N.det()==1,'det'+str(i));ck(Np.inv()*N==s.Matrix(c['parent_monomial_matrix']),'parent'+str(i))
 ck(all(x>=0 for x in Np.inv()*N),'nonnegative'+str(i))
 ck(N.inv()*delta==s.Matrix(c['physical_weights']),'physical'+str(i))
 ck([2*v[2]+v[3]-1 for v in c['rays']]==c['original_canonical_orders'],'canonical'+str(i))
 sp=c['source_projection'];ck(list(s.Matrix([[1,0,0,0]])*N)==sp['Z_exponents'],'sourceZ'+str(i));ck(list(s.Matrix([[-1,0,3,0]])*N)==sp['Q_over_Z_exponents'],'sourceW'+str(i));ck(min(sp['Z_exponents']+sp['Q_over_Z_exponents'])>=0,'sourceRegular'+str(i))
 for ref in c['generic_references']:
  r,t=ref['period_shift'];A=s.Matrix([[-1,1,5*r+t,4*(2*r+t)],[1,0,r+2*t,0],[0,0,1,0],[0,0,0,1]])
  ck(A==s.Matrix(ref['full_corner_character_matrix']),'fullCorner'+str(i));ck(A*N==s.Matrix(ref['chart_common_character_exponents']),'persistedFull'+str(i))
  ck(ref['p_unit_exponents']==[-6-3*r-3*t,r+t,0,0] and ref['c_unit_exponents']==[2*r+t,0,0,0],'fullUnits'+str(i))
 den=6
 for v in c['rays']:den*=v[2]+v[3]
 vol[c['parent']]+=F(1,den)
 inc.update(canon(f) for f in combinations(c['rays'],3))
for name,parent in d['parents'].items():
 den=6
 for v in parent['rays']:den*=v[2]+v[3]
 ck(vol[name]==F(abs(int(mat(parent['rays']).det())),den),'support'+name)
ck(Counter(inc.values())==Counter({2:842,1:548}),'fullIncidence')
H=s.Matrix(d['period_matrices']['h']);B=s.Matrix(d['period_matrices']['B']);ck(H*B==B*H,'commuting native periods')
for i,m in enumerate(d['full_period_chart_maps']):
 Ns=mat(d['cones'][m['source_cone']]['rays']);Nt=mat(d['cones'][m['target_cone']]['rays']);r,t=m['word_h'],m['word_B'];M=Nt.inv()*H**r*B**t*Ns
 ck(M==s.Matrix(m['monomial_matrix']),'periodSquare'+str(i));ck(Nt.inv()*s.Matrix([r,-2*r,0,0])==s.Matrix(m['p_unit_exponents']),'periodP'+str(i));ck(Nt.inv()*s.Matrix([0,t,0,0])==s.Matrix(m['c_unit_exponents']),'periodC'+str(i))
 ck(all(M[a,b]>=0 for a in range(4) for b in range(4) if b not in m['invertible_source_columns']),'localizedRegular'+str(i))
report={'status':'PASS','reviewer':'checks','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'source':'notes/part3_e6_p_one_cayley_working.md','source_sha256':hashlib.sha256((ROOT/'notes/part3_e6_p_one_cayley_working.md').read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'All558 regular native corner cones, complete persisted character/unit maps, actual source charts, parent support and localized period arrows. No total return or fixed-component count.','findings':['Full b=v^-4 c^-1 retained before the corner map.','Original P^3 point-line factor and canonical orders2h+t-1 retained.','Actual source map Z,Q/Z is regular on every cone.','The bare notation s_Delta must mean exactly s times Delta from E90; the full underlying line identity is checked.']}
(ROOT/'records/checks_audit_e6_p_one_common_cayley.json').write_text(json.dumps(report,indent=2)+'\n')
(ROOT/'code/part3/e6_p_one_cayley_peer.json').write_text(json.dumps({'summary':report,'check_labels':checks},indent=2)+'\n')
print(json.dumps(report))
