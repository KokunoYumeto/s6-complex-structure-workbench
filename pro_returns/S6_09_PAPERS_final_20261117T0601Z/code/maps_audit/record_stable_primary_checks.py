"""Append only source passages actually opened and mathematically compared."""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[3]
W=ROOT/'deliverables/work/maps_audit'
EXT=ROOT/'sources/external/maps_audit'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
def artifact(name):
 p=EXT/name
 return dict(source=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
def row(key,title,url,archive,files,locators,scope,limits,applications,corrections=None):
 return dict(key=key,title=title,url=url,**artifact(archive),source_files=[artifact(x) for x in files],
             opened_locators=locators,verification_scope=scope,limits=limits,applications=applications,
             original_version_corrections=corrections or [],status='verified in the specified scope',**META)

rows=[
row('mapsGoerss2008','The Adams–Novikov spectral sequence and the homotopy groups of spheres',
 'https://arxiv.org/abs/0802.1006v1','goerss2008v1.tar',['goerss2008v1_source/stras1.tex'],
 ['Original stras1.tex lines1–601, including the full initial classical Adams construction, cohomological variance, tower/exact-couple discussion, normalized cobar description, and the stated low-line formulas; source identity at32–45'],
 'The receiving proof retains the actual variance H*(Y)→H*(X) for f:X→Y and proves its own finite-tower convergence. The classical normalized cobar construction is compared with the explicit field-coefficient cofree construction. Bounded-below/finite-type hypotheses in the source are not silently discarded.',
 'No reading of later lecture sections is claimed. The source has a displayed vanishing inequality contradicted by its own first Ext line; the receiving proof does not assume a repaired general vanishing line. The macros and bibliography are not part of this current mathematical opening claim.',
 ['CG-S6 Adams-tower chapter §§1–6; source-correction paragraph','CG-S6 actual-mod-two Adams-resolution chapter, comparison of conventions'],
 [dict(locator='stras1.tex133–139, compared with98–102',issue='The basic lemma reverses the two cohomology modules in the displayed target. The actual induced map is H*(Y)→H*(X).',receiving_resolution='Full functorial composition proof printed in Adams-tower §6.'),
  dict(locator='stras1.tex469–490, compared with440–459',issue='The printed inequality 0<t−s<2s+epsilon would kill (s,t)=(1,2), although the same source gives its nonzero h1 class.',receiving_resolution='Explicit primitive [zeta1²] nonboundary and independent adjacent-line/convergence proofs; no corrected general inequality is assumed.')]),
row('mapsDuggerIsaksen2009','The motivic Adams spectral sequence',
 'https://arxiv.org/abs/0901.1632v1','dugger_isaksen2009v1.tar',['dugger_isaksen2009v1_source/author.tex'],
 ['Original author.tex681–916, full coefficient, Adem, dual-algebra and localization passages',
  'Original author.tex1085–1148, full Ext localization proposition and proof',
  'Original author.tex2038–2504, complete opened convergence background, cofree/Kunneth constructions, smash-fibre tower and comparison-of-towers passages',
  'Source identity title/author lines428–431'],
 'Algebraically closed characteristic-zero motivic source conventions were checked against the receiving presented algebras. Cohomological tau has weight+1, homological tau weight−1; original coefficient rings are retained before inversion. The general-X tower is resolved from H**(X), and the cofree comparison has Ext target H**(X). The receiving field-coefficient construction prints both comparison maps and their homotopies, rather than importing motivic hypotheses as topological conclusions.',
 'The imported motivic geometric classification and Voevodsky/Röndigs–Østvær inputs are not being independently re-proved or promoted by this opening. The receiving algebraic results apply to the explicitly presented algebras, and the classical actual-cooperation proof is separate. No reading of intervening unlisted sections is claimed.',
 ['CG-S6 coefficient-ring chapter §§1–5,7.1–7.2','CG-S6 Adams-tower §6 general-X correction','CG-S6 actual-mod-two Adams-resolution comparison'],
 [dict(locator='author.tex770–771',issue='The conversion from zeta_i to tau/xi symbols has an index shift inconsistent with the displayed degrees.',receiving_resolution='Use zeta_i↔tau_(i−1) and xi_i with the full localized coefficient powers printed in the receiving inverse maps.'),
  dict(locator='author.tex881–882,895–896',issue='Negative coefficient exponents in the proof/corollary do not match the preceding positive-weight definition of theta; the odd exponent also has an index mismatch.',receiving_resolution='The receiving proof gives two explicit inverse maps on every original generator and verifies all Adem relations, with cohomological and homological coefficient variables distinguished.'),
  dict(locator='author.tex2362–2374, proof2391–2408',issue='The general-X lemma prints Ext(M2,M2) although its stated resolution starts in H**(X).',receiving_resolution='Use Ext_(H**H)(M2,H**(X)); the sphere specialization remains unchanged.')]),
row('mapsIsaksen2014','Stable stems',
 'https://arxiv.org/abs/1407.8418v2','isaksen2014v2.tar',
 ['isaksen2014v2_source/stable-stems-May.tex','isaksen2014v2_source/stable-stems-tables.tex'],
 ['stable-stems-May.tex280–460: coefficient and dual Hopf algebra, grading, May filtration, localization comparison',
  'stable-stems-May.tex904–1000: E1 generators, d1 formula, and d2(b20)',
  'stable-stems-tables.tex50–118: actual May E2 generator/differential table and first relation rows',
  'stable-stems.tex title/author lines72–74'],
 'Matched the exact low-degree classical formulas after coefficient inversion: d2(b20)=h1³+h0²h2 and d2(h0(1))=h0 h2². The receiving binary filtration is W=2m−s, so these May d2 operations are its weight-drop-three differential. The receiving complete all-length proof independently supplies the cochains, cancellations, exhaustive R-module bases and survival.',
 'Only the listed low-degree table/formula scope is checked; no general 70-stem computation or whole-paper proof verification is claimed. The motivic tau term is retained before localization.',
 ['CG-S6 Milnor-cobar §§2–5, May-filtration comparison','CG-S6 coefficient-ring source conventions']),
row('mapsIWX2020v1','Stable homotopy groups of spheres',
 'https://arxiv.org/abs/2001.04247v1','isaksen_wang_xu2020v1.tar',['isaksen_wang_xu2020v1_source/ms.tex'],
 ['Original ms.tex483–661: classical dual Steenrod coproduct, Adams conventions, complex-motivic coefficient algebra and displayed conversion',
  'Title/author identity43–73'],
 'Checked every displayed coefficient relation and coproduct in this passage against the receiving explicit localized Hopf maps. The conversion must preserve the degrees of zeta1, tau0 and xi1 and all powers of the original coefficient variable.',
 'This is a v1 convention check, not an opening of Theorem2.1 or Table1 or a verification of a stable-stem table. The separately opened 2023 Annals Table1 remains a distinct record.',
 ['CG-S6 coefficient-ring chapter §§1–2 and source correction'],
 [dict(locator='ms.tex652–654',issue='The text says tau_i and xi_(i+1) correspond to zeta_i and zeta_i², inconsistent with its zeta0=1 convention.',receiving_resolution='The explicit receiving inverse uses zeta_(i+1), with the necessary coefficient powers; the original-index mismatch is recorded only for this version.')]),
row('mapsLuecke2021','A short geometric derivation of the dual Steenrod algebra',
 'https://arxiv.org/abs/2109.00048v2','luecke2021v2.tar',['luecke2021v2_source/author.tex'],
 ['Entire original author.tex1–214, including all lemmas/proofs, MO orientation argument, final odd-prime remark and bibliography'],
 'Matched the characteristic-two zero-two-series/strict-coordinate argument and its intended geometric context. The receiving formal proof treats every coefficient over an arbitrary characteristic-two ring and constructs inverse coordinates in all degrees. Its actual projective-cooperation construction directly builds the required Hopf morphism and checks low-degree injectivity/surjectivity.',
 'The source geometric route uses MO_*MO, Thom/splitting principles and flat base change. Those are not imported as unexpanded prerequisites into the receiving actual-projective proof. The source explicitly defers the odd-prime derivation, so it is not credited as an odd-prime proof.',
 ['CG-S6 formal characteristic-two coordinate §§1–4, exercises','CG-S6 projective actual-cooperation construction: comparison and credit']),
row('mapsPetersonPinned','Formal geometry and bordism operations: pinned author source chapters',
 'https://github.com/ecpeterson/FormalGeomNotes/tree/2f1cd08cb4f7b7b643eec441eae78637bbb71973',
 'peterson_2f1cd08cb4f7_cooperations.tex',
 ['peterson_2f1cd08cb4f7_cooperations.tex','peterson_2f1cd08cb4f7_mo.tex'],
 ['Pinned cooperations.tex1–31 and59–353: unstable context, actual product distinction, complete mod-two iterated-bar argument, odd-prime remark, stabilization',
  'Pinned mo.tex32–241: Thom-space models, MO shear equivalence, Thom module map and projective cohomology example'],
 'Matched the iterated bar architecture, distinction between Pontryagin and spectrum products, stabilization by suspension and indecomposables, and the Thom/projective comparison. The receiving proof retains actual bar/prism chains, all signed shuffle identities, complete finite-degree indexing and the low-degree Hopf-kernel argument.',
 'This is the specified pinned author source, not a claim to have opened a particular printed book edition. The source cites Ravenel–Wilson/Wilson for certain Hopf-ring congruences; the receiving finite-degree argument does not import those unexpanded congruences. Only the listed chapter intervals were opened.',
 ['CG-S6 actual degree-eight cooperation comparison','CG-S6 original odd-prime cooperation calculation','CG-S6 original projective-coordinate chapter']),
row('mapsFriedman2023','An elementary illustrated introduction to simplicial sets',
 'https://arxiv.org/abs/0809.4221v8','friedman2008v8.tar',['friedman2008v8_source/simp-06-08-2023.tex'],
 ['Original simp-06-08-2023.tex756–898: geometric realization, degenerate-simplex uniqueness proof, CW statement and realization/singular adjunction',
  'Source identity112–135; printed revision date June8,2023 (original date December6,2011)'],
 'The realization quotient is taken over discrete simplex sets. Matched the nondegenerate-cell description and degeneracy identifications used by the finite-cocycle realization proof. The receiving chapter prints its own actual finite-skeleton/local-trivialization constructions.',
 'The source CW theorem refers to Milnor/May for its proof. This opening verifies its statement/context and the printed uniqueness/adjunction arguments; it is not a claim that a full CW proof is printed in Friedman. No unlisted simplicial fibration theorem is imported.',
 ['CG-S6 Adams-tower §§8–11, finite-cocycle realization context']),
row('mapsStrickland2024','Arithmetic localisation and completion of spectra',
 'https://arxiv.org/abs/2412.09361v1','strickland2024v1.tar',['strickland2024v1_source/author.tex'],
 ['Original author.tex1–185: definitions, ambient stable category and source scope',
  'Original author.tex241–524: bounded-below Hurewicz/CW construction, finite-spectrum criterion, Moore construction and mapping exact sequence',
  'Original author.tex568–600: original polynomial-shift construction of S[1/p], S/p-infinity and its cofibration',
  'Original author.tex1006–1401: derived-completion definitions, bounded torsion, completion fibre, universal mapping property, mod-p detection and finite-spectrum completion (plus beginning of later CW subsection)'],
 'Matched the actual free presentation delta−p, its extension unit and the function-spectrum completion. Bounded-below hypotheses for homological detection and finite-generation hypotheses for pi_*(X_p)=pi_*(X) tensor Z_p are retained. The receiving integral/arithmetic proofs give the full original transition maps and inverse-limit arguments, not merely an abstract completed-group isomorphism.',
 'No whole-paper read or proof of later finite-complete/Brown-representability sections is claimed. The last opened range ends inside the later p-complete CW definition. Two local slips in the proof of the universal mapping corollary are recorded below without altering its correct statement.',
 ['CG-S6 original integral stable group/completion maps','CG-S6 original Adams tower/arithmetic completion'],
 [dict(locator='author.tex1256',issue='The proof of cor-bousfield-hL(a) writes Y equivalent to Hom(S^(-1)/p-infinity,X), where the last variable must be Y; its next display already uses Y.',receiving_resolution='Use the target Y throughout the adjunction.'),
  dict(locator='author.tex1264',issue='The proof of (b) concludes p-local although the statement and split-retract argument give {p}-local (p invertible).',receiving_resolution='Retain the source definition and correct {p}-local conclusion, as in the receiving explicit proof.')]),
]
(W/'stable_primary_source_checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
for filename in ['references_verified.json','course_geometric_source_checks.json']:
 old=json.loads((W/filename).read_text()); keys={x.get('key') for x in old}
 old.extend(x for x in rows if x['key'] not in keys)
 (W/filename).write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
# Retain the original retrieval status and add the later scoped-reading record.
retrieval=json.loads((W/'stable_primary_retrieval.json').read_text())
for item in retrieval:
 matches=[x['key'] for x in rows if item['source']==x['source'] or any(item['source']==f['source'] for f in x['source_files'])]
 if matches:item['subsequent_scoped_readings']=dict(record='deliverables/work/maps_audit/stable_primary_source_checks.json',keys=matches,**META)
(W/'stable_primary_retrieval.json').write_text(json.dumps(retrieval,ensure_ascii=False,indent=2)+'\n')
bib=r'''@misc{mapsGoerss2008,
 author={Goerss, Paul}, title={The Adams--Novikov Spectral Sequence and the Homotopy Groups of Spheres},
 year={2008}, eprint={0802.1006}, archivePrefix={arXiv}, url={https://arxiv.org/abs/0802.1006v1},
 note={Version 1; Strasbourg lectures, May 2007. Only the recorded original-source scope was checked.}}
@misc{mapsDuggerIsaksen2009,
 author={Dugger, Daniel and Isaksen, Daniel C.}, title={The motivic Adams spectral sequence},
 year={2009}, eprint={0901.1632}, archivePrefix={arXiv}, url={https://arxiv.org/abs/0901.1632v1}, note={Version 1.}}
@misc{mapsIsaksen2014,
 author={Isaksen, Daniel C.}, title={Stable stems}, year={2014}, eprint={1407.8418},
 archivePrefix={arXiv}, url={https://arxiv.org/abs/1407.8418v2}, note={Version 2 author source; low-degree May passages and table entries checked.}}
@misc{mapsIWX2020v1,
 author={Isaksen, Daniel C. and Wang, Guozhen and Xu, Zhouli}, title={Stable homotopy groups of spheres},
 year={2020}, eprint={2001.04247}, archivePrefix={arXiv}, url={https://arxiv.org/abs/2001.04247v1}, note={Version 1; coefficient-convention scope only.}}
@misc{mapsLuecke2021,
 author={Luecke, Kiran}, title={A short geometric derivation of the dual Steenrod algebra},
 year={2021}, eprint={2109.00048}, archivePrefix={arXiv}, url={https://arxiv.org/abs/2109.00048v2}, note={Version 2.}}
@misc{mapsPetersonPinned,
 author={Peterson, Eric C.}, title={Formal geometry and bordism operations: author source chapters},
 howpublished={Author repository}, url={https://github.com/ecpeterson/FormalGeomNotes/tree/2f1cd08cb4f7b7b643eec441eae78637bbb71973},
 note={Pinned commit 2f1cd08cb4f7b7b643eec441eae78637bbb71973; cooperations.tex and mo.tex, exact scopes recorded. No publication date is inferred from the source checkout.}}
@misc{mapsFriedman2023,
 author={Friedman, Greg}, title={An elementary illustrated introduction to simplicial sets},
 year={2023}, eprint={0809.4221}, archivePrefix={arXiv}, url={https://arxiv.org/abs/0809.4221v8},
 note={Version 8; original text dated December 6, 2011, revised through June 8, 2023.}}
@misc{mapsStrickland2024,
 author={Strickland, N. P.}, title={Arithmetic localisation and completion of spectra},
 year={2024}, eprint={2412.09361}, archivePrefix={arXiv}, url={https://arxiv.org/abs/2412.09361v1}, note={Version 1.}}
'''
(W/'stable_primary_checked_references.bib').write_text(bib)
event=dict(event_id='new-stable-primary-scoped-readings-20261117',**META,
           scope='Opened and compared the exact original author-source passages listed in stable_primary_source_checks.json; original archives and extracted-file hashes retained.',
           outcome='Eight precise source/edition records appended to the shared reference ledger. Historical receiving-source corrections are confirmed only at their specified original-version locators.',
           reference_keys=[x['key'] for x in rows],record='deliverables/work/maps_audit/stable_primary_source_checks.json')
events=json.loads((W/'check_events.json').read_text())
if not any(x.get('event_id')==event['event_id'] for x in events):
 events.append(event);(W/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(references_added=len(rows),keys=[x['key'] for x in rows])))
