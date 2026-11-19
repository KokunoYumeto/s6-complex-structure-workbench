#!/usr/bin/env python3
"""Actual selected-I3 p=infinity period fan, original integer lattice."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import sympy as S
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,test):
    assert test,name
    checks.append(name)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def area2(t):return cross(sub(t[1],t[0]),sub(t[2],t[0]))
def orient(t):return t if area2(t)>0 else (t[0],t[2],t[1])
poly=[(0,0),(-5,0),(-7,-1),(-7,-2),(-2,-2),(0,-1)]
def inside(p):return all(cross(sub(b,a),sub(p,a))>=0 for a,b in zip(poly,poly[1:]+poly[:1]))
points=[(x,y) for x in range(-7,1) for y in range(-2,1) if inside((x,y))]
tri=[tuple((poly[0],poly[i],poly[i+1])) for i in range(1,len(poly)-1)]
for p in points:
    new=[]
    for t in tri:
        if p in t or not all(cross(sub(b,a),sub(p,a))>=0 for a,b in zip(t,t[1:]+t[:1])):
            new.append(t);continue
        for a,b in zip(t,t[1:]+t[:1]):
            q=(a,b,p)
            if area2(q):new.append(orient(q))
    tri=new
ck('24 primitive upper triangles',len(tri)==24 and all(area2(t)==1 for t in tri))
ck('upper area12',sum(F(area2(t),2) for t in tri)==12)
A=(0,0,0,1);B=(0,-1,0,1)
raw=[{'rays':[A]+[(x,y,1,0) for x,y in t],'parent':'upper','parent_index':i} for i,t in enumerate(tri)]
raw += [{'rays':[A,B,(j,-2,1,0),(j+1,-2,1,0)],'parent':'lower_horizontal','parent_index':j} for j in range(-7,-2)]
raw.append({'rays':[A,B,(-2,-2,1,0),(0,-1,1,0)],'parent':'lower_diagonal','parent_index':0})
def matrix(rs):return S.Matrix.hstack(*map(S.Matrix,rs))
def key(rs):return tuple(sorted(map(tuple,rs)))
def orient4(rs):
    rs=list(rs)
    if matrix(rs).det()<0:rs[0],rs[1]=rs[1],rs[0]
    return rs
cones=[];stellar=[]
for row in raw:
    rs=orient4(row['rays']);M=matrix(rs);D=int(M.det())
    if D==1:cones.append({**row,'rays':rs});continue
    ck('only determinant2 parent',D==2 and row['parent']=='lower_diagonal')
    p=(-1,-2,1,1)
    ck('retained primitive interior ray',list(M.inv()*S.Matrix(p))==[S.Rational(1,2)]*4)
    for k in range(4):
        rr=rs.copy();rr[k]=p;rr=orient4(rr)
        ck(f'stellar determinant{k}',matrix(rr).det()==1)
        cones.append({**row,'rays':rr,'stellar_child':k})
    stellar.append({'parent_rays':rs,'new_ray':p,'coefficients':['1/2']*4})
ck('33 regular cones',len(cones)==33 and len({key(c['rays']) for c in cones})==33)
def faces_on(row):
    return {key(face) for c in cones for face in combinations(c['rays'],3)
            if all(sum(x*y for x,y in zip(row,v))==0 for v in face)}
def transform(v,name):
    x,y,r,z=v
    return {'K':(x+7*r,y+r,r,z),'J':(x+2*r,y+2*r+z,r,z),'KJinv':(x+5*r,y-r-z,r,z)}[name]
facets=[]
for name,target,source in [('K',(1,0,0,0),(1,0,7,0)),('J',(0,1,0,0),(0,1,2,1)),('KJinv',(1,-2,-2,-2),(1,-2,5,0))]:
    src=faces_on(source);dst=faces_on(target);got={key([transform(v,name) for v in face]) for face in src}
    ck('full periodic facet '+name,got==dst)
    facets.append({'period':name,'source_equation':source,'target_equation':target,'faces':len(src),'source_faces':list(src),'target_faces':list(dst),'full_unit_exponents':{'f':{'K':2,'J':1,'KJinv':1}[name]}})
weights=[]
for i,c in enumerate(cones):
    M=matrix(c['rays']);inv=M.inv();ww=list(inv*S.Matrix([1,0,0,0]))
    ck(f'physical weights integral{i}',all(q.q==1 for q in ww))
    sourceZ=[v[1]+3*v[2]+2*v[3] for v in c['rays']];sourceW=[-v[1] for v in c['rays']]
    ck(f'actual QZ inverseZ source monomials{i}',min(sourceZ+sourceW)>=0)
    c.update({'matrix':list(map(list,M.tolist())),'inverse_matrix':list(map(list,inv.tolist())),'physical_weights':ww,'actual_source_QZ':sourceZ,'actual_source_inverseZ':sourceW,'original_canonical_orders':[2*v[2]+v[3]-1 for v in c['rays']]})
    weights.append(ww)
r,z=S.symbols('r z');M=S.Matrix([[7*r,2*r],[r,2*r+z]])
ck('exact period determinant',S.expand(M.det()-12*r*r-7*r*z)==0)
sym=S.diag(1,2)*M
ck('inspection lattice symmetric form',sym==sym.T)
ck('inspection lattice retained',list(sym[1,:])==[2*r,4*r+2*z])
# Independent exact prism determinants at the selected p-boundary.
H=S.Matrix([[3,-1],[6,2]]);I=S.eye(2);u=S.Matrix([1,0]);v=S.Matrix([0,-1]);zero=S.zeros(2,1)
tets=[(0,1,2,5),(0,1,4,5),(0,3,4,5)];signs=[1,-1,1];prisms=[]
for ti,t in enumerate([[zero,u,u+v],[zero,v,u+v]]):
    rr=[(I*p).col_join(S.Matrix([1,0])) for p in t]+[(H*p).col_join(S.Matrix([0,1])) for p in t]
    row=[]
    for j,tet in enumerate(tets):
        determinant=matrix([rr[k] for k in tet]).det()*signs[j]*(-1 if ti==0 else 1)
        ck(f'positive full selected prism{ti},{j}',determinant>0);row.append(int(determinant))
    prisms.append(row)
def enc(a):
    if isinstance(a,dict):return {k:enc(v) for k,v in a.items()}
    if isinstance(a,(tuple,list)):return [enc(v) for v in a]
    if isinstance(a,S.Integer):return int(a)
    if isinstance(a,S.Rational):return str(a)
    return a
out={'status':'PASS','check_count':len(checks),'scope':'Actual selected-I3 p=infinity parent fan and selected p=0 six-prism determinant gate; full simultaneous common refinement, Cartier point graph and compact return remain open.','coordinate_order':['V_reg','Z','ord_R','ord_u'],'physical_cocharacter':[1,0,0,0],'upper_polygon':poly,'upper_triangles':tri,'cones':cones,'stellar_history':stellar,'period_facets':facets,'periods':{'K':{'source':['R^7*f^2*V_reg','R*Z'],'exponents':[[7,0],[1,0]],'word':'h B^2'},'J':{'source':['R^2*f*V_reg','R^2*u*Z'],'exponents':[[2,0],[2,1]],'word':'h B'}},'point_frame':'V_reg=u^6 s Delta V_T=-U6 R^-3 V_pt,R; its reciprocal T_reg=-U6^-1 R^3 V_pt,R^-1 is retained separately','selected_prism_determinants':prisms,'checks':checks}
out=enc(out);Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ('status','check_count','scope','selected_prism_determinants')},indent=2))
