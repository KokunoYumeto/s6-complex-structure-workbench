"""Compute pi1 and all integral homology of a fully marked F.2 gluing.

JSON input keys: matrices (the k finite 6x6 homology matrices), numerators
(k integral six-vectors), orders (actual free affine orders), and optional
clutch, cusp_marking, local_bases.  The finite orders must be genuine,
at least two; eliminate order-one sites as in F.2.31 before this driver.
The optional local bases are computational coordinates, not new markings.

Example:
  python code/fourfolds_marked_gluing.py input.json output.json --fresh
The output retains the exact supplied cusp marking (or its recorded
canonical choice), every affine input, the group structure, full Smith
invariant factors and the reduced integral chain differentials.
"""
from pathlib import Path
import argparse,json,tempfile
import sympy as S
import fourfolds_total_homology as chains
from fourfolds_vankampen import (full_presentation,two_point_structure,
                                three_point_structure)

def compute(data,output):
    matrices=[S.Matrix(M) for M in data['matrices']]
    numerators=[S.Matrix(v) for v in data['numerators']]
    orders=data['orders']
    assert len(matrices)==len(numerators)==len(orders) in (2,3)
    assert all(isinstance(m,int) and m>=2 for m in orders)
    clutch=data.get('clutch')
    group=full_presentation(matrices,numerators,orders,clutch)
    structure=(two_point_structure if len(matrices)==2 else three_point_structure)(
        matrices,numerators,orders,clutch)
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='marked-gluing-',dir=output.parent) as folder:
        chain_file=Path(folder)/'chains.json'
        H=chains.total_homology(matrices,numerators,orders,clutch,
             data.get('local_bases'),data.get('cusp_marking'),chain_file)
        assert H[1]=={'rank':group['H1_free_rank'],'torsion':group['H1_torsion']}
        result=json.loads(chain_file.read_text())
    result['fundamental_group']=group
    result['fundamental_group_structure']=structure
    result['independent_H1_comparison']='passed'
    output.write_text(json.dumps(result,indent=2,default=int)+'\n')
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--fresh',action='store_true',help='recompute every chain-map column')
    args=parser.parse_args()
    chains.CHAIN_CACHE_READ=not args.fresh
    compute(json.loads(args.input.read_text()),args.output)
    print('COMPLETE MARKED GROUP AND INTEGRAL HOMOLOGY; INDEPENDENT H1 CHECK PASSED')
