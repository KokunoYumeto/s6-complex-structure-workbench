from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix='S6_SERIES_PUBLISH_sec07_cubic_double'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    rr=csv.DictReader(f,delimiter='\t'); fields=rr.fieldnames; rows=list(rr)
review=('Complete original/current and receiving P453 subsection read and compared; '
        'complete old/receiving P222 and P300 proofs read. P322 and A.5.3 exact '
        'hypothesis/conclusion maps checked; P452/P451 full-fibre input retained. '
        'All three guards replay once and preserve every existing label/target '
        'multiplicity. Exposed comparison only, no independent credit or required '
        'check increment. Integrated build, page reading and global structure remain.')
for row in rows:row['review_status']=review
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    ef=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
readings=[
 ('conductor_owner','lem:II:conductor-duality / lem:II:proper-conductor-divisor',
  'Read complete old and receiving P222/P300 statements/proofs. P222 retains '
  'all normalization, Ext, endomorphism and compact-section comparisons. Its '
  'additional local criterion uses R=O_S,eta(q), finite semilocal normalization '
  'B and maximal q: c B_q=B_q gives c in conductor outside q; q cap R=m_R '
  'makes c a unit in R, and cB subset R gives B=R. The finite coherent quotient '
  'then vanishes near eta(q), including every branch. P300 applies precisely '
  'this criterion with R=O_S,nu(p), B=(nu_*O_N)_nu(p). Its general-divisor '
  'application, full f=u g^m, exact root, A.5.17 local-fibre inclusion and '
  'complete support/complement conclusions are unchanged.'),
 ('primary_duality','lem:II:conductor-duality',
  'Freshly opened Reid1994 Nonnormal del Pezzo surfaces, full Proposition2.3 '
  'and proof2.4 on printed p703; Theorem2.6 and proof2.7 on pp704–705. Read '
  'both extracted text and all three rendered printed pages, including the '
  'residue/trace diagrams. Proposition2.3 identifies Hom_R(B,R) as the '
  'conductor and gives its S2/reflexive extension; the analytic local proof '
  'in P222 uses these exact multiplier and Ext maps. Download URL '
  'https://ems.press/content/serial-article-files/40537; PDF SHA256 '
  '8786c3c9560d262a174a2a3be343507f59240b62935df08dc6a60993f8b254d7. '
  'Printed p703 is PDF page9, p704 page10, p705 page11. Existing journal '
  'bibliography and DOI10.2977/prims/1195165581 are retained.'),
 ('cubic_geometry','night:P4.53',
  'Read every original/current and receiving P453 statement/proof line. '
  'P452 supplies the identical point blowup beta:Y1→Y, compact S1, '
  'rho1:T1→S1 and coefficient2=n+a. The Weierstrass degree is renamed '
  'mu_L, preserving the ramification-index/residue-degree sum and separating '
  'it from full-fibre m. The conductor formula at P282 gives exactly the '
  'two nodal branches, n=a=1, tangent y^2 ell and weights(1,2,1). All '
  'f4 divisibility, degree-two residue cover, discriminant, weighted-vertex '
  'and reduced-factor cases remain. The explicit identity C5={P5=0} '
  'replaces the former curve name D. Sextic partitions(1^6),(2,1^4), '
  '(3,1^3), quartic partition(1^4), M<=2 or3, and chi(complement)>=2 '
  'are all retained. The positive-genus refinement of A.5.3 applies to '
  'the same exceptional H and canonical D1; adjunction leaves g(H)=1 '
  'and H as the sole exceptional component. P222 then proves whole-germ '
  'normality at p1 from the unit conductor at q. The isolated simple '
  'elliptic conclusion and arbitrary transverse-type scope are unchanged.'),
 ('weighted_application','night:P4.53 / lem:II:weighted-initial-monodromy',
  'Read the complete current P322 and compared the receiving P453 '
  'application with its full original norm, character, Siersma/Wang '
  'and scaling proof. The exact map is D_epsilon=(epsilon x,epsilon^2 y, '
  'epsilon z), G_epsilon=epsilon^-5 g D_epsilon, c=1. The full original '
  'function stays Phi=u g^m; g_u=exp(log(u)/m)g is exactly h in P452. '
  'P451 first clause is used on the same fibre through P452 b1(S)>0. '
  'The free mu5 quotient is P(1,2,1) minus C5; the weighted vertex lies '
  'in C5. The old norm is preserved and its compact core maps through '
  'the same affine fibre, giving the same homology and intersections. '
  'P322 gives lower bound4chi>=8 and upper boundM<=3, including M=0 '
  'for isolated critical points. The gap5 remains. The scaling premise '
  'now precedes its monodromy use. No generic transverse-type hypothesis '
  'or original full-fibre multiplicity is added or removed.')
]
events=[]
for suffix,owner,outcome in readings:
    e=dict.fromkeys(ef,'');e.update(statement_id=owner,date=now[:10],
      who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
      type='used and rechecked in this run',
      outcome=outcome+' Exposed reading and direct comparison only; no independent-check credit, required-check increment or integrated rendered-page reading.',
      event_id='publish:c3:foundations:sec07:cubic_double:'+suffix,
      phase='publication complete cubic double-line subsection',
      source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',
      evidence_group='publish:c3:foundations:sec07:cubic_double',date_utc=now,
      where='Complete P453 subsection; bounded full P222 owner and P300 paragraph')
    events.append(e)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=ef,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)

specific={
 'D01':'The exact P452/P314 setting replaces the inherited remaining-support phrase.',
 'D02':'Arbitrary generic transverse types are stated positively once.',
 'D04':'Literal4.53a and every old equation tag use their stable reference labels.',
 'D08':'The two process uses of actual and the remaining-support wording are removed; original equations keep their mathematical meaning.',
 'D10':'Existing D10 closure stands; dependency records remain hidden.',
 'D12':'P222 alone owns the unit-conductor criterion; P300/P453 use its exact local rings. P322 alone owns weighted transport/variation/character bounds. A.5.3 alone owns exceptional-block positivity.',
 'D13':'The entire subsection is its numbered proposition and proof; numerical partitions are placed inside the relevant proof steps.',
 'D14':'All receiving premises precede their consumers locally, including scaling before monodromy. Whole-paper placement remains with root.',
 'D16':'Existing D16 closure stands; the proposition keeps its mathematical title.',
 'D17':'Freshly opened complete Reid2.3/2.6 proofs replace the repeated finite-duality proof by P222; exact P322 applications replace its already opened Siersma/Hatcher arguments.',
 'D18':'Reid journal pages703–705, DOI and source URL are verified; the existing correct bibliography is retained.',
 'D19':'4.53a–e retain the prepared labels and now use the section equation counter; no paragraph breaks occur inside equations.',
 'D20':'C5 is explicitly the same weighted curve formerly called D; mu_L is its cubic-component multiplicity; m remains full-fibre multiplicity. The root g_u is explicitly the function h of P452.',
 'D22':'The partitions and rank gap are given beside the estimates that use them; the coefficient and field-extension maps explain all integer cases.',
 'D23':'Full source comparison and equation whitespace checks done; integrated build and final page reading remain with root.',
 'D24':'Root must reconcile the final outline/contents with the actual subsection; no global front-matter closure is claimed.',
 'D25':'Every original proof inference was compared with the receiving text. Whole-germ normality follows through B=R, not an unproved branch identification; all multiplicities, conductor factors and full-function maps remain.',
 'restructuring':'The actual P453 subsection is locally consolidated and guard-ready; whole-paper ordering and final integration remain. P222/P300 are bounded owner applications, not extra completed units.'
}
status=[]
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    status.append(dict(unit='night:P4.53',row=kind,
      status='open' if kind in ['D14','D23','D24','restructuring'] else 'done',
      basis=specific.get(kind,'The complete original/current and receiving subsection was read for this class; no instance remains in this receiving text.'),
      fragment='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_II_sec07_cubic_double.tex'))
with (OUT/(prefix+'_unit_progress.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['unit','row','status','basis','fragment'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(status)
lines=['# Cubic double-line subsection: status','',
 'READY: complete original/current and receiving proofs compared; three guards replay once with all old labels and targets retained. No new permanent tag. Root admission pending.','',
 '| Class | Status | Basis |','|---|---|---|']
lines += [f"| {r['row']} | {r['status']} | {r['basis']} |" for r in status]
(OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')

comparison=r'''# Cubic double line: exact consolidation map

The actual subsection is `night:P4.53`, with new heading label `subsec:II:cubic-double-line`. Its statement retains precisely P452's global positive ruled setting, contracted section, multiplicity-three point blowup, normal simple elliptic conclusion, and arbitrary transverse types. No new tag is used. P323/P324 remain reserved.

| Original owner/calculation | Receiving owner/application | Exact preserved map and conclusion |
|---|---|---|
| P300/P453 conductor duality and unit argument | P222, then exact applications | For R=O_S,p and finite semilocal normalization B, a conductor unit at q over p yields c outside q, hence outside m_R, and cB⊂R gives B=R. This proves the entire local germ, including all branches. |
| P300 proper support argument | P300, only one bounded paragraph changes | R=O_S,nu(p), B=(nu_*O_N)_nu(p); all A.5.3, full f=u g^m, root and A.5.17 arguments remain byte-for-byte outside the guard. |
| P453 effective pole divisor and positive block | A.5.3 | Same compact S1 in smooth Y1, same normalized minimal resolution rho1:T1→S1, same dualizing generator. The coefficient identity is2=n+a. Positive genus makes the entire exceptional block positive. |
| P453 weighted transport | P322 first clause | Dε=(εx,ε²y,εz), Gε=ε⁻⁵g∘Dε, c=1. Original full function Phi=u g^m is unchanged; g_u=exp(log(u)/m)g is h in P452. The exact inclusion sends g_u=δ to Phi=δ^m. |
| P453 compact core, free character and variation | P322 second/third clauses | Same reduced P5, weights(1,2,1), degree5 and free mu5 quotient. The original norm remains, its core comparison passes through the identical affine fibre. Rank lower bound8, upper boundM≤3 and gap5 remain. |
| P453 normality at p1 | P222 applied to A=O_S1,p1 and its semilocal normalization B | The positive exceptional fibre is exactly H, disjoint from strict conductor. Reflexivity gives unit conductor at q below H, and the unit criterion gives A=B. Sole elliptic exceptional curve means isolated simple elliptic singularity. |

All cubic component, ramification and residue-field degrees remain. The local Weierstrass degree is now mu_L, equal to the multiplicity of L in the cubic; m exclusively denotes the original full-fibre multiplicity. The projective curve C5 is the same set {P5=0} formerly called D. The sextic partitions(1^6),(2,1^4),(3,1^3), quartic partition(1^4), nodal/tangent alternatives, all weighted-vertex checks and Euler counts are preserved. Numerical partitions now stand beside their estimates, and transport precedes its monodromy use.

Fresh source opening: Miles Reid, Nonnormal del Pezzo surfaces, Publ. RIMS30(5)(1994),695–727, DOI10.2977/prims/1195165581. Complete Proposition2.3/proof2.4 printedp703 and Theorem2.6/proof2.7 pp704–705 read in text and rendered pages, including diagrams. Source https://ems.press/content/serial-article-files/40537; SHA256 8786c3c9560d262a174a2a3be343507f59240b62935df08dc6a60993f8b254d7. Printed703–705 are PDFpages9–11. Existing bibliography is unchanged. The short new local algebra is the precise semilocal form needed by these consumers, not a repeated proof of finite duality.

Three guards cover the full P222 owner, the single P300 paragraph and the entire P453 subsection. Complete old/current and receiving proofs have been read, including their shared owners. Every old label and target multiplicity is retained. Four exposed-reading events and the defect rows record these comparisons without independent credit or a required-check increment. Integrated build/page reading, front matter and whole-paper placement remain with root.
'''
(OUT/(prefix+'_comparison.md')).write_text(comparison,newline='\n')
print(f'{len(rows)} defects; {len(events)} exposed events; {len(status)} subsection rows; no new tag.')
