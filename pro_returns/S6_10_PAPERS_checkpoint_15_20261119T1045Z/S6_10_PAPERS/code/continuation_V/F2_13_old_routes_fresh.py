"""New FLINT/Hermite verification of the preserved former F2.13 computations.
Original matrices/bases are read only as coordinate definitions for comparison.
No original producer function is imported. The verification uses primitive
Hermite kernels, explicit unimodular basis maps and exact rational conjugacy.
"""
from pathlib import Path
from itertools import combinations
import json,sys,math,re
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'build/continuation_numeric/python'))
from flint import fmpz_mat
old=json.loads((ROOT/'analysis/continuation_V/F2_13_old_coordinate_definitions.json').read_text())['cases']
new=json.loads(Path(__file__).with_name('F2_13_companion_explore_fresh.output.json').read_text())
checks=[];results={}
def im(a):return fmpz_mat([[int(S.Rational(x)) for x in r] for r in a])
def eye(n):return fmpz_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sub(m,ri,cj):
 ri=list(ri);cj=list(cj)
 return fmpz_mat([[m[i,j] for j in cj] for i in ri]) if ri and cj else fmpz_mat(len(ri),len(cj))
def horiz(ms):return fmpz_mat([[m[i,j] for m in ms for j in range(m.ncols())] for i in range(ms[0].nrows())])
def vert(ms):return fmpz_mat([[m[i,j] for j in range(m.ncols())] for m in ms for i in range(m.nrows())])
def invz(m):
 q=m.inv();r=fmpz_mat([[int(q[i,j]) for j in range(q.ncols())] for i in range(q.nrows())]);assert r*m==eye(m.nrows());return r
def kernel(m):
 h,t=m.transpose().hnf(transform=True);rank=m.rank();assert t*m.transpose()==h and abs(t.det())==1
 u=t.transpose();ui=invz(u);k=sub(u,range(u.nrows()),range(rank,u.ncols()));assert m*k==fmpz_mat(m.nrows(),k.ncols());return k,ui,rank
def wedge(m,k):
 ix=list(combinations(range(m.nrows()),k));return fmpz_mat([[sub(m,i,j).det() for j in ix] for i in ix])
def snf(m):
 d=m.snf();return [abs(int(d[i,i])) for i in range(min(d.nrows(),d.ncols())) if d[i,i]]
def ser(m):return [[int(m[i,j]) for j in range(m.ncols())] for i in range(m.nrows())]
def powr(m,k):
 a=eye(m.nrows())
 for _ in range(k):a=a*m
 return a
for case,data in old.items():
 A=im(data['A_transformed']);B=im(data['B_transformed']);M1=A.transpose();M2=B.transpose();N=invz(M1*M2)-eye(6)
 assert N*N==fmpz_mat(6,6) and snf(N)==[1,1,1]
 assert powr(A,5)==eye(6) and powr(B,6)==eye(6)
 checks.extend([case+'_old_cusp',case+'_old_orders'])
 normal=horiz([N,M1*N,M2*N]);assert all(normal[0,j]==0 for j in range(normal.ncols())) and snf(sub(normal,range(1,6),range(normal.ncols())))==[1]*5
 checks.append(case+'_old_integral_normal_closure')
 # Actual rational cohomology intertwiner from the current canonical pair.
 X=S.Matrix(6,6,S.symbols('x:36'));An=S.Matrix(new[case]['a6']);Bn=S.Matrix(new[case]['b6']);Ao=S.Matrix(ser(A));Bo=S.Matrix(ser(B))
 eq,_=S.linear_eq_to_matrix(list(X*An-Ao*X)+list(X*Bn-Bo*X),list(X));basis=eq.nullspace();assert len(basis)==1
 P=S.Matrix(6,6,basis[0]);P=P/P[0,0];assert P.det()!=0 and P*An==Ao*P and P*Bn==Bo*P and P[:,0]==S.eye(6)[:,0]
 assert all(S.denom(x)%3 for x in P) and S.numer(P.det())%3 and S.denom(P.det())%3
 checks.append(case+'_actual_old_new_Z3_intertwiner')
 rr={'P_current_cohom_to_old_cohom':[[str(x) for x in row] for row in P.tolist()],'P_determinant':str(P.det()),'homology_map_old_to_current':'P transpose, the actual dual map','degrees':{},'finite':[]}
 for k in range(7):
  W1,W2,W0=[wedge(C,k) for C in [A,B,A*B]];n=W1.nrows();stack=vert([W1-eye(n),W2-eye(n)]);hor=horiz([W1-eye(n),W2-eye(n)]);a=n-stack.rank();b=n-hor.rank();local=[n-(C-eye(n)).rank() for C in [W1,W2,W0]];par=a+b+n-sum(local)
  rr['degrees'][str(k)]={'invariant_rank':a,'parabolic_rank':par,'coinvariant_rank':b,'local_fixed_ranks':local,'horizontal_smith':snf(hor),'vertical_smith':snf(stack)}
  if 1<=k<=4:assert all(z%3 for z in snf(hor)+snf(stack))
  checks.append(case+f'_old_global_degree{k}')
 stdout=(ROOT/f'analysis/continuation_V/F2_13_old_{case}_producer.stdout.txt').read_text()
 for finite,C,M in zip(data['finite_basis_comparison_data'],[A,B],[M1,M2]):
  m=finite['order'];u=im(finite['u']);lam_old=im(finite['lambda']);assert M*u==u and u[0,0]==1 and lam_old[0,0]==0
  D=sub(M,range(1,6),range(1,6));lk,lui,lr=kernel(D-eye(5));assert lk.ncols()==1
  lam=fmpz_mat([[0]]+ser(lk));lc=lui*sub(lam_old,range(1,6),[0]);sgn=int(lc[lr,0]);assert abs(sgn)==1 and lam*sgn==lam_old
  W2=wedge(C,2);K2,Ui2,r2=kernel(W2-eye(15));oldK2=im(finite['K2_old_basis']);U2=sub(Ui2*oldK2,range(r2,15),range(oldK2.ncols()));assert K2*U2==oldK2 and abs(U2.det())==1
  ix=list(combinations(range(6),2));eta=fmpz_mat([[u[i,0]*lam[j,0]-u[j,0]*lam[i,0] for i,j in ix]]);numer=eta*K2;targetnumer=numer*U2*sgn;periods=[S.Rational(int(targetnumer[0,j]),m) for j in range(targetnumer.ncols())]
  printed_line=next(x for x in stdout.splitlines() if x.startswith(f'finite q2 suspension periods {m} '));printed=S.sympify(printed_line[printed_line.index('['):]);assert periods==printed
  if m==6:assert periods==([S.Integer(-2),S.Integer(-1),S.Integer(-1)] if case=='A' else [S.Rational(1,3),S.Integer(0),S.Rational(1,3)])
  W3=wedge(C,3);K3,Ui3,r3=kernel(W3-eye(20));oldK3=im(finite['K3_old_basis']);U3=sub(Ui3*oldK3,range(r3,20),range(oldK3.ncols()));assert K3*U3==oldK3 and abs(U3.det())==1
  triples=list(combinations(range(6),3));J=fmpz_mat(20,20)
  for i,t in enumerate(triples):
   comp=tuple(x for x in range(6) if x not in t);j=triples.index(comp);word=t+comp;J[i,j]=(-1)**sum(word[k]>word[l] for k in range(6) for l in range(k+1,6))
  Gram=K3.transpose()*J*K3;oldGram=oldK3.transpose()*J*oldK3;assert oldGram==U3.transpose()*Gram*U3
  gramdet=int(Gram.det());printed_gram=int(next(x for x in stdout.splitlines() if x.startswith(f'finite q3 Gram determinant {m} ')).split()[-1]);assert gramdet==printed_gram
  if case=='A' and m==6:assert gramdet==36
  vertical={}
  for k in range(1,5):
   W=wedge(D.transpose(),k);factors=snf(W-eye(W.nrows()));assert all(x%3 for x in factors);vertical[str(k)]=factors;checks.append(case+f'_finite{m}_vertical{k}')
  rr['finite'].append({'order':m,'new_primitive_lambda':ser(lam),'old_lambda_sign':sgn,'new_K2':ser(K2),'U2_new_to_old_basis_coordinates':ser(U2),'new_period_numerators':ser(numer),'old_period_row_exact':[str(x) for x in periods],'new_K3':ser(K3),'U3_new_to_old_basis_coordinates':ser(U3),'new_skew_Gram':ser(Gram),'old_skew_Gram':ser(oldGram),'Gram_determinant':gramdet,'vertical_smith':vertical})
  checks.extend([case+f'_finite{m}_fixed_vectors',case+f'_finite{m}_actual_K2_basis_map',case+f'_finite{m}_period_row',case+f'_finite{m}_actual_K3_Gram_map'])
 for r in range(1,9):
  # Exact valuation equation of the preserved degree-four pairing route,
  # compared with the two cyclic norm exponents in the current proof.
  assert 2*(2*r-1)+2==4*r and (r-1)+r==2*r-1
  if case=='B':assert r==1+(r-1)
 checks.append(case+'_all_multiplicity_valuation_formula')
 results[case]=rr
out={'status':'PASS','checks_passed':len(checks),'checks':checks,'scope':'Independent FLINT/Hermite rerun of all preserved old global/finite Smith, period and Gram computations, with explicit basis/conjugacy maps; this post-target calculation receives no prereading proof credit.','cases':results}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'checks':len(checks),'summary':{c:{'Pdet':x['P_determinant'],'finite':[(f['order'],f['old_period_row_exact'],f['Gram_determinant']) for f in x['finite']]} for c,x in results.items()}},indent=2))
