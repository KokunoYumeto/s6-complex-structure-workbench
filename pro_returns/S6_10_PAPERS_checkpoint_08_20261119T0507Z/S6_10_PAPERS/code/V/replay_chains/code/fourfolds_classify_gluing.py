"""Complete canonical linear classification and marked F.2 gluing computation.

The involution branch is a fast complete normal form.  The other linear
branches have the proved finite input-height bound and may be extremely
expensive.  No global height cutoff is used.  Full topology is computed
in the supplied coordinates and the exact conjugator transports every
marking; the output also gives the group in canonical coordinates.
"""
from pathlib import Path
import argparse,json,tempfile
import sympy as S
import fourfolds_total_homology as chains
from fourfolds_tuple_classification import canonical_tuple
from fourfolds_marked_gluing import compute
from fourfolds_vankampen import (full_presentation,two_point_structure,
                                three_point_structure)

def rows(M):return [[int(x) for x in row] for row in M.tolist()]

def genuine_data(data):
    out=dict(data)
    M=[S.Matrix(A) for A in out['matrices']]
    v=[S.Matrix(a) for a in out['numerators']]
    m=list(out['orders']);clutch=S.Matrix(out.get('clutch') or [0]*6)
    if 1 in m:
        assert len(m)==3 and m.count(1)==1
        i=m.index(1);assert M[i]==S.eye(6)
        suffix=S.eye(6)
        for A in M[i+1:]:suffix=suffix*A
        clutch+=suffix.inv()*v[i]
        M.pop(i);v.pop(i);m.pop(i)
        if out.get('local_bases') is not None:
            Q=list(out['local_bases']);Q.pop(i);out['local_bases']=Q
        out['removed_order_one_site']=i
    out.update(matrices=[rows(A) for A in M],numerators=[[int(x) for x in a] for a in v],
               orders=m,clutch=[int(x) for x in clutch])
    return out

def classify_and_compute(data,output):
    M=[S.Matrix(A) for A in data['matrices']]
    original_group=full_presentation(M,data['numerators'],data['orders'],data.get('clutch'))
    product=S.eye(6)
    for A in M:product=product*A
    normal=canonical_tuple(M+[product.inv()]);R=S.Matrix(normal['conjugator'])
    source=dict(data)
    if source.get('cusp_marking') is None:source['cusp_marking']=rows(chains.adapted_cusp(M))
    if source.get('clutch') is None:source['clutch']=[0]*6
    canonical=dict(source)
    canonical['matrices']=[rows(R*A*R.inv()) for A in M]
    canonical['numerators']=[[int(x) for x in R*S.Matrix(v)] for v in source['numerators']]
    canonical['clutch']=[int(x) for x in R*S.Matrix(source['clutch'])]
    canonical['cusp_marking']=rows(R*S.Matrix(source['cusp_marking']))
    if source.get('local_bases') is not None:
        canonical['local_bases']=[rows(R*S.Matrix(Q)) for Q in source['local_bases']]
    assert canonical['matrices']==normal['representative'][:-1]
    target_group=full_presentation(canonical['matrices'],canonical['numerators'],
                                  canonical['orders'],canonical['clutch'])
    target_structure=(two_point_structure if len(M)==2 else three_point_structure)(
        canonical['matrices'],canonical['numerators'],canonical['orders'],canonical['clutch'])
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    reduced=genuine_data(source)
    with tempfile.TemporaryDirectory(prefix='classified-gluing-',dir=output.parent) as folder:
        result=compute(reduced,Path(folder)/'topology.json')
    assert result['homology']['1']=={'rank':target_group['H1_free_rank'],
                                    'torsion':target_group['H1_torsion']}
    result.update(linear_classification=normal,original_fundamental_group=original_group,
                  chain_input_after_order_one_removal=reduced,
                  canonical_marked_data=canonical,canonical_fundamental_group=target_group,
                  canonical_fundamental_group_structure=target_structure,
                  comparison='Exact coordinate diffeomorphism; every cusp and affine marking transported')
    output.write_text(json.dumps(result,indent=2,default=int)+'\n')
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path);parser.add_argument('output',type=Path)
    parser.add_argument('--fresh',action='store_true')
    args=parser.parse_args();chains.CHAIN_CACHE_READ=not args.fresh
    classify_and_compute(json.loads(args.input.read_text()),args.output)
    print('CANONICAL LINEAR CLASS, ALL MARKINGS, FULL GROUP AND INTEGRAL HOMOLOGY PASSED')
