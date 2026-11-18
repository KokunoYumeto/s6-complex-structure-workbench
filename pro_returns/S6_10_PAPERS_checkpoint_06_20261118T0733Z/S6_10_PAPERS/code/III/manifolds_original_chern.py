"""Every nonzero-Chern original additive cap on the172 natural candidate rows.
Exact marked area kernels, primitive Chern vectors, and all additive choices.
"""
from pathlib import Path
import json,itertools,sympy as s
from math import gcd
from collections import Counter
from manifolds_rankone_families import decomp,ikernel,wedge
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'manifolds_all_finite_logs.json').read_text())['rows']
monos=json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']
initial=json.loads((ROOT/'manifolds_sphere_initial.json').read_text())['candidates']
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
M={key(r):r for r in monos};I={key(r):r for r in initial}
def ismult(k):return k.startswith('I') and k[1:].isdigit()
def solve(A,v):
 D,U,V,r=decomp(A);z=U*v;y=s.zeros(A.cols,1)
 for j in range(r):assert z[j]%D[j,j]==0;y[j]=z[j]/D[j,j]
 assert all(z[j]==0 for j in range(r,A.rows));ans=V*y;assert A*ans==v;return ans
cert=[];patterns=[]
for row in rows:
 K=key(row);local=[];sites=[];choices=[]
 for j,(loc,geom) in enumerate(zip(row['local'],I[K]['local'])):
  if ismult(loc['type']):continue
  sites.append(j);opts=['original']
  if 'q' in loc:opts.append('log')
  choices.append(opts)
  if geom['P_component']==0:
   local.append(dict(site=j,zero_Chern=True,defect=geom['component_orbits']-1,h=None));continue
  assert geom['Q_component']==0
  A=s.Matrix(M[K]['local'][j]['matrix'])
  for Bcheck in [A-s.eye(4),wedge(A)-s.eye(6)]:
   DD,UU,VV,rr=decomp(Bcheck);assert all(abs(DD[h,h])==1 for h in range(rr))
  assert gcd(row['a'],row['b'])==1
  z=solve(A[:2,:2]-s.eye(2),A[:2,3])
  ell=s.Matrix([-z[0],-z[1],0,1]);assert A*ell==ell
  F=ikernel(A-s.eye(4));L=(F.T*F).inv()*F.T;assert abs((L*s.Matrix.hstack(s.eye(4)[:,2],ell)).det())==1
  w=s.Matrix([[1,0,z[1],0,-z[0],0]]);assert w*wedge(A)==w
  ker=ikernel(w);omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]])
  h=gcd(*map(int,list(omega*ker)))
  q={'III':2,'III*':2,'IV':3,'IV*':3,'I1*':4,'I3*':4}[loc['type']]
  assert h==row['b']//q and row['b']%q==0
  c=s.Matrix(geom['P_degree_vector'])
  mult=s.Matrix(geom['component_multiplicities']);assert (c.T*mult)[0]==0
  assert gcd(*map(int,list(c)))==1
  ker_c=ikernel(c.T);coord=(ker_c.T*ker_c).inv()*ker_c.T*mult
  assert all(v.q==1 for v in coord) and gcd(*map(int,list(coord)))==1
  rec={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']}
  rec.update(site=j,type=loc['type'],components=len(mult),component_group_order=q,
             z=list(z),area_covector=list(w),fibre_relation=h,chern=list(c),multiplicities=list(mult),
             free_defect=len(mult)-2)
  cert.append(rec);local.append(dict(site=j,zero_Chern=False,defect=len(mult)-2,h=h))
 for cc in itertools.product(*choices):
  original=[j for j,c in zip(sites,cc) if c=='original'];finite=[j for j,c in zip(sites,cc) if c=='log']
  selected=[v for v in local if v['site'] in original]
  L=sum(not v['zero_Chern'] for v in selected);D=sum(v['defect'] for v in selected)
  rec={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']}
  rec.update(additive_choices=list(zip(sites,cc)),finite_indices=finite,nonzero_chern_count=L,
             local_free_defect=D,fibre_relations=[v['h'] for v in selected if v['h'] is not None])
  patterns.append(rec)
# Compare the full original fibre kernels and normal sweeps with the reduced
# presentation on every new additive pattern, including cap torsion and
# zero rational Euler number. Finite multiplicities remain symbolic in proof.
def group(A):
 D,U,V,r=decomp(A);return A.rows-r,[int(abs(D[j,j])) for j in range(r) if abs(D[j,j])>1]
def reduced(b,params,hs):
 size=1+2*len(params);cols=[];v=s.zeros(size,1)
 for i in range(len(params)):v[1+2*i]=1
 cols.append(v)
 for i,(d,q,g,m,n,r0) in enumerate(params):
  qv=q//g
  for c0,cd,cl in [(b*g*n//qv,m//qv,0),(-b*r0,0,m//g),(0,r0,n)]:
   v=s.zeros(size,1);v[0]=c0;v[1+2*i]=cd;v[2+2*i]=cl;cols.append(v)
 for h in hs:
  v=s.zeros(size,1);v[0]=h;cols.append(v)
 return s.Matrix.hstack(*cols)
lookup={key(r):r for r in rows};chern={(key(r),r['site']):r for r in cert};cache={};checks=0;zero_cases=0;tors_caps=0
for pat in patterns:
 if not pat['nonzero_chern_count']:continue
 K=key(pat);row=lookup[K];A=[s.Matrix(v['matrix']) for v in M[K]['local']];N=len(A)
 if K not in cache:
  D=s.Matrix.hstack(*[v-s.eye(4) for v in A[:-1]]);Sd,Ud,Vd,rd=decomp(D);Wi=Vd.inv()[rd:,:];Js=[]
  for i in range(N):
   if i<N-1:
    J=s.zeros(4*(N-1),4);J[4*i:4*i+4,:]=s.eye(4)
   else:
    oo=[]
    for j in range(N-1):
     P=s.eye(4)
     for v in A[j+1:N-1]:P=P*v
     oo.append(-P)
    J=s.Matrix.vstack(*oo)
   Js.append(Wi*J)
  cache[K]=Js
 Js=cache[K];fi=pat['finite_indices'];choices=dict(pat['additive_choices'])
 for case in range(3 if fi else 1):
  params=[]
  for i in fi:
   loc=row['local'][i];d=loc['log_order'];q=loc['q'];g=loc['gamma_index']
   if case==0:m,n,r0=(d,1,0) if g==1 else (d,1,1)
   elif case==1:m,n,r0=(d*q,q,1) if g==1 else (d*q,1,0)
   else:m,n,r0=(d*q,0,1) if g==1 else (d,0,1)
   t=gcd(m,(q//g)*r0,g*n);assert gcd(m,n,r0)==1 and (m//t)%d==0
   tors_caps+=t>1;params.append((d,q,g,m,n,r0))
  bysite={i:p for i,p in zip(fi,params)};cols=[];omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]])
  for i,loc in enumerate(row['local']):
   if i in bysite:
    d,q,g,m,n,r0=bysite[i];qv=q//g;delta=s.eye(4)[:,2];ell=s.Matrix(loc['ell']);beta=s.Matrix(loc['beta']);eta=s.Matrix(loc['eta']);Nm=sum((A[i]**j for j in range(m)),s.zeros(4))
    for c0,v in [(row['b']*g*n//qv,Nm*beta),(-row['b']*r0,Nm*eta),(0,r0*delta+n*ell)]:cols.append(s.Matrix([c0]).col_join(Js[i]*v))
   else:
    F=s.Matrix(loc['fixed'])
    if choices.get(i)=='original' and (K,i) in chern:
     c=chern[K,i];z=c['z'];F=s.Matrix.hstack(s.eye(4)[:,2],s.Matrix([-z[0],-z[1],0,1]));w=s.Matrix([c['area_covector']]);V=ikernel(w)
     for j in range(V.cols):cols.append(s.Matrix([(omega*V[:,j])[0]]).col_join(s.zeros(Js[i].rows,1)))
    for j in range(F.cols):cols.append(s.Matrix([0]).col_join(Js[i]*F[:,j]))
  full=s.Matrix.hstack(*cols);small=reduced(row['b'],params,pat['fibre_relations'])
  assert group(full)==group(small) and group(small)[0]==0
  S=s.zeros(len(params)+1)
  for j,(_,_,g,m,n,r0) in enumerate(params):S[j,0]=-g*n;S[j,j+1]=m;S[-1,j+1]=1
  rr,A1=group(S);assert rr in (0,1);zero_cases+=rr==1;checks+=1
print('Nonzero-Chern original additive certificates:',len(cert),dict(Counter(v['type'] for v in cert)),flush=True)
print('All additive original/log patterns:',len(patterns),'initial rows:',len(set(key(p) for p in patterns)),flush=True)
print('Patterns involving a nonzero-Chern original:',sum(p['nonzero_chern_count']>0 for p in patterns),flush=True)
print('Full unreduced Smith comparisons:',checks,'torsion caps:',tors_caps,'Euler-zero instances:',zero_cases,flush=True)
assert len(cert)==46 and len(patterns)==282 and len(set(key(p) for p in patterns))==172
(ROOT/'manifolds_original_chern.json').write_text(json.dumps(dict(scope=__doc__,local=cert,patterns=patterns,full_Smith_checks=checks,torsion_cap_instances=tors_caps,euler_zero_instances=zero_cases),indent=2,default=int)+'\n')
