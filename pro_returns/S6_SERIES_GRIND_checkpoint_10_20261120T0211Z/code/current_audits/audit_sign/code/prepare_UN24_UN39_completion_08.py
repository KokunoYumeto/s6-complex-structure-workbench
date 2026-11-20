"""Prepare exact source/code guards and bounded row-completion proposals.

No shared body, bibliography, inventory or canonical assessment is modified.
"""
from pathlib import Path
import csv, datetime as dt, hashlib, json

WORK=Path(__file__).resolve().parents[2]; OUT=WORK/'audit_sign'
NOW=dt.datetime.now(dt.timezone.utc).isoformat()
WHO='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name,data):
    p=OUT/name;p.write_text(json.dumps(data,indent=2)+'\n')
    return {'path':str(p.relative_to(WORK)),'sha256':sha(p)}

evidence=json.loads((OUT/'II_95_exact_evidence_map_07.json').read_text())['records']
with (WORK/'S6_SERIES_GRIND_inventory.csv').open() as f:
    inventory={r['label']:r for r in csv.DictReader(f)}
bodypath=WORK/'parts/II.body.linked.tex';body=bodypath.read_text()
blocks={}
for n in [24,39]:
    a=body.index('\\label{cdp:st:C.2.UN.'+str(n)+'}')
    b=body.index('\\end{proof}',a)+len('\\end{proof}')
    blocks[n]=body[a:b]

roulleau={
 'key':'Roulleau2019GeneralizedKummer',
 'url':'https://www.i2m.univ-amu.fr/perso/xavier.roulleau/Site_Pro_English/Publications_files/Roulleau%2C%20On%20generalized%20kummer%20surfaces%20and%20the%20orbifold%20Bogomolov-Miyaoka-Yau%20inequality.pdf',
 'doi':'10.1090/tran/7507',
 'version':'Original author-hosted journal offprint, Transactions of the American Mathematical Society371(11),2019,7651–7668.',
 'opened_locators':'Section3.1, p7659, complete ADE table and its source-credit paragraphs; Section4.1, Theorem27 and attribution paragraph p7663; introduction p7651.',
 'tool_refs':['turn982782393view0','turn104980166view0'],
 'actual_reading':'Primary-host PDF text was opened and the named entire table/paragraphs were read. No full-proof reading of the whole paper or fresh opening of its cited Nikulin/Bertin originals is claimed.',
 'exact_application':'The receiving action g(z)=Lz+b has a fixed point p with(I-L)p=b. The map z->z-p conjugates g to L and induces the actual quotient isomorphism A/<g> -> A/<L>. Take T=A and G=<L> in the published cyclic generalized-Kummer list. Its four configurations agree term for term with the receiving local invariant maps x=u^d,y=v^d,z=uv, xy=z^d and their minimal A_(d-1) resolutions. The receiving proof separately computes fixed-point orbit counts and the quotient/resolution Euler numbers and constructs the compact torus degeneration. This source passage explicitly credits the earlier cyclic work; no global priority claim is added.',
}
source_maps={
24:{'source_event_ids':['ce:45597b532fcf7fe07835','ce:61ba3afba7a3cc99e449','ce:4e9d86e617dfa7d5c29b','S6_SERIES_GRIND_sign_source_Peters1990_UN24','S6_SERIES_GRIND_sign_source_Lagrange1770_UN24','S6_SERIES_GRIND_sign_source_PiatetskiShapiroShafarevich1971_UN24'],
    'exact_input_maps':[
      'Peters author lecture Chapter1 Theorem3.1p10, with p9 definitions, classifies the smooth minimal component only after the receiving elliptic-fibre restriction proves kappa<=1; no unproved non-general-type inference is substituted.',
      'Lagrange modern six-page transcription, TheoremII p5/CorollaryII p6: for positive rational A/B, choose integers ni with sum(ni²)=AB and put xi=ni/B. Then sum(xi²)=A/B. The actual four disjoint exceptional classes have Gram(-2)I4. The displayed orthogonal projection Hprime and D=Hprime-sum(xiCi) have the literal pairings verified by the universal formal certificate.',
      'Piatetski-Shapiro–Shafarevich original English paper Section3 Corollary3p560 and Section6 Theorem1(3)pp573–574/following corollaryp574 supply the nonzero algebraic isotropic-class/reflection elliptic-pencil step on the projective K3 branch. The receiving class is integral after clearing denominators, square zero, and nonzero because D.Hprime=Hprime²>0. The actual proper graph and exceptional-curve contraction comparison in Step5 descends the pencil to the minimal K3 itself.',
      'The published Roulleau cyclic ADE list is applied through the actual translation/quotient/local invariant maps stated in the fresh opening record. UN16/20/22/23 and C3.1 retain their separately documented rank, quotient and fibration input scopes; UN1/4 retain the actual Euler parity/balancing scopes used to globalize.',
    ],'fresh_opening':roulleau},
39:{'source_event_ids':['ce:530345e279aad139a019','S6_SERIES_GRIND_sign_source_ACampo1975_UN39','ce:grind-sign:3609e7ee7c0107e1'],
    'exact_input_maps':[
      "A'Campo1975 original journal, Theorem1p235, Section2pp237–243 and Section3pp243–245; current primary-host opening covers Section2pp237–238 and local Lefschetz calculationpp243–244. Apply to the actual resolved proper analytic map, smooth total space and full SNC divisor sum(NjEj), without a Kahler assumption. The local nearby-cycle trace is Nj for Nj dividing k, zero otherwise, and the crossing strata have zero trace. Proper pushforward and Euler integration give the displayed global sum.",
      'On the actual nearby real four-torus, cohomology is the exterior algebra on H1 and the alternating trace is det(I-T^k). Upper triangularization over C proves this determinant is the product of(1-lambda^k), retaining all eigenvalue multiplicities even for nontrivial unipotent part. Taking L divisible by both the semisimple order and every full Nj retains every component and gives the exact average sum e(Ej°).',
      'Stratifying the resolved support into open surfaces, punctured double curves and triple points yields e(Sresolved)=j-2(sum(gD-1)+t3). Every actual blowup has full reduced inverse image with projective-space fibre; its Euler change is(c-1)e(center), for arbitrary generic multiplicity of the total divisor. Telescoping gives the printed I_pi formula and identifies it with(j-e(S))/2 for every resolution.',
      'UN11 supplies existence of the analytic resolution and the nineteen quasi-unipotent characteristic polynomials at its own recorded scope. The current exact program calculates all nineteen period determinants, Mobius coefficients, averages and zero indices. UN4 supplies the actual point/quartic comparison used in the final example; that input is not re-proved by the finite code.',
    ]},
}
sources_meta=save('UN24_UN39_source_application_08.json',{'date_utc':NOW,'reviewer':WHO,'sources_by_row':source_maps,'reading_order':'Source comparisons and this current certificate were made after receiving-proof access. The earlier complete statement-first routes are retained under their exact event IDs, not silently replaced by new blind claims.','novelty_scope':'Classical cyclic quotient/configuration/pencil inputs and the proper A\'Campo comparison receive positive credit. Keep the receiving actual degeneration, fibration-descent, full-multiplicity and vertical-modification arguments. No worldwide priority or exhaustive absence conclusion is made.'})

guards=[]
def guard(n,old,new,reason):
    assert body.count(old)==1 and blocks[n].count(old)==1,(n,reason)
    guards.append({'label':f'cdp:st:C.2.UN.{n}','old_text':old,'new_text':new,'expected_count':1,'reason':reason})

old='The computation is reproduced with exact integral\nmatrices in \\texttt{code/D\\_cyclic\\_k3.py}.'
new=r'''These cyclic configurations agree with the classical generalized-Kummer
list in \cite[\S3.1, p.~7659; \S4.1, Theorem~27, p.~7663]{Roulleau2019GeneralizedKummer},
which records the preceding cyclic-quotient work.
The exact integer matrices, every power's fixed-point count,
exact-stabilizer subtraction, quotient Euler average and resolution
Euler correction are computed in
\path{code/current_audits/audit_sign/code/UN24_UN39_exact_certificate_08.py};
the full four-row output and the formal identities
\eqref{cdp:eq:C.K3.8}--\eqref{cdp:eq:C.K3.9} are recorded in
\path{code/current_audits/audit_sign/UN24_UN39_exact_certificate_08.json}.'''
guard(24,old,new,'Replace the unavailable historical file by the executed complete current arithmetic certificate and add exact positive cyclic-configuration credit.')

old=r'''The exact independent calculation
in \path{code/A_zero_curve_index.py}
checks all nineteen finite averages
against the sums of the A'Campo
signature coefficients, and writes
the displayed table and
\path{records/A_zero_curve_index.csv}.
All arithmetic is integral or rational.'''
new=r'''The exact integer-matrix calculation in
\path{code/current_audits/audit_sign/code/UN24_UN39_exact_certificate_08.py}
computes every one-period determinant, the M\"obius coefficients,
all nineteen averages and their zero indices. Its complete output is
\path{code/current_audits/audit_sign/UN24_UN39_exact_certificate_08.json}.
For each characteristic polynomial the program uses a direct sum
of cyclotomic companion matrices. Over $\C$, triangularizing the actual
$T$ gives $\det(I-T^k)=\prod_\lambda(1-\lambda^k)$, with every eigenvalue
multiplicity retained; this identity identifies the computed determinant
with the required one even in the presence of a unipotent part.
The average agrees with the sum of the A'Campo coefficients in every row.
All arithmetic is integral or rational.'''
guard(39,old,new,'Replace the unavailable historical program/CSV by the executed current complete nineteen-row certificate and state its exact determinant morphism to actual monodromy.')
guard(39,"The proper analytic A'Campo comparison, with\nits actual nearby-cycle maps as established\nin (C.MS.6), says for every positive $k$ that",r'''The proper analytic A'Campo comparison
\cite[\S2, pp.~237--243; \S3, pp.~243--245]{ACampo1975}, with
its actual nearby-cycle maps as established
in (C.MS.6), says for every positive $k$ that''','Credit the exact proper-analytic full-multiplicity nearby-cycle formula.')
for n,cite in [(24,r'\cite[\S3.1, p.~7659; \S4.1, Theorem~27, p.~7663]{Roulleau2019GeneralizedKummer}'),(39,r'\cite[\S2, pp.~237--243; \S3, pp.~243--245]{ACampo1975}')]:
    a=blocks[n].index('\\StatementRecord');b=blocks[n].index('\n\n',a)
    old=blocks[n][a:b]
    guard(n,old,old[:-1]+'; '+cite+'}','Add the concrete primary input to the uses/source record.')

bib=r'''@article{Roulleau2019GeneralizedKummer,
  author = {Roulleau, Xavier},
  title = {On generalized Kummer surfaces and the orbifold Bogomolov--Miyaoka--Yau inequality},
  journal = {Transactions of the American Mathematical Society},
  volume = {371},
  number = {11},
  pages = {7651--7668},
  year = {2019},
  doi = {10.1090/tran/7507},
  url = {https://www.i2m.univ-amu.fr/perso/xavier.roulleau/Site_Pro_English/Publications_files/Roulleau%2C%20On%20generalized%20kummer%20surfaces%20and%20the%20orbifold%20Bogomolov-Miyaoka-Yau%20inequality.pdf},
  verification = {verified at listed scope},
  note = {Author-hosted original journal offprint opened20November2026. Section3.1p7659: full ADE table and cyclic-source attribution; Section4.1Theorem27 and its attribution p7663. Applied to the actual cyclic symplectic action through the receiving translation and quotient maps. No new full-paper proof or original Nikulin/Bertin opening is claimed.}
}'''
assert '{Roulleau2019GeneralizedKummer,' not in (WORK/'S6_SERIES_GRIND_references.bib').read_text()
guard_meta=save('UN24_UN39_source_code_guards_08.json',{'date_utc':NOW,'target':'parts/II.body.linked.tex','target_sha256':sha(bodypath),'guards':guards,'bibliography_additions':[{'key':'Roulleau2019GeneralizedKummer','expected_count':0,'bibtex':bib}],'source_application_receipt':sources_meta,'certificate':{'code':'audit_sign/code/UN24_UN39_exact_certificate_08.py','code_sha256':sha(OUT/'code/UN24_UN39_exact_certificate_08.py'),'output':'audit_sign/UN24_UN39_exact_certificate_08.json','output_sha256':sha(OUT/'UN24_UN39_exact_certificate_08.json'),'stdout':'audit_sign/UN24_UN39_exact_certificate_08.stdout.txt','checks_shared_total':607},'scope':'No mathematical statement changes. Added source credit and truthful current certificates. Canonical rows remain pending integration and changed-page QA.'})

data={
24:{'before_event':'ce:d9cc8160edf6f2a0e13b','current_event':'ce:grind-sign:d2034b685e48d15e','steps':12,'old_pages':[544,548],
    'credit':'Classical cyclic symplectic torus quotient/ADE configurations are recorded in Roulleau2019 Section3.1p7659 and Theorem27p7663, with explicit Nikulin/Bertin predecessor credit at the source. Peters author lecture Chapter1 Theorem3.1p10 supplies the minimal-surface list. Lagrange modern original-text transcription TheoremII p5/CorollaryIIp6 supplies four squares. Piatetski-Shapiro–Shafarevich1971 Section3 Corollary3p560 and Section6pp573–574 supply the actual isotropic-class reflection and elliptic pencil. The receiving proof retains the exact normalized-cover/fibration descent, algebraic-dimension-zero criterion and compact zero-Euler realization.',
    'scope':'All twelve actual normalized-cover/field/quotient/fibration-descent, cyclic-order, ADE, pencil and compact-realization steps. Current exact certificate includes all four quotient rows and universal projection identities; no finite sampling is substituted for the four-square or pencil theorems.'},
39:{'before_event':'ce:03056313d96408c15380','current_event':'ce:grind-sign:3609e7ee7c0107e1','steps':7,'old_pages':[458,460],
    'credit':"A'Campo1975 proper-analytic nearby-cycle/Lefschetz comparison, original Section2pp237–243 and Section3pp243–245, supplies the full-multiplicity open-stratum sum. UN11 supplies the actual quasi-unipotent monodromy list and analytic resolution input; UN4 supplies the actual point/quartic blowup example. UN39 derives the resolution-independent curve-centre index by averaging that formula and comparing the full reduced inverse images under every actual vertical blowup.",
    'scope':'All seven resolution, full-multiplicity average, SNC-stratum additivity, actual blowup/telescoping, nineteen-polynomial arithmetic and concrete-example steps. Current exact certificate covers every period determinant and Mobius coefficient, every average and zero index.'},
}
proposals=[]
for n,r in data.items():
    label=f'cdp:st:C.2.UN.{n}'; ev=evidence[label]; event=next(e for e in ev['events'] if e['event_id']==r['before_event'])
    updates={
      'credited_to':r['credit'],
      'literature_searches':'Exact retained and current positive-source events/locators are joined in audit_sign/UN24_UN39_source_application_08.json. Historical bounded supplied-corpus comparison remains at its recorded scope; no unavailable historical search file is claimed reopened. '+('Fresh author-hosted Roulleau original offprint was opened at Section3.1p7659 and Section4.1Theorem27p7663, with source attribution read. The current Lagrange opening is a transcription, not the original-volume scan; Peters states the classification without its full proof.' if n==24 else "The current A'Campo original-journal text was opened through primary-host retrieval at Section2pp237–238 and local Lefschetzpp243–244; retained exact opening ce:530345e279aad139a019 covers Section2pp237–243 and Section3pp243–245."),
      'source_credit_verdict':'The stated classical inputs receive exact positive credit through their actual application maps. Retain the receiving full statement/proof. No worldwide novelty, priority or exhaustive literature-absence conclusion is made.',
      'credit_transport':' '.join(source_maps[n]['exact_input_maps']),
      'literature_disposition':'Retain with full proof and precise source credit. '+r['scope']+' Imported results retain their separate proof and exposure scopes.',
    }
    proposals.append({'label':label,'full_target_scope':r['scope'],'exact_retained_before_reading_event':event,'retained_three_check_gates':ev['retained_explicit_three_check_gates'],'current_full_comparison_event':r['current_event'],'guarded_source_updates':[{'field':k,'old_value':inventory[label].get(k,''),'new_value':v} for k,v in updates.items()],
      'computation_applicability':'The new standard-library certificate is after receiving/code exposure and imports no producer. Its607 checks are a shared program total, not607 per row. '+r['scope'],
      'old_actual_layout_sample':{'receipt':'audit_sign/II_95_visual_QA_06.json','pages':r['old_pages'],'scope':'Actually viewed build23 sample only. No transport to the next changed body is asserted.'},
      'remaining_gates':['Root acceptance/integration of the exact source/code guards and Roulleau bibliography entry.','Actual changed-page QA of the rebuilt full target row, with current PDF/image hashes.'],
      'completion_recommendation':'After those exact integration/QA gates pass, recommend this row alone as done on its recorded full target route and current mathematical/source/computation scopes. No canonical mutation yet; no imported row or main theorem is closed by this recommendation.'})
proposal_meta=save('UN24_UN39_completion_proposals_08.json',{'date_utc':NOW,'reviewer':WHO,'records':proposals,'sources':sources_meta,'guards':guard_meta,'scope':'Two exact retained whole-before-reading candidates. No route is inferred merely from an event type; complete retained outcomes and completed-row gates are included. Named historical derivation files are absent from the supplied archive, so their exact retained receipts are the available provenance. Current receiving/source/code work is after exposure.'})

text=['# UN24 and UN39: exact current certificate and completion proposals','',
 'The new standard-library calculation passes **607 exact checks in total**. It computes all nineteen one-period determinant and Möbius rows, averages and zero indices; all four cyclic K3 fixed-point/stabilizer/ADE/Burnside/resolution rows; and seven universal four-curve projection identities. It was written after the receiving proofs and previous current small programs were read. It imports no old producer, and it supplies no new before-reading proof credit.','',
 '## Exact finite model and actual monodromy','',
 'For each integral cyclotomic characteristic polynomial, the code constructs a direct sum of integer companion blocks. Those blocks are finite-order models for the same eigenvalue multiset. For the actual matrix T, triangularization over the complex numbers gives det(I−T^k)=product(1−lambda^k), retaining multiplicities even with a nonzero nilpotent Jordan part. That identity is the exact map from the computed determinant to the receiving one; no conjugacy of the actual T to a finite-order matrix is asserted. Möbius inversion is checked for every divisor and every integer in a full period. All nineteen printed UN39 rows and all nineteen UN11 coefficient rows match.','',
 'For UN24, the order-n matrices have the receiving symplectic eigenvalue multiset. Fixed points are kernels of the actual isogenies. Subtraction over subgroup divisibility gives exact stabilizer counts; division by orbit size gives each A-chain multiplicity. Burnside gives quotient Euler8,6,6,6, and the full exceptional corrections yield24 in every case. A separate sparse formal-polynomial calculation proves the Hprime/D pairing identities for all rational choices of the input pairings and four-square coordinates. It does not infer the four-square theorem from examples.','',
 '## Source application','']
for n in [24,39]:
    text+=['### UN'+str(n),'',data[n]['credit'],'']
    for line in source_maps[n]['exact_input_maps']:text+=['- '+line,'']
    text+=['Retained full before-reading event: `'+data[n]['before_event']+'`. Current complete '+str(data[n]['steps'])+'-step comparison: `'+data[n]['current_event']+'`. The exact historical event and completed-row gate are in the JSON proposal. The named historical proof files are absent from the supplied bundle; no new opening of those files is claimed.','']
text+=['## Exact publication tasks','',
 'The five guarded changes replace two unavailable historical programs/outputs, add direct A\'Campo and Roulleau source credit, and add the corresponding uses records. One new Roulleau bibliography entry is supplied. No mathematical statement changes. Root applies the guards; then the rebuilt whole UN24 and UN39 pages need actual QA. Canonical completion remains pending those tasks and parent acceptance.','',
 'The prior build23 visual samples were UN24pages544/548 and UN39pages458/460. They are preserved as samples, without a claim that unchanged-page transport or a full-row view has already occurred for the next build.']
(OUT/'UN24_UN39_completion_report_08.md').write_text('\n'.join(text)+'\n')

eventspath=OUT/'CHECK_EVENTS_additions.tsv'
with eventspath.open() as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;events=list(reader)
new=[]
for n in [24,39]:
    new.append({'statement_id':f'cdp:st:C.2.UN.{n}','date':NOW,'who':WHO,'type':'computation or formal certificate','outcome':('Shared new standard-library program UN24_UN39_exact_certificate_08.py PASS607 total checks across both rows; do not count607 independently for each row. '+('UN24 scope: all four integer cyclic models, all nonidentity-power fixed counts, exact stabilizers, A-chain multiplicities, Burnside quotient Euler and resolution Euler, plus seven universal Hprime/D pairing identities over a rational polynomial ring.' if n==24 else 'UN39 scope: complete degree-four determinant-one cyclotomic enumeration, every one-period determinant, divisor Mobius coefficient, nineteen averages/zero indices, and exact comparison to all nineteen UN11 coefficient rows and current UN39 table.')+' Written after receiving and previous current small-code exposure. No producer import or new before-reading derivation credit. Exact upper-triangular determinant identity supplies the map from finite models to actual monodromy; geometric inputs retain separate proof records. Output and hashes in UN24_UN39_exact_certificate_08.json.'),'event_id':f'S6_SERIES_GRIND_sign_UN{n}_exact_certificate_08','phase':'current'})
new.append({'statement_id':'cdp:st:C.2.UN.24','date':NOW,'who':WHO,'type':'targeted proof check','outcome':'Fresh primary-source opening: Roulleau2019 original author-hosted journal offprint, Section3.1p7659 complete ADE table and predecessor attribution, Section4.1Theorem27p7663 and attribution, introductionp7651. All four cyclic configurations match through the actual translation z->z-p conjugating g to L, the induced quotient isomorphism and invariant coordinates x=u^d,y=v^d,z=uv. Exact source URL, metadata, tool refs and application in UN24_UN39_source_application_08.json. No full-paper proof or fresh opening of original Nikulin/Bertin cited sources is claimed.','event_id':'S6_SERIES_GRIND_sign_UN24_Roulleau_primary_08','phase':'current'})
ids={e['event_id'] for e in events};events.extend(e for e in new if e['event_id'] not in ids)
with eventspath.open('w') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
print(json.dumps({'source':sources_meta,'guards':guard_meta,'proposal':proposal_meta,'events':len(events)},indent=2))
