"""Exact covering and proof-dependency audit of the compact D.4 certificate."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from flint import arb,acb,ctx
from e4_cover_and_local import audit_cover,SOURCE
from d_push_global_arb import rat,interval,RHO,I_RADIUS,RHO_RADIUS
from d_push_global_refine import children

ctx.prec=256
BASE=Path(__file__).resolve().parent
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def boxeq(a,b):return tuple(map(F,a))==tuple(map(F,b))

def main():
    source_audit=audit_cover()
    original=json.loads((BASE/'d_push_global_arb.json').read_text())
    roots=json.loads((BASE/'e4_arb_certificate.json').read_text())
    source=json.loads(SOURCE.read_text())
    refined=json.loads((BASE/'d_push_global_refine.json').read_text())
    summary=refined['summary']
    assert summary['result']=='COMPACT_PASS'
    assert summary['initial_sha256']==digest(BASE/'d_push_global_arb.json')
    assert summary['e4_roots_sha256']==digest(BASE/'e4_arb_certificate.json')
    assert summary['gradient_script_sha256']==digest(BASE/'d_push_global_arb.py')
    assert summary['script_sha256']==digest(BASE/'d_push_global_refine.py')
    assert len(original['boxes'])==len(roots['boxes'])==19701
    assert roots['summary']['input_sha256']==digest(SOURCE)
    assert all(boxeq(r['box'],s['box']) for r,s in zip(roots['boxes'],source['certified']))
    for out,root in zip(original['boxes'],roots['boxes']):
        assert out['index']==root['index'] and boxeq(out['box'],root['box'])
        assert root['proved']
    nodes={d['index']:d for d in refined['refinement_tree']}
    leaves={d['index']:d for d in refined['leaves']}
    assert len(nodes)==len(refined['refinement_tree'])
    assert len(leaves)==len(refined['leaves'])
    assert not set(nodes)&set(leaves)
    root_by_id={str(d['index']):d for d in refined['new_root_certificates']}
    assert len(root_by_id)==len(refined['new_root_certificates'])
    used_nodes=set();used_leaves=set();all_leaves=[]
    def descend(index,box):
        if index in leaves:
            d=leaves[index];assert boxeq(d['box'],box)
            assert index not in used_leaves;used_leaves.add(index)
            if d['status']=='PASS':
                assert root_by_id[index]['proved']
                assert boxeq(root_by_id[index]['box'],box)
            all_leaves.append(d)
            return
        d=nodes[index];assert boxeq(d['box'],box)
        assert index not in used_nodes;used_nodes.add(index)
        exact=children(box)
        assert len(d['children'])==len(d['child_boxes'])==4
        for j,(child,childbox) in enumerate(zip(d['children'],d['child_boxes'])):
            assert child==str(index)+'.'+str(j)
            assert boxeq(childbox,exact[j])
            descend(child,childbox)
    for d in original['boxes']:
        if d['status']=='UNDECIDED':descend(str(d['index']),d['box'])
        else:all_leaves.append(d)
    assert used_nodes==set(nodes) and used_leaves==set(leaves)
    counts={'PASS':0,'local_i':0,'local_rho':0}
    for d in all_leaves:
        status=d['status'];assert status in counts;counts[status]+=1
        if status=='PASS':
            assert arb(d['Z_abs_lower']).lower()>rat('13/10000')
            assert arb(d['F_abs_lower']).lower()>13
        else:
            x0,x1,y0,y1=d['box']
            tau=acb(interval(x0,x1),interval(y0,y1))
            centre,radius=(acb(0,1),I_RADIUS) if status=='local_i' else (RHO,RHO_RADIUS)
            assert (tau-centre).abs_upper()<radius
    assert counts=={'PASS':18319,'local_i':1425,'local_rho':11}
    import sympy as sp
    a,b,x,T,B,C=sp.symbols('a b x T B C',real=True)
    real_period=sp.Matrix([[6*a,x,1,0],[6*b,T,0,0],
                          [B,a,0,1],[C,b,0,0]])
    assert sp.expand(real_period.det())==T*C-6*b*b
    result={'result':'PASS','source_cover_audit':source_audit,
            'exact_refinement_nodes':len(nodes),'exact_refined_leaves':len(leaves),
            'final_leaf_count':len(all_leaves),'counts':counts,
            'rational_nonvanishing_bounds':{'abs_Z_greater_than':'13/10000','abs_F_greater_than':'13'},
            'every_closed_excluded_rectangle_inside_its_local_disc':True,
            'all_input_hashes_match':True,
            'real_period_determinant':'Im(tau)*Im(beta)-6*Im(mu)^2',
            'gradient_certificate_sha256':digest(BASE/'d_push_global_arb.json'),
            'refinement_certificate_sha256':digest(BASE/'d_push_global_refine.json')}
    (BASE/'d_push_global_cover_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
