"""All finite additive cap positions on the natural sphere-candidate catalogue.
Adds all34 nonprimitive-gamma positions to the68 treated in D.2.29.
All arithmetic and homology formulas are proved without multiplicity bounds.
"""
from pathlib import Path
import json,itertools,sympy as s
from math import gcd,prod
from collections import Counter
from manifolds_rankone_families import decomp,ikernel,wedge,biv
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'manifolds_sphere_normal_lattices.json').read_text())['rows']
monos=json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
mono={key(r):r for r in monos}
orders={'II':(6,1),'III':(4,2),'IV':(3,3),'III*':(4,2),'IV*':(3,3)}

def group(M):
 D,U,V,r=decomp(M);return M.rows-r,[int(abs(D[j,j])) for j in range(r) if abs(D[j,j])>1]

def free(d,q,g,m,n,r):
 t=gcd(m,g*n,(q//g)*r)
 return gcd(m,n,r)==1 and (m//t)%d==0

def matrix(b,finite,e=0):
 f=len(finite);cs=[];glob=s.zeros(1+2*f,1);glob[0]=b*e
 for i in range(f):glob[1+2*i]=1
 cs.append(glob)
 for i,(d,q,g,m,n,r) in enumerate(finite):
  qv=q//g;assert free(d,q,g,m,n,r)
  for a0,ad,al in [(b*g*n//qv,m//qv,0),(-b*r,0,m//g),(0,r,n)]:
   c=s.zeros(1+2*f,1);c[0]=a0;c[1+2*i]=ad;c[2+2*i]=al;cs.append(c)
 return s.Matrix.hstack(*cs)

out=[];new_positions=0;power_checks=0
for row in rows:
 rec={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']};rec['local']=[]
 for j,loc in enumerate(row['local']):
  v=dict(loc);A=s.Matrix(mono[key(row)]['local'][j]['matrix'])
  if loc['type'] in orders:
   d,q=orders[loc['type']];F=ikernel(A-s.eye(4));g=gcd(*map(int,list(F[3,:])))
   assert g in (1,q)
   assert group(A-s.eye(4))==(2,[]) and group(wedge(A)-s.eye(6))==(2,[])
   if g>1:
    N=sum((A**i for i in range(d)),s.zeros(4));delta=s.eye(4)[:,2];eta=s.eye(4)[:,3]
    ell=s.Rational(q,d)*N*eta;assert all(x.q==1 for x in ell)
    G=s.Matrix.hstack(delta,ell);L=(F.T*F).inv()*F.T;assert abs((L*G).det())==1
    D,U,V,rk=decomp(A-s.eye(4));C=U[rk:,:]
    assert abs((C*s.Matrix.hstack(delta,eta)).det())==1
    assert C*ell==q*C*eta and N*eta==(d//q)*ell
    omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]])
    assert (omega*biv(delta,ell))[0]==-row['b']*q
    assert (omega*biv(eta,ell))[0]==0 and (omega*biv(eta,delta))[0]==row['b']
    v.update(log_order=d,delta_index=1,ell=ell.tolist(),beta=delta.tolist(),eta=eta.tolist())
    tests=[]
    for i in range(d):
     Z=ikernel((A**i-s.eye(4)).T).T
     tests.append([(int((Z*ell)[h]),int((Z*delta)[h])) for h in range(Z.rows)])
    for k in range(1,7):
     m=d*k
     for n in range(m):
      for r0 in range(m):
       actual=not any(all((i*(ln*n+lr*r0))%m==0 for ln,lr in tests[i%d]) for i in range(1,m))
       assert actual==free(d,q,g,m,n,r0)
       power_checks+=1
    new_positions+=1
   else:v['eta']=v['ell']
   v.update(q=q,gamma_index=g,vertical_index=q//g)
  rec['local'].append(v)
 out.append(rec)
assert new_positions==34
print('New nonprimitive-gamma positions:',new_positions,'exact affine-power checks:',power_checks,flush=True)

patterns=[];cache={};full_checks=0;torsion_cases=0;one_log_checks=0
for row in out:
 if any(v['type'].startswith('I') and v['type'].endswith('*') and v['type'][1:-1].isdigit() for v in row['local']):continue
 A=[s.Matrix(v['matrix']) for v in mono[key(row)]['local']];N=len(A)
 aa=[i for i,v in enumerate(row['local']) if v['type'] in orders]
 choices=[]
 for i in aa:
  opts=['log']
  if row['local'][i]['original_minimal']:opts.append('original')
  choices.append(opts)
 D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:-1]]);Sd,Ud,Vd,rd=decomp(D);Wi=Vd.inv()[rd:,:]
 def ji(i,x):
  if i<N-1:
   y=s.zeros(4*(N-1),x.cols);y[4*i:4*i+4,:]=x;return y
  oo=[]
  for h in range(N-1):
   p=s.eye(4)
   for z in A[h+1:N-1]:p=p*z
   oo.append(-p*x)
  return s.Matrix.vstack(*oo)
 Js=[Wi*ji(i,s.eye(4)) for i in range(N)]
 for cc in itertools.product(*choices):
  fi=[i for i,c in zip(aa,cc) if c=='log']
  pat={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']}
  pat.update(additive_choices=list(zip(aa,cc)),finite_indices=fi,
             finite_types=[row['local'][i]['type'] for i in fi],
             gamma_indices=[row['local'][i]['gamma_index'] for i in fi])
  patterns.append(pat)
  bad=[j for j,i in enumerate(fi) if row['local'][i]['gamma_index']>1]
  for target in bad:
   for case in range(5):
    params=[]
    for j,i in enumerate(fi):
     loc=row['local'][i];d=loc['log_order'];q=loc['q'];g=loc['gamma_index']
     m,n,r0=(d,1,0) if g==1 else (d,1,1)
     if j==target:m,n,r0=[(d,0,1),(d,1,1),(d*q,1,0),(2*d,2,1),(3*d,3,1)][case]
     assert free(d,q,g,m,n,r0);params.append((d,q,g,m,n,r0))
    slot={i:p for i,p in zip(fi,params)};cs=[]
    for i,loc in enumerate(row['local']):
     if i not in slot:
      F=s.Matrix(loc['fixed']);M=Js[i]*F
      for h in range(M.cols):cs.append(s.Matrix([0]).col_join(M[:,h]))
     else:
      d,q,g,m,n,r0=slot[i];qv=q//g;delta=s.eye(4)[:,2];ell=s.Matrix(loc['ell']);beta=s.Matrix(loc['beta']);eta=s.Matrix(loc['eta'])
      Nm=sum((A[i]**h for h in range(m)),s.zeros(4))
      assert Nm*beta==(m//qv)*delta and Nm*eta==(m//g)*ell
      for c0,u in [(row['b']*g*n//qv,Nm*beta),(-row['b']*r0,Nm*eta),(0,r0*delta+n*ell)]:
       cs.append(s.Matrix([c0]).col_join(Js[i]*u))
      torsion_cases+=gcd(m,g*n,qv*r0)>1
    full=s.Matrix.hstack(*cs);small=matrix(row['b'],params)
    assert group(full)==group(small),(key(row),params,group(full),group(small))
    S=s.zeros(len(params)+1)
    for h,(_,_,g,m,n,r0) in enumerate(params):S[h,0]=-g*n;S[h,h+1]=m;S[-1,h+1]=1
    assert group(S)[0]==group(small)[0]
    full_checks+=1
    # Closed one-finite-log formula, retaining arbitrary integer clutch e.
    if len(params)==1:
     d,q,g,m,n,r0=params[0];t=gcd(m,g*n,(q//g)*r0)
     for e in [-2,-1,0,1,2]:
      nn=n-(m//g)*e;actual=group(matrix(row['b'],params,e))
      if nn:
       h=gcd(row['b'],m//g,nn);want=(0,[z for z in [h,row['b']*g*abs(nn)*t//(q*h)] if z>1])
      else:want=(1,[z for z in [gcd(row['b'],m//g)] if z>1])
      assert actual==want,(key(row),params,e,actual,want)
      one_log_checks+=1
print('All nonstar minimal original/log patterns:',len(patterns),'on',len(set(key(p) for p in patterns)),'initial rows',flush=True)
print('New full unreduced Smith comparisons:',full_checks,'torsion-cap instances:',torsion_cases,flush=True)
print('Closed one-finite-log Smith formula checks:',one_log_checks,flush=True)
record=dict(scope=__doc__,rows=out,all_nonstar_patterns=patterns,new_finite_positions=new_positions,
            exact_power_checks=power_checks,full_Smith_checks=full_checks,
            torsion_cap_instances=torsion_cases,one_log_formula_checks=one_log_checks)
(ROOT/'manifolds_all_finite_logs.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
