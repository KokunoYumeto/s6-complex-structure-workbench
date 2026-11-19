"""Exact constant certificates and independent-sector overlaps for D.2.46.

The residue enumeration is exhaustive: the projected primitive vanishing
line is n/gcd(n,a) times the elliptic vanishing line, so only a modulo the
displayed narrow-MW period occurs.  No upper bound on a,b,weights or logs
is asserted by the sample Smith comparisons.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
import manifolds_general_initial as G
import manifolds_all_weighted_profiles as OLD

ROOT=Path(__file__).resolve().parent

def closure(columns,matrices):
    L=hermite_normal_form(s.Matrix.hstack(*columns))
    while True:
        T=hermite_normal_form(s.Matrix.hstack(L,*[A*L for A in matrices]))
        if T==L:return L
        L=T

def constant_certificates():
    records=[];local=[];elliptic=[]
    for key,info in G.PROFILES.items():
        entry,profile=key
        d0=Fraction(info['height_matrix'][0][0]).denominator
        Bs=[s.Matrix(A) for A in info['elliptic_matrices']]
        allrel=s.Matrix.hstack(*[B-s.eye(2) for B in Bs])
        assert G.W.group(allrel)==dict(free=0,torsion=[])
        generator_product=s.eye(4)
        for B,c in zip(Bs,info['section_cocycles'][0]):
            generator_product*=G.local_lift(B,c,c,0)
        expected=s.eye(4);expected[2,3]=-s.Rational(1,d0)
        assert generator_product==expected
        elliptic.append(dict(entry=entry,profile=profile,relation_matrix=allrel.tolist(),
                              generator_central_product=str(generator_product[2,3])))
        for residue in range(d0):
            a=residue or d0;b=d0
            weights=[0]*len(Bs)+[a]
            AA=[s.Matrix(A) for A in G.om.monodromy_tuple(entry,(a,),(b,),tuple(weights),profile=profile,verbose=False)]
            assert AA==G.actual_lifts(info,a,b,weights)
            columns=[];star_columns=[]
            for i,(kind,B,A) in enumerate(zip(info['kodaira_types'],Bs,AA)):
                if kind.startswith('I') and kind[1:].isdigit():
                    n=int(kind[1:]);N=A-s.eye(4)
                    F=G.satimage(N)
                    projected=hermite_normal_form(F[:2,:])
                    primitive=G.ikernel(B-s.eye(2))[:,0]
                    expected=hermite_normal_form((n//gcd(n,a))*primitive)
                    assert projected==expected
                    columns.extend(projected.columnspace())
                    local.append(dict(entry=entry,profile=profile,a_mod=residue,period=d0,
                                      site=i,type=kind,actual_matrix=A.tolist(),
                                      primitive_full_vanishing=F.tolist(),
                                      projected_line=projected.tolist(),coefficient=n//gcd(n,a)))
                elif kind.startswith('I') and kind.endswith('*') and kind[1:-1].isdigit():
                    comp=info['component_maps'][i]
                    pc=(a*comp['rows'][0][0])%comp['moduli'][0]
                    F=s.eye(4)[:,:3] if pc else G.satimage(A-s.eye(4))
                    projected=hermite_normal_form(F[:2,:])
                    assert projected==s.eye(2)
                    star_columns.extend(projected.columnspace())
            bare=closure(columns,Bs)
            actual=closure(columns+star_columns,Bs)
            quotient=G.W.group(actual)
            exceptional=entry==49 and profile=='II' and residue%2==1
            assert quotient==dict(free=0,torsion=([2,2] if exceptional else []))
            if exceptional:
                assert actual==2*s.eye(2)
                # Original I2, a positive I2 weight, or any original additive
                # adds a primitive elliptic vector and closes the whole lattice.
                site=info['kodaira_types'].index('I2')
                van=G.ikernel(Bs[site]-s.eye(2))[:,0]
                assert closure(columns+[van],Bs)==s.eye(2)
                for j,k in enumerate(info['kodaira_types']):
                    if k=='I2':continue
                    assert int((Bs[j]-s.eye(2)).det())%2==1
                    assert (Bs[j]**3-s.eye(2)).applyfunc(lambda x:x%2)==s.zeros(2)
                    assert (Bs[j]-s.eye(2)).applyfunc(lambda x:x%2)!=s.zeros(2)
                    assert all(int(x)%2==0 for x in AA[j][:2,3])
            records.append(dict(entry=entry,profile=profile,a_mod=residue,period=d0,
                                raw_elliptic_closure=bare.tolist(),
                                original_star_elliptic_closure=actual.tolist(),
                                vertical_quotient_after_delta=quotient))
    assert len(records)==284
    result=dict(scope=__doc__,residues=records,rank_one_local=local,
                common_elliptic_relations=elliptic)
    (ROOT/'manifolds_general_initial_constants.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
    print('Exhaustive residue closures',len(records),'actual rank-one lines',len(local),
          'elliptic unit certificates',len(elliptic),flush=True)
    return result

def overlap_checks():
    results=[]
    for i,p in enumerate(G.W.PATTERNS):
        if i%13:continue
        row=G.W.MONO[G.W.key(p)]
        if row['local'][p['zero_index']]['type']!='I1':continue
        original=[j for j,v in p['additive_choices']+p['multiplicative_choices'] if v=='original']
        for d in [1,2,3]:
            weights=[0]*len(row['local']);weights[p['zero_index']]=d
            old=OLD.compute(i,d,e=(d%3)-1)
            new=G.compute(p['entry'],p['profile'],p['a'],d*p['b'],weights,original=original,e=(d%3)-1)
            assert old['homology']==new['homology']
            results.append(dict(pattern=i,weight=d,homology=new['homology']))
    print('Full D41 overlap Smith comparisons',len(results),flush=True)
    return results

def new_examples():
    examples=[]
    for key,info in G.PROFILES.items():
        entry,profile=key;d0=Fraction(info['height_matrix'][0][0]).denominator
        # Both sections narrow, then P a nonunit at some reducible fibre.
        for a,b in [(d0,d0),(2,d0),(3,d0)]:
            height=a*b//d0
            regular_weights=[0]*len(info['kodaira_types'])+[height]
            original=[j for j in range(len(info['kodaira_types']))]
            for originals in [[],original]:
                r=G.compute(entry,profile,a,b,regular_weights,original=originals,e=1)
                examples.append(r)
        # A positive noncyclic cusp and a second regular zero whenever possible.
        i=next((j for j,k in enumerate(info['kodaira_types']) if k.startswith('I') and k[1:].isdigit()),None)
        if i is not None:
            weights=[0]*len(info['kodaira_types']);weights[i]=2;weights.append(1)
            r=G.compute(entry,profile,3,d0,weights,e=-1)
            examples.append(r)
        print('General initial examples',entry,profile,'completed',flush=True)
    sample=G.compute(45,'default',2,8,[2,0,0,0,0],e=1)
    assert sample['homology'][2]==dict(free=15,torsion=[8])
    assert sample['homology'][3]==dict(free=0,torsion=[8])
    examples.append(sample)
    print('General initial full Smith examples',len(examples),flush=True)
    return examples

if __name__=='__main__':
    constant_certificates()
    overlap=overlap_checks()
    examples=new_examples()
    (ROOT/'manifolds_general_initial_audit.json').write_text(
        json.dumps(dict(scope=__doc__,old_overlap=overlap,new_examples=examples),indent=2,default=int)+'\n')
