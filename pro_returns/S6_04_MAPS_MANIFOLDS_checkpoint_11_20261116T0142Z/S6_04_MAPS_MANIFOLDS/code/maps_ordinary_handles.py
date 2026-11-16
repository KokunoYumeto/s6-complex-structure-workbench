"""Exact chart/framing checks and a complete labelled finite handle inventory.

The geometric attaching embeddings are the macros E.H1--E.H12 in
maps_ordinary_handles_proof.tex.  The JSON expands every torus-sector choice;
it is not a homological cancellation or a recognition from handle counts.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
rays = [s.Matrix(v) for v in [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]]
X,Y,q,z,a,b = s.symbols('X Y q z a b', nonzero=True)
variables = [X,Y,q]
charts=[]
for i in range(6):
    P=s.Matrix([[0,rays[i][0],rays[(i+1)%6][0]],
                [0,rays[i][1],rays[(i+1)%6][1]], [1,1,1]])
    assert P.det()==1
    inv=P.inv()
    values=[s.prod(variables[j]**inv[k,j] for j in range(3)) for k in range(3)]
    n,ai,aj=values
    assert s.simplify(n*ai*aj-q)==0
    assert s.simplify(ai**rays[i][0]*aj**rays[(i+1)%6][0]-X)==0
    assert s.simplify(ai**rays[i][1]*aj**rays[(i+1)%6][1]-Y)==0
    charts.append({'vertex':i,'matrix':[[int(x) for x in P.row(k)] for k in range(3)],
                   'normal_first_exponents':[[int(x) for x in inv.row(k)] for k in range(3)],
                   'n_ai_aj':[str(v) for v in values]})

# Canonical vertex charts 0=Z and 1=W.  Vertex i+2 rotates normal-first
# coordinates once; there is no phase factor in any such chart transition.
canonical={0:('Z',(0,1,2)),1:('W',(0,1,2)),
           2:('Z',(1,2,0)),3:('W',(1,2,0)),
           4:('Z',(2,0,1)),5:('W',(2,0,1))}
edge_endpoints=[]
used=[]
for i in range(3):
    vn,pn=canonical[i]
    vf,pf=canonical[(i-1)%6]
    # At zero: (z,a,b)=(a_next,a_i,n).
    # At infinity: (w,A,B)=(a_prev,a_i,n).
    zero=(vn,pn[2],pn[1],pn[0])
    infinity=(vf,pf[1],pf[2],pf[0])
    used.extend([(zero[0],zero[1]),(infinity[0],infinity[1])])
    edge_endpoints.append({'edge':i,'zero_axis_a_b':zero,
                           'infinity_axis_A_B':infinity,
                           'transition':['1/z','z*a','z*b'],
                           'angular_transition':['-theta','theta+arg(a)','theta+arg(b)']})
assert sorted(used)==[(v,j) for v in ('W','Z') for j in range(3)]
assert s.simplify((1/z)*(z*a)*(z*b)-z*a*b)==0
# Relative normal frames each have a +1 rotation, while the curve angle
# reverses.  They are retained individually, not reduced to a parity class.
angular=s.Matrix([[-1,0,0],[1,1,0],[1,0,1]])
assert s.Matrix([[1,1,1]])*angular==s.Matrix([[1,1,1]])

# Check all six neighbouring dense-sector seam maps in full dimension.
seams=[]
for i in range(6):
    P=s.Matrix(charts[i]['matrix']); Q=s.Matrix(charts[(i+1)%6]['matrix'])
    transition=Q.inv()*P
    assert s.Matrix([[1,1,1]])*transition==s.Matrix([[1,1,1]])
    assert transition.det()==1
    seams.append([[int(x) for x in transition.row(k)] for k in range(3)])
composition=s.eye(3)
for mat in seams:
    composition=s.Matrix(mat)*composition
assert composition==s.eye(3)

# The opposite fan involution and the endpoint gluing are also exact.
for i in range(6):
    assert rays[(i+3)%6]==-rays[i]
    P=s.Matrix(charts[i]['matrix'])
    Q=s.Matrix(charts[(i+2)%6]['matrix'])
    L=s.Matrix([[1,0,-rays[i][0]],[0,1,-rays[i][1]],[0,0,1]])
    assert Q.inv()*L*P==s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
polygon=[(-1,-1),(0,-1),(1,0),(1,1),(0,1),(-1,0)]
for v in polygon:
    assert all((s.Matrix(v).dot(r)>=-1) for r in rays)
assert sorted(tuple(-x for x in v) for v in polygon)==sorted(polygon)

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=s.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
assert A1*A2*M0==s.eye(4)
assert A1**3==s.eye(4) and A2**4==s.eye(4)
B1=A1[1:4,1:4]; B2=A2[1:4,1:4]
assert B1**3==s.eye(3) and B2**4==s.eye(3)

def parameter_handles(name,r,k,n,macro,extra=None):
    """Split each parameter circle into its ordered zero/one intervals."""
    records=[]
    for bits in sorted(product((0,1),repeat=r),key=lambda x:(sum(x),x)):
        j=k+sum(bits)
        records.append({'name':name+''.join(map(str,bits)), 'dimension':n,
                        'index':j,'coindex':n-j,'parameter_bits':list(bits),
                        'base_negative_dimension':k,
                        'attaching_macro':macro,'data':extra or {}})
    return records

E=[]
for vertex in ('Z','W'):
    E += parameter_handles('cusp_vertex_'+vertex,0,0,6,'E.H1',{'vertex':vertex})
for edge in range(3):
    E += parameter_handles(f'cusp_edge_{edge}_',1,1,6,'E.H2--E.H4',{'edge':edge})
E += parameter_handles('cusp_core_',2,2,6,'E.H5--E.H7')
cusp_counts=[Counter(v['index'] for v in E)[j] for j in range(7)]
assert cusp_counts==[2,3,4,2,1,0,0]
for band in range(2):
    E += parameter_handles(f'core_band_{band}_',4,1,6,'E.H9',{'band':band})
for cap in (1,2):
    for circle_sector in (0,1):
        E += parameter_handles(f'finite_cap_{cap}_sector_{circle_sector}_',3,
                               2+circle_sector,6,'E.H10',
                               {'cap':cap,'base_circle_sector':circle_sector})
E_counts=[Counter(v['index'] for v in E)[j] for j in range(7)]
assert E_counts==[2,5,14,22,21,10,2]
assert len(E)==76 and sum((-1)**j*c for j,c in enumerate(E_counts))==2

# The second half is the dual *relative* decomposition of T4 x E.
# This retains the specified full boundary flip E.U6.
P=[]
for side in ('left','right_dual'):
    source=E if side=='left' else list(reversed(E))
    for handle in source:
        bits_list=sorted(product((0,1),repeat=4),key=lambda x:(sum(x),x))
        if side!='left': bits_list=list(reversed(bits_list))
        for bits in bits_list:
            original_index=handle['index']+sum(bits)
            index=original_index if side=='left' else 10-original_index
            P.append({'name':side+'_'+handle['name']+'_' + ''.join(map(str,bits)),
                      'dimension':10,'index':index,'coindex':10-index,
                      'source_E_handle':handle['name'],'product_bits':list(bits),
                      'dual':side!='left','attaching_macro':'E.H11--E.H12'})
P_counts=[Counter(v['index'] for v in P)[j] for j in range(11)]
assert P_counts==[4,31,119,290,485,574,485,290,119,31,4]
assert len(P)==2432 and sum((-1)**j*c for j,c in enumerate(P_counts))==0
assert len({h['name'] for h in P})==len(P)
assert P_counts==list(reversed(P_counts))

certificate={'status':'Exact coordinate identities and inventories passed; geometric proof in companion TeX.',
             'dense_charts':charts,'dense_sector_seams':seams,
             'edge_endpoint_framings':edge_endpoints,
             'edge_angular_matrix':[[int(x) for x in angular.row(k)] for k in range(3)],
             'moment_polygon':polygon,'cusp_handle_counts':cusp_counts,
             'E_handle_counts':E_counts,'P_handle_counts':P_counts,
             'matrices':{name:[[int(x) for x in mat.row(k)] for k in range(mat.rows)]
                         for name,mat in [('A1',A1),('A2',A2),('M0',M0),('B1',B1),('B2',B2)]},
             'E_handles':E,'P_handles':P}
out=ROOT/'code/maps_ordinary_handles.out.json'
out.write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS: six exact dense charts and six full-dimensional sector seams')
print('PASS: six coordinate-axis ends, all endpoint +1,+1 normal rotations retained')
print('PASS: triple rotations, finite matrices, and total monodromy identity')
print('cusp indices 0..6:',cusp_counts)
print('E indices 0..6:',E_counts,'; total',len(E),'; Euler 2')
print('P indices 0..10:',P_counts,'; total',len(P),'; Euler 0')
print('Inventory:',out.relative_to(ROOT))
