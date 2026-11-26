from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix='S6_SERIES_PUBLISH_sec07_quartic'
defects=OUT/(prefix+'_defects.tsv')
with defects.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t')
    fields,rows=reader.fieldnames,list(reader)
review=('Complete original/current and receiving quartic subsection read, including '
        'all P452 proof steps and full P322. Complete A.5.3/P300 original and receiving '
        'proofs compared; complete P318 old/receiving proof read. Exact P451/D1.9 '
        'full-fibre input and complete present P314/R13 statements/proofs compared. '
        'Five guards replay once, preserving every old label/target multiplicity. '
        'No independent credit or required-check increment. Integrated build, page '
        'reading and whole-paper placement remain with root.')
for r in rows:r['review_status']=review
with defects.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)

with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
readings=[
 ('general_divisor','cdp:st:A.5.3',
  'Read complete current and receiving A.5.3 and P300 statements/proofs. '
  'The exact identification is T_i=N,Z_i=T,eta=nu,pi_i=pi,h_i=rho; both divisors '
  'are the negative orders of the same pulled-back local dualizing generator. '
  'A.5.3 keeps its full finite-duality, exceptional-matrix, ruled and Picard proofs '
  'and gains the existing P300 positive-block refinement. On a connected block, '
  '-M^{-1}>0, v_j=(K+Dstr).E_j>=0 and a=-M^{-1}v. Positive geometric genus gives '
  'p_a>=1,E^2<0 and K.E>0. A zero coefficient gives v=0 and only rational -2 '
  'curves disjoint from Dstr. All A.25/A.26 payloads/identifiers remain. '
  'P300 now introduces that canonical D by the exact A.5.3 map and states/proves '
  'only the additional proper-torus support conclusions. Its complete reflexive '
  'conductor, unit-conductor idempotent, full f=u g^m/root and sphere inclusion '
  'proof remains. R6/CR1/UN7 still use the identical D and unchanged hypotheses.'),
 ('weighted_owner','lem:II:weighted-initial-monodromy',
  'Read all original P452 topology and the complete receiving P322. The exact '
  'weighted map is D_epsilon(z)=(epsilon^wi zi), G_epsilon=epsilon^-d g D_epsilon; '
  'gradient flow on nested compact neighbourhoods followed by this holomorphic '
  'scaling preserves the chosen cycles and intersections and gives g=c epsilon^d. '
  'This first clause allows a repeated leading factor. For reduced germs the '
  'source variation identity j2(T-I)=VARII j and dimension-two Wang sequence '
  'give rank(T-I)<=sum mu_i when j=0; no VARII isomorphism is assumed. '
  'The weighted norm Rw=sum |zi|^(2L/wi), its finite critical-value set and '
  'normalized gradient give the invariant compact core and exact local scaling. '
  'The free mu_d action gives the virtual character chi(Q) C[mu_d] and the '
  'lower bound (d-1)chi(Q). All 4.52a/b payloads are retained at this one owner.'),
 ('variation_source','lem:II:weighted-initial-monodromy',
  'Freshly opened Siersma1991 original journal facsimile, full Sections1.2 p445, '
  '3.4–3.6 pp451–452, 5.3 p457 and continuation p458, 6.2–6.5 pp460–461, '
  'and 7.1 p462. Read rendered diagrams on printed pp452/462 as well as text. '
  'The displayed j/j2/VARII composition is exactly the unmodified chain-level '
  'identity in fibre dimension two. Section6.3 preserves H2(boundary2) as the '
  'sum of kernels of vertical A_i-I on H1(F_i). Proposition3.4 supplies the '
  'isolated case. Opened Hatcher2002 Theorem2C.3 and its setup on printed p179 '
  'for the free finite-action Lefschetz application; no new full-book/proof '
  'reading is claimed. Siersma PDF URL '
  'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/siersma.pdf; SHA256 '
  'a1e17e14cc0052271b1d6f8a875aedbae34a08cf1b456046c888420a22904595. '
  'The bibliography continues to cite the published Topology30(3),445–469 edition.'),
 ('quartic_comparison','night:P4.52',
  'Read complete original/current and receiving P452 and full P451,D1.9,P4.12 '
  'inputs. The original positive ruled remainder is made explicit by the '
  'complete present P314/P203 setting; its full proof and refined R13 proof '
  'were read, including the one-or-two elliptic-image alternatives. '
  'Connected fibres give genus(B)=0; D1.9 gives a nonzero integral class on '
  '|mS|=S, hence b1(S)>0. P451 first clause applies to the identical irreducible '
  'full fibre. The full function Phi=u g^m has exact root h=exp(log(u)/m)g, '
  'and the same local level includes into Phi^-1(delta^m). The complete '
  'quartic delta/Milnor estimates, chi=4(7-M), lower bound3(7-M), upper boundM '
  'and gap21-4M remain. The compact strict transform S1 in smooth Y1 applies '
  'A.5.3 directly. The blowup chart multiplies volume by r^2 and g by r^d; '
  'Dold=D1+(d-2)rho1*E gives 2=(d-2)n+a, a>=0 and a>0 on a positive-genus '
  'exceptional H. The n=1,a=0 quartic component map is birational and '
  'multiplicity one. Full A.5.17/root exclusion and the exact R15 even/odd '
  'product normalization exclude degrees1/2; the conclusion d=3 is unchanged.'),
 ('analytic_factorization','night:P4.52 / lem:II:elliptic-minimal-descent',
  'Opened the complete analytic statements and setup of Popescu-Pampu2016 '
  'Propositions3.10 and3.12, printed p20, in the primary Numdam edition. '
  'The first gives minimal-resolution domination for normal complex surface '
  'singularities; the second gives point-blowup factorization for proper '
  'holomorphic modifications between smooth complex surfaces. The source '
  'points to proofs elsewhere; no reading of an unprinted proof, Laufer5.9 '
  'or a projective-to-analytic extension is claimed. In P452 the local maps '
  'over singular points of N glue with the given smooth-locus map to give '
  'T1→T. In P318 the map is exactly rho:X→Z from its statement. Read the '
  'entire old/receiving P318 proof: only the factorization citation changes, '
  'with its nef/canonical-intersection/elliptic-descent conclusions intact. '
  'URL https://www.numdam.org/item/10.5802/wbln.14.pdf; DOI10.5802/wbln.14; '
  'SHA256 3c2190b5fa1e2bf94e2605b41ac6c75dabb1d629139380e67c8bdfdaa811efbd.')
]
events=[]
for suffix,owner,outcome in readings:
    e=dict.fromkeys(event_fields,'')
    e.update(statement_id=owner,date=now[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
        type='used and rechecked in this run',
        outcome=outcome+' Exposed reading and direct comparison only; no independent-check credit, required-check increment, integrated compilation or final rendered-page reading.',
        event_id='publish:c3:foundations:sec07:quartic:'+suffix,
        phase='publication complete quartic tangent subsection',
        source_file=str(defects.relative_to(ROOT)),
        source_event_type='used and rechecked in this run',
        evidence_group='publish:c3:foundations:sec07:quartic',date_utc=now,
        where='Complete quartic subsection; bounded A.5.3/P300/P318 and bibliography guards')
    events.append(e)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(events)

specific={
 'D01':'The inherited remainder phrase is replaced by the exact numbered P314/P203 setting.',
 'D02':'The arbitrary transverse-type scope is stated positively once; repeated defensive variation prose is replaced by the precise dimension-two identity.',
 'D04':'All current body references use stable statement/equation labels; literal4.52b is repaired.',
 'D08':'Production-relative remainder wording is removed; geometric old/strict-transform divisors are defined by their maps.',
 'D10':'Existing Paper II D10 closure stands; all dependency records are hidden and P322 is a numbered mathematical lemma.',
 'D12':'A.5.3 alone owns the general divisor theorem and matrix proof; P300 adds proper-torus support. P322 alone owns shared transport, variation and free-character calculations. P452 applies them and A.5.17 on exact maps.',
 'D13':'The entire receiving subsection consists of P322/P452 with proofs; no orphan result remains.',
 'D14':'P322 precedes every assigned consumer and A.5.3/P300/A.5.17 precede P452. Whole-paper part placement remains with root.',
 'D16':'Existing Paper II D16 closure stands; P322 and the revised P300 have mathematical titles.',
 'D17':'Exact Siersma/Hatcher/Popescu-Pampu loci opened. Only the short weighted-chain, dimension-two Wang and analytic map comparisons needed for these applications remain.',
 'D18':'Analytic factorization uses the opened Numdam journal edition and exact propositions/page. Existing Siersma journal bibliography is correct; new entry is in author order.',
 'D19':'4.52a/b move intact to P322;4.52c/d remain at P452. All use section numbering and the prepared target labels; no blank equation paragraphs.',
 'D20':'C4 denotes the tangent quartic, D/D1 the canonical pole divisors; the identity naming map and every normalization/blowup map are explicit.',
 'D22':'The point-blowup Jacobian r^2 and equation factor r^d explain the coefficient identity; the rank gap and each hypothesis are given at use.',
 'D23':'Complete source and equation-whitespace comparison done; integrated build and final page reading remain with root.',
 'D24':'Root must reconcile the final outline/contents with the new owner and subsection; no global front-matter closure is claimed.',
 'D25':'The complete full-function, divisor, quartic and refined-consumer maps are compared. P451 first-clause b1(S)>0 is explicitly established; no original mathematical assertion is refuted or weakened.',
 'restructuring':'The actual quartic subsection is locally consolidated. Root admission and whole-paper structure remain; bounded A.5.3/P300/P318 guards are not additional completed subsections.'
}
status=[]
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    status.append(dict(unit='subsec:II:quartic-tangent-obstruction',row=kind,
        status='open' if kind in ['D14','D23','D24','restructuring'] else 'done',
        basis=specific.get(kind,'The complete original/current and receiving subsection was read for this class; no source instance remains in this receiving text.'),
        fragment='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_II_sec07_quartic.tex'))
with (OUT/(prefix+'_unit_progress.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['unit','row','status','basis','fragment'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(status)
lines=['# Quartic tangent obstruction: unit status','',
       'Complete original/current and receiving subsection read. Five guards replay once and preserve all old label/target multiplicities. P322 is the only new tag. Root admission is pending.','',
       '| Class | Status | Basis |','|---|---|---|']
lines.extend(f"| {r['row']} | {r['status']} | {r['basis']} |" for r in status)
(OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')

comparison=r'''# Quartic subsection and common owners

## Actual unit and scope

The complete subsection now contains P322 followed by P452, ending before the cubic double-line subsection. P452's old remaining-positive-ruled phrase is resolved to the exact earlier P314/P203 setting: the global irreducible-or-normal-crossings fibration, irreducible full mS, positive Euler number and positive-genus ruled normalization. The conclusion and arbitrary transverse-type scope are unchanged. Complete present P314 and refined P4R.13 proofs were read; no one-component-only elliptic conclusion is used.

| Original calculation | Unique owner or exact application | Preserved map/conclusion |
|---|---|---|
| A.5.3 and P300 general pole-divisor proof | A.5.3 | T_i=N, Z_i=T, eta=nu, pi_i=pi, h_i=rho, and the same meromorphic dualizing generator. The positive-block/positive-genus refinement now stands with the whole original matrix proof. All ruled/Picard conclusions remain. |
| P300 proper-torus support | P300 applying A.5.3 | Canonical D is introduced by that exact map. The reflexive conductor, unit-conductor idempotent, original f=u g^m, root and local-fibre inclusion, full support and complement proof remain. |
| P452 compact-cycle flow | P322 first clause | D_epsilon=(epsilon^wi zi), G_epsilon=epsilon^-d g D_epsilon, level c, with compact chains and intersection representatives. Leading P may have repeated factors. |
| P452 variation inequality | P322 second clause | Same j,j2,VARII,T,vertical A_i and transverse F_i; the dimension-two Wang kernel gives rank(T-I)<=M. Isolated case is Siersma3.4. |
| P452 compact-core/free character proof | P322 third clause | Rw=sum |zi|^(2L/wi), scalar monodromy, quotient Q and virtual character chi(Q) C[mu_d]. |
| P452 zero pairing | P451 first clause | D1.9 gives b1(S)>0 on the same underlying full fibre. Full Phi=u g^m, h=exp(log(u)/m)g and h^-1(delta)→Phi^-1(delta^m) are unchanged. |
| P452 strict-transform effectiveness | A.5.3 | beta:Y1→Y, S1 compact Cartier strict transform, mu=beta|S1, rho1:T1→S1 normalization/minimal resolution. This is a general hypersurface application. |
| P452 pole identity | Retained in P452 | The chart (r,u1,u2)→(r,ru1,ru2) gives volume factor r^2 and equation factor r^d. Hence omega_S1=mu*omega_S⊗O((2-d)E), Dold=D1+(d-2)rho1*E and 2=(d-2)n+a. |
| P452 isolated critical point | A.5.17 | Same full Phi=u g^m, exact root and identity local-fibre inclusion; square−2 sphere excludes the point. |
| P452 analytic resolution comparison | Popescu-Pampu3.10/3.12 p20 | Local domination over singular N glues with the smooth-locus map, giving the proper holomorphic modification T1→T, then its point-blowup factorization. |
| P318 factorization | Popescu-Pampu3.12 p20 | Exactly rho:X→Z from P318. Only this citation sentence changes; full old/receiving canonical-intersection and elliptic-descent proofs were read. |

The quartic proof keeps the complete delta/Milnor estimate M<=5, Euler count4(7-M), monodromy lower bound3(7-M), gap21-4M, and all degree-one/two/four/higher exclusions. Equations4.52a/b retain their prepared exact labels at P322;4.52c/d remain at P452. No full-fibre multiplicity is altered.

## Primary source openings

Siersma, Topology30(3),445–469(1991): opened Sections1.2,3.4–3.6,5.3,6.2–6.5,7.1 at printed pp445,451–452,457–458,460–462; diagrams on452/462 also read as rendered images. The ordinary chain maps in j2(T-I)=VARII j remain valid in dimension two; only the separate isomorphism statements have their exceptional-degree qualifications. Download: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/siersma.pdf; SHA256 a1e17e14cc0052271b1d6f8a875aedbae34a08cf1b456046c888420a22904595. Existing bibliography retains the journal identity and DOI.

Hatcher, Algebraic Topology(2002): reopened Theorem2C.3 and its finite-complex/compact-manifold setup, printed p179, for the free-action Lefschetz conclusion. No new full-book or complete theorem-proof reading is claimed. PDF SHA256 bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618.

Popescu-Pampu, Winter Braids Lecture Notes3(2016), CourseIII,1–74: complete Propositions3.10/3.12 and the analytic surface setup at printed p20 opened. The source refers to proofs elsewhere, so this records statement/setup reading, not reading an unprinted proof or Laufer's book. URL https://www.numdam.org/item/10.5802/wbln.14.pdf; DOI10.5802/wbln.14; SHA256 3c2190b5fa1e2bf94e2605b41ac6c75dabb1d629139380e67c8bdfdaa811efbd.

## Admission and remaining work

Five exact guards cover A.5.3, P300, the complete quartic subsection, P318's single citation sentence and the bibliography insertion. Every old label/target multiplicity is preserved. P322 is used; P323/P324 remain available. Root owns integrated compilation/page reading, front matter and final whole-paper placement. P453/P454/R19/P456/P457/R20 remain the next assigned actual subsections; their complete current proofs have been read, and their receiving replacements are still being prepared.
'''
(OUT/(prefix+'_comparison.md')).write_text(comparison,newline='\n')
print(f'{len(rows)} defects; {len(events)} exposed events; {len(status)} actual-subsection rows; P322 used.')
