"""Assemble all 129 classes in ONE explicit Leech lattice; recompute mass.

The source Leech Gram matrix is B_standard_Leech_basis.json.  Exact
isometries to the A1- and A2-marked models are constructed from roots,
glue codes, and the intersection functional, and checked over Q.
"""
from B_global_lattice import *
from B_A2_fusion import mark_isometry,MODEL as A2
from B_A1_fusion import markA1,MODEL as A1
from collections import Counter
import csv

CO0=8315553613086720000
LB=qmat(json.loads((REC/'B_standard_Leech_basis.json').read_text())['basis']);LI=LB.inv();G=LB*LB.transpose()/8
I=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
STD=object.__new__(PlaneModel);STD.G=G;STD.L=I;STD.Li=I
assert not enumerate_gram(ints(G),2,REC/'B_standard_Leech_no_roots')
def unpack(a):return [((a>>i)&1)+2*((a>>(24+i))&1) for i in range(24)]
def mod3(A):return np.array([[x.numerator*pow(x.denominator,-1,3)%3 for x in row] for row in qrows(A)],dtype=np.int64)
def neighbour(packed,name):
 v=qmat([mod3(qmat([unpack(packed)])*LI)[0].tolist()]);pair=ints(I*G*v.transpose());j=next(j for j,x in enumerate(pair) if x[0]%3)
 q=F(str((v*G*v.transpose())[0,0]))/2;assert q.denominator==1 and int(q)%3==0
 k=-(int(q)//3)*pow(pair[j][0],-1,3)%3
 z=fmpq_mat(v);z[0,j]+=3*k;assert F(str((z*G*z.transpose())[0,0]))%18==0
 K=congruence_kernel([x[0] for x in pair]);N=span(qrows(K)+qrows(z/3));NG=ints(N*G*N.transpose());assert fmpz_mat(NG).det()==1
 roots=[r for norm,r in enumerate_gram(NG,2,REC/f'B_standard_{name}_neighbor') if norm==2]
 rs=root_system(NG,roots);assert rs=={'A2':'12A2','A1':'24A1'}[name]
 return {'basis':qjson(N),'roots':roots,'root_system':rs}

T2=mark_isometry(neighbour(0xeee000,'A2'),STD)
T1=markA1(neighbour(0x111111,'A1'),STD)
for name,T,M in [('A2',T2,A2),('A1',T1,A1)]:
 assert T*M.G*T.transpose()==G and span(qrows(T))==span(qrows(M.L))
 print('Verified exact standard-Leech to',name,'marked-Leech isometry.',flush=True)
(REC/'B_global_model_isometries.json').write_text(json.dumps({'standard_Gram':ints(G),'standard_to_A2_N_coordinates':qjson(T2),'standard_to_A1_N_coordinates':qjson(T1)}))

rows=json.loads((REC/'B_rooted_plane_orbits.json').read_text())
rare=json.loads((REC/'B_rare_plane_orbits.json').read_text())['orbits']
for r in rows:
 name=r['type'];s,o=r['representative'];dat=json.loads((REC/f'B_{name}_flags'/f'{s}_{o}.json').read_text());M,T=(A2,T2) if name=='A2' else (A1,T1)
 P=qmat(qrows(M.v)+[dat['y']])*T.inv();p=mod3(P);p,_=rr(p);assert p.shape==(2,24) and np.array_equal(p@mod3(G)@p.T%3,np.zeros((2,2),dtype=np.int64))
 r['plane_basis_standard_mod3']=p.tolist();r['representative_record']=f'B_{name}_flags/{s}_{o}.json';r['eight_extensions']=[e['root_system'] for e in dat['extensions']]
 r['generator_recipe']='B_plane_stabilizer_recipe.py: rooted marked-neighbor Schreier method'
for i,r in enumerate(rare):
 dat=json.loads((REC/f'B_rare_plane_{i+1}.json').read_text());p,_=rr([dat['v'],[int(F(x)) for x in dat['y']]])
 rows.append({'type':r['line_type'],'representative':r['representative'],'stabilizer_order':r['stabilizer_order'],'plane_orbit_size':r['plane_orbit_size'],'extensions':{'Leech':8},'opposite':['Leech']*4,'flag_orbits':r['flag_ids'],'plane_basis_standard_mod3':p.tolist(),'representative_record':f'B_rare_plane_{i+1}.json','eight_extensions':['Leech']*8,'generator_recipe':'B_rare_plane_groups.py: stored rare-orbit Schreier trees'})
assert len(rows)==129
for i,r in enumerate(rows):
 r['orbit_id']=i+1;r['full_group_record']=f'B_plane_groups/{i+1:03d}.json';assert len(r['eight_extensions'])==8 and Counter(r['eight_extensions'])==r['extensions'];assert CO0//r['stabilizer_order']==r['plane_orbit_size'] and CO0%r['stabilizer_order']==0

# Count the entire split-orthogonal Grassmannian directly, independently
# of all orbit and stratum enumeration outputs.
points=(3**11+1)*(3**12-1)//2
quotient_points=(3**10+1)*(3**11-1)//2
assert points*quotient_points%4==0
TOTAL=points*quotient_points//4
covered=sum(r['plane_orbit_size'] for r in rows)
mass=sum((F(1,r['stabilizer_order']) for r in rows),F(0))
print('Co0 order:',CO0)
print('Isotropic lines in dimension 24:',points)
print('Isotropic lines in the dimension-22 quotient:',quotient_points)
print('Total isotropic 2-planes, direct incidence count:',TOTAL)
print('Classes with an A2 neighbor:',sum(r['type']=='A2' for r in rows))
print('Additional classes with an A1 neighbor:',sum(r['type']=='A1' for r in rows))
print('Remaining classes:',sum(r['type'] in ['3','622'] for r in rows))
print('Sum of 129 exact orbit lengths:',covered)
print('Sum of reciprocal full stabilizer orders:',mass)
print('Total planes / Co0:',F(TOTAL,CO0))
print('RESIDUAL PLANES:',TOTAL-covered)
print('RESIDUAL MASS:',F(TOTAL,CO0)-mass)
assert TOTAL==covered and mass==F(TOTAL,CO0)
print('PASS: all 129 classes are certified; no residual mass remains.')
(REC/'B_all_129_plane_orbits.json').write_text(json.dumps(rows))
with (REC/'B_all_129_plane_orbits.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['orbit','mark','representative','full_stabilizer_order','orbit_length','eight_Niemeier_extensions','four_opposite_extensions','plane_basis_standard_mod3','representative_record','full_group_record','generator_recipe'])
 for r in rows:w.writerow([r['orbit_id'],r['type'],r['representative'],r['stabilizer_order'],r['plane_orbit_size'],r['eight_extensions'],r['opposite'],r['plane_basis_standard_mod3'],r['representative_record'],r['full_group_record'],r['generator_recipe']])

# Compact complete printed table.  Each word is an eight-entry multiset;
# the numerical labels are defined in the surrounding theorem text.
labels={'Leech':'L','24A1':'1','12A2':'2','8A3':'3','6A4':'4','4A5+D4':'5','6D4':'6','4A6':'7','2A7+2D5':'8','3A8':'9','4E6':'10'}
lines=[r'\begin{longtable}{rllrrl}',r'\caption{All 129 isotropic-plane orbits. The representative is the stratum and flag identifier, or the packed rare vector; all planes are also supplied in one common integral Leech basis.}\label{tab:B129}\\',r'ID&mark&representative&$|\mathrm{Co}_{0,P}|$&$|\mathrm{Co}_0P|$&extensions\\\hline\endfirsthead',r'ID&mark&representative&$|\mathrm{Co}_{0,P}|$&$|\mathrm{Co}_0P|$&extensions\\\hline\endhead']
for r in rows:
 ex=','.join(labels[t]+('^{'+str(c)+'}' if c>1 else '') for t,c in sorted(r['extensions'].items(),key=lambda kv:(kv[0]!='Leech',labels[kv[0]])))
 rep=','.join(map(str,r['representative'])) if isinstance(r['representative'],(list,tuple)) else str(r['representative'])
 lines.append(f"{r['orbit_id']}&{r['type']}&{rep}&{r['stabilizer_order']}&{r['plane_orbit_size']}&${ex}$\\\\")
lines.append(r'\end{longtable}')
(REC/'B_all_129_table.tex').write_text('\n'.join(lines)+'\n')
