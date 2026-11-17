"""Record exact primary openings and receiving-hypothesis comparisons."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / 'deliverables/work/maps_audit'
META = dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17')
def row(key, source, url, locators, scope, limits, applications):
    p = ROOT / source
    return dict(key=key, source=source, sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                url=url, opened_locators=locators, verification_scope=scope,
                limits=limits, applications=applications, status='verified in the specified scope', **META)

rows = [
    row('ffNikulin', 'sources/external/maps_audit/nikulin1980.pdf',
        'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1677&what=fullteng',
        ['Original English Corollary 1.9.4, printed p.116 (PDF p.14), text lines690–695, visually verified',
         'Original English Theorem 1.14.2 and its printed proof, p.125 (PDF p.23), text1147–1167, visually verified'],
        'In F4.1 the complement K is even and indefinite of signature (2,1), rank3, with discriminant group Z/2 and quadratic value +1/2. Corollary1.9.4 identifies its genus with U+<2>. Theorem1.14.2(a) requires rank >= odd-primary length+2, here 3>=2. Its extra 2-primary clause applies only at rank=length, whereas 3>1 here. The unique-genus conclusion applies. The extension to the odd unimodular ambient lattice is proved directly by its unique order-two gluing graph; the source theorem is applied only to the even complement.',
        'This checks the cited exact statements and the printed p.125 proof, not all local-lattice classification results referenced inside Nikulin. The stale hashed PDF URL redirected to the journal homepage; retrieval succeeded through the actual English-version link.', ['MAPS:F.4.1']),
    row('ffBHS', 'sources/external/maps_audit/bhs2019v2.pdf',
        'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/BHS19.pdf',
        ['Version2, December2,2019; conventions §1.2 p.6',
         'Recollections2.2–2.3 p.7; Definitions2.4–2.5 and Theorem2.6 p.8; p.8 visually verified'],
        'The Wall theorem is stated for closed smooth oriented (n-1)-connected 2n-manifolds; all diffeomorphisms preserve orientation. For n=4 the middle lattice and normal-bundle function determine the connected-sum orbit under Theta8. The receiving proof reconstructs the rank-four normal clutching class from its Euler and Pontryagin numbers: (a,b) maps to (a-b,-2(a+b)), an injective homomorphism. Thus matching intersection forms and p1 matches the full n-space, not merely its stable rational image.',
        'The classification statement is credited to Wall in this research paper. No use is made of the high-dimensional inertia remark2.7 or of the paper’s asymptotic main theorem, neither of which supplies the dimension-eight inertia conclusion.', ['MAPS:F.4.1']),
    row('ffNagy2026', 'sources/external/maps_audit/nagy.html',
        'https://www.cambridge.org/core/journals/compositio-mathematica/article/extended-surgery-theory-for-simplyconnected-4kmanifolds/85B4255F03634F86890D193F39350770',
        ['Publisher Theorem1.4; §1.4 Theorems1.7–1.8',
         '§9 Definition9.1, Propositions9.2/9.5/9.6/9.7, Theorem9.8 and final proofs of1.8/1.4; complete mathematical text opened, including the divisibility conversion',
         'Searchable original extraction nagy_paragraphs.txt31–32,49–59,564–600; complete §9 extraction nagy_section9_complete.txt1–504'],
        'The exact theorem gives I(M)=0 iff p1 is divisible by8 for a closed 3-connected 8-manifold; otherwise I(M)=Theta8=Z/2. Its §9 proof identifies the normal-type bordism kernel and uses q=4 in the free-Hq Q-form theorem. The final formula d_M=2 alpha_M makes the criterion 4|alpha_M equivalent to8|d_M. The receiving manifold has p1=2(1,1,1,1), divisibility2; therefore both homotopy-sphere possibilities are absorbed with the given orientation.',
        'This is an exact theorem/application check and a reading of its §9 derivation, not an independent verification of the whole extended-surgery theory or the Senger–Zhang stable calculation imported by Theorem1.7.', ['MAPS:F.4.1']),
    row('ffChen', 'sources/external/maps_audit/chen2021.pdf',
        'https://qymath.github.io/Steenbrink.pdf',
        ['Author manuscript dated September1,2021, title page',
         'TheoremA and surrounding hypotheses pp.2–3; TheoremB p.4, exact sequence visually verified'],
        'E1.3 uses the C3=0 family after the finite deck-lattice cover 2Z^3. The already printed properness proof and unimodular toric charts give a proper holomorphic map, smooth away from0, with smooth total space and SNC central fibre. The strictly coherent positive quadratic function Q=4 sum n_i^2-(sum n_i)^2 supplies a relative projective polarization, hence a Kähler total space over the disc. These are Chen’s exact hypotheses. Complex surjectivity onto monodromy invariants implies rational surjectivity by scalar extension; finite deck invariants are exact over Q.',
        'Chen is not used as an integral invariant-cycle theorem. Integral surjectivity in E1.3 is established separately by the printed line-bundle descent, wedge products and saturated kernel calculation. The pure-weight degeneration of the normalization complex is a separate Deligne source gate.', ['MAPS:E.1.3', 'MAPS:F.2.5', 'MAPS:F.2.6']),
    row('ffMandal', 'sources/papers/arXiv_2609.27929_Mandal_src/FINAL.tex',
        'https://arxiv.org/abs/2609.27929',
        ['Attached original source lines1–315: title, conventions, Theorems1.1/1.3, Corollary1.4',
         'Lines465–564: connected-sum cohomology and normalized Pontryagin formula with printed proof',
         'Section5 lines1398–1493: Corollary1.4 complete proof and precise orientation qualification'],
        'The original criterion concerns the stated orientation on l HP2 # m(-HP2): almost-complex existence iff l=2m+1 with m odd. The proof substitutes p1=2 sum x_i, p2=7(l-m)u and Euler number l+m+2 in the stable congruence and Euler obstruction. At (l,m)=(3,1) both conditions hold. The normalized basis and sign on the negatively oriented summand agree with F1.3 and the comparison manifold of F4.1.',
        'This result is known and must be credited to Mandal; it does not identify a newly constructed manifold up to diffeomorphism. F2.5 instead proves its relative almost-complex extension directly, before smooth classification. No scope is claimed for the later separately listed Mandal preprint.', ['MAPS:F.1.3', 'MAPS:F.4.1'])
]
(W/'fourfold_priority_source_checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
old=json.loads((W/'references_verified.json').read_text())
keys={x.get('key') for x in old}
for r in rows:
    if r['key'] not in keys: old.append(r)
    else:
        target=next(x for x in old if x.get('key')==r['key'])
        target.setdefault('additional_dated_checks',[])
        if r not in target['additional_dated_checks']:target['additional_dated_checks'].append(r)
(W/'references_verified.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')

checks=[
 dict(event_id='new-fourfold-F41-source-closure-20261117',results=['MAPS:F.4.1'],
      scope='Reopened every named classification source and matched all receiving hypotheses; retained earlier full receiving-proof reading and recorded reviews.',
      outcome='Nikulin genus/uniqueness, Wall full normal invariant via BHS, and Nagy exact inertia gates pass. Prior scoped records remain unchanged.',
      locator='fourfold_priority_source_checks.json entries ffNikulin/ffBHS/ffNagy2026; source F4.1 lines3–82.',
      independent_derivation='For primitive characteristic v with v²=2, K=v-perp is even, determinant2 and signature(2,1). If (w,v)=1, characteristicity gives w² odd; k=w-v/2 has discriminant square1/2. The unique nontrivial order-two gluing extends a complement isometry. Normal Euler/p1 pair is injective on pi3Spin4. Divisibility(p1)=2 excludes8-divisibility, so the full Theta8 ambiguity is absorbed.',
      remaining_dependencies=['Root-owned F3.7 complex realization and upstream characteristic-number/three-connectivity results retain their separate records.'], **META),
 dict(event_id='new-fourfold-relative-AC-extension-20261117',results=['MAPS:F.2.5'],
      scope='Rechecked the actual relative almost-complex extension in F2.5, independent of Mandal’s connected-sum criterion.',
      outcome='Passes as printed; the boundary sections extend over the actual two-dimensional pair of pants.',
      locator='sources/returns/S6_04_MAPS_MANIFOLDS/sections/fourfolds.tex985–1011',
      independent_derivation='The oriented linear-complex-structure fibre retracts to SO6/U3. Both groups are connected, and pi1(U3)=Z→pi1(SO6)=Z/2 is onto via rotation in one complex coordinate. The quotient is connected and simply connected. Extend a prescribed section on boundary collars over relative zero-, one-, and two-cells; the only obstructions use pi0 and pi1 and vanish. Smooth relative approximation is performed in the smooth bundle. Choose the given J-invariant horizontal distributions on boundary collars and extend them using the affine space of splittings; combining the extended vertical J and base J reproduces the filling structures on collars.',
      remaining_dependencies=['The three actual fillings and their boundary markings are the receiving construction; Chen and pure-weight scopes belong to E1.3, separately recorded.', 'Root owns full F program reruns.'], **META),
 dict(event_id='new-B611-PUSH-A4-prerequisite-20261117',results=['MAPS:B.6.11'],
      scope='Personally reopened the exact upstream integral H2 and small exceptional-curve computations after parent supplied their precise locations.',
      outcome='The needed rank and nullhomology input is closed; the former A2.2-only pointer should cite both printed I results.',
      locator='sources/returns/S6_02_PUSH/sections/AB_push.tex855–881 and1067–1082; PaperI push:src:A.4.1 and push:src:A.4.4.',
      independent_derivation='The nodal generizations (a,b)→(a,a+b) have determinant1, so R²h*Z is the normalization pushforward. Its only nonzero base cohomology is free in degrees0,2. The Leray rows are free and even, hence collapse and add one H² generator. Equal branch values imply b=0; every global section has degree0 on the small exceptional curve, as do pulled-back classes. Leray exhausts H², so the curve is nullhomologous.',
      remaining_dependencies=['B6.11 own program/source records remain separate.'], **META)
]
events=json.loads((W/'check_events.json').read_text());ids={x['event_id'] for x in events}
events.extend(x for x in checks if x['event_id'] not in ids)
(W/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
(W/'fourfold_priority_application_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
audit=json.loads((W/'results_audit.json').read_text())
for e in checks:
    for x in audit:
        if 'MAPS:'+x['id'] in e['results']:
            x.setdefault('check_event_ids',[])
            if e['event_id'] not in x['check_event_ids']:x['check_event_ids'].append(e['event_id'])
            x.setdefault('additional_check_records',[])
            if e not in x['additional_check_records']:x['additional_check_records'].append(e)
            x.setdefault('source_check_keys',[])
            for r in rows:
                if 'MAPS:'+x['id'] in r['applications'] and r['key'] not in x['source_check_keys']:x['source_check_keys'].append(r['key'])
(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('Recorded five scoped primary checks and three receiving-application events; retained earlier audit events.')
