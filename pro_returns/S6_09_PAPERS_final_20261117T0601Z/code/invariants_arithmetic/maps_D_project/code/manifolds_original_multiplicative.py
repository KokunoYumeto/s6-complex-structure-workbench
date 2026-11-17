"""Every original/Mumford multiplicative choice on the natural candidate rows.
Exact nonzero-Chern nodal-cycle cap kernels and full global Smith comparisons.
"""
from pathlib import Path
import json,itertools,sympy as s
from math import gcd
from collections import Counter
from manifolds_rankone_families import decomp,ikernel,wedge,biv,bezout
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'records/manifolds_all_finite_logs.json').read_text())['rows']
monos=json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']
initial=json.loads((ROOT/'records/manifolds_sphere_initial.json').read_text())['candidates']
add=json.loads((ROOT/'records/manifolds_original_chern.json').read_text())
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
M={key(r):r for r in monos};I={key(r):r for r in initial};R={key(r):r for r in rows}
def mult(k):return k.startswith('I') and k[1:].isdigit()
def group(A):
 D,U,V,r=decomp(A);return A.rows-r,[int(abs(D[j,j])) for j in range(r) if abs(D[j,j])>1]
def solve(A,v):
 D,U,V,r=decomp(A);z=U*v;y=s.zeros(A.cols,1)
 for j in range(r):assert z[j]%D[j,j]==0;y[j]=z[j]/D[j,j]
 assert all(z[j]==0 for j in range(r,A.rows));out=V*y;assert A*out==v;return out

cert=[];byrow={};zero_equiv={}
for row in rows:
 K=key(row);ids=[];eq=[]
 for j,(loc,geom) in enumerate(zip(row['local'],I[K]['local'])):
  if j==row['zero_index'] or not mult(loc['type']):continue
  n=int(loc['type'][1:])
  if geom['P_component']==0:
   assert geom['component_orbits']==1;eq.append(j);continue
  assert n>1 and geom['Q_component']==0 and gcd(n,geom['P_component'])==1
  A=s.Matrix(M[K]['local'][j]['matrix']);B=A[:2,:2];D,U,V,r=decomp(B-s.eye(2));assert r==1 and abs(D[0,0])==n
  u=U.inv()[:,0];bez,g=bezout(list(u));assert g==1
  v=s.Matrix([-bez[1],bez[0]]);assert s.Matrix.hstack(u,v).det()==1
  z=solve(B-s.eye(2),A[:2,3]);u1=u.col_join(s.zeros(2,1));u2=v.col_join(s.zeros(2,1));delta=s.eye(4)[:,2];ell=s.Matrix([-z[0],-z[1],0,1])
  C=s.Matrix.hstack(u1,u2,delta,ell);assert C.det()==1
  Ac=C.inv()*A*C;nn=Ac[0,1];p=Ac[2,1]
  assert abs(nn)==n and gcd(int(nn),int(p))==1
  expected=s.eye(4);expected[0,1]=nn;expected[2,1]=p;assert Ac==expected
  assert group(A-s.eye(4))==(3,[]) and group(wedge(A)-s.eye(6))==(4,[])
  F=ikernel(A-s.eye(4));Fl=s.Matrix.hstack(u1,delta,ell);Finv=(F.T*F).inv()*F.T;assert abs((Finv*Fl).det())==1
  K2=s.Matrix.hstack(biv(u1,delta),biv(u1,ell),biv(delta,ell));assert K2.rank()==3
  Dk,Uk,Vk,rk=decomp(K2);assert all(abs(Dk[h,h])==1 for h in range(rk))
  Ki=(K2.T*K2).inv()*K2.T;im=Ki*(wedge(A)-s.eye(6));assert K2*im==wedge(A)-s.eye(6)
  assert all(x.q==1 for x in im) and group(im)==(1,[])
  omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]]);values=omega*K2;h=gcd(*map(int,list(values)))
  assert row['b']%n==0 and h==row['b']//n and (omega*biv(u2,delta))[0]==0
  c=s.Matrix(geom['P_degree_vector']);ones=s.ones(n,1);assert (c.T*ones)[0]==0 and gcd(*map(int,list(c)))==1
  ker=ikernel(c.T);coord=(ker.T*ker).inv()*ker.T*ones;assert all(x.q==1 for x in coord) and gcd(*map(int,list(coord)))==1
  rec={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']}
  rec.update(site=j,type=loc['type'],n=n,basis=C.tolist(),normal_form=Ac.tolist(),p=int(p),
             fixed=Fl.tolist(),fibre_kernel=K2.tolist(),omega_values=list(values),fibre_relation=h,
             free_defect=n-2,chern=list(c),normal_adjustment_class=biv(u2,delta).tolist())
  cert.append(rec);ids.append(j)
 byrow[K]=ids;zero_equiv[K]=eq
lookup={(key(c),c['site']):c for c in cert};addlocal={(key(c),c['site']):c for c in add['local']}
patterns=[];checks=0;tors_caps=0;zero_euler=0;cache={}
for old in add['patterns']:
 K=key(old);row=R[K];ids=byrow[K];A=[s.Matrix(v['matrix']) for v in M[K]['local']];N=len(A)
 for choices in itertools.product(['mumford','original'],repeat=len(ids)):
  original=[j for j,c in zip(ids,choices) if c=='original'];new=dict(old)
  new.update(multiplicative_choices=list(zip(ids,choices)),homology_equivalent_zero_degree_choices=zero_equiv[K])
  new['nonzero_chern_count']=old['nonzero_chern_count']+len(original)
  new['local_free_defect']=old['local_free_defect']+sum(lookup[K,j]['free_defect'] for j in original)
  new['fibre_relations']=old['fibre_relations']+[lookup[K,j]['fibre_relation'] for j in original]
  patterns.append(new)
  if not original:continue
  if K not in cache:
   D=s.Matrix.hstack(*[v-s.eye(4) for v in A[:-1]]);Sd,Ud,Vd,rd=decomp(D);Wi=Vd.inv()[rd:,:];Js=[]
   for i in range(N):
    if i<N-1:J=s.zeros(4*(N-1),4);J[4*i:4*i+4,:]=s.eye(4)
    else:
     oo=[]
     for j in range(N-1):
      P=s.eye(4)
      for v in A[j+1:N-1]:P=P*v
      oo.append(-P)
     J=s.Matrix.vstack(*oo)
    Js.append(Wi*J)
   cache[K]=Js
  Js=cache[K];fi=new['finite_indices'];params=[];case=checks%3
  for i in fi:
   loc=row['local'][i];d=loc['log_order'];q=loc['q'];g=loc['gamma_index']
   if case==0:m,n,r0=(d,1,0) if g==1 else (d,1,1)
   elif case==1:m,n,r0=(d*q,q,1) if g==1 else (d*q,1,0)
   else:m,n,r0=(d*q,0,1) if g==1 else (d,0,1)
   t=gcd(m,(q//g)*r0,g*n);assert gcd(m,n,r0)==1 and (m//t)%d==0;tors_caps+=t>1
   params.append((d,q,g,m,n,r0))
  f=len(params);small=[];v=s.zeros(1+2*f,1)
  for i in range(f):v[1+2*i]=1
  small.append(v)
  for i,(d,q,g,m,n,r0) in enumerate(params):
   qv=q//g
   for c0,cd,cl in [(row['b']*g*n//qv,m//qv,0),(-row['b']*r0,0,m//g),(0,r0,n)]:
    v=s.zeros(1+2*f,1);v[0]=c0;v[1+2*i]=cd;v[2+2*i]=cl;small.append(v)
  for h in new['fibre_relations']:
   v=s.zeros(1+2*f,1);v[0]=h;small.append(v)
  small=s.Matrix.hstack(*small);bysi={i:p for i,p in zip(fi,params)};addchoices=dict(new['additive_choices']);omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]]);cols=[]
  for i,loc in enumerate(row['local']):
   if i in bysi:
    d,q,g,m,n,r0=bysi[i];qv=q//g;ell=s.Matrix(loc['ell']);beta=s.Matrix(loc['beta']);eta=s.Matrix(loc['eta']);delta=s.eye(4)[:,2];Nm=sum((A[i]**j for j in range(m)),s.zeros(4))
    for c0,u in [(row['b']*g*n//qv,Nm*beta),(-row['b']*r0,Nm*eta),(0,r0*delta+n*ell)]:cols.append(s.Matrix([c0]).col_join(Js[i]*u))
   else:
    F=s.Matrix(loc['fixed']);Fk=s.zeros(6,0)
    if i in original:
     F=s.Matrix(lookup[K,i]['fixed']);Fk=s.Matrix(lookup[K,i]['fibre_kernel'])
    elif addchoices.get(i)=='original' and (K,i) in addlocal:
     c=addlocal[K,i];z=c['z'];F=s.Matrix.hstack(s.eye(4)[:,2],s.Matrix([-z[0],-z[1],0,1]));Fk=ikernel(s.Matrix([c['area_covector']]))
    for j in range(Fk.cols):cols.append(s.Matrix([(omega*Fk[:,j])[0]]).col_join(s.zeros(Js[i].rows,1)))
    for j in range(F.cols):cols.append(s.Matrix([0]).col_join(Js[i]*F[:,j]))
  full=s.Matrix.hstack(*cols);assert group(full)==group(small) and group(small)[0]==0
  S=s.zeros(f+1)
  for i,(_,_,g,m,n,r0) in enumerate(params):S[i,0]=-g*n;S[i,i+1]=m;S[-1,i+1]=1
  zero_euler+=group(S)[0]==1;checks+=1
print('Nonzero-Chern original multiplicative certificates:',len(cert),dict(Counter(c['type'] for c in cert)),flush=True)
print('All additive/multiplicative patterns:',len(patterns),'initial rows:',len(set(key(p) for p in patterns)),flush=True)
print('New full unreduced Smith comparisons:',checks,'torsion caps:',tors_caps,'Euler-zero:',zero_euler,flush=True)
(ROOT/'records/manifolds_original_multiplicative.json').write_text(json.dumps(dict(scope=__doc__,local=cert,patterns=patterns,
 full_Smith_checks=checks,torsion_cap_instances=tors_caps,euler_zero_instances=zero_euler),indent=2,default=int)+'\n')
