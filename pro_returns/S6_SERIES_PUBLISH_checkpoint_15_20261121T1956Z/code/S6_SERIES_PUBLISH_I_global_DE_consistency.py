from pathlib import Path
import json,datetime,hashlib
from fractions import Fraction
r=Path(__file__).resolve().parents[1]
# Tables are generated from the body formulas, in increasing q order.
h=1
dol=[[1,0,0,0],[1,h+1,h,0],[0,h,h+1,1],[0,0,0,1]]
bc=[[1,0,0,0],[0,2,h,0],[0,h,2*h,1],[0,0,1,1]]
ae=[[1,1,0,0],[1,2*h,h,0],[0,h,2,0],[0,0,0,1]]
ranks={(0,1):1,(1,1):h,(1,2):h,(2,2):1}
e2=[[dol[q][p]-ranks.get((p-1,q),0)-ranks.get((p,q),0) for p in range(4)] for q in range(4)]
assert e2==[[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
assert all(ae[q][p]==bc[3-q][3-p] for p in range(4) for q in range(4))
assert sum(map(sum,bc))==10
def d(n):
 num=n-4*(n%3)-3*((3*n)%4);assert num%12==0;return num//12
def uv(n):return max(d(n)+1,0),max(-d(n)-1,0)
def dims(n):
 u,v=uv(n);u1,v1=uv(n-1);u2,v2=uv(n+2);u6,v6=uv(n+6)
 return [u+u1,v+v1+u+u1+u2,v+v1+v2+u6+int(n%3!=0),v6]
assert dims(0)==[1,1,1,0]
# Exact twelve residue formulas prove the integer/period identity for all n.
residues=[{'r':n,'d':d(n),'d_shift':d(n+12),'tuple':dims(n)} for n in range(12)]
assert all(x['d_shift']==x['d']+1 for x in residues)
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'New exposed-input consistency calculation of body-to-main table and formula transport. It is not an independent proof of the body theorems.',
 'dolbeault_q_increasing':dol,'BC_q_increasing':bc,'A_q_increasing':ae,'E2_q_increasing':e2,
 'positive_BC_dimension':sum(map(sum,bc))-1,'untwisted':dims(0),'residue_formulas':residues}
p=r/'records/S6_SERIES_PUBLISH_I_global_DE_consistency.json';p.write_text(json.dumps(out,indent=2)+'\n')
files=[r/'records/S6_SERIES_PUBLISH_I_global_DE_intake.json',r/'records/S6_SERIES_PUBLISH_I_global_DE_derivation.md',Path(__file__),p]
freeze={'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Final main D/E claim map and new consistency calculation, frozen before reopening the current outlines in this pass; prior proof/frontmatter exposure disclosed.',
 'files':[{'path':str(q.relative_to(r)),'sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'bytes':q.stat().st_size} for q in files]}
fp=r/'records/S6_SERIES_PUBLISH_I_global_DE_freeze.json';assert not fp.exists();fp.write_text(json.dumps(freeze,indent=2)+'\n')
print(json.dumps({'result':'PASS','freeze':str(fp),'freeze_sha256':hashlib.sha256(fp.read_bytes()).hexdigest()}))
