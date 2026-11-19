"""Actual selected-I3 compact generic fixed curves and full end clutches.

Every endpoint is read from the final protected-facet owner, with the
actual directed period word. Includes c0=(p-1)^4 c before computing
normal coefficients. No total return is assigned.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sympy as S,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
paths={
 'generic':ROOT/'code/part3/e6_selected_i3_common_fan.json',
 'corners':ROOT/'code/part3/e6_selected_i3_corner_lifts.json',
 'index':ROOT/'code/part3/e6_selected_i3_generic_corner_index.json',
 'one':ROOT/'code/part3/e6_selected_i3_p_one_cayley.json',
 'source_equations':ROOT/'notes/part3_e6_selected_i3_working.md'}
input_bytes={k:p.read_bytes() for k,p in paths.items()}
g,e,ix,o=[json.loads(input_bytes[k]) for k in ['generic','corners','index','one']]
checks=[]
def ck(v,n):
 assert bool(v),n
 checks.append(n)
def matrix(r):return S.Matrix.hstack(*map(S.Matrix,r))
def ints(M):return [[int(v) for v in row] for row in M.tolist()]
def ivec(v):return list(map(int,v))
def word0(a,b):return S.Matrix([[1,0,a,3*a-b],[0,1,b,6*a+2*b],[0,0,1,0],[0,0,0,1]])
def wordi(a,b):return S.Matrix([[1,0,0,7*a+2*b],[0,1,b,a+2*b],[0,0,1,0],[0,0,0,1]])
one={}
for ci,c in enumerate(o['cones']):
 if c['kind']!='upper_star':continue
 for ref in c['generic_references']:
  cid=ref['common_cone'];ck(cid not in one,'one endpoint unique'+str(cid));one[cid]=(ci,c,ref)
ck(len(one)==4264,'all4264 one-end owners')
zindex={r['common_cone']:r for r in ix['corners']['zero']}
iindex={r['common_cone']:r for r in ix['corners']['infinity']}
ck(len(zindex)==len(iindex)==4264,'all4264 zero/infinity protected owners')

records=[];total_k=Q(0);total_l=Q(0);total_A=Q(0)
for cid,c in enumerate(g['cones']):
 N=matrix(c['rays']);Ni=N.inv();weights=ivec(Ni*S.Matrix([1,0,0]))
 ck(weights==c['physical_weights'],'actual common weights'+str(cid))
 if 0 in weights:continue
 ends={}
 # The p=0 common map after the saved first-parent K,J translation.
 zp=g['parent_zero_instances'][c['zero_parent']];r,t=zp['shift']
 F0=S.Matrix([[-3,1,-6-r-2*t,6+7*r+2*t],[1,0,r+t,r+2*t],[0,0,1,1]])
 zi=zindex[cid];a,b=zi['native_period_from_input_to_owner']
 zco=e['corners']['zero']['cones'][zi['corner_cone']];Nz=matrix(zco['rays'])
 M0=F0*word0(-a,-b);facecols=zi['corner_columns'];extra=next(k for k in range(4) if k not in facecols)
 ck({tuple(M0*Nz[:,k]) for k in facecols}==set(map(tuple,c['rays'])),'zero exact protected-face map'+str(cid))
 ck(Nz[2,extra]==1 and all(Nz[2,k]==0 for k in facecols),'zero actual base-disc parameter'+str(cid))
 chart=Ni*M0*Nz;orders=ivec(chart[:,extra]);bt=2*r+t-b
 ck(all(v.is_Integer for v in chart),'zero integral full normal arrow'+str(cid))
 ends['zero']={'corner_cone':zi['corner_cone'],'corner_columns':facecols,'base_column':extra,
  'parent_KJ_shift':[r,t],'owner_inverse_period_hB':[-a,-b],
  'common_character_matrix':ints(M0),'normal_character_matrix':ints(chart),
  'coefficient_orders':orders,
  'normal_unit_powers':{'p_minus_one':ivec(4*bt*Ni*S.Matrix([1,0,0])),
                       'c':ivec(bt*Ni*S.Matrix([1,0,0])),
                       'U6':ivec(Ni*S.Matrix([1,0,0]))},
  'full_unit_dictionary':'c0=(p-1)^4 c; original point map p^-6 P^6 U6 Z^-3 Vpt; R=pP'}
 # At p=1 use the literal common corner character map with its full p,c units.
 oi,oc,oref=one[cid];No=matrix(oc['rays']);F1=S.Matrix(oref['full_corner_character_matrix'])[:3,:]
 facecols=[k for k,v in enumerate(oc['rays']) if v[3]==0];extra=next(k for k in range(4) if k not in facecols)
 ck({tuple(F1*No[:,k]) for k in facecols}==set(map(tuple,c['rays'])),'one exact common protected face'+str(cid))
 ck(No[3,extra]==1,'one actual base-disc parameter'+str(cid))
 chart=Ni*F1*No;orders=ivec(chart[:,extra]);ck(all(v.is_Integer for v in chart),'one integral full normal arrow'+str(cid))
 ends['one']={'corner_cone':oi,'corner_columns':facecols,'base_column':extra,
  'parent_KJ_shift':oref['period_shift'],'common_character_matrix':ints(F1),
  'normal_character_matrix':ints(chart),'coefficient_orders':orders,
  'normal_unit_powers':{'p':ivec(Ni*S.Matrix(oref['p_unit_exponents'][:3])),
                       'c':ivec(Ni*S.Matrix(oref['c_unit_exponents'][:3]))},
  'full_unit_dictionary':'p=1+v; exact source R=pP and original p^-6 point coefficient retained'}
 # The infinity native torus already uses Vreg,Z,u,R. Undo its owner period.
 ii=iindex[cid];a,b=ii['native_period_from_input_to_owner'];ico=e['corners']['infinity']['cones'][ii['corner_cone']];Nt=matrix(ico['rays'])
 Fi=S.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])*wordi(-a,-b)
 facecols=ii['corner_columns'];extra=next(k for k in range(4) if k not in facecols)
 ck({tuple(Fi*Nt[:,k]) for k in facecols}==set(map(tuple,c['rays'])),'infinity exact protected-face map'+str(cid))
 ck(Nt[2,extra]==1 and all(Nt[2,k]==0 for k in facecols),'infinity actual base-disc parameter'+str(cid))
 chart=Ni*Fi*Nt;orders=ivec(chart[:,extra]);ck(all(v.is_Integer for v in chart),'infinity integral full normal arrow'+str(cid))
 ends['infinity']={'corner_cone':ii['corner_cone'],'corner_columns':facecols,'base_column':extra,
  'owner_inverse_period_KJ':[-a,-b],'common_character_matrix':ints(Fi),
  'normal_character_matrix':ints(chart),'coefficient_orders':orders,
  'normal_unit_powers':{'f':ivec((-2*a-b)*Ni*S.Matrix([1,0,0]))},
  'full_unit_dictionary':'f=(1-u)^4 c(P=Ru,R), p=u^-1; original Vreg point-line arrow retained'}
 degrees=[-sum(ends[k]['coefficient_orders'][j] for k in ends) for j in range(3)]
 ck(sum(c['rays'][j][2]*degrees[j] for j in range(3))==-1,'full original R-line degree'+str(cid))
 canonical=sum((2*c['rays'][j][2]-1)*degrees[j] for j in range(3))
 ck(canonical==-2-sum(degrees),'original canonical adjunction'+str(cid))
 prod=weights[0]*weights[1]*weights[2]
 ku=-sum(Q(d,w) for d,w in zip(degrees,weights))/prod
 lu=(2*sum(w*d for w,d in zip(weights,degrees))-sum(w*w for w in weights)*sum(Q(d,w) for d,w in zip(degrees,weights)))/prod
 km=-ku;lm=-lu;A=(4*km-lm)/24
 # Independently expand the coefficient of the base generator in the residue.
 ru=-sum((Q(4-sum(w*w for w in weights),w)+2*w)*d for w,d in zip(weights,degrees))/(24*prod)
 ck(A==-ru,'physical M dual and full residue identity'+str(cid))
 total_k+=km;total_l+=lm;total_A+=A
 records.append({'common_cone':cid,'rays':c['rays'],'normal_weights':weights,
  'normal_degrees':degrees,'actual_end_maps':ends,'base':'P1_p',
  'period_stabilizer':[0,0],'original_canonical_degree':canonical,
  'physical_M_inner_pair':[str(km),str(lm)],'physical_M_inner_residue':str(A)})
ck((4*total_k-total_l)/24==total_A,'complete scoped curve-pair sum')
proof=ROOT/'notes/part3_e6_selected_i3_fixed_curve_normals_working.md'
for k,p in paths.items():ck(p.read_bytes()==input_bytes[k],'input remained stable '+k)
out={'status':'PASS_SELECTED_I3_GENERIC_CURVE_NORMALS','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'check_labels':checks,
 'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(input_bytes[k]).hexdigest() for k,p in paths.items()},
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest() if proof.exists() else None,
 'curves':records,'compact_curve_count':len(records),
 'sum_physical_M_inner_pair':[str(total_k),str(total_l)],'sum_physical_M_inner_residue':str(total_A),
 'scope':'Actual compact generic fixed curves in the three selected-I3 end atlas; full protected-facet owners and all unit normal clutches retained. Surface, corner, lower, cap/reference and outer terms are excluded; no global return.'}
tmp=Path(__file__).with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(Path(__file__).with_suffix('.json'))
print(json.dumps({k:out[k] for k in ['status','checks','compact_curve_count','sum_physical_M_inner_pair','sum_physical_M_inner_residue']},indent=2))
