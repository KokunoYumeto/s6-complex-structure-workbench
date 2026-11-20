"""Exact IL replay from the one ordered native common-edge chain.

Usage: python K111_replay_edge_chain.py --input CHAIN.json
CHAIN.json is a list [[a0,b0],...,[an,bn]] or an object with
ordered_native_edge_chain containing that list. Endpoints are(0,1),(1,1).
The original upper rays are(3a,a+12b,b,0).

With no input, this executes four explicitly generated example chains
to compare the cyclic intersection and chronological blowdown routes.
Those examples are not the missing actual common edge.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,floor,ceil
from collections import Counter
import argparse,hashlib,json

checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def prim(a,b):
 g=gcd(a,b);return(a//g,b//g)
def lift(p,l=0):
 x,r=p;q=F(x,3);z=ceil(q)-floor(q)
 return(x,ceil(q)+12*r+l*z,r,z)
def native_orders(p):
 x,r=p;return(-floor(F(x,3))-12*r,ceil(F(x,3))+12*r)
def solve_tridiagonal(diag,rhs):
 d=list(map(F,diag));v=list(map(F,rhs))
 for i in range(len(d)-1):
  ck(d[i]<0,'negative exact Schur pivot')
  multiplier=1/d[i];d[i+1]-=multiplier;v[i+1]-=multiplier*v[i]
 ck(d[-1]<0,'last negative exact Schur pivot')
 x=[F(0)]*len(d);x[-1]=v[-1]/d[-1]
 for i in range(len(d)-2,-1,-1):x[i]=(v[i]-x[i+1])/d[i]
 return x

def replay(chain,name):
 start=checks
 chain=list(map(tuple,chain))
 ck(chain[0]==(0,1) and chain[-1]==(1,1),'original marked upper endpoints')
 ck(all(b>0 and 0<=a<=b and gcd(a,b)==1 for a,b in chain),'primitive original boundary lattice rays')
 ck(all(a*d-c*b==-1 for (a,b),(c,d) in zip(chain,chain[1:])),'complete regular ordered upper boundary chain')
 source=set();types=Counter();parent_records=[]
 for (a,b),(c,d) in zip(chain,chain[1:]):
  local={prim(3*a,b),prim(3*c,d)}
  if b%3 and d%3:
   if b%3==d%3:
    types['two_interior']+=1
    local|={(2*a+c,(2*b+d)//3),(a+2*c,(b+2*d)//3)}
   else:
    types['one_interior']+=1;local.add((a+c,(b+d)//3))
  else:types['endpoint_division']+=1
  ordered=sorted(local,key=lambda p:F(*p));source|=local
  # Exact raw-parent barycentric coefficients for every native lift.
  D=3*(a*d-c*b)
  mapped=[]
  for x,r in ordered:
   lam0=F(d*x-3*c*r,D);lam1=F(-b*x+3*a*r,D)
   alpha=F(x,3)-floor(F(x,3));beta=ceil(F(x,3))-F(x,3)
   ck(min(lam0,lam1,alpha,beta)>=0,'actual nonnegative raw-parent coefficient map')
   original=[(0,0,0,1),(0,1,0,1),(3*a,a+12*b,b,0),(3*c,c+12*d,d,0)]
   co=[alpha,beta,lam0,lam1]
   recovered=tuple(sum(co[j]*original[j][i] for j in range(4)) for i in range(4))
   ck(recovered==lift((x,r)),'full original-lattice source/normal lift')
   mapped.append(dict(source_ray=[x,r],native_ray=lift((x,r)),raw_barycentric=list(map(str,co))))
  parent_records.append(dict(upper_endpoints=[(a,b),(c,d)],source_rays=ordered,maps=mapped))
 source=sorted(source,key=lambda p:F(*p))
 ck(source[0]==(0,1) and source[-1]==(3,1),'marked native source period endpoints')
 ck(all(gcd(x,r)==1 for x,r in source),'all actual source rays primitive')
 ck(all(x*s-y*r==-1 for (x,r),(y,s) in zip(source,source[1:])),'all actual source charts regular')
 cyc=source[:-1];n=len(cyc);walls=[];diag=[];dm=[];dp=[]
 for i,p in enumerate(cyc):
  left=(cyc[-1][0]-3*cyc[-1][1],cyc[-1][1]) if i==0 else cyc[i-1]
  right=source[i+1]
  c=F(-left[1]-right[1],p[1])
  ck(c.denominator==1 and -left[0]-right[0]==c*p[0],'full source wall and actual inverse L at zero')
  c=int(c);diag.append(c)
  op=native_orders(p);ol=native_orders(left);orr=native_orders(right)
  nd=tuple(-ol[j]-orr[j]-c*op[j] for j in range(2));dm.append(nd[0]);dp.append(nd[1])
  # Check the complete four-lattice wall, not only its source projection.
  residual=tuple(-lift(left)[j]-lift(right)[j]-c*lift(p)[j] for j in range(4))
  ck(residual==(0,nd[1],0,nd[0]+nd[1]),'actual negative/positive normal wall columns')
  walls.append(dict(source_ray=p,left=left,right=right,self_intersection=c,normal_degrees=nd))
 ck(sum(r*d for (x,r),d in zip(cyc,dm))==sum(r*d for (x,r),d in zip(cyc,dp))==0,'both normal degrees vanish on the full multiplicity fibre')
 cm=[F(0)]+solve_tridiagonal(diag[1:],dm[1:]);cp=[F(0)]+solve_tridiagonal(diag[1:],dp[1:])
 for v,d in [(cm,dm),(cp,dp)]:
  ck(all(diag[i]*v[i]+v[(i-1)%n]+v[(i+1)%n]==d[i] for i in range(n)),'every original cyclic intersection equation')
 pair=[sum(F(dm[i])*cm[i] for i in range(n)),sum(F(dm[i])*cp[i] for i in range(n)),sum(F(dp[i])*cp[i] for i in range(n))]
 remaining=list(source);chronology=[];hist=Counter();protected={(0,1),(1,1),(2,1),(3,1)}
 ck(protected<=set(remaining),'all three minimal source components retained')
 while len(remaining)>4:
  possible=[i for i in range(1,len(remaining)-1) if remaining[i] not in protected and remaining[i]==add(remaining[i-1],remaining[i+1])]
  ck(bool(possible),'next actual ordinary source contraction exists')
  i=min(possible,key=lambda k:(remaining[k][1],remaining[k][0]));left,p,right=remaining[i-1:i+2]
  ol=native_orders(left);op=native_orders(p);orr=native_orders(right)
  ds=tuple(op[j]-ol[j]-orr[j] for j in range(2));hist[ds]+=1
  residual=tuple(lift(p)[j]-lift(left)[j]-lift(right)[j] for j in range(4))
  ck(residual==(0,ds[1],0,ds[0]+ds[1]),'each exact contracted normal coefficient comparison')
  ck(ds in [(-1,0),(0,-1),(-1,-1),(0,0)],'all chronological degree pairs from modulo-three rule')
  chronology.append(dict(left=left,removed=p,right=right,normal_degrees=ds,source_chart_maps=['(u,w)->(u,u*w)','(u,w)->(u*w,w)'],line_coefficient_powers=list(ds)))
  remaining.pop(i)
 ck(remaining==[(0,1),(1,1),(2,1),(3,1)],'actual minimal I3 endpoint')
 changes=[-sum(k*ds[0]**2 for ds,k in hist.items()),-sum(k*ds[0]*ds[1] for ds,k in hist.items()),-sum(k*ds[1]**2 for ds,k in hist.items())]
 minimum=[-F(2,3),-F(1,3),-F(2,3)]
 ck(pair==[a+b for a,b in zip(minimum,changes)],'full cyclic solve agrees with chronological contraction route')
 reference=[-F(2,3),F(2,3),-F(2,3)];closed=[a-b for a,b in zip(pair,reference)]
 tangent=-3*len(chronology);x,y,z=closed;k=x-y+z;ell=tangent-x-z+4*y+2*k
 ck(k.denominator==ell.denominator==1,'completed lower pair integral with the retained reference character')
 return dict(name=name,checks=checks-start,upper_chain=chain,upper_intervals=len(chain)-1,quotient_types=dict(types),source_cycle=cyc,source_charts=n,raw_parent_maps=parent_records,walls=walls,collision_pairings=list(map(str,pair)),chronological_contractions=chronology,histogram={str(ds):k for ds,k in hist.items()},normal_changes=changes,tangent_change=tangent,completed_pair=[int(k),int(ell)])

parser=argparse.ArgumentParser();parser.add_argument('--input',type=Path);parser.add_argument('--output',default='K111_supplied_edge_chain_replay.json');args=parser.parse_args()
p=Path(__file__).resolve().parents[1]
if args.input:
 raw=json.loads(args.input.read_text());chain=raw if isinstance(raw,list) else raw['ordered_native_edge_chain']
 results=[replay(chain,'supplied ordered edge chain')]
 provenance=dict(path=str(args.input.resolve()),sha256=hashlib.sha256(args.input.read_bytes()).hexdigest())
 filename=args.output
 scope='Exact IL evaluation for the supplied ordered edge chain. Provenance must identify it with the actual I2F common edge before this supplies the original lower contribution.'
else:
 farey=sorted({F(a,b) for b in range(1,11) for a in range(b+1)})
 examples=[('minimal raw edge',[(0,1),(1,1)]),('one ordinary upper insertion',[(0,1),(1,2),(1,1)]),('endpoint-division case',[(0,1),(1,3),(1,2),(1,1)]),('Farey order10',[(t.numerator,t.denominator) for t in farey])]
 results=[replay(chain,name) for name,chain in examples];provenance=None
 filename='K111_example_edge_chain_replays.json'
 scope='Four explicit example chains check the exact replay and independent intersection/blowdown routes. No actual I2F common-edge chain is loaded.'
out=dict(scope=scope,checks=checks,input_provenance=provenance,results=results)
(p/filename).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=checks,supplied_edge_chain_loaded=bool(args.input),output=filename,summary=[{k:v for k,v in r.items() if k in ['name','upper_intervals','source_charts','histogram','completed_pair']} for r in results]),indent=2))
