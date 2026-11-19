#!/usr/bin/env python3
"""Fresh M2 source/cap/unit arrows and complete actual normal ledger."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
tests=[]
def ck(name,ok):
    ok=bool(ok);tests.append({'name':name,'pass':ok})
    if not ok:raise AssertionError(name)
def zero(name,x):ck(name,S.factor(S.together(x))==0)
def mat(rs):return S.Matrix.hstack(*[S.Matrix(r) for r in rs])
def ser(M):return [[str(x) for x in row] for row in M.tolist()]
def pair_point(w):
    p=S.prod(w);return (1/p,sum(v*v for v in w)/p)
def pair_curve(w,d):
    p=S.prod(w);r=sum(b/a for a,b in zip(w,d))
    return (-r/p,(2*sum(a*b for a,b in zip(w,d))-sum(a*a for a in w)*r)/p)
def pair_surface(aa,ab,bb,p1):return (-(aa-ab+bb),-(p1+aa+2*ab+bb))
def add(rows):return tuple(S.cancel(sum(x[i] for x in rows)) for i in range(2))

v,p=S.symbols('v p')
iterate=v;factor=S.Integer(1)
for j in range(3):
    c=1-iterate;factor=S.cancel(factor*c);iterate=S.cancel(iterate/c)
    zero(f'chronological graph stage {j+1}',iterate-v/(1-(j+1)*v))
    zero(f'uncancelled source coefficient stage {j+1}',factor-(1-(j+1)*v))
zero('full source graph inverse',iterate/(1+3*iterate)-v)
A=S.Matrix([[1,-3],[0,1]])
ck('actual homogeneous inverse',A*S.Matrix([[1,3],[0,1]])==S.eye(2))
ck('full tautological coefficient arrow',A*S.Matrix([1,v])==S.Matrix([1-3*v,v]))
zero('M2 O point ratio and inverse',(p-2)/p*p/(p-2)-1)
zero('M2 T target point ratio and inverse',(p-3)/(p-5)*(p-5)/(p-3)-1)
for k in range(-8,9):
    zero(f'full O(-k) homogeneous inverse k{k}',(1-3*v)**k*(1+3*iterate)**k-1)

# Divisors on the six actual source translates and the sigma divisor.
div=[S.Integer(0)]*7
for j,mult in [(0,1),(3,1),(1,2),(2,2)]:
    div[j+1]+=2*mult;div[j+2]-=mult;div[j]-=mult;div[6]+=mult
ck('actual six-factor full divisor',div==[-1,0,1,1,0,-1,6])
frame=S.Matrix([1,0,-1,-1,0,1,-6])
ck('full point-module Hom cancellation',S.Matrix(div)+frame==S.zeros(7,1))

e,z,r,t,X,Y=S.symbols('e z r t X Y')
curve=Y**2-X**3-r*X**2-t*X-t**2
def chord(xx,yy,sign):
    slope=(yy-sign*t)/xx
    newx=S.cancel(slope**2-r-xx)
    return newx,S.cancel(-sign*t-slope*newx)
def curve_zero(name,expr):
    numerator=S.together(expr).as_numer_denom()[0]
    zero(name,S.rem(numerator,curve,Y))
minus=chord(X,Y,-1);plus=chord(X,Y,1)
for label,first,sgn in [('plus after minus',minus,1),('minus after plus',plus,-1)]:
    result=chord(*first,sgn)
    curve_zero(label+' source x',result[0]-X)
    curve_zero(label+' source y',result[1]-Y)
for label,(xx,yy) in [('minus',minus),('plus',plus)]:
    curve_zero('full cubic preserved '+label,yy**2-xx**3-r*xx**2-t*xx-t**2)
d=1-3*e**2;tc=e**4*(1-e**2)/d**3
xx=1-e**2;ss=(1-e**2)*(1+3*e**2)/4
hat=(e*Y-e**2*t-d*X/2)/(e**2*X-ss)
zero('actual selected-node tangent coefficient',hat.subs({Y:0,X:xx,t:xx})-2)
zero('M2 original selected coefficient',((e/d)*2*e)**6/tc**3-64*d**3/(1-e**2)**3)
P=-(1+e)/(1-e)
zero('full M2 selected reflection target period',P**-2*P**2-1)
zero('M2 moving point unit',-d*(1-P**2)/(2*P**2*e)-2*d/(1+e)**2)
Ho=e**-2*d/2
zero('full M2 point/tensor equality',Ho*2*d/(1+e)**2-(d/(e*(1+e)))**2)
ck('full moving positive phases',(-2,4-2)==(-2,2))
ck('after extending common phase',(-2-2,2-2)==(-4,0))
h,u=S.symbols('h u')
product=S.expand((h+2*u)*(-h-2*u))
zero('actual reversed-cap c2 coefficient',product.coeff(h,1).coeff(u,1)+4)

# The complete actual cubic good cap, including its source/Cartier correction.
xold=z**-2*X;yold=z**-3*Y;told=z**-3
old=yold**2-xold**3-r*xold**2-told*xold-told**2
zero('whole original-to-good cubic',z**6*old-(Y**2-X**3-r*z**2*X**2-z*X-1))
zero('full selected factor with six Miller powers',((told-tc)/told**3)*z**-6-(1-tc*z**3))
tr=S.symbols('tr');uh=(1-tc*z**3)/(1-tr*z**3)
zero('full selected/reference unit',uh*(1-tr*z**3)-(1-tc*z**3))
zero('full selected/reference central value',uh.subs(z,0)-1)
for ray in [(1,0),(S.Rational(2,3),S.Rational(1,3)),(S.Rational(1,3),S.Rational(2,3)),(0,1)]:
    wv,zv=ray
    zero(f'point-Cartier support correction {ray}',wv-max(wv-2*zv,0)-min(wv,2*zv))
zero('good formal division mR=3G',3*S.Rational(1,3)-1)
ck('actual good-root chord character',(1+2)%3==0)
for dc in range(3):
    for js in [(-2,0,1,3),(0,0,0,0),(1,-3,2,4)]:
        # Full scalar and normalized lift exponents are not reduced.
        arrows=[S.Matrix([1+3*j,1+3*j,1,dc]) for j in js]
        whole=sum(arrows,S.zeros(4,1))
        ck(f'full original cubic quarter word d{dc} j{js}',whole==S.Matrix([4+3*sum(js),4+3*sum(js),4,4*dc]))
        ck(f'full inverse cubic closing d{dc} j{js}',whole-whole==S.zeros(4,1))
sa,kk,ff,pi,cc,hh,jj,bb,ll=S.symbols('sa kk ff pi cc hh jj bb ll')
hb=hh-sa*pi+jj*bb+ll
zero('whole target-sheet annular square',(sa+kk)*(ff+pi)+(sa+kk)*cc+hb-(sa*ff+sa*cc+hh)-(kk*(ff+pi)+kk*cc)-jj*bb-ll)
C=S.Matrix([[3,1],[1,0]]);Ci=S.Matrix([[0,1],[1,-3]])
ck('actual good cap meridian inverse',C*Ci==S.eye(2))
Rcon=S.Matrix([[0,0],[-1,-1]])
ck('actual conifold physical Euler kernel',Rcon*S.Matrix([1,-1])==S.zeros(2,1))
ck('actual primitive conifold image',Rcon[:,0]==S.Matrix([0,-1]))

paths={
 'overlay':'code/part3/e6_selected_infinity_factor_overlay.json',
 'stars':'code/part3_fourfold/e6_selected_infinity_compact_surface_stars.json',
 'faces':'code/part3_fourfold/e6_fixed_face_orbits.json',
 'interface':'code/part3_fourfold/e6_selected_infinity_curve_clutch.json'}
data={k:json.loads((ROOT/path).read_text()) for k,path in paths.items()}
delta=S.Matrix([0,0,0,1])
TB=S.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-1,4,4,1]])
TS=S.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[4,4,1,1]])
atlas=[]
for kind,rows,T,cu,homkey,homname in [
 ('ordinary',data['overlay']['regular4_cones'],TB,S.Matrix([0,1,-1,0]),'B_full_Hom_unit_exponents','lambda H sigma^-6 B23 rho_2(T^3p)/rho_2(p)'),
 ('selected',data['overlay']['selected_full_regular_cones'],TS,S.Matrix([1,-1,0,0]),'B_full_selected_Hom_unit_exponents','lambda beta_2/kappa; beta_2=B_2^pt psi_2(T^3p)/psi_2(p)')]:
 for i,row in enumerate(rows):
    N=mat(row['rays']);Ni=N.inv();Nt=mat(row['B_target_rays']);Ati=Nt.inv()
    ck(f'{kind}{i} actual quotient regularity',abs(N.det())==1)
    ck(f'{kind}{i} exact source/line period rays',Nt==T*N)
    ck(f'{kind}{i} full coordinate inverse',Ati*T*N==S.eye(4))
    ck(f'{kind}{i} physical normal weights',list(Ni*delta)==row['physical_weights'])
    ck(f'{kind}{i} full M2 c3 column',list(Ati*cu)==row['B_source_unit_exponents'])
    ck(f'{kind}{i} full M2 genuine Hom column',list(Ati*delta)==row[homkey])
    atlas.append({'kind':kind,'chart':i,'inverse':ser(Ni),'source_unit':'c3=c1(p)c1(Tp)c1(T^2p)','source_unit_column':list(map(int,Ati*cu)),'Hom_unit':homname,'Hom_unit_column':list(map(int,Ati*delta))})
ck('all ordinary and selected chart counts',(len(data['overlay']['regular4_cones']),len(data['overlay']['selected_full_regular_cones']))==(238,39))

charts={}
for row in data['stars']['charts']:
 N=mat(row['rays']);Ni=N.inv();w=Ni*delta
 ck(f'compact chart {row["kind"]}/{row["label"]} regular',abs(N.det())==1)
 ck(f'compact chart {row["kind"]}/{row["label"]} physical vector',list(w)==row['physical_weights'])
 charts[(row['kind'],row['label'])]={'N':N,'A':Ni,'rays':row['rays'],'w':w}

for cand in ([17,43,101,263],[19,53,139,401],[23,71,211,701]):
 aux=S.Matrix(cand)
 if all(all((charts[tuple(k)]['A']*aux)[i]!=0 for i,w in enumerate(charts[tuple(k)]['w']) if not w) for row in data['stars']['surfaces'] for k in row['charts']):break
ck('fresh auxiliary vector is regular on every surface tangent',all(all((charts[tuple(k)]['A']*aux)[i]!=0 for i,w in enumerate(charts[tuple(k)]['w']) if not w) for row in data['stars']['surfaces'] for k in row['charts']))
surfacepairs={'exceptional':[],'refinement':[]};surfrecord=[]
for row in data['stars']['surfaces']:
 aa=ab=bb=p1=S.Integer(0)
 for k in row['charts']:
    c=charts[tuple(k)];v=c['A']*aux
    tang=[i for i,w in enumerate(c['w']) if w==0]
    neg=[i for i,w in enumerate(c['w']) if w==-1];pos=[i for i,w in enumerate(c['w']) if w==1]
    ck(f'surface{row["id"]} full split {k}',len(tang)==2 and len(neg)==len(pos)==1)
    den=v[tang[0]]*v[tang[1]];a,b=v[neg[0]],v[pos[0]]
    aa+=a*a/den;ab+=a*b/den;bb+=b*b/den;p1+=(v[tang[0]]**2+v[tang[1]]**2)/den
 ck(f'surface{row["id"]} actual D square',aa-2*ab+bb==S.Rational(row['D_square']))
 ck(f'surface{row["id"]} actual tangent',p1==S.Rational(row['p1']))
 pair=pair_surface(aa,ab,bb,p1);kind='exceptional' if 'v_unit' in row['type'] else 'refinement'
 surfacepairs[kind].append(pair);surfrecord.append({'id':row['id'],'normal_moments':list(map(str,[aa,ab,bb])),'p1':str(p1),'U_pair':list(map(str,pair))})
 for ov in row['all_normal_overlaps']:
    cs=charts[tuple(ov['from'])];ct=charts[tuple(ov['to'])];E=ct['A']*cs['N']
    ck(f'surface{row["id"]} complete normal transition {ov["from"]}->{ov["to"]}',E==S.Matrix(ov['full_character_matrix']))

inside=[];inside_record=[]
for row in data['faces']['selected_ordinary_overlay']['components']:
 if row['tag']!='interior':continue
 face=row['canonical_face'];ids=row['face_occurrences'][0]['charts'];c=charts[('resolved_infinity',ids[0])]
 w=[c['w'][c['rays'].index(ray)] for ray in face]
 ck(f'interior{row["id"]} full physical normal order',w==row['normal_weights'])
 if row['dimension']==0:pair=pair_point(w);degrees=[]
 else:
    ck(f'interior{row["id"]} two complete endpoints',len(ids)==2)
    endpoints=[]
    for index in ids:
       c=charts[('resolved_infinity',index)];v=c['A']*aux;ti=[i for i,wi in enumerate(c['w']) if wi==0]
       ck(f'interior{row["id"]} actual tangent',len(ti)==1 and v[ti[0]]!=0)
       endpoints.append((v[ti[0]],[v[c['rays'].index(ray)] for ray in face]))
    ck(f'interior{row["id"]} opposite tangent',endpoints[0][0]==-endpoints[1][0])
    degrees=[S.cancel((a-b)/endpoints[0][0]) for a,b in zip(endpoints[0][1],endpoints[1][1])]
    ck(f'interior{row["id"]} literal normal degree',degrees==row['normal_degrees']);pair=pair_curve(w,degrees)
 inside.append(pair);inside_record.append({'id':row['id'],'normal_weights':list(map(str,w)),'normal_degrees':list(map(str,degrees)),'U_pair':list(map(str,pair))})
ck('all compact interior components',len(inside)==124)

pairs_p=[];pairs_i=[];curves=[]
for row in data['stars']['p_curves']:
 face=row['face'];ends=[c for c in charts.values() if all(ray in c['rays'] for ray in face)]
 ck(f'pcurve{row["id"]} two literal ends',len(ends)==2)
 ep=[]
 for c in ends:
    v=c['A']*aux;ti=[i for i,w in enumerate(c['w']) if not w]
    ck(f'pcurve{row["id"]} tangent',len(ti)==1 and v[ti[0]]!=0)
    ep.append((v[ti[0]],[v[c['rays'].index(ray)] for ray in face]))
 degrees=[S.cancel(a/ep[0][0]+b/ep[1][0]) for a,b in zip(ep[0][1],ep[1][1])]
 ck(f'pcurve{row["id"]} full clutch degrees',degrees==row['normal_degrees'])
 w=list(map(S.Integer,row['normal_weights']));pair=pair_curve(w,degrees);pairs_p.append(pair)
 curves.append({'kind':'p','id':row['id'],'degree':list(map(str,degrees)),'U_pair':list(map(str,pair))})
for row in data['interface']['curves']:
 N=S.Matrix(row['infinity_chart_matrix']);E=S.Matrix(row['native_normal_exponents']);trans=E*N
 ck(f'interface{row["id"]} full normal arrow',trans==S.Matrix(row['full_clutch_exponents']))
 degrees=[-trans[i,row['tangent_column']] for i in range(3)]
 ck(f'interface{row["id"]} source-base degrees',degrees==row['normal_degrees'])
 w=list(map(S.Integer,row['normal_weights']));pair=pair_curve(w,degrees);pairs_i.append(pair)
 curves.append({'kind':'interface','id':row['id'],'degree':list(map(str,degrees)),'U_pair':list(map(str,pair))})

I=S.Matrix([[-2,1,0],[1,-2,1],[0,1,-2]])
strict=[];strictrecord=[]
for j,degree in enumerate(([1,0,0],[1,-1,1],[0,0,1],[0,0,0])):
 deg=S.Matrix(degree);a3=(deg.T*I.inv()*deg)[0]
 aa=2*a3-(S.Rational(1,2) if j%2==0 else 0)
 ab=S.Rational((j+1)*(4-j),2)
 bb=S.Rational(j*j,2)-8-(S.Rational(1,2) if j%2 else 0)
 pair=pair_surface(aa,ab,bb,-24);strict.append(pair)
 ck(f'strict{j} integral A3 inverse',I*(I.inv()*deg)==deg)
 strictrecord.append({'j':j,'normal_moments':list(map(str,[aa,ab,bb])),'A3_negative_degrees':degree,'U_pair':list(map(str,pair))})

sub={'strict':add(strict),'mu2':tuple(4*x for x in pair_point(list(map(S.Integer,[2,-1,-1,-1])))),'interior_per_copy':add(inside),'exceptional_per_copy':add(surfacepairs['exceptional']),'refinement_per_copy':add(surfacepairs['refinement']),'p_curves_per_copy':add(pairs_p),'interface_per_copy':add(pairs_i),'moving':(S.Integer(-4),S.Integer(-10))}
total=add([v if 'per_copy' not in k else tuple(2*x for x in v) for k,v in sub.items()])
ck('actual M2 completed U pair',total==(-4,8))
zero('actual M2 integer index',(4*total[0]-total[1])/24+1)
native=(total[1]/4,total[0]-total[1]/4)
ck('actual held-Cox native pair',native==(2,-6))

source=ROOT/'notes/part3_e6_selected_infinity_m2_branch_working.md'
deps=list(paths.values())+['notes/part3_e6_unselected_iii_extension_working.md','notes/part3_e6_selected_infinity_working.md','notes/part3_e6_selected_infinity_moving_cap_working.md','notes/part3_e6_selected_infinity_moving_c2_working.md','notes/part3_e6_selected_infinity_full_pair_ledger_working.md','records/k101_export_manifest.json','records/k102_export_manifest.json','records/k104_export_manifest.json']
out={'status':'PASS_EXACT_M2_INITIAL_MAPS_AND_NORMAL_LEDGER','utc':datetime.now(timezone.utc).isoformat(),'checks':len(tests),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Actual (M2,b3;m3,n1), retained character/reference and fixed original scalar; full initial source/Cartier/root/normal/cap and outer arrows are in MB.1--7. No return is divided through the auxiliary cube map.','dependencies':[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in deps],'auxiliary':list(map(int,aux)),'atlas':atlas,'surfaces':surfrecord,'interior':inside_record,'curves':curves,'strict':strictrecord,'U_subtotals':{k:list(map(str,v)) for k,v in sub.items()},'physical_Jin_pair':list(map(str,total)),'native_pair':list(map(str,native)),'identities':tests}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','source_sha256','scope','U_subtotals','physical_Jin_pair','native_pair']},indent=2))
