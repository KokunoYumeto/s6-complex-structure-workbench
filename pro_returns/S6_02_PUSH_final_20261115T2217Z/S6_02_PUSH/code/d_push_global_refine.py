"""Exact dyadic refinement of the unresolved compact gradient rectangles.

Every leaf is either an outward-Arb nonvanishing enclosure or lies wholly
inside one of the explicitly reserved local discs.  The input cover and its
independent E.4 root contractions are recorded by SHA256.  New leaf roots use
the very same independently implemented strict contraction calculation.
"""
from fractions import Fraction
from pathlib import Path
import hashlib, json, time
from flint import arb, acb, ctx
from e4_arb_certificate import certify_box, interval
from d_push_global_arb import certify, I_RADIUS, RHO, RHO_RADIUS

ctx.prec=192
BASE=Path(__file__).resolve().parent
INITIAL=BASE/'d_push_global_arb.json'
ROOTS=BASE/'e4_arb_certificate.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def children(box):
    x0,x1,y0,y1=map(Fraction,box)
    xm,ym=(x0+x1)/2,(y0+y1)/2
    return [[str(a),str(b),str(c),str(d)]
            for a,b in [(x0,xm),(xm,x1)]
            for c,d in [(y0,ym),(ym,y1)]]

def local(box):
    x0,x1,y0,y1=box
    tau=acb(interval(x0,x1),interval(y0,y1))
    if (tau-acb(0,1)).abs_upper()<I_RADIUS:
        return 'local_i',(tau-acb(0,1)).abs_upper()
    if (tau-RHO).abs_upper()<RHO_RADIUS:
        return 'local_rho',(tau-RHO).abs_upper()
    return None,None

def main():
    started=time.time()
    original=json.loads(INITIAL.read_text())
    assert not original['summary']['counts']['ERROR']
    todo=[r for r in original['boxes'] if r['status']=='UNDECIDED']
    assert todo
    tree=[];leaves=[];root_certificates=[]
    def walk(index,box,depth):
        status,distance=local(box)
        if status:
            leaves.append({'index':index,'box':box,'status':status,
                           'distance_upper':distance.str(45,more=True)})
            return
        r=certify_box((index,box))
        root_certificates.append(r)
        if r.get('proved'):
            out=certify(r)
            if out['status']=='PASS':
                leaves.append(out)
                return
        else:
            out={'index':index,'box':box,'status':'ROOT_UNDECIDED',
                 'root_certificate':r}
        if depth>=12:
            leaves.append(out)
            print('FAIL',json.dumps(out),flush=True)
            return
        boxes=children(box)
        child_ids=[str(index)+'.'+str(j) for j in range(4)]
        tree.append({'index':index,'box':box,'depth':depth,
                     'children':child_ids,'child_boxes':boxes,
                     'previous_status':out['status']})
        for j,child_box in enumerate(boxes):
            walk(child_ids[j],child_box,depth+1)
    for old in todo:
        # Retain the initial unresolved record as the tree root.  A new tighter
        # contraction on this same box may already settle it; otherwise split.
        walk(str(old['index']),old['box'],0)
        print('refined original',old['index'],'leaves',len(leaves),flush=True)
    counts={k:sum(r['status']==k for r in leaves)
            for k in ['PASS','local_i','local_rho','UNDECIDED','ROOT_UNDECIDED']}
    passed=[r for r in original['boxes']+leaves if r['status']=='PASS']
    ok=not counts['UNDECIDED'] and not counts['ROOT_UNDECIDED']
    summary={'result':'COMPACT_PASS' if ok else 'UNFINISHED',
             'scope':'Initial rational cover with the listed exact subdivisions; local discs and cusp are separate.',
             'initial_sha256':digest(INITIAL),'e4_roots_sha256':digest(ROOTS),
             'script_sha256':digest(Path(__file__)),
             'gradient_script_sha256':digest(BASE/'d_push_global_arb.py'),
             'original_boxes':len(original['boxes']),
             'original_unresolved':len(todo),'refined_leaf_counts':counts,
             'refinement_nodes':len(tree),'new_root_contractions':len(root_certificates),
             'maximum_depth':max([r['depth']+1 for r in tree],default=0),
             'final_nonvanishing_leaves':len(passed),
             'final_local_i_leaves':original['summary']['counts']['local_i']+counts['local_i'],
             'final_local_rho_leaves':original['summary']['counts']['local_rho']+counts['local_rho'],
             'precision_bits':ctx.prec,'i_radius':'3/20000','rho_radius':'1/50',
             'minimum_Z_lower':min(arb(r['Z_abs_lower']).lower() for r in passed).str(45,more=True),
             'minimum_F_lower':min(arb(r['F_abs_lower']).lower() for r in passed).str(45,more=True),
             'seconds':time.time()-started}
    payload={'summary':summary,'refinement_tree':tree,'leaves':leaves,
             'new_root_certificates':root_certificates}
    (BASE/'d_push_global_refine.json').write_text(json.dumps(payload,indent=2)+'\n')
    (BASE/'d_push_global_refine_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
    main()
