"""Exact test of the only derived cusp-map ambiguity after its homology maps.
The possible Ext class lies in H4(cusp)/2; geometric base filtration places
it in the last seven (base degree two) coordinates. Test its image in the
cokernel of the degree-four gluing map.
"""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('complement_check.py').read_text().split('out={}')[0])
k=4
yz,yp,yr=hpresentation(yd(k),yd(k+1));bz,bp,br=hpresentation(dbdry(0,k),dbdry(0,k+1))
j=(yp*yj(k)*bz).col_join(fcusp(k)*bz)
d,u,v=snf(j);rank=j.rank();assert all(abs(d[i,i])==1 for i in range(rank))
proj=u[rank:,:];Cproj=proj[:,yz.cols:]
F2=Cproj[:,3:]
print('combined degree-four map shape',j.shape,'cokernel rank',proj.rows,flush=True)
print('cusp projection',Cproj,flush=True)
print('base-degree-two projection',F2,'Smith',snf(F2)[0],flush=True)
out={'gluing_matrix':j.tolist(),'cokernel_projection':proj.tolist(),'cusp_projection':Cproj.tolist(),'filtration_two_projection':F2.tolist(),'filtration_two_smith':snf(F2)[0].tolist()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
