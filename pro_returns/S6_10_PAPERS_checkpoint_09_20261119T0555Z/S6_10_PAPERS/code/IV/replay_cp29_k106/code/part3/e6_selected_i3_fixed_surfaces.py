"""Full421 compact surface normal bundles plus interior corner strata.

All three endpoint arrows are reconstructed from their actual character
maps and full unit factors. No global return is inferred from this ledger.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
paths={k:ROOT/v for k,v in {'generic':'code/part3/e6_selected_i3_common_fan.json','corners':'code/part3/e6_selected_i3_corner_lifts.json','one':'code/part3/e6_selected_i3_p_one_cayley.json','index':'code/part3/e6_selected_i3_generic_corner_index.json','faces':'code/part3/e6_selected_i3_fixed_faces.json','curves':'code/part3/e6_selected_i3_fixed_curve_normals.json'}.items()}
D={k:json.loads(p.read_text()) for k,p in paths.items()};g=D['generic']['cones'];at=D['faces']['atlases'];corners={'zero':D['corners']['corners']['zero']['cones'],'one':D['one']['cones'],'infinity':D['corners']['corners']['infinity']['cones']};checks=[]
def ck(n,t):
 assert t,n
 checks.append(n)
def mat(C):return S.Matrix(list(zip(*C)))
def vi(v):
 ck('integral arrow coefficients',all(x.q==1 for x in v));return list(map(int,v))
def mi(M):return [[int(v) for v in row] for row in M.tolist()]
def T0(a,b):return S.Matrix([[1,0,a,3*a-b],[0,1,b,6*a+2*b],[0,0,1,0],[0,0,0,1]])
def Ti(a,b):return S.Matrix([[1,0,0,7*a+2*b],[0,1,b,a+2*b],[0,0,1,0],[0,0,0,1]])
ix={k:{r['common_cone']:r for r in D['index']['corners'][k]} for k in ['zero','infinity']}
one={}
for j,c in enumerate(corners['one']):
 if c['kind']=='upper_star':
  for ref in c['generic_references']:
   ck('unique p1 owner',ref['common_cone'] not in one);one[ref['common_cone']]=(j,ref)
oldcurves={r['common_cone']:r for r in D['curves']['curves']};sections={}
for cid,co in enumerate(g):
 N=mat(co['rays']);A=N.inv();ends={}
 zr=ix['zero'][cid];zpar=D['generic']['parent_zero_instances'][co['zero_parent']];r,s=zpar['shift'];a,b=zr['native_period_from_input_to_owner']
 base=S.Matrix([[-3,1,-6,6],[1,0,0,0],[0,0,1,1],[0,0,1,0]])
 common_period=S.Matrix([[1,0,7*r+2*s,-4*(2*r+s)],[0,1,r+2*s,-s],[0,0,1,0],[0,0,0,1]])
 Zmap=(common_period*base*T0(-a,-b))[:3,:]
 extras=2*r+s-b
 loc=[('zero',zr['corner_cone'],Zmap,zr['corner_columns'],{'p_minus_1':S.Matrix([4*extras,0,0]),'c':S.Matrix([extras,0,0]),'U6':S.Matrix([1,0,0])})]
 oi,oref=one[cid];r,s=oref['period_shift']
 obase=S.Matrix([[-1,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
 oper=S.Matrix([[1,0,7*r+2*s,8*r+4*s],[0,1,r+2*s,0],[0,0,1,0],[0,0,0,1]])
 Omap=(oper*obase)[:3,:];oc=corners['one'][oi];cols=[j for j,v in enumerate(oc['rays']) if v[3]==0]
 ck('actual independent p1 full matrix',mi(Omap)==oref['full_corner_character_matrix'][:3])
 loc.append(('one',oi,Omap,cols,{'p':S.Matrix([-6-r-2*s,r+s,1]),'c':S.Matrix([2*r+s,0,0])}))
 ir=ix['infinity'][cid];a,b=ir['native_period_from_input_to_owner'];Imap=S.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])*Ti(-a,-b)
 loc.append(('infinity',ir['corner_cone'],Imap,ir['corner_columns'],{'f':S.Matrix([-2*a-b,0,0])}))
 for name,owner,L,cols,units in loc:
  Ne=mat(corners[name][owner]['rays']);j=next(k for k in range(4) if k not in cols);normal=A*L*Ne
  ck(name+' actual full protected-face identity '+str(cid),{tuple(L*Ne[:,k]) for k in cols}==set(map(tuple,co['rays'])))
  ck(name+' actual base coordinate order one '+str(cid),Ne[3 if name=='one' else 2,j]==1)
  orders=vi(normal[:,j]);powers={k:vi(A*u) for k,u in units.items()}
  ends[name]={'corner_cone':owner,'base_column':j,'corner_columns':cols,'owner_to_common_matrix':mi(L),'full_normal_matrix':mi(normal),'orders':orders,'normal_unit_exponents':powers}
 deg=[-sum(rec['orders'][j] for rec in ends.values()) for j in range(3)]
 ck('full original source/canonical adjunction '+str(cid),sum(co['rays'][j][2]*deg[j] for j in range(3))==-1)
 if cid in oldcurves:
  ck('independent curve degree agreement '+str(cid),deg==oldcurves[cid]['normal_degrees'])
  for name in ends:ck('independent full curve unit agreement '+str((cid,name)),ends[name]['normal_unit_exponents']=={('p_minus_1' if k=='p_minus_one' else k):v for k,v in oldcurves[cid]['actual_end_maps'][name]['normal_unit_powers'].items()})
 sections[cid]={'degrees':deg,'ends':ends}
matches={name:{r['common_component']:r['component'] for r in at[name]['generic_component_identifications']} for name in corners}
records=[];pair=[F(0),F(0)];nblow=0
for comp in at['generic']['components']:
 if comp['dimension']!=2:continue
 normal=[tuple(v) for _,v in sorted(zip(comp['normal_weights'],comp['canonical_face']))];weights=sorted(comp['normal_weights']);local=[]
 ck('opposite actual physical weights',weights[0]<0<weights[1] and not comp['period_stabilizer_basis'])
 for occ in comp['occurrences']:
  C=list(map(tuple,occ['canonical_four_or_three_rays']));N=mat(C);ni=[C.index(v) for v in normal];ti=next(i for i in range(3) if i not in ni);sr=sections[occ['cone']]
  local.append({'common_cone':occ['cone'],'normal_indices':ni,'tangent_index':ti,'transverse':C[ti],'self':sr['degrees'][ti],'normal_degrees':[sr['degrees'][i] for i in ni],'full_section_map':sr})
 ck('two complete generic fibre charts',len(local)==2)
 W=mat(normal+[local[0]['transverse']]);rel=-W.inv()*(S.Matrix(local[0]['transverse'])+S.Matrix(local[1]['transverse']))
 ck('actual opposite primitive fibre rays',rel[2]==0)
 fibre=vi(rel[:2]);stars={};exceptional=None
 for name in corners:
  ec=at[name]['components'][matches[name][comp['id']]];nr=[tuple(v) for _,v in sorted(zip(ec['normal_weights'],ec['canonical_face']))]
  ck(name+' actual end eigenline matching',sorted(ec['normal_weights'])==weights and not ec['period_stabilizer_basis'])
  star=[]
  for occ in ec['occurrences']:
   C=list(map(tuple,occ['canonical_four_or_three_rays']));ni=[C.index(v) for v in nr];ti=[i for i in range(4) if i not in ni]
   star.append({'cone':occ['cone'],'C':C,'normal_indices':ni,'tangent_indices':ti,'tangent_rays':[C[i] for i in ti],'period_word':occ['period_from_canonical'],'normal_period_unit_exponents':occ['normal_period_unit_exponents']})
  base=mat(nr+star[0]['tangent_rays']);ck(name+' saturated actual surface lattice',abs(base.det())==1);bi=base.inv();qr={}
  for ch in star:
   vv=[]
   for ray in ch['tangent_rays']:
    q=bi*S.Matrix(ray);v=tuple(vi(q[2:]));qr[ray]=v;vv.append(v)
   ck(name+' regular surface cone',abs(mat(vv).det())==1)
  bp=3 if name=='one' else 2
  boundary=[r for r in qr if r[bp]==0];interior=[r for r in qr if r[bp]>0]
  ck(name+' actual boundary two opposite rays',len(boundary)==2 and S.Matrix(qr[boundary[0]])+S.Matrix(qr[boundary[1]])==S.zeros(2,1))
  ck(name+' base multiplicities one',all(r[bp]==1 for r in interior))
  ck(name+' two or three complete surface charts',len(star) in [2,3])
  if len(star)==2:ck(name+' one middle fibre ray',len(interior)==1)
  else:
   ck('only infinity extra corner',name=='infinity' and exceptional is None and len(interior)==2)
   er=sorted(interior)[0];other=next(r for r in interior if r!=er);diff=S.Matrix(qr[er])-S.Matrix(qr[other])
   ck('literal blowup ray sum',tuple(diff) in [tuple(qr[r]) for r in boundary])
   ecorners=[ch for ch in star if er in ch['tangent_rays']];far=[next(r for r in ch['tangent_rays'] if r!=er) for ch in ecorners]
   ck('two exceptional curve charts',len(ecorners)==2)
   relation=-mat(nr+[er,far[0]]).inv()*(S.Matrix(far[0])+S.Matrix(far[1]))
   ck('literal exceptional normal and tangent wall',relation[3]==0 and relation[2]==-1)
   inc=[]
   for sec in local:
    owner=sections[sec['common_cone']]['ends'][name]['corner_cone'];ch=next(ch for ch in star if ch['cone']==owner);inc.append(int(er in ch['tangent_rays']))
   ck('actual two sections meet opposite fibre components',sum(inc)==1)
   exceptional={'end':name,'ray':er,'quotient_ray':qr[er],'old_quotient_ray':qr[other],'difference':vi(diff),'normal_degrees':vi(relation[:2]),'section_incidence':inc,'wall_relation':vi(relation),'charts':[c['cone'] for c in ecorners]}
  stars[name]={'component':ec['id'],'normal_rays':nr,'charts':star,'surface_quotient_rays':[{'native':r,'quotient':v} for r,v in qr.items()]}
 b=int(exceptional is not None);nblow+=b;selfs=[r['self'] for r in local];normal_sections=[r['normal_degrees'] for r in local]
 ck('complete section self degrees',sum(selfs)==-b)
 if b:
  inc=exceptional['section_incidence'];ed=exceptional['normal_degrees'];I=S.Matrix([[selfs[0],1,inc[0]],[1,0,0],[inc[0],0,-1]])
  classes=[I.inv()*S.Matrix([normal_sections[0][j],fibre[j],ed[j]]) for j in range(2)];sec1=I.inv()*S.Matrix([0,1,inc[1]]);K=I.inv()*S.Matrix([-2-selfs[0],-2,-1])
 else:
  I=S.Matrix([[selfs[0],1],[1,0]]);classes=[I.inv()*S.Matrix([normal_sections[0][j],fibre[j]]) for j in range(2)];sec1=I.inv()*S.Matrix([0,1]);K=I.inv()*S.Matrix([-2-selfs[0],-2])
 ck('integral unimodular surface lattice',abs(I.det())==1 and all(x.q==1 for q in classes for x in q))
 ck('independent opposite section self',(sec1.T*I*sec1)[0]==selfs[1])
 for j in range(2):ck('independent opposite normal degree',(classes[j].T*I*sec1)[0]==normal_sections[1][j])
 ints=[F((classes[0].T*I*classes[0])[0]),F((classes[0].T*I*classes[1])[0]),F((classes[1].T*I*classes[1])[0])]
 K2=int((K.T*I*K)[0]);ck('actual canonical square',K2==8-b);p1=K2-2*(4+b);ck('actual tangent p1',p1==-3*b)
 w1,w2=weights;x,y,z=ints;B=x/F(w1*w1)+y/F(w1*w2)+z/F(w2*w2);prod=w1*w2;ku=B/prod;lu=(p1-x-z-2*(F(w1,w2)+F(w2,w1))*y+(w1*w1+w2*w2)*B)/prod
 pair[0]-=ku;pair[1]-=lu
 records.append({'common_component':comp['id'],'normal_rays':normal,'physical_normal_weights':weights,'generic_sections':local,'fibre_normal_degrees':fibre,'section_self_intersections':selfs,'normal_section_degrees':normal_sections,'end_stars':stars,'exceptional':exceptional,'intersection_matrix':mi(I),'normal_Chern_vectors':[vi(v) for v in classes],'normal_intersections':list(map(str,ints)),'canonical_square':K2,'Euler':4+b,'p1':p1,'positive_U_pair':[str(ku),str(lu)],'physical_M_inner_pair':[str(-ku),str(-lu)]})
ck('all421 actual surfaces',len(records)==421);ck('twelve actual infinity blowups',nblow==12)
corner_ledger={}
for name in ['zero','infinity']:
 subtotal=[F(0),F(0)];rows=[]
 for co in at[name]['components']:
  if co['tag']!='interior':continue
  if co['dimension']==0:
   km,lm=map(F,co['physical_M_pair']);subtotal[0]+=km;subtotal[1]+=lm;rows.append({'component':co['id'],'dimension':0,'normal_weights':co['normal_weights'],'physical_M_pair':[str(km),str(lm)]});continue
  ck(name+' interior remaining stratum is curve',co['dimension']==1 and len(co['occurrences'])==2 and not co['period_stabilizer_basis'])
  normals=list(map(tuple,co['canonical_face']));weights=co['normal_weights'];answers=[];auxdata=[]
  for aux in [[1,11,103,1009],[2,17,89,701]]:
   deg=[F(0) for _ in normals];tw=[];vertices=[]
   for occ in co['occurrences']:
    C=list(map(tuple,occ['canonical_four_or_three_rays']));A=mat(C).inv();av=A*S.Matrix(aux);ti=occ['tangent_columns'];ck('actual curve one tangent',len(ti)==1 and av[ti[0]]!=0);k=int(av[ti[0]]);tw.append(k);mn=[]
    for j,nr in enumerate(normals):m=int(av[C.index(nr)]);deg[j]+=F(m,k);mn.append(m)
    vertices.append({'cone':occ['cone'],'tangent_weight':k,'normal_aux_weights':mn,'canonical_rays':C,'actual_period_word':occ['period_from_canonical'],'full_normal_period_units':occ['normal_period_unit_exponents']})
   ck('complete two-point curve weights',tw[0]==-tw[1]);ck('integral actual curve normal degrees',all(x.denominator==1 for x in deg));answers.append(deg);auxdata.append({'aux':aux,'vertices':vertices})
  ck('two independent auxiliary normal computations',answers[0]==answers[1]);degs=list(map(int,answers[0]));prod=1
  for w in weights:prod*=w
  sd=sum(F(d,w) for d,w in zip(degs,weights));ku=-sd/prod;lu=(2*sum(w*d for w,d in zip(weights,degs))-sum(w*w for w in weights)*sd)/prod
  km,lm=-ku,-lu;subtotal[0]+=km;subtotal[1]+=lm;rows.append({'component':co['id'],'dimension':1,'normal_weights':weights,'normal_degrees':degs,'full_auxiliary_checks':auxdata,'physical_M_pair':[str(km),str(lm)]})
 corner_ledger[name]={'rows':rows,'summary':dict(Counter(r['dimension'] for r in rows)),'physical_M_pair':list(map(str,subtotal)),'physical_M_residue':str((4*subtotal[0]-subtotal[1])/24)}
out={'status':'PASS','checks':len(checks),'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths.values()},'surfaces':records,'surface_count':421,'actual_surface_blowups':12,'surface_physical_M_pair':list(map(str,pair)),'surface_physical_M_residue':str((4*pair[0]-pair[1])/24),'interior_corner_ledger':corner_ledger,'scope':'Actual421 compact generic surfaces and126 interior points/four interior curves of the executed selected-I3 atlas, with full normal maps and source/point-line factors. Four lower surfaces, selected moving cap, exterior reference and total return remain unassigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','surface_count','actual_surface_blowups','surface_physical_M_pair','surface_physical_M_residue']},indent=2))
print('CORNERS',json.dumps({k:{a:b for a,b in v.items() if a!='rows'} for k,v in corner_ledger.items()},indent=2))
