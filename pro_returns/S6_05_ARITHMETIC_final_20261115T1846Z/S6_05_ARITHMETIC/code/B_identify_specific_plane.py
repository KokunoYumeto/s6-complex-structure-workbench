"""Exact isometry locating the original A5^4D4 intersection at row4."""
from B_plane_stabilizer_recipe import A2Engine
from B_A2_fusion import mark_isometry,key_from_Nrow,MODEL
from B_global_lattice import *
from B_exact_lattices import J,over,neighbour,gram

D=json.loads((REC/'B_A2_strata_setup.json').read_text());NB=qmat(D['N_basis']);G=qmat(D['N_Gram']);Nd=G.inv()*NB
L=qmat(over[5][2])*Nd.transpose()/144;JB=qmat(J)*Nd.transpose()/144
source=object.__new__(PlaneModel);source.G=G;source.L=L;source.Li=L.inv()
roots=[]
for i in range(12):
 for a,b in [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1)]:
  z=[0]*24;z[2*i:2*i+2]=[a,b];roots.append(ints(fmpq_mat([z])*MODEL.R)[0])
I=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
T=mark_isometry({'basis':qjson(I),'roots':roots},source)
Jdual=(JB*G*JB.transpose()).inv()*JB
rho=np.array(D['rho_N_mod3'],dtype=np.int64);j=next(j for j,x in enumerate(rho) if x)
for row in qrows(3*Jdual*T):
 xx=qmat([row]);a=np.array(ints(xx)[0],dtype=np.int64)%3;a=(a-a[j]*pow(int(rho[j]),-1,3)*rho)%3
 if any(a):break
assert key_from_Nrow(xx)==(0,5)
target=json.loads((REC/'B_A2_flags'/'0_5.json').read_text());engine=A2Engine();U=engine.transport(xx,qmat([target['y']]));T=T*U
assert span(qrows(JB*T))==span(qrows(qmat(target['J_basis'])))
S=qmat(json.loads((REC/'B_global_model_isometries.json').read_text())['standard_to_A2_N_coordinates']);C=L*T*S.inv();Cint=ints(C);assert abs(C.det())==1
GS=qmat(json.loads((REC/'B_standard_Leech_basis.json').read_text())['Gram']);assert C*GS*C.transpose()==L*G*L.transpose()
(REC/'B_specific_to_orbit4.json').write_text(json.dumps({'orbit':4,'flag_key':[0,5],'L0_basis_ambient_times12':over[5][2],'map_from_L0_basis_to_standard_Leech_basis':Cint,'J_basis_in_standard_Leech':qjson(JB*T*S.inv()),'standard_Leech_Gram':ints(GS)}))
print('PASS exact integral unimodular isometry from the original L0 to the common Leech model.')
print('PASS exact image of original J equals the perpendicular lattice in orbit4, A2 flag(0,5).')
