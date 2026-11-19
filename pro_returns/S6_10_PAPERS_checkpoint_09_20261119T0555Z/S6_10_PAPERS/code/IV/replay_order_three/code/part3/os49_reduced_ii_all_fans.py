"""Reconstructed K87 certificate; no historical byte-hash claim."""
from pathlib import Path
import sys,json,hashlib
from fractions import Fraction as F
from collections import deque
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'code/part3_root'))
from source_all_fans import mul,inv,edges,word_from_vertical,Q0,Q1,Q2
from scalar_all_fans import bounded_inputs
from os49_all_fans import local,child,check_trace,integer
def seed(n,k,l):
 M=3*k*(6*l+1);A0=3*k*l;a=12*M*(n-1)**2
 V=((a,8*M*(1-n),8*M*(n-1)),(8*M*(1-n),4*M,0),(8*M*(n-1),0,4*M))
 D=(24*A0-a,8*M*(n-1),8*M*(1-n));P=(1,0,n,1)
 check_trace(P,V,D,M)
 return P,V,D,A0-M*(n-1)**2
def calculate(P,k,l,history=False):
 n,word,target=word_from_vertical(P);cur,V,D,S=seed(n,k,l);steps=[];M=3*k*(6*l+1)
 for i in word:
  a,b=V[i][i],D[i];cur,V,D,S=child(cur,V,D,S,i,M)
  if history:steps.append({'edge':i,'target_basis':cur,'old_variation':a,'old_derivative':b,'single_native_right':integer(F(b-a,4)),'double_variation':V,'double_stable_derivative':D,'integer_path_sum':S})
 assert cur==target
 d={'input_basis':P,'canonical_basis':target,'vertical_index':n,'word':word,'k':k,'l':l,'m':3*k,'h':6*l+1,'M':M,'chi':k*(3*l+1),'positive_reference_class':3*k*l,'double_variation':V,'double_stable_derivative':D,'integer_path_sum':S,'physical_class_mod28':S%28}
 if history:d['steps']=steps
 return d
def traverse(k,l,depth=8):
 M=3*k*(6*l+1);P,V,D,S=seed(0,k,l);todo=deque([(P,V,D,S,0)]);seen=set();skipped=0
 while todo:
  P,V,D,S,lev=todo.popleft();key=(P,V,D,S%28)
  if key in seen:continue
  seen.add(key);assert calculate(P,k,l)['physical_class_mod28']==S%28
  if lev==depth:continue
  for i,Q in enumerate((Q0,Q1,Q2)):
   T=mul(P,Q);r=(2,2,0)[i];a,b=V[i][i],2*V[i][i]-D[i];_,_,w,_,I,W=local(T,M);zero=[j for j in range(3) if not w[j]]
   if not zero:
    c=w[r]**2*a-w[r]*I[r];e=w[r]*b-W[r]
    Vn=tuple(tuple(integer((F(I[x],w[x]) if x==y else 0)+F(c,w[x]*w[y])) for y in range(3)) for x in range(3));Dn=tuple(integer(F(W[x]+e,w[x])) for x in range(3))
   elif zero==[r]:
    vs=[[0]*3 for _ in range(3)];ds=[0]*3;vs[r][r]=a;ds[r]=b
    for x in range(3):
     if x!=r:vs[x][x]=integer(F(I[x],w[x]));vs[r][x]=vs[x][r]=integer(F(-I[r],w[x]));ds[x]=integer(F(W[x]-W[r],w[x]))
    Vn=tuple(map(tuple,vs));Dn=tuple(ds)
   else:skipped+=1;continue
   check_trace(T,Vn,Dn,M);todo.append((T,Vn,Dn,S+integer(F(D[i]-V[i][i],4)),lev+1))
 return {'depth':depth,'independent_states':len(seen),'separate_fixed_target_skips':skipped}
def independent_solve(step,M):
 import sympy as s
 P=step['target_basis'];_,_,w,_,I,W=local(P,M)
 vv=s.symbols('v00 v01 v02 v11 v12 v22');dd=s.symbols('d0:3');V=s.Matrix([[vv[0],vv[1],vv[2]],[vv[1],vv[3],vv[4]],[vv[2],vv[4],vv[5]]]);eq=[]
 for j in [1,2]:
  for r in range(3):eq.append(w[j]*V[r,j]-w[0]*V[r,0]-(I[j] if r==j else 0)+(I[0] if r==0 else 0))
  eq.append(w[j]*dd[j]-w[0]*dd[0]-W[j]+W[0])
 eq += [V[2,2]-step['old_variation'],dd[2]-(2*step['old_variation']-step['old_derivative'])]
 sol=list(s.linsolve(eq,(*vv,*dd)));assert len(sol)==1
 a=sol[0];assert not any(x.free_symbols for x in a)
 out=step['double_variation'];expected=(out[0][0],out[0][1],out[0][2],out[1][1],out[1][2],out[2][2],*step['double_stable_derivative'])
 assert tuple(a)==expected
def main():
 inputs=list(bounded_inputs(18));families=[];witnesses={};hom=0;solves=0
 for k,l in [(1,1),(1,2),(2,1),(5,1),(7,2)]:
  fs={}
  for P in inputs:
   v=calculate(P,k,l);e=edges(P)
   if e in fs:assert fs[e]==v['physical_class_mod28']
   fs[e]=v['physical_class_mod28']
   if k==1 and l==1:
    r=v['physical_class_mod28'];C=v['canonical_basis'];score=(max(map(abs,C)),sum(map(abs,C)),len(v['word']),C)
    if r not in witnesses or score<witnesses[r][0]:witnesses[r]=(score,calculate(C,k,l,True))
   if (k,l)!=(1,1):
    ref=calculate(P,1,l);assert v['integer_path_sum']==k*ref['integer_path_sum'];assert v['double_variation']==tuple(tuple(k*x for x in row) for row in ref['double_variation']);assert v['double_stable_derivative']==tuple(k*x for x in ref['double_stable_derivative']);hom+=1
  for n in range(-30,31):assert calculate((1,0,n,1),k,l)['integer_path_sum']==3*k*l-3*k*(6*l+1)*(n-1)**2
  families.append({'k':k,'l':l,'inputs':len(inputs),'fans':len(fs),'observed_residues':sorted(set(fs.values())),'independent':traverse(k,l)})
 assert sorted(witnesses)==list(range(28))
 ws=[witnesses[r][1] for r in range(28)]
 for v in ws:
  for st in v['steps']:independent_solve(st,v['M']);solves+=1
 ex=calculate((2,-1,-1,1),1,1,True);assert ex['integer_path_sum']==-972;assert [x['single_native_right'] for x in ex['steps']]==[-108,-846]
 result={'statement':'P3K.87','status':'PASS; reconstructed certificate, original geometric audits retained','entry_bound':18,'total_unimodular_executions':len(inputs)*5,'families':families,'independent_target_solves':solves,'full_integer_homogeneity_checks':hom,'smallest_family_witnesses':ws,'example':ex,'scope':'Canonical full r-loop only; actual source/root/Cox proof in the reconstructed working note.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS',len(inputs)*5,'executions;',solves,'fresh target solves;',hom,'homogeneity checks')
if __name__=='__main__':main()
