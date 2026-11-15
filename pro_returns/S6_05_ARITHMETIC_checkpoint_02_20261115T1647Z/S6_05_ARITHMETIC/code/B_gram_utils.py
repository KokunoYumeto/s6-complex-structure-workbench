"""Exact utilities for arbitrary integral positive-definite Gram matrices."""
from fractions import Fraction as F
from pathlib import Path
import json,subprocess
from flint import fmpz_mat,fmpq_mat
ROOT=Path(__file__).resolve().parents[1]
def matrows(a):return [[int(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]
def qrows(a):return [[F(str(a[i,j])) for j in range(a.ncols())] for i in range(a.nrows())]
def qmat(a):return fmpq_mat([[str(x) for x in row] for row in a])
def hnf(a):
 h=fmpz_mat(a).hnf();return [row for row in matrows(h) if any(row)]
def enum_input(g,bound,path,store=True):
 n=len(g);d=[];mi=[1];u=[[F(int(i==j)) for j in range(n)] for i in range(n)]
 for i in range(n):
  v=F(g[i][i])-sum(d[k]*u[k][i]**2 for k in range(i));assert v>0;d.append(v)
  m=mi[-1]*v;assert m.denominator==1;mi.append(int(m))
  for j in range(i+1,n):u[i][j]=(F(g[i][j])-sum(d[k]*u[k][i]*u[k][j] for k in range(i)))/v
 mm=[]
 for i in range(n):
  row=[]
  for j in range(n):
   x=u[i][j]*mi[i+1];assert x.denominator==1;row.append(int(x))
  mm.append(row)
 assert max(mi)<2**60 and max(abs(x) for row in mm for x in row)<2**60
 s=f'{n} {bound} {int(store)}\n'+' '.join(map(str,mi))+'\n'+'\n'.join(' '.join(map(str,row)) for row in mm)+'\n'
 path.write_text(s)
def enumerate_gram(g,bound,prefix):
 G=fmpz_mat(g);Q,T=G.lll(transform=True,rep='gram',gram='exact')
 assert T.det() in (-1,1) and T*G*T.transpose()==Q
 gg=matrows(Q);tt=matrows(T);prefix=Path(prefix);ip=prefix.with_suffix('.enum');op=prefix.with_suffix('.out')
 enum_input(gg,bound,ip)
 with ip.open() as a,op.open('w') as b:subprocess.run([str(ROOT/'code'/'B_enumerate')],stdin=a,stdout=b,check=True)
 vv=[]
 for line in op.read_text().splitlines():
  ss=line.split()
  if ss and ss[0]=='vector':
   norm=int(ss[1]);v=list(map(int,ss[2:]));w=[sum(v[i]*tt[i][j] for i in range(len(v))) for j in range(len(v))]
   assert sum(w[i]*g[i][j]*w[j] for i in range(len(v)) for j in range(len(v)))==norm
   vv.append((norm,w))
 return vv
def root_system(g,roots):
 if not roots:return 'Leech'
 n=len(roots);R=fmpz_mat(roots);A=R*fmpz_mat(g)*R.transpose();seen=set();out=[]
 for i in range(n):
  if i in seen:continue
  comp=set([i]);todo=[i]
  while todo:
   u=todo.pop()
   for v in range(n):
    if v not in comp and A[u,v]:comp.add(v);todo.append(v)
  seen|=comp;rk=fmpz_mat([roots[j] for j in comp]).rank();nr=len(comp)
  if nr==rk*(rk+1):name=f'A{rk}'
  elif rk>=4 and nr==2*rk*(rk-1):name=f'D{rk}'
  elif (rk,nr) in [(6,72),(7,126),(8,240)]:name=f'E{rk}'
  else:raise AssertionError((rk,nr))
  out.append(name)
 from collections import Counter
 return '+'.join((f'{v}' if v>1 else '')+k for k,v in sorted(Counter(out).items()))
