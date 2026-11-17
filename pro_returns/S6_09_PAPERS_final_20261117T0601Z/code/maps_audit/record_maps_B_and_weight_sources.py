"""Append narrowly scoped original-source openings without replacing history."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / 'deliverables/work/maps_audit'
META = dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17')

def source(key, filename, url, locators, scope, limits, applications):
    path = 'sources/external/maps_audit/' + filename
    return dict(key=key, source=path, sha256=hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),
                url=url, opened_locators=locators, verification_scope=scope, limits=limits,
                applications=applications, status='verified in the specified scope', **META)

rows = [
    source('mapsAPS2','aps2.pdf','https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps002.pdf',
           ['Section4, equations(4.11)–(4.14), printed pp.422–424; searchable text774–893',
            'Theorem(4.14), printed p.423 (PDF p.19), original formula visually checked'],
           'For a parallelism on a (4k-1)-manifold the original real Adams invariant is epsilon(k) times the reduced Dirac eta invariant minus its connection transgression. The exact coefficient is epsilon(k)=1/2 for k odd. On the flat Lie-framed T3, k=1, the connection term is zero, paired Fourier eigenvalues give eta=0, and periodic spinors have complex dimension2. Hence the real invariant is (1/2)(2/2)=1/2 modZ. The complex invariant alone would be0 and is not substituted for the real one.',
           'The exact formula and its printed derivation were read; no full independent verification of the APS boundary index theorem is asserted.', ['MAPS:B.1.2']),
    source('mapsToda52','toda1952.pdf','https://www.i-repository.net/contents/osakacu/sugaku/DB-M-002-02-01.pdf',
           ['Section4 Theorem(4.1), Corollaries(4.2)–(4.4), and complete printed proof, pp.76–78; text308–446',
            'Original pp.76,77,79 visually opened, including the double-suspension relation at the start of p.79'],
           'Theorem4.1 gives [i_n,i_n]=2{h_n}-E(alpha_(n-1)); Corollary4.2 gives E2(alpha_(n-1))=2E{h_n}. Corollary4.3 states that some k-fold suspension pi6(S3)→pi(6+k)(S(3+k)), k>=2, is injective. These groups are in the stable range. Together with the separately opened pi6(S3)=Z/12 and stable pi3=Z/24 tables, the image is the unique order12 subgroup. Thus the order2 stable class12nu determines the unique order2 unstable class6nu-prime. The source convention for the Hopf map is explicitly stated on p.76.',
           'Toda is used for suspension and normalization. The actual framed torus, its ambient comparison, and its APS evaluation are receiving-proof computations, not statements attributed to Toda.', ['MAPS:B.1.2']),
    source('mapsBott59','bott1959.pdf','https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bott.pdf',
           ['TheoremII and its corollary, pp.314–315; text90–167',
            'Original stable orthogonal period table, printed p.315 (PDF p.4), visually opened'],
           'The period for pi_k(O), k=0,...,7, is Z/2,Z/2,0,Z,0,0,0,Z. In positive degree SO has the same homotopy; the universal Spin cover removes pi1 and preserves groups of degree>=2. Hence the stable groups used in B1.1 are pi1Spin=pi2Spin=0, pi3Spin=Z, pi4Spin=0, and pi6SO=0. The six-sphere stable framing difference is zero, and the three-dimensional Spin comparison reduces to H3.',
           'Only the exact stable-group statement is certified here. No unstable SO6 group is silently replaced by the stable one.', ['MAPS:B.1.1','MAPS:B.1.2']),
    source('mapsWaldhausen68','waldhausen1968.pdf','https://www.maths.gla.ac.uk/~mpowell/Waldhausen-Irreducible3ManifoldsSufficiently-1968.pdf',
           ['Introductory compact orientable PL convention, p.56',
            'Theorem6.1, printed p.77 (PDF p.23), text1075–1110; exact statement visually opened',
            'Corollary6.5 and its printed proof, p.80; text1244–1272'],
           'The target T2xI is sufficiently large; source and target are irreducible and boundary-irreducible, with nontrivial source pi1. The receiving construction gives a boundary-preserving map inducing a pi1 isomorphism and the prescribed boundary homeomorphisms. Theorem6.1 fixes these boundary maps throughout the homotopy. Its product-into-one-boundary alternative is impossible because the two source boundary components map to distinct target components. The remaining covering has degree1. The positive toric charts in maps_B.tex762–765 are manifolds with corners which are rounded before this compact PL theorem is applied.',
           'This supplies a product homeomorphism relative to the marked boundary, not preservation of an additional radial function. Theorem6.1 was opened and its exact hypotheses matched; its entire hierarchy proof was not independently re-proved.', ['MAPS:B.5.1']),
    source('mapsDeligne1974HodgeIII','deligne1974_hodge_iii.pdf','https://www.numdam.org/item/10.1007/BF02685881.pdf',
           ['Scholie8.1.9, printed p.30; text1164–1217',
            'Theorem8.1.15, printed pp.32–33, complete statement and printed proof8.1.17; text1252–1432, including Lemma8.1.18,8.1.19 and Proposition8.1.20',
            'Proposition8.3.5 and its complete printed proof, pp.42–43; text1685–1749; p.42 (PDF p.39) visually opened'],
           'Proposition8.3.5 makes E1^(p,q)=H^q(X_p,Z)⇒H^(p+q)(X_bullet,Z) a spectral sequence of mixed Hodge structures for a separated simplicial scheme. At C3=0 the finite 2Z3 toroidal cover has smooth projective toric strata and algebraic face maps. Add the degenerate simplices to the finite normalization semisimplicial scheme; its normalized alternating complex is unchanged. Each H^q(stratum,Q) is pure of weightq, so E2^(p,q) is pure of weightq. For r>=2 the differential changes q to q-r+1 and is therefore zero. Finite deck invariants are exact overQ. The explicitly computed integral E2 groups are free, so rational vanishing implies integral vanishing inductively, and extensions of free abelian groups remain free.',
           'This is the Hodge III source for the normalization weight argument; the separately opened Deligne1970 regular-connections book does not supply this scope. Integral invariant-cycle surjectivity is not inferred from mixed-Hodge degeneration: it uses the separately printed explicit line-bundle descent and saturated lattice calculation.', ['MAPS:E.1.3','MAPS:F.2.5','MAPS:F.2.6'])
]
(W/'maps_B_and_weight_source_checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
refs=json.loads((W/'references_verified.json').read_text())
for row in rows:
    target=next((x for x in refs if x.get('key')==row['key']),None)
    if target is None: refs.append(row)
    elif target != row:
        target.setdefault('additional_dated_checks',[])
        if row not in target['additional_dated_checks']: target['additional_dated_checks'].append(row)
(W/'references_verified.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')

events=[
    dict(event_id='new-maps-B-homotopy-source-closure-20261117',results=['MAPS:B.1.1','MAPS:B.1.2','MAPS:B.2.1'],
         scope='Closed the exact Bott, real APS, and Toda primary-source gates after the previously recorded full receiving-proof reads.',
         outcome='The stable framing and two retained evaluations of the canonical quotient pass these source checks. B2.1 retains both its weighted-Hopf proof and the independent divisor-root homotopy.',
         source_check_keys=['mapsBott59','mapsAPS2','mapsToda52'],
         remaining_dependencies=['The explicit map construction is printed in PaperI under mapsI:src:A.2.1. Stable group tables and Hatcher homotopy locators retain their own earlier checks.'],**META),
    dict(event_id='new-maps-B-cusp-product-source-closure-20261117',results=['MAPS:B.5.1'],
         scope='Closed the exact Waldhausen boundary-relative product theorem after the previously recorded full cusp-coordinate proof read.',
         outcome='All compact orientable PL, irreducibility, incompressible-boundary, sufficiently-large-target, pi1 and boundary conditions match. No radial-preservation claim is added.',
         source_check_keys=['mapsWaldhausen68'],remaining_dependencies=['The integral cap/CW calculation B5.2 has a separate full receiving read and its finite program is checked separately.'],**META),
    dict(event_id='new-E13-pure-weight-source-closure-20261117',results=['MAPS:E.1.3'],
         scope='Closed the exact original mixed-Hodge spectral-sequence source and the projective toric normalization hypotheses.',
         outcome='Rational weight degeneration and its integral free-E2 consequence pass. Chen local invariant cycles and explicit integral specialization remain distinct checked steps.',
         source_check_keys=['mapsDeligne1974HodgeIII','ffChen'],remaining_dependencies=['The normalization incidence matrices and integral wedge/saturation calculations retain their separate exact program records.'],**META)
]
(W/'maps_B_and_weight_application_checks.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
old=json.loads((W/'check_events.json').read_text());known={x.get('event_id') for x in old}
old.extend(x for x in events if x['event_id'] not in known)
(W/'check_events.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
audit=json.loads((W/'results_audit.json').read_text())
for row in audit:
    for e in events:
        if 'MAPS:'+row['id'] not in e['results']:continue
        row.setdefault('check_event_ids',[])
        if e['event_id'] not in row['check_event_ids']:row['check_event_ids'].append(e['event_id'])
        row.setdefault('additional_check_records',[])
        if e not in row['additional_check_records']:row['additional_check_records'].append(e)
        row.setdefault('source_check_keys',[])
        for key in e['source_check_keys']:
            if key not in row['source_check_keys']:row['source_check_keys'].append(key)
(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('Appended five exact primary-source scopes and three receiving-application events.')
