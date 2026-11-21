"""Exact reread verification of the eleven displayed CM model transports.

This program was written after reading C.6.3. It gives no preread credit.
It reconstructs the rational scale from the section and cubic coefficient,
then uses rational tangent doubling and the checked local-height formula.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import re,json,hashlib
B=Path(__file__).parent
source=Path('/workspace/scratch/653608133b22/source/S6_SERIES_GRIND_I.tex').read_text()
start=source.index(r'\label{ari:C.6.3}')
end=source.index(r'\label{ari:C.6.4}',start)
part=source[start:end]
models=[]
for line in part.splitlines():
 m=re.fullmatch(r'(\d+) & (-?\d+) & (-?\d+) & (-?\d+) & (-?\d+) & (-?\d+)\\\\',line)
 if m:models.append(tuple(map(int,m.groups())))
assert len(models)==11
def val(x,p):
 x=Q(x);a,b=x.numerator,x.denominator;v=0
 assert a
 while a%p==0:a//=p;v+=1
 while b%p==0:b//=p;v-=1
 return v
def frac_tex(s):
 m=re.fullmatch(r'\\frac\{(\d+)\}\{(\d+)\}',s)
 return Q(*map(int,m.groups())) if m else Q(s)
locals=[]
for line in part.splitlines():
 m=re.fullmatch(r'(\d+) & (\d+) & (.*?) & (.*?) & (\d+) & \$(.*?)\$\\\\',line)
 if m:locals.append((int(m[1]),int(m[2]),m[3],m[4],int(m[5]),frac_tex(m[6])))
assert len(locals)==32
rows=[]
for i,j,a3,a4,a6,yp in models:
 t=Q(j,1728);A=-Q(3,4)*t**3*(t-1);BB=Q(1,4)*t**4*(t-1)**2
 scale=-3*t*(2*yp+a3)/(4*a4)
 assert A==scale**4*a4
 assert BB==scale**6*(Q(a6)+Q(a3*a3,4))
 assert t*t*(t-1)/2==scale**3*(Q(yp)+Q(a3,2))
 assert yp*yp+a3*yp==a6
 delta=-64*a4**3-27*(a3*a3+4*a6)**2
 assert Q(delta)*scale**12==27*t**8*(t-1)**3
 slope=Q(a4,2*yp+a3)
 xx=slope*slope
 yy=-slope*xx-yp-a3
 assert yy*yy+a3*yy==xx**3+a4*xx+a6
 checks=[]
 for row,p,typ,comp,m,expected in locals:
  if row!=i:continue
  x,y=(Q(0),Q(yp)) if m==1 else (xx,yy)
  assert m in (1,2)
  psi=Q(1) if m==1 else Q(2*yp+a3)
  negvx=max(0,-val(x,p)) if x else 0
  if x.denominator%p!=0 and y.denominator%p!=0:
   xm=x.numerator*pow(x.denominator,-1,p)%p
   ym=y.numerator*pow(y.denominator,-1,p)%p
   assert (-3*xm*xm-a4)%p or (2*ym+a3)%p
  else:
   assert negvx>0
  actual=Q(val(delta,p),12)+(Q(negvx,2)-val(psi,p))/(m*m)
  assert actual==expected,(i,p,actual,expected)
  checks.append(dict(p=p,m=m,height_coefficient=str(actual)))
 rows.append(dict(row=i,j=j,scale=str(scale),delta=delta,double=[str(xx),str(yy)],finite=checks))
out=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
 program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 source_sha256=hashlib.sha256(source.encode()).hexdigest(),
 scope="Exact transports and all 32 displayed finite-height entries; no Tate type or global rank reproof.",
 rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
