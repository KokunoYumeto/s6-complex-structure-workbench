"""Exact special-case comparison for the displayed integral twist formulas.

This is a new post-reading arithmetic comparison. It does not create an
independent pre-reading proof event. Weighted sections are counted by their
monomials; the separate residue formula is compared against that count.
The universal Euler identity follows from u-v=d+1 and d(n+12)=d(n)+1,
reducing its verification to the twelve residue classes recorded below.
"""
from pathlib import Path
import datetime as dt, hashlib, json
R=Path(__file__).resolve().parents[1]
def monomials(weight):
    if weight<0: return []
    return [(a,b) for a in range(weight//3+1) for b in range(weight//4+1) if 3*a+4*b==weight]
def d(n):
    numerator=n-4*(n%3)-3*((3*n)%4)
    assert numerator%12==0
    return numerator//12
def u(n): return max(d(n)+1,0)
def v(n): return max(-d(n)-1,0)
def tuple_from_dimensions(h0,h1,n):
    eps=int(n%3!=0)
    return [h0(n)+h0(n-1),h1(n)+h1(n-1)+h0(n)+h0(n-1)+h0(n+2),h1(n)+h1(n-1)+h1(n+2)+h0(n+6)+eps,h1(n+6)]
rows=[]
for n in range(-96,97):
    count=lambda m:len(monomials(m))
    dual=lambda m:len(monomials(-m-7))
    assert (u(n),v(n))==(count(n),dual(n))
    calculated=tuple_from_dimensions(count,dual,n)
    displayed=tuple_from_dimensions(u,v,n)
    assert calculated==displayed
    rank=int(bool(monomials(n+6)))
    assert rank==int(n in {-6,-3,-2} or n>=0)
    assert sum((-1)**i*x for i,x in enumerate(calculated))==1
    rows.append(dict(n=n,dimensions=calculated,normalization_map_rank=rank))
residues=[]
for n in range(12):
    value=d(n+6)-d(n+2)+int(n%3!=0)
    assert value==1
    residues.append(dict(residue=n,d_n_plus_6=d(n+6),d_n_plus_2=d(n+2),epsilon=int(n%3!=0),euler=value))
assert next(x for x in rows if x['n']==0)['dimensions']==[1,1,1,0]
assert next(x for x in rows if x['n']==-1)==dict(n=-1,dimensions=[0,0,1,0],normalization_map_rank=0)
out=R/'code/S6_SERIES_PUBLISH_II_global_E_special_cases.json'; assert not out.exists()
data=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),source_sha256=hashlib.sha256((R/'S6_SERIES_PUBLISH_II.tex').read_bytes()).hexdigest(),method='Weighted-monomial enumeration and Serre-dual counts, compared with the displayed coarse-degree formula; arithmetic only',interval=[-96,96],integral_twists_compared=len(rows),rows=rows,euler_residues=residues,known_special_case='DGKX arXiv2610.00250v1 Theorem6.12 pp81-82: (1,1,1,0)',map_exception='At n=-1 the only H2 class comes from the finite order-three fibre; the normalization target is at the cusp and the preceding displayed exact sequence gives rank zero.',scope='Actual morphisms, analytic direct-image statements and primary proof comparisons are recorded separately. This finite arithmetic calculation alone does not establish those analytic results.',check_events_added=0,required_checks_closed=0)
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(dict(output=str(out.relative_to(R)),sha256=hashlib.sha256(out.read_bytes()).hexdigest(),twists_compared=len(rows),untwisted=next(x for x in rows if x['n']==0),exception=next(x for x in rows if x['n']==-1),euler_residues=residues),indent=2))
