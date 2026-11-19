"""Compute compact one-end strata of the freshly rebuilt raw lower parents.

Uses only this run's K111_lower_parent_reconstruction output. These small
raw-parent resolutions have three lower source charts per label. They
are not the 324-chart common-fan endpoint: no equality to its compact
ledger is inferred without the full refinement comparison.
"""
from pathlib import Path
import json
import sympy as S

p=Path(__file__).resolve().parents[1]
fresh=json.loads((p/'K111_lower_parent_reconstruction.json').read_text())
checks=0
def ck(x,m):
    global checks
    checks+=1
    if not x: raise AssertionError(m)
def matrix(c):return S.Matrix.hstack(*map(S.Matrix,c))
delta=S.Matrix([0,1,0,0])
allcones=[]
for rec in fresh['labels']:
    for c in rec['all_regular_cones']:
        allcones.append((rec['label'],tuple(map(tuple,c))))
face_inventory={}
for label,c in allcones:
    B=matrix(c);w=B.inv()*delta
    normal=tuple(sorted(v for v,a in zip(c,w) if a!=0))
    tangent=tuple(v for v,a in zip(c,w) if a==0)
    # A fixed component lies over the corner precisely when the two
    # actual monomials P and v vanish on its generic normal coordinate locus.
    corner=any(v[2]>0 for v in normal) and any(v[3]>0 for v in normal)
    key=normal
    face_inventory.setdefault(key,[]).append(dict(label=label,rays=c,tangent=tangent,corner=corner))
points=[];curves=[];lower=[]
for normal,owners in face_inventory.items():
    ck(len({x['corner'] for x in owners})==1,'corner property agrees on full fixed face')
    if not owners[0]['corner']:
        lower.append(dict(normal=normal,chart_occurrences=len(owners)));continue
    if len(normal)==4:
        ck(len(owners)==1,'point has one complete regular chart')
        B=matrix(normal);w=list(B.inv()*delta)
        W=S.prod(w);Q=sum(x*x for x in w)
        k=-1/W;ell=-Q/W
        points.append(dict(normal=normal,labels=[x['label'] for x in owners],weights=list(map(str,w)),pair=[str(k),str(ell)]))
    elif len(normal)==3:
        ck(len(owners)==2,'compact curve has its two actual affine charts')
        v0,v1=[x['tangent'][0] for x in owners]
        B=matrix((*normal,v0));ww=B.inv()*delta
        ck(ww[3]==0 and all(x!=0 for x in ww[:3]),'actual three normal weights')
        rel=-B.inv()*(S.Matrix(v0)+S.Matrix(v1))
        ck(rel[3]==0,'tangent rays are opposite primitive quotient generators')
        ck(B*rel==-S.Matrix(v0)-S.Matrix(v1),'full original-lattice normal wall relation')
        w=ww[:3];d=rel[:3];W=S.prod(w)
        SS=sum(a/b for a,b in zip(d,w));Q=sum(x*x for x in w);T=sum(a*b for a,b in zip(w,d))
        k=SS/W;ell=(Q*SS-2*T)/W
        curves.append(dict(normal=normal,tangent_rays=[v0,v1],labels=[x['label'] for x in owners],weights=list(map(str,w)),degrees=list(map(str,d)),pair=[str(k),str(ell)]))
    else:
        raise AssertionError('unexpected compact one-end fixed surface')
pair=[sum(S.Rational(x['pair'][j]) for x in points+curves) for j in range(2)]
perlabel=[]
for l in range(12):
    rows=[x for x in points+curves if l in x['labels']]
    ck(all(set(x['labels'])=={l} for x in rows),'complete corner stars belong to one raw lower parent')
    perlabel.append([sum(S.Rational(x['pair'][j]) for x in rows) for j in range(2)])
ck(len(set(tuple(x) for x in perlabel))==1,'all twelve raw-parent corner values agree')
out=dict(scope='Exact compact one-end points and curves for the newly constructed small raw-parent resolution only. The common-boundary refinement comparison is still required before substituting these values in the full seed.',checks=checks,points=points,curves=curves,other_fixed_faces=lower,pair=list(map(str,pair)),per_label=[list(map(str,x)) for x in perlabel])
(p/'K111_small_one_corner.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=checks,point_count=len(points),curve_count=len(curves),pair=out['pair'],per_label=out['per_label'][0],scope=out['scope']),indent=2))
