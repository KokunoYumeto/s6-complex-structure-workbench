#!/usr/bin/env python3
"""After-reading entrywise audit of the current printed P1.12 Smith bases."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import combinations
import json,hashlib,math,re
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
AN=ROOT/'analysis/continuation_V_ledger'
paths={
 'cone':AN/'P1_12_old_cone_comparison.output.json',
 'fresh':AN/'P1_12_complement_fresh.output.json',
 'old_export':ROOT/'code/V/replay/code/part1/complement_export.json',
 'old_bases':ROOT/'code/V/replay/code/part1/complement_kernel_check.json',
 'known_collapse':ROOT/'code/V/replay/code/part1/cusp_marked_collapse.json'}
data={k:json.loads(p.read_text())for k,p in paths.items()}
cc=data['cone']['certificates'];fc=data['fresh']['certificates'];oe=data['old_export'];ob=data['old_bases'];cm=data['known_collapse']
packet=(ROOT/'analysis/continuation_root/P1_12_complement_clean_assertions_packet.md').read_text()
inp=json.loads(re.search(r'```json\s*(.*?)```',packet,re.S).group(1))
M=[S.Matrix(inp['M1']),S.Matrix(inp['M2'])];U0=(M[0]*M[1]).inv();Smark=S.Matrix(inp['cusp_marking_S'])
def dim(n,k):return math.comb(n,k) if 0<=k<=n else 0
def ext(A,k):
 if not 0<=k<=A.rows:return S.zeros(0,0)
 ids=list(combinations(range(A.rows),k))
 return S.Matrix([[A.extract(i,j).det()for j in ids]for i in ids])
def mat(v,m=None,n=None):
 if m==0 or n==0:return S.zeros(m,n)
 return S.Matrix(v)
def ints(A):return [[int(x)for x in row]for row in A.tolist()]
checks=[];cert={}
def check(name,ok):
 checks.append({'name':name,'pass':bool(ok)})
 if not ok:raise AssertionError(name)
printed1=S.Matrix([[20,1,0,0],[1,0,-1,-1],[1,0,0,0],[0,0,2,1]])
printed2=S.Matrix([[0,0,1,-1,0,-1,0,0,0],[0,0,1,0,0,-1,0,1,0],[0,0,1,-1,0,-2,0,1,0],[0,0,0,0,-1,-1,0,0,-1],[1,1,-1,0,0,1,1,0,0],[1,2,0,0,1,0,0,0,0],[-1,-1,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,0,-1,0,0,0]])
printed3=S.Matrix([[0,1,0,1,0,0,0,0,0,1],[0,1,-1,0,0,0,-1,0,-1,0],[0,0,0,0,0,0,1,0,1,0],[0,0,0,-1,1,-1,0,-1,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,1,0,0],[0,0,1,0,1,-2,1,-1,2,0],[0,1,0,-1,1,-2,0,-1,0,0]])
for k in range(9):
 n=dim(6,k);p=dim(6,k-1);s=str(k)
 own_bd=mat(fc['chains']['dB'][s],dim(6,k-1)+dim(6,k-2),n+p)
 old_bd=mat(oe['boundary_differentials'][s],own_bd.rows,own_bd.cols)
 check(f'export:boundary_differential_degree{k}',old_bd==own_bd)
 own_j=mat(cc[s]['old_boundary_inclusion']);old_j=mat(oe['boundary_to_Y'][s])
 check(f'export:boundary_inclusion_degree{k}',old_j==own_j)
 check(f'export:chain_rank_degree{k}',oe['dimensions'][s]==own_j.rows)
 if k:
  check(f'export:full_differential_degree{k}',mat(oe['differentials'][s])==mat(cc[s]['old_differential']))
 for i in range(2):
  v=S.Matrix(inp[f'v{i+1}']);eps=int(v[0]);P=(eps*v).row_join(S.zeros(1,5).col_join(S.eye(5)));R=M[i][1:,1:]
  ids=list(combinations(range(6),k))if k<=6 else [];prev=list(combinations(range(6),k-1))if 0<=k-1<=6 else []
  nv=dim(5,k);nh=dim(5,k-1);f=S.zeros(n,n);h=S.zeros(n,p)
  if n:
   L=ext(P.inv(),k);vert=[j for j,I in enumerate(ids)if 0 not in I];horiz=[j for j,I in enumerate(ids)if 0 in I]
   f[:nv,:]=L[vert,:]
   if nh:f[nv:,:]=eps*sum((ext(R,k-1)**j for j in range(inp[f'm{i+1}'])),S.zeros(nh,nh))*L[horiz,:]
  if nh:h[nv:,:]=ext(P.inv(),k-1)[[j for j,I in enumerate(prev)if 0 not in I],:]
  check(f'export:finite_cap{i+1}_degree{k}',mat(oe['finite_boundary_to_cap'][f'{i+1}.{k}'],n,n+p)==f.row_join(h))
  main=S.zeros(n+2*p,n+p);main[:n,:n]=S.eye(n);main[n+i*p:n+(i+1)*p,n:]=S.eye(p)
  check(f'export:finite_main{i+1}_degree{k}',mat(oe['finite_boundary_to_main'][f'{i+1}.{k}'],n+2*p,n+p)==main)
 oldh=oe['homology'][s]
 if k<8:
  check(f'export:homology_degree{k}',oldh['free']==data['fresh']['Y_homology'][s]['rank'] and oldh['torsion']==data['fresh']['Y_homology'][s]['torsion'])
 else:check('export:homology_degree8',oldh['free']==0 and oldh['torsion']==[])

for k in [1,2,3]:
 s=str(k);n=dim(6,k);p=dim(6,k-1);nt=1 if k==3 else 0
 d=mat(cc[s]['old_differential']);dn=mat(cc[str(k+1)]['old_differential'])
 db=mat(fc['chains']['dB'][s]);dbn=mat(fc['chains']['dB'][str(k+1)])
 T=mat(cc[s]['comparison_to_frozen_physical_model']);gamma=mat(cc[s]['boundary_fibre_antipode'])
 jold=mat(cc[s]['old_boundary_inclusion']);jf=mat(fc['chains']['boundary_inclusion'][s])
 yz=mat(ob[s]['Ycycles']);yp=mat(ob[s]['Yprojection']);bz=mat(ob[s]['Bcycles']);bp=mat(ob[s]['Bprojection']);br=mat(ob[s]['Brelations'])
 ypf=mat(fc[f'Y{k}:homology']['projection']);bpf=mat(fc[f'B{k}:homology']['projection'])
 check(f'bases{k}:Y_cycles',d*yz==S.zeros(d.rows,yz.cols))
 check(f'bases{k}:Y_projection_inverse',yp*yz==S.eye(yz.cols))
 check(f'bases{k}:Y_projection_kills_boundaries',yp*dn==S.zeros(yp.rows,dn.cols))
 uy=ypf*T*yz
 check(f'bases{k}:Y_basis_transport_unimodular',abs(uy.det())==1)
 check(f'bases{k}:B_cycles',db*bz==S.zeros(db.rows,bz.cols))
 check(f'bases{k}:B_projection_inverse',bp*bz==S.eye(bz.cols))
 ub=bpf*gamma*bz
 check(f'bases{k}:B_free_basis_transport_unimodular',abs(ub[nt:,nt:].det())==1)
 check(f'bases{k}:B_torsion_free_block',ub[nt:,:nt]==S.zeros(ub.rows-nt,nt))
 if nt:check(f'bases{k}:B_torsion_unit_mod2',ub[0,0]%2==1 and br[0,0]==2)
 j=yp*jold*bz
 check(f'bases{k}:stored_boundary_map',j==mat(ob[s]['BtoY']))
 check(f'bases{k}:boundary_map_transports',uy*j==ypf*jf*gamma*bz)
 kc=mat(ob[s]['kernel_cycles']);kr=mat(ob[s]['kernel_relations']);cs=mat(ob[s]['collapse_on_kernel'])
 check(f'bases{k}:kernel_cycles',db*kc==S.zeros(db.rows,kc.cols))
 check(f'bases{k}:kernel_maps_zero',yp*jold*kc==S.zeros(yp.rows,kc.cols))
 qold=mat(cm[s])*ext(Smark.inv(),k)
 collapse_snf=fc[f'collapse{k}:saturated_image'];left=mat(collapse_snf['left']);diag=mat(collapse_snf['diagonal']);rank=sum(diag[i,i]!=0 for i in range(min(diag.shape)))
 qfresh=left[rank:,:];right=left.inv()[:,rank:];uc=qold*right
 check(f'bases{k}:actual_collapse_target_basis_transport',qold==uc*qfresh)
 check(f'bases{k}:collapse_target_unimodular',all(z.q==1 for z in uc)and abs(uc.det())==1)
 check(f'bases{k}:stored_collapse_on_kernel',qold*kc[:n,:]==cs)
 if k>=2:
  check(f'bases{k}:vertical_kernel_exact',kc[n:,:]==S.zeros(p,kc.cols) and mat(ob[s]['kernel_suspension'])==S.zeros(p,kc.cols))
  kf=mat(fc['low_degree_maps'][s]['kernel_HB_coordinates']);kf_old=bpf*gamma*kc
  uk,params=kf.gauss_jordan_solve(kf_old)
  check(f'bases{k}:kernel_transport_integral_unique',params.rows==0 and all(z.q==1 for z in uk))
  check(f'bases{k}:kernel_free_transport_unimodular',abs(uk[nt:,nt:].det())==1)
  check(f'bases{k}:kernel_torsion_free_block',uk[nt:,:nt]==S.zeros(uk.rows-nt,nt))
  if nt:check(f'bases{k}:kernel_torsion_unit_mod2',uk[0,0]%2==1 and kr[0,0]==2)
  cf=mat(fc['low_degree_maps'][s]['collapse_on_kernel'])
  check(f'bases{k}:entire_collapse_diagram',cs==(-1)**k*uc*cf*uk)
  check(f'bases{k}:printed_matrix_entrywise',cs==({2:printed2,3:printed3}[k]))
  check(f'bases{k}:printed_free_determinant',cs[:,nt:].det()==1)
  if nt:check(f'bases{k}:printed_torsion_column_zero',cs[:,:nt]==S.zeros(cs.rows,nt))
  cert[s]={'Y_basis_transport':ints(uy),'B_basis_transport':ints(ub),'kernel_basis_transport':ints(uk),'collapse_target_basis_transport':ints(uc),'verified_printed_matrix':ints(cs)}
 else:
  combined=j.col_join(qold*bz[:n,:])
  check('bases1:combined_printed_entrywise',combined==printed1==mat(ob[s]['combined_map']))
  check('bases1:combined_determinant',combined.det()==1)
  cf=mat(fc['low_degree_maps']['1']['combined_cusp_map'])
  target_transport=S.diag(uy,-uc.inv())
  # The free Y and C basis changes are both explicit; compare directly.
  check('bases1:combined_actual_diagram',S.diag(uy,-uc.inv())*combined==cf*ub)
  cert[s]={'Y_basis_transport':ints(uy),'B_basis_transport':ints(ub),'collapse_target_basis_transport':ints(uc),'verified_printed_matrix':ints(combined)}

out={'completed_at':datetime.now(timezone.utc).isoformat(),'scope':'After-reading producer-basis comparison, following independent pre-read 444-check derivation and exact cone deformation retraction. All printed entries and integral kernel bases compared; no use of unproved higher cusp suspension map.','source_files':{k:{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for k,p in paths.items()},'pass':all(c['pass']for c in checks),'check_count':len(checks),'checks':checks,'certificates':cert,'old_export_description_note':'The old complement_export.json description string refers to a periodic Kuhn central-fibre export; its differential, attaching-map, dimension and homology payloads have separately been verified entrywise against the printed complement model. The incorrect description does not supply mathematical evidence.'}
p=AN/'P1_12_printed_basis_comparison.output.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'pass':out['pass'],'check_count':len(checks),'output':str(p)},indent=2))
