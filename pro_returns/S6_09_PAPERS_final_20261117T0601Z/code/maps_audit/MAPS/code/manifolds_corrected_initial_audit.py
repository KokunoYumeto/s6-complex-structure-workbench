"""Exact full-Smith replays of the height-integral corrected initial algorithm."""
from pathlib import Path
import json
import sympy as S
import manifolds_corrected_initial as C
import manifolds_general_initial as G
ROOT=Path(__file__).resolve().parents[1]

def packed(result):
    return {k:result[k] for k in ['entry','profile','P','Q','weights','e','original_sites',
             'vertical_corrections','euler','relative_free_rank','homology','fundamental_group',
             'local','H1_matrix','H2_matrix']}

if __name__=='__main__':
    overlap=[];new=[];explicit=[];extras=[]
    for key,info in sorted(C.PROFILES.items()):
        den=int(S.Rational(info['height_matrix'][0][0]).q)
        target=next(j for j,k in enumerate(info['kodaira_types']) if k.startswith('I') and k[1:].isdigit())
        weights=[0]*len(info['kodaira_types']);weights[target]=1
        for e in [-1,1]:
            a=C.compute(*key,den,1,weights,e=e)
            b=G.compute(*key,den,1,weights,e=e)
            assert a['homology']==b['homology'] and a['H2_matrix']==b['H2_matrix']
            overlap.append(dict(key=key,e=e,homology=a['homology']))
    print('D46 full-matrix overlaps',len(overlap),flush=True)
    for a,b in [(2,4),(4,2)]:
        for zero in range(1,5):
            weights=[0]*5;weights[zero]=1
            for e in [-1,1]:
                r=C.compute(45,'default',a,b,weights,e=e)
                assert r['homology'][1]==dict(free=0,torsion=[])
                assert r['homology'][2]==dict(free=0,torsion=[b])
                assert r['homology'][3]==dict(free=0,torsion=[b])
                assert r['fundamental_group']['vertical_quotient']==dict(free=0,torsion=[])
                explicit.append(packed(r))
    print('Independent D50 example comparisons',len(explicit),flush=True)
    catalog=json.loads((ROOT/'records/root_vertical_corrections.json').read_text())
    for profile in catalog['global_profile_residue_cases']:
        key=(profile['os_entry'],profile['profile']);info=C.PROFILES[key]
        den=profile['height_denominator'];kinds=info['kodaira_types']
        sites=[j for j,k in enumerate(kinds) if k.startswith('I') and k[1:].isdigit()]
        alloriginal=[j for j,k in enumerate(kinds) if j not in sites]
        for a,b in profile['new_pairs_beyond_narrowness_OR']:
            height=a*b//den
            for zero in sites:
                weights=[0]*len(kinds);weights[zero]=height
                for orig in sorted({tuple(),tuple(alloriginal)}):
                    r=C.compute(*key,a,b,weights,original=orig,e=1)
                    new.append(packed(r))
            # A separate regular zero and a regular free logarithm.
            weights=[0]*len(kinds)+[height]
            r=C.compute(*key,a+den,b,weights[:-1]+[(a+den)*b//den],
                        original=alloriginal,e=-1,regular=[dict(m=2,v=[0,0,0,1])])
            extras.append(packed(r))
        if profile['new_pairs_beyond_narrowness_OR']:
            print(key,'new residue pairs',len(profile['new_pairs_beyond_narrowness_OR']),flush=True)
    report=dict(scope=__doc__,old_full_matrix_overlaps=overlap,D50_examples=explicit,
                new_residue_cases=new,additional_weights_and_regular_logs=extras)
    (ROOT/'records/manifolds_corrected_initial_audit.json').write_text(json.dumps(report,indent=2,default=int)+'\n')
    print('All45 new residue pairs represented; full new Smiths',len(new),flush=True)
    print('Additional higher-weight and regular-log Smiths',len(extras),flush=True)
