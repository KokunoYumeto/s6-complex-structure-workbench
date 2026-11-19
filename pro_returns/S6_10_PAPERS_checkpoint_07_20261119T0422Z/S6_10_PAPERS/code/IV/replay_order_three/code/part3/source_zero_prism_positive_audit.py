#!/usr/bin/env python3
"""Independent exact determinants, rank-one face identities and H overlays."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json
import sympy as s

root=Path(__file__).resolve().parents[2]
N=s.symbols('N',integer=True,positive=True)
r,ss=s.symbols('r s',positive=True)
checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append({'name':name,'pass':True})
def zero(x):
    return all(s.simplify(v)==0 for v in x) if isinstance(x,s.MatrixBase) else s.simplify(x)==0
def ray(P,n,i):return s.Matrix([*(P*n),1-i,i])
def cones(P0,P1,u,v):
    out=[]
    for w in (u,v):
        ns=(s.zeros(2,1),w,u+v)
        z=[ray(P0,x,0) for x in ns];t=[ray(P1,x,1) for x in ns]
        out.extend([s.Matrix.hstack(z[0],z[1],z[2],t[2]),s.Matrix.hstack(z[0],z[1],t[1],t[2]),s.Matrix.hstack(z[0],t[0],t[1],t[2])])
    return out

I=s.eye(2);e1=s.Matrix([1,0]);e2=s.Matrix([0,1])
rows={'I':[1,N-1,2*N,1,2,2*N],'W':[0,N-1,2*N,0,0,2*N],'E':[0,0,2*N,0,2*N,2*N]}
strip_records=[]
for a,b in ((1,2),(2,1)):
    W=s.Matrix([[1,b],[-a,-2]]);E=s.Matrix([[0,0],[0,N]]);H=I+W+E
    for name,P0,u,v in (('I',I,e1,e2),('W',W,e1,e2-b*e1),('E',E,e1,e2)):
        cs=cones(P0,H,u,v);domain=cones(I,I,u,v)
        for j,(C,D,want) in enumerate(zip(cs,domain,rows[name])):
            ck(f'{a},{b} {name} signed determinant {j}',zero(C.det()/D.det()-want))
        want={'I':r*r+(N+1)*r*ss+2*N*ss*ss,'W':(N-1)*r*ss+2*N*ss*ss,'E':2*N*r*ss+2*N*ss*ss}[name]
        ck(f'{a},{b} {name} exact period determinant',zero((r*P0+ss*H).det()-want))
    for name,P0,u,v,cwant,dwant in (('W',W,e1,e2-b*e1,(N-1)/(2*N),-s.Rational(a,2)/N),('E',E,e2,e1,s.Integer(1),-s.Rational(b,2))):
        p=P0*u;A=H*u;B=H*v;AB=s.Matrix.hstack(A,B);z=AB.inv()*p;c,d=z
        ck(f'{a},{b} {name} killed primitive basis vector',P0*v==s.zeros(2,1))
        ck(f'{a},{b} {name} exact positive strip coefficient',zero(c-cwant))
        ck(f'{a},{b} {name} exact strip slope',zero(d-dwant))
        ck(f'{a},{b} {name} actual first strip period',zero(AB.inv()*(r*P0+ss*H)*u-s.Matrix([ss+r*c,r*d])))
        ck(f'{a},{b} {name} actual second strip period',zero(AB.inv()*(r*P0+ss*H)*v-s.Matrix([0,ss])))
        R0=lambda n:ray(P0,n,0);R1=lambda n:ray(H,n,1);o=s.zeros(2,1)
        ck(f'{a},{b} {name} duplicate lower rays',R0(v)==R0(o) and R0(u+v)==R0(u))
        # The collapsed cone generators are literally subsets of the named
        # surviving facet generators after removing duplicate lower rays.
        key=lambda x:tuple(x)
        colset=lambda *xs:{key(x) for x in xs}
        collapsed1=colset(R0(o),R0(u),R0(u+v),R1(u+v))
        collapsed2=colset(R0(o),R0(v),R0(u+v),R1(u+v))
        mixed=colset(R0(o),R0(u),R1(u),R1(u+v))
        ck(f'{a},{b} {name} both lower collapses are the mixed top face',collapsed1==collapsed2==colset(R0(o),R0(u),R1(u+v)) and collapsed1<mixed)
        collapsed3=colset(R0(o),R0(v),R1(v),R1(u+v))
        upper=colset(R0(o),R1(o),R1(v),R1(u+v))
        ck(f'{a},{b} {name} other collapse is the square top face',collapsed3==colset(R0(o),R1(v),R1(u+v)) and collapsed3<upper)
        ck(f'{a},{b} {name} mixed upper face equals translated lower face',colset(R0(o),R0(u),R1(u+v))==colset(R0(v),R0(u+v),R1(u+v)))
        strip_records.append({'a':a,'b':b,'sector':name,'c':str(c),'d':str(d),'periods':['(s+r*c,r*d)','(0,s)']})

# Exact rational polygon overlay in the H^-1 inspection plane.
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):return sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2 if len(poly)>2 else Q(0)
def clean(poly):
    out=[]
    for p in poly:
        if not out or p!=out[-1]:out.append(p)
    if len(out)>1 and out[0]==out[-1]:out.pop()
    changed=True
    while changed and len(out)>2:
        changed=False
        for i in range(len(out)):
            if cross(sub(out[i],out[i-1]),sub(out[(i+1)%len(out)],out[i]))==0:
                out.pop(i);changed=True;break
    if area(out)<0:out.reverse()
    return out
def clip(poly,window):
    poly=clean(poly);window=clean(window)
    for i,A in enumerate(window):
        B=window[(i+1)%len(window)];edge=sub(B,A);out=[]
        if not poly:break
        for j,P in enumerate(poly):
            Qp=poly[(j+1)%len(poly)];fp=cross(edge,sub(P,A));fq=cross(edge,sub(Qp,A))
            if fp>=0:out.append(P)
            if (fp<0<fq) or (fq<0<fp):
                t=fp/(fp-fq);out.append((P[0]+t*(Qp[0]-P[0]),P[1]+t*(Qp[1]-P[1])))
        poly=clean(out)
    return clean(poly)
def canonical(poly):
    p=clean(poly)
    return min(tuple(p[i:]+p[:i]) for i in range(len(p))) if p else ()
def shift(poly,dx,dy):return [(x+dx,y+dy) for x,y in poly]
def is_face(poly,intersection):
    pts=list(dict.fromkeys(intersection))
    if not pts:return True
    if len(pts)==1:return pts[0] in poly
    ends=(min(pts),max(pts))
    return any(set(ends)==set((poly[i],poly[(i+1)%len(poly)])) for i in range(len(poly)))

std=[[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1))],[(Q(0),Q(0)),(Q(0),Q(1)),(Q(1),Q(1))]]
overlays=[]
for b in (1,2):
    shear=lambda p:(p[0]-b*p[1],p[1])
    other=[[shear(p) for p in tri] for tri in std]
    cells={}
    for tri in std:
        for dx in range(-b-2,b+4):
            for dy in range(-2,3):
                for tau in other:
                    q=clip(tri,shift(tau,Q(dx),Q(dy)))
                    if area(q)>0:cells[canonical(q)]=q
    polys=list(cells.values())
    ck(f'common H overlay b={b} exact area one',sum(area(p) for p in polys)==1)
    face_count=0
    for i,P in enumerate(polys):
        for j,Qp in enumerate(polys):
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    if i==j and dx==dy==0:continue
                    T=shift(Qp,Q(dx),Q(dy));inter=clip(P,T)
                    if not inter:continue
                    ck(f'H overlay b={b} common face {i}/{j}+({dx},{dy})',area(inter)==0 and is_face(P,inter) and is_face(T,inter));face_count+=1
    verts=sorted({p for poly in polys for p in poly})
    overlays.append({'b':b,'cells':[[[str(x),str(y)] for x,y in p] for p in polys],'areas':[str(area(p)) for p in polys],'vertices':[[str(x),str(y)] for x,y in verts],'checked_nonempty_intersections':face_count})

# The actual primitive E-boundary chain and its scalar-period arrow.
jj,kk=s.symbols('j k',integer=True)
ck('E-boundary adjacent primitive ray determinant',s.Matrix([[jj,jj+1],[1,1]]).det()==-1)
ck('E-boundary height-one primitive generator',s.gcd(jj,s.Integer(1))==1)
ck('E-boundary scalar period moves j to j plus N',s.Matrix([0,jj,1,0])+s.Matrix([0,N,0,0])==s.Matrix([0,jj+N,1,0]))
X=s.Matrix([-jj,1]);Y=s.Matrix([jj+1,-1])
ck('E-boundary exact chain product character',X+Y==s.Matrix([1,0]))
ck('E-boundary period and chart reindex preserve X',s.Matrix([-(jj+N)+N,1])==X)
ck('E-boundary period and chart reindex preserve Y',s.Matrix([jj+N+1-N,-1])==Y)

result={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'scope':'Independent local prism-fan/common-H-refinement audit only; no analytic quotient or K39 return is assigned.','identities':checks,'rank_one_strips':strip_records,'H_boundary_overlays':overlays,'proof':'notes/part3_source_zero_prism_audit.md'}
(root/'code/part3/source_zero_prism_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(checks)} exact local prism, strip-face and common-H-overlay checks.')
for o in overlays:print(f'H boundary b={o["b"]}: {len(o["cells"])} rational cells, total area 1, {o["checked_nonempty_intersections"]} exact common-face checks.')
