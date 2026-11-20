"""Read-only exact verification of this derivation's newly saved arrays."""
from pathlib import Path
from math import comb
import json, datetime, hashlib
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

P=Path(__file__).parent
source=P/'fresh_candidate_chain.json'
r=json.loads(source.read_text())
nr=r['candidate_global_chain_ranks'];yr=r['Y_chain_ranks']
D={int(k):s.Matrix(v) for k,v in r['candidate_differentials'].items()}
D[0]=s.zeros(0,nr[0]);D[9]=s.zeros(nr[8],0)
Y={k:D[k][:yr[k-1],:yr[k]] for k in range(1,9)}
Y[0]=s.zeros(0,yr[0]);Y[9]=s.zeros(yr[8],0)

def mat(v,rows,cols):return s.Matrix(v) if rows and cols else s.zeros(rows,cols)
def verify(d,records,counts,tag):
    table=[]
    for k in range(9):
        h=records[str(k)];rout=h['out_rank'];rin=h['in_rank']
        Z=mat(h['kernel_basis'],counts[k],counts[k]-rout)
        A=mat(h['incoming'],counts[k]-rout,d[k+1].cols)
        U=mat(h['cycle_to_smith'],Z.cols,Z.cols)
        Q=mat(h['incoming_smith'],A.rows,A.cols)
        H=mat(h['homology_projection'],h['rank'],counts[k])
        assert d[k]*Z==s.zeros(d[k].rows,Z.cols)
        assert Z*A==d[k+1]
        zdiag=smith_normal_form(Z,domain=s.ZZ)
        assert all(abs(zdiag[j,j])==1 for j in range(Z.cols))
        assert d[k].rank()==rout
        assert abs(int(U.det()))==1
        assert hermite_normal_form(U*A)==hermite_normal_form(Q)
        assert H*Z==U[rin:,:]
        assert H*d[k+1]==s.zeros(h['rank'],d[k+1].cols)
        diag=[abs(int(Q[j,j])) for j in range(min(Q.shape)) if Q[j,j]]
        assert len(diag)==rin
        assert [a for a in diag if a>1]==h['torsion']
        assert counts[k]-rout-rin==h['rank']
        assert d[k]*d[k+1]==s.zeros(d[k].rows,d[k+1].cols)
        table.append({'degree':k,'chain_rank':counts[k],'outgoing_rank':rout,
                      'cycle_rank':Z.cols,'incoming_rank':rin,'betti':h['rank'],
                      'torsion':h['torsion'],'nonzero_incoming_factors':diag})
    return table

report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'Y':verify(Y,r['Y_homology'],yr,'Y'),
        'global':verify(D,r['candidate_global_homology'],nr,'global'),
        'fibre_fillers_checked':[]}
for k in (2,3,4,5):
    n=comb(6,k)
    # The last B_k block in d_(k+1) contains (j_Y,-j_C).
    j=D[k+1][:yr[k],yr[k+1]+[1,3,9,9,10,3,1,0,0][k+1]:][:,:n]
    F=mat(r['Y_homology'][str(k)]['fibre_fillers'],yr[k+1],n)
    assert Y[k+1]*F==j
    report['fibre_fillers_checked'].append(k)
report['status']='All displayed identities, kernel saturation, image lattices, and integral fibre fillers verified.'
(P/'fresh_saved_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('Y','global')},indent=2))
print('global table',[(x['degree'],x['chain_rank'],x['outgoing_rank'],x['incoming_rank'],x['betti'],x['torsion']) for x in report['global']])
