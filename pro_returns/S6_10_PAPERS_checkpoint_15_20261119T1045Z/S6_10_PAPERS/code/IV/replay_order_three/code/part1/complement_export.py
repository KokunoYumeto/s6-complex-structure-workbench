"""Export every differential and gluing map actually used for Y, the complement of the cusp.

This export does not set any cusp suspension term to zero.  The main graph,
finite caps, and their boundary maps are the complete cellular cone model.
The map from the cusp boundary to Y is also included in every degree.
"""
from pathlib import Path
import contextlib, io, json
with contextlib.redirect_stdout(io.StringIO()):
    exec(Path(__file__).with_name('complement_check.py').read_text().split('out={}')[0])

out={'description':__doc__, 'differentials':{}, 'boundary_differentials':{},
     'boundary_to_Y':{}, 'finite_boundary_to_cap':{}, 'finite_boundary_to_main':{},
     'dimensions':{}, 'homology':{}}
for k in range(9):
    out['dimensions'][str(k)]=ydim(k)
    if k:
        mat=yd(k)
        out['differentials'][str(k)]=mat.tolist()
        if k>1:
            assert yd(k-1)*mat==s.zeros(ydim(k-2),ydim(k))
    out['boundary_differentials'][str(k)]=dbdry(0,k).tolist()
    out['boundary_to_Y'][str(k)]=yj(k).tolist()
    for i in [1,2]:
        out['finite_boundary_to_cap'][f'{i}.{k}']=fcap(i,k).tolist()
        out['finite_boundary_to_main'][f'{i}.{k}']=fmain(i,k).tolist()
    aa=yd(k) if k else s.zeros(0,ydim(k))
    bb=yd(k+1)
    h=homology(aa,bb)
    out['homology'][str(k)]=h
    print(k,ydim(k),h['free'],h['torsion'],flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
