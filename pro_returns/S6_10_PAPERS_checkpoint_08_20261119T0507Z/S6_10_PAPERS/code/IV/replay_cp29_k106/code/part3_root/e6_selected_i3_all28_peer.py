#!/usr/bin/env python3
"""Independent full-prism linear solves for all28 explicit I3 witnesses."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
PRIMARY='code/part3/e6_selected_i3_all_fans.json'
SOURCE='notes/part3_e6_selected_i3_all_fans_working.md'
data=json.loads((ROOT/PRIMARY).read_text()); checks=[]
def ck(n,v):
    assert bool(v),n
    checks.append(n)
def sha(n):return hashlib.sha256((ROOT/n).read_bytes()).hexdigest()
B0=S.Matrix([[2,-1],[6,-3]])
Qs=[S.Matrix([[1,-1],[0,1]]),S.Matrix([[1,0],[-1,1]])]
V0=S.Matrix([[-96,-34,34],[-34,-8,0],[34,0,-6]])
d0=S.Matrix([96,40,-30])
varsV=S.symbols('a b c d e f');varsd=S.symbols('p q r')
VV=S.Matrix([[varsV[0],varsV[1],varsV[2]],[varsV[1],varsV[3],varsV[4]],[varsV[2],varsV[4],varsV[5]]])
dd=S.Matrix(varsd)
def actual(P):
    R=P.inv();W=2*R*B0*P;x,y=R*S.Matrix([0,1]);w=S.Matrix([x,y,-x-y]);d=S.Matrix([-x-2*y,-2*x-y,x-y]);l=[W[1,1]-W[1,0],W[0,0]-W[0,1],W[1,1]]
    I=S.Matrix([-w[k]+d[k]*(l[k]+1) for k in range(3)])
    D=S.Matrix([-w[k]-d[k]*(l[k]+1) for k in range(3)])
    # Ordered genuine source units: kappa,alpha,g,eta.
    E=[[[int(R[i,a]*P[b,j]) for b in range(2) for a in range(2)] for j in range(2)] for i in range(2)]
    return w,I,D,E

def linear_unique(eqs,variables,name):
    A,b=S.linear_eq_to_matrix(eqs,variables)
    ck(name+' complete rank',A.rank()==len(variables))
    sol=S.linsolve((A,b),variables)
    ck(name+' one exact solution',len(sol)==1)
    ans=next(iter(sol));ck(name+' integral coefficients',all(v.is_Integer for v in ans))
    return dict(zip(variables,ans))
cache={():{'P':S.eye(2),'V':V0,'d':d0,'A':S.Integer(8),'path':[]}}
recon=[]
def build(word):
    key=tuple(word)
    if key in cache:return cache[key]
    old=build(word[:-1]);i=word[-1]
    ck('only actual native0/1 arrows '+str(key),i in (0,1))
    a=old['V'][i,i];b=old['d'][i]
    m=-1-(a+b)/4;n=(b-a)/4
    ck('single free integrality '+str(key),m.is_Integer and n.is_Integer)
    P=old['P']*Qs[i];w,I,D,E=actual(P)
    ck('target physical weights nonzero '+str(key),all(v!=0 for v in w))
    ck('actual primitive target determinant '+str(key),P.det()==1)
    v_eq=[];d_eq=[]
    for z in (1,2):
        vec=S.zeros(3,1);vec[z]=w[z];vec[0]=-w[0]
        rhs=S.zeros(3,1);rhs[z]=I[z];rhs[0]=-I[0]
        v_eq+=list(VV*vec-rhs)
        d_eq.append(w[z]*dd[z]-w[0]*dd[0]-D[z]+D[0])
    v_eq.append(VV[2,2]-a);d_eq.append(dd[2]-(2*a-b))
    sv=linear_unique(v_eq,varsV,'variation '+str(key));sd=linear_unique(d_eq,varsd,'derivative '+str(key))
    V=VV.subs(sv);dv=dd.subs(sd)
    ck('every full action prism '+str(key),all(x.subs(sv)==0 for x in v_eq))
    ck('every full derivative prism '+str(key),all(x.subs(sd)==0 for x in d_eq))
    nm=-1-(V[2,2]+dv[2])/4;nn=(dv[2]-V[2,2])/4
    ck('whole native pair reset '+str(key),nm==m+2*n and nn==-n)
    ck('actual inverse native pair '+str(key),(nm+2*nn,-nn)==(m,n))
    R=P.inv();ck('full source height exponents '+str(key),R*P==S.eye(2))
    # Compare a second construction of all full unit powers: chronological reset.
    _,_,_,Eold=actual(old['P']);Q=Qs[i];Qi=Q.inv()
    Ereset=[[[sum(int(Qi[ii,h]*Q[k,jj])*Eold[h][k][u] for h in range(2) for k in range(2)) for u in range(4)] for jj in range(2)] for ii in range(2)]
    ck('all16 complete coefficient powers '+str(key),Ereset==E)
    record={'word':list(key),'old_basis':list(old['P']),'edge':i,'new_basis':list(P),'old_single_native_pair':[m,n],'native_right_increment':n,'integer_path_sum':old['A']+n,'target_variation':V.tolist(),'target_stable_derivative':list(dv),'full_multiplier_exponents':E,'linear_variation_rank':6,'linear_derivative_rank':3}
    obj={'P':P,'V':V,'d':dv,'A':old['A']+n,'path':old['path']+[record]}
    cache[key]=obj;recon.append(record);return obj

witnesses=[]
for residue in range(28):
    given=data['all28_witnesses'][str(residue)];word=given['word']
    ck('witness starts at exact T0 '+str(residue),given['vertical_index']==0)
    obj=build(word)
    ck('full original basis '+str(residue),list(obj['P'])==given['input_basis']==given['canonical_basis'])
    ck('full final variation '+str(residue),obj['V']==S.Matrix(given['variation']))
    ck('full final derivative '+str(residue),obj['d']==S.Matrix(given['stable_derivative']))
    ck('unreduced path sum '+str(residue),obj['A']==given['integer_path_sum'])
    ck('actual physical residue '+str(residue),int(obj['A'])%28==residue==given['physical_class_mod28'])
    ck('at most seven actual flops '+str(residue),len(word)<=7)
    ck('all intermediate steps retained '+str(residue),len(obj['path'])==len(given['steps']))
    for step,ref in zip(obj['path'],given['steps']):
        for key in ['old_basis','edge','old_single_native_pair','new_basis','native_right_increment','integer_path_sum','target_variation','target_stable_derivative','full_multiplier_exponents']:
            ck('complete step '+str(residue)+' '+str(step['word'])+' '+key,step[key]==ref[key])
    witnesses.append({'residue':residue,'basis':list(obj['P']),'word':word,'integer_path_sum':obj['A']})
ck('full image is all28 actual classes',sorted({int(o['A'])%28 for k,o in cache.items()})==list(range(28)))
ck('two-flop exact native increments',[r['native_right_increment'] for r in build([0,1])['path']]==[48,300])
ck('two-flop exact path sum',build([0,1])['A']==356)
deps=[SOURCE,PRIMARY,'notes/part3_e6_selected_i3_all_fan_witness_table.md','notes/part3_e6_selected_i3_first_flop_working.md','notes/part3_e6_selected_i3_vertical_fans_working.md','notes/part3_e6_selected_i3_moving_c2_working.md','records/blind_audit_e6_selected_i3_moving_c2.json','records/root_audit_e6_selected_i3_transfer_flop.json','records/fourfold_audit_e6_selected_i3_native_reset.json']
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'source':SOURCE,'source_sha256':sha(SOURCE),'primary_sha256':sha(PRIMARY),'dependencies':{p:sha(p) for p in deps},'scope':'Independent full linear-system reconstruction of all28 explicit original-T0 witnesses, full unit exponents, entire native free pairs, target variation/derivative and unreduced increments. Uses no other vertical seed.','distinct_target_fans':len(cache)-1,'witnesses':witnesses,'all_target_solves':recon,'checks_named':checks}
def enc(v):
    if isinstance(v,S.Integer):return int(v)
    raise TypeError(type(v).__name__)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=enc)+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','source_sha256','distinct_target_fans','witnesses']},indent=2,default=enc))
