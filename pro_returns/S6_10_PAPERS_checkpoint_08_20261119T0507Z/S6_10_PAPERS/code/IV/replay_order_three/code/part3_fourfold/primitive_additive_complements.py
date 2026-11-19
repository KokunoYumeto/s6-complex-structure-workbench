#!/usr/bin/env python3
"""Integral complements of the reduced III/IV source fibres in K22.

The basis is an exact integral kernel, obtained from the inverse unimodular
NS Gram matrix.  Cap maps and return indices are not inferred here.
"""
from pathlib import Path
from functools import reduce
from math import gcd
from datetime import datetime, timezone
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'code/part3_fourfold/primitive_source_translation.json'
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+datetime.now(timezone.utc).isoformat()+
            ' — Opened current-team code/part3_fourfold/primitive_source_translation.json; reason: exact reduced-additive source-complement restriction; material: full integral NS, actual negative-translation and section matrices.\n')
data=json.loads(source.read_text())
cases={a['row']:a for a in data['cases']}
def ints(A):
    assert all(s.denom(a)==1 for a in A)
    return [[int(a) for a in row] for row in A.tolist()]
def primitive(v):
    den=s.ilcm(*[s.denom(a) for a in v])
    v=v*den
    g=reduce(gcd,[abs(int(a)) for a in v])
    v=v/g
    for a in v:
        if a:
            if a<0: v=-v
            break
    return v
outputs=[]
for row,p,block,kind in [(47,2,1,'III'),(56,2,2,'III'),(56,3,1,'IV')]:
    a=cases[row]
    G=s.Matrix(a['gram'])
    T=s.Matrix(a['actual_suspension_translation'])
    eye=s.eye(10)
    F,O=eye[:,1],eye[:,0]
    roots=[i for i,name in enumerate(a['basis']) if name.startswith(f'I{p}_{block}_C')]
    assert len(roots)==p-1
    deleted=[1]+roots
    retained=[i for i in range(10) if i not in deleted]
    K=G.inv()[:,retained]
    P=G[retained,:]
    constraint=G[deleted,:]
    assert P*K==s.eye(10-p)
    assert constraint*K==s.zeros(p,10-p)
    # Columns of G^-1 form an integral unimodular full basis; therefore K
    # is the whole integral kernel, not a finite-index sublattice.
    assert abs(G.det())==1
    Tv=P*T*K
    assert K*Tv==T*K
    D=Tv-s.eye(10-p)
    S=smith_normal_form(D,domain=ZZ)
    smith=[abs(int(S[i,i])) for i in range(10-p)]
    ker=primitive(D.nullspace()[0])
    coker=primitive(D.T.nullspace()[0])
    Fc=P*F
    assert D*Fc==s.zeros(10-p,1)
    assert ker==Fc or ker==-Fc
    # The p-fold punctured section cycle, corrected integrally in only
    # the removed additive root lattice.
    Z0=p*(T*O-O)
    rootgram=G[roots,roots]
    desired=-(G[roots,:]*Z0)
    correction=rootgram.inv()*desired
    Z=Z0+eye[:,roots]*correction
    assert all(s.denom(x)==1 for x in correction)
    assert constraint*Z==s.zeros(p,1)
    Zc=P*Z
    z_value=(coker.T*Zc)[0]
    M=s.Matrix(a['line_divisor_class'])
    assert constraint*M==s.zeros(p,1)
    Mc=P*M
    assert D*Mc==-Fc
    m_value=(coker.T*Mc)[0]
    # Source boundary meridian has normal-function order p.  The exact
    # cone cycle (-C,pq) has the above integral image Z.
    outputs.append({
        'row':row,'removed_fibre':kind,'component_count':p,
        'NS_basis':a['basis'],'constraint_rows':ints(constraint),
        'integral_kernel_basis':ints(K),'kernel_left_inverse':ints(P),
        'translation_restriction':ints(Tv),'wang_matrix':ints(D),
        'smith':smith,'intersection_matrix':ints(K.T*G*K),
        'kernel_F_coordinates':ints(Fc),
        'primitive_cokernel_functional':ints(coker),
        'line_M_coordinates':ints(Mc),'line_M_cokernel_value':int(m_value),
        'relative_Wang_source_cycle':ints(Z),
        'relative_Wang_removed_root_correction':ints(correction),
        'relative_Wang_kernel_coordinates':ints(Zc),
        'relative_Wang_cokernel_value':int(z_value),
        'pairing_F_Z':int((F.T*G*Z)[0]),
        'actual_translation':'T_-G',
        'scope':'exact source complement and integral relative-Wang column; cap gluing and global topology require their actual maps',
    })
    print(f'OS{row} minus {kind}: Smith={smith}; boundary pq column={z_value}; M column={m_value}')
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps({'cases':outputs},indent=2)+'\n')
print('PASS: exact integral kernels, actual translations and corrected section columns.')
