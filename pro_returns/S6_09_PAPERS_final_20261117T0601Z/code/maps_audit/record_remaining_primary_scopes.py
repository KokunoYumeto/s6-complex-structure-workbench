"""Retain exact versions and hypotheses for the remaining MAPS primary inputs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];W=ROOT/'deliverables/work/maps_audit'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
def row(key,source,url,locators,scope,limits,applications):
 return dict(key=key,source=source,sha256=hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),url=url,
             opened_locators=locators,verification_scope=scope,limits=limits,applications=applications,
             status='verified in the specified scope',**META)
P='sources/external/maps_audit/'
rows=[
 row('mapsKrylov03',P+'krylov2001v1.pdf','https://arxiv.org/pdf/math/0107005',
     ['Exact author version arXiv:math/0107005v1,1July2001, not asserted to be a page-identical journal scan',
      'Section2.1, complete definition of the normal-framing homomorphism and equation(2), pp.2–3; text62–122',
      'Theorem2 and complete printed proof, pp.10–12; Theorem3 and its preceding calculation, pp.12–13; text399–555'],
     'For M=S3xS3, the framed bounding S3xD4 verifies the hypothesis which makes Theta7 inject into the Torelli group. The quotient is Hom(H3(M),image(pi3SO3→pi3SO4)). The proof of Theorem2 computes the stable Pontryagin number of its generator as absolute value4; therefore the receiving zero integral p1 on the two Wang generators detects the entire normal-framing homomorphism. Theorem3 also gives the quaternionic relation (YUY)^4=Sigma_Milnor^-1 used only as a historical comparison in B6.2.',
     'Kreck’s theorem is explicitly credited as the input restated by Krylov. The source does not identify the actual family transport with a plumbing word; the manuscript retains that limitation.', ['MAPS:B.6.2','MAPS:B.6.4']),
 row('mapsCrowleyNordstrom19',P+'crowley_nordstrom2019v3.pdf','https://arxiv.org/pdf/1406.2226v3',
     ['Exact author version3,29December2018; §1 opening spin/orientation conventions',
      'Section1.4, equations(2)–(3), manuscript p.5; text260–278'],
     'The classical invariant applies to any closed spin seven-manifold with torsion spin Pontryagin class; two-connectivity is not a hypothesis of this formula. The displayed invariant is (p_W^2-sigma(W))/8 in Q/28Z with p_W=p1(W)/2. Dividing by28 gives (p1(W)^2-4sigma(W))/896 in Q/Z. The receiving mapping tori are spin and have integral p1=0; both chosen spin structures are tracked by the actual trace.',
     'Only the classical invariant and its normalization are used here, not the paper’s full two-connected classification theorem. Journal2019 and author2018v3 dates are kept distinct.', ['MAPS:B.6.5','MAPS:B.6.6']),
 row('mapsCrowleyNordstrom21',P+'crowley_nordstrom2021_published.pdf','https://link.springer.com/content/pdf/10.1007/s00208-020-02009-1.pdf',
     ['Published edition MathAnn381(2021)29–74, online8June2020; §2.1 pp.34–35',
      'Lemma2.1 and §2.2 equation(2.1), published p.35 (PDF7), visually opened; matching authorv4 pp.4–5 separately read'],
     'The boundary is a closed spin7-manifold with torsion-free H4, and the actual Spin-c coboundary has a determinant class with a relative lift. With p1(boundary)=0 the source normalization is Z/28. Substituting p-hat=(p1+z^2)/2 and dividing by28 yields (p1^2-4sigma)/896-p1*z^2/192+z^4/384, exactly B6.9. Its relative products and the zero-shear case are verified in the receiving proofs; both spin lifts induce the same boundary Spin-c structure when H2 vanishes.',
     'The published2021 formula is opened directly; no silent author-version substitution is needed. This does not supply a filling whose existence has not been constructed.', ['MAPS:B.6.9','MAPS:B.6.15','MAPS:B.6.19','MAPS:B.6.24']),
 row('mapsShioda90','sources/external/root/retrieved/Shioda90.pdf','https://rikkyo.repo.nii.ac.jp/record/10027/files/AA00610867_39-02_05.pdf',
     ['Retained original reprint pagination: standing hypotheses(1.1), p.3; text96–130',
      'Lemma2.7 equation(2.16), Theorem2.8 equations(2.17)–(2.19), p.8; text284–315',
      'Lemmas8.1–8.3, Theorems8.4 and8.6–8.9, Corollary8.10, all complete printed proofs, pp.19–23; text717–928',
      'Proposition8.12 equation(8.25) and complete printed proof, reprint p.24; text935–957'],
     'The actual auxiliary surface is smooth projective, relatively minimal, has the pulled-back zero section and singular I1 fibres, so the original standing hypotheses hold. The degree12 extension multiplies height1/6 to2. With chi=1 and no reducible fibres the height formula gives P.O=0 and (P-O)^2=-2. Orthogonal section projection is equivariant and injective modulo torsion; the narrow lattice is even. These are the exact geometric lattice/degree inputs in B6.10–13.',
     'The retained scan uses reprint pages19–24, not a guessed journal-page conversion. Theorem2.8 cites Bombieri–Mumford/Kodaira for its canonical-bundle proof; the exact theorem was checked, not those entire source papers.', ['MAPS:B.6.10','MAPS:B.6.11','MAPS:B.6.12','MAPS:B.6.13']),
 row('mapsGriffiths68II',P+'griffiths1968II.pdf','https://publications.ias.edu/sites/default/files/periodsofintegralII68.pdf',
     ['Original journal scan, §II.1(a), precise analytic-fibre-space hypotheses and Theorem(1.1), p.809',
      'Complete printed proof of Theorem(1.1), including Lemmas1.6/1.8/1.10 and Proposition1.11, pp.810–813; text225–518'],
     'A proper holomorphic submersion with compact Kähler fibres over a small polydisc has a holomorphic Hodge-filtration period map in the locally constant marking. The locally simultaneous minimal elliptic pullbacks in B6.12 are smooth projective surfaces and therefore satisfy these hypotheses. Their finite deck characters define holomorphic eigensubbundles. Nonconstant period maps and exclusion of rational Hodge loci then use the separately computed hyperbolic monodromy and signatures.',
     'The theorem proves holomorphic variation; the nonconstancy and exact Mordell–Weil norm image are receiving results. The printed proof imports the Kuranishi analytic-coordinate lemma; no independent reproof of Kuranishi theory is asserted.', ['MAPS:B.6.12']),
 row('mapsRandalWilliams25',P+'randal_williams2025v2.pdf','https://arxiv.org/pdf/2308.06397v2',
     ['Exact author version2,21January2025; Theorem4.1 and complete printed proof, pp.12–13; text676–718',
      'Publisher correction DOI10.1007/s00208-024-02990-x, published online20September2024, issue2025 pp.2005–2006, completely opened; retained randal_williams_correction2025.pdf'],
     'The theorem concerns the degree-d hypersurface family, d>=3, and obtains the Milnor-sphere subgroup from an actual embedded A2 plumbing and its two Dehn twists. Its proof imports Krylov’s (YUY)^4 relation. B6.2 cites this as an example of the additional smooth identification that would be required by the abandoned plumbing approach; it does not apply the hypersurface theorem to the present torus family.',
     'The publisher correction repairs arrow typography and brace size in TheoremB/equation7; it does not change Theorem4.1. No global family comparison is claimed.', ['MAPS:B.6.2']),
 row('mapsJin26',P+'jin.pdf','https://arxiv.org/pdf/2608.26698v2',
     ['Exact version2,12September2026; convention before Theorem1.2 and Corollary1.3, p.3',
      'Lemma2.1 and its complete injectivity proof, pp.7–8; source previously read in new-maps-fixed-conifold-read-20261117 and reopened text368–412',
      'Proposition3.1 p.10; Lemma4.4 p.16; Lemma4.8 and g=1 invariant table pp.23–24; Theorem4.9 p.24, reopened at text514–553,900–924,1275–1363'],
     'The actual quotient is S2xS3, spin and simply connected with no torsion in homology. Preserving the primitive circle Euler class and orientation makes the return Torelli. The source is an isotopy classification, using Lemma2.1, not merely a rational characteristic detection. Its primitive and doubled-sphere twists have (cube,p1*x)=(1,4),(8,8). Thus their bordism coordinates ((4k-ell)/24,k) are (0,1),(1,8), an integral basis; ell=-4 gives A+2B=-1 and k=-1+6B.',
     'This verifies the precise classification and generator normalization. The actual family’s cubic k is supplied by the later collar proof; the source does not by itself evaluate it.', ['MAPS:B.6.18']),
 row('ffDeligne',P+'deligne1971_hodge_ii.pdf','https://publications.ias.edu/sites/default/files/Number15.pdf',
     ['Original HodgeII(1971), conditions4.2.2, Lemma4.2.3, Definition4.2.4 and Proposition4.2.5, pp.43–45',
      'Theorem4.2.6 and complete printed proof via Lemma4.2.7, pp.45–46; text1790–1932'],
     'F3.4 explicitly assumes an algebraic polarized abelian-surface family. Its smooth proper algebraic cohomology is an algebraic Hodge family under Definition4.2.4/Proposition4.2.5, so Theorem4.2.6 gives a semisimple rational monodromy representation. The invariant summand splits globally; N_W has kernel=image of dimension2 and vanishes on that summand, which forces it to be zero. This global algebraic hypothesis is essential.',
     'This is HodgeII1971, not HodgeIII1974 or the1970 regular-connections book. No claim of semisimplicity for an arbitrary punctured-disc unipotent local system is made.', ['MAPS:F.3.4']),
 row('ffAlarconForstneric25',P+'oka.html','https://link.springer.com/article/10.1007/s00209-025-03833-4',
     ['Published2025 full text: Definitions2.1,7.7,7.11, Theorem2.2, Proposition7.13 and its printed proof',
      'Lemma5.1 spray construction and gluing, equations5.6–5.8; Theorem2.13 exact Mergelyan/jet statement; extracted text1390–1451,1096–1102,1664–1775'],
     'The printed spanning tubes supply LSAP, and Proposition7.13(d), rather than the unresolved general Oka-1 fibre-bundle question7.10, supplies the section theorem. For F3.10 the vertical spray dominates on the attaching discs away from the finite fixed-jet set, exactly as in5.6–5.8. At a critical arc the compact set has the Mergelyan property; the fixed jet points lie in its interior. After a holomorphic frame is chosen, Theorem2.13 applies to Grassmannian-valued maps, leaving the base coordinate fixed.',
     'Approximation is on compact subsets of the open Riemann surface. It does not imply uniform estimates at all punctures; F3.11 retains only its explicit one-cusp bounded-correction scope. The source theorem’s own proof references for spray gluing remain credited.', ['MAPS:F.3.8','MAPS:F.3.9','MAPS:F.3.10','MAPS:F.3.11']),
 row('ffForstnericPrezelj02',P+'forstneric_prezelj2001v3.pdf','https://arxiv.org/pdf/math/0101040v3',
     ['Exact author version3,7May2002; Definition1.1, Theorem1.2 and Example1, printed p.3; text90–132'],
     'The frame bundle over the open Riemann surface is a holomorphic submersion over a Stein base with fibre GL(n,C). Its global vertical spray is (g,A)→g exp(A), and its derivative is onto the vertical tangent. A complex bundle over a graph has a continuous frame because GL(n,C) is connected. Theorem1.2 deforms that section to a holomorphic frame, which is the only use in F3.10.',
     'The precise opened-v3 locator is p.3, correcting the source bibliography’s p.2. The theorem is not applied to the noncompact period domain or to an unsupported relative puncture constraint.', ['MAPS:F.3.10'])
]
(W/'remaining_primary_source_checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
refs=json.loads((W/'references_verified.json').read_text())
for r in rows:
 old=next((x for x in refs if x.get('key')==r['key']),None)
 if old is None:refs.append(r)
 elif old!=r:
  old.setdefault('additional_dated_checks',[])
  if r not in old['additional_dated_checks']:old['additional_dated_checks'].append(r)
(W/'references_verified.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
events=json.loads((W/'check_events.json').read_text());known={x.get('event_id') for x in events}
audit=json.loads((W/'results_audit.json').read_text())
for r in rows:
 eid='new-maps-primary-scope-20261117:'+r['key']
 e=dict(event_id=eid,results=r['applications'],scope=r['verification_scope'],outcome='Exact original statement/version and receiving hypotheses checked in the recorded scope.',source_check_keys=[r['key']],limits=r['limits'],**META)
 if eid not in known:events.append(e)
 for a in audit:
  if 'MAPS:'+a['id'] not in r['applications']:continue
  a.setdefault('check_event_ids',[])
  if eid not in a['check_event_ids']:a['check_event_ids'].append(eid)
  a.setdefault('source_check_keys',[])
  if r['key'] not in a['source_check_keys']:a['source_check_keys'].append(r['key'])
(W/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('Appended ten scoped original-source records, preserving all previous checks.')
